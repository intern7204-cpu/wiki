---
type: concept
aliases: [臨界功率, 臨界速度, 臨界輸出, 功率-持續時間關係, critical power, critical speed, CP, CS, power-duration relationship, critical VO2]
tags: [exercise-physiology, thresholds, performance]
sources: [source-Poole-2021-AT-controversy, source-Poole-2016-critical-power, source-Goulding-2021-VO2-kinetics-tolerance, source-Goulding-2022-determinants-of-CP, source-Black-2023-dynamic-power-duration, source-Ventura-2023-severe-extreme-tolerance, source-Sreedhara-2019-power-models-survey, source-Jones-2010-CP-implications, source-Chidnok-2013-exhaustion-recovery-domain]
prerequisites: [運動強度區間（exercise intensity domains）, 乳酸的出現率與消失率（lactate Ra / Rd）]
created: 2026-06-10
updated: 2026-06-12
---

# 臨界功率／臨界速度（critical power / critical speed, CP/CS）

## 本質（一句話）
臨界功率就是「你能**單靠有氧、不持續動用備用能量**而維持下去的最高輸出」——高過它，每一秒都在燒一桶有限的備用油（[[W prime|W′]]），燒完就力竭，而且燒多快、撐多久可以用公式精準算出來。

## 前置概念
- [[Exercise intensity domains|運動強度區間（exercise intensity domains）]]
  （CP 正是「重度↔極重度」那道界線；先懂區間框架。）
- [[Lactate appearance and disappearance|乳酸的出現率與消失率（Ra / Rd）]]
  （CP 之上 Ra 永遠壓過 Rd、乳酸停不下來；先懂這層拔河。）

