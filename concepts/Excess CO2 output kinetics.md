---
type: concept
aliases: [過量CO2輸出動力學, 過量CO2動力學, 過量二氧化碳輸出的時間進程, excess VCO2 kinetics, kinetics of excess CO2 output, excess CO2 output kinetics]
tags: [exercise-physiology, gas-exchange, acid-base, CO2-kinetics, lactate]
sources: [source-Yunoki-1999-excess-CO2-kinetics]
prerequisites: [過量二氧化碳（excess CO2 output）, 身體CO2儲庫（body CO2 stores）, 碳酸氫根對乳酸的緩衝（bicarbonate buffering of lactic acid）, 運動性過度換氣（exercise hyperventilation）, 潮氣末二氧化碳（end-tidal CO2）, 通氣當量（ventilatory equivalent）, 肌酸激酶平衡（creatine kinase equilibrium）, 乳酸（lactate）]
created: 2026-06-12
updated: 2026-06-12
---

# 過量 CO₂ 輸出的動力學（kinetics of excess CO₂ output）

## 本質（一句話）
中和乳酸該放的那批 CO₂，**不是乳酸一產生就立刻從嘴巴出來**：在短而劇烈的運動裡，它在運動當下被「遮蔽」（嘴巴量到的 excess 速率甚至轉**負**），要等運動一停、過度換氣把身體 CO₂ 庫沖開，才以一個**延遲的大峰值**現身（約停後 60 秒），再花約 9 分鐘散盡。一句話：過量 CO₂ 的「**總量**」忠實反映乳酸，但它的「**時間進程**」被換氣與 CO₂ 庫嚴重延遲、打亂。

## 前置概念
- [[Excess CO2 output|過量二氧化碳（excess CO2 output）]]
  （本頁是它的「時間軸」版；先懂「過量 CO₂＝超出純代謝那一份」的強度軸框架。）
- [[Body CO2 stores|身體 CO₂ 儲庫（body CO2 stores）]]
  （延遲與遮蔽的舞台：CO₂ 在運動中被充、運動後被放，全靠這個庫。）
- [[Bicarbonate buffering of lactic acid|碳酸氫根對乳酸的緩衝]]
  （該放的 CO₂ 從這個中和反應來；要懂它如何隨 P_CO₂ 左右移。）
- [[Exercise hyperventilation|運動性過度換氣]]
  （運動後把被遮蔽的 CO₂ 沖出來的力量。）
- [[End-tidal CO2|潮氣末 CO₂]] ＋ [[Ventilatory equivalent|通氣當量 V̇E/V̇CO₂]]
  （讀懂「遮蔽 vs 釋放」的兩個指標：P_CO₂ 升降與通氣划不划算。）
- [[Creatine kinase equilibrium|肌酸激酶平衡]] ＋ [[Lactate|乳酸]]
  （兩個額外延遲源：PCr 對 H⁺ 的收放、乳酸擴散到血。）

## 為什麼會這樣（first-principles 推導）
**先定義本頁的操作型量。** 這篇文獻用 **excess V̇CO₂ ≡ V̇CO₂ − V̇O₂**（速率，每分鐘；Cerretelli & Di Prampero 法）。直覺：穩態純有氧時 V̇CO₂≈V̇O₂（[[Respiratory exchange ratio|RER]]≈1 上下），把 V̇CO₂ 減掉 V̇O₂，剩下的就約等於「**超出純有氧那一份 CO₂**」≈緩衝／洩庫的 CO₂。把它從頭到尾**積分**，就得到 **excess CO₂（總量）**。

1. **乳酸從第一秒就等速生成。** Fig 3：運動時間 ∝ ΔLa peak，且回歸線**過原點**（r=0.91）。意思是「該被緩衝、該放 CO₂」的需求，其實從運動一開始就線性累積——不是運動後才發生。
2. **但運動當下，嘴巴量到的 excess V̇CO₂ 不升反負。** Fig 1：~40 s 時掉到 −300 mL/min。產酸明明在進行，緩衝 CO₂ 卻沒出現、甚至倒扣？因為被**遮蔽**：
   - 運動中肺對 CO₂ 的清除跟不上（[[Ventilatory equivalent|V̇E/V̇CO₂]] 掉到 ~25＝相對通氣不足）→ CO₂ 滯留 → 組織／靜脈 P_CO₂、[[End-tidal CO2|ET_CO₂]] 升（~7%）。
   - 由 [[Bicarbonate buffering of lactic acid|碳酸氫根平衡]] CO₂＋H₂O ⇌ H⁺＋HCO₃⁻：**P_CO₂ 升會把平衡往「右」推**（多生 H₂CO₃／回填 HCO₃⁻）。這恰好**抵消／遮蔽**了乳酸 H⁺ 把 HCO₃⁻ 頂掉（往左）的效果 → 帳面上 HCO₃⁻ 沒怎麼降 → 該放的緩衝 CO₂ 被「**壓回庫裡存起來**」而非吐出。
   - 同時連正常代謝的 CO₂ 都有一部分在運動起始被存進 [[Body CO2 stores|庫]]（onset CO₂ storage，也是 [[Respiratory exchange ratio|RER 起始下降]]的成因）→ V̇CO₂ 落後 V̇O₂ → 兩者相減使 excess V̇CO₂ 為**負**。
