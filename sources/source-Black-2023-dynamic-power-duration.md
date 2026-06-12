---
type: source
tags: [exercise-physiology, critical-power, W-prime, modelling, 3MT]
created: 2026-06-11
---

# 來源：Accounting for Dynamic Changes in the Power–Duration Relationship Improves the Accuracy of W′ Balance Modeling

## 出處
- 檔名：`Accounting for Dynamic Changes in the Power–Duration Relationship Improves the Accuracy of W'\Accounting for Dynamic Changes in the Power–Duration Relationship Improves the Accuracy of W'.md`
- 作者：Matthew I. Black, Philip F. Skiba, Lee J. Wylie, James Lewis, Andrew M. Jones, Anni Vanhatalo（University of Exeter；Skiba 另屬 Advocate Lutheran General Hospital）
- 出處：*Medicine & Science in Sports & Exercise*, 2023, 55(2):235–244. DOI: 10.1249/MSS.0000000000003039
- 類型：原始研究（12 筆實驗室資料庫資料的二次分析；重複 3MT 設計）

## 核心主張
功率–持續時間關係**不是固定的**：一段把 W′ 全力榨乾的運動之後，CP（以 3MT 的 EP 代表）降約 7%、W′（以 WEP 代表）降約 61%；既有 W′BAL 模型假設 CP 恆定，因而在大量消耗 W′ 的情境會誤估 W′ 回填（W′BAL·ODE 與 W′BAL·MORTON 高估，W′BAL·INT 最準），而把 CP/W′ 的下降納入模型可改善 ODE 與 Morton 的準度。

## 本份新增／更新的概念
- [[Power-duration relationship plasticity]]（新增）— 本份的旗艦概念：CP/W′ 在先前力竭運動後左下漂移、機制（PCr/Pi/pH、Type II 全面招募與慢恢復、Ferguson 對照、Clark 2019 糖原路線）、durability、對 W′BAL 模型的後果與 adjusted 修正。
- [[W prime balance model]]（更新）— 明確區分三個 W′BAL 變體：W′BAL·MORTON（線性，eq.1）、W′BAL·INT（卷積積分，Skiba 2012，eq.2–4，含 τ_W′＝546·e^(−0.01·D_CP)+316）、W′BAL·ODE（雙條件微分，Skiba 2015，eq.5）；補上「adjusted W′BAL（把疲勞態 EP/WEP 代回）」與三者在全力榨乾後的準度排名（INT≈實測；ODE/Morton 高估；adjusted 改善 ODE/Morton 但 INT 不變）。
- [[3-minute all-out test]]（更新）— 補上 EP（末 30 秒平均功率≈CP）與 WEP（高出 EP 之功≈W′）的正式術語；以及重複 3MT（C-3MT vs F-3MT）發現疲勞態 EP、WEP、TWD 皆下降。
- [[W prime reconstitution]]（更新）— 補上「全力（all-out）、完全榨乾、最快速率」情境下的回填：60 秒只回約 39%；ODE/Morton 高估、INT 最準；all-out 因 Type II 全面即刻招募且 Type II 恢復慢，使回填較 CWR 慢。
- [[Critical power]]（更新）— 補上 CP 的可塑性／durability：CP 非恆定，先前全力運動後降約 7%、長時間重度運動後降約 9%（Clark），但短時嚴重 CWR 力竭後不降（Ferguson）；「CP 恆定」是 W′BAL 模型的關鍵但會被違反的假設。

## 與既有知識的關係
- **補充並修正**：先前 wiki 把 CP/W′ 當成個人固定參數（[[Critical power]]、[[W prime]]）。本份不推翻 CP 的預測價值，但加上一層重要限制——CP/W′ 會隨先前運動疲勞而漂移；這正面回應了 index.md「pending follow-up」裡點名的開放張力①「反覆力竭疲勞效應併入動態 W′ 模型尚無模型正式納入」。
- **與 [[W prime balance model]] 一致並深化**：呼應該頁既有的「固定-τ 模型會系統性誤差、應走可變/個人化 τ」（Caen 2019、Lievens 2024）。本份提供另一條獨立的誤差來源——不是 τ 不對，而是**連 CP 本身都漂了**；解法之一是 adjusted 模型。Skiba 同時是本文與 W′BAL 模型原作者，立場一致。
- **與 [[W prime reconstitution]] 一致**：本份的「all-out 後回填被 ODE/Morton 高估」與該頁「消耗速率↔回填速率耦合（Caen 2019）」「重複力竭使回填變慢」方向相符，補上「最快速率、完全榨乾」這個極端點。
- **方法學注意**：本份刻意採用「已發表的通用 τ」而非個人化 τ（為貼近實務工具的便利性），且坦言此為限制；與 [[W prime balance model]] 易誤解 #3「群體 τ ≠ 個人 τ」一致。作者亦明確反對沿用通用 τ。
