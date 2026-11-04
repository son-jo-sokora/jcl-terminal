# JCL 練習端末

ブラウザだけで動く、z/OS 風の JCL 練習用シミュレータです。
ISPF に似た画面で JCL を書いて `SUB` で投入すると、JES2 のメッセージが返ってきます。ジョブの出力は SDSF に似た画面で確認できます。

### ▶ 今すぐ試す: https://son-jo-sokora.github.io/jcl-terminal/

上のリンクを開くだけで使えます。ダウンロードやインストールは要りません。

- **インストール不要**です。ファイルは `index.html` の1つだけで、ブラウザで開けば動きます。
- メインフレームの実機やアカウントは要りません。
- 書き間違えると、実機に近い JCL エラーメッセージ（`IEFC605I` など）が返ります。間違え方の練習にも使えます。

> [!IMPORTANT]
> これは本物の z/OS ではなく、学習用のシミュレーションです。メッセージの番号や文面は z/OS 3.2 のマニュアルと照合していますが、実機と異なる場合があります。`JCK` で始まるメッセージと、キーワードの重複を知らせる `IEFC633I`（末尾に `SIMULATOR MESSAGE` と表示）は、この練習端末独自のもので、実際の z/OS にはありません。業務や試験の正解として扱わず、実機の動作は IBM のマニュアルで確認してください。

```
 EDIT       USER01.JCL(HELLO) - 01.00                     Columns 00001 00072
Command ===> SUB                                              Scroll ===> CSR
****** ***************************** Top of Data ******************************
000100 //HELLO    JOB (ACCT),'USER01',CLASS=A,MSGCLASS=X,
000200 //             MSGLEVEL=(1,1),NOTIFY=&SYSUID
000300 //STEP1    EXEC PGM=IEBGENER
  ...

IKJ56250I JOB HELLO(JOB01234) SUBMITTED
***
17.18.43 JOB01234 $HASP165 HELLO    ENDED AT N1  MAXCC=0000 CN(INTERNAL)
***
```

---

## 目次

