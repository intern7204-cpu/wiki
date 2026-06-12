---
type: concept
aliases: [通氣當量, 換氣當量, 通氣當量比, VE/VCO2, VE/VO2, 二氧化碳通氣當量, 氧氣通氣當量, ventilatory equivalent, ventilatory equivalent for CO2, ventilatory equivalent for O2]
tags: [exercise-physiology, ventilation, gas-exchange, CPET]
sources: [source-Yunoki-1999-excess-CO2-kinetics, source-Staes-2024-CPET-exercise-limitations]
prerequisites: [分鐘通氣量（minute ventilation, VE）, 二氧化碳輸出量（VCO2, carbon dioxide output）, 耗氧量（VO2, oxygen uptake）]
created: 2026-06-12
updated: 2026-06-12
---

# 通氣當量（ventilatory equivalent, V̇E/V̇CO₂、V̇E/V̇O₂）

## 本質（一句話）
通氣當量就是「為了排掉 1 公升 CO₂（或吸到 1 公升 O₂），你得讓呼吸搬動**幾公升**空氣」——它是「呼吸划不划算」與「有沒有過度換氣」的計量：數字小代表用很少呼吸就排掉 CO₂，數字大代表呼很多才排掉同樣的 CO₂。

## 前置概念
- [[Minute ventilation|分鐘通氣量（minute ventilation, VE）]]
  （分子就是 V̇E；也先懂 V̇E＝V̇_A＋死腔通氣、與 V̇CO₂＝V̇_A×F_A(CO₂) 這條關係。）
- [[VCO2|二氧化碳輸出量（VCO2, carbon dioxide output）]]
  （V̇E/V̇CO₂ 的分母。）
- [[VO2|耗氧量（VO2, oxygen uptake）]]
  （V̇E/V̇O₂ 的分母；兩種當量要分清。）

## 為什麼會這樣（first-principles 推導）
1. 由 [[Minute ventilation|V̇E]]：呼吸搬空氣是為了**排 CO₂、進 O₂**。同樣排掉一定量 CO₂，你可以呼得剛剛好，也可以呼過頭。把「呼了多少（V̇E）」除以「排了多少 CO₂（V̇CO₂）」，就量出這件事划不划算。
2. 定義兩個比值：
   - **CO₂ 通氣當量 ＝ V̇E / V̇CO₂**（每排 1 L CO₂ 要搬幾 L 空氣）。
   - **O₂ 通氣當量 ＝ V̇E / V̇O₂**（每吸收 1 L O₂ 要搬幾 L 空氣）。
3. 怎麼讀 V̇E/V̇CO₂：
   - **低** ＝ 用較少呼吸就排掉 CO₂（相對「省」，或相對**通氣不足**、CO₂ 被留下）。
   - **高** ＝ 呼很多才排掉同量 CO₂（**過度換氣**，或**死腔大／通氣效率差**）。
4. 為什麼「高」有兩種完全不同的成因？把 [[Minute ventilation|V̇CO₂＝V̇_A×F_A(CO₂)]] 代進去：V̇E/V̇CO₂ 正比於「**死腔佔比**（V̇E 裡有多少是白呼吸的）」乘以「**1/P_aCO₂**」。所以 V̇E/V̇CO₂ 偏高，可能是死腔大（病態、無效率），也可能是 P_aCO₂ 被壓低（[[Exercise hyperventilation|過度換氣]]）。讀數時要分清是哪一種。
5. 典型遞增運動曲線：V̇E/V̇CO₂ 會先**降到一個最低點（nadir，呼吸最划算）**，大約落在 [[Gas exchange threshold|GET]] 附近；再**回升**，回升的起點≈[[Respiratory compensation point|呼吸代償點 RC]]（過度換氣正式上場）。nadir 常被當「通氣效率」的指標（心衰患者 V̇E/V̇CO₂ 偏高＝預後較差）。
5.5. **V̇E/V̇CO₂「斜率（slope）」的臨床用法**：除了 nadir 與單點比值，CPET 也把整段運動的 V̇E 對 V̇CO₂ 作圖取**斜率**，當作 [[Pulmonary gas exchange limitation|肺氣體交換限制]]（與肺血管限制）的招牌指標，常用門檻 **斜率 ≥34**。邏輯沿第 4 步：斜率高＝排同量 CO₂ 要呼更多＝無效通氣（死腔大／通氣血流不匹配）。但它有兩個破綻（見易誤解 #5）：被過度換氣壓低的 P_aCO₂ 設定點也會抬高它（非真的氣體交換壞）；而**過了 [[Respiratory compensation point|RC]] 之後**，驅動通氣的主力換成醣解產酸而非 CO₂，斜率與通氣血流不匹配的關係失效，故**尖峰運動的 V̇E/V̇CO₂ 不能拿來評氣體交換**。
6. 接到本份的短劇烈運動（Yunoki）：V̇E/V̇CO₂ 在運動**中**掉到 ~25（相對通氣不足、CO₂ 被留住→存進 [[Body CO2 stores|CO₂ 庫]]）；運動**後**升到 ~50（[[Exercise hyperventilation|過度換氣]]→洩庫）。它與 [[End-tidal CO2|ET_CO₂]] 近似**鏡像**，正是 [[Excess CO2 output kinetics|excess V̇CO₂ 先負後正]]的「換氣面」。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：CPET 把 V̇E/V̇O₂、V̇E/V̇CO₂ 當核心讀數——用 V̇E/V̇O₂ 的轉折找 [[Gas exchange threshold|GET]]、用 V̇E/V̇CO₂ 的回升找 [[Respiratory compensation point|RC]]、用 V̇E/V̇CO₂ 的 nadir 或斜率評通氣效率。Yunoki 用 V̇E/V̇CO₂ 證明「運動中肺對 CO₂ 清除不足、運動後過度」。
- **背後的推理／證據**：因為（第 4 步）V̇E/V̇CO₂ 同時被死腔比例與 1/P_aCO₂ 決定，它能把「通氣有沒有配上 CO₂」量化。Yunoki 的 Fig 1 顯示 V̇E/V̇CO₂ 運動中掉、運動後升，且與 ET_CO₂ 鏡像——直接對應 CO₂ 先被滯留（庫被充）、後被沖走（庫被洩）。

