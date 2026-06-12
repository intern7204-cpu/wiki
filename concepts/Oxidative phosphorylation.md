---
type: concept
aliases: [氧化磷酸化, oxidative phosphorylation, OXPHOS, 有氧產能, aerobic ATP production]
tags: [exercise-physiology, metabolism, foundation, bioenergetics]
sources: [source-Hargreaves-2020-muscle-energy-metabolism]
prerequisites: [ATP, Cellular respiration（細胞呼吸）, Reducing equivalents, Electron transport chain]
created: 2026-06-12
updated: 2026-06-12
---

# 氧化磷酸化（oxidative phosphorylation）

## 本質（一句話）
氧化磷酸化就是「在粒線體裡用氧氣把食物徹底燒乾、藉此大量補回 ATP」的那條主引擎——慢半拍才轉得上來，但量大又能撐久。

## 前置概念
- [[ATP]]（補 ATP 的三條路，氧化磷酸化是其中最慢但容量最大的一條。）
- [[Cellular respiration|細胞呼吸（cellular respiration）]]（氧化磷酸化是細胞呼吸在分子層的「最後產 ATP」那一段。）
- [[Reducing equivalents|還原當量（NADH、FADH₂）]] 與 [[Electron transport chain|電子傳遞鏈]]（氧化磷酸化真正榨出 ATP 的零件，本頁是它們的上層統稱。）

## 為什麼會這樣（first-principles 推導）
1. 由 [[ATP]]：不靠氧的 [[Substrate-level phosphorylation|受質層次磷酸化]] 啟動快但容量小。要長時間、大量地補 ATP，得靠**靠氧氣**的這條——氧化磷酸化。
2. 拆名字：「氧化（oxidative）」＝過程要用到氧氣把食物的電子一路氧化掉；「磷酸化（phosphorylation）」＝把磷酸接到 ADP 上補成 ATP。合起來＝「靠氧化反應驅動的補 ATP」。
3. 它發生在**粒線體**（細胞裡的發電廠）。流程分兩段：
   - **先收集電子**：醣（經 [[Glycolysis|醣解]]→[[Pyruvate dehydrogenase|PDH]]）和脂肪（經 [[Beta-oxidation|β 氧化]]）都先變成 [[Acetyl-CoA|乙醯輔酶 A]]，進 [[TCA cycle|TCA 循環]] 被拆光，把能量裝上 [[Reducing equivalents|還原當量（NADH、FADH₂）]]。
   - **再兌成 ATP**：滿載的還原當量把電子交給 [[Electron transport chain|電子傳遞鏈]]，電子的能量被一階階釋放、驅動 ATP 合成，電子最後交給**氧氣**變成水。
4. 為什麼「慢但量大又耐久」：
   - **慢**——要等氧氣由心肺循環送達、等粒線體酵素活化、等整條輸送線轉起來，所以從靜止換到運動會有一段延遲（這段延遲的可量版本就是 [[VO2 kinetics|VO2 動力學]]）。
   - **量大**——一個葡萄糖經這條路產約 36 個 ATP，比醣解淨得的 2–3 個多一個量級；脂肪酸更是一次給出上百個。
   - **耐久**——燃料來源（肝醣、血糖、脂肪）儲量龐大，氧氣又源源不絕，所以能撐數小時。
5. 它的「速率上限」由能把氧氣用掉的最大速度封頂——這就是 [[VO2max]]；而它對 ADP 濃度的反應方式（ADP 一升就被驅動加速）就是 [[Mitochondrial respiratory control|粒線體呼吸控制]]。

## 文獻怎麼說 vs 為什麼這樣說
- **主張**：oxidative phosphorylation 是 'aerobic' 路徑，功率低於無氧路但容量大得多；運動超過約 1 分鐘後就成為主要的產 ATP 路徑，肌肉肝醣是主燃料。
- **背後的推理**：因為它依賴心肺把 O₂ 送到、依賴醣與脂肪氧化提供還原當量，這些都要時間到位，故起始慢；但燃料庫存與供氧近乎不竭，故容量大、能久撐。功率上限受 O₂ 輸送限制，正是 [[VO2max]] 主要被輸送（而非肌肉用氧）卡住的原因。

## 易誤解之處
1. **氧化磷酸化的「氧」用在最末端，不是用在燒每一步。** 氧氣只在電子傳遞鏈的終點當「收電子的人」；中段拆食物（醣解、TCA、β 氧化）並不直接碰氧。但因為終點的氧氣一缺、整條線就塞住，所以全程「實質上」都依賴氧。
2. **它不是運動開始後才被叫醒、之前都睡著。** 從第一秒就同步啟動，只是要時間才轉到全速；那段「還沒到全速」的缺口由無氧路頂著（[[O2 deficit|氧虧]]）。
3. **「補大量 ATP」不等於「立刻補上」。** 它的強項是容量與耐久，不是反應速度；要應付瞬間爆發，仍得靠 [[Substrate-level phosphorylation|受質層次磷酸化]]。

## 用生活例子再講一次
氧化磷酸化像「薪水入帳＋銀行轉帳」這條金流。它到帳慢（要等發薪日／系統處理），但**金額大、月月不斷**，足以支撐你的長期開銷。相對地，[[Substrate-level phosphorylation|受質層次磷酸化]]是口袋現金與快速週轉——到手快但量小。一個人能不能長時間維持高消費（持久運動），看的就是這條「薪資金流」的上限有多高，也就是 [[VO2max]]。

（這個類比在哪裡會失準：薪水是固定週期到帳，氧化磷酸化卻是「需求一升、ADP 一多就即時加速」的連續調節——它對需求的靈敏跟隨，是 [[Mitochondrial respiratory control|粒線體呼吸控制]]的重點，銀行轉帳沒這麼即時。）

## 換句話說
換句話說，氧化磷酸化＝在粒線體裡用氧氣把醣和脂肪燒乾、藉此大量且持久地補 ATP 的有氧主引擎。它的零件是 [[TCA cycle|TCA 循環]]（收集電子到還原當量）＋[[Electron transport chain|電子傳遞鏈]]（把電子能量兌成 ATP、氧氣收尾）；它慢啟動、大容量、靠 O₂，速率上限就是 [[VO2max]]。

## 來源
- [[source-Hargreaves-2020-muscle-energy-metabolism]]（Box 1 與 "Aerobic exercise" 節：oxidative phosphorylation 依賴心肺供氧與醣／脂代謝提供還原當量；運動 >1 min 後成為主要產 ATP 路徑；功率低容量大。）
