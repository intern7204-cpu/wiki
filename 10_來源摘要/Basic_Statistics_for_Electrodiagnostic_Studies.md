---
title: Basic Statistics for Electrodiagnostic Studies
created: 2026-05-10
updated: 2026-05-11
type: source_summary
domain: [PMR, methodology, electrodiagnosis, statistics]
tags: [EDX, NCS, diagnostic_statistics, normal_values, cutoff, sensitivity, specificity, Bayes_theorem, likelihood_ratio, false_positive, textbook]
source_path: 'C:\原始資料\Basic Statistics for Electrodiagnostic Studies\Basic Statistics for Electrodiagnostic Studies.md'
source_tier: 1
evidence_level: textbook_chapter
confidence: high
contested: true
contradictions:
  - EDX 不能完全 rule in 或 rule out 某個診斷。
  - Borderline 的 EDX abnormality 在 pre-test probability 不支持時不具臨床意義。
  - 多項檢查若以「任一 abnormal 即診斷」會放大累積 false-positive rate。
---

# Source Summary: Basic Statistics for Electrodiagnostic Studies

## Source Type

- 電生理診斷 textbook chapter；內容說明判讀 EDX 所需的基本統計學。
- 本輪僅以這篇單一來源 ingest，未混入 disease-specific 的 CTS / UNE criteria、NCS protocol chapters 或外部診斷準確度研究。

## Reliability Level

- 在本 wiki 對 EDX textbook chapter 的層級中屬 Tier 1。
- 強項：EDX 中常用的統計推理 — normal distribution、cutoff 選擇、sensitivity / specificity 取捨、type I / II error、Bayes theorem、likelihood ratio，以及多重檢查所造成的累積 false-positive risk。
- 限制：本章舉例使用 median neuropathy at the wrist，但主要訴求是統計邏輯，不是完整的 CTS 診斷指引。

## One-Sentence Summary

EDX 的「abnormality」是機率性陳述，而非二元事實：cutoff 選擇、pre-test probability、likelihood ratio、abnormal 值的偏離程度，以及檢查項目數量，共同決定一個陽性結果是真陽性還是 false positive。

## Core Concepts Extracted

### Concept: EDX 統計閾值與 False-Positive 控制

#### One-Sentence Definition

EDX diagnostic statistics 是用 normal-value 分布、cutoff 選擇、sensitivity / specificity、pre-test probability、likelihood ratio 與多重檢查校正邏輯，避免 borderline 或 isolated abnormality 被當成疾病的判讀工具。

#### Known Facts

- EDX 判讀常需在檢查當下做 normal / abnormal 決定，因為後續 nerve / muscle 的選擇會被前面的結果影響。
- 正常人在生理變項上有變異；許多生理測值可用 normal distribution 近似。
- 在 normal distribution 中，約 68% 的觀察值落在 mean ±1 SD、約 95% 落在 ±2 SD、約 99.7% 落在 ±3 SD。
- EDX 測值常只關心一側 tail；對 one-tail cutoff 而言，超過 mean +2 SD 的觀察值約只佔 2.5%（即 cutoff 內含 97.5%），超過 +2.5 SD 約只佔 0.6%（即 cutoff 內含 99.4%）。
- 多數 EDX cutoff 設在 mean ±2 SD 或 ±2.5 SD。
- Specificity 是「沒有疾病但 test 陰性」的比例。
- Sensitivity 是「有疾病但 test 陽性」的比例。
- 正常與疾病分布通常 overlap，因此沒有 cutoff 能完全消除 false positive 與 false negative。
- 降低 cutoff 提升 sensitivity 但降低 specificity；提高 cutoff 提升 specificity 但降低 sensitivity。
- False positive 屬 type I error；false negative 屬 type II error。
- 來源指出在 EDX 中 type I error 通常較不可接受，因為把正常人標為 abnormal 會導致不必要的檢查與治療。
- 除非僅作 screening，否則 specificity 應優先於 sensitivity；任何 screening 陽性都應由更 specific 的 test 確認。
- ROC curve 顯示不同 cutoff 下 sensitivity 與 specificity 的取捨。
- 在 mild CTS 的 digit 4 sensory comparison 範例中：cutoff ≥ 0.4 ms 時 specificity > 97%，sensitivity 約 70%；把 cutoff 降到 0.1 ms 可提升 sensitivity 至約 90%，但 specificity 降到約 60%。
- 因為 normal 變異與 normal-disease overlap，EDX studies 必然會有少量 false-positive 與 false-negative。
- 來源明確指出 EDX 不能完全 "rule out" 或 "rule in" 任何 condition。
- 由 Bayes theorem，positive test 為真陽性的機率取決於 sensitivity、specificity 與 disease prevalence / pre-test probability。
- 來源範例：sensitivity 95%、specificity 95% 時，prevalence 80% 族群的 PPV 為 98.7%。
- 同樣 sensitivity / specificity 但 prevalence 1% 時，PPV 只有 16.1%；多數陽性都是 false positive。
- 在高 pre-test probability 的 CTS 樣態族群中，borderline 的 palmar median-ulnar difference 可有高 post-test probability；同樣的 borderline 值在低 pre-test probability 族群則 post-test probability 低很多。
- 來源指出 markedly abnormal test 不論臨床機率為何都較可能為真陽性；minimally positive test 只有在臨床機率高時才有意義。
- Positive likelihood ratio = sensitivity ÷ (1 − specificity)。
- 在 Fagan nomogram 範例中，pre-test probability 50% 時，LR 10 可使 post-test probability 約 93%；LR 3 只能到約 72%。
- 多項獨立檢查若以「任一 abnormal 即診斷」，累積 false-positive rate 會迅速升高。
- 若 10 項檢查每項 false-positive rate 為 2.5% 且任一 abnormal 即診斷，累積 false-positive rate 可達 20% 以上、近 25%。
- 若改成「至少兩項 abnormal 才診斷」，10 項檢查（同樣每項 2.5%）的累積 false-positive rate 可維持在 < 2.5%。

