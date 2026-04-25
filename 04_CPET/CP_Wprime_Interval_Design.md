---
title: CP / W' Interval Design（以 CP / W' 設計 severe-domain intervals）
created: 2026-04-25
updated: 2026-04-25
type: method
domain: [CPET, exercise_physiology, training]
tags: [critical_power, W_prime, interval_training, W_BAL, severe_domain, recovery_prescription]
sources:
  - 09_來源摘要/Chorley_Lamb_2020_CP_W_reconstitution_training.md
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
evidence_level: moderate
confidence: medium
contested: true
contradictions:
  - Severe-domain interval prescription should not be reduced to average power or total work alone.
  - W'BAL is a decision-support model, not a direct measurement of a single remaining anaerobic tank.
  - Recovery between bouts is not determined only by recovery duration, because recovery power, depletion pattern, and prior work-bout characteristics also matter.
---

# CP / W' Interval Design（以 CP / W' 設計 severe-domain intervals）

## 一句話定義

以 `CP / W'` 設計 severe-domain intervals，核心不是只決定「踩多大」，而是同時規劃 **work power、work duration、recovery power、recovery duration**，並承認 `W'BAL` 只是 model-based guide。

## 核心概念

### 費曼式理解

- `CP` 像是可長時間維持的上限。
- `W'` 像是你在 `CP` 以上可以額外花掉的工作預算。
- interval design 的問題，不是「有沒有超過 `CP`」而已，而是：
  - 每組用多快速度把 `W'` 花掉
  - 組間又回來多少

### severe-domain dose 至少有四個旋鈕

- work power
- work duration
- recovery power
- recovery duration

只寫「`120% CP` 做 `6 x 2 min`」還不夠，因為 recovery 寫法不同，實際 session stress 會差很多。

### 不能只看平均功率或總工作量

- [[../09_來源摘要/Skiba_2014_work_recovery_durations_Wprime_reconstitution]] 顯示：
  - 即使 model 預測的 `W'BAL depletion` 類似
  - 不同 work / recovery structure 仍可能保留不同的實際可用 `W'`
- 所以 interval architecture 本身就是處方的一部分。

## 方法學重點

### 1. 先確認輸入值是不是可信

- `CP / W'` 從哪個 protocol 來，要先交代。
- [[../09_來源摘要/Karsten_2017_TT_vs_TTE_CP_Wprime]] 提醒：
  - `CP` 可相近
  - 但 `W'` 不一定可在 `TT` 與 `TTE` 間直接互換
- [[../09_來源摘要/Karsten_2016_intertrial_recovery_CP_Wprime]] 也提醒：
  - same-day exhaustive trials 若 inter-trial recovery 不夠
  - `W'` 比 `CP` 更容易失真

### 2. `W'BAL` 的角色是 guide，不是真值

- [[../09_來源摘要/Skiba_Clarke_Wprime_balance_model]] 支持 `W'BAL` 有實用價值，
  但它是建立在 model form 與 recovery parameter 上的估計。
- 比較合理的用途是：
  - 同一受試者內前後追蹤
  - interval design comparison
  - pacing simulation
- 不合理的用法是：
  - 把 `W'BAL = 0` 當成精確 exhaustion 秒數
  - 跨不同模型直接比較數字

### 3. recovery 不能只寫「休多久」

- [[../09_來源摘要/Sreedhara_2020_Modeling_Wprime_Recovery]] 提醒 recovery power 可能比單看 duration 更關鍵。
- [[../09_來源摘要/Ferguson_2010_Wprime_recovery_after_exhaustion]] 與 [[../09_來源摘要/Caen_2021_Wprime_recovery_two_phase]] 顯示 exhaustion 後 recovery 常呈 curvilinear，短 recovery 尤其不像單一固定 `tau`。
- [[../09_來源摘要/Lievens_2024_partial_Wprime_recovery]] 又反向提醒：
  - partial depletion 不一定需要硬套 biexponential
  - 但固定 `tau` 仍不足

### 4. 前一段 work bout 也會改變後續 recovery

- [[../09_來源摘要/Caen_2019_Wprime_reconstitution_depends_on_work_and_recovery]] 顯示：
  - recovery 不只受 recovery power / duration 決定
  - 前一段 exhaustive bout 的 intensity-duration 特性也會改變回補速度
- 實務語言就是：
  - 不能只寫「休 2 分鐘 @ 50 W」
  - 還要看前一組是怎麼把 `W'` 耗掉的

### 5. physiology 可以支持方向，但不能把 model 直接當機制本體

- [[../09_來源摘要/Chidnok_2013_intermittent_exercise_PCr_CP]] 顯示較長 recovery 伴隨更多 PCr reconstitution 與更高後續耐受。
- 但這不等於 `W' = PCr tank`，也不等於所有 interval prescription 都能用單一代謝 proxy 決定。

## 實務處方框架

### 運動員情境

- 先定義 session goal：
  - 提高 `CP`
  - 累積 heavy-domain work
  - 提高 severe-domain tolerance
  - 做 race-specific pacing rehearsal
- 然後才決定每組要耗多少 `W'`、是否允許後段品質下降、需不需要完整 recovery。

### 臨床 / 復健情境

- 若病人已能安全完成可信的 `CPET` 或 `CP/W'` assessment，`CP` 可比 `%HRmax` 或 `%VO2peak` 更貼近生理 domain。
- 但 frailty、HF、重症 COPD、neurologic instability 或高跌倒風險者，不應把 exhaustive severe-domain interval 當 routine default。

## 實務 checklist

- 先確認 `CP / W'` 來源與測試品質。
- 指定 work power 與 work duration。
- 指定 recovery power 與 recovery duration。
- 不要只看平均功率；把 interval structure 一起寫進處方。
- 若使用 `W'BAL`，固定同一 model form 與同一追蹤邏輯。
- 若 session 目標不是做到 exhaustion，就不要把每組都設計成幾乎榨乾 `W'`。

## 限制與未定論

- `W'` recovery 的最佳 model 仍未定論。
- elite athletes、一般訓練者與臨床族群可能不適合同一 recovery parameter。
- current evidence 對 short-rest interval 很多來自 cycling original articles，外推時要保守。

## 來源

### 來源摘要連結

- [[09_來源摘要/Chorley_Lamb_2020_CP_W_reconstitution_training]]
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
- evidence_level：moderate
- confidence：medium

## 相關頁面

- [[Training_Prescription_by_CP]]
- [[Critical_Power]]
- [[Wprime_Balance_Model]]
- [[Wprime_Recovery]]
- [[CP_Test_Reliability]]
- [[Exercise_Intensity_Domains]]
- [[../05_Exercise_Physiology/PCr_Resynthesis]]

