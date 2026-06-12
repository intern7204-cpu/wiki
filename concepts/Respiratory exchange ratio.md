---
type: concept
aliases: [呼吸交換比, 呼吸交換率, 氣體交換比, RER, R, gas exchange ratio, respiratory exchange ratio]
tags: [exercise-physiology, gas-exchange, foundation, metabolism]
sources: [source-Yunoki-1999-excess-CO2-kinetics, source-Stringer-1995-VCO2-VO2-CWR, source-Whipp-2006-pulmonary-CO2-O2-dissociation, source-Storoschuk-2025-zone-2-review]
prerequisites: [二氧化碳輸出量（VCO2, carbon dioxide output）, 耗氧量（VO2, oxygen uptake）, 細胞呼吸（cellular respiration）]
created: 2026-06-12
updated: 2026-06-12
---

# 呼吸交換比（respiratory exchange ratio, RER / R）

## 本質（一句話）
RER 就是「在嘴巴量到的 **吐出 CO₂ ÷ 吸入消耗 O₂**」這個比值——安安靜靜時它告訴你身體現在主要在燒脂肪還是燒醣；但只要身體在**存 CO₂、放 CO₂ 或拼命呼吸**，這個比值就會脫離「燒什麼燃料」、改去講換氣與酸鹼的故事。

## 前置概念
- [[VCO2|二氧化碳輸出量（VCO2, carbon dioxide output）]]
  （RER 的分子；先懂嘴巴吐出的 V̇CO₂ 有「燒食物」與「中和酸／洩庫」多個來源。）
- [[VO2|耗氧量（VO2, oxygen uptake）]]
  （RER 的分母；先懂 V̇O₂ 量的是用掉多少氧。）
- [[Cellular respiration|細胞呼吸（cellular respiration）]]
  （不同燃料燒起來的「用氧/出碳比例」不同，是 RER 能反映燃料的根。）

## 為什麼會這樣（first-principles 推導）
一步一步來：

1. 由 [[Cellular respiration|細胞呼吸]]：燒燃料要用 O₂、會產 CO₂。不同燃料的碳氫氧比例不同，所以「燒它時用幾個 O₂、出幾個 CO₂」的比例也不同。
2. 先定義**細胞層**的比值——**呼吸商（respiratory quotient, RQ）＝ 細胞產生的 CO₂ ÷ 細胞消耗的 O₂**。
   - 純醣：C₆H₁₂O₆ ＋ 6 O₂ → 6 CO₂ ＋ 6 H₂O，RQ ＝ 6/6 ＝ **1.0**。
   - 純脂肪：分子裡碳多、氫多、氧少，要動用**更多** O₂ 去燒、相對出**較少** CO₂，RQ ≈ **0.7**。
   - 蛋白質介於中間，RQ ≈ 0.8。
   所以「RQ 落在哪」就指出在燒哪種燃料。**這條換算有個重要應用**：在遞增運動裡逐級量 RER，就能反推每一級的「燒脂速率」、畫成倒 U 曲線讀出 [[Maximal fat oxidation|最大脂肪氧化（MFO/Fatmax）]]——[[Fatty acid oxidation|脂肪氧化能力]] 常用的量法就是這樣（Storoschuk 2025）。
