---
type: concept
aliases: [磷酸肌酸再合成, PCr再合成, PCr resynthesis, phosphocreatine resynthesis, PCr recovery, PCr回補, 磷酸肌酸恢復, PCr resynthesis kinetics, PCr再合成動力學, PCr recovery kinetics]
tags: [exercise-physiology, metabolism, recovery, mechanism]
sources: [source-Kemp-1993-PCr-resynthesis-control, source-McMahon-2002-PCr-resynthesis, source-Korzeniewski-2013-VO2-PCr-off-kinetics]
prerequisites: [磷酸肌酸（phosphocreatine, PCr）, 粒線體呼吸控制（mitochondrial respiratory control）, 無機磷酸（inorganic phosphate, Pi）, 時間常數（exponential time constant, τ）, 肌酸激酶平衡（creatine kinase equilibrium）, 細胞內 pH（intracellular pH, pHi）]
created: 2026-06-11
updated: 2026-06-12
---

# 磷酸肌酸再合成（phosphocreatine resynthesis, PCr resynthesis）

## 本質（一句話）
PCr 再合成就是「運動把磷酸肌酸這桶救急燃料用掉之後，身體在恢復期把它重新充回來」的過程——而它有三個漂亮的性質：**它純靠有氧**、**它補回的速度正比於『還缺多少』所以走指數曲線**、而且**它補得多快，直接就是這塊肌肉粒線體功能的成績單**。（這個乾淨的單指數是「肌肉沒太酸」時的樣子；一旦運動夠猛、肌肉顯著變酸，補回會裂成「先快後慢」兩段——慢的那段被酸卡住，見推導第 8 點。）

## 前置概念
- [[Phosphocreatine|磷酸肌酸（phosphocreatine, PCr）]]
  （要懂「補回 PCr」，先懂 PCr 是什麼：肌肉的瞬間 ATP 補充包，用掉時 PCr↓、Pi↑。本頁是它的「充電」那一面。）
- [[Mitochondrial respiratory control|粒線體呼吸控制（mitochondrial respiratory control）]]
  （補 PCr 的速率＝粒線體做 ATP 的速率，而那由 ADP 訊號飽和式地驅動；本頁是這條控制律最乾淨的一個應用場景。）
- [[Inorganic phosphate|無機磷酸（inorganic phosphate, Pi）]]
  （PCr 缺多少，就對應 Pi 高多少；下面「速率正比於缺口」用的就是這條鏡像。）
- [[Time constant|時間常數（exponential time constant, τ）]]
  （「補得多快」用 τ 量化；本頁會推出「為什麼 PCr 恢復是指數、能用單一 τ 描述」。）

## 為什麼會這樣（first-principles 推導）
一步一步來，每步只用前面已建立的事實：

1. **先把場景設乾淨。** 運動一停、進入恢復期，三件事同時成立：不再做機械功、[ATP] 維持恆定、而且醣解（無氧產酸那條路）也停了。於是這段時間裡，肌肉內**唯一**在補 ATP 的就是粒線體的有氧氧化。把多出來的氧化 ATP 拿去做一件事：透過肌酸激酶把 ADP 充回 ATP、同時把 PCr 重新合成回來。**所以「PCr 補回的速率 R」就等於「淨氧化 ATP 合成的速率」**——這是個運氣很好的乾淨等式：恢復期把所有干擾項都關掉了，PCr 的補回速度成了直接量「粒線體此刻做了多少 ATP」的窗口。

2. **這就是為什麼說「補 PCr 是純有氧的」。** 用 PCr（放電）不需氧，但補 PCr（充電）這一步，在恢復期被證明完全由有氧氧化買單。所以**間歇運動能一次次重新動用 PCr，前提是恢復段有足夠的有氧供應**——這條是 [[W prime reconstitution|W′ 回填]] 快段的生理地基。

3. **核心一步：為什麼 PCr 恢復是『指數曲線』？放慢講。** 由 [[Mitochondrial respiratory control|呼吸控制]]：氧化 ATP 合成速率（也就是 R）跟著「能量缺口的訊號」走。恢復一開始 PCr 掉得最多（Pi 升得最高、缺口最大），訊號最強，所以**補得最猛**；隨著 PCr 一點點補回、缺口變小，訊號減弱，**補的速度也跟著慢下來**；補到接近滿，缺口趨近零，速度也趨近零。把這句話寫成一條規律就是：**補回速率 ∝ 還缺多少**。而「變化速率正比於離終點還差多少」這件事，數學上**就是**一階動力學（first-order kinetics），它的解必然是一條**指數逼近曲線**——一開始陡、後來緩、平順貼近最終值，用單一個 [[Time constant|時間常數 τ]] 就能描述。**所以「PCr 恢復是單指數、能講『PCr 再合成的 τ』」不是巧合，是『速率正比於缺口』直接逼出來的結果。**

