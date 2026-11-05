# JCL エラー一覧（z/OS 3.2 マニュアル照合）

z/OS 3.2 の MVS System Messages Vol 8（IEFC・IEF）と JES2 Messages に載っているメッセージを全件数え、
利用者の JCL で起きるものをテストにしました。テストは `tests/run.html` をブラウザで開くと実行できます。

- **テスト済み**: `tests/cases.js` にテスト JCL があり、シミュレーターがマニュアルの文面で出すもの
- **対象外**: JCL で起こりうるが、このシミュレーターにない機能や環境に依存するもの（理由を記載）
- **情報メッセージ**: 正常時にシミュレーターが出すもの（IEF236I など）
- **JCL では起きない**: 装置、オペレーター操作、システム障害などのメッセージ（ID だけを載せています）

「確度:低」は、マニュアルから発生条件や文面を一つに決められなかったテストです。

> [!NOTE]
> メッセージの文面と説明は IBM のマニュアルの文章なので、この一覧には写していません。
> 「出典」のページ（PDF のページ番号）で、マニュアルの本文を確認してください。
> 文面はシミュレーターの画面でも確かめられます。「テスト内容」と「対象外」の理由は、このプロジェクトで書いたものです。

この一覧は `tools/make_catalog.py` で作っています。

## 件数

| 種類 | テスト済み | 対象外 | 情報メッセージ | JCL では起きない | 合計 |
|---|---|---|---|---|---|
| IEFC（JCL の解釈） | 73 | 27 | 2 | 0 | 102 |
| IEF（割り振り・実行） | 43 | 91 | 8 | 322 | 464 |
| JES2 | 9 | 18 | 11 | 948 | 986 |

このほか、SMS・実行時のメッセージ（CSV003I, IEC141I, IEW4000I, IGD105I, IGD17101I, IGD17272I）もテストしています。

## IEFC（JCL の解釈）