3. 但我們在**嘴巴**量的不是細胞的 RQ，而是 **RER ＝ 嘴巴 V̇CO₂ ÷ 嘴巴 V̇O₂**。在**穩定狀態、又沒有額外酸鹼事件**時，嘴巴進出 ≈ 細胞進出，所以 **RER ≈ RQ**——這時 RER≈0.7 讀作燒脂肪、≈1.0 讀作燒醣。
4. 為什麼嘴巴的 RER 會**偏離**細胞的 RQ？關鍵不對稱：[[VO2|V̇O₂]] 這邊沒有大儲庫，量到的氧耗相當貼近細胞當下用氧；但 [[VCO2|V̇CO₂]] 這邊隔著一個會充放的 [[Body CO2 stores|CO₂ 庫]]，又會被緩衝與過度換氣加料。所以 **RER 偏離 RQ，幾乎都是分子（V̇CO₂）那一端在動。** 更底層地說，這條不對稱本身來自 [[Gas tissue capacitance|組織氣體容量]]——血液對 CO₂ 的容量是對 O₂ 的好幾倍，所以非穩態時被「先充庫／後洩庫」拖離代謝值的，幾乎只有 V̇CO₂ 那一端。
5. 於是有三種典型情況把 RER 帶離「燃料區間 0.7–1.0」：
   - **(a) 越過 [[Lactate threshold|乳酸閾值]]**：乳酸的酸被 [[Bicarbonate buffering of lactic acid|碳酸氫根緩衝]]擠出額外 CO₂（[[Excess CO2 output|過量 CO₂]]）→ V̇CO₂↑ → **RER 升，可 >1.0**。
   - **(b) [[Exercise hyperventilation|過度換氣]]**：拼命呼氣壓低 P_aCO₂、把 [[Body CO2 stores|庫存 CO₂]]吹出 → V̇CO₂↑ → **RER 升（>1）**。
   - **(c) 運動起始存 CO₂**：剛開始運動，新產的 CO₂ 先被存進身體（組織 PCO₂ 墊高）、晚一點才從嘴巴出來 → V̇CO₂ 暫時落後 V̇O₂ → **RER 暫時下降（甚至低於靜息）**。這就是 onset CO₂ storage 在 RER 上的臉孔（Yunoki／Hughson）。
6. 恢復期同理是動態的：剛停下時之前被遮蔽的緩衝 CO₂ 湧出、V̇O₂ 又快速回落 → RER 衝 >1；再過一段時間補回 CO₂ 庫又可能壓低 RER。所以**運動轉換期與恢復期的 RER 不能當燃料指標讀**。
7. 一個實用後果：臨床／運動測試常把 **RER > 1.10–1.15** 當「已接近最大努力」的客觀旁證（[[VO2max]] 判準之一）。原因就是 (a)+(b)：逼到極限時緩衝＋過度換氣把 V̇CO₂ 推得遠超 V̇O₂。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：RER 在穩態用來估燃料利用（脂肪 vs 醣）、在極量運動用來佐證盡力程度；但在**非穩態**（運動轉換、過閾值、過度換氣、恢復）它不再等於 RQ。Yunoki 等人即利用「運動起始 RER／excess V̇CO₂ 暫時下降」來印證 onset CO₂ storage。
- **背後的推理／證據**：因為 RER 的偏離幾乎都來自 V̇CO₂ 端被 [[Body CO2 stores|CO₂ 庫]]充放與緩衝加料（第 4–5 步），而 Yunoki 的 Fig 1 直接顯示運動起始 excess V̇CO₂（＝V̇CO₂−V̇O₂，與 RER 同向）轉負，對應 CO₂ 被暫存。

