---
title: V-Slope Method（V-slope 法）
created: 2026-04-23
updated: 2026-05-09
type: method
domain: [CPET, methodology]
tags: [V_slope, gas_exchange_threshold, anaerobic_threshold, ramp_test, breakpoint_detection, constant_work_rate, bicarbonate_buffering, CO2_transport]
sources:
  - 10_來源摘要/Beaver_Wasserman_Whipp_1986_V_slope_method.md
  - 10_來源摘要/Poole_2020_anaerobic_threshold.md
  - 10_來源摘要/Physiological_model_of_CO2_output_during_incremental_exercise.md
  - 10_來源摘要/Hirakoba_1996_excess_CO2_lactate_prediction.md
  - 10_來源摘要/Yunoki_1999_excess_CO2_kinetics.md
  - 10_來源摘要/Wooten_2021_excess_VCO2_recovery_fatigability.md
  - 10_來源摘要/Stringer_Wasserman_Casaburi_1995_VCO2_VO2_heavy_constant_work.md
source_tier: 4
evidence_level: high_quality_review_plus_original_method_studies
confidence: medium_high
contested: true
contradictions:
  - This method page is not anchored by a guideline-level source.
  - Historical models that partition V̇CO2 into non-lactic and excess components may be mechanistically useful, but they do not replace standard V-slope GET detection.
---

# V-Slope Method（V-slope 法）

## One-Sentence Definition

V-slope method 是在 incremental CPET 中，以 **V̇CO2 對 V̇O2** 的 slope breakpoint 來偵測 [[Gas_Exchange_Threshold]] 的方法。

## Definition and Boundary

V-slope method 的對象是 **GET / historical AT**，不是 [[Respiratory_Compensation_Point]]、不是 [[Critical_Power]]，也不是 treatment threshold 本身。它回答的是：「在 ramp / incremental exercise 中，何時開始出現 buffering-related excess CO2 output？」

原始演算法細節見 [[V_Slope_Method_Original_Algorithm]]；本頁是多來源 method hub。

## Why It Matters

- 它讓 GET 可用 non-invasive gas exchange data 估計，不必例行 arterial lactate sampling。
- 它比單看 VE / ventilatory equivalents 更靠近 buffering-related V̇CO2 signal。
- 它強迫判讀者把 GET/AT 與更高強度的 RC/RCP 分開，降低把 [[Respiratory_Compensation_Point]] 誤當 GET 的風險。

## Preconditions or Conditions

- 測試型態以 ramp / incremental CPET 最合理。
- 需要足夠品質的 breath-by-breath 或適度 averaging 後 V̇O2、V̇CO2、VE、PETCO2。
- Data processing 需避免兩個極端：過度 smoothing 會抹平 breakpoint；過少 smoothing 則 noise 過大。
- Beaver 1986 的原始演算法會排除 incremental phase 起始約 1 分鐘，因為此時 CO2 stores 造成 V̇CO2 response 較 V̇O2 慢。
- 若已進入 frank hyperventilation / RC region，V̇CO2 不再只反映 tissue CO2 production 與 bicarbonate buffering；因此 RC/RCP 應作為上界或另行標記。

- 在較低強度時，V̇CO2 與 V̇O2 大致線性。
- 當 lactate / H+ 增加並由 HCO3- 緩衝時，會額外產生 CO2。
- 這使 V̇CO2 相對 V̇O2 的斜率出現上移 breakpoint。

## Mechanism

1. Incremental exercise 逐步提高 metabolic rate。
2. 超過 lactate-related transition 後，H+ load 增加。
3. HCO3- buffering 產生 additional CO2。
4. V̇CO2 相對 V̇O2 的斜率增加。
5. Two-segment regression 的交點成為 V-slope GET/AT estimate。

## Observable Patterns

### 操作流程（conceptual workflow）

1. 取得 breath-by-breath 或適度 averaging 後的 V̇O2 與 V̇CO2。
2. 以 V̇CO2（y 軸）對 V̇O2（x 軸）作圖。
3. 找出由較低斜率轉為較高斜率的 breakpoint。
4. 以 ventilatory equivalents、PETCO2 與臨床語境做交叉驗證。

### Beaver 1986 原始方法重點（Tier 5 original article）