4. **把上一步接到實際數字。** 本文獻在人前臂屈指淺肌用 ³¹P-MRS 量到：補回速率 R 對 [Pi]（＝缺口的量尺）近乎**直線**（斜率約 0.8/分），對 [ADP] 呈**雙曲線**（Km≈30 μmol/L、Vmax≈40 mmol/L 細胞水/分）。線性對 Pi 正是第 3 步「速率∝缺口」的實測版；它撐起了「PCr 單指數恢復」。實測 PCr 的半回復時間（half-time）約 0.9 分（≈54 秒，前臂），其他肌群文獻量到 τ 約 25–29 秒（小腿、股外側肌）——量級一致，差異來自肌群與方法。

5. **那條 Vmax 是『有氧機能的成績單』。** 第 4 點的 Vmax（補 PCr 的最高速率）就是這塊肌肉的粒線體產能上限。所以「PCr 補得快」≈「粒線體多／健康」≈「有氧機能好」。這不是空話——本文獻拿**粒線體疾病（mitochondrial myopathy）**患者對照：他們的 R 全程都被壓低，正是因為粒線體產能（Vmax）受損。換句話說，**PCr 再合成速率被當成一個非侵入的『活體粒線體功能檢測』**，這也是這條研究線的臨床價值所在。

6. **兩個會把它拖慢的東西（接到 wiki 既有張力）：**
   - **酸（低 pH）會拖慢 PCr 再合成。** 文獻明指低 pH 與 ATP 耗竭都會顯著降低 PCr 恢復速率。這替「反覆力竭→肌肉變酸→回填變慢」給了肌內機制（但注意 [[W prime reconstitution|W′ 回填]] 推導第 6 點與 [[Bi-exponential W prime reconstitution model|雙指數模型]] 的細緻修正：反覆力竭拖慢的主要是**慢段（清酸）**、而非快段 PCr 本身——兩者要分清）。
   - **粒線體容量本身**（Vmax）：見第 5 點，這是個體與疾病差異的根。

7. **把它放回 wiki 的兩個位置（這是本頁的價值所在）：**
   - **它是 [[W prime reconstitution|W′ 回填]] 快段（FC）的底料。** W′ 回填的快段 τ（≈15–40 s）與 PCr 再合成 τ 吻合，「FC≈PCr」這個對應就建立在本頁的機制上。但要記 [[Oxidative reserve|氧化儲備]] 與 [[W prime reconstitution]] 的分寸：W′ 跟 PCr 綁定的是「有氧可用**空間**（D_[PCr]）」這個容量差（r=0.99），不是補回**速度**（τ_[PCr] 與 τ_W′ 其實不相關）——「快段＝PCr」要在這個 nuance 下理解。
   - **它是 [[Oxygen debt|氧債]]「還債」的主要工作之一。** 運動後多吸的那份氧，相當部分就是拿去跑這個有氧的 PCr 再合成（把開頭 [[O2 deficit|氧虧]] 時向 PCr 借的還回來）。所以氧債之所以是「有氧的、需要時間的」，根在這裡。

8. **再補一層（強度高時）：恢復其實會裂成「快段＋慢段」兩段。** 第 3 點那條乾淨的單指數，是「肌肉沒太酸」時的樣子（Kemp 用的多是中等強度、pH 掉得少）。但 McMahon & Jenkins 盤點更廣的文獻指出：當運動**夠劇烈、pHi 顯著下降**時，PCr 恢復**不再是單一指數**，而裂成兩段（Harris 等：快段 t½≈21 秒、慢段 t½>170 秒）：
   - **快段**：由有氧／[ADP] 控制、**對酸免疫**。證據：把兩組末端 pH 差到 0.59 單位，初始恢復速率仍相同（Walter）；初速與末端 pH 無關（Roussell）。
   - **慢段**：被 **pHi 的恢復**限速。機制就在 [[Creatine kinase equilibrium|CK 平衡]]——補 PCr 會放出 H⁺，肌肉已經很酸就反過來卡住「再多補 PCr」（終產物抑制），而酸退得很慢（十幾分鐘，見 [[Intracellular pH|pHi]]）。
   - **為什麼是「快段先、慢段後」**：恢復前段 [ADP] 快速回落（約 1 分鐘就回靜息），快段被催完；酸退得慢，要到後段才成為瓶頸。所以「先快後慢」不是兩台機器，而是同一個過程在「ADP 先退、酸後退」這個時間差下的兩個面貌。