## 易誤解之處
1. **RER（嘴巴，V̇CO₂/V̇O₂）≠ RQ（細胞，產 CO₂/耗 O₂）。** 只有穩態、無額外酸鹼事件才約略相等；轉換／過閾值／過度換氣時 RER 被 V̇CO₂ 帶離 RQ。別在非穩態用 RER 讀燃料。
2. **RER > 1 不代表「燒了某種比醣更耗 CO₂ 的燃料」**（沒有這種燃料，RQ 上限就是約 1.0）。它代表 V̇CO₂ 被**非燃料來源**（緩衝 CO₂、洩庫、過度換氣）抬高了。
3. **起始 RER 下降不是「忽然多燒脂肪」**，是 CO₂ 被暫存使 V̇CO₂ 落後——是**搬移時間**，不是換燃料。也不是過度換氣造成：[[VCO2-VO2 relationship during constant work rate exercise|Stringer 1995]] 在這段 R nadir（~15–40 秒）期間直接量動脈血，發現 P_aCO₂ 與 [H⁺] **上升**（不是過度換氣該有的下降），確證起始 R 下凹純是存 CO₂，與換氣無關。
4. **RER 是比值，分子或分母任一端動都會改變它。** 解讀前先問「是 V̇O₂ 在變還是 V̇CO₂ 在變」，否則會把換氣事件誤讀成代謝事件。
5. **【診斷用途｜Whipp 2006】基線 R（R₀）配上 V-slope 第一段斜率（S₁），可揪出假閾值。** 若測前過度換氣把 [[Body CO2 stores|CO₂ 庫]]洩空，會同時把 R₀ 抬高、把 S₁ 壓低，使 **R₀/S₁ 明顯大於 1**，提示測到的是 [[Pseudo-lactate threshold|偽乳酸閾值]]而非真閾值。所以 R 不只看絕對值，它和 S₁ 的比也是把關工具。

## 用生活例子再講一次
把身體想成一座工廠，進料口吸空氣取氧（V̇O₂），排氣口吐廢氣 CO₂（V̇CO₂）。「廢氣量 ÷ 取氧量」這個比，平常反映在燒哪種料（脂肪料省排氣、醣料多排氣）。但這工廠的排氣口接了一個**緩衝煙室**（[[Body CO2 stores|CO₂ 庫]]）、一套**滅酸噴氣**（緩衝）和一台**可調大排風扇**（換氣）。剛開工時煙先進緩衝室 → 排氣口讀數暫時偏低（比值降）；趕工滅酸 → 額外噴一股煙（比值升 >1）；排風扇全開 → 把存煙吹出（比值又升）。所以光看排氣口的「廢氣/取氧比」，在這些時刻**並不能**告訴你在燒什麼料。

（失準之處：真實燃料還有蛋白質、酮體等更細的 RQ；而且 O₂ 其實也有一點點儲存（肌紅蛋白、血紅素），只是遠小於 CO₂ 庫，所以「偏離幾乎都在 V̇CO₂ 端」是近似而非絕對。）

## 換句話說
換句話說，RER 是「嘴巴版的碳氧比」。靜下來穩態時，它≈細胞的 RQ，能告訴你在燒脂肪（≈0.7）還是燒醣（≈1.0）；但只要身體在存 CO₂、放 CO₂、或拼命呼吸，分子 V̇CO₂ 就會脫離細胞代謝、把 RER 帶走——這時 RER 講的是**換氣與酸鹼**的故事，不是燃料的故事。它一旦 >1，多半是 [[Excess CO2 output|緩衝 CO₂]] 與 [[Exercise hyperventilation|過度換氣]]在抬高 V̇CO₂。

## 來源
- [[source-Yunoki-1999-excess-CO2-kinetics]]（Fig 1 與引言：運動起始 excess V̇CO₂（＝V̇CO₂−V̇O₂，與 RER 同向）暫時轉負＝onset CO₂ storage，RER 暫時下降；引 Hughson 1985、Linnarsson 1974。）
- [[source-Stringer-1995-VCO2-VO2-CWR]]（動脈血直接證明起始 R nadir 非過度換氣：該期間 P_aCO₂ 與 [H⁺] 上升而非下降。對應易誤解 #3。）
- [[source-Whipp-2006-pulmonary-CO2-O2-dissociation]]（R≠RQ 的容量機制（CO₂ 容量數倍於 O₂）；R₀/S₁ 指標識破 [[Pseudo-lactate threshold|偽乳酸閾值]]。對應推導第 4 步與易誤解 #5。）
- [[source-Storoschuk-2025-zone-2-review]]（§5.2：脂肪氧化能力以 RER 換算的 MFO（最大脂肪氧化率）與 Fatmax（對應強度）量化。對應推導第 2 步的應用延伸；詳見 [[Maximal fat oxidation]]。）
