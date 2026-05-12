---
title: EDX 統計閾值與 False-Positive 控制
created: 2026-05-10
updated: 2026-05-10
type: concept
domain: [PMR, methodology, electrodiagnosis, statistics]
tags: [EDX, diagnostic_statistics, normal_values, cutoff, sensitivity, specificity, pre_test_probability, Bayes_theorem, likelihood_ratio, false_positive]
sources:
  - 10_來源摘要/Basic_Statistics_for_Electrodiagnostic_Studies.md
source_tier: 1
evidence_level: textbook_chapter
confidence: high
contested: true
contradictions:
  - Isolated borderline abnormality is not enough for diagnosis.
  - More EDX tests can increase false-positive risk if one abnormal value is treated as diagnostic.
---

# EDX 統計閾值與 False-Positive 控制

## One-Sentence Definition

EDX 統計閾值與 False-Positive 控制，是把 normal-value cutoff、sensitivity / specificity、pre-test probability、likelihood ratio 與 multiple-testing false-positive risk 納入判讀，避免把 borderline 或孤立 abnormality 誤寫成 disease。

## Definition and Boundary

- 本頁聚焦 EDX normal / abnormal 判讀的統計框架。
- 本頁不提供 CTS、UNE、radiculopathy、polyneuropathy 或任何單一疾病的完整 diagnostic criteria。
- 本頁只使用單一來源：[[../10_來源摘要/Basic_Statistics_for_Electrodiagnostic_Studies]]。
- Technical artifact、protocol error 與 anomalous innervation 另見 [[EDX_技術假象與品質控制]]、[[EDX_異常神經支配變異判讀]]。

## Why It Matters

- EDX 的 "abnormal" 不是疾病存在的絕對證明，而是基於 cutoff 與 pre-test probability 的機率判斷。
- Borderline abnormality 在臨床高度懷疑時可能有意義；在低 pre-test probability 時則很可能是 false positive。
- 多做很多檢查不一定提高確定性；若「任一 abnormal value」就診斷，cumulative false-positive rate 會快速升高。
- Type I error 會把正常病人貼上 abnormal label，可能導致不必要檢查、治療或轉介。

## Preconditions or Conditions

- 判讀前必須先有明確 referral question 與 differential diagnosis，才能估計 pre-test probability。
- Cutoff 應連回 normal distribution、standard deviation、one-tail / two-tail logic 與 lab reference population。
- Borderline abnormality 必須和 symptom distribution、exam、technical validity、protocol completeness 與其他 EDX findings 對齊。
- 若使用多個 NCS comparison studies，應避免只因單一 abnormal value 就下診斷。

## Mechanism

```text
Biologic normal variation
→ normal and disease distributions overlap
→ cutoff creates sensitivity / specificity tradeoff
→ pre-test probability modifies positive predictive value
→ likelihood ratio determines how much a test changes diagnostic probability
→ multiple tests inflate false-positive risk if one abnormality is sufficient
→ diagnosis requires clinical fit, sufficient abnormal magnitude, and convergent evidence
```

## Observable Patterns

