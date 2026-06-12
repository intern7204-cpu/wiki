---
type: concept
aliases: [身體CO2儲庫, 身體二氧化碳儲庫, 體內CO2儲存, CO2儲庫, 碳酸氫根庫, bicarbonate pool, body CO2 stores, body carbon dioxide stores]
tags: [exercise-physiology, gas-exchange, acid-base]
sources: [source-Peronnet-2006-CO2-hyperventilation, source-Yunoki-1999-excess-CO2-kinetics, source-Whipp-2006-pulmonary-CO2-O2-dissociation]
prerequisites: [二氧化碳輸出量（VCO2, carbon dioxide output）, 碳酸氫根對乳酸的緩衝（bicarbonate buffering of lactic acid）]
created: 2026-06-11
updated: 2026-06-12
---

# 身體 CO₂ 儲庫（body CO₂ stores / bicarbonate pool）

## 本質（一句話）
身體裡存著一大缸隨時可進可出的 CO₂，絕大部分是以「碳酸氫根（HCO₃⁻）」的形式溶在血液與組織裡——它像一個緩衝水箱，不必你多燒或少燒一口食物，光是「放酸進去」或「拼命呼氣」就能把它放掉一批 CO₂。運動到一定強度時，從嘴巴多吐出來的那批 [[Excess CO2 output|過量 CO₂]]，其實是**在洩這個水箱**，不是現燒出來的。

## 前置概念
- [[VCO2|二氧化碳輸出量（VCO2, carbon dioxide output）]]
  （水箱的進出最後表現在「每分鐘呼出多少 CO₂」上；先懂 V̇CO₂。）
- [[Bicarbonate buffering of lactic acid|碳酸氫根對乳酸的緩衝（bicarbonate buffering of lactic acid）]]
  （水箱的主成分就是碳酸氫根；先懂 H⁺＋HCO₃⁻ ⇌ H₂CO₃ ⇌ H₂O＋CO₂ 這條可逆反應。）

## 為什麼會這樣（first-principles 推導）
1. 由 [[VCO2|V̇CO₂]]：細胞燒食物產生的 CO₂ 溶進血液。但 CO₂ 在血裡**不是只以氣體溶著**——它大部分立刻和水反應、再被解離成碳酸氫根（HCO₃⁻）存起來：CO₂ ＋ H₂O ⇌ H₂CO₃ ⇌ H⁺ ＋ HCO₃⁻。所以血液帶 CO₂，主力形式是 HCO₃⁻。
2. 這個「以碳酸氫根存著的 CO₂」量很大：成人光血漿 HCO₃⁻ 濃度就約 24 mmol/L，再加上組織，全身可逆釋放的 CO₂ 達好幾公升。把它想成一個**大容量、可快速進出的水箱**。（這個「水箱有多大、分壓動一點能吞吐多少」的量化性質，就是 [[Gas tissue capacitance|組織氣體容量]]——血液對 CO₂ 的容量是對 O₂ 的好幾倍，這條不對稱是運動時 CO₂ 與 O₂ 氣體交換動力學會脫鉤的總源頭。）
3. 水箱的水位（能存多少 CO₂）由一條化學平衡決定，叫 Henderson–Hasselbalch 關係：HCO₃⁻ 的量同時受 **pH** 與 **CO₂ 分壓（P_CO₂）** 牽動。白話：給定血的酸鹼度和 CO₂ 壓力，碳酸氫根存量就被定死在某個值。
4. 於是有**兩個旋鈕**可以「洩水箱」——放出一批 CO₂——而完全不必改變細胞的 CO₂ 產量：
   - **旋鈕一：把 pH 調低（加酸）。** 運動產乳酸 → 血變酸 → 多出的 H⁺ 把 HCO₃⁻ 推回去：H⁺ ＋ HCO₃⁻ → H₂CO₃ → H₂O ＋ CO₂。被擠出來的 CO₂ 隨血到肺、呼掉。經驗值：**血漿 HCO₃⁻ 每掉 1 mmol/L，約釋出 0.4 L CO₂**。
   - **旋鈕二：拼命呼氣（壓低 P_CO₂）。** [[Exercise hyperventilation|過度換氣]] 把 CO₂ 吹掉得比產得快 → P_CO₂ 下降 → 平衡往「釋放」那邊移，再從碳酸氫根逼出一批 CO₂（CO₂ washout）。
5. 最關鍵、也最常被忽略的一點（放慢）：**洩水箱是暫時的、有底的**。一旦「隨手可取」的那部分碳酸氫根放得差不多了，就算 pH 還低、P_CO₂ 還低，也再榨不出更多 CO₂ 了。這解釋了兩個現象：
   - 高強度遞增運動到某點，V̇CO₂ 不再跟著通氣（V̇E）暴衝、反而追不上——那點就是 [[Respiratory compensation point|呼吸代償點]]（水箱見底）。
   - 固定高強度持續運動時，V̇E 持續升、V̇CO₂ 卻平掉甚至回落——同樣是水箱被洩到底。