#### Mechanism Chain

```text
正常生理變異
→ normal 與 disease 分布 overlap
→ cutoff 選擇形成 sensitivity / specificity tradeoff
→ pre-test probability 改變 positive predictive value
→ borderline abnormality 在高 / 低 clinical likelihood 下意義不同
→ 多項檢查在「任一 abnormal 即診斷」下會放大 false positives
→ 診斷應結合臨床、足夠 abnormal 程度、並常需多個 supporting abnormality
```

#### Inferences

- EDX 報告中的「abnormal」應理解為 post-test probability 的陳述，而不是疾病存在本身。
- 模糊的 referral question 不會提升 pre-test probability，反而讓 false positive 機會升高、陽性結果的價值降低。
- 報告應降階 isolated、borderline、與臨床不一致的 abnormality，而不是硬塞成診斷。

#### Assumptions

- Cutoff 與 normative values 來自與病人、實驗室技術相容的族群。
- 對所用的測試，sensitivity 與 specificity 是已知或至少可估算。
- 臨床醫師可由症狀、徵象與 differential 估算 pre-test probability。

#### Uncertainties / Limitations

- 本章傳達統計原理，而非疾病特異的診斷準確度。
- EDX 多項檢查彼此並不完全獨立，實際累積 false-positive rate 會偏離理論值。
- Pre-test probability 的估計屬於臨床判斷，無法精確。

## Clinically Useful Points

- 不要在臨床表現不符合的情況下，僅憑單一 borderline EDX abnormality 下診斷。
- 臨床機率低時，borderline 陽性 EDX 結果較可能是 false positive。
- 臨床機率高時，minimally positive 的 EDX 結果可能有意義，但仍需與整體 pattern 一起判讀。
- 進行多項檢查時，應要求多個 convergent abnormality，而不是接受任何一項 abnormal 即診斷。
- 當 false diagnosis 會帶來不必要的治療或 referral 時，應優先採用高 specificity 的 cutoff。

## Research-Useful Points

- EDX 診斷準確度研究應報告 sensitivity、specificity、cutoff 選擇邏輯，以及採用 one-tail 或 two-tail。
- 使用大量參數的研究應說明如何處理 multiple testing 與累積 false-positive risk。
- 報告「borderline vs markedly abnormal」往往比僵硬的二元 normal / abnormal 標籤更有資訊量。

## Conflicts With Existing Knowledge

- 與「EDX 可以完全 rule in 或 rule out 一個診斷」衝突。
- 與「任何 abnormal 值就等於診斷」衝突。
- 與「borderline abnormal 在高 / 低 pre-test probability 下意義相同」衝突。
- 與「檢查越多越能增加診斷確定性」衝突。
- 與「sensitivity 越高越好」衝突。

## Pages That Should Be Created or Updated

- Created: [[../09_NCV EMG 周邊神經病變/EDX_統計閾值與False_Positive控制]]
- Updated: [[../09_NCV EMG 周邊神經病變/NCV_EMG_周邊神經病變總覽]]
- Updated: [[../09_NCV EMG 周邊神經病變/電生理診斷醫學]]
- Updated: [[../09_NCV EMG 周邊神經病變/EDX_轉介問題設計]]
- Updated: [[../09_NCV EMG 周邊神經病變/EDX_定位導向檢查流程]]
- Updated: [[../09_NCV EMG 周邊神經病變/NCS_軸突損失與脫髓鞘判讀]]

## Suggested Tags

#EDX #diagnostic_statistics #normal_values #cutoff #sensitivity #specificity #Bayes_theorem #likelihood_ratio #false_positive
