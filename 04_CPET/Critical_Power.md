---
title: Critical Power（CP）/ Critical Speed（CS）
created: 2026-04-22
updated: 2026-04-25
type: concept
domain: [CPET, exercise_physiology]
tags: [critical_power, critical_speed, W_prime, W_BAL, MLSS, exercise_intensity, intermittent_exercise, FTP]
sources:
  - 09_來源摘要/Poole_2020_anaerobic_threshold.md
  - 09_來源摘要/Jones_Vanhatalo_2017_critical_power_concept.md
  - 09_來源摘要/Jones_Vanhatalo_Burnley_Morton_Poole_2010_CP_exercise_tolerance.md
  - 09_來源摘要/Goulding_2021_VO2_kinetics_exercise_tolerance.md
  - 09_來源摘要/Chorley_Lamb_2020_CP_W_reconstitution_training.md
  - 09_來源摘要/Triska_2017_CP_reliability.md
  - 09_來源摘要/Wright_2017_3min_allout_CP_validity.md
source_tier: 1
evidence_level: consensus
confidence: high
contested: true
contradictions:
  - W' is not a direct anaerobic tank, and W'BAL outputs depend on model assumptions plus CP/W' estimation error.
  - W' recovery kinetics vary by individual and context; group-derived tau values should not be treated as universal physiology.
  - End power from a 3-min all-out test can approximate CP in some setups, but WEP should not be assumed interchangeable with W' across ergometer modes.
---

# Critical Power（CP）/ Critical Speed（CS）

## 一句話定義

Critical power 是 power-duration 關係的**漸近線**：它代表可持續的最高代謝率，同時也是 **heavy → severe** 強度域的真正生理邊界。

## 核心機制

### 數學關係

`tlim = W' / (P - CP)`

- `tlim`：在某個 `P > CP` 的 power 下可持續到 exhaustion 的時間。
- `CP`：critical power。
- `W'`：**work capacity above CP**；是 severe-domain 內可容忍的有限工作量。

### W' 的正確解讀

- W' 不是單純的「anaerobic tank」。
- 它更接近 **PCr 降低、Pi/ADP/H+ 累積、O2 deficit、neuromuscular fatigue** 等多系統共同形成的 operational construct。
- 因此 W' 可以和 PCr recovery 強相關，但**不等於**單一 PCr 容量或單一 glycolytic capacity。

### 生理意義

### CP 與 GET/LT、V̇O2max 的關係

- CP **不是** [[Gas_Exchange_Threshold]] / [[Lactate_Threshold]]。
- LT/GET 定義的是 moderate-heavy 邊界；CP 定義的是 heavy-severe 邊界。
- CP 也**不是** V̇O2max；它常發生在低於 V̇O2max 的代謝率，但任何 >CP 的 constant-load work 都會把系統推向 V̇O2max。
- 這也是為什麼 CP 比單用 %V̇O2max 更能描述 exercise tolerance。

### 在 CP 以下（heavy，>LT/GET 但 <CP）

- V̇O2 與 lactate 雖可上升，但仍可能達到 delayed steady state。
- PCr、Pi、pH 的變化可穩定在次大值。
- 可持續時間通常明顯長於 severe domain。

### 在 CP 以上（severe）

- V̇O2 會被推向 V̇O2max，系統不再維持 steady state。
- PCr 持續下降、Pi 持續升高、pH 持續下降。
- 耗竭時間由 `P - CP` 和可用 `W'` 共同決定。

### 為何 CP 比 AT/LT 更接近「可持續 vs 不可持續」的原始問題

- [[Lactate_Threshold]] / [[Gas_Exchange_Threshold]] 是 **moderate → heavy** 的邊界。
- 但 heavy domain 仍可維持 steady state，所以並不是「不可持續」。
- 真正把 sustainable 與 unsustainable 分開的，是 **CP/CS**。

### 測量方法與假設

### 1. Constant work rate（CWR）

- 傳統金標。
- 需多次 2–15 min 至 exhaustion 的測試，再做 power-duration 擬合。
- 二參數 CP/W' 模型最合理的適用範圍，也主要落在這個 severe-domain 時窗。
- 優點是概念最直接；缺點是成本高、受動機與恢復狀態影響大。

### 2. 3-min all-out test

- 單次可估 CP 與 W'。
- `end-test power` 在部分 setup 可接近 CP，但對 effort、cadence 與 pacing 很敏感。
- Wright 2017 提醒：
  - `EP` 可在部分 mode 接近 `CP`
  - `WEP` 不應直接視為可靠的 `W'` 等價物
- 所以 3-min all-out 可以是 `CP` 的 shortcut，但不是 `W'` 的通用 shortcut。

### 3. Ramp all-out test

- 可在單一 session 中同時取得 GET、CP、W'。
- 對訓練場景很實用。
- 但由於 ramp 初段存在 aerobic lag，W' 可能被略低估。

### 4. 模型假設不能忽略

- CP 並非永遠固定不變。
- 長時間運動、glycogen depletion、heat stress、cadence 操作都可能讓 CP 下移。
- 因此 CP 最好視為**特定測試條件下的系統性質**，不是不可動搖的生理常數。

### τV̇O2、PCr 與 CP 的機制連結

- [[VO2_Kinetics]] 越快，代表同功率下 O2 deficit 越小，Pi/ADP 累積越慢。
- Goulding 2021 的觀點是：CP 反映系統是否能把 working muscle 維持在 **critical metabolite threshold** 以下。
- [[../05_Exercise_Physiology/PCr_Resynthesis]] 補充：recovery 期的 PCr kinetics 可作為 oxidative ATP synthesis capacity 的讀出。

