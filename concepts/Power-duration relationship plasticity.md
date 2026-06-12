---
type: concept
aliases: [功率-持續時間關係的可塑性, 功率–持續時間關係的可塑性, CP 可塑性, CP 耐久性, power-duration relationship plasticity, dynamic power-duration relationship, CP durability, durability, plasticity of CP and W prime, CP 漂移]
tags: [exercise-physiology, critical-power, fatigue, modelling, performance]
sources: [source-Black-2023-dynamic-power-duration, source-Sreedhara-2020-recovery-W-prime-domain, source-Jones-2023-physiological-resilience, source-Skiba-Clarke-2021-W-prime-balance-mathematics, source-Goulding-2023-priming-VO2-kinetics]
prerequisites: [臨界功率／臨界速度（critical power / critical speed, CP/CS）, W prime, 三分鐘全力測試（3-minute all-out test）, Phosphocreatine, Inorganic phosphate, Muscle fiber types]
created: 2026-06-11
updated: 2026-06-11
---

# 功率–持續時間關係的可塑性（plasticity / durability of the power–duration relationship）

## 本質（一句話）
平常我們把 [[Critical power|臨界功率（CP）]] 和 [[W prime|W′]] 當成一個人「固定的兩個數」——但其實它們不是鐵打的：**只要你先前剛做過一段把自己榨乾的劇烈運動，整條功率–持續時間雙曲線就會被往左下推（CP 略降、W′ 大降）**，也就是「你此刻有多累」會改變你接下來「能撐多高、撐多久」。

## 前置概念
- [[Critical power|臨界功率（critical power, CP）]]
  （這頁講的就是「CP 會不會變」；先懂 CP 在新鮮狀態下是什麼、代表什麼。）
- [[W prime|W′（臨界功率以上的有限功容量）]]
  （另一個會漂移的參數；先懂這桶有限備用功是什麼。）
- [[3-minute all-out test|三分鐘全力測試（3MT）]]
  （本頁的證據全靠它：3MT 末段功率＝EP≈CP、前段多做的功＝WEP≈W′，用一次測試把兩個參數同時量出來。）
- [[Phosphocreatine|磷酸肌酸（PCr）]]、[[Inorganic phosphate|無機磷酸（Pi）]]
  （CP/W′ 被壓低的肌肉內機制，主角就是 PCr 耗竭、Pi 升高、pH 下降這組疲勞代謝物。）
- [[Muscle fiber types|肌纖維類型與運動單位招募]]
  （為什麼「全力衝刺」比「固定功率」更會壓低 CP，關鍵在兩者招募纖維的方式不同。）

## 為什麼會這樣（first-principles 推導）
一步一步來，每步只用前面已建立的事實或常識：

1. 先點出一個被默默接受的假設。所有 [[W prime balance model|W′ 平衡模型]]（拿來即時算「W′ 還剩多少」、據此配速）都建立在一條地基上：**CP 是常數，整場運動從頭到尾不變**。消耗端（超 CP 以 P−CP 速率扣 W′）和回填端（降回 CP 以下才補）都靠「CP 這條線固定不動」才算得出來。如果 CP 會漂，整套帳就要重算。

2. 但這條地基其實沒那麼穩。回憶 [[Critical power|CP]] 那頁的深層結論：CP 不是寫死的基本設定，而是有氧能力的**湧現性質**——它由「氧氣送到、滲入、被粒線體用掉的速度」與「肌內 [[Inorganic phosphate|Pi]] 何時累積到臨界水準」共同決定。既然 CP 是這些可變因素湧現出來的結果，就沒有理由相信它在一場會改變肌肉內環境的運動裡，會始終停在同一個數。問題只剩：**實際上它變不變、變多少？**

3. 怎麼直接量？用**重複 3MT**。流程是：先做第一個 3MT（休息態，C-3MT＝control），量到 EP（末 30 秒平均功率，≈CP）與 WEP（高出 EP 的那塊功，≈W′）；只休息 1 分鐘；再做第二個 3MT（疲勞態，F-3MT＝fatigued），量同樣的 EP 與 WEP。比較兩次的 EP 與 WEP，就能看出「先前榨乾一次」之後，CP 與 W′ 各自動了多少。

4. 結果很清楚（Black 等 2023，12 筆資料）：
   - **EP（≈CP）降了 7%**：282 W → 263 W（p<0.001）。
   - **WEP（≈W′）降了 61%**：16.9 kJ → 6.3 kJ（p<0.001）。
   - 整段功率曲線在 F-3MT 起點更低、末段平台也更低——整條雙曲線**往左下平移**。

