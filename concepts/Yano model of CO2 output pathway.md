---
type: concept
aliases: [Yano模型, Yano CO2輸出模型, 遞增運動CO2輸出路徑模型, CO2輸出路徑模型, Yano model of CO2 output, CO2 output pathway model, non-lactic VCO2, 非乳酸VCO2]
tags: [exercise-physiology, gas-exchange, acid-base, model]
sources: [source-Yano-1997-CO2-output-model]
prerequisites: [血液CO2解離曲線（blood CO2 dissociation curve）, 混合靜脈CO2分壓（mixed venous CO2 pressure, PvCO2）, 動脈CO2分壓（arterial CO2 pressure, PaCO2）, 過量二氧化碳（excess CO2 output）]
created: 2026-06-12
updated: 2026-06-12
---

# Yano 的遞增運動 CO₂ 輸出路徑模型（Yano model of CO₂ output pathway）

## 本質（一句話）
這個模型把「遞增運動時嘴巴吐出的 CO₂（V̇CO₂）為什麼那樣上升」畫成**血液 CO₂ 解離曲線上的一段運輸**：CO₂ 從組織（高壓）循曲線載到肺（低壓）卸下，而這段運走量可以乾淨地切成兩塊——**非乳酸 V̇CO₂**（靜脈端壓力升高貢獻的）＋ **excess V̇CO₂**（血變酸使曲線右移、加上動脈端被過度換氣壓低貢獻的）。

## 前置概念
- [[Blood CO2 dissociation curve|血液CO2解離曲線（blood CO2 dissociation curve）]]
  （整個模型就是在這條曲線上讀「組織端含量 − 肺端含量」；先懂這條曲線與它因酸右移。）
- [[Mixed venous CO2 pressure|混合靜脈CO2分壓（mixed venous CO2 pressure, PvCO2）]]
  （運輸的「載貨端」壓力，驅動非乳酸那一塊；先懂它。）
- [[Arterial CO2 pressure|動脈CO2分壓（arterial CO2 pressure, PaCO2）]]
  （運輸的「卸貨端」壓力，它跌破基準貢獻 excess 那一塊；先懂它與 base PaCO₂。）
- [[Excess CO2 output|過量二氧化碳（excess CO2 output）]]
  （模型把 V̇CO₂ 切出的第二塊就是它；先懂過量 CO₂ 是什麼訊號。）

## 為什麼會這樣（first-principles 推導）
一步步把 Fig. 5 的那張圖在腦中蓋出來：

1. **設定座標。** 橫軸＝血的 CO₂ 分壓 P_CO₂，縱軸＝血的 CO₂ 含量（Vol %）。在這張圖上畫 [[Blood CO2 dissociation curve|血液 CO₂ 解離曲線]]。CO₂ 一趟運輸＝血從某個（高壓、高含量）點，移到另一個（低壓、低含量）點，**兩點的含量差**＝這份血替你運走、最後呼掉的 CO₂。

2. **標三個壓力點。** 在橫軸上：
   - [[Mixed venous CO2 pressure|Pv̄CO₂]]（靜脈載貨端，運動時可到 ~100 mmHg）——最右。
   - **base PaCO₂**（≈休息時被鎖住的動脈值，~40 mmHg）——中間。
   - 實際 [[Arterial CO2 pressure|PaCO₂]]（卸貨端；高負荷被[[Exercise hyperventilation|過度換氣]]壓到 35 mmHg 以下）——最左。

3. **第一塊：非乳酸 V̇CO₂。** 先假裝血沒變酸（曲線不右移）。把血從 Pv̄CO₂ 載到 base PaCO₂，在**同一條曲線**上讀兩點含量之差——這塊就是「與乳酸無關、純粹因為靜脈端壓力比動脈基準高」而運走的 CO₂。它由 Pv̄CO₂ 決定（Yano：非乳酸 V̇CO₂＝0.051·Pv̄CO₂−2.23，r=0.950），對應燒食物的代謝 CO₂ 那條可預期斜率。

4. **第二塊：excess V̇CO₂——它有兩個來源，都疊在第一塊之外。**
   - **(a) 曲線右移（dextroversion）**：高負荷堆乳酸 → H⁺ 消耗碳酸氫根 → [[Blood CO2 dissociation curve|解離曲線右移]]＝同壓力下血載得更少。於是在肺端，血落在「右移後較低的含量」上，比沒右移時**多卸一截**。這一截與乳酸量綁定。
   - **(b) PaCO₂ 跌破 base**：過度換氣把卸貨端壓力從 base PaCO₂（40）再往下壓到實際 PaCO₂（35.5）→ 卸貨端在曲線上更往左下、含量又更低 → **再多卸一截**。
   兩者相加＝excess V̇CO₂（Fig. 5 的陰影帶）。把它沿運動時間積分，就得 **CO₂ excess**，Yano 量到它與血乳酸增量 ΔLa 顯著相關（r=0.828）。

5. **一個關鍵後果：A-V 含量差在肺端比在組織端大。** 血在組織裝貨時曲線還沒右移（或右移較少）；流經肺、且因酸右移後，同樣的壓力落差對應的含量差被拉大。所以「血在肺實際卸掉的 CO₂」會多於「組織當時倒進去的」——多出來的，就是先前存成碳酸氫根、被酸頂出來的既存 CO₂。

