---
type: concept
aliases: [三分鐘全力測試, 3分鐘全力測試, 三分鐘衝刺測試, 3-min all-out test, 3MT, end power, EP, 末段功率, work above end power, WEP, 末段功率以上之功]
tags: [exercise-physiology, methods, performance]
sources: [source-Poole-2016-critical-power, source-Black-2023-dynamic-power-duration, source-Sreedhara-2019-power-models-survey, source-Jones-2010-CP-implications, source-Wright-2017-3MT-reliability-validity]
prerequisites: [臨界功率／臨界速度（critical power / critical speed, CP/CS）, W′（臨界功率以上的有限功容量）, 等速 vs 線性測功車模式（isokinetic vs linear ergometer mode）]
created: 2026-06-10
updated: 2026-06-12
---

# 三分鐘全力測試（3-minute all-out test）

## 本質（一句話）
三分鐘全力測試就是「叫人從頭到尾用盡全力踩 3 分鐘，到最後力氣榨乾、功率自己掉到一個平台——那個平台就是 [[Critical power|臨界功率（CP）]]，前面多踩出來的那塊就是 [[W prime|W′]]」——用一次測試、一次就量出兩個參數。

## 前置概念
- [[Critical power|臨界功率（critical power, CP/CS）]]
  （這測試的目的就是量 CP；先懂 CP 是什麼。）
- [[W prime|W′（臨界功率以上的有限功容量）]]
  （測試前段榨出的就是 W′；先懂 W′。）

## 為什麼會這樣（first-principles 推導）
1. 傳統量 [[Critical power|CP]]/[[W prime|W′]] 要做好幾天、好幾次「固定功率踩到力竭」的測試，再用雙曲線擬合，很耗時。能不能一次測完？
2. 關鍵洞見來自 [[W prime|W′]] 的性質：W′ 是「CP 之上能多做的**有限**功」。如果叫人**從第一秒就用盡全力**踩固定阻力的測功車，他會：
   - 一開始功率極高（同時瘋狂消耗 W′）；
   - W′ 愈用愈少，功率被迫往下掉；
   - 約 2.5 分鐘後 **W′ 見底（降到零）**，此時就只剩「純靠有氧、可持續」的輸出——功率**掉到一個平台不再降**。
3. 那個末段平台高度，就是 [[Critical power|CP]]（因為 CP 的定義正是「不必再動用 W′ 就能維持的最高輸出」）。而**整段功率曲線高出 CP 的那塊面積**，就是 [[W prime|W′]]（CP 之上做的總功）。一次測試、兩個參數到手。
4. 為什麼它也是研究 [[VO2max|VO2max]] 與效率的好模型？因為全力衝刺從一開始就送出「最大代謝訊號」給粒線體，把 [[VO2|VO2]] 一路逼到 [[VO2max|VO2max]]；到末段功率只剩 CP，卻仍要燒掉 VO2max 等級的氧——這個「低輸出、高耗氧」正是巨大效率損失（大 [[VO2 slow component|VO2 慢成分]]）的直接展示。
5. 它也支持「[[VO2 slow component|慢成分]] 不必靠額外招募纖維」這個論點：3 分鐘全力測試從頭就把纖維幾乎全招募了，卻仍有大慢成分——所以慢成分還有纖維內效率下降等其他來源。

### EP 與 WEP：3MT 量出來的兩個工作量（Black 2023 用語）
6. 文獻在用 3MT 時，給「末段平台」與「前段多做的功」各取了一個專名，務必認得：
   - **EP（end power，末段功率）**：3MT **最後 30 秒**的平均功率，是 [[Critical power|CP]] 的操作型代表（EP ≈ CP）。
   - **WEP（work above end power，末段功率以上之功）**：整段曲線**高出 EP 的那塊面積**，是 [[W prime|W′]] 的操作型代表（WEP ≈ W′）。
   一次 3MT → 一組 (EP, WEP) → 一組 (CP, W′)。
