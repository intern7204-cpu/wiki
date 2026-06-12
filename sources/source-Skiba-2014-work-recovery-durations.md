---
type: source
tags: [exercise-physiology, critical-power, W-prime, intermittent, W-prime-balance-model]
created: 2026-06-11
---

# 來源：Effect of Work and Recovery Durations on W′ Reconstitution during Intermittent Exercise

## 出處
- **作者**：Philip F. Skiba, Sarah Jackman, David Clarke, Anni Vanhatalo, Andrew M. Jones
- **期刊**：*Medicine & Science in Sports & Exercise*（MSSE）, Vol. 46, No. 7, pp. 1433–1440, 2014
- **DOI**：10.1249/MSS.0000000000000226
- **機構**：University of Exeter（Sport and Health Sciences）；Simon Fraser University
- **原始檔**：`C:\原始資料\Effect of Work and Recovery Durations on W' Reconstitution during Intermittent Exercise\`（含正文 .md 與 5 張圖：Fig 1 實驗設計、Fig 2 各條件 τ_W′、Fig 3 W′ACT 低估長條、Fig 4 VO2 形態 A–D、Fig 5 D_VO2↔W′ 散點）

## 核心主張
W′ 平衡模型（Skiba 2012 的積分型 W′BAL·INT）在多種間歇工作/恢復時長下大致穩健，但會**系統性地低估**實際可用的 W′——而且低估程度取決於**工作段與恢復段的時長**（不只取決於累積的功或工作:恢復比）：工作段愈短、恢復段愈短（在足夠短的工作段之下），實測回填都比模型預測得多。

## 本份新增／更新的概念
- [[W prime multicompartment model]]（**新增**）——本份在 Discussion 提出（援引 Skiba 2012）：把 W′ 想成數個隔間（觀念上≈Type I/II 纖維群），各有獨立貢獻與不同回填 τ，恢復較快的隔間在間歇中扛較多工作，藉以解釋「累積功相同、切段方式不同卻補回不同」。
- [[W prime reconstitution]]（**更新**）——新增推導點：工作時長與恢復時長**各自**獨立影響回填速度（τ_W′）；縮短工作段（60→40→20 s）使回填快於預測、縮短恢復段（30→20→10 s）亦然；60–30 vs 20–10 同比值同平均功率卻 W′ACT 不同→「不只累積功，時間結構也算數」。新增易誤解條目與來源。
- [[W prime balance model]]（**更新**）——Skiba 2014 是 W′BAL·INT 的實證檢驗：跨六條件平均低估 W′ 約 1.6 kJ、低估 T_lim 約 27 s；60–30 條件 τ_W′＝403 s 與 Skiba 2012 的 377 s 吻合；個體差異大（subject 9 的 τ_W′ 比 eq.3 漸近線快逾 200 s）→ 呼籲「個人化」預測函式。新增來源。
- [[Intermittent exercise critical power model]]（**更新**）——四個「獨立」參數中，工作時長與恢復時長被證實各自影響回填，且模型低估；以多隔間模型詮釋。新增來源。
- [[Priming effect]]（**更新**）——間歇嚴重強度運動本身可作為 priming 刺激：降低 CWR 前的 VO2start、可能抬高表觀 W′ 或 CP；工作:恢復比愈低（平均功率落在重度域）priming 效果愈好。新增來源。
- [[VO2 slow component]]（**更新**）——D_VO2（VO2peak−VO2start）與 CWR 可用 W′ 線性相關（r=0.79, r²=0.63）；VO2start 愈低＝W′ 儲備愈多；把既有「VO2SC 振幅↔W′」關係延伸到間歇情境的「起始 VO2↔可用 W′」。新增來源。

## 與既有知識的關係
- **一致、補充、無矛盾。** 完成 index.md「pending follow-up」開放張力②點名的「工作時長 vs 恢復時長對回填的個別貢獻」——本份把兩者分開操作（固定工作強度，分別變動工作時長與恢復時長），確證**時長結構**（非僅累積功）影響回填；但**工作強度 vs 工作時長**的個別貢獻仍未分離（本份工作強度固定 P_EXP，未變動），該子問題仍開放。
- 與 [[source-Caen-2019-work-recovery-reconstitution|Caen 2019]] 同向且互補：Caen 從「消耗速率↔回填速率耦合」切入工作端，本份從「工作/恢復時長」切入；兩者都指出 [[W prime balance model|Skiba W′BAL]] 只認恢復端 D_CP 會系統性低估。
- 與 [[source-Lievens-2024-partial-depletion|Lievens 2024]]、[[source-Black-2023-dynamic-power-duration|Black 2023]] 一致：固定-τ 的 W′BAL·INT 有系統偏差，出路是「可變、個人化 τ」（subject 9 的個體證據）。
- **命名/版本注意**：本份是 **Skiba 2014**（MSSE 46(7)，間歇工作/恢復時長的實證檢驗），檢驗的是 **Skiba 2012**（MSSE 44(8)，W′BAL·INT 積分模型）這條式子；與 [[W prime balance model]] 提到的「Caen 2021 雙指數」「Skiba 2015 微分（ODE）」皆非同篇。本份已被 wiki 多頁前向引用（[[Intermittent exercise critical power model]]、[[W prime balance model]] 既有「Skiba 2014 用實地資料驗證」），本次補上其來源頁與細節。

## 看圖
- **Fig 1**（實驗設計示意：A 間歇消耗約 50% W′BAL → B 緊接定功率 CWR 至力竭；點線為 W′BAL）——已檢視，確認「比的是 B 開始那一刻模型預測的 W′BAL vs B 實測 W′ACT」。
- **Fig 2**（六條件 τ_W′ 長條）——已檢視：60–30 最高（≈403 s）、往 20–20／20–10 下降到最低（≈210–235 s）、20–5 又回升（≈337 s）；呈現「20–20 附近可能存在回填最快的最佳點」。
- **Fig 3**（W′INT 低估長條，星號為達顯著）——已檢視：20–10、20–20、20–30 三格低估達顯著（約 −2 至 −2.8 kJ），60–30、20–5 接近 0。
- **Fig 4 A–D**（VO2 形態，群體均值）——已檢視：工作段縮短（A）使間歇 VO2 由鋸齒轉為緩升曲線、恢復段縮短（C）使 VO2start 升高；右側 CWR（B/D）以 VO2start=0 對齊，變動恢復條件（D）差異明顯（20–30 起點低、爬升空間大）。
- **Fig 5**（D_VO2 vs W′Observed 散點，r²=0.63）——已檢視：正相關但有單一離群點可能槓桿過大（作者自陳）。

（圖 4 的 sawtooth→緩升轉變、Fig 5 的離群點提醒，已分別寫入 [[VO2 slow component]] 與本頁的限制描述。）
