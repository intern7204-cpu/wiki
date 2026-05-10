---
title: V̇O₂ Kinetics（氧耗動力學）
created: 2026-04-22
updated: 2026-05-09
type: concept
domain: [CPET, exercise_physiology]
tags: [VO2_kinetics, time_constant, O2_deficit, metabolic_stability, CPET_interpretation, PCr, pediatric_exercise]
sources:
  - 10_來源摘要/Goulding_2021_VO2_kinetics_exercise_tolerance.md
  - 10_來源摘要/Goulding_Marwood_2023_critical_power_determinants.md
  - 10_來源摘要/Gaesser_Poole_1996_VO2_slow_component.md
  - 10_來源摘要/Kemp_1993_PCr_resynthesis.md
  - 10_來源摘要/Modelling_the_VO2_kinetic_response_to_heavy_intensity_exercise_in_children.md
  - 10_來源摘要/Korzeniewski_Zoladz_2013_VO2_off_PCr_off_kinetics.md
  - 10_來源摘要/Zacca_2019_VO2FITTING_software.md
  - 10_來源摘要/Wooten_2021_excess_VCO2_recovery_fatigability.md
  - 10_來源摘要/Francescato_Cettolo_2021_VO2_fitting_window.md
  - 10_來源摘要/Goulding_2023_priming_exercise_VO2_kinetics.md
  - 10_來源摘要/Zhang_1991_fitness_VO2_VCO2_step_kinetics.md
  - 10_來源摘要/Geor_2000_horse_warmup_VO2_VCO2_kinetics.md
source_tier: 1
evidence_level: consensus
confidence: high
contested: false
contradictions: []
---

# V̇O₂ Kinetics

## 一句話定義

V̇O2 kinetics 描述運動開始後氧耗如何接近新平衡；其核心參數是 **τV̇O2**，也就是氧化系統追上 ATP demand 的速度。

## 核心機制

### 三相結構

| 相位 | 時間 | 主因 |
|------|------|------|
| Phase 1 | 約前 15–25 s | cardiodynamic transit |
| Phase 2 | 約 20 s 到 2–3 min | 肌肉氧化代謝逐步趕上需求 |
| Phase 3 | 之後 | moderate 時達 steady state；heavy/severe 可出現 slow component |

### τV̇O2 的意義

- τ 越小，代表在同功率下 O2 deficit 越小。
- O2 deficit 越小，Pi、ADP、H+ 等疲勞相關代謝物累積越慢。
- 因此 τV̇O2 本質上是在描述 **metabolic stability**。
- [[Critical_Threshold_Positive_Feedback_Model]] 進一步強調，在 steady-state 條件下，O2 deficit 可近似理解為 `Delta V̇O2 x tauV̇O2`；但超過穩定條件後，O2 deficit 不能再被當成單純 performance predictor。

### 與 CP 的連結

- [[Critical_Power]] 可視為系統能否把 working muscle 維持在 critical metabolite threshold 以下的結果。
- τV̇O2 越快，越能延緩 severe-domain 代謝失穩，因此 CP 越高。
- 這也是 Goulding 2021 強調的 CP 非固定常數，而是 emergent property 的原因。
- Goulding & Marwood 2023 將這點推進為三因素交互模型：tauVO2、convective O2 delivery、diffusive O2 delivery 各自可影響 CP，並共同決定 exercise transition 時 intracellular perturbation 的大小。
- 因此 tauVO2 不是只描述「反應快慢」，而是決定同一 ATP demand 下 O2 deficit、Pi accumulation、fatigue induction 與 CP 高低的核心機制變數之一。

### 與 PCr / ADP recovery 的連結

- [[../05_Exercise_Physiology/PCr_Resynthesis]] 顯示 recovery 期 PCr kinetics 直接反映 oxidative ATP synthesis。
- Kemp 1993 指出：
  - PCr recovery half-time 約 0.9 min
  - ADP recovery 約 15 s
- 這些資料與 τV̇O2 一起支持：**mitochondrial capacity 與代謝控制速度**是連在一起的，不是分離現象。
- 但 Tier 3 theoretical article（Korzeniewski 2013）提醒一個重要 caveat：
  - muscle VO2 off-kinetics 與 PCr off-kinetics 不一定是鏡像
  - 早期 VO2 off 較快，未必代表 PCr 回補也較快
  - 因此 pulmonary VO2 recovery 不應被直接等同於 intramuscular energetic recovery

### fitness 與 priming 會改變 kinetics，但證據層級不一