5. WEP 大降 61% 本身不算意外：第一個 3MT 已經把 W′ 整桶燒乾，中間只休 1 分鐘，依 [[W prime reconstitution|回填動力學]] 大約只補回約 39%，所以第二次能榨出的 W′ 自然少很多。**真正的新發現是 EP 也降了 7%**——也就是連 CP 這個「可持續輸出的天花板」本身都被先前的運動壓低了。這正面動搖了「CP 是常數」的假設。

6. 機制：為什麼一段全力運動之後，CP 與 W′ 會被壓低？分兩條線講。
   - **肌肉內代謝環境惡化（壓低輸出）**：全力 3MT 把肌肉裡的 [[Phosphocreatine|PCr]] 大量耗掉、H⁺（酸）累積使 pH 下降、[[Inorganic phosphate|Pi]] 升高。這組變化會損害**興奮–收縮耦合**（excitation–contraction coupling，意思是「肌肉收到神經電訊號」到「肌纖維真的產生張力」之間那一連串傳遞——酸與高 Pi 會卡住這個傳遞）。耦合變差 → 同樣的功率要燒更多氧（每瓦耗氧上升，本研究實測 F-3MT 的末段 VO₂ gain 確實較高）→ 可持續的最高輸出（CP）因而下降。
   - **招募模式的差別（為什麼是「全力」才壓低 CP）**：這是本頁最關鍵、也最容易被忽略的一步。
     - 在**固定功率（CWR）**運動裡，運動單位是**漸進招募**的：一開始用 Type I（耐久、靠氧）為主，隨疲勞才陸續補進 Type II（爆發、偏醣解、容易累、恢復慢）。
     - 在**全力（all-out）**運動裡，招募是「反過來」的：從第一秒就把所有能用的（task-specific）運動單位**全部招募**，包括大量 Type II。
     - 後果：全力運動讓 Type II 纖維承受巨大、即刻的代謝衝擊，產生深度疲勞；而 Type II 恢復又特別慢。於是只休 1 分鐘後，這批纖維還沒回神，第二次能輸出的可持續功率（CP）與能榨出的 W′ 都跟著掉。
   - **對照證據（很有說服力）**：Ferguson 等（2010）發現，做**固定功率**的劇烈運動到力竭，事後 **W′ 降、但 CP 不變**。同樣是力竭，CWR 不壓 CP、all-out 卻壓 CP——差別正落在招募模式上，這反過來坐實了「是 Type II 的全面即刻招募在壓低 CP」。（另一條路：長達 2 小時的**重度固定功率**運動也會降 CP 約 9%，但那條路與**肌糖原耗竭**相關、補糖可緩解（Clark 2019）；3MT 太短、糖原沒怎麼耗，所以走的是上面 PCr/Pi/pH 那條。同一個 CP 下降，可由不同機制造成。）

7. 對 W′ 平衡模型的後果（這才是為什麼要在意）。既然真實的 CP/W′ 在疲勞下會漂、而模型假設它們不動，模型就會在「先前已大量消耗 W′」的情境系統性誤判。本研究把**疲勞態**的 EP、WEP 灌回模型（稱為「adjusted／ADJ」版），看能不能補救：
   - 原始三個模型對「全力榨乾後的 [[W prime reconstitution|W′ 回填]]」的估計：**W′BAL·INT 最準**（7.5 vs 實測 6.3 kJ，無顯著差）；**W′BAL·ODE（9.8 kJ）與 W′BAL·MORTON（16.9 kJ）都明顯高估**。
   - 改用 adjusted 版（納入 CP/W′ 的下降）後：ODE 與 Morton 的偏差**顯著改善**（ADJ·ODE 與實測相關 r=0.94），但仍未完全對上（ADJ·ODE 反而略**低**估約 17%）；INT 幾乎沒變化（因為它算回填 τ 的公式對 EP 的小變化不敏感，調整前後 τ 只差約 2.5%）。
   - 一句話：**把「CP/W′ 會漂」這件事算進去，確實能讓模型更準**——這就是論文標題「Accounting for dynamic changes… improves accuracy」的由來。但光調這兩個數還不夠完美，背後還有未解的生理。