9. **一個重要的方法學陷阱（解釋了文獻數字為何亂飄）：** 如果硬用「單指數＋一個 τ」去套一個其實**雙段**的恢復，得到的 τ 會落在快、慢之間，而且**取決於你監測多久**——監測愈久，τ 愈偏向慢段、數字愈大（Harris 的洞見）。例：Bogdanis 用單指數、監測 6 分鐘，得 t½＝56 秒，正好卡在快 21／慢 >170 之間。再加 [[Phosphorus-31 magnetic resonance spectroscopy|³¹P-MRS]] 的時間解析度限制（Newcomer 用 0.5 秒解析度發現連雙指數都可能低估初速 56%），所以引用「PCr 再合成的 τ」一定要問清楚：**什麼運動強度（pH 掉多少）、監測多久、什麼解析度**——否則數字不可比。這也回頭限定了第 3 點的單指數圖像：它只在「pH 不顯著下降」時精確。

10. **再補一個上游決定因子（電腦模型視角，接 Korzeniewski 2013）：** 除了 ADP（快段）與 pH（慢段），「補 PCr 補得多快」還受一個更上游的旋鈕牽動——運動後**前饋活化退場的速度** [[Parallel activation of oxidative phosphorylation|τ(OFF)]]。直覺反而是反的：τ(OFF) 愈**大**（運動停了粒線體還高速運轉愈久），PCr 反而補得愈**快**（殘餘有氧產能持續供應）。這也把 PCr 再合成與恢復期 VO2 怎麼降綁成**反向**耦合（[[Inverse VO2-PCr off-kinetics relationship|反向關係]]）；τ(OFF) 大到一定程度，PCr 還會被推過靜息值（[[Phosphocreatine recovery overshoot|PCr 過衝]]）。注意這是 in silico 預測、半定量，與第 3–9 點的實測機制互補而非取代。

## 文獻怎麼說 vs 為什麼這樣說
- **主張**：恢復期的 PCr 再合成速率 R 是「淨氧化 ATP 合成速率」的活體估計；它對 [ADP] 呈雙曲線（受 [[Mitochondrial respiratory control|ADP 動力學控制]]）、對 [Pi]/[PCr] 近乎線性（故 PCr 恢復近單指數）；R 的上限反映粒線體容量，在粒線體疾病中下降。
- **背後的推理／證據**：(1) 恢復期「無功、ATP 恆定、醣解已停」這三條，使 R 能乾淨地等同於氧化 ATP 合成（不被收縮耗能與受質層次磷酸化污染）；(2) ³¹P-MRS 實測 R-對-[ADP] 雙曲線（Hanes 圖回歸 r=0.88、Km≈30、Vmax≈40）、R-對-[Pi] 線性（斜率≈0.8/min）；(3) 一個關鍵的內部一致性：PCr 的半回復時間（≈0.9 min）約是 ADP 的（≈15 s）三倍——這個倍數關係本身，數學上就「逼出」R-對-[ADP] 必為雙曲線；(4) 粒線體肌病患者 R 全程下降且 R-對-[ADP] 近乎線性（表觀 Km 升高），與「Vmax＝粒線體容量」一致。

## 易誤解之處
1. **「用 PCr」不需氧，但「補 PCr」一定要氧。** 這兩件事方向相反、最容易混。放電（供能那一瞬）是無氧的瞬間反應；充電（恢復期補回）是有氧的、要花時間的氧化過程。所以一個人「能不能反覆衝刺」很大程度看他**恢復段的有氧供應**夠不夠把 PCr 充回來。
2. **PCr 恢復的『指數形狀』不是經驗湊出來的曲線，是『速率∝缺口』的必然結果。** 先有「補得多快取決於還缺多少」這條物理（呼吸控制），才有「單指數＋一個 τ」這個數學形狀。把因果倒過來（以為先有指數公式、再去解釋）會錯失重點：τ 之所以存在，是因為粒線體被缺口訊號牽著走。
3. **PCr 再合成的『速度』≠ [[W prime|W′]] 回填的『速度』。** PCr 補得快（t½≈39–54 s），W′ 補得慢得多（t½≈232 s），兩者 τ 不相關（Skiba 2015）。所以別把「W′ 以 PCr 的速度回來」當真——PCr 撐起的是 W′ 回填的**快段**與**容量差（[[Oxidative reserve|氧化儲備]]）**，不是整桶 W′ 的回補速率（詳見 [[W prime reconstitution]] 易誤解 #11）。
4. **R 是『淨』氧化合成、且這個乾淨等式只在恢復期成立。** 在**運動當下**，PCr 同時被「用掉（供能）」和「補回（氧化）」兩股相反的流攪在一起，無法乾淨地把 R 讀成氧化速率；只有運動一停、供能那股關掉，R 才等於純氧化合成。這也是為什麼研究「粒線體功能」要看**恢復期**的 PCr 動力學，而不是運動中的。
5. **「PCr 恢復是單指數」只在『肌肉沒太酸』時精確；劇烈運動會讓它變雙相。** 第 3 點的乾淨單指數（Kemp，中等強度）與「intense 時雙相」（McMahon & Jenkins）**不矛盾**——是同一機制在不同 pH 跌幅下的兩種樣子：pH 不太掉時只看得到快段（近單指數），pH 大跌時慢段現身（雙指數）。所以看到「PCr 是單指數」與「PCr 是雙指數」兩種說法，先問那篇的**運動強度**與 **end-exercise pH**，多半就化解了。

