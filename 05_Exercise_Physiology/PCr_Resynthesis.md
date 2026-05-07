---
title: PCr Resynthesis（phosphocreatine recovery）
created: 2026-04-23
updated: 2026-05-08
type: concept
domain: [exercise_physiology, methodology]
tags: [PCr, phosphocreatine, ADP, Pi, oxidative_phosphorylation, mitochondrial_function, 31P_MRS]
sources:
  - 09_來源摘要/Kemp_1993_PCr_resynthesis.md
  - 09_來源摘要/McMahon_Jenkins_PCr_resynthesis_after_intense_exercise.md
  - 09_來源摘要/Hargreaves_Spriet_2020_muscle_energy_metabolism.md
  - 09_來源摘要/Korzeniewski_Zoladz_2013_VO2_off_PCr_off_kinetics.md
  - 09_來源摘要/Skiba_2015_intramuscular_determinants_Wprime_recovery.md
  - 09_來源摘要/Caen_2021_Wprime_recovery_two_phase.md
source_tier: 1
evidence_level: consensus
confidence: high
contested: false
contradictions: []
---

# PCr Resynthesis（phosphocreatine recovery）

## 一句話定義

運動後 **PCr resynthesis kinetics** 是活體骨骼肌 **oxidative ATP synthesis capacity** 的重要讀出；最常用 **31P MRS** 量測，對粒線體功能與高強度恢復能力都很有價值。

## 核心機制

### 核心概念

### 為什麼 recovery 期特別適合看氧化代謝

- Recovery 期間沒有外在 mechanical work。
- [ATP] 大致維持恆定。
- Glycogenolysis 已大幅減少。
- 因此 PCr 回補速率可近似視為**淨 oxidative ATP synthesis rate**。

### Kemp 1993 的關鍵關係

- PCr resynthesis rate `R` 對 **[ADP]** 呈 **hyperbolic**。
- 估計 `Km ≈ 30 µmol/L cell water`。
- 估計 `Vmax ≈ 40 mmol/L cell water/min`。
- `R` 對 **[Pi]、[PCr]、[creatine]** 則近似**線性**。

### 時間常數的意義

- 正常肌肉中，PCr recovery half-time 約 **0.9 min**。
- ADP recovery 更快，約 **15 s**。
- 這個差異解釋了為何 `R` 對 [ADP] 呈飽和型，而對 [Pi]/[PCr] 看起來較線性。

### 為什麼 PCr recovery 常不像單一速度

- [[../09_來源摘要/McMahon_Jenkins_PCr_resynthesis_after_intense_exercise]] 整理指出，PCr resynthesis 常可見 fast + slow component。
- 早期快相較像：
  - `ADP`
  - 或 ATP hydrolysis free energy
  主導的氧化回補。
- 較慢段則更接近 intracellular `pH` 回到 homeostasis 的限制。
- 所以單一 `tau` 很有用，但它比較像 **practical summary**，不是全部生物學。

### 機制 / 原理

### Creatine kinase（CK）平衡是核心約束

`ADP + PCr + H+ <-> ATP + creatine`

- 這使得 [ADP]、[PCr]、pH 彼此耦合。
- 因此在 in vivo 系統裡，很難把單一調控因子完全分開解釋。

### 兩種經典控制觀點

1. **ADP control**
   - 粒線體 ATP synthesis 主要由 cytosolic [ADP] 驅動。
   - 與 Kemp 1993 的 hyperbolic 關係一致。
2. **Free energy / Pi-linked control**
   - 在整體系統上，也可觀察到與 [Pi]、[PCr]、ATP hydrolysis free energy 的線性相關。

實務上，兩者不是互斥，而是同一受約束系統的不同觀察角度。

### 方法學重點

### 常用量測

- **31P MRS**：非侵入、可重複。
- 常搭配 forearm 或 gastrocnemius exercise protocol。
- 用 Pi 與 PCr 訊號、chemical shift 推估：
  - [PCr]
  - [Pi]
  - intracellular pH
  - 進一步估算 [ADP]

### 讀取時要注意

- τ 或 half-time 會受運動任務、depletion 程度、酸化程度與取樣密度影響。
- 單一 τ 不是全部；最好連同起始 [PCr]、[ADP]、pH 一起解讀。

## 臨床表現

### 臨床與研究重要性

### 1. 粒線體功能評估

- PCr recovery 變慢是 **mitochondrial dysfunction** 的敏感訊號。
- 在 mitochondrial myopathy 中，Kemp 1993 顯示 R 全程下降，且對 [ADP] 的關係也變異常。

### 2. 與 V̇O₂ kinetics 的連接

- PCr 與 ADP recovery kinetics 支持 [[../04_CPET/VO2_Kinetics]] 所描述的 mitochondrial capacity 觀點。
- τV̇O₂ 與 PCr recovery 都在反映氧化系統趕上 ATP demand 的速度，只是測量層級不同。
- 但要加上一個 limited-evidence caveat：
  - Korzeniewski 2013 的 muscle model 指出，早期 VO2 off 較快時，PCr resynthesis 反而可能較慢
  - 所以 pulmonary VO2 recovery 不能被直接當成 PCr recovery 的同義替代

### 3. 與 Critical Power / W' 的連接