6. 把第 4–5 點合起來，就改寫了「過量 CO₂」的身世：它**不是肌肉裡新做出來的**，而是「血裡本來就存著的 CO₂ 庫，被低 pH 與過度換氣兩個旋鈕放出來的」。直接證據（McKenna 1997）：30 秒力竭運動使血乳酸升到 16 mmol/L，按「肌肉現做 CO₂」的舊模型應多出約 15 L CO₂，實測嘴巴只多吐約 6–7 L，而且全身 CO₂ 儲量不增反減（−45~55%）——正好對上「血漿 HCO₃⁻ 掉約 15 mmol/L × 0.4 L ≈ 6 L 從水箱被放掉」。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Péronnet & Aguilaniu（2006）主張——運動中嘴巴多出的 CO₂ 來自「身體裡隨手可取的碳酸氫根庫」（血液與運動肌等灌流良好組織），約每 1 mmol/L 血漿碳酸氫根下降釋出 0.4 L CO₂；這其實是 1982 年「nonmetabolic CO₂」模型出現**之前**就有的舊解釋（Wasserman & Whipp 1975），他們重新把它扶正。
- **背後的推理／證據**：靠 McKenna（1997a,b）兩篇配對研究：嘴巴實測多出的 CO₂（~6–7 L）與「血漿碳酸氫根下降量 ×0.4」（~6 L）幾乎相等，且全身 CO₂ 儲量**下降**——若真有大量「肌肉現做的非代謝 CO₂」，儲量該上升而非下降。資料方向直接否證新做、支持「洩既有庫」。

## 易誤解之處
1. **「放出一批 CO₂」不等於「產生一批 CO₂」。** 水箱裡的 CO₂ 原本就是先前代謝產的、暫存成碳酸氫根；放掉它只是**搬移時間**（先存後放），沒有無中生有。把「洩庫」當「新製造」，就會犯 [[Nonmetabolic CO2|非代謝 CO₂]] 那個質量守恆錯誤。
2. **水箱會見底，所以這招是有限的、暫時的。** 這正是 V̇CO₂ 在高強度或久撐後「追不上 V̇E」的原因；別以為 CO₂ 能一直被擠出來。
3. **兩個旋鈕方向相同（都放 CO₂）但機制不同。** 旋鈕一是「加酸把碳酸氫根頂掉」，旋鈕二是「壓低 P_CO₂ 把平衡吸走」；運動中段以旋鈕一為主（[[Isocapnic buffering region|等碳酸期]]，P_CO₂ 還沒降），高段才加上旋鈕二（[[Respiratory compensation point|呼吸代償]] 後 P_CO₂ 開始降）。
4. **這個「庫」不是肺、不是某個器官，是一個化學形式。** 它分布在全身血液與組織的碳酸氫根裡，靠 Henderson–Hasselbalch 平衡進出，不是某處的氣囊。
5. **【時間軸｜Yunoki 1999】這個庫的「充」與「放」有先後，不是同時。** 短劇烈運動中 CO₂ 來不及排，**先被充進庫**（組織 P_CO₂、[[End-tidal CO2|ET_CO₂]] 升、[[Respiratory exchange ratio|RER]] 暫降）；運動一停、[[Exercise hyperventilation|過度換氣]]才把庫**放掉**，延遲吐出一個 CO₂ 大峰。先充後放，正是 [[Excess CO2 output kinetics|過量 CO₂ 先負後正]]的由來——這是「水箱會充放」這件事在時間軸上最乾淨的證據。

## 用生活例子再講一次
把血液想成一大缸加了小蘇打的氣泡水（碳酸氫根＝溶在水裡的 CO₂ 庫）。平常封著，CO₂ 乖乖待在水裡。現在有兩招能讓它冒泡放氣：① 擠一點檸檬汁（加酸／降 pH），酸一進去就把碳酸氫根頂出 CO₂ 氣泡；② 拿吸管拼命把瓶口的氣抽走（壓低上方 CO₂ 壓力／過度換氣），水裡的 CO₂ 就被吸出來補。兩招都讓你「多收集到一批氣泡」，但你並沒有讓水多產生 CO₂——你只是把本來溶著的放出來。而且氣泡水裡的 CO₂ 有限，抽久了就再也冒不出來。

（失準之處：氣泡水是封閉一缸，身體是持續有代謝 CO₂ 進帳、又持續從肺出帳的動態系統；所以身體的水箱會邊洩邊補，只有當「洩的速度超過補的速度」一段時間後才真的見底。）

## 換句話說
換句話說，身體存了一大缸以碳酸氫根形式溶著的 CO₂。運動到一定強度，血變酸（加酸）加上拼命呼吸（壓低 CO₂ 壓力），把這缸 CO₂ 放掉一批，從嘴巴多吐出來——這就是 [[Excess CO2 output|過量 CO₂]] 的真正來源。它是「洩既有庫存」，不是「肌肉現燒新貨」；而且庫存有限、會見底，這正是高強度久撐後 [[VCO2|V̇CO₂]] 追不上呼吸的原因。

## 來源
- [[source-Peronnet-2006-CO2-hyperventilation]]（§6、§8 與 Fig. 6：過量 CO₂ 來自身體碳酸氫根庫、~0.4 L/mmol、McKenna 1997 證儲量下降而非上升、水箱見底解釋 V̇CO₂–V̇E 脫鉤。）
- [[source-Yunoki-1999-excess-CO2-kinetics]]（Fig 1：短劇烈運動中庫被充（ET_CO₂↑、excess V̇CO₂ 負）、運動後被放（過度換氣→延遲 CO₂ 峰）；庫「先充後放」的時間軸證據。對應易誤解 #5。）
- [[source-Whipp-2006-pulmonary-CO2-O2-dissociation]]（把「水箱大小」量化為 [[Gas tissue capacitance|組織容量]]＝解離曲線斜率，CO₂ 容量數倍於 O₂；此庫的充放延遲是 [[Muscle-to-lung gas exchange dissociation|肌肉到肺 V̇CO₂ 脫鉤]]的主因。對應推導第 2 步。）