1. [自分の PC で試す](#1-自分の-pc-で試す)
2. [最初の5分](#2-最初の5分)
3. [キー操作](#3-キー操作)
4. [サンプル JCL](#4-サンプル-jcl)
5. [できること・できないこと](#5-できることできないこと)
6. [うまく動かないとき](#6-うまく動かないとき)
7. [改造してみる](#7-改造してみる)
8. [ライセンスと商標](#8-ライセンスと商標)

詳しい手順は [docs/tutorial.md](docs/tutorial.md)、プログラムの仕組みは [docs/how-it-works.md](docs/how-it-works.md) にあります。

---

## 1. 自分の PC で試す

必要なのは、新しめのブラウザ（Chrome、Edge、Firefox、Safari）だけです。

**とりあえず触ってみたいだけなら、[公開ページ](https://son-jo-sokora.github.io/jcl-terminal/) を開けば十分です。** 自分の PC に置いて使いたい人や、改造したい人は、次の3つの方法から選んでください。

### 方法 A: ZIP をダウンロードして開く（いちばん簡単）

Git を使ったことがない人向けです。

1. このページの上にある緑色の **「Code」** ボタンを押します。
2. **「Download ZIP」** を選びます。
3. ダウンロードした ZIP ファイルを展開（解凍）します。
   - Windows: ZIP を右クリック →「すべて展開」
   - Mac: ZIP をダブルクリック
4. 展開してできたフォルダの中の **`index.html` をダブルクリック**します。ブラウザで画面が開けば準備完了です。

> [!TIP]
> ダブルクリックで別のアプリ（メモ帳など）が開いてしまう場合は、`index.html` を右クリックして「プログラムから開く」→ ブラウザを選んでください。ブラウザの窓に `index.html` をドラッグ＆ドロップしても開けます。

### 方法 B: git clone する

Git を入れている人向けです。

1. このページの緑色の **「Code」** ボタンを押し、表示された URL（`https://github.com/...`）をコピーします。
2. ターミナル（Windows は PowerShell、Mac は「ターミナル」）で次を実行します。`<コピーしたURL>` はコピーした URL に置き換えてください。

   ```bash
   git clone <コピーしたURL>
   ```

3. できたフォルダの中の `index.html` をブラウザで開きます。

更新を取り込むときは、そのフォルダで `git pull` を実行します。

### 方法 C: GitHub Pages で自分専用の URL を作る

インストールせずにスマホや別の PC からも使いたい人向けです。GitHub アカウントが必要です。

1. このページ右上の **「Fork」** を押して、自分のアカウントにコピーします。
2. コピーしたリポジトリで **Settings → Pages** を開きます。
3. **「Build and deployment」** の Source で **「Deploy from a branch」** を選び、Branch で **`main`**、フォルダで **`/ (root)`** を選んで **Save** を押します。
4. 1〜2分待つと、同じ画面に `https://<あなたのユーザー名>.github.io/<リポジトリ名>/` という URL が表示されます。そこを開けば使えます。

### (任意) ローカルサーバーで開く

通常は不要です。ブラウザの設定で `file://` のページが制限されている場合だけ使ってください。Python が入っていれば、`index.html` のあるフォルダで次を実行します。

```bash
python -m http.server 8000
```

その後、ブラウザで `http://localhost:8000` を開きます。止めるときはターミナルで `Ctrl+C` を押します。

---

## 2. 最初の5分

開くと、`HELLO` という JCL の編集画面が表示されます。

1. 画面上部の **`Command ===>`** に `SUB` と入力して **Enter** を押します。
2. 次のようなメッセージが出ます。`$HASP165 ... MAXCC=0000` は「ジョブが正常に終わった」という意味です。

   ```
   IKJ56250I JOB HELLO(JOB01234) SUBMITTED
   17.18.43 JOB01234 $HASP165 HELLO    ENDED AT N1  MAXCC=0000 CN(INTERNAL)
   ```

3. **Enter** で編集画面に戻ります。
4. `Command ===>` に `=SD` と入力して Enter、続けて `ST` と入力して Enter を押します。ジョブの一覧（SDSF）が開きます。
5. `HELLO` の行の左端の入力欄に `?` と入力して Enter を押すと、出力の一覧（JESMSGLG、JESJCL、JESYSMSG、SYSUT2 など）が出ます。
6. 見たい行の左に `S` と入力して Enter を押すと、中身が表示されます。**F3**（または **Esc**）で前の画面に戻ります。

次は、わざと間違えてみましょう。右側のガイドから **SYNTAX** を開き、`Command ===>` に `JCK` と入力して Enter を押します。投入しなくても、どの行がどう間違っているかが表示されます。

もっと詳しい手順は [docs/tutorial.md](docs/tutorial.md) を見てください。

---

## 3. キー操作

| キー | 動作 |
|---|---|
| **Enter** | コマンドを実行する（編集エリアの中では改行） |
| **Ctrl+Enter** | 編集エリアの中からでもコマンドを実行する |
| **F3** または **Esc** | 前の画面に戻る（編集中なら保存して戻る） |
| **F7 / F8** または **PageUp / PageDown** | 上下にスクロールする |
| 画面下のボタン | タッチ操作用の Enter / F3 / F7 / F8 / F12 |

ブラウザによっては F3 が「ページ内検索」になります。その場合は **Esc** を使ってください。

よく使うコマンドは次のとおりです。

| どこで | コマンド | 意味 |
|---|---|---|
| どこでも | `=2` / `=3.4` / `=3.17` / `=SD` | 編集 / データセット一覧 / z/OS UNIX ファイル一覧 / SDSF |
| 編集画面 | `SUB` | ジョブを投入する |
| 編集画面 | `JCK` | 投入せずに JCL をチェックする |
| 編集画面 | `SAVE` / `CAN` / `CAPS ON` / `CAPS OFF` / `RESET` | 保存 / 保存せず戻る / 大文字変換の切り替え / エラー印の消去 |
| SDSF ST の行 | `?` / `S` / `A` / `C` / `P` | 出力一覧 / 表示 / 保留を解放 / 取り消し / 削除 |
| データセット一覧の行 | `E` / `B` / `D` | 編集 / 表示 / 削除 |

---

## 4. サンプル JCL

`USER01.JCL` に練習用のメンバーが入っています。画面右のガイドの「開く」ボタンからも開けます。

| 種類 | メンバー |
|---|---|
| 基本 | `HELLO`（IEBGENER）、`ALLOC`（データセット作成）、`SORT`（DFSORT）、`IFTEST`（IF/THEN/ELSE）、`CLEANUP`（IDCAMS） |
| エラー体験 | `BADJCL`、`SYNTAX`（よくある間違い12種類）、`ABEND`（S806）、`OPENERR`（S013-20）、`PROCERR` |
| プロシージャ | `PROCJOB`（カタログ式・オーバーライド・INCLUDE）、`INSTREAM`（インストリーム） |
| GDG | `GDGDEF`（最初に1回実行）、`GDGRUN`（4回実行すると古い世代が消える） |
| JES2・出力 | `JES2CTL`（/*JOBPARM など）、`OUTSTMT`（OUTPUT 文） |
| DD パラメーター | `DDPARMS`（LIKE・VOL・RETPD・DDNAME・PATH） |
| ジョブ制御 | `JOBRC`、`JOBCOND`、`RESTART`、`REGION`（S80A と IF ABENDCC）、`HOLDJOB`、`SCHED`、`EXPORT` |

---

## 5. できること・できないこと

**JCL の文**
JOB、EXEC、DD、SET、IF/THEN/ELSE/ENDIF、PROC/PEND、JCLLIB、INCLUDE、OUTPUT、EXPORT、SCHEDULE、JES2 制御文（`/*JOBPARM` `/*PRIORITY` `/*ROUTE` `/*MESSAGE` `/*NOTIFY` `/*XEQ`）

**JCL の機能**
COND（JOB と EXEC）、DISP、DD * / DATA / DUMMY / SYSOUT、記号（SET、プロシージャの記号パラメーター、`&SYSUID` などのシステム記号）、後方参照、プロシージャのオーバーライド、GDG、VOL、LIKE、DDNAME、RETPD/EXPDT、PATH（z/OS UNIX ファイル）、OUTLIM、JOBRC、RESTART、TYPRUN、REGION

**プログラム**
IEFBR14、IEBGENER、SORT（ICEMAN）、IDCAMS（DEFINE GDG、DELETE、LISTCAT、PRINT、REPRO、SET）。これ以外のプログラム名を指定すると、実機と同じく S806 で ABEND します。

**受け付けるが、書式チェックだけで動作には反映しないもの**
TIME、SPIN、FREE、CNTL/ENDCNTL、XMIT、SCHEDULE の AFTER/BEFORE、JOBGROUP。JES3 の制御文（`//*MAIN` など）は、JES2 システムと同じくコメントとして扱います。

**できないこと**
COBOL などのコンパイル、自分で作ったプログラムの実行、VSAM、TSO コマンド（IKJEFT01）、複数ユーザーでの共有、実機との接続。

**データの保存場所**
作ったデータセットやジョブは、**使っているブラウザの中（localStorage）だけ**に保存されます。サーバーには送られません。別のブラウザや別の PC とは共有されず、ブラウザの閲覧データを消すと消えます。最初の状態に戻したいときは、右側のガイドの一番下にある **「初期状態に戻す」** を2回押してください。

---

## 6. うまく動かないとき

**画面が真っ白で、何も表示されない**
- ブラウザを最新版にしてください。Internet Explorer では動きません。
- `index.html` をメモ帳などで開いていないか確認してください。ブラウザで開く必要があります。
- それでもだめなら、[1. の「ローカルサーバーで開く」](#任意-ローカルサーバーで開く) を試してください。

**フォントが端末らしく見えない**
フォントはインターネット経由（Google Fonts）で読み込みます。オフラインのときは PC にある等幅フォントで表示されますが、動作は変わりません。

**F3 を押すと検索窓が出る**
ブラウザの機能と重なっています。**Esc** か、画面下の **「F3 戻る」** ボタンを使ってください。

**入力した小文字が大文字になる**
ISPF の CAPS ON と同じ動作です。小文字を使いたいときは、`Command ===>` に `CAPS OFF` と入力します。JCL のキーワードは大文字で書く必要があるので、小文字にすると JCL エラーになります。

**前に作ったデータが残っていて、サンプルどおりにならない**
たとえば ALLOC を2回投入すると、2回目は「データセットがすでにある」というエラーになります。これは実機と同じ動作です。最初からやり直したいときは、ガイドの **「初期状態に戻す」** を2回押してください。

**スマホで文字が小さい**
画面は横80桁の端末を再現しているため、幅の狭い画面では小さくなります。横向きにするか、PC で使ってください。

---

## 7. 改造してみる

プログラムは `index.html` の1ファイルにまとまっています。テキストエディタ（VS Code など）で開いて書き換え、ブラウザを再読み込み（F5）すると反映されます。ビルドや npm は要りません。

- **サンプル JCL を追加する**: `const SAMPLES={` の中に、`名前:[ "1行目", "2行目", ... ]` の形で追加します。再読み込みすると、新しいサンプルが `USER01.JCL` に自動で追加されます。保存済みのデータは消えません。
- **プログラム（PGM=）を追加する**: `const PROGRAMS={` の中に関数を追加します。書き方は [docs/how-it-works.md](docs/how-it-works.md) を見てください。

---

## 8. ライセンスと商標

- このプログラムは [MIT ライセンス](LICENSE) で公開しています。
- IBM、z/OS、MVS、ISPF、SDSF、JES2、DFSORT は、International Business Machines Corporation の商標です。このプロジェクトは IBM とは関係がなく、IBM の承認も受けていません。
- IBM のソフトウェアや、マニュアルの文章は含まれていません。画面とメッセージは、学習用に一般的な見た目を再現したものです。
