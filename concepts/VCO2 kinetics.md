---
type: concept
aliases: [VCO2動力學, 二氧化碳輸出動力學, 排碳動力學, VCO2 kinetics, carbon dioxide output kinetics, VCO2 on-kinetics, V̇CO2 kinetics, VO2-VCO2 動力學分離]
tags: [exercise-physiology, VO2-kinetics, gas-exchange]
sources: [source-Zhang-1991-fitness-VO2-VCO2-kinetics, source-Yunoki-1999-excess-CO2-kinetics, source-Stringer-1995-VCO2-VO2-CWR, source-Wooten-2021-respiratory-buffering-fatigability, source-Whipp-2006-pulmonary-CO2-O2-dissociation]
prerequisites: [二氧化碳輸出量（VCO2）, VO2 動力學（VO2 kinetics）, 時間常數（exponential time constant, τ）, 身體 CO₂ 庫（body CO2 stores）, 碳酸氫根對乳酸的緩衝（bicarbonate buffering）, 乳酸閾值（lactate threshold）]
created: 2026-06-12
updated: 2026-06-12
---

# VCO2 動力學（VCO2 kinetics）

## 本質（一句話）
VCO2 動力學講的是「出力突然跳高時，嘴巴吐出 CO₂ 的速率**多快**跟上」——它本該是 [[VO2 kinetics|VO2 動力學]]的雙胞胎，卻因為「CO₂ 會先被身體當水箱存起來」和「越過乳酸閾值後緩衝會額外擠出 CO₂」這兩件事，走出一條和 VO2 不一樣的時間曲線。

## 前置概念
- [[VCO2|二氧化碳輸出量（VCO2）]]
  （先懂 VCO2 是什麼、它有「燒食物」與「中和酸」兩個來源。）
- [[VO2 kinetics|VO2 動力學]]
  （VCO2 動力學是拿來和它對照的；先懂 τ、Phase I/II。）
- [[Time constant|時間常數（exponential time constant, τ）]]
  （同樣用指數逼近的快慢來描述。）
- [[Body CO2 stores|身體 CO₂ 庫]]
  （解釋 VCO2 為何在起始落後 VO2 的關鍵。）
- [[Bicarbonate buffering of lactic acid|碳酸氫根對乳酸的緩衝]] ＋ [[Lactate threshold|乳酸閾值]]
  （解釋 VCO2 為何在高強度反而不變慢的關鍵。）

## 為什麼會這樣（first-principles 推導）
一步一步來，每步只用前面已建立的事實：

1. 由 [[VCO2|VCO2]]：CO₂ 主要來自細胞燒食物（與 [[VO2]] 同源）。直覺上 VCO2 應該和 [[VO2 kinetics|VO2]] 同步上升——出力跳高、燒得多、O₂ 用得多、CO₂ 也產得多。
2. 但實測一量就發現**不對稱**：運動一開始（低強度第一步），**VCO2 上升得比 VO2 慢**。中等運動的時間常數，VO2 約 30–40 秒，VCO2 卻長到約 50–60 秒。為什麼？
3. 關鍵在 **CO₂ 很會溶、而且身體有一個大的 [[Body CO2 stores|CO₂ 庫]]**。肌肉新產的 CO₂ 不會立刻全跑到嘴巴——它先溶進組織與血液、把組織的 CO₂ 分壓（PCO₂）墊高、灌進那個庫。要等庫「漲起來」，多出來的 CO₂ 才會溢到肺、被量到。所以嘴巴端的 VCO2 比 VO2 **慢一拍**——這一拍主要花在「填 CO₂ 庫」。（O₂ 沒有對應的大儲庫，所以 VO2 不必等。）
4. 這個落後**集中在第一步（最低強度）**：第一步把組織 PCO₂ 墊起來之後，庫就大致到位了；到第二步，VO2 與 VCO2 的動力學就變得接近（Fig. 3）。換句話說「填庫」這件事主要在運動剛開始那一下發生。
5. 現在把強度往上加（接近個人最大能力的高百分比）。這裡出現本頁最漂亮的**反轉**：**VO2 動力學會變慢，VCO2 動力學卻幾乎不變。** 拆成兩股相反的力：
   - **VO2 變慢**：高強度下有氧引擎追不上、[[VO2 slow component|慢成分]]發展、更多 ATP 靠無氧醣解墊，所以「靠燒食物產生的 CO₂」那條線也跟著慢下來（aerobic CO₂ 變慢，往慢拉）。
   - **緩衝補 CO₂**：越過 [[Lactate threshold|乳酸閾值]]後，乳酸的酸被 [[Bicarbonate buffering of lactic acid|碳酸氫根緩衝]]，**額外擠出一批 CO₂**（[[Excess CO2 output|過量 CO₂]]，往快拉）。
   - 兩件事方向相反、剛好抵銷 → 淨結果是 **VCO2 的「到 75% 反應時間（To.75）」幾乎不動**（Zhang：VO2 從 53→94 秒顯著變慢，VCO2 75→89 秒不顯著）。
