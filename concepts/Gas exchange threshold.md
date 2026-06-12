---
type: concept
aliases: [氣體交換閾值, 氣體交換無氧閾值, 換氣閾值, GET, gas exchange threshold]
tags: [exercise-physiology, gas-exchange, thresholds]
sources: [source-Poole-2021-AT-controversy, source-Beaver-1986-V-slope, source-Whipp-2006-pulmonary-CO2-O2-dissociation]
prerequisites: [乳酸閾值（lactate threshold, LT）, 過量二氧化碳（excess CO2 output）, V-slope 方法（V-slope method）, 等二氧化碳緩衝區（isocapnic buffering region）]
created: 2026-06-10
updated: 2026-06-10
---

# 氣體交換閾值（gas exchange threshold, GET）

## 本質（一句話）
GET 就是「用呼吸氣體（不抽血）估出來的乳酸閾值」——它鎖定「過量 CO₂ 開始冒出來」的那個代謝率，是 [[Lactate threshold|乳酸閾值]] 的無創替身，而且**刻意不帶「無氧」這種有問題的機制含義**。

## 前置概念
- [[Lactate threshold|乳酸閾值（lactate threshold, LT）]]
  （GET 就是 LT 的氣體交換估計值；先懂 LT 這個被估的對象。）
- [[Excess CO2 output|過量二氧化碳（excess CO2 output）]]
  （GET 抓的訊號就是過量 CO₂ 開始出現；先懂這份多出來的 CO₂。）
- [[V-slope method|V-slope 方法（V-slope method）]]
  （GET 在實務上就用 V-slope 的斜率拐點來定位；先懂這個技術。）
- [[Isocapnic buffering region|等二氧化碳緩衝區（isocapnic buffering region）]]
  （確認 GET 是真 LT、而非偽閾值的對照證據；先懂這個窗口。）

## 為什麼會這樣（first-principles 推導）
1. 動機：直接抽血測 [[Lactate threshold|LT]] 是黃金標準，但要反覆扎針、取樣稀疏。能不能用無創、可連續、逐次呼吸取樣的呼吸氣體來估它？
2. 由 [[Bicarbonate buffering of lactic acid|緩衝鏈]]：乳酸一開始堆，H⁺ 被碳酸氫根中和就放出 [[Excess CO2 output|過量 CO₂]]，使 [[VCO2|VCO2]] 相對 [[VO2|VO2]] 多漲一截。所以「乳酸開始累積」必然在氣體上留下印記。
3. **GET 的定義**：在 VCO2-VO2 關係（[[V-slope method|V-slope]] 圖）上，VCO2 相對 VO2 出現**非線性上升的轉折**，且**確認沒有發生過度換氣**（靠 [[Isocapnic buffering region|等碳酸緩衝]]＋PCO₂ 不降來把關）。這個轉折所在的代謝率，就是 GET。
4. GET 與 LT 的關係：GET 發生在**緊鄰 LT 之前/附近**，兩者之間有個小差距（因為還有非碳酸氫根的緩衝機制參與），但此差距「臨床上不具意義」。所以實務上常把 GET 與 LT 當同義詞用。
5. **為什麼要新名字「GET」、不沿用「無氧閾值（AT）」？** 因為本綜述證明 AT 的「無氧/[[Dysoxia|缺氧]]」機制是錯的（見 [[Anaerobic threshold]]、[[Lactate shuttle]]）。但「用氣體交換無創估 LT」這件**方法本身**仍然有效又有用。於是把方法保留、把錯誤的機制含義丟掉，改用中性的名字 GET——它只說「我在氣體上抓到一個對應 LT 的轉折」，不宣稱任何缺氧。
6. GET 的把關條件（很重要）：只有當測試**夠快**、使代謝性酸中毒的發生與「呼吸代償性過度換氣」**分離**時，V-slope 上的轉折才能乾淨歸因於緩衝、而非過度換氣。確認方法就是 [[Isocapnic buffering region|等碳酸緩衝窗口]] 的存在。缺這個窗口（高海拔、McArdle 病、測前過度換氣），GET 可能是偽陽性或失效。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Poole 等人主張，GET 是目前最廣用的 LT 無創估計法，應「在乳酸穿梭生物學的框架下理解其概念基礎」，而非沿用無氧/缺氧的舊解釋。GET 無創、努力獨立（effort-independent）、可逐次呼吸取樣，在運動訓練與臨床都極有價值。
- **背後的推理／證據**：方法效度來自緩衝鏈的化學必然性（乳酸升→必放過量 CO₂）＋等碳酸窗口的排他驗證。臨床效度則來自大量預後數據：GET 對 VO2、相對 VO2max 的位置能評估系統功能正常與否、開運動處方、判定能否承受大手術、預測心衰存活——例如 GET < 11 mL/kg/min 關聯術後死亡率與心衰死亡風險顯著上升。這些用途都不需要「無氧」這個機制假設成立。

