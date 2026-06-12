---
type: concept
aliases: [碳酸氫根緩衝, 碳酸氫鹽緩衝, 乳酸的碳酸氫根緩衝, 重碳酸鹽緩衝, bicarbonate buffering, HCO3 buffering, bicarbonate buffering of lactic acid]
tags: [exercise-physiology, acid-base, metabolism]
sources: [source-Beaver-1986-V-slope, source-Peronnet-2006-CO2-hyperventilation, source-Yunoki-1999-excess-CO2-kinetics, source-Stringer-1995-VCO2-VO2-CWR, source-Wooten-2021-respiratory-buffering-fatigability, source-Hirakoba-1996-lactate-prediction-excess-CO2]
prerequisites: [乳酸（lactate / lactic acid）與它的產生, 二氧化碳輸出量（VCO2, carbon dioxide output）]
created: 2026-06-10
updated: 2026-06-12
---

# 碳酸氫根對乳酸的緩衝（bicarbonate buffering of lactic acid）

## 本質（一句話）
當運動產生乳酸、血裡多出酸（H⁺）時，身體拿「碳酸氫根」這個鹼去中和它；中和的化學後果是**逼出一批額外的 CO₂**——每中和 1 毫當量乳酸，大約擠出 22 毫升 CO₂。

> ⚠️ 本頁主體是 Beaver/Wasserman（1986）的經典觀點，也是整套氣體交換偵測閾值方法的化學說法。其中「緩衝會**新生** CO₂」「碳酸氫根是肌肉主要緩衝劑」「碳酸氫根降幅≈乳酸升幅」三點，已被 Péronnet & Aguilaniu（2006）以質量守恆與直接量肌肉的證據**重估**——見下方易誤解 #4–6。兩造來源並陳，方法本身（V-slope）不受影響。

## 前置概念
- [[Lactate|乳酸（lactate）與它的產生]]
  （要懂在緩衝什麼，得先懂乳酸帶來的那份酸 H⁺ 從哪來。）
- [[VCO2|二氧化碳輸出量（VCO2, carbon dioxide output）]]
  （緩衝的後果是多出 CO₂，最後從肺呼出、被 VCO2 量到；先懂 VCO2 才接得上「為什麼能在呼吸裡看到」。）

## 為什麼會這樣（first-principles 推導）
1. 由 [[Lactate|乳酸]]：強運動時走無氧捷徑，產生乳酸並釋出氫離子 H⁺。H⁺ 多＝變酸。
2. 酸太多會干擾酵素、傷害細胞，身體不能放任 pH 掉下去，必須馬上中和。中和酸要用鹼。
3. 身體體液裡最主要、量最大的鹼，是**碳酸氫根（bicarbonate，HCO₃⁻）**。先用一句話定義：HCO₃⁻ 是血液裡隨時待命、專門吃掉多餘 H⁺ 的「鹼性海綿」。
4. 中和反應一步步看（這是本頁的核心，放慢）：
   - H⁺ ＋ HCO₃⁻ → H₂CO₃（碳酸）。多餘的酸先被碳酸氫根接走，變成碳酸。
   - H₂CO₃ → H₂O ＋ CO₂。碳酸不穩，立刻拆成水和**二氧化碳**。
   - 淨結果：一個 H⁺ 被中和，就「變出」一個 CO₂ 分子。
