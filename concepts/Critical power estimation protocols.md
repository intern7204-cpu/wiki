---
type: concept
aliases: [臨界功率估計協定, CP估計協定, CP與W prime的量測, CP測定方法, critical power estimation, critical power protocols, CWR protocol, constant work-rate protocol, ramp protocol for CP]
tags: [exercise-physiology, critical-power, methods, performance]
sources: [source-Sreedhara-2019-power-models-survey]
prerequisites: [Critical power, W prime, 3-minute all-out test, Incremental exercise test]
created: 2026-06-12
updated: 2026-06-12
---

# 臨界功率的估計協定（critical power estimation protocols）

## 本質（一句話）
要拿到一個人的 [[Critical power|CP]]和 [[W prime|W′]]，得讓他做幾趟「撐到力竭」的測試、再把功率–時間雙曲線擬合上去——而**用哪種測試協定、配哪種數學形式去擬合，會影響估出來的數字**（尤其 W′），所以「CP/W′ 是多少」這個問題的答案，總得附帶「用什麼方法量的」。

## 前置概念
- [[Critical power|臨界功率（critical power, CP）]] 與 [[W prime|W′]]
  （要估的就是這兩個參數；先懂它們是雙曲線 t＝W′/(P−CP) 的漸近線與曲率。）
- [[3-minute all-out test|三分鐘全力測試（3MT）]]
  （三大協定之一，最省時；本頁把它擺進與其他協定並列比較。）
- [[Incremental exercise test|遞增運動測試]]
  （ramp 協定就是用不同坡度的遞增測試到力竭來估 CP/W′；先懂遞增測試長什麼樣。）

## 為什麼會這樣（first-principles 推導）
1. **先回到要量什麼。** [[Critical power|CP]]/[[W prime|W′]] 是功率–持續時間雙曲線 t＝W′/(P−CP) 的兩個參數。要量它們，本質上就是「取幾個（功率 P, 力竭時間 t_lim）的點，再把雙曲線擬合上去，解出 CP（水平漸近線）與 W′（曲率）」。怎麼取點、怎麼擬合，就是「協定」的內容。

2. **經典協定＝CWR（constant work-rate，定功率力竭）。** 這是 Monod & Scherrer 最早的做法、也被當「黃金標準」：受試者在不同日子做 **3–5 趟**「固定一個高於 CP 的功率、一路騎到力竭」的測試，每趟得到一個 (P, t_lim) 點，再擬合。

3. **同一條雙曲線可以寫成幾種代數形式（線性化），而你選哪種會影響結果。** 三種常見：
   - **功–時間線性式**：W_lim ＝ CP·t_lim ＋ W′（總功對時間畫直線，斜率＝CP、截距＝W′）。
   - **功率–倒數時間線性式**：P ＝ W′·(1/t_lim) ＋ CP（功率對 1/t 畫直線，截距＝CP、斜率＝W′）。D. W. Hill 建議用這個、至少 4–5 點。
   - **非線性雙曲線式**：直接擬合 t ＝ W′/(P−CP)。
   數學上它們是同一個模型，但因為含 1/t 這種倒數、捨入與回歸權重不同，**對同一筆資料會解出不同的估計**——尤其 W′。

4. **關鍵陷阱：CP 估得穩，W′ 估得飄。** 跨研究反覆發現，不同形式/模型對同一筆資料解出的 **CP 彼此相近**，但 **W′ 差很多**（例如把兩參數與 [[Three-parameter critical power model|三參數模型]]套到同一筆 Gaesser 資料，CP 是 176 vs 165 W、很接近，W′ 卻是 29.1 vs 47.9 kJ、差了六成）。原因：CP 是曲線的漸近線、由「最終壓到哪」決定，相對穩健；W′ 是曲線彎曲程度、由資料點的分布與線性化方式決定，敏感得多。所以文獻說 W′ 的真值「elusive（難以捉摸）」。（這條雙曲線的**回歸數學細節**——三種線性化各自的偏誤、CP 與 W′ 各自的標準誤、兩試驗 vs 三試驗配適——見 [[Critical power model fitting|CP 模型配適]]；本頁聚焦在上一層的「**該做哪種測試協定**」。）