| ID | 出典 | 分類 | テスト内容 |
|---|---|---|---|
| IEFC001I | MVS System Messages Vol 8 (IEF-IGD) p.503 | テスト済み | インストリーム・プロシージャを呼ぶ（情報） |
| IEFC002I | MVS System Messages Vol 8 (IEF-IGD) p.503 | テスト済み | INCLUDE グループを展開（情報） |
| IEFC003I | MVS System Messages Vol 8 (IEF-IGD) p.504 | テスト済み | JCLLIB のライブラリが存在しない |
| IEFC004I | MVS System Messages Vol 8 (IEF-IGD) p.506 | 情報メッセージ（シミュレーターが出力） |  |
| IEFC005I | MVS System Messages Vol 8 (IEF-IGD) p.506 | テスト済み | IF に ENDIF がない<br>IF のない ENDIF<br>IF のない ELSE |
| IEFC006I | MVS System Messages Vol 8 (IEF-IGD) p.507 | テスト済み | キーワードの後ろに位置パラメーター |
| IEFC007I | MVS System Messages Vol 8 (IEF-IGD) p.507 | テスト済み | PROC 文の記号名が EXEC のキーワード（PARM） |
| IEFC008I | MVS System Messages Vol 8 (IEF-IGD) p.508 | テスト済み | カタログ・プロシージャの途中に PEND |
| IEFC009I | MVS System Messages Vol 8 (IEF-IGD) p.509 | テスト済み | PARM と PARMDD を同時に指定<br>DD で SYSOUT と DISP を同時に指定 |
| IEFC010I | MVS System Messages Vol 8 (IEF-IGD) p.509 | テスト済み | SET 文の記号名がない（確度:低） |
| IEFC011I | MVS System Messages Vol 8 (IEF-IGD) p.510 | テスト済み | INCLUDE の入れ子が15段を超える（自分自身を INCLUDE）<br>プロシージャの入れ子が15段を超える |
| IEFC012I | MVS System Messages Vol 8 (IEF-IGD) p.510 | 対象外: TIOT など、環境で決まる上限 |  |
| IEFC013I | MVS System Messages Vol 8 (IEF-IGD) p.511 | テスト済み | IF に使えないキーワード |
| IEFC014I | MVS System Messages Vol 8 (IEF-IGD) p.512 | テスト済み | IF の式が真偽にならない（RC だけ） |
| IEFC015I | MVS System Messages Vol 8 (IEF-IGD) p.512 | テスト済み | IF で RC とアベンドコードを比較 |
| IEFC016I | MVS System Messages Vol 8 (IEF-IGD) p.513 | テスト済み | IF の比較の右辺がない |
| IEFC017I | MVS System Messages Vol 8 (IEF-IGD) p.513 | テスト済み | INCLUDE のメンバーがない |
| IEFC018I | MVS System Messages Vol 8 (IEF-IGD) p.514 | テスト済み | インストリーム・プロシージャに PEND がない |
| IEFC019I | MVS System Messages Vol 8 (IEF-IGD) p.514 | テスト済み | 最初の EXEC より後ろに JCLLIB |
| IEFC020I | MVS System Messages Vol 8 (IEF-IGD) p.515 | テスト済み | JCLLIB が2つ |
| IEFC021I | MVS System Messages Vol 8 (IEF-IGD) p.516 | 対象外: マニュアルから発生条件を特定できない |  |
| IEFC022I | MVS System Messages Vol 8 (IEF-IGD) p.517 | テスト済み | プロシージャが継続の途中で終わる |
| IEFC023I | MVS System Messages Vol 8 (IEF-IGD) p.517 | 対象外: マニュアルから発生条件を特定できない |  |
| IEFC024I | MVS System Messages Vol 8 (IEF-IGD) p.518 | テスト済み | DD 文に知らない位置パラメーター（確度:低） |
| IEFC025I | MVS System Messages Vol 8 (IEF-IGD) p.519 | 対象外: システム出口（IEFUJV など） |  |
| IEFC026I | MVS System Messages Vol 8 (IEF-IGD) p.519 | 対象外: システム出口（IEFUJV など） |  |
| IEFC027I | MVS System Messages Vol 8 (IEF-IGD) p.520 | 対象外: システム出口（IEFUJV など） |  |
| IEFC028I | MVS System Messages Vol 8 (IEF-IGD) p.520 | 対象外: システム出口（IEFUJV など） |  |
| IEFC029I | MVS System Messages Vol 8 (IEF-IGD) p.521 | 対象外: システム出口（IEFUJV など） |  |
| IEFC030I | MVS System Messages Vol 8 (IEF-IGD) p.522 | テスト済み | PATH なしで PATHOPTS |
| IEFC031I | MVS System Messages Vol 8 (IEF-IGD) p.522 | テスト済み | OUTPUT 文に名前がない |
| IEFC032I | MVS System Messages Vol 8 (IEF-IGD) p.523 | テスト済み | EXEC の最初が PGM/PROC でない |
| IEFC033I | MVS System Messages Vol 8 (IEF-IGD) p.524 | テスト済み | IF の RC が 4095 を超える |
| IEFC034I | MVS System Messages Vol 8 (IEF-IGD) p.524 | テスト済み | JOBCAT DD を使う |
| IEFC035I | MVS System Messages Vol 8 (IEF-IGD) p.525 | テスト済み | VOL=SER に同じボリュームを2回 |
| IEFC037I | MVS System Messages Vol 8 (IEF-IGD) p.526 | 対象外: HSM による再呼び出し・データセットの競合 |  |
| IEFC038I | MVS System Messages Vol 8 (IEF-IGD) p.526 | 対象外: HSM による再呼び出し・データセットの競合 |  |
| IEFC039I | MVS System Messages Vol 8 (IEF-IGD) p.527 | 対象外: HSM による再呼び出し・データセットの競合 |  |
| IEFC040I | MVS System Messages Vol 8 (IEF-IGD) p.527 | 対象外: システム出口（IEFUJV など） |  |
| IEFC041I | MVS System Messages Vol 8 (IEF-IGD) p.528 | テスト済み | MSGLEVEL の値が範囲外（警告） |
| IEFC042I | MVS System Messages Vol 8 (IEF-IGD) p.528 | 対象外: システム出口（IEFUJV など） |  |
| IEFC043I | MVS System Messages Vol 8 (IEF-IGD) p.529 | 対象外: HSM による再呼び出し・データセットの競合 |  |
| IEFC044I | MVS System Messages Vol 8 (IEF-IGD) p.530 | 対象外: HSM による再呼び出し・データセットの競合 |  |
| IEFC165I | MVS System Messages Vol 8 (IEF-IGD) p.531 | テスト済み | COMMAND 文（情報） |
| IEFC417I | MVS System Messages Vol 8 (IEF-IGD) p.532 | 対象外: 入出力障害・システム内部エラー |  |
| IEFC452I | MVS System Messages Vol 8 (IEF-IGD) p.532 | テスト済み | JCL エラーでジョブが実行されない |
| IEFC601I | MVS System Messages Vol 8 (IEF-IGD) p.533 | 対象外: マニュアルから発生条件を特定できない |  |
| IEFC602I | MVS System Messages Vol 8 (IEF-IGD) p.534 | テスト済み | EXEC 文が255を超える |
| IEFC603I | MVS System Messages Vol 8 (IEF-IGD) p.535 | 対象外: 入出力障害・システム内部エラー |  |
| IEFC605I | MVS System Messages Vol 8 (IEF-IGD) p.535 | テスト済み | EXEC のつづり間違い |
| IEFC607I | MVS System Messages Vol 8 (IEF-IGD) p.536 | テスト済み | EXEC 文がない |
| IEFC609I | MVS System Messages Vol 8 (IEF-IGD) p.536 | テスト済み | PGM を EXEC で上書きしようとする（確度:低） |
| IEFC610I | MVS System Messages Vol 8 (IEF-IGD) p.537 | テスト済み | プロシージャに EXEC がない |
| IEFC611I | MVS System Messages Vol 8 (IEF-IGD) p.538 | テスト済み | 上書き先のステップがプロシージャにない |
| IEFC612I | MVS System Messages Vol 8 (IEF-IGD) p.539 | テスト済み | プロシージャが見つからない |
| IEFC614I | MVS System Messages Vol 8 (IEF-IGD) p.540 | 対象外: 入出力障害・システム内部エラー |  |
| IEFC616I | MVS System Messages Vol 8 (IEF-IGD) p.540 | テスト済み | サブリストの中にサブリスト |
| IEFC618I | MVS System Messages Vol 8 (IEF-IGD) p.541 | テスト済み | 閉じかっこの直後に文字が続く（確度:低） |
| IEFC620I | MVS System Messages Vol 8 (IEF-IGD) p.542 | テスト済み | JCL で使えない文字 |
| IEFC621I | MVS System Messages Vol 8 (IEF-IGD) p.543 | テスト済み | カンマで終わるのに継続行がない |
| IEFC622I | MVS System Messages Vol 8 (IEF-IGD) p.544 | テスト済み | かっこの対応が取れていない |
| IEFC624I | MVS System Messages Vol 8 (IEF-IGD) p.546 | テスト済み | データセット名にピリオドが連続 |
| IEFC625I | MVS System Messages Vol 8 (IEF-IGD) p.547 | テスト済み | DSN 全体をかっこで囲む |
| IEFC626I | MVS System Messages Vol 8 (IEF-IGD) p.548 | テスト済み | データセット名にプラス記号 |
| IEFC627I | MVS System Messages Vol 8 (IEF-IGD) p.549 | テスト済み | データセット名にアンパサンド |
| IEFC628I | MVS System Messages Vol 8 (IEF-IGD) p.551 | テスト済み | データセット名にアスタリスク |
| IEFC629I | MVS System Messages Vol 8 (IEF-IGD) p.552 | テスト済み | アポストロフィが閉じていない |
| IEFC630I | MVS System Messages Vol 8 (IEF-IGD) p.553 | テスト済み | 知らないキーワード |
| IEFC632I | MVS System Messages Vol 8 (IEF-IGD) p.555 | テスト済み | REGION の書式が違う |
| IEFC635I | MVS System Messages Vol 8 (IEF-IGD) p.555 | テスト済み | JOB 文にジョブ名がない |
| IEFC640I | MVS System Messages Vol 8 (IEF-IGD) p.556 | テスト済み | DISP の位置パラメーターが多すぎる |
| IEFC641I | MVS System Messages Vol 8 (IEF-IGD) p.557 | テスト済み | プログラマー名をかっこで囲む（確度:低） |
| IEFC642I | MVS System Messages Vol 8 (IEF-IGD) p.558 | テスト済み | プログラム名が9文字 |
| IEFC646I | MVS System Messages Vol 8 (IEF-IGD) p.560 | テスト済み | SPACE の単位がない |
| IEFC647I | MVS System Messages Vol 8 (IEF-IGD) p.561 | テスト済み | プログラム名が数字で始まる |
| IEFC650I | MVS System Messages Vol 8 (IEF-IGD) p.562 | テスト済み | データセット名にスラッシュ |
| IEFC651I | MVS System Messages Vol 8 (IEF-IGD) p.564 | テスト済み | プログラム名にハイフン |
| IEFC652I | MVS System Messages Vol 8 (IEF-IGD) p.565 | テスト済み | DD * でない文に DLM |
| IEFC653I | MVS System Messages Vol 8 (IEF-IGD) p.566 | テスト済み | 記号の置き換え（情報） |
| IEFC654I | MVS System Messages Vol 8 (IEF-IGD) p.566 | テスト済み | 記号で DD * を指定（確度:低） |
| IEFC657I | MVS System Messages Vol 8 (IEF-IGD) p.567 | テスト済み | 設定した記号を使っていない（情報） |
| IEFC658I | MVS System Messages Vol 8 (IEF-IGD) p.568 | テスト済み | プロシージャの途中に PROC 文 |
| IEFC659I | MVS System Messages Vol 8 (IEF-IGD) p.568 | テスト済み | DD * でない文に SYMBOLS= |
| IEFC660I | MVS System Messages Vol 8 (IEF-IGD) p.569 | テスト済み | チェックポイント再開に SYSCHK DD がない |
| IEFC662I | MVS System Messages Vol 8 (IEF-IGD) p.570 | テスト済み | ステップ名が9文字 |
| IEFC663I | MVS System Messages Vol 8 (IEF-IGD) p.570 | テスト済み | インストリーム PROC 文に名前がない |
| IEFC665I | MVS System Messages Vol 8 (IEF-IGD) p.571 | テスト済み | インストリーム・プロシージャが15を超える（確度:低） |
| IEFC668I | MVS System Messages Vol 8 (IEF-IGD) p.571 | テスト済み | PROC のない PEND |
| IEFC677I | MVS System Messages Vol 8 (IEF-IGD) p.572 | 情報メッセージ（シミュレーターが出力） |  |
| IEFC678I | MVS System Messages Vol 8 (IEF-IGD) p.573 | 対象外: 入出力障害・システム内部エラー |  |
| IEFC679I | MVS System Messages Vol 8 (IEF-IGD) p.574 | 対象外: 入出力障害・システム内部エラー |  |
| IEFC680I | MVS System Messages Vol 8 (IEF-IGD) p.574 | 対象外: 入出力障害・システム内部エラー |  |
| IEFC683I | MVS System Messages Vol 8 (IEF-IGD) p.575 | 対象外: 入出力障害・システム内部エラー |  |
| IEFC690I | MVS System Messages Vol 8 (IEF-IGD) p.576 | テスト済み | SCHENV が WLM に定義されていない |
| IEFC691I | MVS System Messages Vol 8 (IEF-IGD) p.576 | テスト済み | SCHENV が16文字を超える |
| IEFC744I | MVS System Messages Vol 8 (IEF-IGD) p.577 | テスト済み | SUBSYS にサブシステム名がない（確度:低） |
| IEFC745I | MVS System Messages Vol 8 (IEF-IGD) p.577 | 対象外: サブシステムの状態に依存 |  |
| IEFC746I | MVS System Messages Vol 8 (IEF-IGD) p.578 | テスト済み | 存在しないサブシステム |
| IEFC747I | MVS System Messages Vol 8 (IEF-IGD) p.579 | 対象外: サブシステムの状態に依存 |  |
| IEFC748I | MVS System Messages Vol 8 (IEF-IGD) p.580 | テスト済み | サブシステム名が4文字を超える |
| IEFC750I | MVS System Messages Vol 8 (IEF-IGD) p.580 | 対象外: サブシステムの状態に依存 |  |
| IEFC822I | MVS System Messages Vol 8 (IEF-IGD) p.581 | 対象外: マニュアルから発生条件を特定できない |  |

