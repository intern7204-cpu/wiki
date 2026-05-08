---
title: W' Balance Model（W'BAL）
created: 2026-04-25
updated: 2026-05-08
type: method
domain: [CPET, exercise_physiology, methodology]
tags: [W_BAL, W_prime, critical_power, intermittent_exercise, modeling]
sources:
  - 09_來源摘要/Jones_Vanhatalo_2017_critical_power_concept.md
  - 09_來源摘要/Chorley_Lamb_2020_CP_W_reconstitution_training.md
  - 09_來源摘要/Chorley_2021_biexponential_Wprime_reconstitution_trained_cyclists.md
  - 09_來源摘要/Skiba_Clarke_Wprime_balance_model.md
  - 09_來源摘要/Skiba_2012_modeling_Wprime_expenditure_reconstitution.md
  - 09_來源摘要/Skiba_2015_intramuscular_determinants_Wprime_recovery.md
  - 09_來源摘要/Ferguson_2010_Wprime_recovery_after_exhaustion.md
  - 09_來源摘要/Caen_2021_Wprime_recovery_two_phase.md
  - 09_來源摘要/Caen_2019_Wprime_reconstitution_depends_on_work_and_recovery.md
  - 09_來源摘要/Lievens_2024_partial_Wprime_recovery.md
  - 09_來源摘要/Skiba_2014_work_recovery_durations_Wprime_reconstitution.md
  - 09_來源摘要/Sreedhara_2019_power_energy_models.md
  - 09_來源摘要/Bartram_2018_Wprime_recovery_elite_cyclists.md
  - 09_來源摘要/Sreedhara_2020_Modeling_Wprime_Recovery.md
  - 09_來源摘要/Chidnok_2013_intermittent_exercise_PCr_CP.md
source_tier: 1
evidence_level: moderate
confidence: medium
contested: true
contradictions:
  - W'BAL is a useful modeling tool, not a direct measurement of a single physiologic tank.
  - Integral, differential, and athlete-specific recovery models should not be mixed without explicitly stating their assumptions.
  - Work/recovery structure and depletion state can change observed W' reconstitution, so one fixed tau should not be treated as universally valid.
---

# W' Balance Model（W'BAL）

## 一句話定義

W'BAL 是把 **CP/W' 延伸到 intermittent exercise** 的實用模型，用來估計 severe-domain work bout 後還剩多少 `W'`；但它是 **model-based estimate**，不是直接量到的單一生理儲槽。

## 核心機制

### 為什麼需要 W'BAL

- 傳統 `CP + W'/t` 適合 continuous severe exercise。
- 真實訓練與比賽常有 work / recovery 交替，需要估計 W' depletion 與 reconstitution。

### 常見 model family

### 1. integral form

- 代表性來源：Skiba 2012（n=7 male recreational cyclists、60 s severe / 30 s recovery）。
- 連續方程式：`W'_bal(t) = W' − ∫₀ᵗ W'_exp · exp(−(t−u)/τ_W') du`。
- 經驗 τ 公式：`τ_W' = 546 · exp(−0.01 · D_CP) + 316`（r² = 0.77；S20+S_M+S_H 合併迴歸）。
- 群均 `τ_W'`：S20（20 W）`377 ± 29 s`、S_M（0.9·P_GET）`452 ± 81 s`、S_H（GET+50%·(CP−GET)）`578 ± 105 s`、S_S（>CP）`7056 ± 11 169 s`（發散，模型在 P > CP 失效）。
- 適用範圍：recovery < CP；P > CP 時 `τ_W'` 失去物理意義，僅代表 depletion 速率變慢。
- 假設：(a) `τ_W'` 由 iterative fit 得，強制 W'BAL = 0 在 exhaustion 時；(b) recovery 期間 power 視為固定；(c) 一個 session 內單一 τ。
- subj 4（VO2max > 5 L/min）的 τ 在 S20 與 S_M 之間幾乎不變，提示高度有氧訓練者需 individualized τ；後續 Bartram 2018 elite cyclist 公式即此延伸。
- 優點：實務上應用廣，提供 race-data simulation 的具體公式。
- 問題：假設 ongoing microscopic recovery，極端情境可能出現不合理行為；Skiba & Clarke 2021 後續指出 Eq 3 原文有 dimensional ambiguity（du vs dt），需明寫成 convolution integral。

### 2. differential / ODE form

- recovery 與 depletion 互斥，計算較直接。
- 但 recovery 有時可能預測過快。

