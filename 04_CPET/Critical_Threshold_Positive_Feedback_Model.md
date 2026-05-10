---
title: Critical Threshold and Positive Feedback Model
created: 2026-05-08
updated: 2026-05-08
type: concept
domain: [CPET, exercise_physiology]
tags: [VO2_kinetics, critical_power, O2_deficit, inorganic_phosphate, muscle_fatigue, work_efficiency, VO2_slow_component, W_prime]
sources:
  - 10_來源摘要/Goulding_2021_VO2_kinetics_exercise_tolerance.md
source_tier: 4
evidence_level: high_quality_mechanistic_review_hypothesis
confidence: medium_high
contested: true
contradictions:
  - The model explains CP / W' mechanistically but is not a clinical threshold rule.
  - Pi is a plausible representative metabolite, not a proven single causal switch in whole-body exercise.
  - Whole-body CP may behave like a boundary layer or phase transition rather than a mathematically sharp threshold.
---

# Critical Threshold and Positive Feedback Model

## One-Sentence Definition

The critical threshold and positive feedback model explains supra-CP exercise intolerance as a metabolite-fatigue-inefficiency loop triggered when O2-deficit-related intramuscular disturbance exceeds a critical range.

## Definition and Boundary

本頁只處理 Goulding et al. 2021 的單一概念：`tauV̇O2` 如何透過 O2 deficit 與 metabolite accumulation 連到 `CP`、V̇O2 slow component 與 `W'`。

本頁不等於：

- CP 測試 protocol
- W'BAL computational model
- V̇O2 kinetics fitting workflow
- clinical CPET guideline
- disease-specific exercise prescription

## Why It Matters

這個模型把三個常被分開看的現象接起來：

- `tauV̇O2`：氧化代謝追上 ATP demand 的速度。
- `CP`：metabolic stability 能否維持的上限。
- `W'` / V̇O2SC：超過穩定邊界後，fatigue 與 inefficiency 如何推進到 intolerance。

因此它提醒：運動耐受度不是只由 V̇O2max 或 AT 決定；transition speed 也會決定同一 work rate 下的 intracellular stress。

## Preconditions or Conditions

適用前提：

- exercise transition 有明確 ATP demand increase
- 可合理討論 V̇O2 kinetics 與 O2 deficit
- 強度接近或高於 metabolic stability boundary
- 解讀重點是 mechanism，而不是直接診斷 cut-off

不適用前提：

- 把 `Pi` 當作 routine clinical biomarker
- 把 `CP` 當成單一固定不變的 sharp threshold
- 用此模型直接開立 disease-specific rehabilitation prescription

## Mechanism

```text
external power demand
  -> ATP turnover demand rises
  -> V̇O2 response is finite and delayed
  -> O2 deficit
  -> PCr breakdown + glycolysis + O2 stores
  -> Pi / ADP / H+ / K+ accumulation and Ca2+ handling disturbance
  -> if below critical range: metabolic stability
  -> if above critical range: fatigue
  -> reduced work efficiency
  -> more ATP needed for the same external power
  -> more metabolite accumulation
  -> V̇O2 slow component and finite exercise tolerance
```

## Observable Patterns

- Faster `tauV̇O2`: smaller O2 deficit at a given transition, less metabolite accumulation, better metabolic stability.
- Slower `tauV̇O2`: larger O2 deficit, faster approach toward fatigue-related metabolite thresholds.
- Below `CP`: V̇O2, PCr, Pi, pH, and lactate can stabilize.
- Above `CP`: V̇O2SC develops, metabolic disturbance progresses, and task failure occurs after finite time.
- Very short intermittent work:recovery bouts may keep metabolite accumulation below the critical range despite high external power.
- Interventions that change V̇O2SC rate / amplitude often also change supra-CP tolerance or `W'`, but simple V̇O2SC amplitude is not always a complete marker.

## Clinical / Research Implication

- For CPET reasoning, low exercise tolerance can arise from slow kinetics and high transition cost, not only low peak capacity.
- For rehabilitation, the model supports attention to pacing, interval duration, recovery duration, and priming, but it does not itself prescribe a protocol.
- For research, `tauV̇O2`, V̇O2SC, intramuscular energetics, fatigue, and `W'` should be interpreted as linked system outputs.

## Fact

- Goulding et al. 2021 is a high-quality mechanistic review / hypothesis article, not a guideline.
- The source states that `tauV̇O2` can vary widely, with examples from about 12 s in elite endurance athletes to about 120 s in elderly COPD patients.
- The source states that steady-state cycle ergometry V̇O2-power gain is typically about 9-11 mL/min/W.
- O2 deficit can be approximated as `Delta V̇O2 x tauV̇O2` only when a steady state is reached.
- The model uses `Pi` as a prime candidate metabolite because of known effects on cross-bridge function and Ca2+ handling.
- The source links V̇O2SC, muscle fatigue, loss of work efficiency, `CP`, and `W'` into one mechanistic model.

## Inference

- `CP` can be interpreted as the highest work rate at which the positive feedback loop does not propagate unstably.
- `W'` reflects finite tolerance above `CP`, not a simple anaerobic energy tank.
- Intermittent exercise may be tolerable above nominal `CP` if work bouts are short enough to prevent critical metabolite accumulation.

## Assumption

- Pulmonary V̇O2 kinetics are a usable proxy for muscle O2 utilization kinetics in many, but not all, settings.
- `Pi` represents a broader fatigue-related metabolite state.
- In silico models can generate useful mechanistic hypotheses for human whole-body exercise.

## Uncertainty

- The critical threshold is not directly measured in routine clinical testing.
- The exact contribution of `Pi`, ADP, H+, K+, Ca2+ handling, fiber recruitment, and afferent feedback remains unresolved.
- Whole-body exercise likely has a transition zone rather than a single sharp point.
- The source explicitly calls for future in vivo experiments.

## Limitations and Misreadings

- Misreading: this model proves a single Pi cutoff for clinical CPET.
- Correction: `Pi` is a plausible mechanistic candidate, not a clinical cut-off.
- Misreading: faster V̇O2 kinetics are always beneficial without tradeoff.
- Correction: O2 deficit is also part of normal ATP homeostasis and buffering.
- Misreading: `W'` is simply anaerobic capacity.
- Correction: `W'` depends on the propagation of fatigue, inefficiency, and limiting systemic / neuromuscular conditions.

## Links

- [[VO2_Kinetics]]
- [[VO2_Slow_Component]]
- [[Critical_Power]]
- [[Wprime_Balance_Model]]
- [[Exercise_Intensity_Domains]]
- [[../10_來源摘要/Goulding_2021_VO2_kinetics_exercise_tolerance]]