7b. **漂移不只一個方向——先前的「重度（非全力）」運動反而可能『抬高』CP（Sreedhara 2020、Miura 2009）。** 上面講的都是「全力榨乾→CP 降」。但 Sreedhara 在間歇測試裡看到相反的一面：有受試者在恢復段踩到接近 CP 的「重度」強度後，再測的 CP（CP_ft，疲勞態）竟**顯著高於**新鮮態 CP_fr（subject 3、5，d>1.4）；還有人四次重複 3MT 的 CP **單調上升**（subject 7：295→305→319→327 W）。這呼應 Miura 2009「先前重度運動抬高 CP」與 priming 文獻——**一段不到力竭的重度運動像「額外暖身」**：加速 [[VO2 kinetics|VO₂ 動力學]]、招募並活化更多纖維、改善送氧，反而把可持續輸出的天花板暫時墊高。和第 6 點併讀就清楚了：**先前運動對 CP 的淨效應，取決於它是「暖身（適度重度）」還是「榨乾（全力到力竭）」**——前者可能抬高 CP、後者壓低 CP。
   - **「CP 升高」這個方向也有人試著塞進 W′BAL 模型（Skiba & Clarke 2021）。** 間歇運動會功能性抬高 CP（Soares-Caldeira 2012 量到約 28%），於是 [[Differential W prime balance model|ODE]] 假設 CP 固定就顯得太悲觀（提早約 300 秒預測力竭）。在 ODE 恢復項乘一個常數 K（=1.28，隱含 CP 升 28%）即得 [[KODE W prime balance model|W′BAL·KODE]]，把這個「抬高」方向納入。這與第 7 點 Black 的 adjusted 版（處理「壓低」方向）剛好是同一個「CP 非常數」問題的兩端。

7d. **更上游的提醒：CP 與 W′ 在「場次之內、場次之間」都不該被當常數（Skiba & Clarke 2021）。** 所有 [[W prime balance model|W′BAL]] 都假設輸入的 CP/W′ 在整場運動內外恆定，但這「很可能不成立」：CP 對運動中**營養**敏感、CP 與 W′ 隨**高海拔**下降、**先前運動**可抬高或壓低兩者。加上 W′ 本身估計誤差就有 7–46%，於是模型算的零線與真實零線都在抖——這是把本頁的「疲勞性漂移」放進建模脈絡看時，最該記住的一句。

7c. **更基本的一層——CP 連「同一個人、相近的時間」量兩次都會抖（個體內變異）。** 可塑性不必等到「先前劇烈運動」才出現；CP 本身就帶**測量／生理層面的個體內變異**。Sreedhara 的證據：把恢復功率設在 0.9 P_GET（本意是「在 CP 以下恢復」）時，有些天受試者竟在這段**淨耗 W′**（E_rec 為負）——表示那天他們的**真實 CP 比實驗室前測的值還低**，使「恢復強度」其實落在 CP 之上。也就是 CP 不是一個鎖死的點，而是一個**會隨日、隨 trial 上下抖的帶**。這對 [[W prime balance model|W′ 平衡模型]] 是另一層麻煩：模型用「某次測到的單一 CP」當固定零線，但真實零線本身在抖，於是「該補還是該耗」的判斷在 CP 附近最不可靠。

8. 收束成一個概念——**durability（耐久性／可塑性）**。傳統把一個人的 CP/W′ 當成兩張固定身分證；本頁的訊息是：它們其實會隨「你已經做了多少、怎麼做的」而漂移。這個「CP 在長時間或反覆力竭下還能不能守得住」的維度，就是近年耐力科學講的 **durability**，是一個獨立於「新鮮狀態 CP 多高」的表現面向：兩個人新鮮 CP 一樣，但比賽後段 CP 掉得少的那個，更能維持配速。

