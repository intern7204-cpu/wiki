---
type: concept
aliases: [W prime, W撇, W', D prime, D', 臨界功率以上的功容量, 無氧功容量, 可疲勞常數, work capacity above critical power, fatigability constant]
tags: [exercise-physiology, thresholds, performance]
sources: [source-Poole-2021-AT-controversy, source-Poole-2016-critical-power, source-Goulding-2021-VO2-kinetics-tolerance, source-Chorley-2023-W-prime-dynamic-model, source-Lievens-2024-partial-depletion, source-Caen-2019-work-recovery-reconstitution, source-Chidnok-2013-intermittent-31P-MRS, source-Burnley-2011-priming-power-duration, source-Ventura-2023-severe-extreme-tolerance, source-Sreedhara-2019-power-models-survey, source-Jones-2010-CP-implications, source-Chidnok-2013-exhaustion-recovery-domain]
prerequisites: [臨界功率／臨界速度（critical power / critical speed, CP/CS）]
created: 2026-06-10
updated: 2026-06-12
---

# W′（臨界功率以上的有限功容量）

## 本質（一句話）
W′ 就是「你在臨界功率之上，總共還能再多擠出的**一筆固定、有限的能量**」——像一桶備用油，超過 CP 就開始燒，燒完就力竭，桶子大小不隨你燒多快而變。

## 前置概念
- [[Critical power|臨界功率／臨界速度（critical power / critical speed, CP/CS）]]
  （W′ 是功率-持續時間雙曲線的第二個參數，只有在 CP 之上才有意義；先懂 CP。）

