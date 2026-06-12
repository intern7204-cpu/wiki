---
type: concept
aliases: [運動強度區間, 運動強度域, 運動強度分域, 中等重度極重度, moderate heavy severe, exercise intensity domains]
tags: [exercise-physiology, thresholds, framework]
sources: [source-Poole-2021-AT-controversy, source-Poole-2016-critical-power, source-Goulding-2021-VO2-kinetics-tolerance, source-Miller-2023-fast-start-HIIE, source-Ventura-2023-severe-extreme-tolerance, source-Coates-2023-HIIT-perspective, source-Storoschuk-2025-zone-2-review]
prerequisites: [乳酸閾值（lactate threshold, LT）, VO2 慢成分（VO2 slow component）]
created: 2026-06-10
updated: 2026-06-12
---

# 運動強度區間（exercise intensity domains）

## 本質（一句話）
運動強度區間就是「把所有運動強度，依照**身體能不能進入穩態、撐多久**，切成性質截然不同的幾段（中等／重度／極重度）」——而切這幾段的兩道界線，就是兩個關鍵閾值。

## 前置概念
- [[Lactate threshold|乳酸閾值（lactate threshold, LT）]]
  （它是「中等↔重度」的下界；先懂這個閾值在標什麼。）
- [[VO2 slow component|VO2 慢成分（VO2 slow component）]]
  （區間的差別之一就是「有沒有慢成分」；先懂這個現象。）

## 為什麼會這樣（first-principles 推導）
1. 為什麼要分區間？因為「強度高低」是連續的，但身體的反應**不是連續地變糟，而是在幾個臨界點上換檔**——過了某個點，代謝、酸鹼、撐多久的規則整套都變了。與其用「百分之幾 VO2max」這種會誤導的相對值，不如用這些自然的轉捩點來分段。
2. 用兩道界線切出三段：
   - **下界＝[[Lactate threshold|乳酸閾值（LT）]]**（也就是 [[Anaerobic threshold|AT]]/[[Gas exchange threshold|GET]] 抓的那個點）。
   - **上界＝[[Critical power|臨界功率（CP/CS）]]**。
3. 三段各自的性質：
   - **中等強度（moderate，< LT）**：血乳酸不升、停在基線；[[VO2|VO2]] 快速進入穩態、無 [[VO2 slow component|慢成分]]。可以撐很久，靠純有氧供能。（訓練語言裡，這一段低強度就是 [[Zone 2 training|Zone 2]]／[[Moderate-intensity continuous training|MICT]] 的所在；但「Zone 2」是相對個人 LT1 的，絕對強度因人差很大——見 [[Zone 2 training]]。）
   - **重度強度（heavy，LT ~ CP）**：血乳酸升高，但能**穩定在一個較高的水平**（Ra＝Rd，只是檔位高）；VO2 出現慢成分、效率變差，但最終仍能達到一個（升高的）穩態。撐得住但比較累。
   - **極重度／嚴重強度（very heavy/severe，> CP）**：血乳酸**穩不住、一路上升**到力竭；VO2 被慢成分一路推向 VO2max；無法穩態。撐多久由 [[Critical power|CP]] 與 [[W prime|W′]] 數學決定。
4. 關鍵洞見（也是本綜述的重點）：**過去把 LT/AT 當成「最重要的那條線」是錯置重點。** LT 只切出「中等↔重度」；真正分出「能不能穩住、撐不撐得久」的，是更高的 CP/CS 那條線。換句話說，LT 之上你還能穩定撐一段（重度），要到 CP 之上才進入「註定走向力竭」的區間。
5. 為什麼這對訓練與臨床重要？因為「同樣是高強度」在 CP 上下意義完全不同：CP 以下可累積訓練量、可長時間維持；CP 以上每一秒都在消耗有限的 [[W prime|W′]]，很快力竭。處方時必須知道對象落在哪一段。

