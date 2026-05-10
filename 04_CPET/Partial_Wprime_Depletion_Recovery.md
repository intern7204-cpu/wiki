---
title: Partial W' Depletion Recovery
created: 2026-05-06
updated: 2026-05-06
type: concept
domain: [CPET, exercise_physiology, performance_modeling]
tags: [W_prime, partial_depletion, recovery, W_BAL, critical_power, interval_exercise]
sources:
  - 10_來源摘要/Lievens_2024_partial_Wprime_recovery.md
source_tier: 3
evidence_level: limited
confidence: medium
contested: true
contradictions:
  - Full-exhaustion W' recovery kinetics should not be assumed to describe partial-depletion recovery.
  - Fixed universal tau is too coarse even when biexponential modeling is not clearly favored.
---

# Partial W' Depletion Recovery

## One-Sentence Definition

Partial W' depletion recovery 是 W' 尚未耗盡時，後續 work capacity above CP 在 recovery interval 中恢復的動力學；它不能直接等同於 full exhaustion 後的 W' reconstitution。

## Definition and Boundary

本頁只處理 partial W' depletion 後的 W' recovery modeling，核心來源是 Lievens et al. 2024。

邊界：

- 不討論完整 [[Wprime_Recovery]] 的多來源共識。
- 不把 [[Wprime_Balance_Model]] 當作直接量測真值。
- 不把 full exhaustion 後的 two-phase recovery 自動套到 partial depletion。

## Why It Matters

多數 cycling interval、road race、track cycling 與 repeated severe-domain efforts 不會每次都把 W' 用到 0；若模型只根據 full exhaustion 估 recovery，就可能錯估下一段 high-intensity work 的可用容量。

## Preconditions or Conditions

Lievens 2024 的條件如下：

- 9 位 healthy young men。
- 以 ramp test 和 3-5 次 constant-load trials 估算 CP/W'。
- WB1 在 P4 做 1 或 3 分鐘，對應理論上的 25% 或 75% W' depletion。
- Recovery duration：30、60、120、300、600 秒。
- Recovery intensity：90% GET。
- WB2 做到 exhaustion，換算 W'OBS。

## Mechanism

### Definition

在 CP/W' model 中，>CP work 會消耗 W'；<CP recovery 期間，W' 可部分恢復。Partial depletion 情境的問題是：W' 沒有被耗盡時，recovery shape 是否仍和 full exhaustion 後一樣。

### Known Facts

- Lievens 2024 比較 monoexponential 與 biexponential models，並同時測試 free amplitude 和 fixed amplitude。
- Biexponential model 的 RMSE 較低，但 AICc 在 free amplitude 條件下 favor monoexponential。
- Fixed amplitude 條件下，DEP25% favor monoexponential，DEP75% favor biexponential。
- Monoexponential tau 為 DEP25% 約 32 s、DEP75% 約 82 s，但 tau 與 amplitude 互相影響，不能只看 tau 判斷哪個 recovery 較快。
- Initial 30 s recovery 在 DEP25% 與 DEP75% 相近，約 +21% vs +23%。

### Preconditions

- W' depletion 是 model-derived estimate，不是直接生理量測。
- Recovery power 固定在 90% GET，因此結論最適合外推到類似 active recovery 條件。

### Mechanism Chain

1. WB1 造成 partial W' depletion。
2. Recovery interval 讓 oxidative contribution、PCr-related recovery、acid-base status 和 neuromuscular state 部分恢復。
3. WB2 performance 反映「此刻可用的 work capacity above CP」，即 W'OBS。
4. 若 WB2 的 aerobic contribution 因 priming effect 增加，W'OBS 可超過理論 100%。
5. 若 prior depletion 較大，metabolic milieu distortion 可能延續，使 W'OBS plateau 低於完整恢復。

### Observable Consequence

