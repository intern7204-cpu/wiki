---
title: Training Prescription by Critical Power（以 CP 處方訓練）
created: 2026-04-23
updated: 2026-04-25
type: method
domain: [CPET, exercise_physiology, training]
tags: [critical_power, W_prime, training_prescription, FTP, interval_training, W_BAL]
sources:
  - 09_來源摘要/Chorley_Lamb_2020_CP_W_reconstitution_training.md
  - 09_來源摘要/Jones_Vanhatalo_2017_critical_power_concept.md
  - 09_來源摘要/Jones_Vanhatalo_Burnley_Morton_Poole_2010_CP_exercise_tolerance.md
  - 09_來源摘要/Poole_2020_anaerobic_threshold.md
  - 09_來源摘要/Triska_2017_CP_reliability.md
  - 09_來源摘要/Skiba_Clarke_Wprime_balance_model.md
  - 09_來源摘要/Bartram_2018_Wprime_recovery_elite_cyclists.md
  - 09_來源摘要/Ferguson_2010_Wprime_recovery_after_exhaustion.md
  - 09_來源摘要/Caen_2021_Wprime_recovery_two_phase.md
  - 09_來源摘要/Caen_2019_Wprime_reconstitution_depends_on_work_and_recovery.md
  - 09_來源摘要/Lievens_2024_partial_Wprime_recovery.md
  - 09_來源摘要/Skiba_2014_work_recovery_durations_Wprime_reconstitution.md
  - 09_來源摘要/Sreedhara_2020_Modeling_Wprime_Recovery.md
  - 09_來源摘要/Karsten_2017_TT_vs_TTE_CP_Wprime.md
  - 09_來源摘要/Karsten_2016_intertrial_recovery_CP_Wprime.md
  - 09_來源摘要/Chidnok_2013_intermittent_exercise_PCr_CP.md
source_tier: 1
evidence_level: consensus
confidence: high
contested: true
contradictions:
  - W'BAL outputs are assumption-sensitive guides, not exact prescriptions of remaining physiologic capacity.
  - TT-derived and TTE-derived W' are not automatically interchangeable for interval prescription.
  - Similar predicted depletion does not guarantee the same actual W' state, because interval structure itself can change reconstitution behavior.
---

# Training Prescription by Critical Power（以 CP 處方訓練）

## 一句話定義

以 **Critical Power（CP）** 處方訓練，核心是在生理上把 **LT/GET** 當作 moderate-heavy 邊界、把 **CP** 當作 heavy-severe 邊界，再用 **W' / W'BAL** 個別化 severe-domain interval 的工作量。

## 核心機制

### 為什麼不用 FTP 當唯一核心

- FTP 是實務上方便的 performance proxy。
- 但 [[Critical_Power]] 才是 heavy-severe 邊界的較佳生理定義。
- Chorley & Lamb 2020 指出 FTP 與 CP 常有 **5–10% 差異**，通常 FTP 略低。
- 結論：FTP 可作 field estimate，但若要精確劃分 domain 與 interval dose，CP 更合理。

### 如何取得 CP 與 W'

### 1. Constant work rate（CWR）

- 傳統金標。
- 需多次 2–15 min 到 exhaustion 測試。
- 精準但成本高，不利常規追蹤。

### 2. 3-min all-out test

- 單次測得 CP 與 W'。
- 但 effort 依賴高、無效測試率較高，且對 cadence 敏感。

### 3. Ramp all-out test

- 可在單一 session 內同時估 **GET、CP、W'**。
- 對訓練者與運動員的週期化追蹤很有吸引力。
- 對 W' 可能略低估，解讀時要保守。

### Severe-domain interval：細節拆到獨立子頁

- 一旦功率 > `CP`，處方就不能只寫 power，還要處理 `W'` 的耗損與回補。
- 這部分已拆成 [[CP_Wprime_Interval_Design]]，避免本頁同時重複 [[Wprime_Balance_Model]] 與 [[Wprime_Recovery]] 的細節。

### 本頁只保留三個實務結論

- severe-domain interval 至少要指定：
  - work power
  - work duration
  - recovery power
  - recovery duration
- `W'BAL` 比較適合當同一受試者內的 design / tracking 工具，不適合當剩餘生理容量的絕對真值。
- 相同平均功率與總工作量，不代表相同 `W'` state；interval structure 本身就會改變後續 recovery。

### 實務應用

### Endurance athlete

- Base / recovery days：多數時間在 Z1。
- Heavy sessions：放在 LT 到 CP 之間，累積較高有氧穩定負荷。
- Interval sessions：>CP，但須控制 W' 耗損比例，避免每組都「完全榨乾」。

### 臨床 / 復健情境

- 若受試者已能安全完成 CPET，CP 可用來避免只靠 %HRmax 或 %V̇O₂peak 的粗略分區。
- 但 frail patients、HF、重症 COPD 或高跌倒風險者，不應把 exhaustive CP testing 當成 routine default。

### 方法學重點

- 每次重測前，應盡量維持相近的恢復狀態、營養狀態與 testing modality。
- 若用 TT-based CP/W' 追蹤，應先做至少一次 **familiarization**；否則重測誤差會放大，尤其是 W'。
- 若 CP / W' 來自 same-day multi-bout protocol，必須看 inter-trial recovery 多長：
  - Karsten 2016 支持短 recovery 對 `CP` 可能還行
  - 但對 `W'` 的 distortion 可能大到不適合直接拿來做 interval dose