- [[V_Slope_Method_Original_Algorithm]] 是 Beaver / Wasserman / Whipp 1986 的單一來源概念頁。
- 10 位健康男性，cycle ergometer，4 分鐘 unloaded exercise 後 15 W/min ramp to tolerance。
- Breath-by-breath V̇O2、V̇CO2、VE、heart rate、PETCO2；另用 arterial lactate / bicarbonate data 驗證。
- Breath-by-breath data 先內插到 regular time intervals，並用 minimal moving average filter；該研究使用 9 秒。
- 作者用 PETCO2 fluctuation correction 減少 ventilation-driven V̇CO2 noise。
- 以 V̇CO2-V̇O2 兩段 linear regression 交點作 AT estimate，並用 [[Respiratory_Compensation_Point]] 作 upper boundary。
- 接受 breakpoint 需 slope change 超過預設門檻；原文使用 >0.1 以降低 noise 造成的假 breakpoint。

### Beaver 1986 主要數據

- V-slope AT mean V̇O2：1.83 +/- 0.30 L/min。
- Panel visual AT mean V̇O2：1.85 +/- 0.34 L/min；與 V-slope 差異不顯著。
- V-slope coefficient of variation：0.023 +/- 0.006；panel average：0.127 +/- 0.080。
- Gas-exchange AT 對應 lactate 比 mathematically defined LT 高 0.50 +/- 0.34 meq/L。
- V-slope AT mean V̇O2 1.83 +/- 0.30 L/min 與 estimated HCO3 threshold 1.78 +/- 0.24 L/min 無顯著差異。
- RC/RCP mean V̇O2：2.51 +/- 0.42 L/min，明顯高於 V-slope AT。

### 為何比單看 ventilatory equivalents 更穩

- 較不受呼吸型態與 chemosensitivity 直接干擾。
- 不必只靠 panel visual judgement。
- 能較清楚區分：
  - GET / AT：V̇CO2 開始相對上升，但尚未 frank hyperventilation
  - [[Respiratory_Compensation_Point]] / RCP：之後更高強度的 ventilatory compensation 點

## Clinical / Research Implication

- 臨床 CPET 報告若寫 `anaerobic threshold`，本 wiki 應優先轉譯為 operational GET，而不是 muscle dysoxia。
- 研究上應清楚報告 preprocessing、smoothing、breakpoint criteria、是否有 clear RCP，以及判讀者或演算法規則。
- V-slope 結果應作為 physiological localization / risk stratification / exercise prescription 的輸入之一，不可單獨跳到治療結論。

### constant-work physiological corroboration（Tier 5）

- [[Heavy_Constant_Work_VCO2_VO2_Inflection]] 整理 Stringer / Wasserman / Casaburi 1995 的單一來源證據。
- [[../10_來源摘要/Stringer_Wasserman_Casaburi_1995_VCO2_VO2_heavy_constant_work]] 用 arterial lactate / bicarbonate data 顯示：
  - heavy exercise 時 `V̇CO2` 相對 `V̇O2` 的上翹，確實和 buffering-related blood chemistry 同步
- 這支持 V-slope 背後不是單純圖形技巧，
  而是有實際 acid-base physiology 對應。

### 歷史性補充模型（Tier 5 original physiology studies）

- [[Incremental_Exercise_VCO2_Partitioning_Model]] 整理 Yano 1997 的單一來源模型；Yano 曾把 V̇CO2 拆成 non-lactic V̇CO2 與 excess V̇CO2。
- [[Constant_Work_Excess_CO2_Lactate_Prediction]] 整理 Hirakoba 1996 的單一來源模型；constant exercise 的 excess CO2 可預測 lactate accumulation，但在 100% AT 顯著高估。
- [[Excess_VCO2_Kinetics_Lag_After_Intensive_Exercise]] 整理 Yunoki 1999 的單一來源模型；短時間 intense exercise 的 excess V̇CO2 kinetics 可明顯延後於 lactate rise，且會被 CO2 stores 與 postexercise hyperventilation 扭曲。
- 這些 historical physiology models 強調：
  - non-lactic V̇CO2 與 mixed venous CO2 pressure 有關
  - excess V̇CO2 與 lactate rise、PaCO2 下降與 hyperventilation 有關
- 這有助於理解高強度時 V̇CO2 不只反映單一來源，但不應取代標準 GET / V-slope 判讀。
- [[Estimated_Excess_VCO2_and_Performance_Fatigability]] 整理 Wooten et al. 2021 的後續 feasibility-stage application；以 V-slope AT 作為 estimated excess VCO2 演算法錨點，探索 recovery VCO2 off-kinetics 與 performance fatigability 的關聯，但不是 GET algorithm。