## 易誤解之處
1. **「當量」是比值，不是量；高不一定壞、低不一定好。** 高可能是**保護性**過度換氣（抗酸），低可能是**通氣不足**把 CO₂ 留下。要配合 [[End-tidal CO2|ET_CO₂]]／P_aCO₂ 一起判斷方向。
2. **V̇E/V̇O₂ 與 V̇E/V̇CO₂ 不同步，對應不同閾值。** 過 [[Gas exchange threshold|GET]] 後**先**是 V̇E/V̇O₂ 上升（V̇O₂ 還穩、V̇E 已多）；**較晚**才輪到 V̇E/V̇CO₂ 上升（到 [[Respiratory compensation point|RC]]）。兩個拐點是兩個閾值的招牌，別混。
3. **「高 V̇E/V̇CO₂」要區分死腔 vs 過度換氣兩種來源。** 病態（心肺疾病）多是死腔／通氣血流不匹配；健康人過閾值多是過度換氣。同一個「高」，意義相反。
4. **它是嘴巴端的效率指標，受呼吸型態影響大。** 又快又淺（死腔佔比高）會抬高 V̇E/V̇CO₂；同樣的 V̇CO₂，慢而深的呼吸當量較低。
5. **V̇E/V̇CO₂ 斜率高 ≠ 一定有氣體交換異常，且尖峰運動不能用它評氣體交換。** 過度換氣（壓低 P_aCO₂ 設定點）也會抬高斜率；過了 [[Respiratory compensation point|RC]] 後通氣改由醣解產酸驅動，斜率與通氣血流不匹配脫鉤。故臨床上 V̇E/V̇CO₂ 斜率要配血氧一起看，真要確認氣體交換異常仍需動脈血氣（PA−aO₂、VD/VT）（Staes 2024）。

## 用生活例子再講一次
想像房間有人抽菸（產 CO₂），你開排風扇排煙。V̇E/V̇CO₂ ＝「每排掉 1 單位煙，你讓排風扇吹了幾單位空氣」。風扇開得剛好 ＝ 低當量（省）；為了壓住嗆味故意狂開 ＝ 高當量（過度換氣）；但若排風扇只在門口空轉（死腔）、煙其實排不太出去，你也得開很大才排掉一點 ＝ 同樣高當量（但這是**沒效率**）。所以同樣是「高」，一個是故意過度、一個是效率差——光看數字大小不夠，要看煙到底有沒有被排掉（配 ET_CO₂ 一起看）。

（失準之處：真實呼吸的「死腔」會隨每口氣深淺而變——深呼吸時死腔佔比變小——不像門廊那樣是固定一段空間。）

## 換句話說
換句話說，通氣當量是「每排 1 公升 CO₂（或進 1 公升 O₂）要呼幾公升氣」的划算度。低＝相對通氣不足（CO₂ 被留下，可能正在存進 [[Body CO2 stores|庫]]），高＝過度換氣或效率差。在遞增運動裡它有個最低點（最划算）、過了 [[Respiratory compensation point|RC]] 回升；在 Yunoki 的短劇烈運動裡，它運動中掉、運動後升——正是 CO₂ 先被留住（[[Excess CO2 output kinetics|excess 轉負]]）、後被沖出（excess 轉正）的換氣解釋。

## 來源
- [[source-Yunoki-1999-excess-CO2-kinetics]]（Fig 1：V̇E/V̇CO₂ 運動中 ~25、運動後 ~50，與 ET_CO₂ 鏡像；Discussion 以「運動中清除不足、運動後過度」解釋 excess V̇CO₂ 的時間曲線。）
- [[source-Staes-2024-CPET-exercise-limitations]]（氣體交換限制節：V̇E/V̇CO₂ 斜率≥34 為肺氣體交換/肺血管限制主判準；討論：斜率受過度換氣壓低 P_aCO₂ 而升高、過 RC 後與通氣血流不匹配脫鉤、尖峰不適用，須配血氧並以動脈血氣確認。）
