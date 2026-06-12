---
type: concept
aliases: [潮氣末二氧化碳, 呼氣末二氧化碳, 潮氣末CO2, 呼氣末CO2, 末段吐氣CO2, PETCO2, P_ETCO2, ET CO2, ETCO2, end-tidal CO2, end-tidal carbon dioxide]
tags: [exercise-physiology, gas-exchange, ventilation, acid-base]
sources: [source-Yunoki-1999-excess-CO2-kinetics]
prerequisites: [二氧化碳輸出量（VCO2, carbon dioxide output）, 分鐘通氣量（minute ventilation, VE）]
created: 2026-06-12
updated: 2026-06-12
---

# 潮氣末二氧化碳（end-tidal CO₂, P_ETCO₂）

## 本質（一句話）
這是「你每一口氣**最後吐出來那一段**的 CO₂ 濃度」——因為最後吐出的是最深、最接近肺泡的氣，而肺泡裡的 CO₂ 又幾乎等於動脈血裡的 CO₂，所以 end-tidal CO₂ 是一扇「**不抽血就能估到[[Arterial CO2 pressure|動脈 P_aCO₂]]**」的窗口。

## 前置概念
- [[VCO2|二氧化碳輸出量（VCO2, carbon dioxide output）]]
  （末段吐氣的 CO₂ 從哪來、由什麼決定，要先懂 V̇CO₂。）
- [[Minute ventilation|分鐘通氣量（minute ventilation, VE）]]
  （ET_CO₂ 的高低由「CO₂ 產量 vs 肺泡通氣」決定，這條關係在 V̇E 頁；也先懂死腔與肺泡通氣的區分。）

## 為什麼會這樣（first-principles 推導）
1. 一口氣吐出來有先後順序：**先**吐出的是**死腔**（dead space，氣管、支氣管那段只運送、不換氣的舊空氣，見 [[Minute ventilation|V̇E]] 第 5 步）；**後**吐出的是來自**肺泡**、剛跟血液換過氣的氣。所以「末段（end-tidal）」最能代表肺泡裡的氣體成分。
2. 先用一句話定義**分壓**：一團混合氣體裡，某種氣體「自己貢獻的那一份壓力」。CO₂ 分壓（P_CO₂）愈高＝這口氣裡 CO₂ 愈濃。可用 **%** 或 **mmHg** 表示（海平面靜息肺泡 CO₂ 約 5%，對應約 40 mmHg）。
3. 肺泡氣和肺微血管血之間隔著極薄的膜、接觸時間夠，兩邊的 CO₂ **幾乎達到平衡**——所以（健康肺）**肺泡 P_CO₂ ≈ 動脈 P_aCO₂**。把第 1 步合起來：量末段吐氣的 P_CO₂ ≈ 肺泡 P_CO₂ ≈ 動脈 P_aCO₂。這就是 ET_CO₂ 能當 P_aCO₂ 代理的理由。
4. ET_CO₂ 由什麼決定？沿用 [[Minute ventilation|V̇E]] 第 6 步那條關係：P_aCO₂（≈P_ETCO₂）是「**CO₂ 產量** 對上 **肺泡通氣量**」的拔河結果。產得多、或呼得太少 → P_ETCO₂ 升；呼得超過所需（[[Exercise hyperventilation|過度換氣]]）→ P_ETCO₂ 降。
5. 接到 CO₂ 庫與過量 CO₂：
   - 運動**起始**或清除不足時，CO₂ 被存進身體（組織 P_CO₂ 墊高，見 [[Body CO2 stores]]）→ ET_CO₂ **升**。
   - **過度換氣**把 CO₂ 沖走 → ET_CO₂ **降**，甚至**掉到靜息以下**。
   - 所以 ET_CO₂ 與「通氣划不划算」的指標 [[Ventilatory equivalent|V̇E/V̇CO₂]] 近似**鏡像**（一個升、另一個降）。Yunoki 的 80 s 劇烈運動：ET_CO₂ 由靜息 ~5% 升到 ~7%（停止前後），之後落到靜息以下 ~4.3% 並維持。