- [[../04_CPET/Critical_Power]] 上方運動會持續消耗 PCr、累積 Pi。
- W' reconstitution 與 PCr recovery 強相關，但 **W' 恢復通常比 PCr 更慢**，因此 W' 不等於單一 PCr 儲量。
- 這也是 [[../04_CPET/Training_Prescription_by_CP]] 中 interval recovery 必須看整體系統，而不能只看短期 PCr 的原因。
- Skiba 2015 提供了一個更直接的 MRS-based 例子（single-leg knee-extension, n=10）：
  - bulk `[PCr]` recovery half-time 約 **39 ± 16 s**（abstract `38 s`）
  - `W'` recovery half-time 約 **232 ± 108 s**（個體範圍 `135–426 s`）
  - `τ_[PCr]` 與 `τ_W'` 之間 **r = 0.38, p = 0.28**（無顯著相關）。
  - 而 `D[PCr]`（B_C 結束 [PCr] − B_E 耗竭 [PCr]，亦即「再可動員的 oxidative reserve」）與 model-predicted `W'` recovery `r = 0.99, p = 0.005`。
  - 因此 W' recovery 的較貼近指標是 `D[PCr]` / oxidative reserve，而不是把 W' 硬翻譯成「bulk PCr 回來多少」。
  - Caveat：本研究為 single-leg passive recovery、`CP ≈ 8.1 W`、最早採樣 60 s；單腳 group mean 呈線性，與 whole-body 曲線形不同；外推到 cycling / running 須保守。
- Caen 2021 的 whole-body cycling 則補上一個 practical layer：
  - exhaustion 後的 `W'` recovery 呈 fast + slow phase
  - 較快的 `VO2` kinetics 可解釋部分短休息回補
  - 但 `W'OBS` 仍高於 `W'ADJ`，表示還有其他恢復過程參與
- McMahon review 則提供了較上游的生理理由：
  - 早期回補不必完全靠 pH 已經正常化
  - 但後段恢復常不能忽略 acid-base restoration

## 評估方式

- 目前頁面尚未整理出 History、Physical examination、Scale / test、Imaging / lab 的實際用法。

## 治療原則

- 本頁以概念或來源為主；若要進入真正 treatment plan，需連回對應臨床頁。

## 臨床決策點

- 什麼情況要治療？先看是否真的改變 pain、function、safety、participation 或訓練輸出。
- 什麼情況要轉介？遇到 red flags、診斷不確定、需要程序性介入或超出本頁可處理範圍時。
- 什麼情況不該做？當證據不足、機制不合、風險高於預期收益，或結果不會改變決策時。

## 限制與未定論

### 目前限制 / 爭議點

- MRS 量到的是區域平均訊號，不能直接分辨 individual fibers。
- CK equilibrium 造成變數高度耦合，推論因果要保守。
- 不同 muscle、不同 protocol、不同 fit method 之間的 τ 不可直接硬比。
- 若只看 pulmonary recovery kinetics，就想直接推論 intramuscular PCr recovery，風險很高。

## 理解缺口

- PCr Resynthesis（phosphocreatine recovery） 和最相近、最常被混用的概念差在哪？
- 這個指標或概念反映的是直接機制，還是只是 operational proxy？
- 在什麼測試條件或族群下，這個概念最容易被錯用或外推失真？
- 目前缺少完整評估框架：History、Physical examination、Scale / test、Imaging / lab 仍需補強。
- 目前缺少明確處置順序：何時觀察、何時介入、何時轉介仍需補強。

## 臨床使用版

- 若要把 PCr Resynthesis（phosphocreatine recovery） 用在 bedside 或運動處方，先確認它回答的是哪一個機制或強度邊界，再決定能否改變評估與處置。
- 若這個概念無法改變你的臨床決策，就不要只為了名詞完整而硬套到病人身上。

## 來源

### 來源摘要連結

- [[09_來源摘要/Kemp_1993_PCr_resynthesis]]
- [[09_來源摘要/McMahon_Jenkins_PCr_resynthesis_after_intense_exercise]]
- [[09_來源摘要/Hargreaves_Spriet_2020_muscle_energy_metabolism]]
- [[09_來源摘要/Korzeniewski_Zoladz_2013_VO2_off_PCr_off_kinetics]]
- [[09_來源摘要/Skiba_2015_intramuscular_determinants_Wprime_recovery]]

### 證據標記

- 來源層級：1
- evidence_level：consensus
- confidence：high

## 相關頁面

### 相關頁面

- [[Muscle_Fiber_Types]]
- [[Skeletal_Muscle_Energy_Metabolism]]
- [[../04_CPET/VO2_Kinetics]]
- [[../04_CPET/VO2_Slow_Component]]
- [[../04_CPET/Critical_Power]]
- [[../04_CPET/Wprime_Recovery]]
- [[../04_CPET/Training_Prescription_by_CP]]
- [[../09_來源摘要/Kemp_1993_PCr_resynthesis]]
- [[../09_來源摘要/McMahon_Jenkins_PCr_resynthesis_after_intense_exercise]]
- [[../09_來源摘要/Korzeniewski_Zoladz_2013_VO2_off_PCr_off_kinetics]]
- [[../09_來源摘要/Skiba_2015_intramuscular_determinants_Wprime_recovery]]