## IEF（割り振り・実行）

| ID | 出典 | 分類 | テスト内容 |
|---|---|---|---|
| IEF032I | MVS System Messages Vol 8 (IEF-IGD) p.62 | 情報メッセージ（シミュレーターが出力） |  |
| IEF033I | MVS System Messages Vol 8 (IEF-IGD) p.63 | 情報メッセージ（シミュレーターが出力） |  |
| IEF042I | MVS System Messages Vol 8 (IEF-IGD) p.64 | 対象外: システム出口（IEFUJV など） |  |
| IEF083I | MVS System Messages Vol 8 (IEF-IGD) p.67 | 対象外: マニュアルから発生条件を特定できない |  |
| IEF085I | MVS System Messages Vol 8 (IEF-IGD) p.68 | 対象外: 性能・資源の指定（WLM ゴールモードで無視） |  |
| IEF092I | MVS System Messages Vol 8 (IEF-IGD) p.73 | 対象外: 性能・資源の指定（WLM ゴールモードで無視） |  |
| IEF099I | MVS System Messages Vol 8 (IEF-IGD) p.77 | 対象外: HSM による再呼び出し・データセットの競合 |  |
| IEF127I | MVS System Messages Vol 8 (IEF-IGD) p.100 | テスト済み | パラメーターのない DD 文 |
| IEF128I | MVS System Messages Vol 8 (IEF-IGD) p.101 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF129I | MVS System Messages Vol 8 (IEF-IGD) p.102 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF130I | MVS System Messages Vol 8 (IEF-IGD) p.102 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF131I | MVS System Messages Vol 8 (IEF-IGD) p.103 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF132I | MVS System Messages Vol 8 (IEF-IGD) p.104 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF133I | MVS System Messages Vol 8 (IEF-IGD) p.105 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF134I | MVS System Messages Vol 8 (IEF-IGD) p.106 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF135I | MVS System Messages Vol 8 (IEF-IGD) p.107 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF136I | MVS System Messages Vol 8 (IEF-IGD) p.108 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF141I | MVS System Messages Vol 8 (IEF-IGD) p.110 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF142I | MVS System Messages Vol 8 (IEF-IGD) p.111 | テスト済み | ステップが正常に実行（情報）<br>PARMDD で PARM を渡す（正常） |
| IEF143I | MVS System Messages Vol 8 (IEF-IGD) p.112 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF174I | MVS System Messages Vol 8 (IEF-IGD) p.127 | 対象外: 入出力障害・システム内部エラー |  |
| IEF187I | MVS System Messages Vol 8 (IEF-IGD) p.132 | 対象外: 入出力障害・システム内部エラー |  |
| IEF197I | MVS System Messages Vol 8 (IEF-IGD) p.138 | 対象外: 入出力障害・システム内部エラー |  |
| IEF201I | MVS System Messages Vol 8 (IEF-IGD) p.141 | テスト済み | JOB の COND が成立してジョブ打ち切り |
| IEF202I | MVS System Messages Vol 8 (IEF-IGD) p.142 | テスト済み | EXEC の COND が成立してステップを飛ばす<br>COND=ONLY で前のステップが正常 |
| IEF206I | MVS System Messages Vol 8 (IEF-IGD) p.143 | テスト済み | IF が偽でステップを飛ばす |
| IEF210I | MVS System Messages Vol 8 (IEF-IGD) p.144 | テスト済み | 存在しない UNIT 名 |
| IEF212I | MVS System Messages Vol 8 (IEF-IGD) p.146 | テスト済み | 存在しないデータセットを DISP=SHR |
| IEF219I | MVS System Messages Vol 8 (IEF-IGD) p.151 | テスト済み | GDG 名が35文字を超える |
| IEF221I | MVS System Messages Vol 8 (IEF-IGD) p.153 | テスト済み | PGM=*.ステップ.DD で参照先ステップが実行されていない |
| IEF236I | MVS System Messages Vol 8 (IEF-IGD) p.163 | 情報メッセージ（シミュレーターが出力） |  |
| IEF237I | MVS System Messages Vol 8 (IEF-IGD) p.164 | 情報メッセージ（シミュレーターが出力） |  |
| IEF240I | MVS System Messages Vol 8 (IEF-IGD) p.167 | 対象外: TIOT など、環境で決まる上限 |  |
| IEF245I | MVS System Messages Vol 8 (IEF-IGD) p.170 | テスト済み | テープ装置に DASD のボリュームを指定 |
| IEF253I | MVS System Messages Vol 8 (IEF-IGD) p.173 | 対象外: SMS 管理のためほかのメッセージになる（IGD17101I など） |  |
| IEF257I | MVS System Messages Vol 8 (IEF-IGD) p.175 | 対象外: SMS 管理のためほかのメッセージになる（IGD17101I など） |  |
| IEF258I | MVS System Messages Vol 8 (IEF-IGD) p.176 | テスト済み | SPACE の平均レコード長がトラック容量を超える |
| IEF260I | MVS System Messages Vol 8 (IEF-IGD) p.178 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF261I | MVS System Messages Vol 8 (IEF-IGD) p.179 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF262I | MVS System Messages Vol 8 (IEF-IGD) p.179 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF263I | MVS System Messages Vol 8 (IEF-IGD) p.180 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF264I | MVS System Messages Vol 8 (IEF-IGD) p.181 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF267I | MVS System Messages Vol 8 (IEF-IGD) p.183 | テスト済み | ディレクトリー・ブロックが1次量より多い |
| IEF272I | MVS System Messages Vol 8 (IEF-IGD) p.184 | テスト済み | 割り振りエラーでステップが実行されない |
| IEF283I | MVS System Messages Vol 8 (IEF-IGD) p.192 | 情報メッセージ（シミュレーターが出力） |  |
| IEF285I | MVS System Messages Vol 8 (IEF-IGD) p.196 | テスト済み | SYSOUT データセットの後処理（情報） |
| IEF286I | MVS System Messages Vol 8 (IEF-IGD) p.198 | テスト済み | GDG の世代 (0) がまだない（確度:低） |
| IEF295I | MVS System Messages Vol 8 (IEF-IGD) p.205 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF318I | MVS System Messages Vol 8 (IEF-IGD) p.211 | テスト済み | 新規 DASD データセットに UNIT=AFF |
| IEF365I | MVS System Messages Vol 8 (IEF-IGD) p.238 | テスト済み | VOL=REF に GDG のベース名 |
| IEF366I | MVS System Messages Vol 8 (IEF-IGD) p.239 | テスト済み | GDG の相対世代番号が 255 を超える |
| IEF372I | MVS System Messages Vol 8 (IEF-IGD) p.243 | テスト済み | VOL=REF が実行されなかったステップの DD を参照 |
| IEF373I | MVS System Messages Vol 8 (IEF-IGD) p.244 | テスト済み | ステップ開始時刻（情報） |
| IEF375I | MVS System Messages Vol 8 (IEF-IGD) p.246 | 情報メッセージ（シミュレーターが出力） |  |
| IEF377I | MVS System Messages Vol 8 (IEF-IGD) p.247 | 対象外: SMS 管理のためほかのメッセージになる（IGD17101I など） |  |
| IEF403I | MVS System Messages Vol 8 (IEF-IGD) p.259 | テスト済み | ジョブ開始・終了（情報） |
| IEF404I | MVS System Messages Vol 8 (IEF-IGD) p.259 | 情報メッセージ（シミュレーターが出力） |  |
| IEF430I | MVS System Messages Vol 8 (IEF-IGD) p.265 | 情報メッセージ（シミュレーターが出力） |  |
| IEF450I | MVS System Messages Vol 8 (IEF-IGD) p.270 | テスト済み | 存在しないプログラムで S806 |
| IEF452I | MVS System Messages Vol 8 (IEF-IGD) p.272 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF453I | MVS System Messages Vol 8 (IEF-IGD) p.273 | テスト済み | 割り振り時の JCL エラー |
| IEF491I | MVS System Messages Vol 8 (IEF-IGD) p.299 | 対象外: TIOT など、環境で決まる上限 |  |
| IEF602I | MVS System Messages Vol 8 (IEF-IGD) p.310 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF604I | MVS System Messages Vol 8 (IEF-IGD) p.311 | テスト済み | EXPDT の日数が 000 |
| IEF606I | MVS System Messages Vol 8 (IEF-IGD) p.311 | テスト済み | 最初の EXEC より前に JOBLIB 以外の DD |
| IEF617I | MVS System Messages Vol 8 (IEF-IGD) p.312 | テスト済み | EXEC 直後の DD に名前がない |
| IEF619I | MVS System Messages Vol 8 (IEF-IGD) p.313 | テスト済み | SYSOUT の書き出しプログラムと DEST のユーザーを同時に指定 |
| IEF623I | MVS System Messages Vol 8 (IEF-IGD) p.313 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF624I | MVS System Messages Vol 8 (IEF-IGD) p.315 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF625I | MVS System Messages Vol 8 (IEF-IGD) p.316 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF631I | MVS System Messages Vol 8 (IEF-IGD) p.316 | テスト済み | 未解決の DDNAME= が6つ |
| IEF632I | MVS System Messages Vol 8 (IEF-IGD) p.317 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF633I | MVS System Messages Vol 8 (IEF-IGD) p.318 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF634I | MVS System Messages Vol 8 (IEF-IGD) p.320 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF635I | MVS System Messages Vol 8 (IEF-IGD) p.321 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF636I | MVS System Messages Vol 8 (IEF-IGD) p.323 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF637I | MVS System Messages Vol 8 (IEF-IGD) p.323 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF638I | MVS System Messages Vol 8 (IEF-IGD) p.325 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF639I | MVS System Messages Vol 8 (IEF-IGD) p.326 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF640I | MVS System Messages Vol 8 (IEF-IGD) p.327 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF641I | MVS System Messages Vol 8 (IEF-IGD) p.329 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF642I | MVS System Messages Vol 8 (IEF-IGD) p.330 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF643I | MVS System Messages Vol 8 (IEF-IGD) p.331 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF644I | MVS System Messages Vol 8 (IEF-IGD) p.333 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF645I | MVS System Messages Vol 8 (IEF-IGD) p.334 | テスト済み | OUTPUT= が存在しない OUTPUT 文を参照<br>DSN=*.ステップ.DD が存在しないステップを参照（確度:低） |
| IEF646I | MVS System Messages Vol 8 (IEF-IGD) p.336 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF647I | MVS System Messages Vol 8 (IEF-IGD) p.337 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF648I | MVS System Messages Vol 8 (IEF-IGD) p.339 | テスト済み | 一時データセットに DISP=KEEP（PASS に置き換え） |
| IEF649I | MVS System Messages Vol 8 (IEF-IGD) p.340 | 対象外: TIOT など、環境で決まる上限 |  |
| IEF650I | MVS System Messages Vol 8 (IEF-IGD) p.340 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF653I | MVS System Messages Vol 8 (IEF-IGD) p.341 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF654I | MVS System Messages Vol 8 (IEF-IGD) p.341 | テスト済み | 2つの DD が同じ名前を DDNAME= で参照 |
| IEF655I | MVS System Messages Vol 8 (IEF-IGD) p.342 | 対象外: マニュアルから発生条件を特定できない |  |
| IEF661I | MVS System Messages Vol 8 (IEF-IGD) p.343 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF670I | MVS System Messages Vol 8 (IEF-IGD) p.345 | 対象外: マニュアルから発生条件を特定できない |  |
| IEF673I | MVS System Messages Vol 8 (IEF-IGD) p.347 | 対象外: 権限・TSO 固有 |  |
| IEF674I | MVS System Messages Vol 8 (IEF-IGD) p.348 | テスト済み | DYNAMNBR が数字でない（警告）（確度:低） |
| IEF675I | MVS System Messages Vol 8 (IEF-IGD) p.348 | 対象外: 性能・資源の指定（WLM ゴールモードで無視） |  |
| IEF677I | MVS System Messages Vol 8 (IEF-IGD) p.349 | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF679I | MVS System Messages Vol 8 (IEF-IGD) p.350 | 対象外: 入出力障害・システム内部エラー |  |
| IEF680I | MVS System Messages Vol 8 (IEF-IGD) p.350 | 対象外: 入出力障害・システム内部エラー |  |
| IEF681I | MVS System Messages Vol 8 (IEF-IGD) p.351 | テスト済み | COPIES が255を超える（警告）（確度:低） |
| IEF682I | MVS System Messages Vol 8 (IEF-IGD) p.352 | テスト済み | FREE が CLOSE/END 以外（警告）（確度:低） |
| IEF683I | MVS System Messages Vol 8 (IEF-IGD) p.352 | 対象外: 入出力障害・システム内部エラー |  |
| IEF684I | MVS System Messages Vol 8 (IEF-IGD) p.353 | テスト済み | HOLD が YES/NO 以外（警告）（確度:低） |
| IEF686I | MVS System Messages Vol 8 (IEF-IGD) p.355 | テスト済み | DDNAME= の参照先がステップにない（警告） |
| IEF687I | MVS System Messages Vol 8 (IEF-IGD) p.355 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF689I | MVS System Messages Vol 8 (IEF-IGD) p.357 | テスト済み | PARMDD の DD がない（確度:低） |
| IEF691I | MVS System Messages Vol 8 (IEF-IGD) p.358 | 対象外: 権限・TSO 固有 |  |
| IEF692I | MVS System Messages Vol 8 (IEF-IGD) p.359 | テスト済み | VOL=REF で z/OS UNIX ファイルの DD を参照 |
| IEF694I | MVS System Messages Vol 8 (IEF-IGD) p.360 | テスト済み | DDNAME= で連結 DD を参照（警告） |
| IEF702I | MVS System Messages Vol 8 (IEF-IGD) p.363 | テスト済み | マウントされていないボリューム |
| IEF707I | MVS System Messages Vol 8 (IEF-IGD) p.369 | 対象外: 入出力障害・システム内部エラー |  |
| IEF713I | MVS System Messages Vol 8 (IEF-IGD) p.370 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF714I | MVS System Messages Vol 8 (IEF-IGD) p.370 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF715I | MVS System Messages Vol 8 (IEF-IGD) p.371 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF716I | MVS System Messages Vol 8 (IEF-IGD) p.372 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF717I | MVS System Messages Vol 8 (IEF-IGD) p.373 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF718I | MVS System Messages Vol 8 (IEF-IGD) p.373 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF720I | MVS System Messages Vol 8 (IEF-IGD) p.375 | 対象外: 権限・TSO 固有 |  |
| IEF725I | MVS System Messages Vol 8 (IEF-IGD) p.379 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF726I | MVS System Messages Vol 8 (IEF-IGD) p.380 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF740I | MVS System Messages Vol 8 (IEF-IGD) p.390 | 対象外: 権限・TSO 固有 |  |
| IEF751I | MVS System Messages Vol 8 (IEF-IGD) p.394 | 対象外: サブシステムの状態に依存 |  |
| IEF752I | MVS System Messages Vol 8 (IEF-IGD) p.394 | 対象外: サブシステムの状態に依存 |  |
| IEF753I | MVS System Messages Vol 8 (IEF-IGD) p.395 | 対象外: サブシステムの状態に依存 |  |
| IEF754I | MVS System Messages Vol 8 (IEF-IGD) p.396 | 対象外: サブシステムの状態に依存 |  |
| IEF755I | MVS System Messages Vol 8 (IEF-IGD) p.397 | 対象外: サブシステムの状態に依存 |  |
| IEF756I | MVS System Messages Vol 8 (IEF-IGD) p.398 | 対象外: サブシステムの状態に依存 |  |
| IEF812I | MVS System Messages Vol 8 (IEF-IGD) p.423 | 対象外: 入出力障害・システム内部エラー |  |
| IEF815I | MVS System Messages Vol 8 (IEF-IGD) p.424 | 対象外: マニュアルから発生条件を特定できない |  |
| IEF817I | MVS System Messages Vol 8 (IEF-IGD) p.424 | 対象外: マニュアルから発生条件を特定できない |  |
| IEF818E | MVS System Messages Vol 8 (IEF-IGD) p.425 | 対象外: 入出力障害・システム内部エラー |  |
| IEF819I | MVS System Messages Vol 8 (IEF-IGD) p.426 | 対象外: マニュアルから発生条件を特定できない |  |
| IEF820I | MVS System Messages Vol 8 (IEF-IGD) p.427 | 対象外: マニュアルから発生条件を特定できない |  |
| IEF823I | MVS System Messages Vol 8 (IEF-IGD) p.428 | 対象外: マニュアルから発生条件を特定できない |  |
| IEF824I | MVS System Messages Vol 8 (IEF-IGD) p.428 | テスト済み | データセット名の修飾子が9文字（確度:低） |
| IEF825I | MVS System Messages Vol 8 (IEF-IGD) p.429 | テスト済み | データセット名の修飾子が数字で始まる（確度:低） |
| IEF861I | MVS System Messages Vol 8 (IEF-IGD) p.430 | 対象外: HSM による再呼び出し・データセットの競合 |  |
| IEF864I | MVS System Messages Vol 8 (IEF-IGD) p.432 | 対象外: HSM による再呼び出し・データセットの競合 |  |
| IEF910I | MVS System Messages Vol 8 (IEF-IGD) p.450 | テスト済み | PARMDD がメンバーなしの PDS |
| IEF911I | MVS System Messages Vol 8 (IEF-IGD) p.451 | 対象外: マニュアルから発生条件を特定できない |  |