6. 收束這個對照（Fig. 1–3 的整個故事）：低強度時 VCO2 比 VO2 慢（填庫）；高強度時 VO2 自己慢下來、VCO2 卻被緩衝撐住不慢，於是兩者**交叉**、變得一樣快甚至 VCO2 反而略快。所以「VCO2 動力學對強度不敏感」不是因為它本身穩定，而是**兩個相反效應的巧合抵銷**。
7. 體能這條軸（與強度軸正交）：在**相同的相對強度**（同樣是各自最大能力的某百分比）下比較，**體能好的人 VO2 與 VCO2 動力學都更快**（To.75 與 [[VO2max|peak VO2]] 負相關 r≈−0.75～−0.90）。體能差的人更極端：在最大能力的上半段（>50%），他們的 VO2 「階梯狀上升」**整個消失**（被慢成分／無氧填補抹平），VCO2 的階梯卻還在。意思是：體能好＝同樣相對吃力時，有氧 ATP 通量相對無氧通量更高、動力學更靈敏（呼應 [[Metabolic stability|代謝穩定性]]）。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Zhang/Wasserman 用「四個 3 分鐘遞增階梯、各跨受試者最大能力的 25%」這種**相對強度**協定，可快速評估 VO2/VCO2 動力學。結論：隨相對強度上升，**VO2 動力學變慢、VCO2 不變**；同一相對強度下，**體能好者兩者都更快**。
- **背後的推理／證據**：VCO2 不變慢，被歸因於「緩衝放出的 CO₂」補上了「有氧變慢少掉的 CO₂」（明確用 HCO₃⁻ 緩衝乳酸解釋，並引 Casaburi 1989 同向結果）；VCO2 起始落後則歸因於 CO₂ 高溶解度與 CO₂ 庫填充。證據是 Table 2 的 To.75 數字與 Fig 3 的逐步曲線。

## 易誤解之處
1. **「VCO2 動力學穩定」是抵銷出來的假象，不是 CO₂ 系統本身穩。** 高強度下它其實同時被「有氧變慢」往下拉、被「緩衝 CO₂」往上推，淨值才剛好不動。把它讀成「CO₂ 不受強度影響」會錯失底下兩股相反的力。
2. **VCO2 起始落後 VO2 ≠ 身體少產 CO₂。** CO₂ 一樣在產，只是先被存進 [[Body CO2 stores|CO₂ 庫]]、晚一點才從嘴巴出來。量到的是「**排出**」動力學，不是「**產生**」動力學。
3. **這裡的「VCO2 不隨強度變慢」是 on-kinetics（時間軸），別和 [[V-slope method|V-slope]]／[[Excess CO2 output|過量 CO₂]]（強度軸）混淆。** 前者問「同一次跳階，CO₂ 多快到位」；後者問「強度愈高，CO₂ 相對 VO2 多冒多少」。兩者都牽涉緩衝 CO₂，但問的是不同維度。（而緩衝 CO₂ 自己也有第三條時間曲線——運動中被遮蔽、運動後達峰——見 [[Excess CO2 output kinetics|過量 CO₂ 輸出的動力學]]。）
   此外，本頁主談「上去（on-kinetics）」；運動停止後「下來（off-kinetics）」是另一個維度——VCO2 的恢復比 VO2 慢（Wooten 2021：off-τ≈81 vs 48 s），因為 CO₂ 還要額外「退 [[Body CO2 stores|庫存]]」；且 VCO2-off 受緩衝／酸鹼狀態與換氣驅動左右、有氧訓練後加快。完整見 [[Gas exchange recovery kinetics|氣體交換恢復動力學]]。
5. **【上游機制｜Whipp 2006】嘴巴量到的 V̇CO₂ 動力學，不是肌肉真正在產 CO₂ 的動力學。** 肌肉端的 CO₂ 產率（Q̇_CO₂）其實是單指數、τ 和 V̇O₂ 差不多；本頁說的「V̇CO₂ 起始落後」是這股 CO₂ 經血管運送延遲＋灌滿高容量 [[Body CO2 stores|CO₂ 庫]]後，在肺端被**拖慢、抹平**的結果（中等運動 τV̇CO₂≈50–60 s vs τV̇O₂≈30–40 s）。同一個容量也解釋兩個本頁沒展開的觀察：①做兩段等量遞增時，第二段的 V̇CO₂ 相對 V̇O₂ **更快**（倉庫已部分充電）；②過閾值後 V̇CO₂ 看似單指數、卻看不到對應 V̇O₂ 的慢相——那是「[HCO₃⁻] 下降變慢＋過度換氣延遲＋有氧慢成分」三股混疊出的假平順，不是 CO₂ 真的單純。完整見 [[Muscle-to-lung gas exchange dissociation|肌肉到肺的氣體交換脫鉤]]、根源見 [[Gas tissue capacitance|組織氣體容量]]。
4. **R（[[Respiratory exchange ratio|呼吸交換比]]＝VCO2/VO2）在轉換期是動態的。** 起始 VCO2 落後使 R 短暫偏低；越過閾值緩衝放 CO₂ 又把 R 推高（甚至 >1）。所以運動轉換期的 R 不能當穩態燃料指標讀（[[Respiratory exchange ratio|R]]＝「每用一份氧吐出幾份 CO₂」，靜息約 0.8、純燒醣≈1.0、緩衝／過度換氣時 >1；轉換期它脫離燃料、講的是換氣與酸鹼）。