7. 把 3MT 當「探針」反覆用，可以量出**疲勞會不會改變 CP/W′**：做兩個 3MT、中間只休 1 分鐘（重複 3MT），第一個在休息態（C-3MT）、第二個在疲勞態（F-3MT）。Black 等（2023）發現 F-3MT 的 EP 降約 7%、WEP 降約 61%、總功（TWD）也降——也就是**先前的全力運動把 CP 與 W′ 都壓低了**（完整推導見 [[Power-duration relationship plasticity|功率–持續時間關係的可塑性]]）。這把 3MT 從「測一組固定參數」升級成「測參數會怎麼漂」的工具。

### 為什麼相信末段功率真的等於 CP：一手驗證（Jones 2010）
8. 末段平台＝CP 不是靠定義硬說的，而是直接對照驗證過：同一批人身上，用傳統「五次力竭」獨立量到的 CP，與 3MT 末段功率**幾乎重合**——10 人中 8 人兩者相差在 5 W 以內；WEP 與 W′ 也無顯著差異，只是 WEP 較不穩（變異較大）。
9. 還有一個漂亮的「跨過界線、行為相反」驗證：讓人用「末段功率**減** 15 W」做固定負荷，11 人中 9 人撐完 30 分鐘、7 人達穩態（乳酸 10→30 分上升 <1 mM）；用「末段功率**以上**」則**無人**撐完 30 分、平均約 13 分鐘力竭、VO2 升到 [[VO2max|VO2max]]、乳酸一路漲。這正是 [[Critical power|CP]]＝heavy/severe 邊界該有的行為，反過來確認末段功率就坐在 CP 上。
10. 末段功率對「該變的介入會變、不該變的不變」也對得上：4 週高強度間歇訓練把傳統 CP 與 3MT 末段功率**同步**抬高約 25 W；3MT 前 2 分鐘先做一次 30 秒全力衝刺會**壓低 WEP（≈W′）卻不動末段功率（≈CP）**——正合「先前運動耗 W′、不耗 CP」。反之，肌酸負荷、碳酸氫鈉、以及改變頭 30 秒的配速，對末段功率與 WEP **都沒有影響**——表示它估的是穩健的生理參數，不是隨手法擺動的人為產物。其他運動型態也成立：等長收縮版（連續最大隨意收縮的「末段扭矩」）同樣收斂到獨立量到的 [[Critical torque|臨界扭矩]]。

### 量得「準」嗎？測功車模式與踏頻會左右答案（Wright 2017）
11. 上面 #8–10 說末段功率「對得上」CP，是把 3MT 當概念**驗證**過了。但實務上還有一層——**用哪種測功車模式跑這個 3MT，會改變它準不準**。先分清兩個問題（見 [[Reliability and validity of measurement|信度與效度]]）：
    - **信度（穩不穩）**：同一人重做兩次，EP 一致嗎？
    - **效度（準不準）**：EP 對得上傳統多日量到的 [[Critical power|CP]] 嗎？
12. Wright 等（2017）讓 12 位車手同時做傳統 CP 測試與兩種模式的 3MT（見 [[Isokinetic vs linear ergometer mode|等速 vs 線性模式]]），結果是「**穩的不一定準**」的教科書案例：
    - **EP 在兩種模式下都很穩**（[[Reliability and validity of measurement|CoV]] 等速 1.93%、線性 1.17%，ICC 0.97–0.99）。
    - 但只有 **等速模式的 EP 準**（240.9 W vs 真 CP 244.9 W，無顯著差異）；**線性模式高估 CP 約 30 W**（275.1 W）＝穩穩地量歪。