6. 應用：麻醉與急救用 **capnography（連續 ET_CO₂ 監測）**判斷有沒有在通氣、氣管插管位置；CPR 時 ET_CO₂ 驟降代表心輸出沒了（沒血把 CO₂ 帶到肺）。運動測試（CPET）用 ET_CO₂ 配合 [[Ventilatory equivalent|V̇E/V̇CO₂]] 看通氣效率與找閾值。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：把 ET_CO₂ 當肺泡／動脈 P_CO₂ 的無創代理，用它的時間變化追蹤組織 P_CO₂ 與酸鹼。Yunoki 用 ET_CO₂（Fig 1 中段）追蹤 P_CO₂ 怎麼隨運動先升後降，據此解釋 [[Excess CO2 output kinetics|excess V̇CO₂ 為何先負後正]]。
- **背後的推理／證據**：因為（第 3 步）末段吐氣 P_CO₂≈P_aCO₂，ET_CO₂ 升即反映身體在**滯留** CO₂（庫被充）、降即反映在**沖走** CO₂（庫被洩）。Yunoki 觀察到 ET_CO₂ 與 V̇E/V̇CO₂ 鏡像、且 ET_CO₂ 終究落到靜息以下，正對應「過度換氣把庫洩到底」。

## 易誤解之處
1. **是「末段」，不是整口氣的平均。** 要取末段才≈肺泡≈動脈；把整口氣（含死腔舊氣）平均會低估。
2. **「P_ETCO₂ ≈ P_aCO₂」只在健康肺、正常死腔時成立。** 重度肺病、死腔變大、或運動極喘換氣血流不均（V/Q 不匹配）時，兩者會出現落差（a-ET gradient），ET_CO₂ 會**低估** P_aCO₂。別當永遠相等。
3. **ET_CO₂ 升不一定是「多產 CO₂」。** 也可能是呼太少（通氣不足）或 CO₂ 被存起來；同理 ET_CO₂ 降可能是過度換氣而非少產。它是「**產 vs 呼**」拔河的結果，不是產量本身。
4. **單位有 % 也有 mmHg。** 近似換算：%　×（大氣壓 − 水蒸氣壓 ≈ 713 mmHg 於海平面）≈ mmHg（例如 5% ≈ 38 mmHg）。

## 用生活例子再講一次
想像你對著一根長管子慢慢吹一口氣，管子末端裝了 CO₂ 偵測器。你吹出的氣，**前半**是嘴巴、喉嚨、氣管裡的舊空氣（死腔），**後半**才是肺最深處、剛跟血換過氣的。偵測器盯「最後那一段」，因為那段最能反映肺深處（≈血液）的 CO₂。房間悶、你又不太呼吸（存 CO₂／通氣不足）→ 末段 CO₂ 濃；你嚇得狂喘把 CO₂ 都吹光（過度換氣）→ 末段 CO₂ 淡到比平常還低。

（失準之處：真實的肺有換氣與血流分布不均（V/Q），所以肺泡氣不是完美等於動脈血——這個落差在運動極限與肺病時被放大，使 ET_CO₂ 不再精準代表 P_aCO₂。）

## 換句話說
換句話說，end-tidal CO₂ 是「一口氣最後吐出那段的 CO₂」，因為那段最接近肺泡、也最接近動脈血，所以是不抽血估 P_aCO₂ 的方便窗口。它隨「存 CO₂／通氣不足」而升、隨「[[Exercise hyperventilation|過度換氣]]」而降——在 Yunoki 的故事裡，正是它先升（[[Excess CO2 output kinetics|遮蔽]]了緩衝 CO₂）、後降到靜息以下（把被遮蔽的 CO₂ 放出來），畫出 [[Excess CO2 output kinetics|excess CO₂ 先負後正]]的時間曲線。

## 來源
- [[source-Yunoki-1999-excess-CO2-kinetics]]（Fig 1：ET_CO₂ 由靜息 ~5% 升至 ~7%、再落到靜息以下 ~4.3%；與 V̇E/V̇CO₂ 鏡像；Discussion 以 ET_CO₂ 升降反映組織/肺 P_CO₂、解釋 excess V̇CO₂ 的遮蔽與釋放。）
