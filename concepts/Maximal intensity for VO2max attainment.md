---
type: concept
aliases: [達到VO2max的最高強度, 最高可達VO2max強度, IHIGH, I_HIGH, highest intensity for VO2max, maximal intensity for VO2max attainment, severe-extreme boundary]
tags: [exercise-physiology, thresholds, VO2-kinetics]
sources: [source-Ventura-2023-severe-extreme-tolerance, source-Jones-2010-CP-implications]
prerequisites: [最大攝氧量（VO2max）, VO2 動力學（VO2 kinetics）, 運動強度區間（exercise intensity domains）]
created: 2026-06-12
updated: 2026-06-12
---

# 達到 VO2max 的最高強度（IHIGH, maximal intensity for VO2max attainment）

## 本質（一句話）
IHIGH 就是「你還能在力竭之前、把攝氧量逼到最大值（[[VO2max|VO2max]]）的那個**最高**運動強度」——再高一點點，運動就結束得太快，攝氧量還沒爬到頂你就先力竭了。它正好是 severe 與 extreme 兩個強度區間的分界線。

## 前置概念
- [[VO2max|最大攝氧量（VO2max）]]
  （IHIGH 是用「能不能達到 VO2max」來定義的；先懂 VO2max 是攝氧能力的天花板。）
- [[VO2 kinetics|VO2 動力學（VO2 kinetics）]]
  （關鍵在於「VO2 爬到頂需要時間」；先懂 VO2 不是瞬間跳到位、而是有速度（τ）地逼近。）
- [[Exercise intensity domains|運動強度區間（exercise intensity domains）]]
  （IHIGH 是區間框架裡再多切出來的一道界線；先懂強度怎麼分區。）

## 為什麼會這樣（first-principles 推導）
一步一步來，每一步只用前面的事實：

1. 由 [[VO2 kinetics|VO2 動力學]]：運動一開始，攝氧量不會瞬間跳到該有的值，而是要花**時間**爬升。在 [[Critical power|CP]] 之上的高強度，[[VO2 slow component|慢成分]] 還會把 VO2 一路往上推，最終（如果撐得夠久）推到 [[VO2max|VO2max]]。重點是：**「把 VO2 推到最大值」這件事本身需要一段時間。**
2. 由 [[Critical power|CP]] 的公式 t_lim = W′/(P−CP)：強度（P）愈高，能撐的時間（t_lim）愈短。
3. 把第 1、2 步擺在一起，就會出現一個**競賽**：一邊是「VO2 爬到頂需要的時間」，另一邊是「這個強度下你能撐的時間」。
   - 強度不太高時：你撐的時間 > VO2 爬到頂所需 → VO2 來得及抵達 [[VO2max|VO2max]]。
   - 強度高到某個點之後：你撐的時間 < VO2 爬到頂所需 → 你**還沒**把 VO2 逼到頂就先力竭了。
4. 這兩種情況的**轉捩強度**——「VO2 還剛好來得及達到最大值的最高強度」——就是 **IHIGH**。它是 severe 區間的**上界**，也是 [[Extreme intensity domain|extreme（極限強度）域]] 的**下界**。

### severe 域是「力竭時剛好達到 VO2max」的一條帶（Jones 2010 的歷史定位）
把 IHIGH 和 [[Critical power|CP]] 一起看，severe 域其實被**兩條都和 VO2max 有關**的界線夾住：
- **下界＝CP**：歷史上曾有一場爭論——Wilkie 認為 CP 落在 VO2max 對應功率**之上**，Moritani 卻認為 CP＝[[Anaerobic threshold|無氧閾值]]（低得多）。Jones 等判定兩者皆非：CP **不可能高於** VO2max 對應的功率；但只要強度**剛過 CP**、讓 [[VO2 slow component|慢成分]]跑完，VO2 終究會被推到 VO2max。所以 CP 是「力竭時仍**能**達到 VO2max 的**最低**功率」。
- **上界＝IHIGH**：力竭時仍能達到 VO2max 的**最高**功率（本頁）。
所以 severe 域可一句話定義成：「**力竭時 VO2 會剛好達到 VO2max**」的整段強度帶；CP 之下（heavy）VO2 穩在 VO2max 以下、IHIGH 之上（extreme）力竭太快來不及到頂。這也解釋了 [[Critical power|CP]] 易誤解 #2「CP≠VO2max」的另一面：CP 雖低於 VO2max 對應功率，卻是「會在力竭時碰到 VO2max」的下緣。