13. 為什麼線性會高估？兩個機械／程序原因——(1) 線性模式的阻力係數是用受試者口述的「**慣用踏頻**」回推的，而那個數字常含 ±5–10 rpm 誤差，且 EP 對踏頻敏感（高 10 rpm 可降 EP ~10 W）；(2) 線性模式起始要把**飛輪**加速，那段動能被灌成假的高功率，傳統定功率測試卻沒有這段。等速模式（或 SRM 曲柄）不受飛輪慣性影響，故較乾淨。注意這**與原開發者 Vanhatalo（線性、EP≈CP）相反**，矛頭指向「定阻力的方法」而非 3MT 概念本身。
14. **W′ 這一邊更糟**：WEP 在**兩種模式下都既不穩也不準**——CoV 5–8%（不穩）、且系統性低估 W′ 達 7–9 kJ（22.7 → 15.6/13.5 kJ，不準）。Wright 由此下了比 Jones 2010 更強的結論：**3MT 不應拿來估 W′**。可能原因＝3 分鐘對某些人不足以把 W′ 榨乾，以及上述功率量測基準不一致。這把先前 #6 的「WEP≈W′」收緊成「WEP 只是個會系統性偏低、又不太穩的粗估」。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Poole 等人把 3 分鐘全力測試當成「能達到 VO2max、產生大慢成分、並完全耗盡 W′」的理想實驗模型；末段功率平台即 CP，約在 2.5 分鐘後 W′ 歸零。Wright（2017）補上實務警告：**末段功率只有在等速模式下才是有效的 CP 估計，線性模式會高估；而不論哪種模式，3MT 都不該用來估 W′**。
- **背後的推理／證據**：理由是 W′ 的「有限可耗盡」性質——只要逼人從頭全力，W′ 必在固定時間內被榨乾，剩下的就是 CP。實驗（Vanhatalo, Burnley 等）證實此末段平台與多次傳統測試擬合的 CP 一致，使單次測試成為可行的替代。

## 易誤解之處
1. **「全力」是真的從第一秒就拼盡，不是配速。** 若受試者保留體力、配速踩，W′ 不會在末段乾淨耗盡，平台就不等於 CP。正確執行要求最大努力、不留力。
2. **末段平台 = CP，不是平均功率。** 別把整段 3 分鐘的平均功率當 CP；CP 是**最後那段**穩定下來的功率（W′ 耗盡後）。
3. **它測的是 CP/W′，不是 [[VO2max|VO2max]] 本身**——雖然過程中通常會達到 VO2max。三者是不同參數，別混為一談。
4. **單次測試有便利也有誤差。** CP 本身就有 ~5% 日間變異；單次全力測試方便，但結果仍是帶誤差的估計值。
5. **EP/WEP 不是永遠等於同一組 CP/W′。** EP≈CP、WEP≈W′ 只在「新鮮、正確全力」下成立；同一個人在疲勞態做 3MT，EP 與 WEP 都會降（見 [[Power-duration relationship plasticity|可塑性]]）。所以「3MT 量到的 CP」要附帶「在什麼狀態下量的」，不能當成不變的身分證號。
6. **單次 3MT 抓不到「日間變異」，而那個變異對 3MT 還特別大。** #4 說 CP 有 ~5% 日間變異，這裡給 3MT 的具體數字：兩次 3MT 的 Bland-Altman 顯示 CP 的 95% 一致界限約 **±15 W**，而 15 W 的 CP 差攤到 3 分鐘＝**2700 J** 的 W′ 差。更麻煩的是，單次 3MT 因為是「算面積」而非「擬合曲線」，**連 W′ 的標準誤都給不出來**。所以 3MT 省時的代價，是把「這次估得有多不確定」也一起省掉了——拿單次 3MT 開處方前要把這個擺動放在心上（完整見 [[Intra-individual variability of critical power and W prime|個體內變異（IIV）]]）。

7. **「3MT 量到 CP」要連測功車模式一起講。** 同一場 3MT 在[[Isokinetic vs linear ergometer mode|線性模式]]會把 CP 高估約 30 W、在等速模式才對得上；末段功率「穩」（可重複）不等於「準」（有效）。報告 3MT 的 CP 時，模式（等速／線性）、踏頻設定與阻力如何決定，都要一併交代，否則數字無法跨研究比較。
8. **3MT 估 W′ 要打很大的折扣。** WEP 不只變異大（#6），還會**系統性低估** W′（Wright 報告低 7–9 kJ）；要 W′ 請改用多趟定功率測試擬合（見 [[Critical power estimation protocols]]），別只信一場 3MT。

