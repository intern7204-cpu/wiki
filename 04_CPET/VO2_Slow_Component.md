---
title: V̇O₂ Slow Component
created: 2026-04-22
updated: 2026-05-09
type: concept
domain: [CPET, exercise_physiology]
tags: [VO2_slow_component, VO2_kinetics, constant_load_exercise, work_rate_nonlinearity, heavy_intensity, severe_intensity, muscle_efficiency, fiber_type]
sources:
  - 10_來源摘要/Gaesser_Poole_1996_VO2_slow_component.md
  - 10_來源摘要/Goulding_2021_VO2_kinetics_exercise_tolerance.md
  - 10_來源摘要/Poole_Gaesser_2025_VO2_slow_component_enigma.md
  - 10_來源摘要/Blemker_2023_fiber_type_traps.md
  - 10_來源摘要/Korzeniewski_Zoladz_2015_VO2_slow_component_mechanisms.md
  - 10_來源摘要/Ma_2010_Heaviside_VO2_kinetics_equation.md
  - 10_來源摘要/Goulding_2023_priming_exercise_VO2_kinetics.md
source_tier: 3
evidence_level: mixed_mechanistic_review_and_model_evidence
confidence: medium_high
contested: true
contradictions:
  - This hub is not anchored by a guideline-level source.
  - The VO2-work rate relation is not globally linear during constant-load exercise above GET / LT.
  - Type II fiber recruitment alone does not fully explain the VO2 slow component.
  - Model-based mechanisms such as glycolysis inhibition or rising ATP cost are useful supplements, but they are not standalone consensus proof.
  - Fixed external power does not necessarily mean unchanged internal muscular input during prolonged heavy / severe exercise.
---

# V̇O₂ Slow Component

## 一句話定義

V̇O2 slow component 是在 **>LT/GET** 的 constant-load 運動中，fundamental oxygen cost 之外額外出現、延遲上升的 V̇O2 分量，代表 **muscle efficiency 下降與代謝穩定性喪失**。

## 核心機制

### 發生條件

- 必須高於 LT / GET。
- 在 moderate domain 幾乎不出現。
- 在 heavy domain 可出現後再穩定。
- 在 severe domain 則持續把 V̇O2 推向 V̇O2max。
- [[VO2_Work_Rate_Nonlinearity_Above_GET]] 是 Gaesser and Poole 1996 的核心訊息：sub-GET 的 V̇O2-work rate linear gain 不能外推到 constant-load heavy / severe exercise。

### 機制

### 1. Constant-load 下 V̇O2-work rate 不再全域線性

- Gaesser and Poole 1996 的重點不是只命名 slow component，而是指出 fast incremental ramp 看起來 linear，不代表 constant-load exercise 全域 linear。
- 在 >GET / LT 的 constant-load exercise，slow component 讓 V̇O2 高於 sub-GET gain 推估值。
- 因此 heavy / severe intensity 不適合只用固定 %V̇O2max 當唯一 anchor，應搭配 intensity domain 與 protocol context。

### 2. 纖維募集與效率下降

- 高強度下較多快纖維募集，可能增加能量成本。
- 但這裡必須精確：**快纖維募集不等於一定低 oxidative capacity**。
- Blemker 2023 已明確指出，MHC 類別與 oxidative phenotype 不是一對一。

### 3. Pi / ADP / H+ 累積

- 代謝物累積會降低 cross-bridge 與 calcium handling 效率。
- 結果是同樣外在功率需要更多 ATP，V̇O2 因而額外上升。
- Goulding 2021 把這件事寫成一個 **positive feedback loop**：Pi 上升與效率下降互相放大，最後把系統推向 severe-domain intolerance。

### 4. 其他次要來源

- 呼吸肌、心臟工作與體溫上升會貢獻一部分，但不是主體。

### 5. 外在功率固定不等於肌肉輸入固定

- [[../10_來源摘要/Poole_Gaesser_2025_VO2_slow_component_enigma]] 是 expert Viewpoint，不是 primary experiment 或 systematic review；它適合用來標示概念邊界，不適合單獨決定 clinical prescription。
- 該文延續 Gaesser / Poole 的核心觀點：V̇O2SC 多數來源在 exercising muscle，而不是 ventilation、body temperature、lactate 或 catecholamines 的全身性代謝成本。
- 但 authors 也反對單一驅動模型：fatigue、cycling biomechanics、fiber contribution、chemical-mechanical coupling 與個體差異可能同時參與。
- 重點是：constant external power 不代表內部肌肉 force pattern、fatigue state 或 coupling efficiency 保持不變。
- 因此 V̇O2SC 最保守的解讀，是 heavy / severe exercise 中 **內部效率逐步下降的系統表徵**，不是單一分子路徑或單一纖維型態的 proxy。

### 6. priming exercise 會改變 slow component，但不能誤讀成 tau 變快

- [[../10_來源摘要/Goulding_2023_priming_exercise_VO2_kinetics]] 強調 prior heavy / severe exercise 後，overall VO2 kinetics 變快常可能來自 slow component amplitude 下降，而不是 fundamental phase `tauVO2` 真的降低。
- 若沒有把 fundamental phase 與 slow component 分開 fitting，會把 phase-amplitude change 誤判成 oxidative kinetics speed-up。
- 可能機制包含 altered motor unit recruitment、improved O2 delivery 對 slow component 的調節，以及 enhanced intracellular O2 utilization；但 residual lactic acidosis 或 muscle temperature alone 不足以解釋。

### 7. 理論模型補充（Tier 3）