- [[../10_來源摘要/Zhang_1991_fitness_VO2_VCO2_step_kinetics]] 顯示：
  - 在 proportional step test 中，fitter subjects 的 `VO2 / VCO2` kinetics 較快
  - `VO2` kinetics 會隨更高工作步階逐步變慢，但 `VCO2` kinetics 不會同程度變慢
- 這提醒我們：
  - step protocol 下的 kinetics 不應被硬壓成單一固定 `tau` 敘事
  - fitness level 會改變同相對工作率下的代謝反應速度
- [[../10_來源摘要/Geor_2000_horse_warmup_VO2_VCO2_kinetics]] 則提供 comparative physiology 補充：
  - 在馬匹中，不論低或較高強度 warm-up，都可加快 `VO2 / VCO2` on-kinetics 並減少 `O2 deficit`
  - 但這是 equine treadmill data，只能當 priming physiology 的輔助訊號，不能直接當成人類 CPET 處方規則
- [[../10_來源摘要/Goulding_2023_priming_exercise_VO2_kinetics]] 把 human priming exercise 的判讀收斂成 phase-specific model：
  - prior heavy / severe exercise 後，overall VO2 response 變快不等於 `tauVO2` 一定降低
  - 真正需要區分的是 `tauVO2` lowering、fundamental amplitude increase 與 `VO2 slow component` reduction
  - baseline `tauVO2` 較慢時，priming 後較可能看到 true `tauVO2` reduction；`tauVO2 <= 25 s` 的 groups 常較不明顯
  - lactic acidosis、muscle temperature 或 O2 delivery alone 都不足以完整解釋 priming effect
  - enhanced intracellular O2 utilization 與 altered motor unit recruitment 是較有支持的機制方向，詳見 [[Priming_Exercise_and_VO2_Kinetics]]

### 方法學重點

- 需要 breath-by-breath 或足夠高頻率資料。
- 要清楚定義 baseline 與 transition。
- 若強度超過 LT，應和 [[VO2_Slow_Component]] 分開解讀。
- curve fitting 本身是方法學，不只是軟體按鈕：
  - 去 aberrant breaths
  - interpolation / binning
  - phase I 是否排除
  - mono- vs bi-exponential
  - CI 怎麼算
  都會改變 `tau` 與 `slow component` 估計。
- fitting window 應被視為 model assumption；固定移除前 `20 s` 不是中性預設，詳見 [[VO2_Kinetics_Fitting_Window]]。
- Francescato & Cettolo 2021 進一步提醒：
  - 起始資料移除多長，不是小設定
  - 在 moderate-intensity breath-by-breath data，`tau` 可因 fitting window 改變約 `30%`
  - 固定 `20 s` 只是慣例，不是 neutral default
- Zacca 2019 的 `VO2FITTING` 提供一個 open-source workflow 來標準化這些步驟，但作者也明講：軟體不能取代 physiology judgment，且當時版本對 off-transient 支援仍有限。

## 臨床表現

### 臨床或研究上的重要性

- 同樣 V̇O2max 的兩個人，τV̇O2 慢的人在短時高需求 task 上可能更快進入代謝失穩。
- Priming、training、oxygen availability 與 disease 都會改變 τV̇O2。
- 因此 τV̇O2 對 rehabilitation、exercise tolerance 與 mechanism research 都有價值。
- 但 recovery / off-kinetics 的應用仍要保守：
  - [[Estimated_Excess_VCO2_and_Performance_Fatigability]] 提示，Wooten 2021 feasibility pilot 可取得 estimated excess VCO2、recovery VCO2 off-kinetics 與 fatigability measures，且在 n=7 healthy adults 中有強 exploratory associations
  - 但該研究沒有 lactate、bicarbonate 或 pH 對照；estimated excess VCO2 仍屬 indirect、hypothesis-generating evidence，還不是 routine CPET doctrine

## 評估方式

- 目前頁面尚未整理出 History、Physical examination、Scale / test、Imaging / lab 的實際用法。

## 治療原則

- 本頁以概念或來源為主；若要進入真正 treatment plan，需連回對應臨床頁。

## 臨床決策點

- 什麼情況要治療？先看是否真的改變 pain、function、safety、participation 或訓練輸出。
- 什麼情況要轉介？遇到 red flags、診斷不確定、需要程序性介入或超出本頁可處理範圍時。
- 什麼情況不該做？當證據不足、機制不合、風險高於預期收益，或結果不會改變決策時。

## 限制與未定論

### 兒童資料與 limited-evidence caveat