### 3. athlete-specific refinement

- elite cyclists 或個別受試者可能需要更快或不同的 recovery parameter。
- 這類修正較適合個體內應用，不適合直接外推。
- Caen 2021 的 exhaustion model 更進一步提醒：
  - `W'` recovery 可能呈現 fast + slow 兩階段
  - 若硬用單一 `tau`，短 recovery 常被低估
- Chorley 2021 也在 trained cyclists 的 repeated maximal ramp 資料中看到：
  - biexponential fit 優於 monoexponential
  - repeated bouts 主要讓 slow component 變慢
- 但 Lievens 2024 也提醒：
  - 在 partial depletion 條件下，資料不一定支持 biexponential 優於 monoexponential
  - 所以 exhaustion-based two-phase behavior 不能直接外推到所有 interval 情境

### 生理支撐來自哪裡

- Chidnok 2013 用 `31P-MRS` 顯示：recovery interval 越長，PCr reconstitution 越多，intermittent `W>CP` 就越大。
- 這不等於 `W'BAL` 已被「證明為唯一正確模型」。
- 但它提供了一個重要方向：**reconstitution 不是純數學幻覺，而與 muscle metabolic recovery 有一致的生理訊號**。
- Skiba 2015 進一步在 single-leg knee-extension（n=10）裡用 31P-MRS / 1H-MRS 顯示：
  - `W'` recovery half-time 約 **232 ± 108 s**（個體 `135–426 s`）
  - bulk `[PCr]` recovery half-time 約 **39 ± 16 s**（abstract `38 s`）
  - 但 `τ_[PCr]` 與 `τ_W'` **無顯著相關**（`r = 0.38, p = 0.28`）；與 W' 較貼近的是 `D[PCr]` / oxidative reserve（`r = 0.99, p = 0.005`），而不是 bulk PCr 是否回到很高。
  - 同篇還推導了不需 fitting 的新 `τ_W' = W'_0 / D_CP`；對 Skiba 2012 既有資料 `r = 0.84` 但 Passing–Bablok 顯示 systematic offset（intercept ≈ 288 s，slope ≈ 0.79），代表新推導要當成 starting point 而非 universal formula。
  - carnosine 與 `W' T1/2` 的 inverse curvilinear 關係 `R² = 0.55`（剔除單一 outlier 升至 0.80）屬 exploratory，非 mechanism 結論。
- Ferguson 2010 也支持這個方向：
  - prior exhaustion 後 `CP` 幾乎不變（`P = 0.922` 跨 2 / 6 / 15 min recovery）
  - `W'` recovery 呈 curvilinear（`37 / 65 / 86%` 對應 2 / 6 / 15 min recovery），interpolated `t1/2 ≈ 234 s`
  - `VO2` recovery 顯著較快（`t1/2 ≈ 74 s`）、blood lactate recovery 顯著較慢（`t1/2 ≈ 1366 s`）
  - 這代表 `W'` 不是單一 PCr / `VO2` / lactate proxy，而較可能是 **fatigue-metabolite accumulation/clearance 的整合**
- Caen 2021 的 whole-body cycling 也支持這個方向：
  - `W'BAL` 對 `<5 min` 的 recovery 系統性偏慢
  - 更快的 `VO2` kinetics 能解釋部分短休息恢復，但不是全部
- Skiba 2014 在 11 位 recreational athletes（5M/6F）的 cycle 模型，固定 work power = `P6 + 50%(P6 − CP)`、recovery power = 20 W、目標 50% depletion 的 6 種 protocol 中：
  - 整體均值：W'_pred 6.76 ± 1.13 kJ vs W'_ACT 8.34 ± 1.42 kJ，Diff = `−1.58 ± 1.06 kJ`；模型平均 underprediction，但條件性顯著。
  - 顯著 underprediction：20-30 (`−1.86 kJ`)、20-20 (`−2.77 kJ`)、20-10 (`−2.78 kJ`)。
  - 不顯著：60-30 (`−0.22 kJ`)、40-30 (`−1.19 kJ`)、20-5 (`−0.75 kJ`)。
  - 同 work-recovery ratio = 2、同 mean P 的 60-30 vs 20-10：`W'_ACT 7.35 vs 8.27 kJ`、fitted `τ_W' 403 vs 234 s`，差 ~12% / ~170 s，顯示「同 ratio 同 mean P ≠ 同效果」。
  - subj 9（CP 366 W、`τ_W' = 104 s` in 60-30）已超出 Skiba 2012 經驗式漸近 316 s，作者明文呼籲「personalized predictive function」（後續 Bartram 2018 elite cyclist 公式即此延伸）。
  - 也就是 session architecture 本身就會改變 model error，且 `W'BAL` 無法靠單一 D_CP-only 經驗 τ 公式描述 short-work / short-recovery 的 priming 效應。