### 重度「穩得住」、極重度「跑不停」的機制（Goulding 2021）
6. 為什麼重度能穩、極重度會失控？[[Critical Pi threshold and positive feedback model|臨界閾值模型]] 給了機制：兩者都越過了臨界 [[Inorganic phosphate|[Pi]（≈18 mM）]]、都啟動「疲勞 → 效率損失 → 更多 Pi」的正回饋，差別只在**當下 [Pi] 高出臨界多少**。
   - **重度**：[Pi] 停在「略高於臨界」，多出來的 ATP 周轉不足以讓 Pi 失控 → 迴路穩下來 → VO2／代謝物達一個升高的穩態。
   - **極重度**：[Pi] 一路爬向**尖峰 [Pi]（≈25 mM）**，迴路自我推進到力竭；撐多久＝爬到尖峰的速率，總功＝固定的 [[W prime|W′]]。
7. 同一機制也解釋一個反直覺現象：**間歇運動**能把同一高功率的耐受從幾分鐘變成可長時間維持——因為短工作段＋恢復段讓 [Pi]（與 VO2）來不及爬過臨界，等於把「極重度的功率」在代謝上拉回「重度甚至中等」的行為。換句話說，決定你落在哪一段的不只是功率，還有 [[VO2 kinetics|VO2 動力學]] 與運動的時間結構。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Poole 等人主張，LT/GET 有效區分「中等↔重度」邊界，但**CP/CS 才是區分「重度↔極重度」、且更貼近運動表現與疲勞機制的關鍵線**。他們指出絕大多數奧運耐力項目都落在重度（< CS，如馬拉松約 96% CS）到極重度（> CS，萬米以下）區間。
- **背後的推理／證據**：證據是「過了 CP 與否，一整組生理變數的行為完全相反」（見 [[Critical power]] 與綜述 Fig. 13）：CP 以下每個變數都能穩定、可持續；CP 以上每個變數都失控到力竭。這種「整組變數同步換檔」正是把 CP 當作真正區間界線的理由。
  - **直接的肌肉內證據（³¹P-MRS）**：Poole 等人（2016）引用單腿伸膝實驗——在 CP **之下 10%** 運動時，肌肉磷酸肌酸（PCr）、無機磷酸（Pi）、pH 都在 1–2 分鐘內達穩定並維持 20 分鐘；在 CP **之上 10%** 時，這些變數一路惡化到力竭（約 12 分鐘）。同樣地，肺攝氧、通氣、血乳酸在 CP 達穩態、在 CP +5% 則 [[VO2|VO2]] 漂向 [[VO2max|VO2max]]、乳酸無止境上升。
  - **量化落點**：以 %[[VO2max|VO2max]] 表示，健康年輕人 [[Lactate threshold|LT]]/[[Gas exchange threshold|GET]] 約 50–65%、[[Critical power|CP]] 約 70–80%；訓練有素者可達 70–80% 與 80–90%。但因人而異，這也是不該單用 %VO2max 標定強度的原因。

## 易誤解之處
1. **重度 ≠ 註定力竭。** 很多人以為「乳酸一升就撐不久」。其實在重度區間（LT~CP），乳酸雖高但能穩住，仍可維持相當長時間。真正「穩不住、一路到力竭」的是 CP 之上的極重度區間。
2. **界線要用 [[VO2]] 標、別用功率。** 同一個閾值用瓦數表示會隨遞增速率漂移；用 VO2（代謝率）表示才穩定可比。
3. **「百分之幾 VO2max」會誤導。** 同樣是 70% VO2max，對 A 可能在重度、對 B 可能在極重度，因為每個人 LT 和 CP 落在 VO2max 的比例不同。要用區間，不要只用相對百分比。
4. **LT 不是最重要的那條線。** 這是本綜述要矯正的核心錯置：原始 AT 概念想抓的「能不能持續」，其實是 CP 在管的，不是 LT。
5. **「極重度」不是均質的一段——它內部還要再切一刀。** 本頁把 [[Critical power|CP]] 之上統稱極重度（severe），但嚴格的四分法在 CP 之上還有一道界線——[[Maximal intensity for VO2max attainment|IHIGH（達到 VO2max 的最高強度）]]：
   - **severe（CP ~ IHIGH）**：撐的時間夠長，[[VO2 slow component|慢成分]] 有時間把 [[VO2|VO2]] 推到 [[VO2max|VO2max]]；力竭、VO2 到頂、[[W prime|W′]] 耗盡大致同時發生。
   - **[[Extreme intensity domain|extreme（極限強度）]]（> IHIGH）**：力竭太快，慢成分來不及發展、VO2 還沒爬到頂就結束，[[VO2max|VO2max]] 達不到、W′ 也沒燒乾。後果：CP 的 t_lim 公式（假設「力竭＝W′ 耗盡」）會在這裡**高估**耐受，且愈往上愈不準（Ventura 2023；完整見 [[Extreme intensity domain|極限強度域]]）。
   這帶出一個實務陷阱：就算兩個人用同樣的 [[W prime|W′]] 消耗量做間歇（[[W prime-matched interval prescription|W′ 配平處方]]），[[W prime|W′]]較小的人那份功率可能落在更高的次區間（甚至跨進 extreme）——**劑量配平了，強度落點卻沒配平**（Miller 2023 列為限制）。
   *（術語提醒：本 wiki 早期把 CP 之上全部叫「極重度／severe」；採四分法後，「severe」專指 CP→IHIGH，「extreme（極限強度）」專指 >IHIGH。）*

