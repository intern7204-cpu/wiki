---
type: concept
aliases: [無機磷酸, 無機磷, Pi, inorganic phosphate, 臨界Pi, critical Pi, peak Pi, 尖峰Pi, Pi累積, 橫橋, cross-bridge, power stroke]
tags: [exercise-physiology, fatigue, metabolism, mechanism]
sources: [source-Goulding-2021-VO2-kinetics-tolerance]
prerequisites: [ATP（adenosine triphosphate，三磷酸腺苷）, 磷酸肌酸（phosphocreatine, PCr）, 肌肉疲勞（fatigue）與任務失敗（task failure）]
created: 2026-06-11
updated: 2026-06-11
---

# 無機磷酸（inorganic phosphate, Pi）與肌肉疲勞

## 本質（一句話）
無機磷酸（Pi）是你花掉 ATP 和磷酸肌酸時被折下來、會在肌肉裡愈堆愈多的游離磷酸——而它是頭號「疲勞分子」：一旦堆過某個臨界量，就會卡住肌肉產生力量的機器。

## 前置概念
- [[ATP|ATP（adenosine triphosphate，三磷酸腺苷）]]
  （ATP→ADP+Pi 放能時就釋出 Pi；先懂這個「付錢動作」。）
- [[Phosphocreatine|磷酸肌酸（phosphocreatine, PCr）]]
  （PCr→肌酸+Pi 是 Pi 的主要來源；先懂「PCr 掉＝Pi 升」。）
- [[Muscle fatigue|肌肉疲勞（fatigue）與任務失敗（task failure）]]
  （Pi 的後果是周邊疲勞；先懂疲勞 vs 任務失敗、周邊 vs 中樞。）

## 為什麼會這樣（first-principles 推導）
1. 由 [[ATP|ATP]] 與 [[Phosphocreatine|PCr]]：每一次 ATP→ADP+Pi 放能、每一次 PCr→肌酸+Pi 補 ATP，都**折下一個游離磷酸（Pi）**。靜止時這些 Pi 會被回收；但激烈運動時 ATP/PCr 周轉太快，回收跟不上，**Pi 就累積**。
2. 所以肌肉裡的 [Pi]，其實是「能量系統被榨了多少」的一個**累計計量**——它隨 PCr 下降而上升（同一組反應的兩面）。
3. Pi 為什麼造成疲勞（先講「橫橋」這個詞）：肌肉的力量來自**橫橋（cross-bridge）**——肌凝蛋白頭抓住肌動蛋白、做出一個產生力量的「動力衝程（power stroke）」（這裡只給一句 gloss，完整的肌肉收縮力學超出本頁）。Pi 在三個地方搞破壞：
   - **抑制動力衝程**：擋住橫橋進入「高張力狀態」的那一步，於是每個橫橋出的力變小；
   - **降低肌絲對鈣離子（Ca²⁺，收縮的觸發訊號）的敏感度**：同樣的 Ca²⁺ 只能換到較弱的活化；
   - **在肌漿網（sarcoplasmic reticulum，肌肉裡儲存 Ca²⁺ 的倉庫）內與 Ca²⁺ 共沉澱**：使每次收縮能放出的 Ca²⁺ 變少。
   合起來：Pi 一升，「每分努力換到的力」就下降——這正是**周邊疲勞**（見 [[Muscle fatigue|疲勞]]）。
4. 兩個關鍵的閾值數值（後面模型的核心量）：
   - **臨界 [Pi]（critical [Pi]）≈ 18 mM**：越過它，就開始觸發疲勞與效率下降（也就是代謝物與 [[VO2 slow component|VO2 慢成分]] 開始出現的點）。
   - **尖峰 [Pi]（peak [Pi]）≈ 25 mM**：到達這個極限值，任務就失敗（力竭）。
   （模擬顯示這兩個數即使取 16–20 與 22.5–27.5 的範圍，仍能貼合功率-持續時間資料——所以它們是**代表值**，不是魔術常數。）
