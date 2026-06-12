---
type: concept
aliases: [無氧閾值, 無氧門檻, 厭氧閾值, AT, anaerobic threshold, 乳酸酸中毒閾值, LAT, lactic acidosis threshold]
tags: [exercise-physiology, thresholds, gas-exchange, controversy]
sources: [source-Beaver-1986-V-slope, source-Poole-2021-AT-controversy, source-Stringer-1995-VCO2-VO2-CWR]
prerequisites: [乳酸閾值（lactate threshold, LT）, 碳酸氫根對乳酸的緩衝（bicarbonate buffering of lactic acid）, 過量二氧化碳（excess CO2 output）]
created: 2026-06-10
updated: 2026-06-12
---

# 無氧閾值（anaerobic threshold, AT）

## 本質（一句話）
無氧閾值就是「運動加重到某個程度，無氧代謝開始顯著插手、乳酸開始堆積」的那個轉捩點——它可以用血乳酸看（就是 [[Lactate threshold|乳酸閾值]]），也可以不抽血、純用呼出氣體裡的 [[Excess CO2 output|過量 CO₂]] 來抓。

## 前置概念
- [[Lactate threshold|乳酸閾值（lactate threshold, LT）]]
  （AT 的血液版定義幾乎就是 LT；先懂 LT 才懂 AT 在標定什麼。）
- [[Bicarbonate buffering of lactic acid|碳酸氫根對乳酸的緩衝]]
  （AT 能用氣體偵測，全靠乳酸→緩衝→CO₂ 這條鏈。）
- [[Excess CO2 output|過量二氧化碳（excess CO2 output）]]
  （氣體交換 AT 的操作定義，就是「過量 CO₂ 開始出現」的那一點。）

## 為什麼會這樣（first-principles 推導）
1. 收束前面幾頁：運動一強，無氧醣解貢獻增加 → [[Lactate|乳酸]] 開始堆（這個點＝[[Lactate threshold|LT]]）→ 乳酸的 H⁺ 被 [[Bicarbonate buffering of lactic acid|碳酸氫根中和]] → 放出 [[Excess CO2 output|過量 CO₂]] → [[VCO2|VCO2]] 比 [[VO2|VO2]] 多漲一截。
2. 這整串連鎖反應**始於同一個轉捩點**：無氧代謝開始顯著插手的那一刻。把這個轉捩點取個總名，就叫「無氧閾值（anaerobic threshold, AT）」。
3. 為什麼一個閾值有「好幾種名字、好幾種量法」？因為同一個事件在不同地方留下不同印記：
   - 在血乳酸上 → 看到 [[Lactate threshold|乳酸閾值（LT）]]。
   - 在血碳酸氫根上 → 看到它開始下降（HCO₃⁻ threshold）。
   - 在呼出氣體上 → 看到 [[Excess CO2 output|過量 CO₂]] 開始出現（這就是 [[Gas exchange threshold|氣體交換閾值（GET）]]——現代用這個中性名取代「氣體交換無氧閾值」）。
   它們是「同一事件的不同臉孔」，位置非常接近但不必數字全等。Wasserman 一系的文獻（如 [[VCO2-VO2 relationship during constant work rate exercise|Stringer 1995]]）又把這同一個點叫 **LAT（lactic acidosis threshold，乳酸酸中毒閾值）**——強調的就是「碳酸氫根開始緩衝乳酸酸中毒」這張臉，本質仍是同一個閾值。
4. 為什麼大家偏愛用氣體交換版？因為它**無創**（不必反覆抽血）、可連續即時讀，且只要會看 VCO2-VO2 的斜率變化就能抓（見 [[V-slope method|V-slope 方法]]）。
5. AT 為什麼重要？它把運動強度切成兩個性質不同的區間：在 AT 以下，代謝大致能進入穩態、乳酸與 CO₂ 不會無止境上升；越過 AT，無氧貢獻與酸的累積開始主導，身體進入「撐不久」的狀態。所以 AT 是評估有氧體能、開運動處方、評估心肺/代謝疾病的關鍵指標。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Beaver 等人主張用 VCO2-VO2 的斜率轉折（V-slope）來定義並偵測氣體交換 AT，並證明它「不顯著異於」用血碳酸氫根估的 HCO₃⁻ 閾值（1.83 vs 1.78 L/min VO2），也對應到 LT 之上約 0.5 meq/L。換言之，氣體交換 AT 是底層代謝轉變的可靠無創替身。
- **背後的推理／證據**：理由是第 1 步那條化學因果鏈是**強制性的**——乳酸一堆，緩衝就一定放 CO₂。傳統靠通氣反應（ventilatory equivalents）的方法，依賴「身體有沒有用力多呼吸」這個比較飄的反應；V-slope 直接抓「多出來的 CO₂ 產量」，命中的是 AT 的中心機制，所以更可靠、適用範圍更廣（連通氣反應遲鈍的人也行）。

