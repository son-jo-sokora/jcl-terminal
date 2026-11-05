"""docs/error-catalog.md を作る。

z/OS 3.2 の MVS System Messages Vol 8（IEFC・IEF）と JES2 Messages に載っている
メッセージを全件数え、tests/cases.js のテストと突き合わせて分類する。
マニュアルの文章は IBM の著作物なので、一覧にはメッセージ ID と出典ページだけを載せ、
文面や説明は写さない（テスト内容と対象外の理由は、このプロジェクトで書いたもの）。

使い方: 環境変数 ZOS_TEXT_DIR に、マニュアル PDF をテキスト化したファイル
（ieam800_v3r2.txt、hasa100_v3r2.txt。ページ区切りは "=== PAGE n ===" の行）のあるフォルダを指定して
  python -I tools/make_catalog.py
をリポジトリの一番上のフォルダで実行する。
"""
import os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
T = os.environ.get("ZOS_TEXT_DIR") or sys.exit("環境変数 ZOS_TEXT_DIR にマニュアルのテキストのフォルダを指定してください")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BOOKS = [  # (ファイル, ID の形, 書名)
    ("ieam800_v3r2.txt", r"IEFC\d{3}I|IEF\d{3}[IEWA]", "MVS System Messages Vol 8 (IEF-IGD)"),
    ("hasa100_v3r2.txt", r"\$HASP\d{3,4}", "JES2 Messages"),
]

def messages():
    """各メッセージの ID・書名・ページ。Explanation が続く見出しだけを数え、同じ ID は最初の1つ。"""
    seen, out = set(), []
    for fname, pat, book in BOOKS:
        L = open(os.path.join(T, fname), encoding="utf-8", errors="replace").read().split("\n")
        idre = re.compile(r"^(" + pat + r")(?:\s+.*)?$")
        page = None
        for n, ln in enumerate(L):
            s = ln.strip()
            pm = re.match(r"=== PAGE (\d+) ===", s)
            if pm:
                page = int(pm.group(1)); continue
            m = idre.match(s)
            if not m or m.group(1) in seen:
                continue
            if not any(x.strip().startswith("Explanation") for x in L[n + 1:n + 20]):  # 長い文面（IEF705I など）も拾う
                continue
            seen.add(m.group(1))
            out.append({"id": m.group(1), "book": book, "page": page})
    return out

M = messages()
src = open(os.path.join(ROOT, "tests", "cases.js"), encoding="utf-8").read()
html = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()

tested = {}
for m in re.finditer(r"\{id:'([^']+)',t:'([^']*)'(.*?)\},?\n", src):
    tested.setdefault(m.group(1), []).append((m.group(2), "low:true" in m.group(3)))
na = {}
na_block = src[src.index("const NA={"):src.index("};", src.index("const NA={"))]
for m in re.finditer(r"'([^']+)':\[([^\]]*)\]", na_block):
    for i in re.findall(r"'([^']+)'", m.group(2)):
        na[i] = m.group(1)
emitted = set(re.findall(r"(IEFC?\d{3}[IEWA]|\$HASP\d{3,4})\b", html))

K_T, K_NA, K_INFO, K_NO = "テスト済み", "対象外", "情報メッセージ", "JCL では起きない"
rows = {"IEFC": [], "IEF": [], "HASP": []}
never = {"IEFC": [], "IEF": [], "HASP": []}
count = {}
for o in M:
    i = o["id"]
    g = "IEFC" if i.startswith("IEFC") else "IEF" if i.startswith("IEF") else "HASP"
    if i in tested:
        k, cls = K_T, K_T
    elif i in na:
        k, cls = K_NA, "対象外: " + na[i]
    elif i in emitted:
        k, cls = K_INFO, "情報メッセージ（シミュレーターが出力）"
    else:
        k, cls = K_NO, None
    count[(g, k)] = count.get((g, k), 0) + 1
    if k == K_NO:
        never[g].append(i)
    else:
        rows[g].append((o, cls, tested.get(i, [])))

L = ["# JCL エラー一覧（z/OS 3.2 マニュアル照合）", "",
     "z/OS 3.2 の MVS System Messages Vol 8（IEFC・IEF）と JES2 Messages に載っているメッセージを全件数え、",
     "利用者の JCL で起きるものをテストにしました。テストは `tests/run.html` をブラウザで開くと実行できます。", "",
     "- **テスト済み**: `tests/cases.js` にテスト JCL があり、シミュレーターがマニュアルの文面で出すもの",
     "- **対象外**: JCL で起こりうるが、このシミュレーターにない機能や環境に依存するもの（理由を記載）",
     "- **情報メッセージ**: 正常時にシミュレーターが出すもの（IEF236I など）",
     "- **JCL では起きない**: 装置、オペレーター操作、システム障害などのメッセージ（ID だけを載せています）", "",
     "「確度:低」は、マニュアルから発生条件や文面を一つに決められなかったテストです。", "",
     "> [!NOTE]",
     "> メッセージの文面と説明は IBM のマニュアルの文章なので、この一覧には写していません。",
     "> 「出典」のページ（PDF のページ番号）で、マニュアルの本文を確認してください。",
     "> 文面はシミュレーターの画面でも確かめられます。「テスト内容」と「対象外」の理由は、このプロジェクトで書いたものです。", "",
     "この一覧は `tools/make_catalog.py` で作っています。", "",
     "## 件数", "", "| 種類 | テスト済み | 対象外 | 情報メッセージ | JCL では起きない | 合計 |", "|---|---|---|---|---|---|"]
NAMES = (("IEFC", "IEFC（JCL の解釈）"), ("IEF", "IEF（割り振り・実行）"), ("HASP", "JES2"))
for g, name in NAMES:
    c = [count.get((g, k), 0) for k in (K_T, K_NA, K_INFO, K_NO)]
    L.append(f"| {name} | {c[0]} | {c[1]} | {c[2]} | {c[3]} | {sum(c)} |")
ids = {o["id"] for o in M}
other = sorted(i for i in tested if i not in ids)
L += ["", f"このほか、SMS・実行時のメッセージ（{', '.join(other)}）もテストしています。", ""]
for g, name in NAMES:
    if g == "HASP":
        name = "JES2（JCL に関係するもの）"
    L += [f"## {name}", "", "| ID | 出典 | 分類 | テスト内容 |", "|---|---|---|---|"]
    for o, cls, ts in rows[g]:
        tt = "<br>".join(x + ("（確度:低）" if low else "") for x, low in ts)
        L.append(f"| {o['id']} | {o['book']} p.{o['page']} | {cls} | {tt} |")
    L.append("")
    if g != "HASP" and never[g]:
        L += [f"**JCL では起きないもの（{len(never[g])} 件）**: " + ", ".join(never[g]), ""]
L.append("JES2 のうち JCL では起きないもの（オペレーター操作・プリンター・NJE など）は、件数だけを数えています。")
open(os.path.join(ROOT, "docs", "error-catalog.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
print({f"{g}/{k}": v for (g, k), v in sorted(count.items())})