## 易誤解之處
1. **GET 是方法/估計值，不是「真的乳酸閾值」本身。** 它估的是 [[Lactate threshold|LT]]，兩者很近但有小系統差距。報告時要講清楚用 GET 還是直接抽血。
2. **GET 不是「無氧閾值」的新瓶舊酒。** 名字換掉是有意義的：保留「氣體交換估 LT」這個有效方法，剔除「缺氧」這個錯誤機制。把 GET 當成 AT 的同義詞、又連帶相信缺氧解釋，就回到了被否證的舊觀念。
3. **GET 切的是「中等↔重度」邊界，不是「能不能持續」的線。** 它對應 LT，落在相對低的代謝率；真正分出「穩態 vs 力竭」的是更高的 [[Critical power|CP]]。別把 GET 當成最高、最關鍵的閾值。
4. **沒有等碳酸窗口時要懷疑 GET。** 高海拔、McArdle 病、測前過度換氣都可能讓 V-slope 出現「假轉折」。一定要用 [[Isocapnic buffering region|等碳酸緩衝]] 對照。其中「測前過度換氣／遞增太快」這一類假轉折有正式名稱與量化把關——[[Pseudo-lactate threshold|偽乳酸閾值（ψ_L）]]：成因是 [[Body CO2 stores|CO₂ 庫]]被洩空後重新充填、充填率突變（非乳酸），用 **R₀/S₁ 明顯大於 1** 揪出（Whipp 2006）。
5. **GET 努力獨立、可在無法力竭者身上測。** 這是它相對 CP/[[VO2|VO2max]] 的最大臨床優勢——老人、病人不必拼到力竭就能量到。

## 用生活例子再講一次
想像你不准進廚房（不能抽血），只能靠「排氣口冒出的泡沫量」來判斷廚房何時開始忙不過來。你知道一條鐵律：廚房一開應急快炒檯（乳酸堆積），洗碗工就會狂用清潔劑、排氣口必冒大量泡沫（過量 CO₂）。於是你盯著「排氣口泡沫相對於進貨量開始多冒」的那一刻，就推斷廚房剛跨過負荷轉捩點——這就是 GET。但你還得確認泡沫不是有人單純在門口猛搧風（過度換氣）造成的假象，所以你同時檢查「門口空氣的酸味濃度有沒有維持穩定」（[[Isocapnic buffering region|等碳酸]]）。穩定，就確認泡沫真的來自廚房忙碌，而非搧風。

（失準之處：泡沫和廚房忙碌之間在比喻裡是固定鐵律；真實的 GET 與 LT 之間有小差距，且在某些人身上（缺等碳酸窗口）這條鐵律會失效。）

## 換句話說
換句話說，GET 是「用呼吸氣體無創估出來的乳酸閾值」：抓 [[V-slope method|V-slope]] 上的拐點、用 [[Isocapnic buffering region|等碳酸窗口]] 確認它是真 LT。它特意拋棄「無氧/缺氧」這個錯誤機制名（那是 [[Anaerobic threshold|AT]] 的歷史包袱），只保留「氣體交換估 LT」這個依然好用、努力獨立、臨床預後價值高的方法。

## 來源
- [[source-Poole-2021-AT-controversy]]（The gas exchange threshold: uses and limitations 整節：GET 定義、與 LT 的小差距、把關條件、臨床用途與預後數據。）
- [[source-Beaver-1986-V-slope]]（GET 的具體偵測技術 V-slope 之原始方法。）
- [[source-Whipp-2006-pulmonary-CO2-O2-dissociation]]（偽乳酸閾值與 R₀/S₁ 把關，補強易誤解 #4 的假轉折判讀。詳見 [[Pseudo-lactate threshold]]。）