3. **運動一停，劇情反轉。** [[Exercise hyperventilation|過度換氣]]持續（V̇E/V̇CO₂ 衝到 ~50）、肺把 CO₂ 大量沖走 → ET_CO₂、P_CO₂ 掉 → 碳酸氫根平衡往「**左**」移（放 CO₂）→ 剛才被遮蔽、存起來的那批緩衝 CO₂ 現在**湧出** → excess V̇CO₂ 衝正，峰值 ~+1100 mL/min 落在停後 ~60 s，再衰退到 ~9 min 歸零（ET_CO₂ 甚至掉到靜息以下，繼續把庫洩到底）。這正是 [[Body CO2 stores|CO₂ 庫]]「先充後放」與 [[Exercise hyperventilation|V̇CO₂ 跟著 V̇E 跑]]在時間軸上的具體演出。
4. **還有兩個讓 CO₂ 更延後的因素：**
   - **(a) 磷酸肌酸（PCr）的 H⁺ 收放。** 由 [[Creatine kinase equilibrium|CK 平衡]]：PCr＋ADP＋H⁺ ⇌ ATP＋肌酸。運動中 PCr 分解（往右）**吸掉 H⁺**，暫時抵掉一部分乳酸的酸 → 更少 HCO₃⁻ 被頂掉 → 運動中更少緩衝 CO₂。運動後 PCr 再合成（往左，停後 2–6 min）把 H⁺ **放回來** → 即使乳酸不再增加，H⁺ 仍上升 → 延後再逼出一批 CO₂。
   - **(b) 乳酸擴散到細胞外液。** 碳酸氫根緩衝在血液（細胞外液）比在肌肉內部強。乳酸要時間從肌肉擴散到血／全身（Fig 2：停後 5 min 血乳酸還在升）；擴散到細胞外液後被碳酸氫根緩衝的比例才高 → CO₂ 延後出現。
5. **但「總量」守得住。** 把 excess V̇CO₂ 從運動開始積分到停後 10 min ＝ excess CO₂，與 ΔLa 成正比（Fig 4：excess CO₂/kg ∝ ΔLa，r=0.88）。所以延遲與遮蔽打亂的是「**何時**出現」，不是「**總共多少**」——總量仍忠實記錄了緩衝掉多少乳酸的酸。
6. **收束對照。** [[Excess CO2 output|過量 CO₂]]（強度軸：強度↑→V̇CO₂ 相對 V̇O₂ 多冒一截）講的是穩態下的閾值訊號；本頁是**時間軸**：同一批緩衝 CO₂，在快速變動的短劇烈運動下，它的「**速率臉孔**（excess V̇CO₂）」被換氣／CO₂ 庫嚴重延遲甚至**反號**，只有「**積分臉孔**（excess CO₂ 總量）」還對得上乳酸。這也呼應 [[CO2 flow to the lungs|嘴巴 V̇CO₂ ≠ 循環運到肺]]、更 ≠ 即時的緩衝產生。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Yunoki 等人——excess CO₂（總量）與乳酸增加相關，但 excess V̇CO₂（時間進程）相對乳酸生成被**延遲**，且受**過度換氣**左右：運動中暫為負、停後達峰、約 9 min 散盡。
- **背後的推理／證據**：Fig 1（excess V̇CO₂ 先負後正；ET_CO₂ 與 V̇E/V̇CO₂ 鏡像）、Fig 3（時間 ∝ ΔLa peak 過原點＝等速產酸）、Fig 4（excess CO₂ ∝ ΔLa，r=0.88）。機制用三件事解釋延遲：碳酸氫根平衡隨 P_CO₂ 左右移（遮蔽／釋放）、PCr 對 H⁺ 的運動中吸／運動後放、乳酸擴散到細胞外液。

