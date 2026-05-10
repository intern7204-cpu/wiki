---
title: Priming Exercise and V̇O2 Kinetics
created: 2026-05-08
updated: 2026-05-08
type: concept
domain: [CPET, exercise_physiology, performance_modeling]
tags: [priming_exercise, VO2_kinetics, VO2_slow_component, critical_power, W_prime, warm_up, motor_unit_recruitment, oxygen_delivery]
sources:
  - 10_來源摘要/Goulding_2023_priming_exercise_VO2_kinetics.md
source_tier: 4
evidence_level: moderate
confidence: medium_high
contested: true
contradictions:
  - Priming exercise is not equivalent to generic warm-up.
  - Overall VO2 kinetics speeding does not prove fundamental phase tau is faster.
  - Lactic acidosis, increased muscle temperature, and increased O2 delivery alone do not adequately explain the priming effect.
---

# Priming Exercise and V̇O2 Kinetics

## One-Sentence Definition

Priming exercise 是在 criterion exercise 前安排 heavy / severe exercise，使後續 VO2 kinetics 的 `tauVO2`、fundamental phase amplitude 或 `VO2 slow component` 改變的現象。

## Definition and Boundary

這裡的 priming exercise 不是一般「熱身」的同義詞。

本頁只處理 Goulding et al. 2023 review 支持的概念邊界：

- prior bout 通常是 heavy / severe intensity exercise。
- criterion bout 可是 moderate、heavy 或 severe exercise。
- 解讀時必須區分三個輸出：
  - fundamental phase `tauVO2` 是否降低
  - fundamental phase amplitude 是否增加
  - `VO2 slow component` amplitude 是否降低
- 若只看整段 VO2 response 的 mean response time 或 monoexponential fit，可能把 slow component 減少誤讀成真正的 `tauVO2` speeding。

## Why It Matters

Priming exercise 重要，因為它把 [[VO2_Kinetics]]、[[VO2_Slow_Component]]、[[Critical_Power]] 與 [[Wprime_Recovery]] 接在一起。

同樣是「VO2 response 變快」，可能代表完全不同的 performance consequence：

- `tauVO2` 真的降低：O2 deficit 下降，critical power 較可能增加。
- fundamental amplitude 增加且 slow component 降低：後段額外 O2 cost 減少，`W'` 較可能增加。

所以 priming 不是單純提高興奮度或增加體溫，而是改變 exercise transition 的 bioenergetic trajectory。

## Preconditions or Conditions

- Baseline `tauVO2` 越慢，priming 後越有機會看到 true `tauVO2` reduction。
- Goulding et al. 2023 的 43-study retrospective synthesis 顯示，group-level non-primed `tauVO2 <= 25 s` 時，bout 2 `tauVO2` 多半接近 bout 1；`tauVO2 > 25 s` 時，bout 2 較常降低。
- Healthy young active upright cycling 常見的是 fundamental amplitude 增加與 slow component 降低，不一定有 `tauVO2` reduction。
- Supine / prone exercise、older adults、type 2 diabetes mellitus、heart failure 或其他 O2 delivery / utilization constrained state，較可能顯示 `tauVO2` reduction。
- Performance 解讀必須知道 prior bout、criterion bout、recovery duration 與 power 相對於 [[Critical_Power]] 的位置。

## Mechanism

### Output-side mechanism

```text
prior heavy / severe exercise
-> subsequent exercise onset VO2 response changes
-> possible lower tauVO2
-> possible increased fundamental amplitude
-> possible reduced VO2 slow component
-> reduced O2 deficit or lower late-exercise O2 cost
-> altered CP or W'
```

### Input-side mechanism

最支持的機制不是單一因子，而是多個層級共同作用：

- Enhanced intracellular O2 utilization：single-fibre 與 animal data 支持第二次 contraction onset 可更快調整 intracellular PO2，即使 O2 delivery ratio 沒變。
- Altered motor unit recruitment：prior exercise 可能讓較多 motor units 在 onset 被招募，減少後續 progressive recruitment，因此增加 fundamental amplitude 並降低 slow component。
- Improved O2 delivery：prior exercise 常提高 heart rate、blood flow、muscle oxygenation 與 microvascular O2 availability；這可能調節 slow component，也可能在 O2 constrained populations 中更重要。

較不支持作為主要因果機制：

- Residual lactic acidosis：效果可在沒有 systemic lactic acidosis 的情境出現。
- Muscle temperature alone：human passive heating 多數不能重現 priming-like pulmonary VO2 kinetics change。
- O2 delivery alone：delivery 增加常同時出現，但不是充分或必要條件。