**JCL では起きないもの（322 件）**: IEF001I, IEF002W, IEF003I, IEF004I, IEF005I, IEF006I, IEF007I, IEF008I, IEF009I, IEF010I, IEF011I, IEF013I, IEF014I, IEF016I, IEF017I, IEF018I, IEF019I, IEF020I, IEF021I, IEF022I, IEF023I, IEF024I, IEF030I, IEF031I, IEF044I, IEF086I, IEF087I, IEF089I, IEF090E, IEF091I, IEF093I, IEF094A, IEF097I, IEF098I, IEF100I, IEF101I, IEF102I, IEF103I, IEF104I, IEF105I, IEF106I, IEF107I, IEF108I, IEF109I, IEF110I, IEF111I, IEF112I, IEF113I, IEF114I, IEF115I, IEF116I, IEF118I, IEF119I, IEF120I, IEF121I, IEF121A, IEF122I, IEF123I, IEF124I, IEF125I, IEF126I, IEF140I, IEF145I, IEF147I, IEF148I, IEF150I, IEF151I, IEF152I, IEF153I, IEF154I, IEF155I, IEF156I, IEF157E, IEF167I, IEF168I, IEF169I, IEF170I, IEF172E, IEF173I, IEF175I, IEF176I, IEF177I, IEF179I, IEF180I, IEF186I, IEF188I, IEF191I, IEF192I, IEF193I, IEF194I, IEF195I, IEF196I, IEF198I, IEF199I, IEF209I, IEF211I, IEF213I, IEF214I, IEF217I, IEF218I, IEF220I, IEF222I, IEF223I, IEF229I, IEF230I, IEF233A, IEF234E, IEF242I, IEF244I, IEF246I, IEF251I, IEF254I, IEF256I, IEF259I, IEF266I, IEF273I, IEF274I, IEF275I, IEF278I, IEF280I, IEF281I, IEF284I, IEF287I, IEF288I, IEF289E, IEF291I, IEF292I, IEF293I, IEF294I, IEF300I, IEF301I, IEF302A, IEF303I, IEF307I, IEF311I, IEF314I, IEF316I, IEF321I, IEF322I, IEF323I, IEF324I, IEF325I, IEF326I, IEF327I, IEF328I, IEF329I, IEF330I, IEF331I, IEF333I, IEF336I, IEF337I, IEF341I, IEF343I, IEF344I, IEF345I, IEF347I, IEF348I, IEF350I, IEF351I, IEF352I, IEF353A, IEF354I, IEF355A, IEF356I, IEF357I, IEF358I, IEF359I, IEF360I, IEF361I, IEF362I, IEF363I, IEF364I, IEF367I, IEF368I, IEF371I, IEF374I, IEF376I, IEF378I, IEF379I, IEF380I, IEF381I, IEF382A, IEF383A, IEF384I, IEF387I, IEF388A, IEF391I, IEF396I, IEF402I, IEF405I, IEF406I, IEF414I, IEF415I, IEF420I, IEF428I, IEF429I, IEF431E, IEF438I, IEF447I, IEF448I, IEF449I, IEF451I, IEF456I, IEF462I, IEF463I, IEF464I, IEF465I, IEF466I, IEF467I, IEF468I, IEF469I, IEF470I, IEF471E, IEF472I, IEF473I, IEF474I, IEF475I, IEF476I, IEF477I, IEF478I, IEF479I, IEF480I, IEF481I, IEF482I, IEF483I, IEF484I, IEF485I, IEF488I, IEF490I, IEF492I, IEF493I, IEF500I, IEF502I, IEF503I, IEF506I, IEF510I, IEF524I, IEF525E, IEF550I, IEF572I, IEF656I, IEF667E, IEF669I, IEF671I, IEF672I, IEF685I, IEF688I, IEF690I, IEF695I, IEF696I, IEF700I, IEF701I, IEF703I, IEF704I, IEF705I, IEF706I, IEF719I, IEF721I, IEF722I, IEF723E, IEF724I, IEF729I, IEF730I, IEF731I, IEF732I, IEF734I, IEF735I, IEF736A, IEF737I, IEF738I, IEF741I, IEF742I, IEF743I, IEF757I, IEF758I, IEF759I, IEF760I, IEF761I, IEF764I, IEF765I, IEF766I, IEF767I, IEF768I, IEF769I, IEF770I, IEF771I, IEF772I, IEF773I, IEF775I, IEF776I, IEF777I, IEF778I, IEF779I, IEF781I, IEF783I, IEF786I, IEF787I, IEF788I, IEF789I, IEF790I, IEF791I, IEF811I, IEF863I, IEF874I, IEF875I, IEF876I, IEF877E, IEF878I, IEF879I, IEF880I, IEF881I, IEF882E, IEF883E, IEF893I, IEF894I, IEF895I, IEF896I, IEF897I, IEF898I, IEF900I, IEF901I, IEF990I