## 易誤解之處
1. **excess V̇CO₂（速率）「為負」不代表「沒在緩衝、沒產酸」。** 酸從第一秒就在產（Fig 3）；只是 CO₂ 被升高的 P_CO₂ 暫時壓回庫裡存著，沒從嘴巴出來。把負值讀成「沒緩衝」就錯了。
2. **「總量 ∝ 乳酸」與「速率不同步乳酸」並不矛盾。** 延遲／遮蔽搬動了 CO₂ 出現的**時間**，但搬不走**總量**——積分起來仍 ∝ ΔLa。**區分速率（rate）與積分（integral）是本頁的關鍵。**
3. **這裡的 excess V̇CO₂＝V̇CO₂−V̇O₂（以 RER≈1 為基準），與 [[Excess CO2 output|V-slope 的過量 CO₂]]（以「純代謝斜率」為基準）是兩種操作定義。** 抓的是同一件事（超出純有氧的 CO₂），但算法不同、別混用。
4. **運動後那個大峰值不是「運動後才開始緩衝／才產酸」。** 是運動中被遮蔽、存起來的 CO₂，加上 PCr 再合成放 H⁺、乳酸續擴散到血，三者延到運動後才被過度換氣一起沖出。
5. **別把它和 [[Oxygen debt|氧債／EPOC]] 的恢復 V̇O₂ 當成同一條曲線。** 兩者都在恢復期、都和先前的代謝擾動有關，但一個量的是**補氧**（V̇O₂ off-kinetics），一個量的是**延遲吐出的 CO₂**（V̇CO₂−V̇O₂）。順帶一提：這個恢復期 excess V̇CO₂ 峰會使恢復期 [[Respiratory exchange ratio|RER]] >1。

## 用生活例子再講一次
把中和乳酸該放的 CO₂，想成演唱會散場要離開的觀眾。運動**中**，場館出口被「換氣不足」堵住（[[Ventilatory equivalent|V̇E/V̇CO₂]] 低、P_CO₂ 高像把門頂著），觀眾被擋在館內（存進 [[Body CO2 stores|CO₂ 庫]]）；門口的計數器（excess V̇CO₂）甚至因為連正常散場的人都被擋而顯示**負成長**。演出一結束，保全把門全開（[[Exercise hyperventilation|過度換氣]]），積在館內的人潮一次湧出 → 門口計數**暴衝出峰值**，過一陣子才散完。你若只看「散場那一刻門口多少人」，會以為人是散場後才生出來的——其實他們在演出進行中就到了，只是被擋著。但「**總人數**」不會變：積分起來仍等於買票數（∝乳酸）。

（失準之處：出口被堵是機械式擋門，身體則是化學平衡——升高的 P_CO₂ 把碳酸氫根平衡頂回去、讓 CO₂「溶回」庫裡，不是物理擋門；而且身體同時還有 PCr 放 H⁺、乳酸擴散兩個額外延遲源，比單純塞門複雜。）

## 換句話說
換句話說，在短而猛的運動裡，緩衝乳酸該吐的 CO₂ 被「換氣跟不上 → P_CO₂ 升 → 把 CO₂ 壓回 [[Body CO2 stores|身體 CO₂ 庫]]」這件事遮蔽住，所以運動當下嘴巴量到的 excess V̇CO₂ 不升反負；運動一停、[[Exercise hyperventilation|過度換氣]]把庫沖開，這批被延遲的 CO₂ 才湧出，形成停後約 1 分鐘的大峰值、約 9 分鐘散盡。再加上 [[Creatine kinase equilibrium|磷酸肌酸再合成放回 H⁺]]、乳酸慢慢擴散到血液被緩衝，都把 CO₂ 往後推。但無論時間怎麼被打亂，把整段 excess V̇CO₂ **積分起來的總量，仍與乳酸累積成正比**——時間被延遲，總帳沒少。這就是 [[Excess CO2 output|過量 CO₂]] 在「時間軸」上的樣子。

## 來源
- [[source-Yunoki-1999-excess-CO2-kinetics]]（Fig 1：excess V̇CO₂ 運動中 −300、停後峰 +1100 mL/min（~60 s）、~9 min 歸零，ET_CO₂ 與 V̇E/V̇CO₂ 鏡像；Fig 3：時間∝ΔLa peak 過原點；Fig 4：excess CO₂/kg ∝ ΔLa，r=0.88；Discussion：碳酸氫根平衡隨 P_CO₂ 左右移、PCr 的 H⁺ 收放、乳酸擴散到 ECF 三條延遲機制。）
