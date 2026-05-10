---
title: Caen et al. 2021 - W' recovery kinetics after exhaustion
created: 2026-04-25
updated: 2026-05-07
type: source_summary
domain: [CPET, exercise_physiology, performance_modeling]
tags: [W_prime, recovery, exhaustion, biexponential, VO2_kinetics, PCr, aerobic_fitness, W_BAL, original_article]
source_tier: 3
evidence_level: limited
confidence: medium
contested: true
contradictions:
  - Exhaustion-based W' recovery should not be reduced to a single universal monoexponential tau.
  - Short-rest W' recovery partly reflects enhanced aerobic energy provision, but W'OBS remains a whole-system operational construct.
  - Complete-exhaustion two-phase behavior should not be directly generalized to partial-depletion interval work.
---

# Source Summary: Caen et al. 2021 - W' Recovery Kinetics after Exhaustion

## Source Type

- Original research article.
- Journal: *Medicine & Science in Sports & Exercise*.
- Citation: Caen K, Bourgois G, Dauwe C, Blancquaert L, Vermeire K, Lievens E, Van Dorpe J, Derave W, Bourgois JG, Pringels L, Boone J. *W' Recovery Kinetics after Exhaustion: A Two-Phase Exponential Process Influenced by Aerobic Fitness.* 2021;53(9):1911-1921.
- DOI: 10.1249/MSS.0000000000002673.
- 原始檔：`C:\原始資料\w__recovery_kinetics_after_exhaustion__a_two_phase\w__recovery_kinetics_after_exhaustion__a_two_phase.md`
- 本輪只處理此一篇來源；未混入 Ferguson 2010、Skiba 2015、Chorley 2021、Lievens 2024 或其他 W' recovery 來源。

## Reliability Level

- Evidence tier: Tier 3 original article.
- 可信度：medium。
- 理由：研究問題明確，直接比較 `W'OBS`、`W'BAL`、`W'ADJ`，並用 monoexponential / biexponential fitting 與 AICc 評估模型；但樣本僅 21 位 physically active young men，皆為 cycling protocol，且 `W'OBS` 與 `W'ADJ` 都是 operational / model-derived 指標。

## One-Sentence Summary

在 complete exhaustion 後，Caen et al. 2021 顯示 `W'` recovery 比單一 universal tau 更像 fast + slow two-phase process；短 recovery 的高於預期恢復部分來自 `VO2` kinetics 帶來的 enhanced aerobic contribution，但仍不能把 `W'` 簡化成單一 aerobic、PCr 或 anaerobic tank。

## Core Concepts Extracted

### Concept: Exhaustion-Based Two-Phase W' Recovery

#### One-Sentence Definition

Exhaustion-based two-phase W' recovery 指 complete W' depletion 後，下一段 work capacity above CP 的恢復呈現 fast initial phase 與 slower second phase，而不是由單一固定 time constant 完整描述。

#### Known Facts

- 研究納入 21 位 physically active men；平均年齡 25 ± 2 yr，`VO2peak` 54.4 ± 5.3 mL/min/kg。
- 受試者先以多次 constant-load tests 估計 `CP` 與 `W'`，平均 `CP` 269 ± 31 W，`W'` 19.2 ± 5.1 kJ。
- 實驗 protocol 使用兩段相同 exhaustive work bouts（WB1 / WB2），中間 recovery durations 為 30、60、120、180、240、300、600、900 秒。
- Recovery power 固定為 90% `GET`。
- `W'OBS` 以 WB2 TTE / WB1 TTE 估計，假設 WB1 結束時 `W' = 0`。
- Standard `W'BAL` model 的 `tau` 為 524 ± 41 秒，fitting `W'OBS` 的 RMSE 為 18.6%。
- `W'BAL` 在 30 秒到 5 分鐘 recovery 條件下低估 `W'OBS`。
- Monoexponential fitting of `W'OBS`：`tau` 約 104 秒，RMSE 6.4%。
- Biexponential fitting of `W'OBS`：`tau1` 約 11 秒，`tau2` 約 256 秒，RMSE 1.7%；AICc 支持 biexponential 優於 monoexponential。
- 若把 amplitude 固定為理論 100%，biexponential fit 仍優於 monoexponential，但參數變成 `tau1` 約 33 秒、`tau2` 約 965 秒。
- `W'OBS` 在 10 分鐘約 73.7% ± 19.3%，15 分鐘約 71.3% ± 20.8%，呈現 group-level plateau-like response。
- `W'ADJ` 平均比 `W'OBS` 低 11.0% ± 1.5%，代表 improved onset `VO2` kinetics 可解釋一部分短休息恢復。
- `W'ADJ` 的 AICc 不再支持 biexponential 優於 monoexponential，但 biexponential RMSE 仍較低（2.1% vs 3.5%）。
- `VO2` recovery 與 `W'OBS` recovery 正相關（r = 0.47, P = 0.033），但 `VO2` recovery 在 30 秒後多數時間高於 `W'OBS` recovery。
- `W'OBS` 與 `VO2peak` 正相關（r = 0.62, P = 0.003），也與 relative `CP` 正相關（r = 0.57, P = 0.003）。
- Muscle fiber type distribution 在主要分析中不是 significant predictor；但作者指出樣本的 `VO2peak` variability 或 fiber-type heterogeneity 不足可能遮蔽關係。

