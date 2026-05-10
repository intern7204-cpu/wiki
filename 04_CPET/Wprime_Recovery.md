---
title: W' Recovery（W' reconstitution）
created: 2026-04-25
updated: 2026-05-07
type: concept
domain: [CPET, exercise_physiology, methodology]
tags: [W_prime, recovery, critical_power, W_BAL, interval_exercise, aerobic_fitness]
sources:
  - 10_來源摘要/Jones_Vanhatalo_2017_critical_power_concept.md
  - 10_來源摘要/Chorley_Lamb_2020_CP_W_reconstitution_training.md
  - 10_來源摘要/Chorley_2021_biexponential_Wprime_reconstitution_trained_cyclists.md
  - 10_來源摘要/Bartram_2018_Wprime_recovery_elite_cyclists.md
  - 10_來源摘要/Skiba_2015_intramuscular_determinants_Wprime_recovery.md
  - 10_來源摘要/Ferguson_2010_Wprime_recovery_after_exhaustion.md
  - 10_來源摘要/Caen_2021_Wprime_recovery_two_phase.md
  - 10_來源摘要/Caen_2019_Wprime_reconstitution_depends_on_work_and_recovery.md
  - 10_來源摘要/Lievens_2024_partial_Wprime_recovery.md
  - 10_來源摘要/Skiba_2014_work_recovery_durations_Wprime_reconstitution.md
  - 10_來源摘要/McMahon_Jenkins_PCr_resynthesis_after_intense_exercise.md
  - 10_來源摘要/Karsten_2016_intertrial_recovery_CP_Wprime.md
  - 10_來源摘要/Sreedhara_2020_Modeling_Wprime_Recovery.md
  - 10_來源摘要/Chidnok_2013_intermittent_exercise_PCr_CP.md
source_tier: 1
evidence_level: moderate
confidence: medium
contested: true
contradictions:
  - W' recovery should not be treated as a single universal monoexponential recharge constant.
  - PCr and VO2 recovery contribute to W' reconstitution, but W' recovery remains a broader whole-system construct.
  - Exhaustion-derived two-phase recovery behavior cannot be assumed to generalize unchanged to partial depletion conditions.
---

# W' Recovery（W' reconstitution）

## 一句話定義

W' recovery 指的是 severe-domain effort 後，**再次可用的 work capacity above CP 如何回來**；它不是單純「電池充電」，而是受 recovery power、recovery duration、aerobic fitness 與模型假設共同影響的 whole-system process。

## 核心機制

### 費曼式理解

- `W'` 像是你在 `CP` 以上能額外花掉的那一段「超額工作預算」。
- 休息時，這段預算會回來。
- 但它不是一格一格等速補滿，也不是只看 PCr 回來多少。

### 哪些因素會影響恢復

- recovery power
- recovery duration
- aerobic fitness
- depletion 程度
- 用哪種 model 去估

### 目前 field 最重要的共識與修正

### 1. recovery 確實存在，且與 muscle metabolic restoration 有關

- [[../10_來源摘要/Chidnok_2013_intermittent_exercise_PCr_CP]] 支持較長 recovery 可帶來較多 intramuscular metabolic restoration，也讓後續 `W > CP` 維持更久。

### 2. 但 W' recovery 不等於 PCr recovery

- [[../10_來源摘要/Skiba_2015_intramuscular_determinants_Wprime_recovery]] 顯示：
  - bulk `[PCr]` recovery half-time 約 `38 s`
  - `W'` recovery half-time 約 `232 s`
- 結論不是 PCr 無關，而是 **W' 不是單一 PCr tank 的別名**。

### 3. exhaustion 後 recovery 確實是曲線式，但不等於單一代謝 proxy

- [[../10_來源摘要/Ferguson_2010_Wprime_recovery_after_exhaustion]] 顯示：
  - recovery `2 / 6 / 15 min` 後，`W'` 約回到 `37% / 65% / 86%`
  - `CP` 幾乎不變
  - `W'` recovery half-time 約 `234 s`
  - `VO2` recovery 較快、lactate recovery 較慢
- 結論是：**W' recovery 有自己的 whole-system kinetics，不能直接縮成單一 `VO2` 或 lactate 曲線。**

### 4. exhaustion data 常支持 fast + slow phase