6. **模型的四個要點（Yano 原文總結）**：(1) 用血液 CO₂ 解離曲線當把 CO₂ 從組織運到肺的**向量**；(2) 立一個 **base PaCO₂** 來切非乳酸 vs excess；(3) 乳酸造成的曲線**右移**連到 excess V̇CO₂；(4) **PaCO₂ 下降**連到「從組織端額外移走的」excess V̇CO₂。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Yano（1997）主張 V̇CO₂ 的上升可由「組織→血→肺、循解離曲線」這條運輸路徑完整解釋；把 V̇CO₂ 拆成由 Pv̄CO₂ 驅動的非乳酸段、與由曲線右移＋PaCO₂ 降驅動的 excess 段。
- **背後的推理／證據**：V̇CO₂ 對 Pv̄CO₂＋PaCO₂ 多元相關 R=0.971；非乳酸 V̇CO₂ 對 Pv̄CO₂ 單迴歸 r=0.950；CO₂ excess 對 ΔLa r=0.828；解離曲線右移引 Miyamura & Honda 1978 實測。把這些拼起來，「壓力↔含量↔運走量」這條鏈在資料上對得起來。

## 易誤解之處
1. **【機制需在 Péronnet 2006 下讀】「從組織移走 CO₂ 以利緩衝」「右移 ＝ 新增 CO₂」是舊 Wasserman 學派語言，要修正。** 質量守恆下，緩衝**不新生** CO₂（見 [[Nonmetabolic CO2]]）。但 Yano 模型的核心機制其實**與修正後的圖像相容**：曲線右移＝「酸使血在給定壓力下少載 CO₂、於是把先前存成碳酸氫根的既存 CO₂ 頂出來卸掉」——這正是 Péronnet 說的「從 [[Body CO2 stores|碳酸氫根庫]]釋放」，不是肌肉現做新碳。要丟的只是「字面新生」那層說法，運輸幾何本身站得住。
2. **base PaCO₂（40）vs 非乳酸外推值（43.7）的小落差不是矛盾。** Yano 自己指出：用「分壓線性外推」本就不精確（曲線在低壓段彎），嚴謹要回到含量。所以他改用「休息 PaCO₂ 當 base」沿解離曲線來切，而非死守 43.7。
3. **excess V̇CO₂ 有兩個來源（曲線右移＋PaCO₂ 降），別只記乳酸。** 即使 PaCO₂ 沒掉（等於 base），光是曲線右移就能產生 excess；反過來，過度換氣壓低 PaCO₂ 也獨立貢獻一塊。兩條可分開存在。
4. **這是「壓力—含量」的穩態幾何，不是時間動力學。** 本模型講遞增運動各負荷下的量級關係；CO₂ 在時間軸上被庫拖慢、運動中轉負、停後達峰那套，是 [[Excess CO2 output kinetics]]／[[Muscle-to-lung gas exchange dissociation]] 的事，別混。
5. **小樣本警示。** n=8、高負荷僅 3 人出現 excess V̇CO₂、Pv̄CO₂/PaCO₂ 皆間接估算；屬模型建構，非大樣本驗證。

## 用生活例子再講一次
把一份血想成沿軌道跑的**纜車**，軌道就是 [[Blood CO2 dissociation curve|解離曲線]]。在山下車間（組織）裝貨到「滿載刻度」Pv̄CO₂，開到山上工廠（肺）卸到「基準刻度」base PaCO₂——這兩刻度之間卸下的貨，是**非乳酸 V̇CO₂**（看裝得多滿，即 Pv̄CO₂ 多高）。現在加兩個變化：(a) 半路有人把車廂層架拆掉（乳酸使曲線右移），到廠時同刻度下車廂裝不住、多掉一批；(b) 工廠把卸貨平台又降低一截（過度換氣壓低 PaCO₂），逼車再多吐一批。這兩批多卸的，合起來就是 **excess V̇CO₂**。它們不是路上新長的貨，是車本來就裝不穩、被逼提早卸的存貨。

（失準之處：纜車載量與刻度成正比，真實曲線是彎的、且「拆層架」是碳酸氫根被 H⁺ 化學消耗＋血紅素氧合（Haldane）一起作用，比機械拆架細緻；且這是穩態量級圖，不含時間延遲。）

## 換句話說
換句話說，Yano 模型把遞增運動的 V̇CO₂ 上升，畫成「血循 CO₂ 解離曲線、從靜脈高壓端載到動脈低壓端」的一段運輸。第一塊是 **非乳酸 V̇CO₂**：靜脈端 [[Mixed venous CO2 pressure|Pv̄CO₂]] 越高、A-V 含量差越大（對應燒食物的代謝 CO₂）。第二塊是 **excess V̇CO₂**：血變酸使曲線**右移**（同壓力少載、肺端多卸）＋[[Exercise hyperventilation|過度換氣]]把 [[Arterial CO2 pressure|PaCO₂]] 壓破 base（卸貨端更低、再多卸），兩者相加、積分後 ∝ 乳酸（r=0.828）。它和 [[Excess CO2 output|過量 CO₂]] 講的是同一件事，只是 Yano 給了它「在解離曲線上長什麼樣」的運輸圖——而這張圖，在丟掉「肌肉現做新碳」那層字面後，恰好與 [[Nonmetabolic CO2|Péronnet 的庫存釋放修正]]接得上。

## 來源
- [[source-Yano-1997-CO2-output-model]]（§4.1–4.3 與 Fig. 1、5：模型四要點；非乳酸 V̇CO₂＝0.051·Pv̄CO₂−2.23（r=0.950）、外推 43.7 mmHg；CO₂ excess 對 ΔLa r=0.828；R=0.971 多元相關；引 Miyamura & Honda 1978 解離曲線右移。）