#### Mechanism Chain

```text
Complete severe-domain exhaustion
-> operational assumption: W' depleted to 0 at WB1 termination
-> short active recovery below GET
-> VO2 remains partially elevated / onset O2 deficit in WB2 decreases
-> early WB2 gets greater aerobic contribution than WB1
-> fast ATP-PCr-related restoration also contributes to early recovery
-> slower acid-base and neuromuscular recovery limit full restoration
-> observed W' recovery appears fast + slow, not one universal tau
```

#### Inferences

- `W'OBS` should be treated as whole-system performance recovery above CP, not as direct anaerobic energy store measurement.
- The fast phase is plausibly partly explained by improved aerobic contribution and ATP-PCr system regeneration, but the source does not prove a single dominant mechanism.
- Biexponential fitting is appropriate for this complete-exhaustion protocol, but it is not automatically the correct model for partial depletion, race-like intermittent work, or clinical exercise prescription.
- Aerobic fitness should be considered a candidate covariate in individualized W' recovery modeling.

#### Assumptions

- WB1 exhaustion represents complete `W'` depletion.
- WB2 TTE relative to WB1 TTE is a valid operational estimate of recovered `W'`.
- The `W'ADJ` calculation reasonably estimates the mechanical work benefit from reduced `O2` deficit, using 1 L `O2` = 21.1 kJ and gross mechanical efficiency of 22%.
- `VO2` off-kinetics can serve as a proxy for intramuscular PCr recovery, but this is not direct `31P-MRS` evidence in this study.

#### Uncertainties / Limitations

- External validity is limited to healthy young physically active men using cycling protocols.
- The study does not test women, older adults, elite athletes, children, heart failure, COPD, neurologic disease, or rehabilitation populations.
- The study uses complete exhaustion; the authors explicitly state that partial W' depletion may not evoke an equally steep fast phase.
- `W'ADJ` is an estimate, not direct partitioning of aerobic vs anaerobic energy contribution.
- Muscle fiber type results are inconclusive rather than evidence that MFT distribution is irrelevant.

## Clinically Useful Points

- For CPET / performance modeling, short recovery after full exhaustion can restore much more `W'OBS` than a single group-derived `W'BAL` tau predicts.
- Do not interpret `W'BAL = remaining anaerobic battery`; the source supports `W'OBS` as a whole-system operational construct.
- In clinical exercise prescription, this study should not be used to justify aggressive severe-domain intervals in vulnerable patients; it is a mechanistic cycling study in healthy young men.
- If short-rest severe-domain intervals are used in athletes, recovery power, recovery duration, prior depletion state, and aerobic fitness all matter.

## Research-Useful Points

- This source supports separating complete-exhaustion W' recovery from partial-depletion W' recovery.
- Model comparison should report both fit error and complexity penalty; lower RMSE alone is not enough.
- Future W' recovery models likely need dynamic parameters that account for recovery intensity, depletion state, aerobic fitness, and accumulated fatigue.
- The `W'ADJ` approach is useful as a conceptual correction for onset `VO2` kinetics, but it remains model-based and should be interpreted cautiously.

## Conflicts With Existing Knowledge

- 與「W' recovery 可由單一 universal tau 描述」衝突；本來源顯示 complete exhaustion 後 `W'OBS` 以 biexponential model fitting 較佳。
- 與「短 recovery 後的高 performance 一定代表 anaerobic store 已快速補滿」衝突；本來源顯示 reduced `O2` deficit / enhanced aerobic contribution 解釋了一部分 `W'OBS`。
- 與「W' recovery = PCr recovery」衝突；本來源顯示 `VO2` recovery 多數時間比 `W'OBS` recovery 快，提示 W' recovery 還包含 acid-base、neuromuscular and whole-system fatigue components。
- 與「complete exhaustion recovery model 可直接套用到 partial depletion intervals」衝突；作者明確指出 partial depletion 可能不會有同樣大的 fast phase。

## Pages That Should Be Created or Updated

- 新增：[[04_CPET/Exhaustion_Based_Two_Phase_Wprime_Recovery]]
- 更新：[[04_CPET/Wprime_Recovery]]
- 更新：[[04_CPET/Wprime_Balance_Model]]
- 更新：[[04_CPET/CP_Wprime_Interval_Design]]
- 連結：[[04_CPET/Partial_Wprime_Depletion_Recovery]]

## Suggested Tags

- W_prime
- recovery
- exhaustion
- biexponential
- VO2_kinetics
- PCr
- aerobic_fitness
- W_BAL
- critical_power