### W' reconstitution：主題另立頁

- recovery 只有在 power 下降到 `CP` 以下時才會真正發生，而且受 recovery power、duration、depletion pattern 與個體差異共同影響。
- `W'` recovery 慢於 bulk `PCr` recovery，表示它不是單一 phosphagen tank。
- `W'BAL` 可做實務估計，但不是直接量到的剩餘容量。
- 細節已拆到：
  - [[Wprime_Recovery]]
  - [[Wprime_Balance_Model]]
  - [[CP_Wprime_Interval_Design]]

### FTP vs CP

- FTP 是實務 proxy，不是生理邊界本身。
- CP 才比較接近 heavy-severe boundary。
- 若目標是區分 Z2 與 Z3、或處方 >CP intervals，應優先使用 CP。

## 臨床表現

### 臨床與研究意義

- 對運動員：CP 是 pacing、training prescription、intermittent design 的核心參數。
- 對復健/心肺患者：若測試安全可行，CP 比單靠 %HRmax 或 %V̇O2peak 更能描述真正的代謝負荷邊界。
- 對研究：CP 連接了 power-duration 現象、V̇O2 kinetics、PCr/Pi 動力學與疲勞整合機制。

## 評估方式

### 測試可靠性

- CP 通常比 W' 更穩定。
- 若用 laboratory time-trial protocol 追蹤 CP / W'，**familiarization** 應視為必要步驟之一。
- 在已熟悉 protocol 的 trained triathletes，TT-derived CP 重測 CoV 可約 2%–3%；W' 仍常約 8% 或更高。
- 因此臨床或訓練現場看到小幅 W' 變動時，不宜直接當成真實生理變化。

## 治療原則

- 本頁以概念或來源為主；若要進入真正 treatment plan，需連回對應臨床頁。

## 臨床決策點

- 什麼情況要治療？先看是否真的改變 pain、function、safety、participation 或訓練輸出。
- 什麼情況要轉介？遇到 red flags、診斷不確定、需要程序性介入或超出本頁可處理範圍時。
- 什麼情況不該做？當證據不足、機制不合、風險高於預期收益，或結果不會改變決策時。

## 限制與未定論

- 目前頁面尚未明確寫出證據限制、教材未講清楚處或不同來源可能衝突之處。

## 理解缺口

- Critical Power（CP）/ Critical Speed（CS） 和最相近、最常被混用的概念差在哪？
- 這個指標或概念反映的是直接機制，還是只是 operational proxy？
- 在什麼測試條件或族群下，這個概念最容易被錯用或外推失真？
- 目前缺少明確處置順序：何時觀察、何時介入、何時轉介仍需補強。

## 臨床使用版

- 若要把 Critical Power（CP）/ Critical Speed（CS） 用在 bedside 或運動處方，先確認它回答的是哪一個機制或強度邊界，再決定能否改變評估與處置。
- 若這個概念無法改變你的臨床決策，就不要只為了名詞完整而硬套到病人身上。

## 來源

### 來源摘要連結

- [[09_來源摘要/Poole_2020_anaerobic_threshold]]
- [[09_來源摘要/Jones_Vanhatalo_2017_critical_power_concept]]
- [[09_來源摘要/Jones_Vanhatalo_Burnley_Morton_Poole_2010_CP_exercise_tolerance]]
- [[09_來源摘要/Goulding_2021_VO2_kinetics_exercise_tolerance]]
- [[09_來源摘要/Chorley_Lamb_2020_CP_W_reconstitution_training]]
- [[09_來源摘要/Kemp_1993_PCr_resynthesis]]
- [[09_來源摘要/Triska_2017_CP_reliability]]
- [[09_來源摘要/Wright_2017_3min_allout_CP_validity]]
- [[09_來源摘要/Skiba_Clarke_Wprime_balance_model]]
- [[09_來源摘要/Sreedhara_2019_power_energy_models]]
- [[09_來源摘要/Bartram_2018_Wprime_recovery_elite_cyclists]]
- [[09_來源摘要/Chidnok_2013_intermittent_exercise_PCr_CP]]

### 證據標記

- 來源層級：1
- evidence_level：consensus
- confidence：high

## 相關頁面

### 相關頁面

- [[Training_Prescription_by_CP]]
- [[CP_Wprime_Interval_Design]]
- [[Wprime_Balance_Model]]
- [[CP_Test_Reliability]]
- [[Exercise_Intensity_Domains]]
- [[VO2_Kinetics]]
- [[VO2_Slow_Component]]
- [[CPET_Protocol_Design]]
- [[../05_Exercise_Physiology/PCr_Resynthesis]]
- [[../05_Exercise_Physiology/Skeletal_Muscle_Energy_Metabolism]]
- [[../09_來源摘要/Poole_2020_anaerobic_threshold]]
- [[../09_來源摘要/Jones_Vanhatalo_2017_critical_power_concept]]
- [[../09_來源摘要/Jones_Vanhatalo_Burnley_Morton_Poole_2010_CP_exercise_tolerance]]
- [[../09_來源摘要/Goulding_2021_VO2_kinetics_exercise_tolerance]]
- [[../09_來源摘要/Chorley_Lamb_2020_CP_W_reconstitution_training]]
- [[../09_來源摘要/Kemp_1993_PCr_resynthesis]]
- [[../09_來源摘要/Skiba_Clarke_Wprime_balance_model]]
- [[../09_來源摘要/Chidnok_2013_intermittent_exercise_PCr_CP]]
