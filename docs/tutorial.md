# チュートリアル

JCL を初めて書く人向けに、JCL 練習端末の使い方を順番に説明します。各レッスンは5〜10分で終わります。

まだ画面を開いていない人は、先に [README の「自分の PC で試す」](../README.md#1-自分の-pc-で試す) を見てください。

> [!NOTE]
> 時刻やジョブ番号（`JOB01234` など）は実行するたびに変わります。この文書の出力例と数字が違っていても問題ありません。

---

## 目次

- [レッスン 1: ジョブを投入して結果を見る](#レッスン-1-ジョブを投入して結果を見る)
- [レッスン 2: 出力の3つの部品を読む](#レッスン-2-出力の3つの部品を読む)
- [レッスン 3: データセットを作る](#レッスン-3-データセットを作る)
- [レッスン 4: JCL エラーを直す](#レッスン-4-jcl-エラーを直す)
- [レッスン 5: ABEND を読む](#レッスン-5-abend-を読む)
- [レッスン 6: 自分で JCL を書く](#レッスン-6-自分で-jcl-を書く)
- [レッスン 7: プロシージャを使う](#レッスン-7-プロシージャを使う)
- [レッスン 8: GDG で世代管理をする](#レッスン-8-gdg-で世代管理をする)
- [練習問題](#練習問題)

---

## レッスン 1: ジョブを投入して結果を見る

**目標:** JCL を投入し、正常に終わったことを確認する。

1. 画面を開くと、`HELLO` メンバーの編集画面が表示されます。

   ```
   000100 //HELLO    JOB (ACCT),'USER01',CLASS=A,MSGCLASS=X,
   000200 //             MSGLEVEL=(1,1),NOTIFY=&SYSUID
   ...
   000600 //STEP1    EXEC PGM=IEBGENER
   000700 //SYSPRINT DD SYSOUT=*
   000800 //SYSIN    DD DUMMY
   000900 //SYSUT2   DD SYSOUT=*
   001000 //SYSUT1   DD *
   001100 HELLO, Z/OS!
   ```

   この JCL は「`SYSUT1` に書いた2行を、`IEBGENER` というプログラムで `SYSUT2`（ジョブの出力）にコピーする」という意味です。

2. `Command ===>` に `SUB` と入力して **Enter** を押します。

   ```
   IKJ56250I JOB HELLO(JOB01234) SUBMITTED
   ***
   17.18.43 JOB01234 $HASP165 HELLO    ENDED AT N1  MAXCC=0000 CN(INTERNAL)
   ***
   ```

   - `IKJ56250I ... SUBMITTED`: ジョブが受け付けられた
   - `$HASP165 ... MAXCC=0000`: ジョブが終わった。`MAXCC` は全ステップの中で最大の戻りコードで、`0000` は正常終了を表す

   2行目は、JOB 文に `NOTIFY=&SYSUID` があるので届きます。`NOTIFY` を消すと、この通知は届きません。

3. **Enter** を押して編集画面に戻ります。

---

## レッスン 2: 出力の3つの部品を読む

**目標:** SDSF でジョブの出力を開き、JES が作る3つのデータセットの役割を知る。

1. `Command ===>` に `=SD` と入力して Enter を押します。SDSF のメニューが出ます。
2. `ST` と入力して Enter を押します。投入したジョブの一覧が表示されます。

   ```
   NP   JOBNAME  JobID    Owner    Prty Queue      C  Max-RC
        HELLO    JOB01234 USER01      1 PRINT      A  CC 0000
   ```

3. `HELLO` の行の左端（`NP` の列）に `?` と入力して Enter を押します。

   ```
   NP   DDNAME   StepName ProcStep DSID ...
        JESMSGLG JES2                 2
        JESJCL   JES2                 3
        JESYSMSG JES2                 4
        SYSPRINT STEP1              101
        SYSUT2   STEP1              103
   ```

4. それぞれの行の左に `S` と入力して Enter を押し、中身を見てみましょう。F3 で一覧に戻れます。

   | 名前 | 中身 | 見るとき |
   |---|---|---|
   | **JESMSGLG** | ジョブの記録。開始・終了時刻と、各ステップの戻りコード（RC）の表 | まず最初に見る。どのステップで失敗したかが分かる |
   | **JESJCL** | 実際に解釈された JCL。行番号付き | 記号（`&SYSUID` など）がどう置き換わったかを確かめる |
   | **JESYSMSG** | システムのメッセージ。データセットの割り当てや、JCL エラーの詳細 | エラーの原因を調べる |
   | **SYSUT2** など | プログラムの出力 | 結果を確認する |

5. `SYSUT2` を開くと、`HELLO, Z/OS!` が表示されているはずです。

> [!TIP]
> SDSF のジョブ一覧で、ジョブ名をクリックするだけでも出力一覧（`?`）を開けます。

---

## レッスン 3: データセットを作る

**目標:** 新しいデータセットを作り、中身を確認する。

1. 右側のガイドの **ALLOC** を「開く」で開きます。

   ```
   //STEP1    EXEC PGM=IEFBR14
   //NEWDS    DD DSN=&SYSUID..SAMPLE.DATA,DISP=(NEW,CATLG,DELETE),
   //            SPACE=(TRK,(1,1)),UNIT=SYSDA,
   //            DCB=(RECFM=FB,LRECL=80,BLKSIZE=0)
   ```

   - `IEFBR14` は何もしないプログラムです。DD 文の `DISP=(NEW,CATLG)` によって、データセットの作成とカタログ登録だけが行われます。
   - `&SYSUID..SAMPLE.DATA` は `USER01.SAMPLE.DATA` になります。ピリオドが2つあるのは、1つ目が「記号の終わり」の印で、置き換えのときに消えるからです。

2. `SUB` で投入し、`MAXCC=0000` を確認します。
3. `Command ===>` に `=3.4` と入力して Enter を押します。Data Set List Utility の画面で `Dsname Level` が `USER01` になっていることを確かめ、もう一度 Enter を押します。データセットの一覧に `USER01.SAMPLE.DATA` が追加されています。
4. その行の左に `B` と入力して Enter を押すと、STEP2 で書き込んだ3行が表示されます。
5. ALLOC をもう一度投入してみましょう。今度は `JCL ERROR` になります。JESYSMSG を開くと、次のメッセージが出ています。

   ```
   IGD17101I DATA SET USER01.SAMPLE.DATA
     NOT DEFINED BECAUSE DUPLICATE NAME EXISTS IN CATALOG
   ```

   同じ名前のデータセットはもう作れない、という意味です。**CLEANUP** を投入すると削除できます。

---

## レッスン 4: JCL エラーを直す

**目標:** JCL エラーのメッセージから、間違っている行を見つけて直す。

1. **BADJCL** を開いて `SUB` を投入します。`ENDED AT N1 - JCL ERROR` になります。
2. SDSF で BADJCL の **JESYSMSG** を開きます。

   ```
    STMT NO. MESSAGE
           2 IEFC605I UNIDENTIFIED OPERATION FIELD
           4 IEFC630I UNIDENTIFIED KEYWORD SPCE
   ```

   `STMT NO.` は JESJCL に表示される文の番号です。JESJCL を開いて、2番と4番の文を探しましょう。

   - 2番: `EXCE` は `EXEC` の書き間違い（IEFC605I: 命令の名前が分からない）
   - 4番: `SPCE` は `SPACE` の書き間違い（IEFC630I: キーワードが分からない）

3. F3 で戻り、`=2` で編集画面に行きます。BADJCL を開いて2か所を直し、`SUB` で投入します。今度は `MAXCC=0000` になるはずです。

**投入せずにチェックする方法:** 編集画面で `JCK` と入力すると、ジョブを投入せずにチェックできます。問題のある行の行番号が `==ERR>` に変わります。**SYNTAX** サンプルには、よくある間違いが12種類入っているので、`JCK` で確認してから1つずつ直してみてください。

---

## レッスン 5: ABEND を読む

**目標:** JCL は正しいのに実行中に失敗する「ABEND」を知る。

1. **ABEND** を開いて投入します。`ABENDED  ABEND=S806` になります。
2. JESMSGLG を開きます。

   ```
   CSV003I REQUESTED MODULE MYPROG   NOT FOUND
   IEF450I ABEND STEP1 - ABEND=S806 U0000 REASON=00000004
   ```

   `S806` は「`PGM=` で指定したプログラムが見つからない」という意味です。

3. ステップの表も見てみましょう。

   ```
   -STEP1              S806 ...
   -STEP2             FLUSH ...
   -STEP3                00 ...
   ```

   ABEND の後のステップは、ふつうは実行されずに `FLUSH` になります。STEP3 は `COND=EVEN`（ABEND があっても実行する）が付いているので実行されています。

よく見る ABEND コードの例（このシミュレータで発生するもの）:

| コード | 意味 | 体験できるサンプル |
|---|---|---|
| S806 | プログラムが見つからない | ABEND |
| S013 | データセットの属性が合わず、開けない | OPENERR |
| S213 | 指定したボリュームにデータセットがない | DDPARMS |
| S80A | REGION（メモリ）が足りない | REGION |
| S722 | 出力行数の上限（OUTLIM）を超えた | `OUTLIM=` を付けて試す |

---

## レッスン 6: 自分で JCL を書く

**目標:** 新しいメンバーを作り、自分で JCL を書いて投入する。

1. `Command ===>` に `=2` と入力して Enter を押します。メンバー一覧が出ます。
2. `Command ===>` に `S MYJOB` と入力して Enter を押します。左端が `''''''` の入力行が並んだ、空の編集画面が開きます。
3. 次の JCL を入力します。各行の先頭の `//` は1桁目から書いてください。行を移るときは **↓** キーか **Shift+Enter**（行番号欄に移るので、続けて **Tab**）を使います。Enter を押すと、何も書いていない `''''''` 行は消えます。行が足りなくなったら、最後の行に入力した直後に Enter を押すと、次の入力行が自動で開きます。行番号欄に `I5` と入力して5行まとめて足すこともできます。

   ```
   //MYJOB    JOB (ACCT),'USER01',CLASS=A,MSGCLASS=X,NOTIFY=&SYSUID
   //STEP1    EXEC PGM=SORT
   //SYSOUT   DD SYSOUT=*
   //SORTOUT  DD SYSOUT=*
   //SORTIN   DD *
   BANANA
   APPLE
   CHERRY
   /*
   //SYSIN    DD *
     SORT FIELDS=(1,6,CH,A)
   /*
   ```

4. `JCK` でチェックし、問題がなければ `SUB` で投入します。
5. SDSF で `SORTOUT` を開くと、`APPLE` `BANANA` `CHERRY` の順に並んでいるはずです。

> [!TIP]
> - JCL の行は **71桁目まで** です。72桁目より右は無視されます。
> - 1つの文が長いときは、カンマで行を終わらせ、次の行を `//` と空白で始めます（4〜16桁目から続きを書く）。
> - `SORT FIELDS=` の前には空白が必要です。1桁目から書くと DFSORT のエラーになります。

---

## レッスン 7: プロシージャを使う

**目標:** よく使う JCL をプロシージャ（部品）にして呼び出す。

1. **INSTREAM** を開きます。`PROC` から `PEND` までが、`SAY` というプロシージャの定義です。

   ```
   //SAY      PROC MSG='DEFAULT MESSAGE'
   ...
   //         PEND
   //RUN1     EXEC SAY
   //RUN2     EXEC SAY,MSG='HELLO FROM RUN2'
   ```

   `MSG` は記号パラメーターです。`RUN1` では既定値の `DEFAULT MESSAGE` が、`RUN2` では `HELLO FROM RUN2` が使われます。

2. 投入して JESJCL を開くと、プロシージャが展開された結果が `++` で始まる行で表示されます。
3. 次に **PROCJOB** を開きます。こちらは、ライブラリ `USER01.PROCLIB` に保存されたプロシージャ（カタログ式）を呼び出します。JESJCL では次の印が付きます。
   - `XX`: ライブラリから読み込んだ行
   - `X/`: 上書き（オーバーライド）された行

プロシージャの中身は、`=3.4` の一覧で `USER01.PROCLIB` の左に `E` と入力すると見られます。

---

## レッスン 8: GDG で世代管理をする

**目標:** 毎日作る帳票のように、同じ名前のデータを世代ごとに残す。

1. **GDGDEF** を一度だけ投入します。`USER01.DAILY.REPORT` という GDG（世代データグループ）が作られます。最新の3世代まで残す設定です。
2. **GDGRUN** を投入します。`DSN=USER01.DAILY.REPORT(+1)` で、新しい世代 `G0001V00` が作られます。
3. GDGRUN をあと3回投入します。4回目の JESYSMSG に、次の行が出ます。

   ```
   IGD107I USER01.DAILY.REPORT.G0004V00             ROLLED IN, DDNAME=SYSUT2
             USER01.DAILY.REPORT.G0001V00 ROLLED OFF AND DELETED (GDG LIMIT 3)
   ```

   1行目は、新しい世代が GDG に組み込まれた（ロールイン）ことを示す z/OS のメッセージです。2行目は、4世代目ができたので、いちばん古い世代が消えたことを示しています。実際の z/OS にはこの処理専用のメッセージがないので、2行目はこの練習端末が付けている説明です。

4. GDGRUN の `READALL` ステップの出力を見ると、残っている3世代の中身が新しい順に並んでいます。

| 書き方 | 意味 |
|---|---|
| `名前(+1)` | このジョブで作る新しい世代 |
| `名前(0)` | 最新の世代 |
| `名前(-1)` | 1つ前の世代 |
| `名前` | すべての世代（新しい順につなげて読む） |

---

## 練習問題

答えは自分で `JCK` と `SUB` を使って確かめてください。

1. HELLO を書き換えて、`SYSUT1` のデータを3行に増やしてください。
2. ALLOC を書き換えて、`USER01.MY.DATA` という名前のデータセットを作ってください。
3. SORT サンプルを書き換えて、点数の小さい順（昇順）に並べてください。ヒント: `D` は降順です。
4. IFTEST を、ALLOC の実行前と実行後に投入して、実行されるステップがどう変わるか確かめてください。
5. 次の JCL には3種類の間違いがあります（1つは2か所にあるので、`JCK` では4件のエラーが出ます）。`JCK` で探して直してください。

   ```
   //Q5       JOB (ACCT),'USER01',CLASS=A,MSGCLASS=X
   //STEP1    EXEC PGM=IEFBR14
   //DD1      DD DSN=USER01.QUESTION5.DATA,DISP=(NEW,CATLG),SPACE=(TRK,1)
   //STEP2    EXEC PGM=IEBGENER,
   //SYSPRINT DD SYSOUT=*
   //SYSUT1   DD DSN=USER01.QUESTION5.DATA,DISP=SHR,
   //SYSUT2   DD SYSOUT=*
   ```

   <details>
   <summary>ヒントを見る</summary>

   - `QUESTION5` は9文字です。データセット名の1区切りは8文字までです（DD1 と SYSUT1 の2か所）。
   - STEP2 の行の最後のカンマは「次の行に続く」という意味になります。
   - SYSUT1 の行の最後も同じです。

   </details>