## 為什麼會這樣（first-principles 推導）
1. 做一個觀察實驗：讓人用幾種不同的固定高功率分別騎到力竭，記下「功率」對「能撐多久（持續時間 t）」。把這些點連起來，得到一條**雙曲線**：功率愈高、撐的時間愈短，而且不是線性、是急遽縮短。
2. 這條雙曲線有一條**水平漸近線**——功率降到某個值時，理論上可以撐「無限久」。這條漸近線的高度，就是**臨界功率（CP）**（用速度表示就是臨界速度 CS）。它代表「不會一路把你逼向力竭」的最高可持續輸出。
3. 雙曲線還有第二個參數：**[[W prime|W′]]（W-prime）**，代表「在 CP 之上你總共能多擠出的一筆**有限**能量」（騎車單位是 kJ，跑步用 D′、單位是距離）。不管你用多高的功率超過 CP，超出的部分累積消耗的總量都等於這同一筆 W′。
4. 把這關係寫成公式（極重要、放慢看）：
   $$t_{lim} = \frac{W'}{P - CP}$$
   - P＝你實際用的功率，CP＝臨界功率，W′＝那筆有限備用能量，t_lim＝力竭前能撐的秒數。
   - 直覺：分子 W′ 是「油箱裡的備用油」，分母 (P − CP) 是「你超過 CP 多少、也就是燒備用油的速度」。超得愈多、燒愈快、撐愈短；剛好等於 CP 時分母為 0、撐無限久。
5. 為什麼 CP 是「真正的閾值」？因為**只有越過 CP，身體才進入「再也穩不住」的狀態**（見 [[Exercise intensity domains|區間]]）：
   - CP 以下：[[VO2|VO2]]、血乳酸、肌肉裡的磷酸肌酸/無機磷酸/pH **都能穩定**，撐得住。
   - CP 以上：上述每一個變數都**回不了穩態、一路惡化到力竭**；[[Lactate appearance and disappearance|乳酸 Ra]] 持續超過 Rd，[[VO2 slow component|VO2 慢成分]] 把 VO2 推向 VO2max。
6. 關鍵矯正（本綜述主旨）：原始 [[Anaerobic threshold|無氧閾值]] 概念想抓的「持續非氧化供能開始的那條線」，其實對應的是 CP，**不是** LT/AT。LT 只切「中等↔重度」，而 CP 才切出「能穩 vs 註定力竭」。所以 CP「比 AT 本身更能實現 AT 概念原本的意圖」。
7. 但同一個提醒仍成立：即使在 CP 之上，也**沒有證據顯示肌肉真的變「無氧/缺氧」**（見 [[Dysoxia]]）。W′ 雖含無氧能源（醣解、磷酸肌酸），但「超過 CP」不等於「缺氧」。

### CP 其實是一個代謝率（「critical VO2」），不只是機械功率
8. CP 表面上量到的是機械功率（瓦），但它**本質上是一個氧化代謝率**——「全身整體仍能完全靠有氧供能（substrate-level phosphorylation 達穩態、血乳酸不持續累積、肌肉磷酸肌酸不持續下降）的最高代謝率」。所以更精確的名字是「critical VO2」。
9. 由此推出一個易被忽略的後果：同一個 critical VO2，對應的「瓦數」會隨**運動經濟性**（如騎車踏頻、跑步技術）而變。換言之，CP 的瓦數不是鐵打的，背後的代謝率才是。正因為它用「功率/速度」這種功能性單位表達，才這麼好用來預測表現。
10. CP 在強度地圖上的位置：大約落在 [[Lactate threshold|LT]]/[[Gas exchange threshold|GET]] 與最大功率的**中間**。以 %[[VO2max|VO2max]] 表示，健康年輕人 LT/GET 約 50–65%、CP 約 70–80%；訓練有素者可達 70–80% 與 80–90%。但這些百分比因人而異，不能當固定值套用。
11. CP 對 **O₂ 輸送高度敏感**（連到 [[Microvascular O2 delivery|微血管 O₂ 輸送]]）：吸高氧（hyperoxia）會**升 CP、降 W′**；吸低氧（hypoxia）與血流阻斷會**降 CP**（完全阻斷甚至使 CP < 0，因為連靜息代謝率都撐不住）。這證明 CP 是「有氧能力」的參數。

### CP 是「疲勞閾值」
12. 為什麼把 CP 稱為「fatigue threshold」？因為它正好分隔兩種疲勞行為（見 [[Muscle fatigue|疲勞]]、[[Critical torque|臨界扭矩]]）：低於 CP，[[Muscle fatigue|周邊疲勞]] 緩慢、代謝穩定；高於 CP，周邊疲勞發展快 4–5 倍、肌肉內 PCr/Pi/pH 持續惡化到力竭。³¹P-MRS 直接量到：CP 之下 10% 時肌肉 PCr、Pi、pH 在 1–2 分鐘內達穩定並維持 20 分鐘；CP 之上 10% 時這些變數一路惡化到力竭（~12 分鐘）。
13. 一個常被誤解的精細點：CP **不是**分隔「可持續 vs 不可持續」——而是分隔「可穩態 vs 不可穩態」。CP 之上仍能運動，只是無法穩態、且撐多久可由 t_lim 精準預測。
13a. **CP 不只分隔「運動中穩 vs 不穩」，還分隔「力竭後能不能逆轉回補」（Chidnok 2013）。** 上面 §12 講的是運動進行中的穩定性；再加一層**恢復向**的證據把 CP 釘成肌內代謝閾值：讓人先在 CP 之上力竭，**緊接著**改成不同強度恢復並用 ³¹P-MRS 即時量肌內代謝物——降到 **CP 以下**，[[Phosphocreatine|PCr]] 從 40% **回補到 76%**、pH 回到 7.0、[[Inorganic phosphate|Pi]]/ADP 下降，可再撐 10 分鐘；維持在 **CP 以上**（即使只降 19% 功率），這些代謝物**一個都不回補**（PCr 停 37%、pH 停 6.6、Pi 停 545%），只能再撐約 39 秒；被動休息補得最快（PCr→96%）。所以 CP 不僅是「運動中代謝穩不穩」的線，也是「力竭後代謝能不能**回頭**」的線——這正是 [[W prime reconstitution|W′ 回填只在 CP 以下發生]] 的肌內機制底（那 39 秒的殘留另見 [[W prime expenditure is rate-limited]]）。

### τVO2 決定 CP：CP 是湧現的，不是基本設定（Goulding 2021）
14. 再往機制深一層問：CP 這個「可穩態的最高代謝率」由什麼決定？答案是 **[[VO2 kinetics|VO2 動力學]] 的速度（τVO2）**。動力學愈快（τ 小）→ [[O2 deficit|氧虧]] 愈小 → 同功率下 [[Inorganic phosphate|Pi]] 累積愈少 → 要到更高功率才越過臨界 [Pi] → CP 愈高。
15. 所以在這個觀點下，**CP 不是寫死的基本設定值，而是一個湧現性質**——它是「讓你正好坐在臨界 [Pi] 上」的那個功率（完整推導見 [[Critical Pi threshold and positive feedback model|臨界閾值模型]]）。證據：τVO2 與 CP **反相關 R²=0.90**（Murgatroyd），跨族群呈線性；訓練 ↓τ↑CP、缺氧 ↑τ↓CP、提高踏頻 ↑τ↓CP；而且在**同一個人**身上急性加速/減慢 τVO2，CP 就相應升/降——有時與送氧改變無關，證明 τVO2 對 CP 有**獨立於送氧**的決定作用。
16. 由此補一個精細點，和上面「critical VO2」並不衝突：最深層的不變量其實是**「臨界代謝物（[Pi]）累積水準」**，CP 的瓦數則隨效率而變。Barker 發現不同踏頻下 CP 的瓦數不同、但各自 CP 處的 VO2 相同——正說明「瓦數可變、背後的代謝臨界才是本體」。也因為真實肌肉是上千條性質連續的纖維，CP 更像一段窄的**「邊界層」**而非剃刀般的單點（Pethick）。

### CP 由什麼決定：氧氣運送鏈的每一步（Goulding & Marwood 2022）
17. 把上面「τVO₂ 決定 CP」再放大：既然 CP 是有氧能力的上限，那麼「氧氣最終被肌肉用掉多快」這條鏈的**每一步**都該能改變它。這條鏈有三步，**各自獨立**地決定 CP（判準是「能單獨改它而不動其他兩條」）：
    - **[[Convective oxygen delivery|對流送氧（Q̇O₂ = 心輸出 × CaO₂）]]**：把含氧血整批運到肌肉。缺氧↓CP、高氧↑CP（~10%）、縮短工作週期↑CP、血流阻斷使 CP<0。
    - **[[Diffusive oxygen transport|擴散送氧（Fick 定律 V̇O₂ = DO₂ × ΔPO₂）]]**：氧再從微血管滲進細胞。微血管化與 CP 高相關（r 達 0.88–0.94）；小肌群運動裡擴散往往是主導瓶頸。
    - **[[VO2 kinetics|肌肉氧利用速率（τVO₂）]]**：粒線體吃氧多快。work-to-work 單獨放慢 τ（送氧不變）即降 CP，證明它獨立於送氧。
18. 三條旁路最終都改的是**同一件事**：起跑轉換時肌內 [[Inorganic phosphate|Pi]] 累積多快、何時碰到臨界 [Pi]（共同出口見 [[Critical Pi threshold and positive feedback model|臨界閾值模型]]）。再升級到全身，最終 CP 還取決於**肌纖維型組成**（Type I 比例高→CP 高，r≈0.67–0.79）、**運動肌肉量**與**運動單位招募**（招募愈多→每條纖維負擔愈小→CP 愈高）。完整的「決定因子交互」總成見 [[Determinants of critical power|臨界功率的決定因子]]。

### CP 不是固定常數：它會被先前的疲勞壓低（durability，Black 2023）
19. 上面把 CP 講成「一個人某個確定的有氧上限」，但要補一個關鍵限制：**CP 不是恆定不變的**。既然 CP 是 τVO₂、送氧、臨界 [Pi] 湧現出來的結果（§14–16），而這些東西會被先前運動改變，CP 自然也會漂。實測（[[3-minute all-out test|3MT]] 的 EP 代表 CP）：
    - **全力（all-out）運動後**：做完一次榨乾 W′ 的 3MT、只休 1 分鐘，第二次的 EP（≈CP）降約 **7%**（Black 2023）。
    - **長時間重度運動後**：連續 2 小時重度固定功率運動，CP 降約 **9%**，且與**肌糖原耗竭**相關、補糖可緩解（Clark 2019）。
    - **但不是「只要力竭 CP 就降」**：短時間嚴重強度的**固定功率**力竭後，CP **不變**、只有 W′ 降（Ferguson 2010）。差別在招募模式——全力運動一開始就把 Type II 全招募、深度疲勞且恢復慢，才會壓到 CP。
20. 這件事對前面所有把 CP 當固定線的工具（尤其 [[W prime balance model|W′ 平衡模型]]）是重要警訊：「CP 恆定」是這些模型的關鍵假設，疲勞下會被違反，導致誤估。這個「CP 在長時間/反覆力竭下守不守得住」的維度，就是 **durability（耐久性）**；完整推導、機制與對模型的修正見 [[Power-duration relationship plasticity|功率–持續時間關係的可塑性]]。

### 兩參數模型只是一種寫法：它的數學形式與兩個破綻（Sreedhara 2019）
21. 前面用的 t_lim ＝ W′/(P−CP) 只是這個雙曲線的**一種寫法**。歷史上它有好幾種等價的代數形式：Monod & Scherrer 最早寫成「總功對時間的線性式」W_lim＝CP·t＋W′；Moritani 改寫成「功率對 1/t 的線性式」P＝W′·(1/t)＋CP；Whipp 等用非線性雙曲線。數學上是同一個模型，但用不同形式去擬合**同一筆**力竭資料，會解出**不同的參數估計**——尤其 [[W prime|W′]]（CP 相對穩）。所以引用一個 W′ 數字，一定要附「用什麼形式／協定估的」（完整見 [[Critical power estimation protocols|CP/W′ 估計協定]]）。
22. 這個簡潔的兩參數模型有**兩個已知破綻**，正好各自催生了一族修正模型：
    - **破綻一：t→0 時 P→∞。** 模型說「衝刺夠短、功率可以無限大」，但肌肉有最大瞬間功率上限。修法＝加一個參數，把曲線在短時間端封頂到有限的 Pmax → [[Three-parameter critical power model|三參數模型]]。
    - **破綻二：CP 被當成「能無限維持」。** 實際 CP 大約只能撐不到一小時、且會在疲勞下漂移（見 §19–20、[[Power-duration relationship plasticity|可塑性]]）。改用指數函數整條描述、並讓可持續功率會衰退的，是 [[Exponential power-duration models|指數型功率–持續時間模型]]（如 Péronnet-Thibault 假設 MAP 只撐 ~7 分鐘）。
   再加上 CP/W′ 還有跨天的 [[Intra-individual variability of critical power and W prime|個體內變異（IIV）]]，所以「一個人的 CP/W′」其實是一組帶著模型依賴與日間擺動的估計，而非寫死的常數。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Poole 等人主張 CP/CS 是預測運動表現、區分重度/極重度、理解疲勞與力竭機制最有用的閾值，遠勝 LT/AT。CP 能解釋自行車計時賽 80% 以上的表現變異；幾乎所有奧運徑賽都在 CP/CS 上下競技。
- **背後的推理／證據**：兩條腿。其一，CP 是唯一能**精準預測力竭時間**的閾值（t_lim = W′/(P−CP)）。其二，「跨過 CP 與否，一整組生理變數行為相反」（Fig. 13），顯示它是真正的生理分界，而非任意挑的點。此雙曲線關係跨物種（蠑螈、鼠、馬）、跨運動型態（跑、騎、游、划）都成立，極為穩健。

## 易誤解之處
1. **CP ≠ AT/LT，且明顯高於它們。** CP 落在比 LT 高得多的代謝率（常 ~70% VO2max 或更高）。把兩者混為一談，是判讀與處方的大錯。
2. **CP ≠ VO2max。** CP 是「可持續的最高輸出」，VO2max 是「攝氧能力的天花板」。CP 之上你還能短暫運動（燒 W′），只是撐不久。
3. **CP 不是「無氧 vs 有氧的開關」。** 越過 CP 代表「需要持續動用 W′（含非氧化能源）」，但不代表肌肉缺氧。名字裡沒有「無氧」是刻意的優點。
4. **CP 與 [[Maximal lactate steady state|MLSS]] 概念相近但量法不同。** MLSS（最大乳酸穩態）在概念上接近 CP，但測定方式常使它略低估 CP；別當成數值完全相等。
5. **閾值用速度/功率表示會帶來協定依賴。** 嚴格上 CP 是個功率/速度值，但跨人比較時仍應留意測定方式（需數次力竭測試，或單次 [[3-minute all-out test|3 分鐘全力測試]]）。
6. **CP 是帶誤差的估計值，約有 ~5% 的日間變異。** 估到「整數瓦」（如 200 W）並不代表真值就是 200——典型誤差下實際可能落在約 190–210 W。後果：若叫人「剛好踩在估計的 CP」，他很可能其實已在 CP 之上，生理反應與耐受度完全不同。處方時要把這個不確定區間放在心上。
7. **CP 還會隨「先前累了多少」而漂，不只是量測誤差。** §19–20：全力運動後 CP 可暫時降約 7%、長時間重度運動後約 9%。所以「新鮮狀態量的 CP」不能無條件套到比賽後段或間歇的疲勞狀態（見 [[Power-duration relationship plasticity|可塑性]]）。這是真實的生理漂移，與第 6 點的隨機日間誤差是兩回事。
8. **CP 對「未致疲勞的介入」相當穩健，且與 [[W prime|W′]] 可分離地動。** 與第 7 點互補：**重度（heavy，<CP）[[Priming effect|預熱]]會把 W′ 做大 ~17%、卻完全不動 CP**（Burnley 2011）。所以 CP 與 W′ 是**兩個可獨立移動的參數**——同一介入可以只抬 W′ 不碰 CP（heavy 預熱），也可以兩個都不動（severe 預熱因致疲勞而抵銷）。別預設「凡是讓人撐更久的介入都會抬 CP」。
9. **t_lim 公式的「準確範圍」有上限——進入 [[Extreme intensity domain|extreme（極限強度）域]]會開始高估。** 公式 t_lim = W′/(P−CP) 隱含「力竭＝W′ 剛好耗盡」。這在 severe 域（[[Critical power|CP]] ~ [[Maximal intensity for VO2max attainment|IHIGH]]）成立、預測準確；但過了 IHIGH 進入 extreme 域，力竭來得太快、W′ 還沒燒乾就停，於是公式會**高估**能撐多久，且愈往高強度愈不準（Ventura 2023）。所以別把 t_lim 公式無限外推到任何超 CP 強度——它有適用的上邊界。另外，估出的 CP 本身**準（SEE~5%）、但 W′ 較不準（SEE 常 >10%）**，且用兩試驗配適會放大極端強度的高估（見 [[Critical power model fitting|CP 模型配適]]）。

## 用生活例子再講一次
把身體想成一台有「主油箱（有氧、邊跑邊補）」和「一小罐 NOS 氮氣加速（W′、用完就沒）」的賽車。CP 就是「只靠主油箱、不碰 NOS 能維持的最高車速」。低於 CP，你想跑多久跑多久。一旦超過 CP，差額全靠噴 NOS 補——噴得愈猛（P−CP 愈大），那罐 NOS 愈快見底，見底就熄火。能撐幾秒，就是「NOS 總量（W′）÷ 噴射速度（P−CP）」。

（失準之處：NOS 用完就真的沒了；W′ 在你把強度降到 CP 以下時還會慢慢「回填」（recovery of W′），不是一次性耗材。）

## 換句話說
換句話說，臨界功率是「不必持續燒備用能量就能維持的最高輸出」，是把運動分成「能久撐」與「註定力竭」的真正分水嶺。配上有限的 [[W prime|W′]] 和公式 t_lim = W′/(P−CP)，它能精準算出力竭時間——這是任何其他閾值都做不到的，也是為什麼本綜述說 CP 才真正實現了 [[Anaerobic threshold|無氧閾值]] 概念當初的抱負。

## 來源
- [[source-Poole-2021-AT-controversy]]（Coincidence 節「Critical power concept」、Fig. 11 與 Fig. 13、t_lim 公式、跨物種跨模態證據。）
- [[source-Poole-2016-critical-power]]（CP=critical VO2、~5% 日間誤差、%VO2max 落點、O₂ 輸送敏感性（hyperoxia/hypoxia/occlusion）、CP 作為疲勞閾值與 ³¹P-MRS 證據。）
- [[source-Goulding-2021-VO2-kinetics-tolerance]]（τVO2 決定 CP：反相關 R²=0.90、急性介入升降 τ 帶動 CP 且獨立於送氧；CP 為臨界閾值模型的湧現性質、臨界代謝物（[Pi]）才是本體、CP 為邊界層（Pethick）。）
- [[source-Goulding-2022-determinants-of-CP]]（CP 決定因子綜述：對流／擴散／利用三路各為獨立決定因子、與纖維型/肌肉量/招募交互；§17–18 一節即源於此。）
- [[source-Burnley-2011-priming-power-duration]]（易誤解 #8：heavy（<CP）預熱抬高 W′~17% 而 CP 不變 → CP 對未致疲勞介入穩健、CP 與 W′ 可分離操弄。）
- [[source-Black-2023-dynamic-power-duration]]（§19–20 與易誤解 #7：CP 非恆定——全力 3MT 後 EP↓7%、2 小時重度運動後 ↓9%（Clark，糖原相關）、但短時嚴重 CWR 力竭後不降（Ferguson）；「CP 恆定」是 W′BAL 模型會被違反的關鍵假設、durability 維度。）
- [[source-Ventura-2023-severe-extreme-tolerance]]（易誤解 #9：t_lim = W′/(P−CP) 在 severe 域準、進入 [[Extreme intensity domain|extreme 域]]（>[[Maximal intensity for VO2max attainment|IHIGH]]）高估且愈高愈不準；CP SEE~4.5% vs W′ SEE 14–17%、兩試驗配適在 IHIGH+5% 顯著高估。）
- [[source-Sreedhara-2019-power-models-survey]]（§21–22：兩參數模型的歷史代數形式（Monod-Scherrer 線性功-時間、Moritani P vs 1/t、Whipp 雙曲線）與兩個破綻（t→0 時 P→∞、CP 假設無限），分別催生 [[Three-parameter critical power model|三參數]] 與 [[Exponential power-duration models|指數型]] 模型；W′ 跨模型分歧而 CP 相近；CP/W′ 帶 [[Intra-individual variability of critical power and W prime|IIV]]。）
- [[source-Chidnok-2013-exhaustion-recovery-domain]]（§13a：CP 作為肌內代謝閾值的「恢復向」證據——力竭後 <CP 恢復使 [PCr] 40→76%、pH→7.0、Pi/ADP 下降可續 10 分；>CP 恢復（降 19% 仍 >CP）代謝物完全不回補、僅再撐 39 s；被動 [PCr]→96%。CP 分隔「力竭後能不能逆轉回補」。）
- [[source-Jones-2010-CP-implications]]（地標級 CP 綜述、本頁多處主張的一手源頭：CP≈80% VO2max 且落在 GET 與 VO2max 之間（Poole et al.）、CP 之上每個強度經 [[VO2 slow component|慢成分]]達 VO2max、力竭時固定 [PCr]/pH 終點（³¹P-MRS, Jones et al. 2008）、hyperoxia 升 CP 降 W′ 呈反相關 r=−0.88（Vanhatalo et al.）、兩參數模型八條假設與 Monod-Scherrer／Moritani 線性形式、CP 為與 GET/VO2max/效率並列的「第四個有氧參數」。歷史上「CP 在 VO2max 之上（Wilkie）vs CP=AT（Moritani）」之爭由本綜述判定：CP 是高於 LT/GET、但不超過 VO2max 對應功率的獨立參數。）