5. 所以「乳酸一上升 → H⁺ 一上升 → 被 HCO₃⁻ 中和 → 必然多生一批 CO₂」。這批 CO₂ 是被酸「逼」出來的，**不是燒食物來的**——它疊加在正常代謝的 CO₂ 之上。這多出來的部分，就叫 [[Excess CO2 output|過量 CO₂]]。
6. 量化它：文獻給出大約「每 1 毫當量（meq）乳酸，被緩衝後產生約 22 mL 的 CO₂」。重點不是死記 22，而是理解「乳酸的累積，會以一個近乎固定的比例，轉成可被偵測的額外 CO₂」——正因為比例穩定，這份 CO₂ 才能當作乳酸累積的可靠替身。**這個「近乎固定的比例」正是反推的鑰匙**：把它逐人實測（個人匯率 [[CO2 excess per unit lactate|CO₂ excess-ΔLa]]，因緩衝化學打折又受體能微調而需校準），就能從呼吸裡的[[Excess CO2 output|過量 CO₂]]無創**反推血乳酸累積量**（[[Lactate prediction from excess CO2 output|用過量 CO₂ 預測乳酸]]，Hirakoba 1996）。（**重估警示**：Péronnet 2006 指出這 22 mL 並非肌肉「現做」的新 CO₂，而是先存成碳酸氫根、之後再放出的同一批——嚴格說緩衝不增加 CO₂ 總量；見易誤解 #5、[[Nonmetabolic CO2|非代謝 CO₂]]。下游用「過量 CO₂」偵測閾值或反推乳酸仍可行，但機制解讀要修正。）
7. 推到底：這批額外 CO₂ 隨血流回肺、被呼出，於是 [[VCO2|VCO2]] 在乳酸開始堆的那一刻起，會「比 VO2 多漲一截」。**不必抽血，光看呼出的 CO₂，就能間接看到乳酸在堆。** 這是整套用氣體交換偵測閾值方法的物理化學基礎。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Beaver 等人明言——「運動使乳酸增加時會產生過量 CO₂，因為它的 H⁺ 主要由 HCO₃⁻ 緩衝（每 1 meq 乳酸約 22 mL）」，並據此主張用無創的氣體交換來偵測 [[Anaerobic threshold|無氧閾值]]。
- **背後的推理／證據**：理由就是第 4–6 步的化學必然性——碳酸氫根是體液主要緩衝鹼，中和酸「一定」副產 CO₂。正因為這一步是強制性的（obligatory），「乳酸上升」和「CO₂ 多漲」之間才有可信賴的因果，不是巧合。

## 易誤解之處
1. **這批 CO₂ 不是「呼吸變多吸進來的」，是化學反應「現做」出來的。** 它源自碳酸的分解，和燒食物無關；把它和代謝 CO₂ 混為一談，就會看不懂為什麼 VCO2 會突然多漲。
2. **緩衝是「先擋一下」，不是「解決乳酸」。** HCO₃⁻ 中和的是酸（H⁺），代價是自己被消耗、且把問題轉成必須排掉的 CO₂。所以緩衝時血中 HCO₃⁻ 會下降——這個下降本身也是一個可量的閾值訊號（HCO₃⁻ threshold）。
3. **「22 mL/meq」是近似值、是平均比例，不是精準守恆律。** 它夠穩到能拿來偵測，但別當成每次都剛好的定律。
4. **【現代重估｜Péronnet 2006】碳酸氫根其實不是肌肉裡的主要緩衝劑。** Beaver 等人由血液數據推得「碳酸氫根緩衝約 92% 的肌肉 H⁺」，但直接量肌肉的證據（Hultman & Sahlin 1980、³¹P-MRS）顯示：碳酸氫根在肌肉內最多只緩衝約 **18–25%** 的 H⁺ 負荷；真正的主力是**蛋白質（約 31%）**與[[Phosphocreatine|磷酸肌酸分解]]（約 29%），[[Muscle carnosine|肌肽]]約 4%、磷酸約 8%。兩造來源並陳（Beaver 1986 ↔ Péronnet 2006）。
5. **【現代重估｜Péronnet 2006】「緩衝現做新 CO₂」是質量守恆的誤解。** 推導第 4 步看似「中和→生出一個 CO₂」，但那個碳酸氫根本身來自先前代謝的 CO₂；把整條反應式寫全，前後 CO₂ 數目不變。所以嚴格說緩衝**不增加 CO₂ 總量**，只是把代謝 CO₂ 先存成碳酸氫根、之後再放出。詳見 [[Nonmetabolic CO2|非代謝 CO₂]]。你最終在嘴巴量到的那批 [[Excess CO2 output|過量 CO₂]]，來自 [[Body CO2 stores|身體碳酸氫根庫]]被低 pH 與[[Exercise hyperventilation|過度換氣]]放出來，而非肌肉新生。
6. **【現代重估｜Péronnet 2006】血漿（標準）碳酸氫根的下降不是乳酸上升的 1:1 鏡像。** 經典模型主張「標準碳酸氫根降幅 ≈ 乳酸升幅」（1:1），用以支持「碳酸氫根進肌肉緩衝乳酸」。但彙整 38 研究 106 點顯示兩者只**鬆散**相關、且乳酸愈高差距愈大（標準碳酸氫根最多降約 24，乳酸可升約 30 mmol/L）。原因：標準碳酸氫根由 pH 與 P_aCO₂ 唯一決定，而 pH/P_aCO₂ 與乳酸的關係本就鬆散（受個人通氣反應強弱左右，「responder vs nonresponder」、McArdle 病等可完全脫鉤）。
7. **【時間軸｜Yunoki 1999】緩衝該放的 CO₂ 會「延遲」出現，運動中甚至被遮蔽。** 中和雖在運動中持續發生（乳酸從第一秒起等速產，Fig 3），但運動中升高的 P_CO₂ 會把這條反應暫時往**左**頂（CO₂ 被壓回 [[Body CO2 stores|庫]]存著），使該放的 CO₂ 延到運動後、[[Exercise hyperventilation|過度換氣]]時才湧出（停後 ~60 s 達峰）。所以「中和 → 放 CO₂」在**時間上不是即時對應**，但**總量仍守恆**（excess CO₂ ∝ 乳酸）。完整見 [[Excess CO2 output kinetics|過量 CO₂ 輸出的動力學]]。
8. **【應用｜Wooten 2021】緩衝不只「讓你運動撐得久」，也「保護你的恢復」。** 一般把緩衝想成「中和酸→延後力竭」，這只說了一半。運動**停下來後**的復原主要是有氧工作（補 [[Phosphocreatine|PCr]]，見 [[Phosphocreatine resynthesis]]），而未被清掉的 H⁺ 會**抑制恢復期的氧化磷酸化**與橫橋作用。所以緩衝能力強（清酸快）的人，不只撐得久（[[Performance fatigability|表現疲勞性低]]），[[Gas exchange recovery kinetics|恢復動力學]]也更快。緩衝能力的代理量 [[Excess CO2 output|excess V̇CO₂]] 因此能同時連結「耐操」與「復原快」兩端。