## 用生活例子再講一次
接續 [[Phosphocreatine|PCr]] 那頁的「相機閃光燈電容」類比：閃光燈電容放完電後，要靠主電池**透過一個電阻慢慢充回來**——而充電的電流會隨「電容還差多少電」自動變化：剛放完電時電壓差最大、充得最猛，愈充愈滿、電流愈小，平順地逼近滿格。這條「先快後慢、趨近滿格」的充電曲線，物理上就是一條指數（RC 充電曲線）——**而 PCr 補回來，走的就是同一種曲線、同樣是「缺愈多補愈快」**。充電的最大電流由主電池能給多少決定（＝粒線體容量 Vmax），主電池弱（粒線體病），整條充電就慢。

（這個類比在哪裡會失準：電容充電的快慢由固定的電阻與電池決定，環境不太影響；PCr 再合成的速度卻會被**肌肉變酸（低 pH）**額外拖慢——電容不會「因為剛剛放電太多次、環境變酸」就變得更難充，PCr 會。）

## 換句話說
換句話說，磷酸肌酸再合成是「恢復期把用掉的 PCr 用有氧方式充回來」的過程。因為恢復期沒有功、ATP 恆定、醣解已停，PCr 補回的速率就乾淨地等於粒線體做 ATP 的速率；而由 [[Mitochondrial respiratory control|呼吸控制]]，這個速率正比於「還缺多少（Pi 多高）」，於是 PCr 恢復是一條先快後慢、用單一 [[Time constant|τ]] 描述的指數曲線。它補得多快，封頂在粒線體容量（Vmax），所以成了量活體有氧機能的窗口（粒線體病時下降）；酸會把它拖慢。把它放回大圖：它是 [[W prime reconstitution|W′ 回填]] 快段與 [[Oxygen debt|氧債]] 還債的肌內地基。（補一句分寸：這條乾淨的單指數是 pH 沒太掉時的樣子；運動一劇烈、肌肉顯著變酸，恢復就裂成快段（有氧／ADP 控制、不怕酸）＋慢段（被 [[Intracellular pH|pHi]] 恢復經 [[Creatine kinase equilibrium|CK 平衡]] 限速）兩段——這也是為什麼引用「PCr 的 τ」要連帶說明強度與監測時長。）

## 來源
- [[source-Kemp-1993-PCr-resynthesis-control]]（全篇：恢復期「無功、ATP 恆定、醣解已停」使 PCr 再合成速率 R＝淨氧化 ATP 合成速率（高於 0.8 mmol/L/min 的基礎值）；R 對 [ADP] 雙曲線（Km≈30 μmol/L、Vmax≈40 mmol/L 細胞水/min、Hanes 回歸 r=0.88）、對 [Pi] 線性（斜率≈0.8/min）；PCr 半回復≈0.9 min、ADP≈15 s，PCr t½≈3×ADP t½ 為「雙曲線」的數學根源；低 pH 與 ATP 耗竭降低 R；粒線體肌病 R 全程下降、表觀 Km 升高，佐證 Vmax＝粒線體容量。其他肌群 τ≈25–29 s 為對照文獻值。）
- [[source-McMahon-2002-PCr-resynthesis]]（第 5、6、7 節：強度高、pHi 顯著下降時 PCr 恢復為**雙相**（Harris 快段 t½≈21 s／慢段 t½>170 s），pH 不顯著下降時近單指數（Mahler、Meyer）；快段由有氧／[ADP] 控制、對酸免疫（Walter 兩組差 0.59 pH 單位初速相同；Roussell 初速與末端 pH 無關），慢段被 pHi 恢復經 CK 平衡限速（Bendahan r=0.90、Lodi r=0.89、Takahashi severe/exhaustive r=−0.71/−0.83）；單指數硬套雙段恢復使 τ 隨監測時長而偏移（Bogdanis 6 min 單指數 t½=56 s 落在快慢之間）；Newcomer 0.5 s 解析度顯示初速被低估達 56%。）
- [[source-Korzeniewski-2013-VO2-PCr-off-kinetics]]（推導第 10 點：電腦模型顯示恢復期前饋活化衰減時間 τ(OFF) 共決 PCr off 速率——τ(OFF)↑ 使 PCr 補得**更快**（中等運動 τ(OFF) 0→1000 s 時 PCr t₀.₆₃(off) 174→23 s）、並與 VO2 off 反向耦合、τ(OFF) 夠大時出現 PCr 過衝；in silico、半定量。）