## Observable Patterns

- 若 priming 後整體 VO2 response 變快，第一個問題不是「tau 變快了嗎」，而是「哪個 phase 改變了」。
- High aerobic fitness / fast baseline kinetics 的人，較可能表現為 `W'` improvement，而不是 CP increase。
- Slower baseline kinetics 的人，較可能因 `tauVO2` lowering 而表現為 CP increase。
- Prior severe-intensity priming 若 recovery 太短，可能傷害後續 severe-domain performance。
- Prior heavy-intensity priming，且只造成 modest lactate increase 約 `2-3 mmol/L`，在文獻中較常見一致的 performance improvement。

## Clinical / Research Implication

### CPET interpretation

- 做 VO2 kinetics analysis 時，必須拆 fundamental phase 與 slow component。
- 若受試者做過 prior exercise，baseline state 已不是 neutral rest-to-work transition。
- 對 disease / older adult groups，priming effect 可能反映 O2 delivery-utilization matching 改變，不應直接外推到 athlete warm-up prescription。

### Training / performance

- 競賽前 priming 不應用「越強越好」處理。
- 必須依 criterion event duration、CP boundary、recovery duration 與 baseline kinetics 決定。
- 若目標事件是 supra-CP 約 2-30 分鐘，trained athlete 可能主要從 `W'` 增加受益。
- 若個體 baseline `tauVO2` 較慢，priming 可能較有機會透過 CP increase 影響更長時間 performance；但這是 review-level hypothesis，不是定論。

### Rehabilitation boundary

- 本來源不能直接支持在 frailty、heart failure、COPD、neurologic disease 或高跌倒風險病人 routine 使用 severe priming。
- 若要測試 priming-like strategy，需有 symptom monitoring、intensity-domain control、recovery control 與停止標準。

## Fact

- Prior heavy exercise 可改變後續 VO2 kinetics。
- 變化可以來自 `tauVO2` lowering、fundamental amplitude increase 或 slow component reduction。
- Baseline `tauVO2` 較慢時，priming 後較可能看到 true `tauVO2` reduction。
- Lactic acidosis 與 muscle temperature alone 不足以解釋主要 priming effect。
- Enhanced intracellular O2 utilization 與 altered motor unit recruitment 是 Goulding et al. 2023 最支持的機制方向。
- Priming 對 CP 或 W' 的影響取決於 VO2 response 的哪一個 phase 被改變。

## Inference

- 用 priming 來設計 warm-up 時，應先判斷運動員是 fast kinetics / W' limited，還是 slow kinetics / CP limited。
- 臨床族群若 baseline kinetics 慢，理論上可能更容易有 `tauVO2` response，但風險與安全邊界比 ergogenic logic 更重要。
- 若研究沒有明確定義 CP，priming performance result 很容易被錯誤歸因。

## Assumption

- `tauVO2`、fundamental amplitude 與 slow component 的 phase partition 是合理且可重現的。
- CP 是判讀 heavy vs severe exercise 的主要 boundary。
- Event duration mapping，例如 2-30 分鐘或 >30 分鐘，是建立在 authors' mechanistic reasoning 上，而不是完成驗證的 prescription rule。

## Uncertainty

- 最佳 priming intensity 與 recovery duration 尚未確定。
- Mitochondrial calcium 是否直接介導 human dynamic exercise 的 priming effect 尚未證實。
- Motor unit recruitment evidence 仍受 surface EMG 方法限制。
- 不同 disease group、older adults、women、children、rehabilitation populations 的安全性與效果仍需直接研究。

## Limitations and Misreadings

- 誤讀 1：Priming exercise 就是一般熱身。錯；本頁處理的是 prior heavy / severe exercise 對 VO2 kinetics 的 phase-specific effect。
- 誤讀 2：血乳酸高，所以 priming 有效。錯；residual acidosis 不是主要因果解釋。
- 誤讀 3：整體 VO2 response 快了，所以 `tauVO2` 一定變快。錯；可能只是 slow component 變小。
- 誤讀 4：severe priming 越強越好。錯；recovery 太短時可能降低後續 performance。
- 誤讀 5：這可直接套到病人訓練。錯；review 提供機制框架，不等於 clinical prescription。

## Links

- [[VO2_Kinetics]]
- [[VO2_Slow_Component]]
- [[Critical_Power]]
- [[Wprime_Recovery]]
- [[CP_Wprime_Interval_Design]]
- [[Exercise_Intensity_Domains]]
- [[../10_來源摘要/Goulding_2023_priming_exercise_VO2_kinetics]]
