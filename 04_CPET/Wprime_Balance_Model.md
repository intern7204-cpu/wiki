---
title: W' Balance Model（W'BAL）
created: 2026-04-25
updated: 2026-04-25
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

- 代表性來源：Skiba 早期模型。
- 核心 original article（Skiba 2012）把 intermittent exercise 的 `W'` 消耗 / 回補寫成連續方程式，並提出早期 `tau-W'` 與 `DCP` 的經驗式。
- 優點：實務上應用廣。
- 問題：假設 ongoing microscopic recovery，極端情境可能出現不合理行為。

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
- Skiba 2015 進一步顯示：
  - `W'` recovery half-time 約 **232 s**
  - bulk `[PCr]` recovery half-time 約 **38 s**
  - 與 W' 更貼近的是 `D[PCr]` / oxidative reserve 的概念，而不是把 `W'` 直接等同於一個 PCr tank。
- Ferguson 2010 也支持這個方向：
  - prior exhaustion 後 `CP` 幾乎不變
  - `W'` recovery 呈 curvilinear，且速度慢於 `VO2` recovery、快於 lactate recovery
  - 這代表 `W'` 不是單一 PCr / `VO2` / lactate proxy
- Caen 2021 的 whole-body cycling 也支持這個方向：
  - `W'BAL` 對 `<5 min` 的 recovery 系統性偏慢
  - 更快的 `VO2` kinetics 能解釋部分短休息恢復，但不是全部
- Skiba 2014 再補一個 practical caveat：
  - 同樣目標 depletion，不同 work / recovery duration 排列，`W'ACT` 可實際高於 `W'BAL`
  - 也就是 session architecture 本身就會改變 model error
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
