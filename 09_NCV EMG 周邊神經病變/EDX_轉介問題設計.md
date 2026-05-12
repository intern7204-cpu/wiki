---
title: EDX 轉介問題設計
created: 2026-05-01
updated: 2026-05-09
type: concept
domain: [PMR, electrodiagnosis, methodology]
tags: [EDX, EMG, NCS, referral_question, diagnostic_reasoning, pre_test_probability, false_positive]
sources:
  - 10_來源摘要/Approach_NCS_EMG_Neuromuscular_Ultrasound.md
  - 10_來源摘要/Basic_Statistics_for_Electrodiagnostic_Studies.md
  - 10_來源摘要/Electrodiagnostic_medicine.md
source_tier: 1
evidence_level: consensus
confidence: high
contested: false
contradictions: []
---

# EDX 轉介問題設計

## 一句話定義

高品質 EDX 不是先做檢查再想問題，而是先用 symptom distribution、weakness、sensory loss 與 reflex pattern，寫出能提高 pre-test probability 並改變 management 的 referral question。

## Definition and Boundary

- 這個 concept 指的是 electrodiagnostic study 的前測臨床問題設計。
- 它不是「rule out everything」式的模糊轉介。
- 本頁加入統計邊界：referral question 會決定 pre-test probability，進而改變 positive test 是否可能是真陽性。

## Fact

- 本章把 EDX 定義為 history + focused physical examination 的神經生理延伸。
- clinical framework 應先由 symptom distribution、weakness / sensory loss / reflex pattern 建立，再決定 NCS / needle EMG 的內容。
- 來源章節明確把 EDX encounter 排成：brief history / directed examination → differential diagnosis → study plan → patient explanation → NCS → needle EMG，且檢查中需依結果即時修正。
- EDX 的 principal goal 是 localization，而不是蒐集越多數值越好。
- EDX 的目的包括 narrow differential、確認 severity / prognosis、排除 mimic 與改變 management。
- report 至少應交代 referral question、focused history / exam、tabulated data、normative values 與 limitations。
- Bayes theorem 下，positive EDX 的 true-positive probability 取決於 sensitivity、specificity 與 pre-test probability。
- Borderline abnormal test value 只有在 clinical likelihood 高時才比較有意義；若 symptoms / signs 不支持該診斷，borderline abnormality 可能是 false positive。
- 若多個 tests 中任一 abnormal value 就下診斷，cumulative false-positive rate 會升高。

## Mechanism Chain

```text
Focused bedside question
→ higher pre-test probability for a specific differential
→ targeted NCS / needle EMG design
→ physiologic localization and post-test probability update
→ management-relevant interpretation
```

## Inference

- referral question 若太含糊，得到的往往只是很多數值，而不是可用的臨床結論；統計上也會提高 clinically irrelevant positive findings 的比例。

## Assumption

- 檢查室能提供完整 needle EMG、normative standard 與適當報告格式。

## Uncertainty

- 即使問題設計良好，sensitivity / specificity 仍會受 disease timing、background polyneuropathy、cutoff selection 與 multiple testing 影響。

## Clinical Use

- 下單前可先問：這個 EDX 要回答哪一個 differential、severity 或 prognosis 問題？
- 若只是低 pre-test probability 的 broad screening，borderline positive result 需預設有高 false-positive 風險。

## Links

- [[電生理診斷醫學]]
- [[EDX_定位導向檢查流程]]
- [[EDX_統計閾值與False_Positive控制]]
- [[../10_來源摘要/Approach_NCS_EMG_Neuromuscular_Ultrasound]]
- [[../10_來源摘要/Basic_Statistics_for_Electrodiagnostic_Studies]]
- [[../10_來源摘要/Electrodiagnostic_medicine]]
