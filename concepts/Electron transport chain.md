---
type: concept
aliases: [電子傳遞鏈, 呼吸鏈, 電子傳遞鍊, electron transport chain, ETC, respiratory chain]
tags: [exercise-physiology, metabolism, foundation, bioenergetics]
sources: [source-Hargreaves-2020-muscle-energy-metabolism]
prerequisites: [Reducing equivalents, ATP, Oxidative phosphorylation, Mitochondrial respiratory control]
created: 2026-06-12
updated: 2026-06-12
---

# 電子傳遞鏈（electron transport chain，ETC）

## 本質（一句話）
電子傳遞鏈是粒線體內膜上的「兌現窗口」——把載著高能電子的車（還原當量）開來卸貨，一階一階放掉電子的能量去打造大量 ATP，最後把電子交給氧氣變成水。

## 前置概念
- [[Reducing equivalents|還原當量（NADH、FADH₂）]]（電子傳遞鏈的進料就是這些載著電子的車。）
- [[ATP]]（電子傳遞鏈的產物，也是整個有氧代謝的終點。）
- [[Oxidative phosphorylation|氧化磷酸化]]（電子傳遞鏈是氧化磷酸化「真正產 ATP、真正用氧」的那一段。）
- [[Mitochondrial respiratory control|粒線體呼吸控制]]（ADP 一升就驅動這條鏈加速——這就是它的油門。）

## 為什麼會這樣（first-principles 推導）
1. 由 [[Reducing equivalents|還原當量]]：醣解、[[TCA cycle|TCA 循環]]、[[Beta-oxidation|β 氧化]] 把食物的能量裝成一車車 NADH、FADH₂。現在要把這些車的能量**兌成 ATP**。兌現的地方就是電子傳遞鏈。
2. 它在哪裡：**粒線體內膜**上，由一串蛋白質複合體排成一條「鏈」。
3. 它怎麼運作（抓邏輯，不必記每個複合體）：
   - 載滿的車（NADH、FADH₂）開到鏈的入口，把**電子**卸下交給鏈。
   - 電子沿著這條鏈**一階一階往下傳**，每傳一階就放掉一點能量。為什麼要分階？因為一次放掉全部能量會浪費成熱；分階釋放，才能把能量收集起來利用。
   - 這些被收集的能量被拿去**把 ADP＋Pi 接成 ATP**（即 [[Oxidative phosphorylation|氧化磷酸化]] 的核心動作）。
   - 走到鏈的**終點**，已經沒什麼能量的電子必須交給**氧氣**——氧氣接了電子、再配上氫，就變成**水**。氧氣是「最終電子接收者」。
4. 這裡才是「**為什麼產能一定要耗氧**」的最終答案：氧氣是整條鏈末端唯一的電子出口。氧氣若缺席，電子就堵在鏈上、卸不掉貨，所有滿載的車回不了空車狀態，於是 [[TCA cycle|TCA]]、[[Beta-oxidation|β 氧化]] 全部因「無空車可用」而停擺。**整個有氧代謝的命脈，就拴在這個末端的氧氣出口上。** 你吸進的氧氣，最終幾乎都用在這一步。
5. 它的速率怎麼被控制：當肌肉花掉 ATP、ADP 與 Pi 增加，這條鏈被驅動加速產 ATP——這個「ADP 一多就加速」的關係就是 [[Mitochondrial respiratory control|粒線體呼吸控制]]，也是 [[VO2 kinetics|VO2 動力學]] 與 [[O2 deficit|氧虧]] 存在的最底層原因。
6. 它的最大速率（能多快地用掉氧氣）就封頂了全身的 [[VO2max]]——不過實務上 VO2max 多半先被「氧氣送得多快（心肺輸送）」卡住，而非這條鏈本身的容量。

## 文獻怎麼說 vs 為什麼這樣說
- **主張**：粒線體的呼吸鏈（電子傳遞鏈）需要 NADH/FADH₂ 形式的還原當量、游離 ADP、Pi 與 O₂；在 O₂ 與 ADP、Pi 充足下，運動時 ADP 濃度上升被認為是活化呼吸鏈產 ATP 的關鍵；把 ATP 移出粒線體、ADP/Pi 移回粒線體的轉運比過去認為的受更嚴格調控。
- **背後的推理**：把四項投入（還原當量、ADP、Pi、O₂）並列，是要強調這條鏈是「醣脂代謝（供還原當量）」與「心肺循環（供 O₂）」兩大系統的匯流終點——任一缺位都會限制它。ADP 作為驅動訊號，呼應 [[Mitochondrial respiratory control|呼吸控制]]：產能精準跟隨花用。

## 易誤解之處
1. **氧氣用在「最末端收電子」，不是用來燒每一步。** 前面拆食物（醣解、TCA、β 氧化）都不直接碰氧；氧氣只在這條鏈的終點當電子出口。但因為這個出口一塞、全線停擺，所以整套代謝「實質上」全依賴氧——「有氧」之名由此而來。
2. **這裡才是大量 ATP 真正產出的地方。** [[TCA cycle|TCA]] 只是把能量裝上車，電子傳遞鏈才把車兌成 ATP。把產 ATP 的功勞算給 TCA 是常見錯置。
3. **缺氧不是「這條鏈壞了」，是「出口被堵」。** 鏈本身沒問題，只是末端沒有氧氣收電子，整條輸送線回堵。這也說明了為何運動肌肉其實很少真的缺氧到限制這條鏈（見 [[Dysoxia|dysoxia]]）——限制通常在更上游的輸送。

## 用生活例子再講一次
把電子傳遞鏈想成水力發電廠的一道**階梯式洩洪道**。滿載的計程車（NADH、FADH₂）把水（電子）倒進最高的閘口，水順著一階一階的落差往下流，每一階都推動一台小發電機（產 ATP）。分階落水的好處是「每一階都榨出電」，而不是一口氣沖到底白白浪費。流到最底層的水必須有個排水口才流得走——這個排水口就是**氧氣**，水（電子）在這裡被氧氣接走、變成水（H₂O）排掉。排水口一旦堵住（缺氧），整條洩洪道立刻回堵、上游所有發電機停轉。

（這個類比在哪裡會失準：洩洪道的水是被動往低處流；電子傳遞鏈傳電子其實是嚴密的化學接力，且它的「水量」（通量）會被 ADP 即時調節——花用愈多、放水愈快，這種需求驅動的靈敏度，單純的重力洩洪沒有。）

## 換句話說
換句話說，電子傳遞鏈＝粒線體內膜上的兌現窗口：把 [[Reducing equivalents|還原當量]]載來的電子一階階卸下、把落差能量收成大量 [[ATP]]，電子最後交給氧氣變水。它是 [[TCA cycle|TCA]]／[[Beta-oxidation|β 氧化]]（供電子）與心肺循環（供氧）的匯流終點，也是「產能為何非耗氧不可」的最終答案——氧氣就是這條鏈唯一的電子出口。

## 來源
- [[source-Hargreaves-2020-muscle-energy-metabolism]]（"Aerobic exercise" 節：呼吸鏈需 NADH/FADH₂、ADP、Pi、O₂；ADP 上升活化呼吸鏈產 ATP；ATP/ADP/Pi 跨粒線體膜轉運受嚴格調控。呼吸控制見 [[Mitochondrial respiratory control]]。）