5. 為什麼挑「Pi」當代表（它是個 surrogate）：真實疲勞牽涉一大堆代謝物（H⁺、ADP、K⁺、Ca²⁺ 處理）。但 Pi 有**充分確立的致疲勞作用**，而且在模擬裡，**單一個「臨界 [Pi]」就能重現整條功率-持續時間曲線與 VO2 動力學**。所以模型用 [Pi] 當那一大群疲勞過程的**替身／標記**——作者明說這是「有效的簡化」。
6. 一個微妙但重要的性質（之後解釋 [[W prime|W′]] 會用到）：Pi 剛越過臨界時，多一點 Pi 對效率的打擊很大；接近尖峰時，多一點 Pi 的邊際effect變小（就像在離體肌纖維裡，Pi 對出力的抑制也是遞減的）。這個「遞減報酬」正是為什麼 CP 之上能做的總功（W′）會大致**固定**。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Goulding 等人提出，**Pi 是「臨界閾值」最佳的候選中介物**——它同時負責啟動正回饋迴路、以及最終在到達尖峰 [Pi] 時終結運動。
- **背後的推理／證據**：(a) 離體肌肉的疲勞機制（Allen 2008）確立 Pi 干擾橫橋與 Ca²⁺；(b) Korzeniewski & Rossiter 的**電腦模擬（in silico）**用單一臨界 [Pi] 就重現了雙曲線功率-持續時間關係與代謝物／VO2 慢成分；(c) 實測到慢成分起點的 [Pi]≈18、力竭時的 [Pi]≈25，與模型設定吻合。

## 易誤解之處
1. **Pi 升高 ≠ 肌肉沒氧氣。** Pi 累積是因為「周轉太快、回收跟不上」，不是因為缺氧（見 [[Dysoxia|dysoxia]]）。這是最容易滑回去的舊直覺。
2. **Pi 是「替身」，不一定是唯一元兇。** 模型說的是「單一代謝物越過閾值就能驅動整個系統行為」，不是「疲勞只由 Pi 造成」；真實疲勞是多因子的，Pi 是好用的標記。
3. **「臨界 [Pi]」是你在『靜止→運動』轉換時會越過的一條線。** 越過之後，代謝會**穩下來（重度）還是失控（極重度）**，取決於你當下的 [Pi] 比臨界高出多少——這條通往 [[Exercise intensity domains|強度區間]] 與 [[Critical Pi threshold and positive feedback model|模型]]。
4. **臨界 [Pi] 與尖峰 [Pi] 會因纖維型、運動型態、個體而異。** 18／25 mM 是代表值，不要當成對每個人都精準的固定刻度。

## 用生活例子再講一次
把 Pi 想成你猛燒爐子時積在爐排上的爐渣。燒得愈猛、爐渣積愈快。一點爐渣沒關係（火照樣旺）；但積過某個量（臨界 [Pi]），爐排開始被堵、進氣受阻，火（出力）就開始悶——而且一悶就更難燒、更積渣，惡性循環；積到把爐排完全堵死（尖峰 [Pi]），火就熄了（力竭）。

（這個類比在哪裡會失準：爐渣是純粹被動堆積的固體；Pi 的破壞是分子層級地干擾橫橋與鈣離子訊號，而且它「剛越線打擊大、接近尖峰打擊遞減」這個微妙的非線性，是單純積渣沒有的。）

## 換句話說
換句話說，無機磷酸是花 ATP／PCr 時折下來、會在肌肉裡累積的游離磷酸；它一多就卡住橫橋、削弱鈣訊號，造成周邊疲勞。它有兩條線：越過臨界 [Pi]（≈18 mM）開始觸發疲勞與效率損失，到達尖峰 [Pi]（≈25 mM）就力竭。模型用它當所有疲勞過程的替身，因為「單一個臨界 [Pi]」就足以重現整條 [[Critical power|功率-持續時間曲線]]——這正是 [[Critical Pi threshold and positive feedback model|臨界閾值模型]] 的基石。

## 來源
- [[source-Goulding-2021-VO2-kinetics-tolerance]]（"The critical threshold and positive feedback model" 節：Pi 抑制動力衝程、降 Ca²⁺ 敏感度、SR 內共沉澱（Allen 2008）；critical [Pi]≈18、peak [Pi]≈25 及其 16–20／22.5–27.5 容許範圍；Pi 為多重疲勞過程之 surrogate；遞減報酬與 W′。）