## 用生活例子再講一次
想像你有一支主油箱（有氧、邊跑邊補）和一小罐 NOS（[[W prime|W′]]、用完就沒）。叫你「從綠燈起就把油門踩到底、催 3 分鐘」：一開始你猛噴 NOS，車速飆高；NOS 愈噴愈少、車速被迫往下掉；大約 2.5 分鐘 NOS 噴光，車速就**穩定在「只靠主油箱能跑的最高速」**——那個穩定速就是 CP，而前面靠 NOS 多跑出來的那截，加起來就是這罐 NOS 的總量 W′。一趟全力衝刺，就把「可持續最高速」和「NOS 容量」同時測了出來。

（失準之處：真正的 3 分鐘測試是固定阻力下功率自然衰減，不是你主動換速；而且要真的全力，留力就測不準。）

## 換句話說
換句話說，三分鐘全力測試利用「[[W prime|W′]] 會被全力榨乾」這個性質：逼人從頭拼到底，W′ 在約 2.5 分鐘耗盡後，功率自動掉到只剩 [[Critical power|CP]] 的平台；末段平台給你 CP，前段高出的總功給你 W′。一次測試同時拿到雙曲線的兩個參數，還順帶把 [[VO2|VO2]] 逼到 [[VO2max|VO2max]]。

## 來源
- [[source-Poole-2016-critical-power]]（Role of oxygen 節：3 分鐘全力測試達 VO2max、~2.5 分 W′ 歸零、末段平台＝CP、大慢成分與效率損失。）
- [[source-Black-2023-dynamic-power-duration]]（Methods：EP＝末 30 秒平均功率、WEP＝高出 EP 之功、重複 3MT（C-3MT/F-3MT，間隔 1 分）設計；Results：F-3MT EP↓7%（282→263 W）、WEP↓61%（16.9→6.3 kJ）、TWD↓，且 F-3MT 仍達 VO₂peak 確認為真力竭。）
- [[source-Sreedhara-2019-power-models-survey]]（易誤解 #6：3MT 的 trial-to-trial 變異——Bland-Altman CP ±15 W ⇒ 2700 J W′；單次 3MT 算面積故無法得 W′ 標準誤；與 CWR 比 3MT 的 W′ 有高估報告（11.37 vs 9.55 kJ）。詳見 [[Intra-individual variability of critical power and W prime]]、[[Critical power estimation protocols]]。）
- [[source-Wright-2017-3MT-reliability-validity]]（§11–14、易誤解 #7–8：12 車手同時做傳統 CP 與兩模式 3MT；EP 兩模式皆穩（CoV 1.93%/1.17%、ICC 0.97–0.99）但僅等速有效（240.9≈244.9 W）、線性高估 30 W（275.1 W）；WEP 兩模式皆不穩不準、系統低估 W′ 7–9 kJ → 「3MT 不應估 W′」；高估歸因慣用踏頻誤差＋飛輪慣性，與 Vanhatalo 線性結論相反。）
- [[source-Jones-2010-CP-implications]]（§8–10：Application to All-Out Exercise 節的一手驗證——末段功率 8/10 與獨立 CP 相差 ≤5 W、WEP≈W′ 但較變異（Vanhatalo et al.）；末段功率 −15 W 可 30 分穩態、+以上 13 分力竭達 VO2max；4 週 HIIT 同抬 CP 與末段功率 ~25 W、前置 30 s 衝刺壓 WEP 不動末段功率；肌酸/碳酸氫鈉/頭 30 s 配速皆不改末段功率與 WEP；Burnley 間歇 MVC 末段扭矩≈[[Critical torque|臨界扭矩]]的跨型態類比。）
