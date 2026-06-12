---
type: concept
aliases: [TCA循環, 三羧酸循環, 檸檬酸循環, 克氏循環, Krebs cycle, TCA cycle, tricarboxylic acid cycle, citric acid cycle]
tags: [exercise-physiology, metabolism, foundation, bioenergetics]
sources: [source-Hargreaves-2020-muscle-energy-metabolism]
prerequisites: [Acetyl-CoA, Reducing equivalents, Electron transport chain]
created: 2026-06-12
updated: 2026-06-12
---

# 三羧酸循環（TCA cycle / Krebs cycle）

## 本質（一句話）
TCA 循環是粒線體裡的一個「轉圈拆解機」——把每塊燃料磚（乙醯輔酶 A）的碳徹底拆成 CO₂，並把拆出來的能量裝滿一車車還原當量，送去下一站兌成 ATP。

## 前置概念
- [[Acetyl-CoA|乙醯輔酶 A]]（TCA 循環的進料；醣和脂肪都先變成它才進來。）
- [[Reducing equivalents|還原當量（NADH、FADH₂）]]（TCA 循環的主要產物——它本身不直接產很多 ATP，而是產「載著能量的車」。）
- [[Electron transport chain|電子傳遞鏈]]（TCA 裝好的車送去這裡卸貨換 ATP；先知道有下一站。）

## 為什麼會這樣（first-principles 推導）
1. 由 [[Acetyl-CoA|乙醯輔酶 A]]：醣與脂肪都先做成這塊兩碳燃料磚。現在要把磚的能量真正榨出來。
2. 怎麼榨？把磚上的碳一個一個氧化掉、變成 CO₂，同時把每一步釋放的能量**裝到 [[Reducing equivalents|還原當量]] 上**。這個「逐步氧化、邊拆邊充電」的過程被安排成一個**循環**。
3. 為什麼設計成循環而不是直線？因為循環的起點分子可以**重複使用**：乙醯輔酶 A 的兩個碳先掛到一個既有的接收分子（草醯乙酸）上，繞一圈把這兩個碳氧化成 2 個 CO₂ 後，接收分子又回到原狀、等下一塊磚。如此一塊接一塊、源源不絕，不必每次都重造接收分子。
4. 繞一圈的收穫（抓重點即可，數字不必硬背）：
   - 把乙醯基的 2 個碳拆成 **2 個 CO₂**（這就是你呼出的 CO₂ 的來源之一，呼應 [[Cellular respiration|細胞呼吸]]）。
   - 充出數車 **[[Reducing equivalents|NADH 與 FADH₂]]**（這是主要收穫，能量幾乎都裝在這些車上）。
   - 順手以 [[Substrate-level phosphorylation|受質層次磷酸化]] 直接做出極少量 ATP（相對於下游簡直不值一提）。
5. 關鍵分工：**TCA 循環本身不消耗氧氣、也不直接產大量 ATP**。它的職責是「收集電子、裝滿車」。真正用掉氧氣、把這些車兌成大量 ATP 的，是下一站 [[Electron transport chain|電子傳遞鏈]]。理解這個分工很重要——它解釋了為何 TCA 是有氧代謝的一部分（沒氧氣，下游塞車，車卸不掉，TCA 也被迫停），卻又不在自己這步用氧。
6. 它怎麼被調快調慢：運動時粒線體內**鈣離子（Ca²⁺）**升高，活化循環裡的兩個去氫酶（isocitrate、α-ketoglutarate dehydrogenase），加上受質堆積與局部調節因子細調，使通量跟上需求——又是一個 [[Dual-stage control of metabolism|鈣前饋＋受質回饋]] 的實例。

## 文獻怎麼說 vs 為什麼這樣說
- **主張**：TCA 循環專責產出還原當量，接受主要來自醣與脂肪的乙醯輔酶 A；運動時上升的粒線體鈣活化 isocitrate 與 α-ketoglutarate 去氫酶，受質與局部調節因子細調通量，citrate synthase 控制整體循環通量。
- **背後的推理**：把 TCA 定位成「還原當量工廠」而非「ATP 工廠」，是因為實測它每圈直接產的 ATP 微乎其微，能量幾乎全在 NADH/FADH₂ 裡、留待電子傳遞鏈兌現。鈣同時活化磷酸化酶、PDH、TCA 去氫酶，顯示鈣是貫穿整條供能線的共同前饋訊號。

## 易誤解之處
1. **TCA 循環自己不太產 ATP，也不直接用氧。** 它產的是「載能量的車」（還原當量）。把 TCA 當成主要 ATP 來源是常見誤解——大頭在下游的 [[Electron transport chain|電子傳遞鏈]]。但它仍屬有氧代謝，因為車卸不掉（缺氧）它就得停。
2. **它是循環、起點分子會回收。** 乙醯基的碳變成 CO₂ 離開，但承載它的接收分子繞一圈後復原、再接下一塊磚。所以「投入的是乙醯輔酶 A、消耗掉的是它的兩個碳」，不是整個循環的分子都被耗掉。
3. **你呼出的 CO₂ 主要從這裡來。** 不是從肺「混進來」，而是 TCA 把燃料的碳氧化掉的直接產物——這把 [[VCO2|VCO2]] 與真實代謝綁在一起。

## 用生活例子再講一次
把 TCA 循環想成一座**旋轉式拆解台**。你把一塊燃料磚（乙醯輔酶 A）放上轉台，轉一圈的過程中，工人把磚上的碳逐一拆下、當廢氣（CO₂）排掉，同時把拆解釋放的能量一桶一桶裝進「電子計程車」（NADH、FADH₂）。轉台本身幾乎不發電，它的產品是**一車車裝滿能量的計程車**，這些車開去隔壁發電廠（電子傳遞鏈）才真正換成電（ATP）。轉台轉完一圈會回到起始位置，等下一塊磚。

（這個類比在哪裡會失準：旋轉拆解台就算隔壁發電廠停電也能照轉；TCA 循環卻會因為下游缺氧、計程車全部滿載卸不了貨而「無空車可裝」被迫停轉——它表面不用氧，命脈卻拴在氧氣上。）

## 換句話說
換句話說，TCA 循環＝粒線體裡把 [[Acetyl-CoA|燃料磚]] 的碳逐一氧化成 CO₂、並把能量裝滿 [[Reducing equivalents|還原當量]]的旋轉拆解機。它不直接產多少 ATP、自己也不耗氧，職責是「收集電子上車」；真正的發電在下一站 [[Electron transport chain|電子傳遞鏈]]。鈣與受質讓它的轉速跟著運動需求走。

## 來源
- [[source-Hargreaves-2020-muscle-energy-metabolism]]（"Aerobic exercise" 節：TCA 循環專責產還原當量、接受醣與脂肪來的乙醯輔酶 A、鈣活化 isocitrate/α-ketoglutarate 去氫酶、citrate synthase 控通量。）