- 長時間運動、glycogen depletion、heat stress 可使 CP 本身下降，因此 CP 不是永遠固定。
- 若用 field data 估 CP，需清楚標示其精度低於實驗室 exhaustion tests。

## 臨床表現

- 目前頁面尚未整理出可直接辨識的症狀、檢查發現或 red flags。

## 評估方式

- 目前頁面尚未整理出 History、Physical examination、Scale / test、Imaging / lab 的實際用法。

## 治療原則

### 基本三域處方

| 區域 | 生理定位 | 常見目標 |
|------|----------|----------|
| Z1 | < LT / GET | base aerobic、恢復、容量累積 |
| Z2 | LT / GET 到 CP | 提升 LT、mitochondrial adaptation、耐受 heavy work |
| Z3 | > CP | 提升 V̇O₂max、CP、severe-domain tolerance |

## 臨床決策點

- 什麼情況要治療？先看是否真的改變 pain、function、safety、participation 或訓練輸出。
- 什麼情況要轉介？遇到 red flags、診斷不確定、需要程序性介入或超出本頁可處理範圍時。
- 什麼情況不該做？當證據不足、機制不合、風險高於預期收益，或結果不會改變決策時。

## 限制與未定論

### 目前限制 / 爭議點

- W' 的生理底層不是單一系統，不能把它簡化成純 anaerobic capacity。
- W' reconstitution 的時間常數具高度個體差異，也會隨 fatigue 改變。
- 把 CP/W' 直接外推到所有團隊運動或臨床族群，仍需要情境修正。
- laboratory TT 與 TTE 的 CP 可相近，但 W' 可能不同；若處方高度依賴 W'，方法差異不能忽略。

## 理解缺口

- Training Prescription by Critical Power（以 CP 處方訓練） 量到的是什麼，不是什麼？
- 這個方法最常見的 protocol pitfall 是什麼？
- 如果結果異常，哪些情況不能直接跳到 treatment conclusion？
- 目前缺少完整評估框架：History、Physical examination、Scale / test、Imaging / lab 仍需補強。
- 目前缺少 bedside 可辨識表現：症狀、檢查發現或 red flags 仍需補強。

## 臨床使用版

- 若 Training Prescription by Critical Power（以 CP 處方訓練） 不能改變診斷、風險分層或 treatment plan，就不該例行使用。
- 先界定問題、輸入條件與輸出格式，再執行方法，否則結果很容易只有數字沒有決策價值。

## 來源

### 來源摘要連結

- [[09_來源摘要/Chorley_Lamb_2020_CP_W_reconstitution_training]]
- [[09_來源摘要/Jones_Vanhatalo_2017_critical_power_concept]]
- [[09_來源摘要/Jones_Vanhatalo_Burnley_Morton_Poole_2010_CP_exercise_tolerance]]
- [[09_來源摘要/Poole_2020_anaerobic_threshold]]
- [[09_來源摘要/Triska_2017_CP_reliability]]
- [[09_來源摘要/Skiba_Clarke_Wprime_balance_model]]
- [[09_來源摘要/Bartram_2018_Wprime_recovery_elite_cyclists]]
- [[09_來源摘要/Ferguson_2010_Wprime_recovery_after_exhaustion]]
- [[09_來源摘要/Caen_2021_Wprime_recovery_two_phase]]
- [[09_來源摘要/Caen_2019_Wprime_reconstitution_depends_on_work_and_recovery]]
- [[09_來源摘要/Lievens_2024_partial_Wprime_recovery]]
- [[09_來源摘要/Skiba_2014_work_recovery_durations_Wprime_reconstitution]]
- [[09_來源摘要/Sreedhara_2020_Modeling_Wprime_Recovery]]
- [[09_來源摘要/Karsten_2017_TT_vs_TTE_CP_Wprime]]
- [[09_來源摘要/Karsten_2016_intertrial_recovery_CP_Wprime]]
- [[09_來源摘要/Chidnok_2013_intermittent_exercise_PCr_CP]]

### 證據標記

- 來源層級：1
- evidence_level：consensus
- confidence：high

## 相關頁面

### 相關頁面

- [[Critical_Power]]
- [[CP_Wprime_Interval_Design]]
- [[Wprime_Balance_Model]]
- [[Wprime_Recovery]]
- [[CPET_Protocol_Design]]
- [[Exercise_Intensity_Domains]]
- [[VO2_Kinetics]]
- [[VO2_Slow_Component]]
- [[CP_Test_Reliability]]
- [[../05_Exercise_Physiology/PCr_Resynthesis]]
- [[../05_Exercise_Physiology/Training_Intensity_Distribution]]
- [[../09_來源摘要/Chorley_Lamb_2020_CP_W_reconstitution_training]]
- [[../09_來源摘要/Jones_Vanhatalo_2017_critical_power_concept]]
- [[../09_來源摘要/Jones_Vanhatalo_Burnley_Morton_Poole_2010_CP_exercise_tolerance]]
- [[../09_來源摘要/Chidnok_2013_intermittent_exercise_PCr_CP]]