9. **把鏡頭拉遠——這不只是 CP/W′ 的小毛病，而是整個耐力表現模型缺的一塊（Jones 2023）。** 本頁用「重複 3MT（中間休 1 分鐘）」量到的是**短時間、全力榨乾**造成的漂移；但同一現象在**長時間有氧運動**裡更貼近真實賽事：Clark 等（2018/2019）讓車手先做 **2 小時重度（<CP）運動**，前後各量一次 CP，發現 **CP 降約 8–11%、W′ 降約 17–22%**，且 [[Lactate threshold|LT]]/[[Gas exchange threshold|GET]] 也同步下移約 10%（Stevenson 2022）——**三根表現支柱全會鬆動，不只 CP**。更關鍵的是下降幅度的**個體差異極大（0.4–32%）、且無法用起跑線的 VO2max/CP/W′ 預測**（r 全不顯著），這讓「衰退多少」升格成一個**獨立於新鮮體能的第四維**。Jones 把它命名為 [[Physiological resilience|生理韌性（resilience / durability）]] 並加進 [[Joyner model of endurance performance|Joyner 模型]]。換句話說：**本頁（Black 2023）是這個第四維在「CP/W′ 參數＋W′BAL 模型」層次的機制與建模證據；[[Physiological resilience]] 則是同一現象升上「整體表現決定因子」的概念層。** 兩個時間尺度的下降機制也不同——本頁短時全力走 PCr/Pi/pH 與 Type II 招募；2 小時長時運動主要走**肌糖原耗竭**（補糖 60 g/h 能讓 CP 幾乎不降，Clark 2019），同一個「CP 下降」可由不同路徑造成。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：(1) 先前的全力衝刺運動會改變功率–持續時間關係——EP（≈CP）與 WEP（≈W′）都下降；(2) 既有的 [[W prime balance model|W′BAL 模型]] 假設 CP 固定，因而在「大量消耗 W′」的情境會誤估回填（ODE/Morton 高估）；(3) 把 CP/W′ 的下降納入模型（adjusted 版）能改善 ODE 與 Morton 的準度。實務建議：在無法即時量 CP/W′ 的真實訓練/比賽中，全力衝刺後較宜採用 **W′BAL·INT** 來客觀評估剩餘能力。
- **背後的推理／證據**：用「重複 3MT（兩次 3MT 中間休 1 分鐘）」直接量到疲勞態的 EP 與 WEP——EP 降 7%、WEP 降 61%，且受試者在 F-3MT 仍達到並維持 VO₂peak（≥95%），證明第二次是**真力竭、非保留體力**，所以這些下降是真實的生理可塑性而非測試瑕疵。把 F-3MT 的 EP/WEP 代回模型後，ODE 與 Morton 的平均偏差統計上顯著縮小（p<0.001），這就是「納入動態變化能改善準度」的直接證據。

## 易誤解之處
1. **EP（≈CP）下降，不是「人變懶、保留體力」的假象，是真的可持續輸出下降。** 證據：受試者在第二次 3MT 仍把 VO₂ 逼到 VO₂peak 並維持，功率曲線也沒有「先低後又升」的偷懶痕跡——他們確實拼盡了，CP 還是掉了。
2. **「力竭」不等於「CP 一定會降」——要看你怎麼力竭。** 固定功率（CWR）力竭後 CP 不變、只 W′ 降（Ferguson 2010）；全力（all-out）力竭後連 CP 都降。差別在招募模式（Type II 是否被即刻全面招募），不是「只要累到底 CP 就會掉」。
3. **這不是在說「CP 沒用」，而是在說「新鮮狀態量的 CP 不能無條件套到疲勞狀態」。** CP 仍是最有預測力的閾值；只是把它當成一場長時間/間歇運動全程不變的常數，會在後段或反覆衝刺時失準。
4. **CP 的下降是（在這個時間尺度上）可逆的疲勞性漂移，不是永久損壞。** 充分恢復後 CP 會回到原值——它是「暫時被壓低」，不是「能力被破壞」。
5. **WEP 大降 ≠ 全是 CP 那條線在變。** F-3MT 的 WEP 降 61%，主因是第一次已榨乾 W′、只休 1 分鐘、回填不全（約只回 39%）；EP 那 7% 的下降才是「CP 本身會漂」的乾淨證據。兩件事要分開看。
6. **「先前運動一定壓低 CP」是過度推論——方向看你做了什麼。** 全力到力竭（all-out）會壓低 CP；但**不到力竭的重度運動可能反而抬高 CP**（像暖身／priming，Sreedhara 2020、Miura 2009，見推導第 7b 點）。所以漂移有兩個方向，不是單向衰減。Goulding 2023 進一步把「向上漂」這條拆細：**良好劑量（heavy、不致疲勞）的[[Priming effect|預熱]]會抬 CP 還是抬 W′，取決於它改到 VO2 反應的哪一相**——降 τVO2→CP↑、抬基礎相振幅/壓[[VO2 slow component|慢成分]]→W′↑（見 [[Priming effect on the power-duration relationship]]）。所以同一條雙曲線，**疲勞往左下推、適度預熱往右上推（且推 CP 或推 W′ 因人而異）**。
7. **CP 不是一個精準的點，是一條會抖的帶。** 連同一人、相近時間量兩次，CP 都有個體內變異（Sreedhara 2020：本意「在 CP 以下恢復」卻淨耗 W′，表示那天真實 CP 更低）。在 CP 附近（恢復強度逼近 CP 時）下「該補還是該耗」的判斷因此最不可靠——這是 [[W prime balance model|W′ 平衡模型]] 用單一固定 CP 當零線的隱藏弱點。