- Korzeniewski 2015 提出另一種 mechanistic 補充：
  - proton accumulation 可能逐步抑制 anaerobic glycolysis
  - creatine kinase 的 ATP 支援也會慢慢下降
  - fixed power output 下 ATP cost 可能因 fatigue 而逐漸上升
- 這些變化都會迫使 oxidative phosphorylation 持續上調，形成或放大 slow component。
- 這個模型的價值是補強「代謝穩定性喪失」的解釋。
- 但它仍屬 theoretical / limited evidence，不能單獨升格成 field consensus。

### 方法學重點

- 需以 constant-load data 評估，不宜直接把 ramp 曲線偏移當成同義替代。
- 若做 model fitting，需區分 fundamental component 與 slow component。
- Ma 2010 再補一個數學層面的 caveat：
  - 若 delayed component 要在 `TD1 / TD2` 後才真正開始，
    equation implementation 應明確使用 piecewise / Heaviside gating
  - 否則 printed equation 看起來像 delayed model，實作上卻可能是 smooth sum
- 這不直接改變 physiology 解釋，
  但會影響你如何寫 code、畫圖與教模型。

### 常見誤解

- 「type 2 recruitment = slow component」太粗糙。
- 更準確的說法是：高強度募集型態、代謝物累積、fiber-specific efficiency 與 fatigue 共同造成 slow component。

## 臨床表現

### 為何重要

- 它是 heavy 與 severe domain 的定義性現象之一。
- 解釋了為何單靠固定 %V̇O2max 不足以描述高強度工作成本。
- 也是 [[Critical_Power]]、[[VO2_Kinetics]] 與肌肉 fatigue 機制之間的重要橋梁。

## 評估方式

- 目前頁面尚未整理出 History、Physical examination、Scale / test、Imaging / lab 的實際用法。

## 治療原則

- 本頁以概念或來源為主；若要進入真正 treatment plan，需連回對應臨床頁。

## 臨床決策點

- 什麼情況要治療？先看是否真的改變 pain、function、safety、participation 或訓練輸出。
- 什麼情況要轉介？遇到 red flags、診斷不確定、需要程序性介入或超出本頁可處理範圍時。
- 什麼情況不該做？當證據不足、機制不合、風險高於預期收益，或結果不會改變決策時。

## 限制與未定論

- 本頁是多來源 hub；Gaesser and Poole 1996 建立歷史脈絡與 domain definition，但機制部分已被後續研究補強與修正。
- 沒有單一機制能完整解釋所有 slow component。
- fiber recruitment、fatigue-related efficiency loss、glycolysis inhibition、ATP cost rise 可能同時參與，但不同 protocol 與族群權重不一。
- Poole / Gaesser 2025 是 Viewpoint，只能支持「不要過度單一化機制」與「注意 biomechanics / fatigue」的概念邊界；不能當作新 consensus 或臨床處方證據。
- 將 V̇O2SC 視為 muscle efficiency loss 時，仍需避免把它直接等同於單一原因，例如 type II fiber recruitment、mitochondrial P:O ratio 下降或 lactate effect。

## 理解缺口

- V̇O₂ Slow Component 和最相近、最常被混用的概念差在哪？
- 這個指標或概念反映的是直接機制，還是只是 operational proxy？
- 在什麼測試條件或族群下，這個概念最容易被錯用或外推失真？
- 目前缺少完整評估框架：History、Physical examination、Scale / test、Imaging / lab 仍需補強。
- 目前缺少明確處置順序：何時觀察、何時介入、何時轉介仍需補強。

## 臨床使用版

- 若要把 V̇O₂ Slow Component 用在 bedside 或運動處方，先確認它回答的是哪一個機制或強度邊界，再決定能否改變評估與處置。
- 若這個概念無法改變你的臨床決策，就不要只為了名詞完整而硬套到病人身上。

## 來源

### 來源摘要連結

- [[10_來源摘要/Gaesser_Poole_1996_VO2_slow_component]]
- [[10_來源摘要/Goulding_2021_VO2_kinetics_exercise_tolerance]]
- [[10_來源摘要/Poole_Gaesser_2025_VO2_slow_component_enigma]]
- [[10_來源摘要/Blemker_2023_fiber_type_traps]]
- [[10_來源摘要/Korzeniewski_Zoladz_2015_VO2_slow_component_mechanisms]]
- [[10_來源摘要/Ma_2010_Heaviside_VO2_kinetics_equation]]
- [[10_來源摘要/Goulding_2023_priming_exercise_VO2_kinetics]]

### 證據標記

- 來源層級：Tier 3 + Tier 4 + Tier 6
- evidence_level：mixed_mechanistic_review_and_model_evidence
- confidence：medium_high

## 相關頁面

### 相關頁面

- [[VO2_Kinetics]]
- [[VO2_Work_Rate_Nonlinearity_Above_GET]]
- [[Critical_Power]]
- [[Priming_Exercise_and_VO2_Kinetics]]
- [[Exercise_Intensity_Domains]]
- [[../05_Exercise_Physiology/Muscle_Fiber_Types]]
- [[../05_Exercise_Physiology/Skeletal_Muscle_Energy_Metabolism]]
- [[../10_來源摘要/Gaesser_Poole_1996_VO2_slow_component]]
- [[../10_來源摘要/Goulding_2021_VO2_kinetics_exercise_tolerance]]
- [[../10_來源摘要/Poole_Gaesser_2025_VO2_slow_component_enigma]]
- [[../10_來源摘要/Blemker_2023_fiber_type_traps]]
- [[../10_來源摘要/Korzeniewski_Zoladz_2015_VO2_slow_component_mechanisms]]
- [[../10_來源摘要/Goulding_2023_priming_exercise_VO2_kinetics]]