- DEP25% 後，既有 models 可能低估 W'OBS，且 W'OBS 可能超過理論 100%。
- DEP75% 後，W'OBS model fit 可 plateau 在約 83%，提示 large depletion 後可能未完全恢復。
- W'OBS 與 VO2peak、CP、GET 呈正相關；recoverer 快的人在不同 depletion 條件下也傾向一致。

### Clinical or Research Implication

Interval prescription 不應只寫「work bout 強度與時間」；至少要同時寫：

- work power
- work duration
- recovery power
- recovery duration
- expected depletion state
- 是否允許 fatigue carryover

## Observable Patterns

- `W'OBS` 在 DEP25% 與 DEP75% 間高度相關（r = 0.92）。
- `W'OBS` 與 VO2peak、CP、GET 呈正相關（r = 0.67-0.77）。
- Perceived W' recovery 平均比 W'OBS 低約 25%，表示 subjective fatigue 與 model-derived work capacity recovery 可能脫鉤。

## Clinical / Research Implication

### 對 CPET / performance modeling

- Model family selection 應同時看 fit error 與 complexity penalty。
- Fixed tau 不應被當作跨 depletion level 的通用常數。
- Future models 應納入 dynamic tau、depletion state、recovery intensity 與 aerobic fitness。

### 對 rehabilitation / clinical exercise

- 這篇不支持在臨床族群直接開 aggressive severe-domain intervals。
- 它支持的是更保守的解讀：若用 W'BAL 輔助運動處方，應把輸出視為 assumption-sensitive estimate。

## Fact

- 本來源為 n = 9 的 cycling physiology original article。
- Partial depletion 條件是理論 25% 與 75% W' depletion。
- Recovery durations 是 30、60、120、300、600 秒。
- Recovery power 設在 90% GET。
- Free amplitude models 的 AICc 不支持 biexponential 優於 monoexponential。
- Fixed amplitude models 中，DEP25% favor monoexponential，DEP75% favor biexponential。
- 既有 Skiba-1、Skiba-2、Bartram models 未能準確描述本研究 temporal W' recovery profile。

## Inference

- Partial depletion recovery 應被視為獨立 model problem。
- Exhaustion-derived two-phase recovery 是重要背景，但不應未經驗證直接套到 all intermittent efforts。
- Aerobic fitness 可能是 individualized W' recovery model 的必要 covariate。

## Assumption

- W' depletion 的 25% / 75% 是 CP/W' model 推估。
- WB2 to exhaustion 可代表 W'OBS。
- P4 work bout 和 90% GET recovery 足以形成 controlled comparison。

## Uncertainty

- 不知道 women、older adults、elite athletes、heart failure、COPD 或 rehabilitation populations 是否呈現相同 pattern。
- 不知道不同 recovery power 是否會改變 monoexponential vs biexponential 的相對優勢。
- 不知道 absence of true warm-up 對 W'OBS >100% 的影響程度。

## Limitations and Misreadings

- 誤讀 1：partial depletion 不支持 biexponential，所以 W' recovery 一定是 monoexponential。
  - 修正：本來源只表示目前資料不支持強行用 biexponential；同時也指出 fixed tau 不足。
- 誤讀 2：W'OBS 超過 100% 代表 CP/W' model 沒用。
  - 修正：作者將此解釋為 WB2 aerobic priming / relative aerobic contribution 增加造成的 operational estimate 現象。
- 誤讀 3：subjective recovery 低估 W'OBS，所以可以忽略 fatigue sensation。
  - 修正：perceived fatigue 與 metabolic acidosis recovery 可能較慢，臨床或訓練決策仍須保守。

## Links

- [[Wprime_Recovery]]
- [[Exhaustion_Based_Two_Phase_Wprime_Recovery]]
- [[Wprime_Balance_Model]]
- [[CP_Wprime_Interval_Design]]
- [[Critical_Power]]
- [[Gas_Exchange_Threshold]]
- [[../10_來源摘要/Lievens_2024_partial_Wprime_recovery]]