## 用生活例子再講一次
想像泳池水質開始變酸（乳酸堆積放出 H⁺）。管理員撒小蘇打（碳酸氫根）中和。小蘇打和酸一反應，會冒出氣泡——那氣泡就是 CO₂。你站在池邊，就算看不到水裡的酸度計，只要看到「開始冒氣泡、而且愈冒愈多」，就知道水正在變酸、管理員正在拼命中和。VCO2 的「多漲一截」，就是你看到的那串氣泡。

（失準之處：泳池是一次性撒料，身體是持續動態地產酸與中和；而且身體的 HCO₃⁻ 是有限庫存，中和久了會見底——這對應到運動後段更激烈的代償反應。）

## 換句話說
換句話說，乳酸帶來的酸被碳酸氫根中和，而中和的「廢氣」正好是 CO₂。於是體內一個看不見的化學事件（變酸、中和）被翻譯成一個看得見的呼吸訊號（多吐 CO₂）。這個翻譯比例還相當穩定，所以我們能反過來，從呼出的 CO₂ 推回血裡的乳酸正在累積——這就是為什麼一根咬嘴、一台氣體分析儀，就能取代抽血去找代謝轉折。

## 來源
- [[source-Beaver-1986-V-slope]]（摘要與引言：乳酸 H⁺ 主要由 HCO₃⁻ 緩衝、每 meq 約 22 mL CO₂，為過量 CO₂ 與 V-slope 法的化學基礎。）
- [[source-Peronnet-2006-CO2-hyperventilation]]（§2、§3、§4 的批判性重估：碳酸氫根僅緩衝肌肉 H⁺ 約 18–25%、緩衝不新生 CO₂（質量守恆）、標準碳酸氫根非乳酸的 1:1 鏡像。對應易誤解 #4–6。）
- [[source-Yunoki-1999-excess-CO2-kinetics]]（時間軸：升高的 P_CO₂ 把中和反應暫時往左頂、遮蔽緩衝 CO₂，使其延到運動後才湧出；總量仍 ∝ ΔLa。對應易誤解 #7。）
- [[source-Wooten-2021-respiratory-buffering-fatigability]]（DISCUSSION：未緩衝的 H⁺ 抑制橫橋與恢復期氧化磷酸化，故緩衝能力同時左右耐受與恢復；excess V̇CO₂ 調節恢復↔疲勞性關係。對應易誤解 #8。）
- [[source-Hirakoba-1996-lactate-prediction-excess-CO2]]（22 mL/meq 的近固定比例＝反推乳酸的化學基礎；逐人校準成 CO₂ excess-ΔLa 後可由過量 CO₂ 預測血乳酸累積（r＝0.954）。對應推導 #6、見 [[Lactate prediction from excess CO2 output]]、[[CO2 excess per unit lactate]]。）
