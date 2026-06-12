---
type: concept
aliases: [動脈CO2分壓, 動脈二氧化碳分壓, PaCO2, 動脈CO2壓力, arterial CO2 pressure, arterial PCO2, PaCO₂]
tags: [exercise-physiology, gas-exchange, acid-base]
sources: [source-Yano-1997-CO2-output-model]
prerequisites: [二氧化碳輸出量（VCO2, carbon dioxide output）, 分鐘通氣量（minute ventilation, VE）]
created: 2026-06-12
updated: 2026-06-12
---

# 動脈 CO₂ 分壓（arterial CO₂ pressure, PaCO₂）

## 本質（一句話）
PaCO₂ 是「剛離開肺、進入動脈的血裡，CO₂ 有多少壓力」——而這個數字其實是一個**比值**：你**產生**多少 CO₂ ÷ 你**呼掉**多少。身體會死守它在 ~40 mmHg，直到劇烈運動時為了排酸而呼過頭，才把它壓下去。

## 前置概念
- [[VCO2|二氧化碳輸出量（VCO2, carbon dioxide output）]]
  （PaCO₂ 的分子是「產生多少 CO₂」；先懂 V̇CO₂。）
- [[Minute ventilation|分鐘通氣量（minute ventilation, VE）]]
  （PaCO₂ 的分母是「呼掉多少」；先懂 V̇E＝每分鐘搬動多少空氣，以及它的有效部分 V̇_A。）

## 為什麼會這樣（first-principles 推導）
1. 身體一直在產 CO₂（[[Cellular respiration|燒食物]]的廢氣），必須從肺呼掉。問：動脈血裡 CO₂ 最後會停在什麼壓力？
2. 把「進」與「出」寫成一條關係：肺泡（≈動脈）的 CO₂ 壓力 ＝ **產生速率 ÷ 有效通氣速率**，即 **PaCO₂ ≈ K · V̇CO₂ / V̇_A**（V̇_A＝肺泡通氣量，是 [[Minute ventilation|V̇E]] 扣掉無效死腔後真正參與交換的部分；K 是換算常數）。這就是它「是一個比值」的意思。
3. 讀這條式子：
   - 產得多、呼得不夠 → 比值升 → PaCO₂ **升**（CO₂ 積在血裡，叫換氣不足 hypoventilation）。
   - 呼得比產得還猛 → 比值降 → PaCO₂ **降**（CO₂ 被洗出，叫 [[Exercise hyperventilation|過度換氣]]）。
4. **為什麼休息到中等運動 PaCO₂ 幾乎不動（≈40 mmHg）？** 因為通氣會**跟著** CO₂ 產量等比例上調——產得多就呼得多，分子分母一起漲，比值不變。這不是巧合，是身體**主動把 PaCO₂ 鎖在設定點**（它直接決定血液酸鹼：CO₂＋H₂O⇌H⁺＋HCO₃⁻，PaCO₂ 升＝偏酸）。Yano 的資料正是如此：休息 39.2、到 1080 kpm/min 仍 40.8，**沒有顯著變化**。
5. **什麼時候 PaCO₂ 才掉下來？** 高負荷堆乳酸、血變酸後，身體**呼得超過排自身 CO₂ 所需**（多呼是為了用「吹掉 CO₂＝降酸」來代償乳酸酸中毒）→ 分母 V̇_A 衝過分子 V̇CO₂ → PaCO₂ **下降**。Yano 資料：力竭時降到 35.5 mmHg（p<0.001）。
6. **接回本份模型**：在 [[Yano model of CO2 output pathway|Yano 模型]]裡，把休息那個被鎖住的值取名 **base PaCO₂**，當成切「非乳酸 vs excess」的基準；而高負荷時 PaCO₂ **跌破 base** 的那一截，本身就是 excess V̇CO₂ 的來源之一（呼過頭、額外洗掉一批存著的 CO₂）。
7. 量測：嚴格要動脈採血；實務上常用 [[End-tidal CO2|潮氣末 CO₂（P_ETCO₂）]]＋校正式（如 Jones 1979）來**估** PaCO₂——Yano 即用此法。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Yano（1997）以 PaCO₂ 在低負荷恆定、高負荷下降，作為模型把 V̇CO₂ 切成兩段的依據——恆定段對應非乳酸 V̇CO₂，下降段對應 excess V̇CO₂「來自 PaCO₂ 降」那一支（模型要點 4）。
- **背後的推理／證據**：恆定 ≈40 mmHg 來自通氣與 CO₂ 產量等比例耦合（肺泡通氣方程）；力竭時顯著下降（39.2→35.5）由過度換氣解釋。PaCO₂ 由 P_ETCO₂ 經 Jones 1979 迴歸式推得。

## 易誤解之處
1. **PaCO₂（動脈）≠ Pv̄CO₂（混合靜脈）。** 動脈是剛出肺、被通氣壓低的一端（~40，運動末更低）；[[Mixed venous CO2 pressure|靜脈]]是載滿組織廢氣回肺的一端（運動時可飆到近 100）。兩者差很大，是 CO₂ 一趟運輸的「卸貨前 vs 載貨後」，別混。
2. **PaCO₂ 下降不代表 CO₂ 產得少——剛好相反。** 它代表「呼得比產得更兇」（過度換氣排酸）。把「壓力降」讀成「產量降」會完全相反。
3. **PaCO₂ 在寬範圍恆定是『被調控』，不是『剛好』。** 那是身體拿通氣去守住一個酸鹼設定點的結果；理解這點，才看得懂為何一旦設定點被乳酸打破（高負荷）它就被主動拉低。
4. **它是分壓不是含量。** PaCO₂ 是壓力（驅動力）；血實際載多少 CO₂ 要回到 [[Blood CO2 dissociation curve|解離曲線]]讀含量。

## 用生活例子再講一次
想像一個一直在滴水的水龍頭（CO₂ 產量），底下水槽有個排水孔（通氣）。水位高低（PaCO₂）＝進水 ÷ 排水。平常你會把排水孔開到剛好配進水，水位穩穩停在一格（≈40 mmHg）——進水變大你就把孔開大，水位不動。但某天水質變糟（血變酸），你乾脆把排水孔開到比進水還大去沖洗，水位就掉到一格以下（PaCO₂ 降）。看到水位掉，不是進水變少，是你**故意排得更兇**。

（失準之處：水位是純物理進出比，PaCO₂ 還同時是身體的酸鹼旋鈕——它被「守住」是因為它直接定 pH，這層「為了酸鹼而調」的目的性，單純水槽沒有。）

## 換句話說
換句話說，PaCO₂ 是動脈血的 CO₂ 壓力，等於「產 CO₂÷呼 CO₂」這個比值。通氣會跟著產量走，所以從休息到中等運動它被鎖在 ~40 mmHg（叫 isocapnia）；只有到高負荷、身體為了中和乳酸而[[Exercise hyperventilation|呼過頭]]，分母超過分子，它才跌破基準。那個被鎖住的休息值就是 [[Yano model of CO2 output pathway|Yano 模型]]的 **base PaCO₂**，而它跌破基準的那一截，是 [[Excess CO2 output|過量 CO₂]] 的來源之一。

## 來源
- [[source-Yano-1997-CO2-output-model]]（Results：PaCO₂ 休息 39.2→1080 kpm 40.8（無顯著變化）→力竭 35.5（p<0.001）；§2.3 以 P_ETCO₂＋Jones 1979 式估 PaCO₂；模型要點 2、4。）