- [[Exhaustion_Based_Two_Phase_Wprime_Recovery]] 整理 [[../10_來源摘要/Caen_2021_Wprime_recovery_two_phase]] 的 single-source concept。
- Caen 2021 在 complete exhaustion 後 whole-body cycling 顯示：
  - fast phase `tau1 ≈ 11 s`
  - slower phase `tau2 ≈ 256 s`
- standard group-derived `W'BAL` 對 `<5 min` recovery 會系統性低估恢復。
- 但校正 changed `VO2` kinetics 後，`W'ADJ` 的 AICc 不再支持 biexponential 優於 monoexponential；所以 fast phase 不能被簡化成單一 anaerobic tank 迅速補滿。

### 5. trained cyclists 的 repeated maximal ramps 也支持 two-phase behavior

- [[../10_來源摘要/Chorley_2021_biexponential_Wprime_reconstitution_trained_cyclists]] 顯示：
  - 在 trained cyclists 的 repeated maximal ramps 中，
    biexponential fit 優於 monoexponential
  - 第一段 recovery 可見約各半的 fast / slow amplitude
  - 第二段 recovery 主要是 slow component 變慢
- 這支持：
  - `W'` recovery 不是單一固定 `tau`
  - repeated-bout state 會改變 recovery shape

### 6. 但 partial depletion 不一定同樣需要 biexponential

- 詳見 [[Partial_Wprime_Depletion_Recovery]]。
- [[../10_來源摘要/Lievens_2024_partial_Wprime_recovery]] 顯示：
  - 在 partial depletion 條件下，`AICc` 多數情況不支持 biexponential 明顯優於 monoexponential
  - 但固定 `tau` 仍不足以同時描述不同 depletion 程度
- 所以目前更合理的表述是：
  - **partial depletion 已有資料，但還不足以建立單一共識模型**
  - exhaustion-based two-phase story 不能直接照搬

### 7. 前一段 work bout 本身也會改變回補表現

- [[../10_來源摘要/Caen_2019_Wprime_reconstitution_depends_on_work_and_recovery]] 顯示：
  - `W'` reconstitution 不只看 recovery duration 與 recovery power
  - 前一段 exhaustive bout 的 intensity-duration 特性也會改變 recovery rate
  - 較慢 depletion 的 `P8` 條件，後續 recovery 反而比 `P4` 更慢
- 這代表：
  - 不能把 `W'` recovery 縮成「休多久、休多輕」兩個旋鈕就夠

### 8. interval structure 本身會改變回補表現

- [[../10_來源摘要/Skiba_2014_work_recovery_durations_Wprime_reconstitution]] 顯示：
  - `W'BAL` 整體上仍有實用性
  - 但短 work intervals 或某些短 recovery 結構，會讓 `W'ACT` 高於模型預測
- 這代表 severe-domain interval 不能只看總工作量，還要看 session architecture。

### 9. athlete-specific difference 很大

- [[../10_來源摘要/Bartram_2018_Wprime_recovery_elite_cyclists]] 提示 elite cyclists 的 recovery 可比 SKIBA 2 預測更快。
- [[../10_來源摘要/Sreedhara_2020_Modeling_Wprime_Recovery]] 則提醒 individualized model 與 recovery power 都可能改變預測。

### 10. recovery biology 本身就可能有快相與慢相

- [[../10_來源摘要/McMahon_Jenkins_PCr_resynthesis_after_intense_exercise]] 從 PCr physiology 整理出：
  - 較早的恢復比較像 ADP / free-energy driven
  - 較慢的恢復較受 intracellular pH normalization 影響
- 這不能直接等同於 `W'` recovery 全貌，
  但它很能解釋為什麼 short-rest behavior 常不像單一固定速度。

### 11. 測試 protocol 本身就能讓 W' 比 CP 更容易失真

- [[../10_來源摘要/Karsten_2016_intertrial_recovery_CP_Wprime]] 顯示：
  - 把 exhaustive trials 之間的 recovery 從 `24 h` 壓到 `3 h` 或 `30 min`
  - `CP` 仍可接近
  - `W'` agreement 則明顯變差
- 這提醒我們：`W'` recovery 不只是模型問題，也會直接反映在 **測試輸入值本身的脆弱性**。

## 臨床表現

### 訓練與研究上的重要性

- 設計 severe-domain intervals 時，不能只看 work bout。
- 你還要決定：
  - 休多輕
  - 休多久
  - 想讓每組恢復到多少
- 這也是為什麼同樣寫成 `6 x 2 min`，不同 recovery 設計會變成完全不同 session。