## 用生活例子再講一次
把運動強度想成開車的轉速區。**中等**＝市區巡航，引擎輕鬆、水溫穩定，能開整天（< LT）。**重度**＝爬長坡，引擎吼、水溫升高但停在一個偏高卻穩定的刻度，撐得住只是吃力（LT~CP）。**極重度**＝紅線區猛催，水溫一路飆、警示燈狂閃，再撐下去必定熄火，能撐幾分鐘由油箱裡那點備用油（W′）決定（> CP）。真正決定「會不會開到拋錨」的，是有沒有越過紅線（CP），而不是水溫剛開始上升那一刻（LT）。

（失準之處：引擎轉速區的界線是固定刻度；人的 LT 與 CP 會隨訓練移動，且界線是統計/數學定義的，不是儀表板上印死的紅線。）

## 換句話說
換句話說，運動強度區間是用兩道自然界線——[[Lactate threshold|LT]] 和 [[Critical power|CP]]——把強度切成「能久撐（中等）／吃力但能穩（重度）／註定力竭（極重度）」三段。它的重要矯正是：別把 LT 當成最關鍵的線，真正分出「持續 vs 力竭」的是更高的 CP。

## 來源
- [[source-Poole-2021-AT-controversy]]（Coincidence of exercise thresholds：三區間定義、LT 切 moderate-heavy、CP 切 heavy-severe、奧運項目落點。）
- [[source-Poole-2016-critical-power]]（CP 作為 heavy-severe 邊界的 ³¹P-MRS 肌肉內證據、肺氣體/乳酸穩態實驗、%VO2max 落點。）
- [[source-Goulding-2021-VO2-kinetics-tolerance]]（重度=Pi 略高於臨界而穩定、極重度=Pi 跑向尖峰而力竭的臨界閾值機制；間歇運動把功率與代謝負荷脫鉤、提高耐受。）
- [[source-Miller-2023-fast-start-HIIE]]（易誤解 #5：極重度域可再細分次區間（extreme 力竭太快、達不到 VO2max）；配平 W′ 消耗不保證配平次區間落點，W′ 較小者同 ΔW′ 可能落在更高次區間——Discussion 列為本研究限制。）
- [[source-Ventura-2023-severe-extreme-tolerance]]（易誤解 #5：以 [[Maximal intensity for VO2max attainment|IHIGH]] 把 CP 之上精確切成 severe（仍達 VO2max）與 [[Extreme intensity domain|extreme]]（達不到 VO2max、CP 模型高估耐受）；四分法術語釐清。）
- [[source-Coates-2023-HIIT-perspective]]（第 2 節：本生理三/四域分類與公衛「輕/中等/費力」分級是兩套不同語言、邊界不對齊；詳見 [[Physical activity intensity classification|身體活動強度分級]]。）
- [[source-Storoschuk-2025-zone-2-review]]（§3：Zone 2＝中等強度域（<LT1）的訓練語言名稱；同一標籤的絕對強度因人而異極大。對應推導第 3 步中等域 gloss。）