## JES2（JCL に関係するもの）

| ID | 出典 | 分類 | テスト内容 |
|---|---|---|---|
| $HASP003 | JES2 Messages p.30 | 情報メッセージ（シミュレーターが出力） |  |
| $HASP100 | JES2 Messages p.125 | 情報メッセージ（シミュレーターが出力） |  |
| $HASP107 | JES2 Messages p.130 | テスト済み | DLM の値が2文字でない（確度:低） |
| $HASP108 | JES2 Messages p.131 | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
| $HASP109 | JES2 Messages p.132 | 対象外: システム出口（IEFUJV など） |  |
| $HASP110 | JES2 Messages p.132 | テスト済み | JOB 文に SYSTEM と SYSAFF の両方 |
| $HASP111 | JES2 Messages p.136 | テスト済み | /*ROUTE に PRINT/PUNCH/XEQ がない<br>/*ROUTE の宛先が無効 |
| $HASP112 | JES2 Messages p.137 | テスト済み | /*JOBPARM の値が無効<br>/*JOBPARM に知らない位置パラメーター |
| $HASP113 | JES2 Messages p.139 | テスト済み | /*OUTPUT の COPIES が大きすぎる |
| $HASP114 | JES2 Messages p.140 | テスト済み | /*XEQ のノードが存在しない |
| $HASP116 | JES2 Messages p.142 | テスト済み | /*NOTIFY のユーザー ID が8文字を超える（確度:低） |
| $HASP118 | JES2 Messages p.143 | テスト済み | 知らない JES2 制御文 |
| $HASP139 | JES2 Messages p.158 | 対象外: システム出口（IEFUJV など） |  |
| $HASP146 | JES2 Messages p.162 | 対象外: マニュアルから発生条件を特定できない |  |
| $HASP165 | JES2 Messages p.173 | 情報メッセージ（シミュレーターが出力） |  |
| $HASP250 | JES2 Messages p.227 | 情報メッセージ（シミュレーターが出力） |  |
| $HASP373 | JES2 Messages p.307 | テスト済み | 正常終了（情報） |
| $HASP375 | JES2 Messages p.308 | 情報メッセージ（シミュレーターが出力） |  |
| $HASP395 | JES2 Messages p.310 | 情報メッセージ（シミュレーターが出力） |  |
| $HASP396 | JES2 Messages p.311 | 情報メッセージ（シミュレーターが出力） |  |
| $HASP646 | JES2 Messages p.484 | 情報メッセージ（シミュレーターが出力） |  |
| $HASP890 | JES2 Messages p.632 | 情報メッセージ（シミュレーターが出力） |  |
| $HASP892 | JES2 Messages p.646 | 情報メッセージ（シミュレーターが出力） |  |
| $HASP893 | JES2 Messages p.647 | 情報メッセージ（シミュレーターが出力） |  |
| $HASP1110 | JES2 Messages p.659 | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
| $HASP1111 | JES2 Messages p.664 | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
| $HASP1112 | JES2 Messages p.666 | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
| $HASP1114 | JES2 Messages p.669 | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
| $HASP1115 | JES2 Messages p.671 | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
| $HASP1116 | JES2 Messages p.672 | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
| $HASP1117 | JES2 Messages p.673 | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
| $HASP1118 | JES2 Messages p.674 | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
| $HASP1120 | JES2 Messages p.675 | 対象外: マニュアルから発生条件を特定できない |  |
| $HASP1132 | JES2 Messages p.679 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| $HASP1133 | JES2 Messages p.680 | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| $HASP6175 | JES2 Messages p.843 | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
| $HASP6176 | JES2 Messages p.844 | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
| $HASP6177 | JES2 Messages p.844 | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |

JES2 のうち JCL では起きないもの（オペレーター操作・プリンター・NJE など）は、件数だけを数えています。