## 為什麼會這樣（first-principles 推導）
1. 由 [[Critical power|CP]]：功率-持續時間是一條雙曲線，水平漸近線是 CP。但光有 CP 還不能算出「超過 CP 時撐多久」——還缺一個描述「超出部分總共能做多少功」的量。那個量就是 W′。
2. W′ 的定義：**在 CP 之上，累積能額外完成的功的總量**，是個有限的固定值（自行車用 kJ；跑步因為是距離，改稱 D′、單位是公尺）。
3. 它有個反直覺但關鍵的性質：**不管你用多高的功率超過 CP，把「超出 CP 的那部分功率 × 撐的時間」加起來，總是同一個 W′。** 在 [[Critical power|CP]] 頁的圖上，這表現成「每條不同高度的力竭測試，超出 CP 的陰影面積都相等」。（這個「總是同一個 W′」有直接的生理根據：力竭時肌肉內部會停在一個**與功率無關的固定代謝終點**——見 [[Metabolic milieu at task failure|力竭時的代謝終點]]。正因終點固定，「能做的總功」才固定，也才能合理假設**力竭那一刻 W′＝0**，這個假設是後續用「再次力竭撐多久」反推回填量的基礎。）
4. 由此得到 [[Critical power|CP]] 頁那條公式：
   $$t_{lim} = \frac{W'}{P - CP}$$
   W′ 是分子（油箱容量），(P − CP) 是分母（燒油速度＝你超過 CP 多少）。容量固定，燒得愈快、撐愈短——這正是雙曲線的數學內容。
5. W′ 裝的是什麼能量？主要是**非氧化的能源**：醣解（伴隨淨乳酸累積）與磷酸肌酸（PCr）等肌肉內的有限儲備。所以 W′「與『無氧功容量』相關，但不完全等同」。
6. 重要澄清（延續整篇主旨）：「W′ 裝無氧能源」**不代表**用 W′ 時肌肉缺氧。即使在 CP 之上消耗 W′，也沒有證據顯示肌肉變 [[Dysoxia|dysoxia]]。W′ 是「有限的非氧化儲備」，不是「缺氧的證據」。
7. W′ 不是純粹的一次性耗材：當你把強度**降回 CP 以下**，W′ 會逐漸**回填（reconstitution）**——這讓間歇運動（衝刺-恢復交替）能反覆動用 W′，是間歇訓練與競賽配速的生理基礎。回填的速度與形狀（先快後慢兩段、恢復強度依賴、**消耗速度依賴**——燒得愈快補得愈快、反覆力竭會變慢、部分消耗 vs 完全力竭的差別）見 [[W prime reconstitution|W′ 回填]]；如何把即時餘量算出來供配速用，見 [[W prime balance model|W′ 平衡模型]]。（量到的回填甚至可能短暫**超過 100%**——那不是桶子變大，而是 [[Priming effect|預熱效應]]讓第二輪運動佔了有氧供能的便宜、少花了 W′。）「會回填」最直接的證據，就是間歇運動裡實際做的[[Work done above critical power|超 CP 功（W>CP）]]會**大於**單次的 W′：Chidnok 2013 三種被動恢復下測到 W>CP＝3.8/5.6/7.9 kJ，全部超過 W′（≈1.9 kJ），且休愈久超得愈多——多出來的就是恢復補回、再被燒掉的份；而 W>CP 超過 W′ 的量與恢復間 [[Phosphocreatine|PCr]] 回補幅度相關（r=0.61），是「PCr 是 W′ 重要成分」的一根釘子。

### W′ 不是「一桶固定的無氧油」那麼單純（Poole 2016 的重要複雜化）
8. 原始模型（Monod & Scherrer）把 W′ 想成「固定的、主要無氧的能量儲備（高能磷酸＋醣解）」。數學上成立，但生理解讀被一連串發現挑戰：
   - **W′ 與有氧特徵掛鉤**：吸高氧（hyperoxia）會**升 CP、卻降 W′**（Vanhatalo 的高氧 vs 常氧實驗中，同一批人 ΔCP 與 ΔW′ 呈**反相關 r=−0.88**——抬高了「有氧」的 CP 反而縮小了「無氧」的 W′，直接打臉 W′＝固定無氧儲備）；訓練也常讓 CP 升幅大於 [[VO2max|VO2max]]，同時 W′ 縮小。若 W′ 純無氧，不該對「供氧」這麼敏感。
   - **回填動力學不像 PCr**：用「不同恢復時間反覆做到力竭」量 W′ 回填，發現其半回復時間約 **5 分鐘**，比磷酸肌酸（PCr）慢，反而和 [[VO2]]、血乳酸回到基線的動力學吻合。
   - **W′ 與 [[VO2 slow component|VO2 慢成分]] 正相關**：慢成分愈大、W′ 愈大——暗示 W′ 連著「肌肉效率損失與疲勞發展」，而非單純一桶儲備能。
   - **連 W′ 的「回填速度」都掛在有氧體能上**（Lievens 2024）：一個人 W′ 補得多快、多滿，與他的 [[VO2max|VO2peak]]、CP、GET 正相關（r＝0.67–0.77）——有氧愈強，桶子補得愈好、愈耐反覆消耗（即耐力運動講的 durability）。若 W′ 純無氧，它的恢復不該這麼吃有氧體能。這是又一根「W′ 連著有氧系統、不是孤立無氧儲備」的釘子。
9. 所以現代理解：**CP 與 W′ 不是分離的「有氧 vs 無氧」兩塊，而是同一個整合生物能系統的兩個面向。** 它們常一起改變（訓練、缺氧、疾病），不能各自貼「有氧/無氧」標籤。
10. **W′ 是「任務特定」的，沒有單一生理對應物。** 因為雙曲線跨各種運動型態都成立，而小肌群（如手握）和全身運動的限制機制根本不同：
    - 小肌群運動：W′ 主要對應**肌肉內**的限制（PCr/醣原耗竭、Pi/H⁺ 累積、周邊疲勞）。
    - 全身運動：W′ 還摻入**中樞/神經**限制（如高海拔時 W′ 大降 ~45%，部分是「無法把大肌群充分動員」的『取用受限』，而非肌肉內儲備變少）。
    - W′ 與大腿圍正相關——大 W′ 需要大肌肉量可動員。
11. 所以「W′ 是什麼」這個問題，等於「運動為何力竭」這個問題——答案隨運動型態、條件、對象而變，沒有單一密碼。

### W′ 在老化與疾病中
12. 老化、心衰（CHF）、慢性阻塞性肺病（COPD）會**同時壓低 CP 與 W′**，把整條功率-時間曲線往原點推。有趣的是：健康年輕人 [[VO2max|VO2max]] 與 W′ 在群體層級不相關（r²≈0.01），但跨越極廣的有氧能力範圍（10–70 mL/kg/min）來看，兩者就浮現關聯——再次說明 W′ 不是單純的肌肉內儲備。
13. 疾病壓低 W′ 的機制偏中樞：CHF/COPD 的肌肉量流失幅度，遠小於 W′ 的下降幅度，所以主因不在肌肉萎縮，而更可能是**通氣限制、呼吸困難（dyspnea）、[[Group III-IV muscle afferents|Group III/IV 肌肉傳入]]抑制中樞驅動**等中樞性疲勞機制。

### W′ 為什麼是「固定的一桶」：正回饋迴路的湧現結果（Goulding 2021）
14. 把 W′ 接到 [[Critical Pi threshold and positive feedback model|臨界閾值模型]]：在 CP 之上，[[Inorganic phosphate|Pi]] 以正回饋方式一路爬向**尖峰 [Pi]（≈25 mM）**，到達就力竭。而「CP 之上能做的總功」之所以湧現成一個**大致固定**的量（W′），是因為 Pi 有**遞減報酬**——剛越過臨界 [Pi] 時、多一點 Pi 對效率打擊大；接近尖峰時、多一點 Pi 的邊際效果小。這個非線性使「達到尖峰前累積的總功」對不同超出幅度都差不多，正是 W′ 為固定值的機制由來。
15. 由此 W′ 不再只是「一桶與有氧無關的無氧油」，更可理解為**「到達尖峰 [Pi] 之前能容納多少效率損失」**的容量——這同時解釋了它為何與 [[VO2 slow component|VO2 慢成分]] 正相關（兩者同屬一個迴路）、為何對供氧敏感、以及為何 [[Group III-IV muscle afferents|Group III/IV 傳入神經]] 抑制（抬高可忍受的尖峰 [Pi]）會放大 W′。

### W′ 可以被「預熱」直接做大——且與 CP 可分離（Burnley 2011）
16. W′ 不只會回填，還能被介入**直接做大**。Burnley 2011 讓人先做一段**重度（heavy，<CP）**[[Priming effect|預熱]]、再做極重度運動到力竭，量到 **W′ 升約 17%（+2.7 kJ）、而 CP 完全不變**。這有兩層意義：
    - **W′ 是可正向操弄的，不只是被動的一桶定量。** 把 VO2 動力學在「不致疲勞」的前提下預熱起來，CP 之上能做的功就增加（機制見下點與 [[Three-factor model of severe-intensity exercise tolerance|三因子模型]]）。
    - **CP 與 W′ 可被分離地動。** 同一次預熱把 W′ 抬高、卻沒碰 CP——這是「CP 與 W′ 是兩個可獨立移動的參數」的乾淨證據（呼應 [[Critical power|CP]] 對未致疲勞介入的穩健性）。
17. **為什麼 heavy 預熱有效、severe 沒效？** 同研究的對照組做**極重度（severe，>CP）**預熱，對 VO2 動力學的改善其實相似，但 **W′、CP、力竭時間全無變化**——因為 severe 預熱過了 CP、先耗掉一部分非氧化備援（留下疲勞代謝物），其動力學益處被這份代價抵銷。這把 W′ 拆成「非氧化備援容量 × VO2 動力學 × VO2peak」三條（[[Three-factor model of severe-intensity exercise tolerance|三因子模型]]）：heavy 預熱只動了後兩條、沒動備援 → W′ 變大；severe 預熱動了動力學卻也花了備援 → 打平。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Poole 等人把 W′（跑步為 D′）定義為「在 CP/CS 之上以依賴於超出幅度的速率被消耗的有限能量儲存」，並指出其持續耗竭正是 CP 之上「無法穩態、註定力竭」的根源。
- **背後的推理／證據**：證據在於力竭時間的高度可預測性——只要知道個人的 CP 與 W′，就能用 t_lim = W′/(P−CP) 準確預測各種超 CP 強度下的力竭時間。陰影面積恆等（不隨功率變）正是 W′ 為「固定有限量」的經驗支持。

## 易誤解之處
1. **W′ 是「能量總量」，不是「功率」也不是「時間」。** 它是一桶油的容量（kJ）。撐多久＝容量 ÷ 燒油速度；別把 W′ 直接當成「能撐多久」。
2. **「無氧功容量」是近親但不等同。** W′ 主要由非氧化能源構成，但兩者定義與量法不同，文獻刻意用「related to, but not synonymous with」。
3. **用 W′ ≠ 肌肉缺氧。** 這是最容易滑回去的舊觀念。W′ 含醣解/PCr 等非氧化能源，但「動用非氧化能源」和「組織缺氧（dysoxia）」是兩回事。
4. **W′ 會回填。** 把它想成「用完就沒」的純耗材會錯估間歇運動；降到 CP 以下時 W′ 逐漸恢復（整體半回復 ~5 分鐘，但其實是先快後慢兩段：[[W prime reconstitution|快段≈PCr 再合成、慢段≈清酸]]）。
5. **別把 W′ 當成「一桶固定的無氧儲備」。** 它對供氧敏感、回填動力學像有氧而非 PCr、且與 [[VO2 slow component|VO2 慢成分]] 相關——它是整合生物能系統的一部分，不是純無氧那一塊。
6. **W′ 沒有單一生理對應物，是任務特定的。** 小肌群運動的 W′ 偏肌肉內限制，全身運動的 W′ 還摻中樞限制。「W′ 是什麼」其實等於「運動為何力竭」，答案隨情境而變。
7. **W′ 可理解為「可疲勞常數（fatigability constant）」或「抗力竭的緩衝量」。** 對應 [[Critical power|CP]] 作為「疲勞閾值」：CP 標出疲勞會開始失控的界線，W′ 則是越界後還能撐多少的緩衝；緩衝愈小，愈快力竭、愈顯「易疲勞」。
8. **「力竭＝W′ 耗盡」只在 severe 域成立——進入 [[Extreme intensity domain|extreme（極限強度）域]]就破功。** 推導第 3 點的「力竭那一刻 W′＝0」是 t_lim 公式與所有回填反推的地基，但它有適用範圍：在 severe 域（[[Critical power|CP]]~[[Maximal intensity for VO2max attainment|IHIGH]]）力竭時 W′ 確實大致燒乾；但在強度高到 IHIGH 之上的 extreme 域，力竭來得太快，**W′ 還沒完全耗竭就停了**（單關節研究甚至顯示 extreme 域有自己一筆較小的 W′，1.7 vs 5.9 kJ；Alexander 2019）。後果：用 severe 域的 W′ 去算 extreme 域的 t_lim 會**高估**（Ventura 2023）。所以「W′ 是一桶固定、力竭時剛好燒完」這個乾淨圖像，只在它原本適用的 severe 域裡才成立。
9. **同一筆資料，W′ 的數值還會隨「用哪個模型擬合」而變。** 除了上面的域限制，W′ 連「估出來是多少」都不穩：把[[Three-parameter critical power model|三參數模型]]套到與兩參數**同一筆**力竭資料，CP 估值相近（如 165 vs 176 W），W′ 卻可以差六成（47.9 vs 29.1 kJ）；[[Exponential power-duration models|指數型模型]]甚至給不出 W′。所以一個 W′ 數字一定要附「用什麼模型／協定估的」，跨方法直接比 W′ 很危險（完整見 [[Critical power estimation protocols|CP/W′ 估計協定]]、[[Intra-individual variability of critical power and W prime|個體內變異]]）。
10. **「桶子大小不隨你燒多快而變」要補一句但書：能多快把它倒出來，是有上限的、而且桶愈空上限愈低。** 上面把 W′ 講成「可猛噴可淺噴、總是把同一罐噴完」，這在容量層次對；但 W′ 能被**消耗的最大速率**並非無上限——定功率力竭後只要把功率降一點（仍 >CP），人還能再擠出一小段（~39 s、0.17 kJ），代表力竭那刻 W′ 並非字面歸零，只是剩的那點當下倒不夠快。所以「力竭＝W′＝0」是夠用的近似、W′ 帶輕微協定依賴。容量（多少）與最大流速（多快）是兩件事，完整見 [[W prime expenditure is rate-limited|W′ 消耗的速率上限]]（Chidnok 2013）。

## 用生活例子再講一次
延續 [[Critical power|CP]] 的賽車比喻：CP 是「只靠主油箱能維持的最高車速」，W′ 就是車上那「一小罐 NOS 氮氣加速」的**總容量**。這罐子大小是固定的——你可以選擇猛噴（超 CP 很多，分母大，幾秒就見底）或淺噴（超 CP 一點，分母小，撐久一點），但「噴射功率 × 時間」加起來總是把同一罐噴完。鬆油門回到 CP 以下時，這罐 NOS 還會慢慢自動回充。

（失準之處：真正的 NOS 罐回充要靠外部加氣；W′ 的回填是身體在低強度時靠有氧代謝原地補回磷酸肌酸、清乳酸，是內生的。）

## 換句話說
換句話說，W′ 是「臨界功率之上你總共還能多做的那筆有限功」，一桶大小固定的備用油。它和 [[Critical power|CP]] 兩個參數合起來，就能用 t_lim = W′/(P−CP) 算出任何超 CP 強度下撐多久。它主要裝非氧化能源，但動用它不代表缺氧——這點和整篇綜述對「無氧」一詞的矯正一脈相承。

## 來源
- [[source-Poole-2021-AT-controversy]]（Fig. 11 圖說、Critical power concept 節：W′/D′ 定義、陰影面積恆等、t_lim 公式、與「無氧功容量」之區別。）
- [[source-Poole-2016-critical-power]]（Unraveling W′ 整節：W′ 對供氧敏感、回填半時 ~5 分、與慢成分相關、任務特定無單一對應、老化/CHF/COPD 同降 CP 與 W′、「fatigability constant」。）
- [[source-Chorley-2023-W-prime-dynamic-model]]（回填的雙指數細節與恢復強度依賴，支持本頁「W′ 會回填」一節；詳見 [[W prime reconstitution|W′ 回填]] 與 [[W prime balance model|W′ 平衡模型]]。）
- [[source-Lievens-2024-partial-depletion]]（Results/Discussion：W′ 回填量與 VO2peak/CP/GET 正相關 r＝0.67–0.77、與 durability 連結，支持「W′ 連著有氧系統」一節；小消耗後回填可超過 100%（[[Priming effect|預熱效應]]）。）
- [[source-Caen-2019-work-recovery-reconstitution]]（推導第 3 點與第 7 點：以「力竭時固定代謝終點」支持 W′ 固定性與「力竭時 W′＝0」假設（見 [[Metabolic milieu at task failure|力竭時的代謝終點]]）；回填速度受消耗速度影響（消耗快→補快，R＝0.68），詳見 [[W prime reconstitution|W′ 回填]]。）
- [[source-Chidnok-2013-intermittent-31P-MRS]]（推導第 7 點：間歇運動實測 [[Work done above critical power|W>CP]]＞W′（3.8/5.6/7.9 vs ≈1.9 kJ）直接驗證 W′ 會回填、可反覆動用；W>CP 超過 W′ 的量與 ³¹P-MRS 量到的 [PCr] 回補幅度相關 r=0.61，支持 PCr 為 W′ 成分。）
- [[source-Burnley-2011-priming-power-duration]]（新增第 16–17 點：heavy（<CP）預熱使 W′↑~17%、CP 不變 → W′ 可被 VO2 動力學介入正向做大、且與 CP 可分離；severe（>CP）預熱因致疲勞而 W′/CP 不變 → 把 W′ 拆成三因子（見 [[Three-factor model of severe-intensity exercise tolerance]]）。）
- [[source-Ventura-2023-severe-extreme-tolerance]]（易誤解 #8：「力竭＝W′＝0」只在 severe 域成立；[[Extreme intensity domain|extreme 域]]（>[[Maximal intensity for VO2max attainment|IHIGH]]）力竭時 W′ 未完全耗竭、CP 模型高估 t_lim；引 Alexander 2019 extreme 域專屬較小 W′（1.7 vs 5.9 kJ）。）
- [[source-Sreedhara-2019-power-models-survey]]（易誤解 #9：W′ 是「elusive」——同筆資料下兩參數/三參數模型給出差很多的 W′（29.1 vs 47.9 kJ）而 CP 相近、指數模型無 W′；W′ 跨模型與跨天（IIV）皆不穩，詳見 [[Critical power estimation protocols]]。）
- [[source-Chidnok-2013-exhaustion-recovery-domain]]（易誤解 #10：力竭後降 19% 功率（仍 >CP）八人皆再撐 39±31 s、多做 0.17 kJ W>CP（> SEE、> 理論殘留、與 t_lim 變異無關）→ 力竭時 W′ 非字面歸零、最大消耗速率隨剩餘量遞減、W′ 帶協定依賴；完整見 [[W prime expenditure is rate-limited]]。）
- [[source-Jones-2010-CP-implications]]（地標級 CP 綜述，本頁「W′ 不是固定無氧儲備」的一手源頭：古典定義 W′＝substrate-level phosphorylation（PCr＋醣解）＋少量肌紅蛋白/靜脈血氧儲備、「anaerobic work capacity」為不精確舊稱（推導第 5、8 點）；高氧升 CP 卻降 W′、ΔCP 與 ΔW′ 反相關 r=−0.88（Vanhatalo et al.）→ W′ 更像「[PCr]/pH 趨向力竭低值前能用的機械功容量、與 CP 到 VO2max 的『距離』相關」而非固定無氧庫；W′ 可被先前 >CP 運動、醣原耗竭壓低，被衝刺訓練、肌酸負荷、[[Priming effect|預熱]]抬高、且訓練升 CP 常伴 W′ 降。）
