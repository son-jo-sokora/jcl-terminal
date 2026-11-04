# JCL エラー一覧（z/OS 3.2 マニュアル照合）

z/OS 3.2 の MVS System Messages Vol 8（IEFC・IEF）と JES2 Messages に載っているメッセージを全件数え、
利用者の JCL で起きるものをテストにしました。テストは `tests/run.html` をブラウザで開くと実行できます。

- **テスト済み**: `tests/cases.js` にテスト JCL があり、シミュレーターがマニュアルの文面で出すもの
- **対象外**: JCL で起こりうるが、このシミュレーターにない機能や環境に依存するもの（理由を記載）
- **情報メッセージ**: 正常時にシミュレーターが出すもの（IEF236I など）
- **JCL では起きない**: 装置、オペレーター操作、システム障害などのメッセージ

「確度:低」は、マニュアルから発生条件や文面を一つに決められなかったテストです。

## 件数

| 種類 | テスト済み | 対象外 | 情報メッセージ | JCL では起きない | 合計 |
|---|---|---|---|---|---|
| IEFC（JCL の解釈） | 73 | 27 | 2 | 0 | 102 |
| IEF（割り振り・実行） | 43 | 91 | 8 | 322 | 464 |
| JES2 | 9 | 18 | 5 | 954 | 986 |

このほか、SMS・実行時のメッセージ（CSV003I, IEC141I, IEW4000I, IGD105I, IGD17101I, IGD17272I）もテストしています。

## IEFC（JCL の解釈）