- Many biologic measures can be modeled as normal distributions.
- In a normal distribution, about 68% of observations fall within 1 SD, about 95% within 2 SDs, and about 99.7% within 3 SDs.
- EDX values often use only one abnormal tail; 2 SD one-tail logic includes about 97.5% of the normal population, and 2.5 SD includes about 99.4%.
- EDX cutoff values are often set at 2 or 2.5 SDs above or below the mean.
- Lower cutoff increases sensitivity but decreases specificity.
- Higher cutoff increases specificity but decreases sensitivity.
- Type I error = false positive diagnosis; type II error = false negative diagnosis.
- The source states specificity should generally take precedence over sensitivity unless a test is used only as screening.
- ROC curve helps identify the tradeoff point between sensitivity and specificity.
- In the source's digit 4 CTS comparison example, cutoff >=0.4 ms gives specificity >97% and sensitivity about 70%; 0.1 ms gives sensitivity about 90% but specificity about 60%.
- EDX can never completely rule in or rule out a condition because false positives and false negatives are unavoidable.
- With the same 95% sensitivity / 95% specificity test, high prevalence disease population can yield high positive predictive value, while low prevalence disease population can yield mostly false positives.
- In the source's examples, 80% prevalence gives positive predictive value 98.7%, while 1% prevalence gives positive predictive value 16.1%.
- A minimally positive EDX value has significance only when clinical likelihood is high.
- A markedly abnormal EDX value is more likely true positive, even when clinical likelihood is lower.
- Positive likelihood ratio = sensitivity / (1 - specificity).
- In the Fagan nomogram example, LR 10 moves 50% pre-test probability to about 93%; LR 3 moves it to about 72%.
- Ten independent tests with 2.5% false-positive rate each can produce cumulative false-positive rate above 20% / almost 25% if one abnormal value is enough for diagnosis.
- Requiring two or more abnormal tests can reduce cumulative false-positive risk to an acceptable level in the source's example.

## Clinical / Research Implication

- EDX report should distinguish borderline abnormality from clearly abnormal physiology.
- A positive EDX finding should be interpreted as post-test probability conditioned on clinical likelihood, not as a free-standing diagnosis.
- When pre-test probability is low, a borderline positive result should usually be labeled clinically uncertain or likely false positive unless there is additional convergent evidence.
- When multiple comparison studies are done, diagnosis should rely on a coherent pattern rather than one isolated abnormal value.
- For screening-style EDX use, positive results need confirmation by a more specific test or a stronger overall pattern.

## Fact

- Normal and disease populations overlap in biologic measurements.
- Cutoff selection produces a sensitivity / specificity tradeoff.
- Type I errors are false positives; type II errors are false negatives.
- Bayes theorem links positive predictive value to sensitivity, specificity, and disease prevalence / pre-test probability.
- Positive likelihood ratio is calculated from sensitivity and specificity.
- Multiple testing increases cumulative false-positive risk when one abnormal test is sufficient.

## Inference

- Referral quality is part of statistical validity: a vague referral lowers pre-test probability and increases the chance that a positive result is misleading.
- "No electrodiagnostic evidence of" is usually more accurate than "ruled out" because EDX cannot fully exclude a condition.
- The more tests are added without a clear hypothesis, the more the report should protect against isolated false positives.

## Assumption

- The clinician can estimate pre-test probability from history, examination, and differential diagnosis.
- The normal-value reference population and lab method are comparable to the tested patient.
- Tests are sufficiently independent for cumulative false-positive logic to be relevant; if not independent, the exact number changes but the caution remains.

## Uncertainty

- The source does not provide disease-specific diagnostic thresholds for all EDX diagnoses.
- Pre-test probability is not directly measured and may vary by examiner.
- Borderline values may be meaningful when multiple clinical and electrophysiologic findings converge, but unsafe when isolated.

## Limitations and Misreadings

- 誤讀：「EDX abnormal 就是 disease。」正確是 abnormal value 只改變 post-test probability。
- 誤讀：「EDX 可以完全 rule in / rule out。」正確是 false positives 與 false negatives 不可完全消除。
- 誤讀：「Borderline abnormal 在任何情境都一樣。」正確是 pre-test probability 會大幅改變 positive predictive value。
- 誤讀：「多做幾個 tests 一定更準。」正確是若任一 abnormal 即診斷，cumulative false-positive risk 會快速增加。
- 誤讀：「Sensitivity 越高越好。」正確是除非作為 screening，EDX 通常要優先避免低 specificity 造成 type I error。

## Links

- [[電生理診斷醫學]]
- [[EDX_轉介問題設計]]
- [[EDX_定位導向檢查流程]]
- [[NCS_軸突損失與脫髓鞘判讀]]
- [[EDX_技術假象與品質控制]]
- [[EDX_異常神經支配變異判讀]]
- [[NCV_EMG_周邊神經病變總覽]]
- [[../10_來源摘要/Basic_Statistics_for_Electrodiagnostic_Studies]]