## Fact

- Beaver 1986 showed V-slope AT was close to bicarbonate threshold and panel mean AT in 10 healthy men.
- Beaver 1986 showed RC/RCP was consistently higher than V-slope AT.
- V-slope method directly analyzes V̇CO2-V̇O2 rather than VE-V̇O2 alone.
- The method depends on data conditioning and breakpoint modeling choices.

## Inference

- V-slope is usually preferable to VE-only threshold detection when ventilatory control is delayed, noisy, or abnormal.
- A CPET report should document whether the detected breakpoint is GET/AT or RCP, because the physiological meaning differs.
- In contemporary teaching, V-slope supports gas-exchange threshold detection but not the old claim that AT equals a discrete muscle hypoxia point.

## Assumption

- The selected calculation window can be approximated by two linear segments.
- The slope change is caused primarily by bicarbonate-buffering-related excess CO2 before frank hyperventilation.
- The ramp protocol gives enough time resolution to locate the transition.

## Uncertainty

- Generalization from Beaver 1986 to disease cohorts is limited by small healthy-male sample size.
- Automated breakpoint detection can still fail with poor signal quality, abnormal ventilatory response, early termination, anxiety-related hyperventilation, or absent RCP.
- Historical V-slope physiology does not settle modern debates about MLSS, RCP, LT2, and [[Critical_Power]].

## Limitations and Misreadings

- 不可把 V-slope 偵測到的 GET 誤當成 [[Critical_Power]] 或 true sustainability boundary。
- 不可把 `anaerobic threshold` 字面解讀成 muscle dysoxia。
- 不可用單一 graph breakpoint 取代完整 CPET pattern recognition。
- Yano 1997 / Hirakoba 1996 / Yunoki 1999 等 historical mechanistic models 可作教學補充，但不能取代標準 GET / V-slope framework。

## 來源

### 來源摘要連結

- [[10_來源摘要/Beaver_Wasserman_Whipp_1986_V_slope_method]]
- [[10_來源摘要/Poole_2020_anaerobic_threshold]]
- [[10_來源摘要/Physiological_model_of_CO2_output_during_incremental_exercise]]
- [[10_來源摘要/Hirakoba_1996_excess_CO2_lactate_prediction]]
- [[10_來源摘要/Yunoki_1999_excess_CO2_kinetics]]
- [[10_來源摘要/Wooten_2021_excess_VCO2_recovery_fatigability]]
- [[10_來源摘要/Stringer_Wasserman_Casaburi_1995_VCO2_VO2_heavy_constant_work]]

### 證據標記

- 來源層級：Tier 4 + Tier 5 original physiology / method studies
- evidence_level：high_quality_review_plus_original_method_studies
- confidence：medium_high

## 相關頁面

### 相關頁面

- [[Gas_Exchange_Threshold]]
- [[Incremental_Exercise_VCO2_Partitioning_Model]]
- [[Constant_Work_Excess_CO2_Lactate_Prediction]]
- [[Excess_VCO2_Kinetics_Lag_After_Intensive_Exercise]]
- [[Estimated_Excess_VCO2_and_Performance_Fatigability]]
- [[V_Slope_Method_Original_Algorithm]]
- [[Heavy_Constant_Work_VCO2_VO2_Inflection]]
- [[Respiratory_Compensation_Point]]
- [[Anaerobic_Threshold_概念史]]
- [[Lactate_Threshold]]
- [[Critical_Power]]
- [[VO2max_Measurement]]
- [[../10_來源摘要/Beaver_Wasserman_Whipp_1986_V_slope_method]]
- [[../10_來源摘要/Poole_2020_anaerobic_threshold]]
- [[../10_來源摘要/Physiological_model_of_CO2_output_during_incremental_exercise]]
- [[../10_來源摘要/Hirakoba_1996_excess_CO2_lactate_prediction]]
- [[../10_來源摘要/Yunoki_1999_excess_CO2_kinetics]]
- [[../10_來源摘要/Wooten_2021_excess_VCO2_recovery_fatigability]]
- [[../10_來源摘要/Stringer_Wasserman_Casaburi_1995_VCO2_VO2_heavy_constant_work]]
