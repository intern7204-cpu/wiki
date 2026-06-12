---
type: concept
aliases: [最大攝氧量, 最大耗氧量, 最大有氧能力, VO2max, maximal oxygen uptake, VO2 peak, VO2peak]
tags: [exercise-physiology, VO2-kinetics, foundation]
sources: [source-Poole-2016-critical-power, source-Midgley-2008-incremental-test-duration, source-Molmen-2024-mitochondrial-capillary-training]
prerequisites: [耗氧量（VO2, oxygen uptake）, 細胞呼吸（cellular respiration）]
created: 2026-06-10
updated: 2026-06-12
---

# 最大攝氧量（VO2max, maximal oxygen uptake）

## 本質（一句話）
VO2max 就是「身體每分鐘能用掉氧氣的**最高上限**」——再怎麼加強運動、再怎麼催，攝氧量也只能到這個天花板，不會再往上。

## 前置概念
- [[VO2|耗氧量（VO2, oxygen uptake）]]
  （VO2max 是 VO2 這個量的「最大值」；先懂 VO2 是什麼、怎麼隨強度上升。）
- [[Cellular respiration|細胞呼吸（cellular respiration）]]
  （上限為什麼存在，要從「細胞用氧產能」這條鏈的瓶頸來理解。）

## 為什麼會這樣（first-principles 推導）
1. 由 [[VO2|VO2]]：運動愈強、需要的能量愈多 → 需要燒掉的氧愈多 → VO2 隨強度上升。直覺上，強度一直加，VO2 是不是也一直升？
2. 不是。VO2 會升到一個值之後**就上不去了**，形成一個平台（plateau）。這個平台高度就是 VO2max。再增加運動強度，多出來的能量只能靠非氧化途徑（醣解、磷酸肌酸）硬撐，攝氧量本身不再增加。
3. 為什麼有上限？因為從「空氣 → 肺 → 血液 → 心臟打出去 → 肌肉細胞用掉」這整條氧氣輸送鏈上，有一個最窄的瓶頸。在健康、非久坐的人身上，**瓶頸主要是 O₂ 輸送（O₂ delivery）**——心臟把含氧血送到肌肉的能力，跟不上肌肉粒線體想要的量。粒線體本身還有餘力，但氧氣送不夠快。
4. 換句話說（本文獻的精確說法）：VO2max 是「即使代謝刺激（ADP、肌酸累積）持續增加，粒線體的氧化流量也再增不上去」的那一點。所以它反映的是「氧氣供給 × 利用」整個系統的綜合天花板。
5. 單位與標定：通常用 mL/min，或除以體重寫成 mL/kg/min（這樣不同體型才好比較）。健康年輕人約 40 mL/kg/min 上下，菁英耐力選手可達 70–80+，重症病人可能低到 10 幾。
6. 為什麼它在閾值框架裡很重要？因為其他閾值常用「占 VO2max 的百分比」來表達位置：[[Lactate threshold|LT]]/[[Gas exchange threshold|GET]] 約落在 50–65% VO2max（未受訓者）、[[Critical power|CP]] 約 70–80%。但要小心——這些百分比因人而異（見易誤解），且 [[VO2 slow component|VO2 慢成分]] 會讓「同一功率對應固定 %VO2max」這個假設失效。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Poole 等人指出，健康非久坐者在全身運動時的**最大粒線體氧化速率，高於實際 in vivo 能達到的 VO2max**——也就是說，限制因素是 O₂ 輸送，不是粒線體本身。VO2max 在 severe 強度（>CP）運動中被達到，正是限制細胞呼吸的「主導機制」之一。
- **背後的推理／證據**：理由在於「拿掉輸送瓶頸就能提高 VO2」的實驗——例如吸高氧氣體（hyperoxia）能提高運動表現與 [[Critical power|CP]]，說明輸送端確實是瓶頸。若瓶頸在粒線體，補氧就不會有效。