5. 怎麼實際量到它（操作定義，Turnes 2016；Ventura 2023 沿用）？用「逼近法」：
   - 從約 125% 巔峰功率（PPO）的一次定功率力竭測試開始。
   - 如果這次**達到或維持了 VO2max** → 下次再加 5% 功率，繼續試，直到某個功率**達不到** VO2max 為止。
   - 如果第一次就**達不到** → 下次降 5%，直到能達到為止。
   - IHIGH ＝「最高 15 秒平均 VO2 ≥ VO2max 減去一個體內標準差（約 4%）」的**最高**那個功率。減一個 SD 是為了避免把正常的日間量測波動誤判成「沒達到」。
6. 一個重要的精細點：**IHIGH 不是像 [[Critical power|CP]] 那樣「兩側生理反應截然相反」的鋒利閾值。** CP 上下一點點，肌肉裡的 PCr/Pi/pH 行為就翻轉（穩 vs 失控）；但 IHIGH 上下的神經肌肉與代謝反應**沒有實質性差異**（Iannetta 2022）。它更像一個「**漸進的轉換帶**」而非一條印死的線——這點對下面 [[Extreme intensity domain|extreme 域]] 為什麼「邊界附近模型還勉強能用」很關鍵。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：IHIGH 是區分 severe 與 extreme 強度域的操作性邊界——severe 域的最高強度、extreme 域的起點。
- **背後的推理／證據**：Ventura 2023 直接量到這個分界的兩側行為不同。在 IHIGH，運動中的 VO2peak（3.72 L/min）與 VO2max（3.75 L/min）**沒有差異**——確實達標；但在 IHIGH 上方 5%（IHIGH+5%），**沒有任何一位受試者達到 VO2max**，VO2peak 顯著掉到 3.50 L/min。這就是「再高一點就達不到 VO2max」的直接證據，定出了這道界線的位置。

## 易誤解之處
1. **IHIGH ≠ [[Critical power|CP]]。** CP 是「heavy↔severe」的下界（可穩態 vs 不可穩態）；IHIGH 高得多，是「severe↔extreme」的上界（達不達得到 VO2max）。兩者都在 CP 之上的高強度區，但管的事不同、位置不同。
2. **IHIGH 不是鋒利閾值。** 它上下的生理反應沒有突然翻轉（Iannetta 2022），是漸變帶。別把它想成像 CP 那樣的相變點。
3. **「達不到 VO2max」不代表有氧系統沒出力或變弱。** 是「時間不夠」——強度太高、力竭來得太快，VO2 還在往上爬就被打斷了，不是攝氧能力下降。

## 用生活例子再講一次
想像你要把一壺水煮到沸騰（VO2max）。爐火開得中等偏大時（severe 域），水要燒幾分鐘才滾，但你有足夠時間，水到得了沸點。如果你把火開到最大、但同時設定「只准燒很短一段就強制關火」（extreme 域，力竭太快），水溫雖然衝得很猛，卻在還沒滾之前就被關掉了。IHIGH 就是那個臨界火力：「在被強制關火之前，水還剛好來得及滾起來」的**最大**火力——再大一格，水就燒不到沸點了。

（失準之處：水的沸點是固定物理常數，而 VO2max 是個人的攝氧天花板、且還受當天狀態影響；「強制關火的時間」在身體裡不是外部設定，而是由 [[W prime|W′]] 與強度內生地決定的力竭。）

## 換句話說
換句話說，IHIGH 是「力竭前還來得及把攝氧量逼到最大值的最高強度」。它來自一場時間競賽：VO2 爬到頂要時間，而強度愈高你能撐的時間愈短——當「能撐的時間」短到追不上「VO2 爬頂的時間」，就跨過了 IHIGH，進入 VO2 永遠到不了頂的 [[Extreme intensity domain|extreme 域]]。它是 severe 與 extreme 的分界，但不是一條鋒利的線，而是一段漸變帶。

## 來源
- [[source-Ventura-2023-severe-extreme-tolerance]]（IHIGH 作為 severe/extreme 邊界的操作定義（Turnes 2016 逼近法、VO2max−1SD 判準）；IHIGH 達 VO2max、IHIGH+5% 無人達 VO2max 的直接數據；引 Iannetta 2022「IHIGH 非鋒利閾值」。）
- [[source-Jones-2010-CP-implications]]（§4 後的「severe 帶」定位：Historical Bases 節判定「CP 在 VO2max 之上（Wilkie）vs CP=AT（Moritani）」之爭——CP 不超過 VO2max 對應功率，但剛過 CP 經慢成分仍達 VO2max，故 CP 是「力竭時仍達 VO2max 的最低功率」、構成 severe 域下界；Poole et al. CP≈80% VO2max、CP+5% 即達 VO2max（Fig. 3–4）。）