## 用生活例子再講一次
把身體想成一台高性能引擎賽車。CP 是「只靠正常供油、不爆增壓就能維持的最高巡航轉速」，W′ 是「氮氣加速罐的總量」。你以為這兩個規格是出廠就定死的——但如果你剛剛把車**操到極限跑了一趟**（全力 3MT），引擎會進入**保護性降載**：機件過熱、油氣環境變差，這趟之後它的「可持續最高巡航轉速」（CP）會暫時掉一截，氮氣罐也還沒回填滿。你若拿「冷車狀態量到的規格」去規劃下一趟，就會高估它的能耐、提早熄火。而且——**全力暴衝**比**穩定快跑**更會觸發這種降載，因為暴衝一上來就把每個汽缸都逼到底（對應 Type II 全面招募）。

（這個類比在哪裡會失準：真實引擎的「降載」是電子保護、機件本身規格沒變；而 CP 的下降是肌肉代謝環境（PCr/Pi/pH）與纖維疲勞造成的**真實參數漂移**，恢復後才回升。另外引擎不會「跑久了就把最高轉速本身改掉」，但人的 CP 真的會隨先前運動上下。）

## 換句話說
換句話說，CP 與 W′ 不是兩個刻在身上的固定常數，而是會隨「你先前做了多少、用什麼方式做」而上下漂移的量：一段全力榨乾的運動之後，CP（用 3MT 的 EP 代表）會降約 7%、W′（用 WEP 代表）會降約 61%，整條功率–持續時間雙曲線往左下移。這之所以重要，是因為 [[W prime balance model|W′ 平衡模型]] 預設 CP 不變、據此即時算剩餘 W′——一旦 CP 真的漂了，模型就會誤判；把這個漂移納入（adjusted 版）能讓 ODE 與 Morton 模型更準。這個「CP 在疲勞下守不守得住」的維度，就是耐力表現裡的 durability。

## 來源
- [[source-Jones-2023-physiological-resilience]]（推導第 9 點：2 小時重度運動使 CP 降 8–11%、W′ 降 17–22%、LT/GET 同步下移約 10%；下降幅度個體差異 0.4–32% 且與基線變項不相關→升格為獨立第四維 [[Physiological resilience|生理韌性]]；長時間運動的 CP 下降走肌糖原耗竭路線、補糖可緩解，與本頁短時全力的 PCr/Pi 路線並存。本頁是該第四維在 CP/W′ 與 W′BAL 模型層次的機制證據。）
- [[source-Goulding-2023-priming-VO2-kinetics]]（易誤解 #6 補充：向上漂的細分——適度（heavy）預熱改 VO2 哪一相決定它抬 CP（降 τ）或抬 W′（抬振幅/壓慢成分）；與本頁「疲勞向左下漂」對稱成「同一曲線兩個方向的急性可塑性」，完整見 [[Priming effect on the power-duration relationship]]。）
- [[source-Sreedhara-2020-recovery-W-prime-domain]]（推導第 7b、7c 點與易誤解 #6、#7：漂移的相反方向——重度（非全力）運動／重複 3MT 反而抬高 CP（subject 3、5 的 CP_ft>CP_fr d>1.4、subject 7 四次 3MT CP 295→327 W 單調升，呼應 Miura 2009 與 priming）；CP 的個體內變異——0.9 P_GET 的「恢復」段竟淨耗 W′（E_rec<0）證明那天真實 CP 低於前測值；對 W′BAL「CP 恆定」假設的另一層挑戰。）
- [[source-Black-2023-dynamic-power-duration]]（Introduction：W′BAL 模型假設 CP 恆定、all-out vs CWR 招募差異；Methods：重複 3MT 設計、EP/WEP 定義、adjusted 模型作法；Results：EP↓7%、WEP↓61%、三模型偏差與 adjusted 改善；Discussion：機制（PCr/Pi/pH、Type II 招募與慢恢復、Ferguson 對照、Clark 2019 糖原路線）、durability 與實務建議用 W′BAL·INT。）
- [[source-Skiba-Clarke-2021-W-prime-balance-mathematics]]（推導第 7b 補充與第 7d 點：W′BAL 假設 CP/W′ 在場次內外恆定「很可能不成立」——對營養/海拔/先前運動敏感、W′ 估計誤差 7–46%；間歇運動功能性抬高 CP（Soares-Caldeira 2012 約 28%）→ 在 ODE 乘常數 K=1.28 得 [[KODE W prime balance model|W′BAL·KODE]]，與 Black adjusted 版的「壓低」方向同屬「CP 非常數」問題兩端。）