## 易誤解之處
1. **VO2max 是「能用氧的上限」，不是「能撐多久」或「表現好壞」的唯一指標。** 兩個 VO2max 相同的人，[[Critical power|CP]]、[[W prime|W′]]、運動經濟性可能差很多，表現也差很多。本文獻反覆強調 CP 比 VO2max 更能預測表現。
2. **「VO2peak」常用來指「測到的最高值」，未必是真平台。** 嚴格的 VO2max 要看到平台；很多人（尤其病人）在出現平台前就力竭，這時報的是 VO2peak。兩詞常混用，判讀時要留意。怎麼判斷測到的是真平台還是只是 VO2peak、以及沒平台時怎麼確認，見 [[VO2max attainment criteria|VO2max 達標判準]] 與 [[Verification phase|驗證階段]]。
3. **用「%VO2max」標定強度會誤導。** 同樣 70% VO2max，對 A 可能在重度區間、對 B 可能在極重度——因為每個人 LT、CP 落在 VO2max 的比例不同。這正是本文獻主張改用 [[Critical power|CP]] 來標定強度的原因（見 [[Exercise intensity domains|運動強度區間]]）。
4. **上限主要卡在輸送、不是肌肉沒力。** 在健康人身上瓶頸是 O₂ delivery；這也是為什麼心衰（CHF）、肺病（COPD）這類輸送受損的疾病會大幅壓低 VO2max 與 CP。
5. **VO2max 是「中樞 × 周邊」的綜合天花板，訓練時兩端不同步——別把粒線體大漲當成 VO2max 會等比大漲。** 周邊的 [[Mitochondrial content|粒線體含量]] 訓練後增幅約是 VO2max 的 **2–3 倍**；甚至「直接看粒線體的金標準 MvD 與 VO2max 的訓練變化**不相關**」（r=−0.03，n.s.）——因為 VO2max 還被**中樞輸送**（心輸出、血量）卡著（呼應易誤解 #4）。所以「粒線體含量上去了、VO2max 只上去其零頭」是必然，不是矛盾（Mølmen 2024）。

## 用生活例子再講一次
把身體想成一座工廠，氧氣是原料。VO2max 就是「這座工廠每分鐘最多能消化多少原料」的上限。你以為瓶頸是車間（粒線體）產能不足，但實際上是**送貨卡車（心血管輸送）**的車隊規模有限——車間還有空位，但原料送不進來那麼快。所以想提高上限，得擴充車隊（心臟、血液、微血管），而不是只催車間。

（失準之處：工廠的「上限」是固定設備規格；VO2max 會隨訓練、疾病、年齡上下移動，而且不同運動型態（跑步 vs 手搖）測到的值也不同，因為動用的肌肉量不同。）

## 換句話說
換句話說，VO2max 是「身體每分鐘用氧能力的天花板」，主要被氧氣輸送（而非粒線體）卡住。它是運動生理常用的標尺，但本身不決定「撐多久、跑多好」——那要看 [[Critical power|CP]] 與 [[W prime|W′]]。把強度換算成 %VO2max 容易誤導，因為每個人的閾值落點不同。

## 來源
- [[source-Poole-2016-critical-power]]（Role of oxygen 節：VO2max＝O₂ 輸送限制下粒線體流量的上限；CP 約 70–80% VO2max；批評以 %VO2max 標定強度。）
- [[source-Midgley-2008-incremental-test-duration]]（VO2peak/plateau 判準與測後驗證的延伸來源；遞增測試時長在很寬範圍內不損 VO2max 效度。）
- [[source-Molmen-2024-mitochondrial-capillary-training]]（中樞-周邊脫鉤的大數據：粒線體含量增幅 ≈2–3× VO2max、MvD 與 VO2max 變化不相關（r=−0.03 n.s.）、CS 與 VO2max 中度相關（r=0.45）；女性 VO2max 百分比進步>男性（基線低、mL/kg/min 相當）；VO2max trainability 主要由起點體能決定、終生保留——見 [[Trainability]]。）