- [[Pediatric_Heavy_Exercise_VO2_Kinetics_Modeling]] 提醒：兒童 heavy-intensity cycle exercise 並不代表沒有 slow-component-like behavior；Fawkner and Armstrong 2004 這篇 original article 顯示多數 healthy children 的 response profiles 不能用單一 exponential model 充分描述。
- 但 pediatric kinetics 的 secondary component 參數穩定性較差，實務上通常仍以較穩健的 phase-2 fitting window 估計 primary component。
- 舊文獻常用 TAN / anaerobic threshold 術語；整理進本 wiki 時，應優先翻譯回 [[Lactate_Threshold]]、[[Gas_Exchange_Threshold]] 與 [[Critical_Power]] 的當代框架。
- recovery kinetics 也有 similar caveat：
  - muscle-level theoretical model 顯示 VO2 off 與 PCr off 可呈 inverse relation
  - 因此不能把 recovery VO2 曲線直接當成肌肉內部 recovery 的完整替代

## 理解缺口

- V̇O₂ Kinetics 和最相近、最常被混用的概念差在哪？
- 這個指標或概念反映的是直接機制，還是只是 operational proxy？
- 在什麼測試條件或族群下，這個概念最容易被錯用或外推失真？
- 目前缺少完整評估框架：History、Physical examination、Scale / test、Imaging / lab 仍需補強。
- 目前缺少明確處置順序：何時觀察、何時介入、何時轉介仍需補強。

## 臨床使用版

- 若要把 V̇O₂ Kinetics 用在 bedside 或運動處方，先確認它回答的是哪一個機制或強度邊界，再決定能否改變評估與處置。
- 若這個概念無法改變你的臨床決策，就不要只為了名詞完整而硬套到病人身上。

## 來源

### 來源摘要連結

- [[10_來源摘要/Goulding_2021_VO2_kinetics_exercise_tolerance]]
- [[10_來源摘要/Goulding_Marwood_2023_critical_power_determinants]]
- [[10_來源摘要/Gaesser_Poole_1996_VO2_slow_component]]
- [[10_來源摘要/Kemp_1993_PCr_resynthesis]]
- [[10_來源摘要/Modelling_the_VO2_kinetic_response_to_heavy_intensity_exercise_in_children]]
- [[10_來源摘要/Korzeniewski_Zoladz_2013_VO2_off_PCr_off_kinetics]]
- [[10_來源摘要/Zacca_2019_VO2FITTING_software]]
- [[10_來源摘要/Wooten_2021_excess_VCO2_recovery_fatigability]]
- [[10_來源摘要/Francescato_Cettolo_2021_VO2_fitting_window]]
- [[10_來源摘要/Goulding_2023_priming_exercise_VO2_kinetics]]
- [[10_來源摘要/Zhang_1991_fitness_VO2_VCO2_step_kinetics]]
- [[10_來源摘要/Geor_2000_horse_warmup_VO2_VCO2_kinetics]]

### 證據標記

- 來源層級：1
- evidence_level：consensus
- confidence：high

## 相關頁面

### 相關頁面

- [[VO2_Slow_Component]]
- [[Critical_Threshold_Positive_Feedback_Model]]
- [[Estimated_Excess_VCO2_and_Performance_Fatigability]]
- [[Pediatric_Heavy_Exercise_VO2_Kinetics_Modeling]]
- [[Critical_Power]]
- [[Critical_Power_生理決定因子]]
- [[Priming_Exercise_and_VO2_Kinetics]]
- [[CPET_Protocol_Design]]
- [[VO2max_Measurement]]
- [[../05_Exercise_Physiology/PCr_Resynthesis]]
- [[../05_Exercise_Physiology/Skeletal_Muscle_Energy_Metabolism]]
- [[../10_來源摘要/Goulding_2021_VO2_kinetics_exercise_tolerance]]
- [[../10_來源摘要/Goulding_Marwood_2023_critical_power_determinants]]
- [[../10_來源摘要/Kemp_1993_PCr_resynthesis]]
- [[../10_來源摘要/Modelling_the_VO2_kinetic_response_to_heavy_intensity_exercise_in_children]]
- [[../10_來源摘要/Korzeniewski_Zoladz_2013_VO2_off_PCr_off_kinetics]]
- [[../10_來源摘要/Zacca_2019_VO2FITTING_software]]
- [[../10_來源摘要/Wooten_2021_excess_VCO2_recovery_fatigability]]
- [[../10_來源摘要/Goulding_2023_priming_exercise_VO2_kinetics]]