| ID | 文面 | 分類 | テスト内容 |
|---|---|---|---|
| IEFC001I | PROCEDURE procname WAS EXPANDED USING text | テスト済み | インストリーム・プロシージャを呼ぶ（情報） |
| IEFC002I | INCLUDE GROUP group-name WAS EXPANDED USING text | テスト済み | INCLUDE グループを展開（情報） |
| IEFC003I | ALLOCATION ERROR IN PROCESSING A cntr STATEMENT | テスト済み | JCLLIB のライブラリが存在しない |
| IEFC004I | OPEN OF JCLLIB DATASETS WAS NOT SUCCESSFUL | 情報メッセージ（シミュレーターが出力） |  |
| IEFC005I | statement1 STATEMENT WITHOUT MATCHING statement2 STATEMENT | テスト済み | IF に ENDIF がない<br>IF のない ENDIF<br>IF のない ELSE |
| IEFC006I | POSITIONAL PARAMETERS MUST BE SPECIFIED BEFORE KEYWORD PARAMETERS | テスト済み | キーワードの後ろに位置パラメーター |
| IEFC007I | EXEC STATEMENT KEYWORDS ARE RESERVED AND CANNOT BE USED AS SYMBOLIC PA | テスト済み | PROC 文の記号名が EXEC のキーワード（PARM） |
| IEFC008I | PEND STATEMENT FOUND BEFORE END OF PROCEDURE | テスト済み | カタログ・プロシージャの途中に PEND |
| IEFC009I | KEYWORD key1 IS MUTUALLY EXCLUSIVE WITH KEYWORD key2 ON THE statement  | テスト済み | PARM と PARMDD を同時に指定<br>DD で SYSOUT と DISP を同時に指定 |
| IEFC010I | SYNTAX ERROR IN THE field FIELD OF THE statement STATEMENT | テスト済み | SET 文の記号名がない（確度:低） |
| IEFC011I | MAXIMUM OF nn LEVELS OF statement STATEMENT NESTING EXCEEDED | テスト済み | INCLUDE の入れ子が15段を超える（自分自身を INCLUDE）<br>プロシージャの入れ子が15段を超える |
| IEFC012I | JCL STATEMENT MAXIMUM LENGTH EXCEEDED | 対象外: TIOT など、環境で決まる上限 |  |
| IEFC013I | ERROR IN IF STATEMENT: keyword NOT VALID | テスト済み | IF に使えないキーワード |
| IEFC014I | ERROR IN IF STATEMENT: EXPRESSION MUST BE EVALUATED TO TRUE OR FALSE | テスト済み | IF の式が真偽にならない（RC だけ） |
| IEFC015I | ERROR IN IF STATEMENT: INCOMPATIBLE TYPES IN A COMPARISON | テスト済み | IF で RC とアベンドコードを比較 |
| IEFC016I | ERROR IN IF STATEMENT | テスト済み | IF の比較の右辺がない |
| IEFC017I | INCLUDE member WAS NOT FOUND | テスト済み | INCLUDE のメンバーがない |
| IEFC018I | UNEXPECTED END OF JCL | テスト済み | インストリーム・プロシージャに PEND がない |
| IEFC019I | MISPLACED statement STATEMENT | テスト済み | 最初の EXEC より後ろに JCLLIB |
| IEFC020I | DUPLICATE statement STATEMENT | テスト済み | JCLLIB が2つ |
| IEFC021I | EXTRANEOUS PARAMETERS SPECIFIED text | 対象外: マニュアルから発生条件を特定できない |  |
| IEFC022I | UNEXPECTED END OF PROCEDURE | テスト済み | プロシージャが継続の途中で終わる |
| IEFC023I | SYSIN OVERRIDE ERROR | 対象外: マニュアルから発生条件を特定できない |  |
| IEFC024I | INVALID POSITIONAL PARAMETER text | テスト済み | DD 文に知らない位置パラメーター（確度:低） |
| IEFC025I | INSTALLATION MODIFIED JCL - jclcardimage | 対象外: システム出口（IEFUJV など） |  |
| IEFC026I | EXIT ERROR: NON-ZERO RETURN CODE FROM IEFUJV EXIT STATEMENT IS IGNORED | 対象外: システム出口（IEFUJV など） |  |
| IEFC027I | EXIT ERROR: IEFUJV ATTEMPTED TO CHANGE VERB | 対象外: システム出口（IEFUJV など） |  |
| IEFC028I | EXIT ERROR: IEFUJV ATTEMPTED TO CHANGE JCL STATEMENT ID | 対象外: システム出口（IEFUJV など） |  |
| IEFC029I | EXIT ERROR: IEFUJV ATTEMPTED TO INSERT JCL COMMENTS STATEMENT IN ERROR | 対象外: システム出口（IEFUJV など） |  |
| IEFC030I | KEYWORD key1 SPECIFIED WITHOUT REQUIRED KEYWORD key2 ON THE statement  | テスト済み | PATH なしで PATHOPTS |
| IEFC031I | MISSING LABEL ON THE statement STATEMENT | テスト済み | OUTPUT 文に名前がない |
| IEFC032I | REQUIRED PARAMETER PROC OR PGM MUST PRECEDE ALL OTHER PARAMETERS ON TH | テスト済み | EXEC の最初が PGM/PROC でない |
| IEFC033I | ERROR IN IF STATEMENT: RC GREATER THAN MAXIMUM max | テスト済み | IF の RC が 4095 を超える |
| IEFC034I | JOBCAT OR STEPCAT NOT PERMITTED | テスト済み | JOBCAT DD を使う |
| IEFC035I | DUPLICATE VOLUME SERIAL volser FOUND | テスト済み | VOL=SER に同じボリュームを2回 |
| IEFC037I | ATTEMPTING TO RECALL MIGRATED DATA SET - DSNAME=dsname | 対象外: HSM による再呼び出し・データセットの競合 |  |
| IEFC038I | ATTEMPT TO RECALL MIGRATED DATA SET FAILED - RETURN CODE=return-code R | 対象外: HSM による再呼び出し・データセットの競合 |  |
| IEFC039I | ATTEMPT TO RECALL MIGRATED DATA SET WAS SUCCESSFUL | 対象外: HSM による再呼び出し・データセットの競合 |  |
| IEFC040I | ERROR ACCESSING DATA SET IN CONVERTER IEFUJV EXIT IN CONVERTER TEXT EX | 対象外: システム出口（IEFUJV など） |  |
| IEFC041I | INVALID MSGLEVEL, DEFAULTS (parameter1,parameter2) USED | テスト済み | MSGLEVEL の値が範囲外（警告） |
| IEFC042I | JOB CANCELLED BY INSTALLATION EXIT - IEFUJV | 対象外: システム出口（IEFUJV など） |  |
| IEFC043I | DATA SET dsname UNAVAILABLE - JOB jobname TO BE RESUBMITTED AUTOMATICA | 対象外: HSM による再呼び出し・データセットの競合 |  |
| IEFC044I | DATA SET dsname UNAVAILABLE - JOB job-name WILL WAIT FOR THE DATA SET | 対象外: HSM による再呼び出し・データセットの競合 |  |
| IEFC165I | cmd | テスト済み | COMMAND 文（情報） |
| IEFC417I | PROCLIB DEVICE I/O ERROR READING FOR JOB jobname | 対象外: 入出力障害・システム内部エラー |  |
| IEFC452I | text - JOB NOT RUN - JCL ERROR | テスト済み | JCL エラーでジョブが実行されない |
| IEFC601I | INVALID JCL STATEMENT | 対象外: マニュアルから発生条件を特定できない |  |
| IEFC602I | EXCESSIVE NUMBER OF EXECUTE STATEMENTS | テスト済み | EXEC 文が255を超える |
| IEFC603I | PROCLIB DEVICE I/O ERROR READING FOR JOB | 対象外: 入出力障害・システム内部エラー |  |
| IEFC605I | UNIDENTIFIED OPERATION FIELD | テスト済み | EXEC のつづり間違い |
| IEFC607I | JOB HAS NO STEPS | テスト済み | EXEC 文がない |
| IEFC609I | INVALID OVERRIDE KEYWORD keyword | テスト済み | PGM を EXEC で上書きしようとする（確度:低） |
| IEFC610I | PROCEDURE HAS NO STEP | テスト済み | プロシージャに EXEC がない |
| IEFC611I | OVERRIDDEN STEP NOT FOUND IN PROCEDURE | テスト済み | 上書き先のステップがプロシージャにない |
| IEFC612I | PROCEDURE [procname] WAS NOT FOUND | テスト済み | プロシージャが見つからない |
| IEFC614I | PROCLIB DEVICE I/O ERROR SEARCHING FOR PROCEDURE/INCLUDE | 対象外: 入出力障害・システム内部エラー |  |
| IEFC616I | SUBLIST WITHIN SUBLIST INCORRECT text | テスト済み | サブリストの中にサブリスト |
| IEFC618I | OPERAND FIELD DOES NOT TERMINATE IN COMMA OR BLANK | テスト済み | 閉じかっこの直後に文字が続く（確度:低） |
| IEFC620I | UNIDENTIFIABLE CHARACTER c text | テスト済み | JCL で使えない文字 |
| IEFC621I | EXPECTED CONTINUATION NOT RECEIVED | テスト済み | カンマで終わるのに継続行がない |
| IEFC622I | UNBALANCED PARENTHESIS text | テスト済み | かっこの対応が取れていない |
| IEFC624I | INCORRECT USE OF PERIOD text | テスト済み | データセット名にピリオドが連続 |
| IEFC625I | INCORRECT USE OF PARENTHESIS text | テスト済み | DSN 全体をかっこで囲む |
| IEFC626I | INCORRECT USE OF PLUS text | テスト済み | データセット名にプラス記号 |
| IEFC627I | INCORRECT USE OF AMPERSAND text | テスト済み | データセット名にアンパサンド |
| IEFC628I | INCORRECT USE OF ASTERISK text | テスト済み | データセット名にアスタリスク |
| IEFC629I | INCORRECT USE OF APOSTROPHE text | テスト済み | アポストロフィが閉じていない |
| IEFC630I | UNIDENTIFIED KEYWORD text | テスト済み | 知らないキーワード |
| IEFC632I | FORMAT ERROR {IN THE prm FIELD / ON THE cntr STATEMENT} | テスト済み | REGION の書式が違う |
| IEFC635I | JOBNAME MISSING ON THE JOB STATEMENT. SPECIFY JOBNAME AND RE-SUBMIT. | テスト済み | JOB 文にジョブ名がない |
| IEFC640I | EXCESSIVE NUMBER OF POSITIONAL PARAMETERS text | テスト済み | DISP の位置パラメーターが多すぎる |
| IEFC641I | IMPROPER SUBPARAMETER LIST text | テスト済み | プログラマー名をかっこで囲む（確度:低） |
| IEFC642I | EXCESSIVE PARAMETER LENGTH text | テスト済み | プログラム名が9文字 |
| IEFC646I | REQUIRED POSITIONAL PARAMETER MISSING text | テスト済み | SPACE の単位がない |
| IEFC647I | FIRST CHARACTER OF NAME MUST BE ALPHABETIC OR NATIONAL text | テスト済み | プログラム名が数字で始まる |
| IEFC650I | INCORRECT USE OF SLASH text | テスト済み | データセット名にスラッシュ |
| IEFC651I | INCORRECT USE OF HYPHEN text | テスト済み | プログラム名にハイフン |
| IEFC652I | DLM INCORRECTLY SPECIFIED ON A NON SYSIN DD STATEMENT (ONE THAT DOES N | テスト済み | DD * でない文に DLM |
| IEFC653I | SUBSTITUTION JCL - text | テスト済み | 記号の置き換え（情報） |
| IEFC654I | ILLEGAL USE OF SYMBOLIC ON SYSIN STATEMENT | テスト済み | 記号で DD * を指定（確度:低） |
| IEFC657I | THE SYMBOL symbol WAS NOT USED | テスト済み | 設定した記号を使っていない（情報） |
| IEFC658I | PROC VERB STATEMENT OUT OF SEQUENCE | テスト済み | プロシージャの途中に PROC 文 |
| IEFC659I | IEFC659I key INCORRECTLY SPECIFIED ON A NON SYSIN DD STATEMENT (ONE TH | テスト済み | DD * でない文に SYMBOLS= |
| IEFC660I | MISSING SYSCHK DD STATEMENT | テスト済み | チェックポイント再開に SYSCHK DD がない |
| IEFC662I | INVALID LABEL | テスト済み | ステップ名が9文字 |
| IEFC663I | NO LABEL ON THE PROC STATEMENT | テスト済み | インストリーム PROC 文に名前がない |
| IEFC665I | EXCESSIVE NUMBER OF INSTREAM PROCEDURES | テスト済み | インストリーム・プロシージャが15を超える（確度:低） |
| IEFC668I | PEND VERB STATEMENT OUT OF SEQUENCE | テスト済み | PROC のない PEND |
| IEFC677I | WARNING MESSAGE(S) FOR JOB jobname ISSUED | 情報メッセージ（シミュレーターが出力） |  |
| IEFC678I | DEVICE I/O ERROR CONVERTING/INTERPRETING JCL | 対象外: 入出力障害・システム内部エラー |  |
| IEFC679I | DEVICE I/O ERROR CONVERTING/INTERPRETING JCL FOR JOB jobname | 対象外: 入出力障害・システム内部エラー |  |
| IEFC680I | DEVICE I/O ERROR WRITING TO SYSTEM MESSAGE DATA SET FOR JOB jobname | 対象外: 入出力障害・システム内部エラー |  |
| IEFC683I | {CONVERTER / INTERPRETER ] TERMINATED DUE TO abendcde ABEND REASON=rea | 対象外: 入出力障害・システム内部エラー |  |
| IEFC690I | SCHEDULING ENVIRONMENT schenvname DOES NOT EXIST IN THE WLM SERVICE DE | テスト済み | SCHENV が WLM に定義されていない |
| IEFC691I | INCORRECT USE OF THE SCHENV FIELD | テスト済み | SCHENV が16文字を超える |
| IEFC744I | SUBSYSTEM NOT SPECIFIED | テスト済み | SUBSYS にサブシステム名がない（確度:低） |
| IEFC745I | SUBSYSTEM ssysname DOES NOT SUPPORT THE SUBSYSTEM KEY WORD | 対象外: サブシステムの状態に依存 |  |
| IEFC746I | SUBSYSTEM ssysname DOES NOT EXIST | テスト済み | 存在しないサブシステム |
| IEFC747I | SUBSYSTEM ssysname IS NOT OPERATIONAL | 対象外: サブシステムの状態に依存 |  |
| IEFC748I | SUBSYSTEM NAME INVALID | テスト済み | サブシステム名が4文字を超える |
| IEFC750I | SYSTEM ERROR IN PROCESSING SUBSYS DD PARAMETER | 対象外: サブシステムの状態に依存 |  |
| IEFC822I | KEYWORD keyword NOT SUPPORTED {BEFORE / AFTER} FIRST EXEC STATEMENT | 対象外: マニュアルから発生条件を特定できない |  |

## IEF（割り振り・実行）

| ID | 文面 | 分類 | テスト内容 |
|---|---|---|---|
| IEF001I | ERROR ON WRITE TO SYSTEM MESSAGE FILE | JCL では起きない（装置・運用・システム） |  |
| IEF002W | PENDING DEVICE PROCESSING MODULE IEFHBPDB HAS FAILED | JCL では起きない（装置・運用・システム） |  |
| IEF003I | jobname procstep stepname ddname + xxx - DD THAT IS CAUSING THE ABEND0 | JCL では起きない（装置・運用・システム） |  |
| IEF004I | jobname procstep stepname ddname + xxxx ERROR PROCESSING UNIT AFFINITY | JCL では起きない（装置・運用・システム） |  |
| IEF005I | jobname procstep stepname ddname + xxx - EDL CHANGED OUTSIDE ALLOCATIO | JCL では起きない（装置・運用・システム） |  |
| IEF006I | jobname RESTARTING AT xxxxxxxx K, yyyyyyyy K, aaaaaaaa K, bbbbbbbb K | JCL では起きない（装置・運用・システム） |  |
| IEF007I | RESTART NOT SUCCESSFUL FOR jobname (reason-code) | JCL では起きない（装置・運用・システム） |  |
| IEF008I | DASD DEVICE devnum NOT VARIED ONLINE - VOLUME SERIAL NOT VALID | JCL では起きない（装置・運用・システム） |  |
| IEF009I | CONCATENATE REQUEST FAILED - ACTUAL/CAPTURED UCB ATTRIBUTES OF SPECIFI | JCL では起きない（装置・運用・システム） |  |
| IEF010I | CHECKPOINT RESTART OF JOB jobname ABENDED - code | JCL では起きない（装置・運用・システム） |  |
| IEF011I | jobname [procstep] stepname ddname[+ xxx] — DEVICE dev IS BOXED — CANN | JCL では起きない（装置・運用・システム） |  |
| IEF013I | jobname CANNOT BE CANCELLED BECAUSE IT IS WAITING ON I/O | JCL では起きない（装置・運用・システム） |  |
| IEF014I | jobname [procstep] stepname ddname [+XXX] MAXIMUM GENERATED DDNAMES LI | JCL では起きない（装置・運用・システム） |  |
| IEF016I | jobname procstep stepname ddname +xxx UNABLE TO ALLOCATE UNINITIALIZED | JCL では起きない（装置・運用・システム） |  |
| IEF017I | jobname procstep stepname ddname +xxx FAILED TO UNLOAD VOLUME volser f | JCL では起きない（装置・運用・システム） |  |
| IEF018I | CRITICAL INTERNAL ALLOCATION TAPE PROCESSING ERROR DETECTED | JCL では起きない（装置・運用・システム） |  |
| IEF019I | jobname procstep stepname ddname +xxx THE ALLOCATED/OFFLINE EXIT, IEF_ | JCL では起きない（装置・運用・システム） |  |
| IEF020I | jobname procstep stepname TCT I/O TABLE SIZE EXCEEDS THE 16MB MAXIMUM. | JCL では起きない（装置・運用・システム） |  |
| IEF021I | jobname [procstep] stepname ddname [+ xxx] EXTENDED ADDRESS VOLUME USE | JCL では起きない（装置・運用・システム） |  |
| IEF022I | jobname [procstep] stepname ddname [+ xxx] ALLOCATION FAILED REQUESTED | JCL では起きない（装置・運用・システム） |  |
| IEF023I | jobname [procstep] stepname ddname [+ xxx] ALLOCATION FAILED NOT ENOUG | JCL では起きない（装置・運用・システム） |  |
| IEF024I | DASD DEVICE devnum NOT VARIED ONLINE - VOLUME IS INITIALIZED TO REMAIN | JCL では起きない（装置・運用・システム） |  |
| IEF030I | VOLUME actvol DOES NOT MATCH REQUESTED VOLUME reqvol | JCL では起きない（装置・運用・システム） |  |
| IEF031I | DEVICE CANNOT BE USED | JCL では起きない（装置・運用・システム） |  |
| IEF032I | STEP/stepname/STOP yyyyddd.hhmm CPU: xxxxx HR xx MIN xx.xx SEC SRB: xx | 情報メッセージ（シミュレーターが出力） |  |
| IEF033I | JOB/jobname/STOP yyyyddd.hhmm CPU: xxxxx HR xx MIN xx.xx SECSRB: xxxxx | 情報メッセージ（シミュレーターが出力） |  |
| IEF042I | JOB CANCELLED BY INSTALLATION EXIT - xxxxxxxx | 対象外: システム出口（IEFUJV など） |  |
| IEF044I | Actions ignored by SMFLIMxx parmlib policy for jobname stepname Step r | JCL では起きない（装置・運用・システム） |  |
| IEF083I | UNIDENTIFIED PARAMETER IN THE parameter FIELD | 対象外: マニュアルから発生条件を特定できない |  |
| IEF085I | REGION UNAVAILABLE, ERROR CODE=cde | 対象外: 性能・資源の指定（WLM ゴールモードで無視） |  |
| IEF086I | ERROR IN SWA RECOVERY - RESTART CANCELLED. REASON CODE = reason-code | JCL では起きない（装置・運用・システム） |  |
| IEF087I | ERROR ON JOB JOURNAL - RESTART CANCELLED. REASON CODE = reason-code | JCL では起きない（装置・運用・システム） |  |
| IEF089I | ERROR ON WRITE TO JOB JOURNAL-JOB NOT ELIGIBLE FOR RESTART. | JCL では起きない（装置・運用・システム） |  |
| IEF090E | PROTECT KEY UNAVAILABLE jobname PLACED ON HOLDQ | JCL では起きない（装置・運用・システム） |  |
| IEF091I | PROTECT KEY UNAVAILABLE START ppp REJECTED | JCL では起きない（装置・運用・システム） |  |
| IEF092I | jobname [procstep] stepname WAITING FOR xxxK REAL STORAGE | 対象外: 性能・資源の指定（WLM ゴールモードで無視） |  |
| IEF093I | INITIATOR TERMINATED DUE TO REGION LOSS location | JCL では起きない（装置・運用・システム） |  |
| IEF094A | INITIATOR TERMINATED DUE TO REGION LOSS location, RESTART INITIATOR | JCL では起きない（装置・運用・システム） |  |
| IEF097I | jobname USER userid ASSIGNED | JCL では起きない（装置・運用・システム） |  |
| IEF098I | SCHEDxx LINE num: PPT STMT IGNORED. NO OPERANDS SPECIFIED. | JCL では起きない（装置・運用・システム） |  |
| IEF099I | JOB jobname WAITING FOR DATA SETS | 対象外: HSM による再呼び出し・データセットの競合 |  |
| IEF100I | text1 [text2] ABEND=cde[,REASON=rrrrr] | JCL では起きない（装置・運用・システム） |  |
| IEF101I | jobname [procstep] stepname STEP FAILED, UNABLE TO RESOLVE UNIT AFFINI | JCL では起きない（装置・運用・システム） |  |
| IEF102I | jobname [procstep] stepname ddname [+ xxx] - UNRECOVERABLE DADSM ERROR | JCL では起きない（装置・運用・システム） |  |
| IEF103I | jobname [procstep] stepname ddname [+ xxx] - UNKNOWN DADSM ERROR RETUR | JCL では起きない（装置・運用・システム） |  |
| IEF104I | UNIT dev NOT BROUGHT ONLINE | JCL では起きない（装置・運用・システム） |  |
| IEF105I | jobname [procstep] stepname ddname callername UNKNOWN ERROR DURING LOG | JCL では起きない（装置・運用・システム） |  |
| IEF106I | jobname - UNIT dev BROUGHT ONLINE NAME=name CODE=code [text]... | JCL では起きない（装置・運用・システム） |  |
| IEF107I | PARMLIB CONCATENATION WAS UPDATED FROM loadxx | JCL では起きない（装置・運用・システム） |  |
| IEF108I | jobname [procstep] stepname callername READ BUFFER INPUT TO LOGICAL PA | JCL では起きない（装置・運用・システム） |  |
| IEF109I | PARMLIB CONCATENATION WAS NOT UPDATED FROM loadxx. reason | JCL では起きない（装置・運用・システム） |  |
| IEF110I | UNIT dddd DEALLOCATED BY SYSTEM DURING VARY OFFLINE PROCESSING BECAUSE | JCL では起きない（装置・運用・システム） |  |
| IEF111I | jobname [procstep] stepname ddname [ + xxx ] ALLOCATION FAILED DEVICE  | JCL では起きない（装置・運用・システム） |  |
| IEF112I | jobname [procstep] stepname ddname [ + xxx ] UNABLE TO ALLOCATE UNITS  | JCL では起きない（装置・運用・システム） |  |
| IEF113I | jobname [procstep] stepname ddname [ + xxx ] ALLOCATION FAILED - A LIB | JCL では起きない（装置・運用・システム） |  |
| IEF114I | DEVICE POOLS devpool-list | JCL では起きない（装置・運用・システム） |  |
| IEF115I | jobname [procstep] stepname ddname [+ xxx] ALLOCATION FAILED - ddd UNI | JCL では起きない（装置・運用・システム） |  |
| IEF116I | jobname stepname MOUNT OF VOLUME ser ON DEVICE dev FAILED | JCL では起きない（装置・運用・システム） |  |
| IEF118I | jobname stepname MOUNT OF VOLUME ser ON DEVICE dev FAILED | JCL では起きない（装置・運用・システム） |  |
| IEF119I | ERROR VERIFYING INTERNAL VOLUME LABEL ser ON DEVICE dev | JCL では起きない（装置・運用・システム） |  |
| IEF120I | jobname [procstep] stepname ddname [+ xxx] ALLOCATION FAILED - A NON-L | JCL では起きない（装置・運用・システム） |  |
| IEF121I | ALLOCATION QUEUE CHAIN ERROR DETECTED AND REPAIRED | JCL では起きない（装置・運用・システム） |  |
| IEF121A | CRITICAL ALLOCATION QUEUE CHAIN ERROR DETECTED | JCL では起きない（装置・運用・システム） |  |
| IEF122I | jobname [procstep] stepname ddname [+ xxx] SMS DETECTED AN ERROR DURIN | JCL では起きない（装置・運用・システム） |  |
| IEF123I | jobname [procstep] stepname ddname [+ xxx] SMS DETECTED AN ERROR DURIN | JCL では起きない（装置・運用・システム） |  |
| IEF124I | jobname [procstep] stepname ddname [+ xxx] ALLOCATION FAILED DEVICE PO | JCL では起きない（装置・運用・システム） |  |
| IEF125I | userid-LOGGED ON [-TIME=hh.mm.ss] | JCL では起きない（装置・運用・システム） |  |
| IEF126I | userid-LOGGED OFF [-TIME=hh.mm.ss] | JCL では起きない（装置・運用・システム） |  |
| IEF127I | jobname [procstep] stepname ddname[+ xxx] - NO SPACE PARAMETER OR ZERO | テスト済み | パラメーターのない DD 文 |
| IEF128I | jobname [procstep] stepname ddname[+ xxx] - INVALID REQUEST FOR ISAM I | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF129I | jobname [procstep] stepname ddname[+ xxx] - MULTIVOLUME INDEX NOT ALLO | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF130I | jobname [procstep] stepname ddname[+ xxx] - DSNAME ELEMENT WRONG - MUS | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF131I | jobname [procstep] stepname ddname[+ xxx] - MULTIVOLUME OVFLOW REQUEST | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF132I | jobname [procstep] stepname ddname[+ xxx] - SPACE PARAMETER WRONG - CY | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF133I | jobname [procstep] stepname ddname[+ xxx] - SPACE PARAMETER WRONG - CY | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF134I | jobname [procstep] stepname ddname[+ xxx] - SUBPARAMETER WRONG IN SPAC | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF135I | jobname [procstep] stepname ddname[+ xxx] - PRIMARY SPACE REQUEST MAY  | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF136I | jobname [procstep] stepname ddname[+ xxx] - DUPLICATION IN ALLOCATION  | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF140I | jobname [procstep] stepname ddname[+ xxx] - DIRECTORY SPACE REQUEST LA | JCL では起きない（装置・運用・システム） |  |
| IEF141I | jobname [procstep] stepname ddname[+ xxx] - INDEX REQUEST MUST PRECEDE | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF142I | jobname [procstep] stepname STEP WAS EXECUTED - COND CODE cde | テスト済み | ステップが正常に実行（情報）<br>PARMDD で PARM を渡す（正常） |
| IEF143I | jobname [procstep] stepname ddname[+ xxx] - LAST CONCATENATED DD STATE | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF145I | jobname [procstep] stepname ddname[+ xxx] - SPACE REQUEST MUST BE ABST | JCL では起きない（装置・運用・システム） |  |
| IEF147I | jobname [procstep] stepname ddname [xxx] ALLOCATION FAILED - NO DEVICE | JCL では起きない（装置・運用・システム） |  |
| IEF148I | jobname [procstep] stepname ddname [xxx] ALLOCATION FAILED REQUESTED D | JCL では起きない（装置・運用・システム） |  |
| IEF150I | jobname [procstep] stepname ddname [xxx] ALLOCATION FAILED UNABLE TO O | JCL では起きない（装置・運用・システム） |  |
| IEF151I | jobname [procstep] stepname ddname [+ xxx] ALLOCATION FAILED NON-LIBRA | JCL では起きない（装置・運用・システム） |  |
| IEF152I | jobname [procstep] stepname ddname [+ xxx] ALLOCATION FAILED NON-LIBRA | JCL では起きない（装置・運用・システム） |  |
| IEF153I | jobname [procstep] stepname ddname [+ xxx] ALLOCATION FAILED LIBRARY l | JCL では起きない（装置・運用・システム） |  |
| IEF154I | jobname stepname CANNOT BRING DEVICES ONLINE IN LIBRARY libname BECAUS | JCL では起きない（装置・運用・システム） |  |
| IEF155I | jobname [procstep] stepname ddnamexx [+ xxx] ALLOCATION FAILED UNABLE  | JCL では起きない（装置・運用・システム） |  |
| IEF156I | jobname [procstep] stepname ddnamexx [+ xxx] ALLOCATION FAILED UNABLE  | JCL では起きない（装置・運用・システム） |  |
| IEF157E | jobname [procstep] stepname ddname [+ xxx ] NEEDS ddd UNIT(S) [[FOR VO | JCL では起きない（装置・運用・システム） |  |
| IEF167I | NO JOB JOURNAL OPTION SPECIFIED - RESTART CANCELLED | JCL では起きない（装置・運用・システム） |  |
| IEF168I | ERROR ON JOB JOURNAL - RESTART FOR JOB CANCELLED | JCL では起きない（装置・運用・システム） |  |
| IEF169I | RESTART CANCELLED FOR JOB jobname | JCL では起きない（装置・運用・システム） |  |
| IEF170I | n jobname message | JCL では起きない（装置・運用・システム） |  |
| IEF172E | jobname HELD, CPU (x) OFFLINE OR UNAVAILABLE FOR JOB SCHEDULING | JCL では起きない（装置・運用・システム） |  |
| IEF173I | jobname FAILED, CPU (x) OFFLINE OR UNAVAILABLE FOR JOB SCHEDULING | JCL では起きない（装置・運用・システム） |  |
| IEF174I | SYSTEM ERROR BEFORE JOB INITIATION | 対象外: 入出力障害・システム内部エラー |  |
| IEF175I | AMP KEY WORD keyword DUPLICATE OR CONFLICTING PARM STEP NOT EXECUTED | JCL では起きない（装置・運用・システム） |  |
| IEF176I | WTR jobname WAITING FOR WORK, {CLASS= / FORMS= / WRITER= / DEST= / JOB | JCL では起きない（装置・運用・システム） |  |
| IEF177I | WTR jobname INVALID MODIFY KEY WORD | JCL では起きない（装置・運用・システム） |  |
| IEF179I | WTR jobname INVALID {JOBID jjjjjjjj/DEST xxxxxx} | JCL では起きない（装置・運用・システム） |  |
| IEF180I | jobname [procstep] stepname - INSUFFICIENT REAL OR VIRTUAL STORAGE FOR | JCL では起きない（装置・運用・システム） |  |
| IEF186I | REGION UNAVAILABLE FOR RESTART, ERROR CODE=cde | JCL では起きない（装置・運用・システム） |  |
| IEF187I | jobname FAILED - SYSTEM ERROR IN INITIATOR | 対象外: 入出力障害・システム内部エラー |  |
| IEF188I | PROBLEM PROGRAM ATTRIBUTES ASSIGNED | JCL では起きない（装置・運用・システム） |  |
| IEF191I | RESTART CANCELLED FOR JOB jobname - NO FURTHER STEPS TO BE EXECUTED | JCL では起きない（装置・運用・システム） |  |
| IEF192I | jobname [procstep] stepname ddname[+ xxx] - NO ELIGIBLE DEVICE TYPE CO | JCL では起きない（装置・運用・システム） |  |
| IEF193I | jobname [procstep] stepname ddname[+ xxx] - SPACE NOT OBTAINED BECAUSE | JCL では起きない（装置・運用・システム） |  |
| IEF194I | jobname [procstep] stepname ddname[+ xxx] - VOLUME SEQUENCE NUMBER EXC | JCL では起きない（装置・運用・システム） |  |
| IEF195I | jobname [procstep] stepname ddname[+ xxx] - MAXIMUM NUMBER OF DEVICES  | JCL では起きない（装置・運用・システム） |  |
| IEF196I | text | JCL では起きない（装置・運用・システム） |  |
| IEF197I | SYSTEM ERROR DURING {ALLOCATION/UNALLOCATION} | 対象外: 入出力障害・システム内部エラー |  |
| IEF198I | jobname [procstep] stepname ddname [+ xxx] - INSUFFICIENT UNRESTRICTED | JCL では起きない（装置・運用・システム） |  |
| IEF199I | jobname [procstep] stepname - CATALOG NOT MOUNTED - VOLUME MOUNTING NO | JCL では起きない（装置・運用・システム） |  |
| IEF201I | jobname [procstep] stepname - JOB TERMINATED BECAUSE OF CONDITION CODE | テスト済み | JOB の COND が成立してジョブ打ち切り |
| IEF202I | jobname [procstep] stepname - STEP WAS NOT RUN BECAUSE OF {CONDITION C | テスト済み | EXEC の COND が成立してステップを飛ばす<br>COND=ONLY で前のステップが正常 |
| IEF206I | jobname [procstep] stepname - STEP WAS NOT RUN BECAUSE OF CONDITIONAL  | テスト済み | IF が偽でステップを飛ばす |
| IEF209I | VIRTUAL STORAGE UNAVAILABLE FORjobname.procstep.stepname | JCL では起きない（装置・運用・システム） |  |
| IEF210I | jobname [procstep] stepname ddname[+ xxx] - UNIT FIELD SPECIFIES INCOR | テスト済み | 存在しない UNIT 名 |
| IEF211I | jobname [procstep] stepname ddname[+ xxx] - DATA SET RESERVATION UNSUC | JCL では起きない（装置・運用・システム） |  |
| IEF212I | jobname [procstep] stepname ddname[+ xxx] - DATA SET NOT FOUND | テスト済み | 存在しないデータセットを DISP=SHR |
| IEF213I | jobname [procstep] stepname ddname[+ xxx] - UNDETERMINED ERROR PROCESS | JCL では起きない（装置・運用・システム） |  |
| IEF214I | jobname [procstep] stepname ddname[+ xxx] - UNDETERMINED ERROR PROCESS | JCL では起きない（装置・運用・システム） |  |
| IEF217I | jobname [procstep] stepname ddname[+ xxx] - VOLUME CONTAINING PATTERN  | JCL では起きない（装置・運用・システム） |  |
| IEF218I | jobname [procstep] stepname ddname[+ xxx] - PATTERN DSCB RECORD NOT FO | JCL では起きない（装置・運用・システム） |  |
| IEF219I | jobname [procstep] stepname ddname[+ xxx] - GDG GROUP NAME EXCEEDS 35  | テスト済み | GDG 名が35文字を超える |
| IEF220I | jobname [procstep] stepname ddname[+ xxx] - GDG DEFINITION NOT VALID - | JCL では起きない（装置・運用・システム） |  |
| IEF221I | jobname [procstep] stepname - PGM=*.DD - REFERENCED STEP WAS NOT EXECU | テスト済み | PGM=*.ステップ.DD で参照先ステップが実行されていない |
| IEF222I | ALLOCxx LINE yyyy: ERROR IN tttt STATEMENT, {KEYWORD kkkk.} REASON=rea | JCL では起きない（装置・運用・システム） |  |
| IEF223I | ERROR(S) IN ALLOCxx PARMLIB MEMBER(S), REFER TO HARDCOPY LOG | JCL では起きない（装置・運用・システム） |  |
| IEF229I | LRECL EXCEEDS 32K | JCL では起きない（装置・運用・システム） |  |
| IEF230I | THE ATS WORK TASK IEFHTSWT ABENDED AND WAS REATTACHED | JCL では起きない（装置・運用・システム） |  |
| IEF233A | M dev,ser,[labtyp], jobname [,stepname [,dsname [,mediatype [,storgrp] | JCL では起きない（装置・運用・システム） |  |
| IEF234E | text1. dev [,ser, text2, jobname[,stepname]] [,SPACE=cpcc,tttt,aaaa/ y | JCL では起きない（装置・運用・システム） |  |
| IEF236I | ALLOC. FOR jobname [procstep] stepname | 情報メッセージ（シミュレーターが出力） |  |
| IEF237I | dev ALLOCATED TO ddname | 情報メッセージ（シミュレーターが出力） |  |
| IEF240I | jobname [procstep] stepname - TASK I/O TABLE EXCEEDS TIOT LIMIT OF xxx | 対象外: TIOT など、環境で決まる上限 |  |
| IEF242I | ALLOC. FOR jobname [procstep] stepname AT ABEND | JCL では起きない（装置・運用・システム） |  |
| IEF244I | jobname [procstep] stepname - UNABLE TO ALLOCATE nnn UNIT(S) text | JCL では起きない（装置・運用・システム） |  |
| IEF245I | jobname [procstep] stepname ddname[+ xxx] - INCONSISTENT UNIT NAME AND | テスト済み | テープ装置に DASD のボリュームを指定 |
| IEF246I | jobname [procstep] stepname ddname[+ xxx] - INSUFFICIENT SPACE ON STOR | JCL では起きない（装置・運用・システム） |  |
| IEF251I | jobname [procstep] stepname - JOB CANCELLED (in SYSOUT) --or-jobname J | JCL では起きない（装置・運用・システム） |  |
| IEF253I | jobname [procstep] stepname ddname[+ xxx] - DUPLICATE NAME ON DIRECT A | 対象外: SMS 管理のためほかのメッセージになる（IGD17101I など） |  |
| IEF254I | jobname [procstep] stepname ddname[+ xxx] - NO SPACE IN VTOC OR VTOC I | JCL では起きない（装置・運用・システム） |  |
| IEF256I | jobname [procstep] stepname ddname[+ xxx] - ABSOLUTE TRACK NOT AVAILAB | JCL では起きない（装置・運用・システム） |  |
| IEF257I | jobname [procstep] stepname ddname[+ xxx] - SPACE REQUESTED NOT AVAILA | 対象外: SMS 管理のためほかのメッセージになる（IGD17101I など） |  |
| IEF258I | jobname [procstep] stepname ddname[+ xxx] - INVALID RECORD LENGTH SPEC | テスト済み | SPACE の平均レコード長がトラック容量を超える |
| IEF259I | UNIT devnum IS NO LONGER DEFINED AS AUTOSWITCH. | JCL では起きない（装置・運用・システム） |  |
| IEF260I | jobname [procstep] stepname ddname[+ xxx] - WRONG DSORG OR DISP | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF261I | jobname [procstep] stepname ddname[+ xxx] - NO PRIME AREA REQUEST FOR  | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF262I | jobname [procstep] stepname ddname[+ xxx] - PRIME AREA MUST BE REQUEST | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF263I | jobname [procstep] stepname ddname[+ xxx] - SPACE REQUEST WRONG - MUST | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF264I | jobname [procstep] stepname ddname[+ xxx] - DUPLICATION OF THE DSNAME  | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF266I | jobname [procstep] stepname ddname[+ xxx] - INVALID JFCB POINTER | JCL では起きない（装置・運用・システム） |  |
| IEF267I | jobname [procstep] stepname ddname[+ xxx] - DIRECTORY SPACE REQUEST IS | テスト済み | ディレクトリー・ブロックが1次量より多い |
| IEF272I | jobname [procstep] stepname - STEP WAS NOT EXECUTED | テスト済み | 割り振りエラーでステップが実行されない |
| IEF273I | jobname [procstep] stepname ddname[+ xxx] - INVALID USER LABEL REQUEST | JCL では起きない（装置・運用・システム） |  |
| IEF274I | jobname [procstep] stepname ddname[+ xxx] - SPACE REQUEST REJECTED BY  | JCL では起きない（装置・運用・システム） |  |
| IEF275I | jobname [procstep] stepname ddname[+ xxx] - SPACE REQUEST CANNOT BE SA | JCL では起きない（装置・運用・システム） |  |
| IEF278I | jobname {procstep} stepname ddname {+ xxx} UNIT AFFINITY IGNORED, REAS | JCL では起きない（装置・運用・システム） |  |
| IEF280I | jobname {procstep} stepname STEP FAILED, UNABLE TO RESOLVE INCONSISTEN | JCL では起きない（装置・運用・システム） |  |
| IEF281I | dev NOW OFFLINE [-DEVICE IS BOXED] | JCL では起きない（装置・運用・システム） |  |
| IEF283I | dsname {NOT DELETED rc / UNCATALOGED} VOL SER NOS= ser [z],ser [z],ser | 情報メッセージ（シミュレーターが出力） |  |
| IEF284I | jobname stepname procname ddname +relpos UNABLE TO ALLOCATE DEVICE dev | JCL では起きない（装置・運用・システム） |  |
| IEF285I | dsname dsp rc VOL SER NOS= ser,ser,ser,ser,ser VOL SER NOS= ser,ser,se | テスト済み | SYSOUT データセットの後処理（情報） |
| IEF286I | jobname [procstep] stepname ddname[+ xxx] - DISP FIELD INCOMPATIBLE WI | テスト済み | GDG の世代 (0) がまだない（確度:低） |
| IEF287I | dsname dsp w VOL SER NOS= ser,ser,ser,ser,ser VOL SER NOS= ser,ser,ser | JCL では起きない（装置・運用・システム） |  |
| IEF288I | dsname SYSOUT | JCL では起きない（装置・運用・システム） |  |
| IEF289E | jobname stepname WAITING FOR VOLUME(S) OR UNIT(S) | JCL では起きない（装置・運用・システム） |  |
| IEF291I | jobname stepname HAS RECEIVED AN INVALID ACTION CODE xxx FROM yyy USER | JCL では起きない（装置・運用・システム） |  |
| IEF292I | UNIT devnum IS ASSIGNED TO A FOREIGN HOST | JCL では起きない（装置・運用・システム） |  |
| IEF293I | UNIT dev NOT VARIED ONLINE, UNABLE TO REGISTER DEVICE. SAME NED ASdupd | JCL では起きない（装置・運用・システム） |  |
| IEF294I | UNIT devnum IS NO LONGER ASSIGNED TO A FOREIGN HOST | JCL では起きない（装置・運用・システム） |  |
| IEF295I | jobname [procstep] stepname ddname [+ xxx] — VOLUME MOUNTING NOT ALLOW | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF300I | jobname WTR CLOSED - SUBSYSTEM INTERFACE ERROR xxxx/yyyy | JCL では起きない（装置・運用・システム） |  |
| IEF301I | jobname WTR CLOSED | JCL では起きない（装置・運用・システム） |  |
| IEF302A | jobname WTR WAITING TO START aaaaaaaa FOR JOBID nnnnnnnn | JCL では起きない（装置・運用・システム） |  |
| IEF303I | jobname WTR CLOSED - OUTPUT ERROR | JCL では起きない（装置・運用・システム） |  |
| IEF307I | jobname WTR CLOSED-OUTPUT DCB FAILED TO OPEN | JCL では起きない（装置・運用・システム） |  |
| IEF311I | NOP - SETPRT PARAMETER LIST INVALID | JCL では起きない（装置・運用・システム） |  |
| IEF314I | SYSIO | JCL では起きない（装置・運用・システム） |  |
| IEF316I | CCBAD | JCL では起きない（装置・運用・システム） |  |
| IEF318I | jobname [procstep] stepname ddname[+ xxx] ‘UNIT=AFF’ INVALID FOR REQUE | テスト済み | 新規 DASD データセットに UNIT=AFF |
| IEF321I | INVALID SEGMENT | JCL では起きない（装置・運用・システム） |  |
| IEF322I | NO FCB IMAGE-ID SPECIFIED FOR VERIFICATION | JCL では起きない（装置・運用・システム） |  |
| IEF323I | NO FCB IMAGE-ID SPECIFIED FOR ALIGNMENT | JCL では起きない（装置・運用・システム） |  |
| IEF324I | NO UCS IMAGE-ID SPECIFIED FOR VERIFICATION | JCL では起きない（装置・運用・システム） |  |
| IEF325I | OPERATOR CANCELLED LOAD. UCS/FCB IMAGE-ID/CHAIN NOT AVAILABLE. | JCL では起きない（装置・運用・システム） |  |
| IEF326I | PERMANENT I/O ERROR ON BLDL LOCATE ON UCS/FCB IMAGE IN SYSTEM LIBRARY | JCL では起きない（装置・運用・システム） |  |
| IEF327I | WTR dev CLOSED. PERMANENT I/O ERROR WHILE LOADING UCS/FCB BUFFER | JCL では起きない（装置・運用・システム） |  |
| IEF328I | WTR dev CLOSED. PERMANENT I/O ERROR ON UCS/FCB IMAGE VERIFICATION. | JCL では起きない（装置・運用・システム） |  |
| IEF329I | WTR dev CLOSED. OPERATOR CANCELLED LOAD. INCORRECT UCS/FCB IMAGE DISPL | JCL では起きない（装置・運用・システム） |  |
| IEF330I | jobname [procstep] stepname ddname[+ xxx] - DATA SET WAIT REQUEST CANC | JCL では起きない（装置・運用・システム） |  |
| IEF331I | WTR dev CLOSED. SETPRT NOP-UNCORRECTABLE OUTPUT ERROR ON PREVIOUS OPER | JCL では起きない（装置・運用・システム） |  |
| IEF333I | jobname [procstep] stepname ddnamexx [+ xxx ] UNABLE TO ALLOCATE UNITS | JCL では起きない（装置・運用・システム） |  |
| IEF336I | jobname [procstep] stepname ddname [+ xxx] JOB CANCELLED BY {/VOLUME_M | JCL では起きない（装置・運用・システム） |  |
| IEF337I | jobname [procstep] stepname - UNABLE TO ACCESS LOCKED CATALOG | JCL では起きない（装置・運用・システム） |  |
| IEF341I | ALLOCATION LISTEN REQUEST FAILED. VARYING A DEVICE ONLINE WILL NOT STA | JCL では起きない（装置・運用・システム） |  |
| IEF343I | jobname [procstep] stepname - ddname[+ xxx] REQUEST FAILED - text | JCL では起きない（装置・運用・システム） |  |
| IEF344I | jobname [procstep] stepname - ddname [+ xxx] ALLOCATION FAILED DUE TO  | JCL では起きない（装置・運用・システム） |  |
| IEF345I | jobname [procstep] stepname - ddname [+ xxx] ALLOCATION FAILED DUE TO  | JCL では起きない（装置・運用・システム） |  |
| IEF347I | jobname [procstep] stepname - ddname [+ xxx] DEVICE - dev CANNOT BE AL | JCL では起きない（装置・運用・システム） |  |
| IEF348I | AUTOSWITCH DEVICE dddd WILL NOT BE CONSIDERED FOR THIS ALLOCATION DUE  | JCL では起きない（装置・運用・システム） |  |
| IEF350I | CHECKPOINT OF JOB jobname STEP stepname.procstep ABENDED Sabn REASON=r | JCL では起きない（装置・運用・システム） |  |
| IEF351I | ASSIGN PROCESSING TIMED OUT FOR AUTOSWITCH DEVICE dddd | JCL では起きない（装置・運用・システム） |  |
| IEF352I | ADDRESS SPACE UNAVAILABLE ASID=aaaa JOBNAME=jjjjjjjj | JCL では起きない（装置・運用・システム） |  |
| IEF353A | INITIATOR TERMINATED DUE TO CROSS MEMORY BIND, RESTART INITIATOR | JCL では起きない（装置・運用・システム） |  |
| IEF354I | DISABLED DASD DEVICE dev NOT VARIED ONLINE | JCL では起きない（装置・運用・システム） |  |
| IEF355A | INITIATOR TERMINATED, RESTART INITIATOR | JCL では起きない（装置・運用・システム） |  |
| IEF356I | ADDRESS SPACE TERMINATED DUE TO CROSS MEMORY BIND | JCL では起きない（装置・運用・システム） |  |
| IEF357I | jobname[procstep] stepname ddname [xxx] ALLOCATION FAILED UNABLE TO OB | JCL では起きない（装置・運用・システム） |  |
| IEF358I | jobname [procstep] stepname ddname(+xxx) - TP DEVICE dev NOT ALLOCATED | JCL では起きない（装置・運用・システム） |  |
| IEF359I | RESERVED OR BROKEN DASD DEVICE dev NOT VARIED ONLINE | JCL では起きない（装置・運用・システム） |  |
| IEF360I | RESTART NOT SUCCESSFUL FOR jobname: ERROR IN SAF | JCL では起きない（装置・運用・システム） |  |
| IEF361I | jobname [procstep] stepname - UNABLE TO ALLOCATE/OPEN PRIVATE CATALOG  | JCL では起きない（装置・運用・システム） |  |
| IEF362I | jobname [procstep] stepname - UNABLE TO CLOSE/UNALLOCATE PRIVATE CATAL | JCL では起きない（装置・運用・システム） |  |
| IEF363I | jobname [procstep] stepname - INSUFFICIENT REAL OR VIRTUAL STORAGE FOR | JCL では起きない（装置・運用・システム） |  |
| IEF364I | jobname [procstep] stepname - PERMANENT I/O ERROR PROCESSING CATALOGED | JCL では起きない（装置・運用・システム） |  |
| IEF365I | jobname [procstep] stepname ddname[+ xxx] - INVALID REFERENCE TO A GEN | テスト済み | VOL=REF に GDG のベース名 |
| IEF366I | jobname [procstep] stepname ddname[+ xxx] - RELATIVE GENERATION NUMBER | テスト済み | GDG の相対世代番号が 255 を超える |
| IEF367I | jobname [procstep] stepname - I/O ERROR OBTAINING PATTERN DSCB | JCL では起きない（装置・運用・システム） |  |
| IEF368I | jobname [procstep] stepname - UNABLE TO function CATALOG - RETURN INFO | JCL では起きない（装置・運用・システム） |  |
| IEF371I | - jobname [procstep] stepname ddname [+ xxx] - TELECOMMUNICATION DEVIC | JCL では起きない（装置・運用・システム） |  |
| IEF372I | jobname [procstep] stepname ddname[+ xxx] - VOLUME FIELD CONTAINS REFE | テスト済み | VOL=REF が実行されなかったステップの DD を参照 |
| IEF373I | STEP/stepname/START yyyyddd.hhmm | テスト済み | ステップ開始時刻（情報） |
| IEF374I | STEP/stepname/STOP yyyyddd.hhmm CPU xxxx MIN xx.xx SECSRB xxxx MIN xx. | JCL では起きない（装置・運用・システム） |  |
| IEF375I | JOB/jobname/START yyyyddd.hhmm | 情報メッセージ（シミュレーターが出力） |  |
| IEF376I | JOB/jobname/STOP yyyyddd.hhmm CPU xxxx MIN xx.xx SEC SRB xxxx MIN xx.x | JCL では起きない（装置・運用・システム） |  |
| IEF377I | jobname [procstep] stepname dsname NOT disp w | 対象外: SMS 管理のためほかのメッセージになる（IGD17101I など） |  |
| IEF378I | jobname [procstep] stepname - JOB FAILED [ - TIME= hh.mm.ss] CATALOG D | JCL では起きない（装置・運用・システム） |  |
| IEF379I | jobname [procstep] stepname - JOB ENDED BECAUSE OF CATALOG ERROR | JCL では起きない（装置・運用・システム） |  |
| IEF380I | jobname [procstep] stepname ddname [+ xxx] - VOLUME COUNT FOR DD EXCEE | JCL では起きない（装置・運用・システム） |  |
| IEF381I | DEVICE dev HAS NO UNIT NAME, DEVICE TYPE IS 'dddddddd'X | JCL では起きない（装置・運用・システム） |  |
| IEF382A | jobname WTR WAIT DUE TO PAUSE | JCL では起きない（装置・運用・システム） |  |
| IEF383A | jobname WTR, CHANGE FORM TO nnnn | JCL では起きない（装置・運用・システム） |  |
| IEF384I | jobname [procstep] stepname ddname - WARNING: VOLUME NOT RETRIEVED FRO | JCL では起きない（装置・運用・システム） |  |
| IEF387I | ADDRESS SPACE TERMINATED DUE TO EDT LATCH BIND | JCL では起きない（装置・運用・システム） |  |
| IEF388A | ADDRESS SPACE TERMINATED DUE TO EDT LATCH BIND, RESTART INITIATOR | JCL では起きない（装置・運用・システム） |  |
| IEF391I | jobname stepname procname ddname +relpos UNABLE TO ALLOCATE - A TAPE A | JCL では起きない（装置・運用・システム） |  |
| IEF396I | ERROR DETECTED BY THE INITIATOR, SYMPTOM CODES = xx,yyyy,zzzzzzzz. | JCL では起きない（装置・運用・システム） |  |
| IEF402I | {jobname/cm/ stc_procname.identifier} FAILED IN ADDRESS SPACE asid SYS | JCL では起きない（装置・運用・システム） |  |
| IEF403I | jobname-STARTED [-TIME=hh.mm.ss] | テスト済み | ジョブ開始・終了（情報） |
| IEF404I | jobname-ENDED [-TIME=hh.mm.ss] | 情報メッセージ（シミュレーターが出力） |  |
| IEF405I | jjobname .procstep. stepname ddname dsname WARNING: 2-DIGIT EXPDT | JCL では起きない（装置・運用・システム） |  |
| IEF406I | jjobname .procstep. stepname ddname dsname APPLICATION FAILED: 2-DIGIT | JCL では起きない（装置・運用・システム） |  |
| IEF414I | dev UNIT NOT AVAILABLE - UNLOAD ATTEMPTED | JCL では起きない（装置・運用・システム） |  |
| IEF415I | dev NOT UNLOADED - NO LONGER PENDING UNLOAD | JCL では起きない（装置・運用・システム） |  |
| IEF420I | MVS DEFAULT MODE CONTROL FAILURE, DEVICE dev NOT ASSIGNED | JCL では起きない（装置・運用・システム） |  |
| IEF428I | WARNING: 2-DIGIT EXPIRATION DATE USED | JCL では起きない（装置・運用・システム） |  |
| IEF429I | ALLOCATION FAILED: 2-DIGIT EXPIRATION DATE USED IN THE EXPDT SUBPARAME | JCL では起きない（装置・運用・システム） |  |
| IEF430I | RESTART STEP NOT FOUND FOR JOB jobname | 情報メッセージ（シミュレーターが出力） |  |
| IEF431E | ZERO QMPA POINTER FOUND. SWA MANAGER REASON CODE=3C | JCL では起きない（装置・運用・システム） |  |
| IEF438I | SUBTASK OF jobname TERMINATED. COMPLETION CODE cde | JCL では起きない（装置・運用・システム） |  |
| IEF447I | AMP KEY WORD keywd IS INVALID STEP WAS NOT EXECUTED | JCL では起きない（装置・運用・システム） |  |
| IEF448I | AMP KEY WORD keywd VALUE val IS TOO LARGE STEP NOT EXECUTED | JCL では起きない（装置・運用・システム） |  |
| IEF449I | AMP KEY WORD keywd REQUIRES A DECIMAL VALUE STEP NOT EXECUTED | JCL では起きない（装置・運用・システム） |  |
| IEF450I | jobname [procstep] stepname - ABEND {Scde / Ucde} REASON=xxxxxxxx [TIM | テスト済み | 存在しないプログラムで S806 |
| IEF451I | jobname [procstep] stepname - ENDED BY CC cde[-TIME=hh.mm.ss] | JCL では起きない（装置・運用・システム） |  |
| IEF452I | jobname - JOB NOT RUN - JCL ERROR [- TIME=hh.mm.ss] | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF453I | jobname - JOB FAILED - JCL ERROR [- TIME=hh.mm.ss] | テスト済み | 割り振り時の JCL エラー |
| IEF456I | jobname [procstep] stepname - DEVICE ALLOCATION UNABLE TO ESTABLISH ES | JCL では起きない（装置・運用・システム） |  |
| IEF462I | jobname [procstep] stepname ddname[+ xxx] - NO AVAILABLE OFFLINE DEVIC | JCL では起きない（装置・運用・システム） |  |
| IEF463I | jobname [procstep] stepname ddname[+ xxx] - UNABLE TO ALLOCATE SUBSYST | JCL では起きない（装置・運用・システム） |  |
| IEF464I | jobname [procstep] stepname ddname[+ xxx] - DEVICE IS BOXED CANNOT BE  | JCL では起きない（装置・運用・システム） |  |
| IEF465I | jobname [procstep] stepname - UNABLE TO ALLOCATE SUBSYSTEM DATA SET | JCL では起きない（装置・運用・システム） |  |
| IEF466I | jobname [procstep] stepname ddname[+ xxx] - UNABLE TO RECOVER FROM DAD | JCL では起きない（装置・運用・システム） |  |
| IEF467I | jobname [procstep] stepname ddname[+ xxx] - UNITS REQUIRED NOT CURRENT | JCL では起きない（装置・運用・システム） |  |
| IEF468I | jobname [procstep] stepname - INSUFFICIENT REAL OR VIRTUAL STORAGE FOR | JCL では起きない（装置・運用・システム） |  |
| IEF469I | jobname [procstep] stepname DATA SETS HAVE NOT BEEN RELEASED | JCL では起きない（装置・運用・システム） |  |
| IEF470I | jobname [procstep] stepname - UNALLOCATION FAILED | JCL では起きない（装置・運用・システム） |  |
| IEF471E | FOLLOWING VOLUMES NO LONGER NEEDED BY jobname ser,ser,...ser | JCL では起きない（装置・運用・システム） |  |
| IEF472I | jobname [procstep] stepname - COMPLETION CODE - SYSTEM=Scde USER=Ucde  | JCL では起きない（装置・運用・システム） |  |
| IEF473I | jobname [procstep] stepname - ERROR ATTEMPTING TO SELECT OPTIMUM DEVIC | JCL では起きない（装置・運用・システム） |  |
| IEF474I | jobname [procstep] stepname ddname[+ xxx] - UNIT OR VOLUME IN USE BY S | JCL では起きない（装置・運用・システム） |  |
| IEF475I | jobname [procstep] stepname ddname[+ xxx] - VOL ON INELIGIBLE PERMRES  | JCL では起きない（装置・運用・システム） |  |
| IEF476I | jobname [procstep] stepname ddname[+ xxx] - OVERLAPPING DATA SETS IN V | JCL では起きない（装置・運用・システム） |  |
| IEF477I | jobname [procstep] stepname ddname[+ xxx] - OVERLAPPING DOS SPLIT CYLI | JCL では起きない（装置・運用・システム） |  |
| IEF478I | jobname [procstep] stepname ddname[+ xxx] - VTOC ERROR MAY EXIST - ANA | JCL では起きない（装置・運用・システム） |  |
| IEF479I | jobname [procstep] stepname ddname[+ xxx] - POSSIBLE VTOC ERROR ON 2ND | JCL では起きない（装置・運用・システム） |  |
| IEF480I | jobname [procstep] stepname ddname[+ xxx] - INVALID DESTINATION REQUES | JCL では起きない（装置・運用・システム） |  |
| IEF481I | jobname [procstep] stepname ddname[+ xxx] - SAME UNIT REQUESTED TWICE  | JCL では起きない（装置・運用・システム） |  |
| IEF482I | jobname [procstep] stepname ddname[+ xxx] - PERMRES/RESRV VOLUME ON RE | JCL では起きない（装置・運用・システム） |  |
| IEF483I | jobname [procstep] stepname ddname[+ xxx] - REQUESTED DEVICE IS A CONS | JCL では起きない（装置・運用・システム） |  |
| IEF484I | jobname [procstep] stepname ddname[+ xxx] - MORE UNITS REQUIRED FOR RE | JCL では起きない（装置・運用・システム） |  |
| IEF485I | jobname [procstep] stepname [ddname] - VOLUMES REQUIRED NOT CURRENTLY  | JCL では起きない（装置・運用・システム） |  |
| IEF488I | jobname - ddname +nnn MUST WAIT FOR [UNIT dev/VOLUME ser ON UNIT dev] | JCL では起きない（装置・運用・システム） |  |
| IEF490I | jobname - INVALID REPLY. [text] | JCL では起きない（装置・運用・システム） |  |
| IEF491I | jobname [procstep] stepname - DD GENERATIONS CAUSE TOTAL DD STATEMENTS | 対象外: TIOT など、環境で決まる上限 |  |
| IEF492I | jobname [procstep] stepname ddname[+ xxx] - INVALID DATA SET NAME SPEC | JCL では起きない（装置・運用・システム） |  |
| IEF493I | jobname [procstep] stepname ddname[+ xxx] - INVALID PARAMETERS SPECIFI | JCL では起きない（装置・運用・システム） |  |
| IEF500I | ddtype DD ddname IS ERRONEOUSLY MARKED AS AN SMS LIBRARY MANAGED TAPE  | JCL では起きない（装置・運用・システム） |  |
| IEF502I | text | JCL では起きない（装置・運用・システム） |  |
| IEF503I | {UNIT dev INCORRECT VOLUME LABEL / UNIT dev I/O ERROR} | JCL では起きない（装置・運用・システム） |  |
| IEF506I | jobname [procstep] stepname ddname[+ xxx] - NO STORAGE VOLUMES. ‘VOLUM | JCL では起きない（装置・運用・システム） |  |
| IEF510I | VOLUME HAS ANS LABEL | JCL では起きない（装置・運用・システム） |  |
| IEF524I | dev{, VOLUME ser} PENDING OFFLINE | JCL では起きない（装置・運用・システム） |  |
| IEF525E | dev{, VOLUME ser} STILL PENDING OFFLINE | JCL では起きない（装置・運用・システム） |  |
| IEF550I | jobname {procstep} stepname STEP FAILED, UNABLE TO RESOLVE DATA SET ST | JCL では起きない（装置・運用・システム） |  |
| IEF572I | [jobname.stepname] VOLUME VERIFICATION ERROR ON ser | JCL では起きない（装置・運用・システム） |  |
| IEF602I | EXCESSIVE NUMBER OF EXECUTE STATEMENTS | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF604I | EXPDT SUBPARAMETER OF LABEL KEYWORD SPECIFIES ZERO DAYS VALUE | テスト済み | EXPDT の日数が 000 |
| IEF606I | MISPLACED DD STATEMENT | テスト済み | 最初の EXEC より前に JOBLIB 以外の DD |
| IEF617I | NO NAME ON FIRST DD STATEMENT AFTER EXEC STATEMENT | テスト済み | EXEC 直後の DD に名前がない |
| IEF619I | SUBPARAMETER IN SYSOUT FIELD IS MUTUALLY EXCLUSIVE WITH SUBPARAMETER I | テスト済み | SYSOUT の書き出しプログラムと DEST のユーザーを同時に指定 |
| IEF623I | SOURCE TEXT CONTAINS UNDEFINED OR ILLEGAL CHARACTERS text | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF624I | INCORRECT USE OF PERIOD text | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF625I | INCORRECT USE OF PARENTHESIS IN THE parameter FIELD | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF631I | NUMBER OF DDNAMES EXCEEDS MAXIMUM | テスト済み | 未解決の DDNAME= が6つ |
| IEF632I | FORMAT ERROR text | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF633I | PROGRAMMER NAME MISSING text | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF634I | ACCOUNT NUMBER MISSING text | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF635I | JOBNAME MISSING text | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF636I | MISPLACED JOBLIB STATEMENT | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF637I | EXCESSIVE ACCOUNT FIELD LENGTH text | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF638I | SPECIFIED NUMERIC EXCEEDS MAXIMUM ALLOWED text | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF639I | INVALID CLASS DESIGNATION text | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF640I | EXCESSIVE NUMBER OF POSITIONAL PARAMETERS text | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF641I | IMPROPER SUBPARAMETER LIST text | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF642I | EXCESSIVE PARAMETER LENGTH text | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF643I | UNIDENTIFIED POSITIONAL PARAMETER text | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF644I | INVALID NUMERIC text | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF645I | INVALID REFER BACK text | テスト済み | OUTPUT= が存在しない OUTPUT 文を参照<br>DSN=*.ステップ.DD が存在しないステップを参照（確度:低） |
| IEF646I | REQUIRED POSITIONAL PARAMETER MISSING text | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF647I | FIRST CHARACTER OF NAME NOT ALPHABETIC OR NOT NATIONAL text | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF648I | INVALID DISP FIELD - {KEEP/PASS} SUBSTITUTED | テスト済み | 一時データセットに DISP=KEEP（PASS に置き換え） |
| IEF649I | EXCESSIVE NUMBER OF DD STATEMENTS | 対象外: TIOT など、環境で決まる上限 |  |
| IEF650I | INCORRECT USE OF SLASH xxx | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF653I | SUBSTITUTION JCL - text | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF654I | MULTIPLE DDNAMES REFER TO ONE DD STATEMENT | テスト済み | 2つの DD が同じ名前を DDNAME= で参照 |
| IEF655I | INVALID DSNAME SPECIFIED WHEN SYSIN OR SYSOUT SPECIFIED | 対象外: マニュアルから発生条件を特定できない |  |
| IEF656I | DD STATEMENT NAME INCONSISTENT WITH AMP | JCL では起きない（装置・運用・システム） |  |
| IEF661I | RESTART STEP NOT FOUND | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF667E | ENF LISTEN EXIT ERROR FOR EVENT CODE xx | JCL では起きない（装置・運用・システム） |  |
| IEF669I | INVALID REFER FORWARD TO DYNAM DATA SET | JCL では起きない（装置・運用・システム） |  |
| IEF670I | NO VALUE ASSIGNED TO SYMBOLIC PARAMETER ON PROC STMT VIA THE EXEC STMT | 対象外: マニュアルから発生条件を特定できない |  |
| IEF671I | MISPLACED JOBCAT DD STATEMENT | JCL では起きない（装置・運用・システム） |  |
| IEF672I | MULTIPLE STEPCAT DD STATEMENT IN STEP | JCL では起きない（装置・運用・システム） |  |
| IEF673I | ADDRSPC=REAL INVALID ON THE cntr STATEMENT | 対象外: 権限・TSO 固有 |  |
| IEF674I | INVALID DYNAMNBR VALUE - 0 SUBSTITUTED | テスト済み | DYNAMNBR が数字でない（警告）（確度:低） |
| IEF675I | PERFORM VALUE INVALID OR OMITTED - SYSTEM DEFAULT SUBSTITUTED | 対象外: 性能・資源の指定（WLM ゴールモードで無視） |  |
| IEF677I | WARNING MESSAGE(S) FOR JOB jobname ISSUED | 対象外: 古い形式（今は IEFC 側のメッセージが出る） |  |
| IEF679I | DEVICE I/O ERROR CONVERTING/INTERPRETING JCL FOR JOB jobname | 対象外: 入出力障害・システム内部エラー |  |
| IEF680I | DEVICE I/O ERROR WRITING TO SYSTEM MESSAGE DATA SET FOR JOB jobname | 対象外: 入出力障害・システム内部エラー |  |
| IEF681I | INVALID COPIES VALUE - DEFAULT OF ONE SUBSTITUTED | テスト済み | COPIES が255を超える（警告）（確度:低） |
| IEF682I | FREE VALUE INVALID - DEFAULT OF (END) SUBSTITUTED | テスト済み | FREE が CLOSE/END 以外（警告）（確度:低） |
| IEF683I | {CONVERTER / INTERPRETER} TERMINATED DUE TO abendcde ABEND REASON=reas | 対象外: 入出力障害・システム内部エラー |  |
| IEF684I | HOLD VALUE INVALID - DEFAULT OF ‘NO’ SUBSTITUTED | テスト済み | HOLD が YES/NO 以外（警告）（確度:低） |
| IEF685I | STATIC PLUS DYNAMIC DD COUNT EXCEEDS MAX - DYNAMIC DD'S REDUCED | JCL では起きない（装置・運用・システム） |  |
| IEF686I | DDNAME REFERRED TO ON DDNAME KEYWORD IN PRIOR STEP WAS NOT RESOLVED | テスト済み | DDNAME= の参照先がステップにない（警告） |
| IEF687I | jobname [procstep] stepname ddname [+ xxx] - REQUESTED VOLUME MOUNTED  | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF688I | jobname [procstep] stepname ddname [+ xxx] - NULLFILE AND DSNAME CONFL | JCL では起きない（装置・運用・システム） |  |
| IEF689I | JOB jjjjjjjj FAILED ddname DID NOT OPEN | テスト済み | PARMDD の DD がない（確度:低） |
| IEF690I | FOLLOWING VOLUMES UNAVAILABLE TO jobname stepname ser1 ser2 … ser9 | JCL では起きない（装置・運用・システム） |  |
| IEF691I | jobname [procstep] stepname ddname[+ xxx] - DATA SET/VOLUME COULD NOT  | 対象外: 権限・TSO 固有 |  |
| IEF692I | INVALID REFERENCE TO HIERARCHICAL FILE [text] | テスト済み | VOL=REF で z/OS UNIX ファイルの DD を参照 |
| IEF694I | DDNAME REFERENCE TO DD CONCATENATION REFERS ONLY TO FIRST DD | テスト済み | DDNAME= で連結 DD を参照（警告） |
| IEF695I | START mbrname WITH JOBNAME jobname IS ASSIGNED TO USER userid ,GROUP g | JCL では起きない（装置・運用・システム） |  |
| IEF696I | I/O TIMEOUT ON DEVICE dev - DEVICE MARKED NOT READY | JCL では起きない（装置・運用・システム） |  |
| IEF700I | jobname [procstep] stepname - ENVIRONMENT CHANGED. NOW UNABLE TO ALLOC | JCL では起きない（装置・運用・システム） |  |
| IEF701I | jobname [procstep] stepname [ddname[+ xxx]] - ERROR CHANGING ALLOCATIO | JCL では起きない（装置・運用・システム） |  |
| IEF702I | jobname [procstep] stepname ddname [+ xxx] UNABLE TO ALLOCATE | テスト済み | マウントされていないボリューム |
| IEF703I | - jobname [procstep] stepname ddname[+ xxx] - NEW DATA SETS NOT ALLOWE | JCL では起きない（装置・運用・システム） |  |
| IEF704I | jobname [procstep] stepname ddname[+ xxx] - UNABLE TO ACCESS REQUIRED  | JCL では起きない（装置・運用・システム） |  |
| IEF705I | DIAGNOSTIC INFORMATION FOR UNSUCCESSFUL ALLOCATION DETECTED AT date ti | JCL では起きない（装置・運用・システム） |  |
| IEF706I | EDT BUILT FROM THIS IODF MAY CAUSE DEVICE ALLOCATION FAILURES ON RELEA | JCL では起きない（装置・運用・システム） |  |
| IEF707I | INTERNAL ALLOCATION ERROR description | 対象外: 入出力障害・システム内部エラー |  |
| IEF713I | jobname [procstep] stepname - MSS VOLUME NOT AVAILABLE | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF714I | jobname [procstep] stepname - MSS VOLUME NOT DEFINED | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF715I | jobname [procstep] stepname - MSS VOLUME INACCESSIBLE | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF716I | jobname [procstep] stepname - UNABLE TO MOUNT MSS VOLUME | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF717I | jobname [procstep] stepname - MSS VOLUME NOT MOUNTED. MSVGP NAME DOES  | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF718I | jobname [procstep] stepname - MSS VOLUME NOT MOUNTED. SPACE OR MSVGP R | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF719I | jobname [procstep] stepname ddname [+ xxx] - DATA SET PREVIOUSLY DEFIN | JCL では起きない（装置・運用・システム） |  |
| IEF720I | jobname [procstep] stepname ddname [+ xxx] - USER NOT AUTHORIZED TO DE | 対象外: 権限・TSO 固有 |  |
| IEF721I | jobname [procstep] stepname ddname [+ xxx] - PROTECTION CONFLICT IN IS | JCL では起きない（装置・運用・システム） |  |
| IEF722I | jobname - FAILED - text | JCL では起きない（装置・運用・システム） |  |
| IEF723E | ERROR OCCURRED IN ENF MODULE name | JCL では起きない（装置・運用・システム） |  |
| IEF724I | jobname [procstep] stepname ALLOCATION OF STEPCAT(S) FOR DISPOSITION P | JCL では起きない（装置・運用・システム） |  |
| IEF725I | jobname [procstep] stepname ddname [+ xxx] - MSS VOLUME SELECTION FAIL | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF726I | jobname [procstep] stepname ddname [+ xxx] - ALLOCATION REQUEST FAILUR | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| IEF729I | stmt STATEMENT IGNORED, NOT SUPPORTED FOR DYNAMIC UPDATE | JCL では起きない（装置・運用・システム） |  |
| IEF730I | INVALID REPLY SPECIFIED. | JCL では起きない（装置・運用・システム） |  |
| IEF731I | SCHEDxx LINE num: PPT STMT [FOR PGMNAME name] [IGNORED. / ACCEPTED.] R | JCL では起きない（装置・運用・システム） |  |
| IEF732I | SCHEDxx LINE num: DUPLICATE PPT STMT FOR PGMNAME name IGNORED. | JCL では起きない（装置・運用・システム） |  |
| IEF734I | SCHEDxx LINE num:[RESTART/NORESTART] [CODE cde/STATEMENT] [IGNORED/ACC | JCL では起きない（装置・運用・システム） |  |
| IEF735I | IEFSSNyy: PRIMARY IGNORED. PREVIOUSLY SPECIFIED IN IEFSSNzz | JCL では起きない（装置・運用・システム） |  |
| IEF736A | SPECIFY PRIMARY SUBSYSTEM NAME | JCL では起きない（装置・運用・システム） |  |
| IEF737I | IEFSSNxx LINE nnnn: KEYWORD keyword IGNORED. NOT RECOGNIZED. | JCL では起きない（装置・運用・システム） |  |
| IEF738I | mem LINE num:[RESTART/NORESTART] STMT IGNORED. NO OPERANDS SPECIFIED. | JCL では起きない（装置・運用・システム） |  |
| IEF740I | jobname [procstep] stepname ddname [+ xxx] - DATA SET/VOLUME COULD NOT | 対象外: 権限・TSO 固有 |  |
| IEF741I | jobname [procstep] stepname ddname[+ xxx] - PROTECT REQUEST FAILED - I | JCL では起きない（装置・運用・システム） |  |
| IEF742I | jobname [procstep] stepname - STEP IN ALLOCATION BEFORE SYSTEM RESTART | JCL では起きない（装置・運用・システム） |  |
| IEF743I | jobname FORCED - CODE SA22 - IN ADDRESS SPACE asid | JCL では起きない（装置・運用・システム） |  |
| IEF751I | jobname [procstep] stepname - JOB FAILED BY SUBSYSTEM | 対象外: サブシステムの状態に依存 |  |
| IEF752I | jobname [procstep] stepname ddname[+ xxx] - REQUEST FAILED BY SUBSYSTE | 対象外: サブシステムの状態に依存 |  |
| IEF753I | jobname [procstep] stepname ddname[+ xxx] - REQUEST FAILED SUBSYSTEM D | 対象外: サブシステムの状態に依存 |  |
| IEF754I | jobname [procstep] stepname ddname [+ xxx] - REQUEST FAILED SUBSYSTEM  | 対象外: サブシステムの状態に依存 |  |
| IEF755I | jobname [procstep] stepname ddname[+ xxx] - REQUEST FAILED SUBSYSTEM D | 対象外: サブシステムの状態に依存 |  |
| IEF756I | jobname [procstep] stepname ddname[+ xxx] - REQUEST FAILED SYSTEM ERRO | 対象外: サブシステムの状態に依存 |  |
| IEF757I | ILLEGAL DATA SET NAME ON DD STATEMENT | JCL では起きない（装置・運用・システム） |  |
| IEF758I | SUBSYSTEM AVAILABILITY LIMITED text | JCL では起きない（装置・運用・システム） |  |
| IEF759I | [xxxx] SUBSYSTEM UNAVAILABLE, text | JCL では起きない（装置・運用・システム） |  |
| IEF760I | ERROR IN memname, CODE=yyyrc incorrect-record | JCL では起きない（装置・運用・システム） |  |
| IEF761I | jobname [procstep] stepname ddname callername DD IS ALREADY ALLOCATED  | JCL では起きない（装置・運用・システム） |  |
| IEF764I | jobname [procstep] stepname ddname callername PARMLIB READ FAILED - ME | JCL では起きない（装置・運用・システム） |  |
| IEF765I | jobname [procstep] stepname ddname callername PARMLIB READ FAILED FOR  | JCL では起きない（装置・運用・システム） |  |
| IEF766I | jobname [procstep] stepname ddname callername PARMLIB READ FAILED FOR  | JCL では起きない（装置・運用・システム） |  |
| IEF767I | jobname [procstep] stepname ddname callername ALLOCATE FAILED FOR dsna | JCL では起きない（装置・運用・システム） |  |
| IEF768I | jobname [procstep] stepname ddname callername CONCATENATION OF THE LOG | JCL では起きない（装置・運用・システム） |  |
| IEF769I | jobname [procstep] stepname callername LOADING OF THE PARMLIB READ ROU | JCL では起きない（装置・運用・システム） |  |
| IEF770I | jobname [procstep] stepname ddname callername UNABLE TO ACCESS THE LOG | JCL では起きない（装置・運用・システム） |  |
| IEF771I | dev [PENDING] OFFLINE - {ASSIGNED TO ANOTHER SYSTEM/ ASSIGN FAILED, RE | JCL では起きない（装置・運用・システム） |  |
| IEF772I | dev PENDING OFFLINE - MUST BE VARIED OFFLINE TO JES3 | JCL では起きない（装置・運用・システム） |  |
| IEF773I | TIOT SIZE = xxxxK, MAXIMUM SINGLE UNIT DD ENTRIES = zzzzzzzz | JCL では起きない（装置・運用・システム） |  |
| IEF775I | jobname [procstep] stepname ddname callername UNALLOCATION OF THE LOGI | JCL では起きない（装置・運用・システム） |  |
| IEF776I | jobname [procstep] stepname ddname callername UNALLOCATION OF THE LOGI | JCL では起きない（装置・運用・システム） |  |
| IEF777I | jobname [procstep] stepname ddname callername PARMLIB READ ROUTINE REC | JCL では起きない（装置・運用・システム） |  |
| IEF778I | FURTHER INFORMATION NOT PROVIDED BY SUBSYSTEM ssnm | JCL では起きない（装置・運用・システム） |  |
| IEF779I | dddd, VOLUME vvvvvv PENDING OFFLINE BY callerid | JCL では起きない（装置・運用・システム） |  |
| IEF781I | jobname [procstep] stepname callername LIST BUFFER INPUT TO LOGICAL PA | JCL では起きない（装置・運用・システム） |  |
| IEF783I | jobname [procstep] stepname callername READ BUFFER INPUT TO LOGICAL PA | JCL では起きない（装置・運用・システム） |  |
| IEF786I | ERROR VERIFYING INTERNAL VOLUME LABEL ser ON DEVICE dev | JCL では起きない（装置・運用・システム） |  |
| IEF787I | jobname stepname - ERROR VERIFYING INTERNAL LABEL OF VOLUME ser ON DEV | JCL では起きない（装置・運用・システム） |  |
| IEF788I | jobname stepname - ERROR VERIFYING INTERNAL LABEL OF VOLUME ser ON DEV | JCL では起きない（装置・運用・システム） |  |
| IEF789I | jobname stepname - ERROR VERIFYING INTERNAL LABEL OF VOLUME ser ON DEV | JCL では起きない（装置・運用・システム） |  |
| IEF790I | jobname stepname - ERROR VERIFYING INTERNAL LABEL OF VOLUME ser ON DEV | JCL では起きない（装置・運用・システム） |  |
| IEF791I | jobname stepname - ERROR VERIFYING INTERNAL LABEL ser ON DEVICE dev. | JCL では起きない（装置・運用・システム） |  |
| IEF811I | DUPLICATE VERB AND LABEL text | JCL では起きない（装置・運用・システム） |  |
| IEF812I | JCL USAGE LIMITED - SYSTEM ERROR | 対象外: 入出力障害・システム内部エラー |  |
| IEF815I | INVALID HEXADECIMAL VALUE IN THE parameter FIELD | 対象外: マニュアルから発生条件を特定できない |  |
| IEF817I | PARAMETER LENGTH LESS THAN MINIMUM ALLOWED IN THE parameter FIELD | 対象外: マニュアルから発生条件を特定できない |  |
| IEF818E | JCL USAGE LIMITED - text | 対象外: 入出力障害・システム内部エラー |  |
| IEF819I | EXCESSIVE NUMBER OF POSITIONAL PARAMETERS IN SUBPARAMETER LIST IN THE  | 対象外: マニュアルから発生条件を特定できない |  |
| IEF820I | SPECIFIED NUMERIC LESS THAN MINIMUM ALLOWED IN THE parameter FIELD | 対象外: マニュアルから発生条件を特定できない |  |
| IEF823I | NUMBER OF LEVELS EXCEEDS MAXIMUM IN THE parameter FIELD | 対象外: マニュアルから発生条件を特定できない |  |
| IEF824I | LENGTH OF LEVEL xx EXCEEDS yy IN THE parameter FIELD | テスト済み | データセット名の修飾子が9文字（確度:低） |
| IEF825I | INVALID CHARACTER IN THE parameter FIELD | テスト済み | データセット名の修飾子が数字で始まる（確度:低） |
| IEF861I | FOLLOWING RESERVED DATA SET NAMES UNAVAILABLE TO jobname | 対象外: HSM による再呼び出し・データセットの競合 |  |
| IEF863I | DSN=dsname jobname RC=returncodeRSN=reasoncode FROM SERVICE servicenam | JCL では起きない（装置・運用・システム） |  |
| IEF864I | DATA SET dsname ALREADY IN USE | 対象外: HSM による再呼び出し・データセットの競合 |  |
| IEF874I | jjj proc sss ddname ALLC_OFFLN EXIT CHOSE "BRING DEVICE ONLINE" WITHOU | JCL では起きない（装置・運用・システム） |  |
| IEF875I | jobname [procstep] stepname ddname[+ xxx] ALLOC_OFFLN EXIT CHOSE "ISSU | JCL では起きない（装置・運用・システム） |  |
| IEF876I | jobname [procstep] stepname JOB CANCELLED BY {VOLUME_ENQ} INSTALLATION | JCL では起きない（装置・運用・システム） |  |
| IEF877E | jobname NEEDS xxx UNIT(S) FOR stepname procname ddname[ +zzz] [[FOR VO | JCL では起きない（装置・運用・システム） |  |
| IEF878I | END OF IEF877E FOR jobname stepname procname ddname [+zzz .] | JCL では起きない（装置・運用・システム） |  |
| IEF879I | dddd PENDING OFFLINE BY callerid | JCL では起きない（装置・運用・システム） |  |
| IEF880I | dddd NOW OFFLINE BY callerid [-DEVICE IS BOXED] | JCL では起きない（装置・運用・システム） |  |
| IEF881I | cmd COMMAND FOR DEVICE devn FAILED - ABEND abcd, REASON rsn | JCL では起きない（装置・運用・システム） |  |
| IEF882E | jobname [procstep] stepname IS WAITING FOR A REPLY TO pmsgid | JCL では起きない（装置・運用・システム） |  |
| IEF883E | jobname [procstep] stepname IS WAITING FOR DEVICE(S) WHILE HOLDING SYS | JCL では起きない（装置・運用・システム） |  |
| IEF893I | CONCATENATE REQUEST FAILED - CORRESPONDING DSABS RESIDE IN BOTH ABOVE  | JCL では起きない（装置・運用・システム） |  |
| IEF894I | COMPONENT TRACE PARMLIB OPTION optname IS NOT VALID. | JCL では起きない（装置・運用・システム） |  |
| IEF895I | SYSIEFAL CTRACE DEFINITION FAILED. RC = rc, RSN = rsn. | JCL では起きない（装置・運用・システム） |  |
| IEF896I | UNABLE TO OBTAIN SYSIEFAL CTRACE BUFFER MAXIMUM SIZE OF hexnum BYTES | JCL では起きない（装置・運用・システム） |  |
| IEF897I | SYSIEFAL CTRACE DEFINITION FAILED USING CTIIEFAL. RC = rc, RSN = rsn. | JCL では起きない（装置・運用・システム） |  |
| IEF898I | jobname stepname procstep ddname [+ xxx] FAILED TO ALLOCATE SPECIFIED  | JCL では起きない（装置・運用・システム） |  |
| IEF900I | SYSTEM SYMBOLS WERE UPDATED FROM memname | JCL では起きない（装置・運用・システム） |  |
| IEF901I | SYSTEM SYMBOLS WERE NOT UPDATED FROM memname. text | JCL では起きない（装置・運用・システム） |  |
| IEF910I | PARMDD DATA SET UNUSABLE. | テスト済み | PARMDD がメンバーなしの PDS |
| IEF911I | EXCESSIVE USER PARAMETER STRING LENGTH. | 対象外: マニュアルから発生条件を特定できない |  |
| IEF990I | CANNOT DETERMINE VOLUME CORRESPONDING TO DEVICE sdddd | JCL では起きない（装置・運用・システム） |  |

## JES2（JCL に関係するもの）

| ID | 文面 | 分類 | テスト内容 |
|---|---|---|---|
| $HASP107 |  | テスト済み | DLM の値が2文字でない（確度:低） |
| $HASP108 |  | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
| $HASP109 |  | 対象外: システム出口（IEFUJV など） |  |
| $HASP110 |  | テスト済み | JOB 文に SYSTEM と SYSAFF の両方 |
| $HASP111 |  | テスト済み | /*ROUTE に PRINT/PUNCH/XEQ がない<br>/*ROUTE の宛先が無効 |
| $HASP112 |  | テスト済み | /*JOBPARM の値が無効<br>/*JOBPARM に知らない位置パラメーター |
| $HASP113 |  | テスト済み | /*OUTPUT の COPIES が大きすぎる |
| $HASP114 |  | テスト済み | /*XEQ のノードが存在しない |
| $HASP116 |  | テスト済み | /*NOTIFY のユーザー ID が8文字を超える（確度:低） |
| $HASP118 |  | テスト済み | 知らない JES2 制御文 |
| $HASP139 |  | 対象外: システム出口（IEFUJV など） |  |
| $HASP146 |  | 対象外: マニュアルから発生条件を特定できない |  |
| $HASP165 |  | 情報メッセージ（シミュレーターが出力） |  |
| $HASP373 |  | テスト済み | 正常終了（情報） |
| $HASP375 |  | 情報メッセージ（シミュレーターが出力） |  |
| $HASP395 |  | 情報メッセージ（シミュレーターが出力） |  |
| $HASP396 |  | 情報メッセージ（シミュレーターが出力） |  |
| $HASP890 |  | 情報メッセージ（シミュレーターが出力） |  |
| $HASP1110 |  | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
| $HASP1111 |  | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
| $HASP1112 |  | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
| $HASP1114 |  | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
| $HASP1115 |  | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
| $HASP1116 |  | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
| $HASP1117 |  | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
| $HASP1118 |  | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
| $HASP1120 |  | 対象外: マニュアルから発生条件を特定できない |  |
| $HASP1132 |  | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| $HASP1133 |  | 対象外: ISAM・テープ装置・MSS・JES3（このシミュレーターにない機能） |  |
| $HASP6175 |  | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
| $HASP6176 |  | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
| $HASP6177 |  | 対象外: ジョブグループ・NJE 転送（このシミュレーターにない機能） |  |
