---
title: Three-Minute All-Out Critical Power Test
created: 2026-05-08
updated: 2026-05-08
type: method
domain: [CPET, exercise_physiology, methodology, training]
tags: [critical_power, W_prime, 3_min_all_out, end_power, WEP, cycling, reliability, validity]
sources:
  - 10_來源摘要/Wright_2017_3min_allout_CP_validity.md
source_tier: 5
evidence_level: original_research_small_validation_study
confidence: medium_low
contested: true
contradictions:
  - EP and WEP do not have the same validity behavior.
  - Linear mode can be reliable yet overestimate CP when resistance / cadence setup is wrong.
  - WEP underestimated W' in both tested modes.
---

# Three-Minute All-Out Critical Power Test

## One-Sentence Definition

3-minute all-out cycling test 是用 3 分鐘 maximal effort 的末段 `end power` (`EP`) 估計 `critical power` (`CP`) 的 single-bout protocol，但 `EP` 與 `WEP` 的 validity 必須分開判讀。

## Definition and Boundary

本頁只整理 Wright et al. 2017 對 3-minute all-out cycling test 的 reliability / validity 評估。

- `EP`: final 30 seconds mean power。
- `WEP`: power-time integral above `EP`。
- Criterion comparison:
  - `CP` 與 `W'` 來自 3 次 fixed-power time-to-exhaustion tests。
- Testing modes:
  - `isokinetic mode`: fixed cadence。
  - `linear mode`: fixed resistance。

本頁不處理 ramp all-out、field critical speed、running 3-minute all-out、clinical CPET safety protocol，或其他 3-minute all-out literature 的 synthesis。

## Why It Matters

3-minute all-out test 的吸引力是 single-bout convenience；但 Wright 2017 顯示，方便不等於所有輸出都 valid。

- `EP` 可能可作 `CP` shortcut。
- `WEP` 不可自動作 `W'` shortcut。
- Reliability 與 validity 必須分開看。
- Ergometer mode、cadence 與 resistance setup 是核心 method variables，不是背景細節。

## Preconditions or Conditions

依 Wright 2017 的 protocol，3-minute all-out test 至少需要：

- Familiarization。
- No elapsed-time or power feedback，以降低 pacing。
- Strong verbal encouragement。
- Warm-up 10 min at 100 W，接 30 s unloaded cycling。
- Participants 被要求在 3 min 內維持 all-out effort。
- 監測 V̇O2，並要求達到 >95% ramp V̇O2max 且末段沒有 decremental V̇O2 trend。
- 明確記錄 ergometer mode、preferred cadence、resistance setting 與 bike setup。

## Mechanism

1. All-out exercise 會快速消耗可在 `CP` 以上使用的 finite work capacity。
2. 若 `W'` 被充分 depleted，末段可維持 power 應接近 `CP`。
3. 因此 final 30 s mean power 被定義為 `EP`。
4. 高於 `EP` 的累積 work 被定義為 `WEP`。
5. 但 power-time profile 受 cadence、resistance、ergometer mode 與 flywheel / inertia 影響。
6. 所以同一個 3-minute all-out protocol 可出現 `EP` reliable、但 criterion validity 不足；也可出現 `EP` valid、但 `WEP` 不 valid。

## Observable Patterns

Wright 2017 的直接結果：

- Original CP protocol:
  - `CP` 244.9 +/- 26.2 W。
  - `W'` 22.7 +/- 5.6 kJ。
- Isokinetic 3-minute all-out:
  - `EP` 240.9 +/- 23.3 W，與 `CP` 無顯著差異。
  - `WEP` 15.6 +/- 5.6 kJ，顯著低於 `W'`。
  - EP CoV 1.93%，ICC 0.97。
- Linear 3-minute all-out:
  - `EP` 275.1 +/- 41.2 W，顯著高於 `CP`。
  - `WEP` 13.5 +/- 4.7 kJ，顯著低於 `W'`。
  - EP CoV 1.17%，ICC 0.99。

## Clinical / Research Implication

- 若目標是快速估計 `CP`，Wright 2017 只支持 **isokinetic EP** 在類似 male cyclist sample 與 protocol control 下有有限 validity。
- 若使用 linear mode，不能只因 EP repeatability 好就接受 CP estimate。
- 若目標是 `W'` 或 severe-domain interval capacity，Wright 2017 不支持用 `WEP` 直接替代。
- 在 clinical CPET 場景，3-minute all-out test 不是 routine substitute；若要用，需另有 safety screening、population-specific validation 與 clear stopping criteria。

## Fact

- Source 是 Tier 5 original research article。
- Participants 是 12 位 male cyclists，不是 clinical patients。
- `EP-isokinetic` 與 `CP` 無顯著差異。
- `EP-linear` 顯著高於 `CP`。
- `WEP-isokinetic` 與 `WEP-linear` 都顯著低於 `W'`。
- `EP` 的 CoV 低於 `WEP`。

## Inference

- `EP` 的 method validity 主要取決於 testing mode 與 setup control。
- `WEP` 的 construct validity 比 `EP` 更脆弱，不宜用於高精度 prescription。
- 若 clinical or rehab use 需要安全與決策價值，本研究證據不足以支持常規採用。

## Assumption

- 本頁把 Wright 2017 的 three fixed-power CP estimate 視為 criterion comparator。
- 本頁假設 source 所描述的 all-out effort criteria 足以支持內部 protocol validity。
- 本頁不假設其他 ergometers、load-setting methods 或 populations 會得到相同結果。

## Uncertainty

- Linear mode 若改用 body-mass based resistance 或其他 load-setting procedure，是否能改善 CP validity，仍需另查來源。
- Isokinetic mode 是否在 women、older adults、low-fit adults、HF / COPD / PH patients 中 valid，未知。
- 3 分鐘是否足以完整 deplete `W'`，source 也保留疑問。

## Limitations and Misreadings

- 錯誤讀法：3-minute all-out test 已經全面取代 multi-bout CP testing。
- 修正：Wright 2017 只支持特定 protocol 下的 isokinetic `EP` 可近似 `CP`。
- 錯誤讀法：EP reliable，所以 WEP 也 reliable and valid。
- 修正：WEP 在兩種 mode 都低估 `W'`。
- 錯誤讀法：linear mode EP CoV 很低，所以可用於 CP。
- 修正：linear mode 在本研究 reliable but not valid。

## Links

- [[../10_來源摘要/Wright_2017_3min_allout_CP_validity]]
- [[CP_Test_Reliability]]
- [[CPET_Protocol_Design]]
- [[Critical_Power]]