## 易誤解之處
1. **「無氧閾值」是機制上錯誤的誤稱，現代只建議保留作歷史用途。** 這是 Poole 等人（2021）整篇綜述的核心結論。原始理論假設「過了這點肌肉就 [[Dysoxia|缺氧（dysoxia）]]、被迫走無氧」，但三條直接證據（直接量肌肉內 PO₂ 從未低到限制粒線體、NAD⁺/NADH 反而變更氧化、肌肉還能同時氧化乳酸）顯示**運動肌肉根本沒有缺氧**。乳酸上升的真正原因是醣解流量被強度催快、[[Lactate appearance and disappearance|Ra 壓過 Rd]]，並非缺氧（見 [[Warburg effect|Warburg 效應]]、[[Lactate shuttle|乳酸穿梭]]）。所以本頁的「無氧」二字應理解為歷史名稱；要描述「氣體交換無創估乳酸閾值」這個仍然有效的**方法**，現代改用中性名 [[Gas exchange threshold|氣體交換閾值（GET）]]。
2. **AT 不是疲勞極限、也不是 VO2max。** 它是一個中等偏高強度的轉折，遠在力竭之前；越過它仍能撐一段，只是性質改變。
3. **氣體交換 AT 與真正的「乳酸開始升」有個小落差。** 文獻測到氣體交換 AT 約在 LT 之上 0.5 meq/L；兩者很近但非同點，報告數值時要講清楚用哪種方法。
4. **AT ≠ [[Respiratory compensation point|呼吸代償點（RC）]]。** RC 是更高強度時「通氣開始爆衝去代償酸中毒」的第二個、更靠後的轉折；把 AT 和 RC 搞混，是判讀遞增測試最常見的錯誤之一（也是某些舊方法高估 AT 的原因）。
5. **AT 不是「能不能持續運動」的那條線——那條線是 [[Critical power|臨界功率（CP）]]。** 這是 Poole 等人的重要矯正：AT/LT 只切「中等↔重度」邊界，過了 AT 你**還能穩定撐一段**（重度區間，乳酸雖高但停得住）。真正分出「能穩態 vs 註定力竭」的是更高的 CP。換句話說，原始 AT 概念想抓的「持續非氧化供能的起點」，其實是 CP 在管，不是 AT。詳見 [[Exercise intensity domains|運動強度區間]]。

## 用生活例子再講一次
想像一間餐廳的廚房（有氧產能）。客人慢慢變多，廚房還能正常出餐，桌面乾淨（乳酸低、CO₂ 正常）。到某個客流量，廚房忙不過來，開始用「快炒應急檯」（無氧）幫忙，於是檯面開始堆髒盤（乳酸），洗碗工拼命用清潔劑中和油污、結果冒出大量泡沫（過量 CO₂）。你站在門口，光看「泡沫開始大量冒出來」的那一刻，就知道廚房剛跨過它的負荷轉捩點——那一刻就是 AT。

（失準之處：廚房的「應急檯」是另開的，身體的有氧/無氧其實是同一批細胞裡比例的此消彼長；而且 AT 之上身體仍大量有氧產能，不是廚房整個停擺。）

## 換句話說
換句話說，無氧閾值是「無氧代謝開始顯著上陣、乳酸開始堆」的那個強度。它在血液裡叫乳酸閾值、在碳酸氫根上是 HCO₃⁻ 下降、在呼吸氣體裡是過量 CO₂ 冒頭——同一件事的三張臉。因為呼吸這張臉最好看（無創、即時），我們就發展出 [[V-slope method|V-slope 方法]] 去抓它。

## 來源
- [[source-Beaver-1986-V-slope]]（全文核心：定義並驗證氣體交換 AT 與 LT、HCO₃⁻ 閾值的對應關係。）
- [[source-Poole-2021-AT-controversy]]（否證「無氧/dysoxia」機制、主張保留 GET 方法但棄用 AT 之名、指出 CP 才是真正關鍵閾值。）
- [[source-Stringer-1995-VCO2-VO2-CWR]]（LAT 別名來源；定功率氣體折點 V̇O₂ 與動脈乳酸升、標準碳酸氫根降的 V̇O₂ 高度吻合（r＝0.90、0.95），一手驗證氣體閾值＝代謝閾值。）