- Caen 2019 則再往前推一步：
  - recovery 不只受 recovery interval 決定
  - 前一段 exhaustive bout 的 intensity-duration 特性也會改變後續 `W'` reconstitution
  - 這也是為什麼單靠 `DCP` 的 group-derived recovery constant 會不夠

## 評估方式

### 使用 W'BAL 前先確認三件事

- CP / W' 是如何得到的
- 用的是哪一種 W'BAL form
- recovery parameter 是 group-derived 還是 individual-derived

### 什麼時候比較有用

- 同一受試者前後比較
- interval design
- pacing simulation
- race file retrospective interpretation

### 什麼時候要保守

- 跨研究比較
- 把 `W'BAL = 0` 當精確 exhaustion time
- 使用與原驗證情境差很大的族群

## 治療原則

### 實務解讀原則

- recovery power 越低，通常 recovery 越快，但不表示只有 power 重要。
- W' recovery 具個體差異，且可能隨 fatigue 狀態改變。
- 即使預測總 depletion 類似，短 work bouts 也可能留下比模型預估更多的可用 `W'`。
- W'BAL 比較適合當 **decision support**，不適合當絕對真值。

## 臨床決策點

### 反對論點

- 「W'BAL 就是剩餘無氧油箱。」
- 「模型算到 0 就一定在那一秒耗竭。」

### 反駁

- W' 本身就不是單一 anaerobic tank；W'BAL 更是建立在多層假設上的 operational estimate。
- CP/W' 輸入誤差、model form、individual variability 都會改變輸出。

### 結論

- W'BAL 應被當成 **assumption-sensitive tool**，不是 mechanistic truth machine。

## 限制與未定論

### frontmatter contradictions

- W'BAL is a useful modeling tool, not a direct measurement of a single physiologic tank.
- Integral, differential, and athlete-specific recovery models should not be mixed without explicitly stating their assumptions.

## 理解缺口

- 哪種 intermittent pattern 最適合哪個 model form？
- exhaustion 應該怎麼 operationalize，才不會對 `0 J` 過度迷信？

## 臨床使用版

- 若你只是想比較同一位選手不同 interval 設計，W'BAL 很有用。
- 若你想用它宣布某人真正剩幾焦耳，技術上就過頭了。

## 來源

### 來源摘要連結

- [[../09_來源摘要/Jones_Vanhatalo_2017_critical_power_concept]]
- [[../09_來源摘要/Chorley_Lamb_2020_CP_W_reconstitution_training]]
- [[../09_來源摘要/Chorley_2021_biexponential_Wprime_reconstitution_trained_cyclists]]
- [[../09_來源摘要/Skiba_Clarke_Wprime_balance_model]]
- [[../09_來源摘要/Skiba_2012_modeling_Wprime_expenditure_reconstitution]]
- [[../09_來源摘要/Skiba_2015_intramuscular_determinants_Wprime_recovery]]
- [[../09_來源摘要/Ferguson_2010_Wprime_recovery_after_exhaustion]]
- [[../09_來源摘要/Caen_2021_Wprime_recovery_two_phase]]
- [[../09_來源摘要/Caen_2019_Wprime_reconstitution_depends_on_work_and_recovery]]
- [[../09_來源摘要/Lievens_2024_partial_Wprime_recovery]]
- [[../09_來源摘要/Skiba_2014_work_recovery_durations_Wprime_reconstitution]]
- [[../09_來源摘要/Sreedhara_2019_power_energy_models]]
- [[../09_來源摘要/Bartram_2018_Wprime_recovery_elite_cyclists]]
- [[../09_來源摘要/Sreedhara_2020_Modeling_Wprime_Recovery]]
- [[../09_來源摘要/Chidnok_2013_intermittent_exercise_PCr_CP]]

### 證據標記

- 來源層級：1
- evidence_level：moderate
- confidence：medium

## 相關頁面

- [[Critical_Power]]
- [[Wprime_Recovery]]
- [[CP_Wprime_Interval_Design]]
- [[Training_Prescription_by_CP]]
- [[CP_Test_Reliability]]
- [[../05_Exercise_Physiology/PCr_Resynthesis]]