5. **第二種協定＝ramp（遞增坡度力竭）。** Morton 導出力竭時間 T 與遞增坡度 S（瓦/秒）的關係：
   $$T = \frac{CP}{S} + \sqrt{\frac{2W'}{S}}$$
   做 4–5 趟**不同坡度**的遞增測試到力竭，把 (S, T) 擬合上式即得 CP/W′。它估出的值通常**比 CWR 低一些**，剛好部分修正了「CWR 會高估 CP」的問題；但與 CWR 相比，W′ 有時被低估、有時被高估（個體差異大）。

6. **第三種協定＝[[3-minute all-out test|3MT]]。** 單次 3 分鐘全力：CP＝末 30 秒平均功率、W′＝功率曲線高出 CP 的面積。**最省時**（少進幾趟實驗室）。代價：有高估 CP 的報告，且單次測試**拿不到 W′ 的標準誤**（見易誤解 #4 與 [[Intra-individual variability of critical power and W prime|IIV]]）。

7. **協定本身還有幾個會偏掉結果的旋鈕（放慢，這是實務最容易踩雷的地方）：**
   - **預測試的時長會影響估計**：用「最短的 3 趟」算出的 CP 與 W′，**顯著高於**用「最長的 3 趟」算出的（Bishop、Jenkins）。太短的力竭測試（如 <2 min）會系統性把 CP/W′ 撐高。
   - **踏頻會影響**：60 rpm 估出的 CP 顯著高於 100 rpm（同一個人）。
   - **建議的折衷**（Muniz-Pumares）：用非線性雙曲線、至少 **3 趟 CWR**、時長落在 **2–15 分鐘**、自選踏頻，估得最可靠。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：CP/W′ 可用多種協定（CWR、ramp、3MT）與多種代數形式估計；3MT 最省時、CWR 為傳統黃金標準、ramp 可修正 CWR 的高估；但無論哪種，W′ 都比 CP 更受模型與協定影響，且預測試時長與踏頻會系統性偏移結果。
- **背後的推理／證據**：所有協定都是在擬合同一條雙曲線，差別只在取點方式與擬合形式。CP 是漸近線、相對穩健；W′ 是曲率、對資料點分布與線性化（尤其含 1/t 的捨入）敏感——這從「同資料、不同模型，CP 一致而 W′ 分歧」（Gaesser 等多篇）直接看得出來。Bishop/Jenkins 的「短趟 vs 長趟」對照則證明取點的時長窗口本身就會偏移估計。

## 易誤解之處
1. **「CP/W′ 是量一次就定的身體常數」是錯的。** 同一個人，數值會隨你用的協定與模型而變（尤其 W′），還疊加日間變異（見 [[Intra-individual variability of critical power and W prime|IIV]]）。報一個 CP/W′，要附「怎麼量的」。
2. **別把 CP 與 W′ 當成同等可靠。** CP 跨模型穩健；W′ 跨模型分歧。看到一個 W′ 數字，先問它是用哪種協定/形式估的，否則拿兩篇不同方法的 W′ 直接比是危險的。
3. **預測試時長要落在合理窗口（約 2–15 min）。** 用太短的力竭測試會高估 CP/W′；混入時長差很大的趟次也會讓估計漂掉。
4. **3MT 省時 ≠ 更準。** 它一樣可能高估 CP，而且單次 3MT 給不出 W′ 的標準誤——省了實驗室時間，卻犧牲了對估計不確定性的掌握。

## 用生活例子再講一次
想量一個形狀不規則的水池有多大容量、漏水有多快。你把水位灌到幾個不同高度，各記錄一次「排空要多久」，再套公式回推「容量」和「漏速」。你會發現：不論用哪組水位、哪條擬合公式，回推出的**漏速（≈CP）**都差不多；但回推出的**容量（≈W′）**卻可能差很多——因為容量靠的是把曲線往外延伸的那段彎曲，對你取的點和用的公式最敏感。量 CP/W′ 就是這麼回事：漸近線好抓，曲率難抓。

（這個類比在哪裡會失準：水池的容量與漏速是固定的物理量，多量幾次只是減少誤差；人的 CP/W′ 本身還會日間漂移（見 [[Intra-individual variability of critical power and W prime|IIV]]），所以「多量幾次取平均」不只是降噪，更是在描繪一個會動的目標。）

## 換句話說
換句話說，估 CP/W′ 就是「取幾個力竭點、擬合雙曲線」，但取點的協定（多趟定功率 CWR／不同坡度 ramp／單次 3MT）和擬合的代數形式都會左右結果——CP 相對穩、W′ 特別飄。3MT 最省時但拿不到 W′ 標準誤、CWR 是黃金標準但受預測試時長與踏頻影響、ramp 可修正 CWR 的高估。所以任何一個 CP/W′ 數字，都該連同「用什麼方法量的」一起讀，並記得它還疊著 [[Intra-individual variability of critical power and W prime|日間變異]]。

## 來源
- [[source-Sreedhara-2019-power-models-survey]]（Methods and Protocols to Estimate CP and W′ 與 Limitations 兩節：CWR 多趟（3–5）＋線性/非線性擬合、Hill 建議 P vs 1/t、ramp 協定 T＝CP/S＋√(2W′/S)（Morton）、3MT（Vanhatalo）；W′ 跨模型分歧而 CP 相近（Table 1）；預測試時長（Bishop/Jenkins，短趟 CP/W′ 顯著較高）與踏頻（60 vs 100 rpm）影響；Muniz-Pumares 建議 ≥3 趟 2–15 min 自選踏頻非線性擬合。）