## 評估方式

- 目前沒有 single gold-standard clinical test 直接量到「真實 W' recovery」。
- 多數實務仍依賴：
  - intermittent performance protocol
  - model-based estimate
  - 同一 athlete repeated testing

## 治療原則

### 實務原則

- 用同一模型追同一個人，比拿不同模型跨人比較更有意義。
- 若 recovery 很短，不要過度相信單一 `tau`。
- 若目標是維持後續 interval quality，recovery power 和 recovery duration 都要一起設計。

## 臨床決策點

### 反對論點

- 「只要看 PCr 回補，就知道 W' 回來多少。」
- 「W'BAL 算出一個數字，就可以當真實剩餘能力。」

### 反駁

- PCr recovery 比 W' recovery 快得多，兩者不能直接畫等號。
- W'BAL 很有用，但它輸出的是 assumption-sensitive estimate，不是直接量到的生理真值。

### 結論

- W' recovery 最好的定位，是 **operational guide for interval design**，不是 exact recharge meter。

## 限制與未定論

### 目前限制 / 爭議點

- exhaustion 後的 kinetics 不一定能直接外推到 partial depletion；目前只有小樣本 original article 提供初步修正。
- 不同運動型態、不同 athlete level、不同 model family，恢復常數可能不同。
- aerobic contribution、PCr recovery、acid-base restoration 與 neuromuscular fatigue 的相對權重，仍未被單一模型完整統整。

### frontmatter contradictions

- W' recovery should not be treated as a single universal monoexponential recharge constant.
- PCr and VO2 recovery contribute to W' reconstitution, but W' recovery remains a broader whole-system construct.
- Exhaustion-derived two-phase recovery behavior cannot be assumed to generalize unchanged to partial depletion conditions.

## 理解缺口

- partial depletion 與 full exhaustion 的 recovery curve 差多少？
- 什麼情況下應該用 integral model，什麼情況下該用 individualized or differential model？

## 臨床使用版

- 若你要用費曼式方式教 severe-domain interval，這頁應先看。
- 最重要的不是背哪個 `tau`，而是記住：**W' 回得不是同一種速度，也不是只靠一種機制。**

## 來源

### 來源摘要連結

- [[10_來源摘要/Jones_Vanhatalo_2017_critical_power_concept]]
- [[10_來源摘要/Chorley_Lamb_2020_CP_W_reconstitution_training]]
- [[10_來源摘要/Chorley_2021_biexponential_Wprime_reconstitution_trained_cyclists]]
- [[10_來源摘要/Bartram_2018_Wprime_recovery_elite_cyclists]]
- [[10_來源摘要/Skiba_2015_intramuscular_determinants_Wprime_recovery]]
- [[10_來源摘要/Ferguson_2010_Wprime_recovery_after_exhaustion]]
- [[10_來源摘要/Caen_2021_Wprime_recovery_two_phase]]
- [[10_來源摘要/Caen_2019_Wprime_reconstitution_depends_on_work_and_recovery]]
- [[10_來源摘要/Lievens_2024_partial_Wprime_recovery]]
- [[10_來源摘要/Skiba_2014_work_recovery_durations_Wprime_reconstitution]]
- [[10_來源摘要/McMahon_Jenkins_PCr_resynthesis_after_intense_exercise]]
- [[10_來源摘要/Karsten_2016_intertrial_recovery_CP_Wprime]]
- [[10_來源摘要/Sreedhara_2020_Modeling_Wprime_Recovery]]
- [[10_來源摘要/Chidnok_2013_intermittent_exercise_PCr_CP]]

### 證據標記

- 來源層級：1
- evidence_level：moderate
- confidence：medium

## 相關頁面

- [[Wprime_Balance_Model]]
- [[Exhaustion_Based_Two_Phase_Wprime_Recovery]]
- [[Partial_Wprime_Depletion_Recovery]]
- [[CP_Wprime_Interval_Design]]
- [[Training_Prescription_by_CP]]
- [[Critical_Power]]
- [[../05_Exercise_Physiology/PCr_Resynthesis]]
- [[../05_Exercise_Physiology/Skeletal_Muscle_Energy_Metabolism]]
- [[../10_來源摘要/McMahon_Jenkins_PCr_resynthesis_after_intense_exercise]]
- [[../10_來源摘要/Karsten_2016_intertrial_recovery_CP_Wprime]]
