---
type: source
tags: [exercise-physiology, critical-power, W-prime, modelling, performance, methods, review]
created: 2026-06-12
---

# 來源：A survey of mathematical models of human performance using power and energy

## 出處
- **檔名**：`A survey of mathematical models of human performance using power and energy`（原始資料夾）
- **作者／年份**：Sreedhara, V. S. M.; Mocko, G. M.; Hutchison, R. E.（2019）
- **期刊**：*Sports Medicine - Open* **5**:54，doi:10.1186/s40798-019-0230-z（open access, CC BY）
- **單位**：Clemson University（機械工程）＋ Furman University（健康科學）
- **類型**：綜述（review article）；功率為基礎的人體表現（疲勞與恢復）數學模型總覽
- **備註**：本團隊即已 ingest 的 [[source-Sreedhara-2020-recovery-W-prime-domain|Sreedhara 2020（配速最佳化）]]的同一群作者；本篇是其**前作綜述**，鋪設了 2020 實作的概念背景。

## 核心主張
功率為基礎的人體表現模型裡，**兩參數 [[Critical power|CP]]–[[W prime|W′]] 模型因簡單而最流行**，但它有兩個破綻（t→0 時 P→∞、CP 假設可無限維持），催生了[[Three-parameter critical power model|三參數]]與[[Exponential power-duration models|指數型]]等更準但參數更多的模型；更關鍵的是，**現有所有方法都只給「擬合貼合度（SEE）」、抓不到 CP/W′ 的「日間個體內變異（[[Intra-individual variability of critical power and W prime|IIV]]）」**，而 W′ 還額外**依模型而變**——這兩個缺口（IIV 與一個可靠的 W′ **回填**模型）正是把表現模型推向「即時、個人化最佳化」前必須補上的。

## 內容地圖（按小節）
- **Modeling Performance Using Power**：CP 概念史（Hill → Monod-Scherrer → Moritani → Whipp）與兩參數模型的代數形式（W=CP·t+W′、P=W′/t+CP、t=W′/(P−CP)）；兩破綻；alternate 全曲線模型——Ward-Smith（熱力學）、Hopkins（坡度）、Péronnet-Thibault（60 m–全馬、MAP 僅撐 ~7 min）、Weyand、Morton 指數版；[[Three-parameter critical power model|三參數模型]]（t=W′/(P−CP)+k）。Table 1：同筆資料下三模型 CP 相近（176/165/205 W）但 W′ 分歧（29.1/47.9 kJ/NA）。
- **Methods and Protocols to Estimate CP and W′**：CWR 多趟（3–5）、ramp（Morton T=CP/S+√(2W′/S)）、[[3-minute all-out test|3MT]]（Vanhatalo）。→ [[Critical power estimation protocols]]
- **Limitations of the Protocols**：預測試時長（短趟 CP/W′ 偏高，Bishop/Jenkins）、踏頻（60 vs 100 rpm）、SEE≠IIV、3MT 的 Bland-Altman CP ±15 W（=2700 J W′）、Triska 重複 TT 之 ICC/CV。→ [[Intra-individual variability of critical power and W prime]]
- **Adding Recovery to the Two-Parameter Model**：Morton 水力學水箱、Morton-Billat 間歇式（eq.16）、Ferguson 曲線回填、Skiba W′BAL 積分（eq.17–18，τ_W′=546·e^(−0.01·D_CP)+316）與三種形式（du/dt/單位 Joule-second）、biconditional/ODE（eq.19）。
- **Applications / Research Opportunities / Conclusions**：energy management、peloton 減阻 ~40%、Breaking2／sub-2h marathon、士兵任務、團隊運動、穿戴感測；研究機會表（groups vs individuals、W′ 的模型依賴、IIV、回填模型、最佳化、穿戴、團隊、健康）。

## 本份新增／更新的概念
**新增（4）：**
- [[Critical power estimation protocols]]（新增）— CWR／ramp／3MT 三種估計協定、代數形式、W′ 跨模型分歧、預測試時長與踏頻效應。
- [[Three-parameter critical power model]]（新增）— Morton t=W′/(P−CP)+k；k=W′/(CP−Pmax)<0；封頂 Pmax、修 t→0 時 P→∞。
- [[Exponential power-duration models]]（新增）— Ward-Smith/Hopkins/Péronnet-Thibault/Weyand/Morton 指數族；整條曲線指數描述、bound Pmax 與（Péronnet-Thibault）有限時間有氧；給不出乾淨 W′。
- [[Intra-individual variability of critical power and W prime]]（新增）— 本綜述核心命題；SEE≠IIV、需重複測、3MT ±15 W=2700 J、Triska CV 2.6%/8.2%。

**更新（6）：**
- [[Critical power]]（§21–22：兩參數模型的代數形式與兩破綻，分別催生三參數/指數模型；W′ 跨模型分歧）。
- [[W prime]]（易誤解 #9：W′「elusive」、同筆資料不同模型 W′ 差六成）。
- [[3-minute all-out test]]（易誤解 #6：3MT 的 trial-to-trial 變異 ±15 W=2700 J、單次無 W′ 標準誤）。
- [[Phenomenological vs mechanistic models]]（補一個「準確 vs 精簡」的 worked example：2-param 簡單有破綻 vs 3-param/指數準但參數多）。
- [[Critical power pacing optimization]]（同團隊前作，框出即時最佳化的兩前提：可靠回填模型＋量化 IIV）。
- （恢復模型 eq.16/17–19 與 Morton 水力學已分別由 [[Intermittent exercise critical power model]]、[[Integral W prime balance model]]、[[Differential W prime balance model]]、[[Mechanistic power-duration models]]（Skiba & Clarke 2021 那批）涵蓋，本份不重複編輯，僅在此標明連結。）

## 與既有知識的關係
- **補空白、非矛盾**：補進 wiki 既有 CP/W′ 層**缺的「模型形式與量測」面**——三參數、指數族、估計協定、IIV。與既有的 W′BAL 恢復模型族（[[Integral W prime balance model]]、[[Differential W prime balance model]]）一致：本篇獨立記載了同樣的 du/dt 差異與「積分項單位 Joule-second」不一致，呼應 [[source-Skiba-Clarke-2021-W-prime-balance-mathematics|Skiba & Clarke 2021]]。
- **與並行 ingest 的 [[source-Ventura-2023-severe-extreme-tolerance|Ventura 2023]] 相鄰互補**：對方建的 [[Critical power model fitting]] 講「配適／SEE 與 extreme 域高估」，本篇的 [[Critical power estimation protocols]] 講「協定選擇與 W′ 的模型依賴」——兩頁從不同角度談「CP/W′ 怎麼被量出來、為什麼會偏」，已互相連結。
- **誠實面**：本篇是**敘事綜述**（非系統性、無資料分析），主旨偏「指出缺口、倡議方向」（IIV 量化、回填模型、個人化、穿戴）。其結論「兩參數模型可靠範圍約 2 min–1 h」與並行 Ventura 2023「t_lim 公式進 extreme 域高估」一致。

## 圖
- **Fig. 1–2**：兩參數模型的雙曲線形式與線性轉換、t→0 時 P→∞ 的破綻。
- **Fig. 3 ＋ Table 1**：兩參數/三參數/指數三模型擬合同一筆 Gaesser 資料——CP 相近、W′ 分歧（最直接的「W′ 依模型而變」證據）。
- **Fig. 5**：重複 CWR 測試求 grand mean 以捕捉 IIV 的示意。
- **Fig. 7**：Morton 水力學水箱（<CP / >CP 兩水箱以固定管徑相連）。