## 用生活例子再講一次
想像工廠（肌肉）生產時會冒煙（CO₂），煙要先經過一個大煙囪緩衝室（[[Body CO2 stores|CO₂ 庫]]）才從頂端排出（嘴巴 VCO2）。剛開工時，煙先把緩衝室灌滿，外面看到的排煙比實際耗料（VO2）慢半拍；等緩衝室滿了就跟上。後來工廠拼命趕工、爐子卻燒不太動了（VO2 變慢），照理排煙該減速；但此時廠裡的「滅酸裝置」啟動、額外放一股煙（緩衝 CO₂），剛好補上爐子少冒的，於是煙囪頂端的排煙速度看起來幾乎沒變。

（這個類比在哪裡會失準：工廠的緩衝室與滅酸裝置是兩套硬體；人體的 CO₂ 庫與碳酸氫根緩衝其實是同一套碳酸–碳酸氫根化學的不同面向，彼此並非獨立。）

## 換句話說
換句話說，VCO2 動力學是「CO₂ 排出追上突增需求的速度」。它和 [[VO2 kinetics|VO2 動力學]]本是同源，卻被兩件事拉開：起始時 CO₂ 先去填 [[Body CO2 stores|身體的 CO₂ 庫]]（所以慢半拍），高強度時 [[Bicarbonate buffering of lactic acid|緩衝]]額外放 CO₂（所以不像 VO2 那樣變慢）。淨效果是 VCO2 的到位時間對強度出奇地穩——但那是兩股相反效應抵銷的巧合。體能好的人在相同相對強度下，VO2 與 VCO2 都更快。

## 來源
- [[source-Zhang-1991-fitness-VO2-VCO2-kinetics]]（Table 2／Fig 1–5：To.75 VO2 53.3→63.5→79.5→94.5 s 顯著變慢、VCO2 74.9→75.6→85.1→89.4 s 不顯著；起始 VCO2 慢於 VO2（CO₂ 高溶解度/填 CO₂ 庫）、第二步起趨同；高強度 VCO2 不變慢＝有氧變慢與緩衝放 CO₂ 相抵（引 Casaburi 1989）；體能好者 To.75 與 peak VO2 負相關 r≈−0.75～−0.90、不適者上半相對強度 VO2 階梯消失；HR 與 VO2 平行。）
- [[source-Yunoki-1999-excess-CO2-kinetics]]（時間軸互補：excess V̇CO₂＝V̇CO₂−V̇O₂ 在短劇烈運動先負後正；本頁易誤解 #3 的「緩衝 CO₂ 第三條時間曲線」與 #4 的 [[Respiratory exchange ratio|RER]] 連結即由本份補實。）
- [[source-Stringer-1995-VCO2-VO2-CWR]]（佐證定功率超閾值下 V̇CO₂ 先落後、約 60–90 s 追過 V̇O₂；把此時間差幾何化即 [[VCO2-VO2 relationship during constant work rate exercise|定功率 VCO2-VO2 折點]]。）
- [[source-Wooten-2021-respiratory-buffering-fatigability]]（off-kinetics 維度：Table 3 VCO2-off τ 81.0→73.3 s（p=.009）顯著快於訓練前、且慢於 VO2-off（48 s，因退 CO₂ 庫）；peak V̇E 與 VCO2-off ORI R²=0.496（CO₂ 通量驅動恢復期換氣）。對應易誤解 #3 的 off-kinetics 補充，詳見 [[Gas exchange recovery kinetics]]。）
- [[source-Whipp-2006-pulmonary-CO2-O2-dissociation]]（上游機制：肌肉 Q̇_CO₂ 單指數、τ≈τV̇O₂，肺端 τV̇CO₂≈50–60 s 由運送延遲＋高容量 CO₂ 庫造成；兩段遞增第二段較快、過閾值 heavy 過衝 vs very heavy 似單指數混疊。對應易誤解 #5，詳見 [[Muscle-to-lung gas exchange dissociation]]、[[Gas tissue capacitance]]。）
