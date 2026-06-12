---
type: concept
aliases: [受質層次磷酸化, 受質層級磷酸化, 基質層次磷酸化, substrate-level phosphorylation, 無氧產能, anaerobic ATP production]
tags: [exercise-physiology, metabolism, foundation, bioenergetics]
sources: [source-Hargreaves-2020-muscle-energy-metabolism]
prerequisites: [ATP, Phosphocreatine, Glycolysis]
created: 2026-06-12
updated: 2026-06-12
---

# 受質層次磷酸化（substrate-level phosphorylation）

## 本質（一句話）
受質層次磷酸化就是「不靠氧氣、直接把一個磷酸從某個分子上摘下來、當場接到 ADP 上補成 ATP」——是肌肉最快能調出能量的應急手段。

## 前置概念
- [[ATP]]
  （要懂這個，你得先懂：補 ATP＝把 ADP＋Pi 重新接成 ATP。本頁講的是「不用氧氣、最快的那種接法」。）
- [[Phosphocreatine|磷酸肌酸（PCr）]] 與 [[Glycolysis|醣解]]
  （這兩條就是受質層次磷酸化的兩個實例；本頁是把它們抽象成同一個機制。）

## 為什麼會這樣（first-principles 推導）
1. 由 [[ATP]]：補 ATP 有兩大類辦法。一類**靠氧氣**、在粒線體裡慢慢做（[[Oxidative phosphorylation|氧化磷酸化]]）；另一類**不靠氧氣**、在細胞質裡當場做——後者就是受質層次磷酸化。
2. 「磷酸化（phosphorylation）」＝「把一個磷酸基接上去」。這裡接的對象是 ADP，接上一個磷酸就變回 ATP。
3. 「受質層次（substrate-level）」是關鍵限定詞：磷酸的來源是**某個已經帶著高能磷酸的分子（即『受質』）**，直接把這個磷酸**手交手**遞給 ADP。不繞道粒線體、不需要氧氣、不需要電子傳遞鏈。
4. 身體有兩個這樣的「手交手」實例：
   - **[[Phosphocreatine|磷酸肌酸（PCr）]]**：PCr 身上帶一個高能磷酸，直接捐給 ADP → ATP＋肌酸。只要一步反應，**幾毫秒**就完成，是最快的。
   - **[[Glycolysis|醣解]]**：把葡萄糖／肝醣拆解的過程中，有幾步會把中間產物上的磷酸直接交給 ADP，淨得少量 ATP，並產出 [[Lactate|乳酸]]。
5. 為什麼這種辦法「快但有限」：因為它不必等氧氣送到、不必等粒線體轉起來，所以**啟動極快**；但 PCr 庫存只夠幾秒，醣解又會愈做愈酸（[[Proton inhibition of glycolysis|H⁺ 回頭抑制醣解酵素]]）而自我設限。所以它擅長「瞬間爆發、短時間頂著」，撐不了長時間——這正是 [[Power and capacity of energy systems|高功率、低容量]] 的由來。
6. 與氧化路的分工：運動一開始 ATP 需求瞬間跳高，但 [[Oxidative phosphorylation|氧化磷酸化]] 要花時間才轉得上來；這段空檔就由受質層次磷酸化頂著，頂出來的缺口就是 [[O2 deficit|氧虧]]。

## 文獻怎麼說 vs 為什麼這樣說
- **主張**：Hargreaves & Spriet 把補 ATP 的路徑分成 substrate-level phosphorylation（'anaerobic'，含 PCr 分解與肝醣分解到乳酸）與 oxidative phosphorylation（'aerobic'）兩大類；前者功率高、容量小。
- **背後的推理**：因為這兩條不需氧、反應步數少（PCr 一步、醣解十步上下），啟動以毫秒計；全力衝刺時，6–10 秒後 PCr 與醣解兩條的無氧供能貢獻大致相當。容量小則是物理事實——PCr 約 75 mmol/kg 乾肌、醣解約三倍但被酸度卡住。

## 易誤解之處
1. **「anaerobic（無氧）」是指這條路不需要氧氣參與反應，不是指當下肌肉缺氧。** 受質層次磷酸化從運動第一秒就在用，那時組織根本不缺氧（見 [[Dysoxia|dysoxia]]）。把「動用無氧路」讀成「缺氧」是經典錯誤。
2. **它和氧化磷酸化不是「先用完這個才換那個」，而是一開始就同時啟動、只是比例不同。** 連 30 秒全力衝刺裡，後段也有約一半能量來自有氧。

## 用生活例子再講一次
想像你急需現金。受質層次磷酸化就像「跟身邊的人手交手借錢」——口袋裡那張應急鈔票（PCr）掏出來最快，或找街口攤販快速週轉（醣解，但要付利息＝產酸）。它的優點是**立刻到手、不必跑銀行**；缺點是金額有限、利息會愈滾愈高。要源源不絕的大錢，還是得靠「銀行轉帳」（[[Oxidative phosphorylation|氧化磷酸化]]）那條慢但量大的路。

（這個類比在哪裡會失準：手交手借錢可以借很多次，但 PCr 庫存是固定的一小筆、醣解則被酸度自我喊停，所以「應急」真的只能應急。）

## 換句話說
換句話說，受質層次磷酸化＝不靠氧、把磷酸從某分子直接遞給 ADP 補成 ATP 的應急產能。它有兩個實例（[[Phosphocreatine|PCr]] 與 [[Glycolysis|醣解]]），共同特點是**啟動極快、容量有限**，負責墊運動起始與高強度爆發那段 [[Oxidative phosphorylation|有氧主引擎]]還沒跟上的缺口（即 [[O2 deficit|氧虧]]）。

## 來源
- [[source-Hargreaves-2020-muscle-energy-metabolism]]（Box 1 與 "Intense short-term exercise" 節：substrate-level phosphorylation 含 PCr 分解、腺苷酸激酶、肝醣分解到乳酸；無氧路功率高容量小、PCr 與醣解貢獻在 6–10 s 後相當。）
