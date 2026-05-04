---
title: Gas Exchange Threshold（GET）
created: 2026-04-22
updated: 2026-04-25
type: concept
domain: [CPET, exercise_physiology]
tags: [gas_exchange_threshold, anaerobic_threshold, V_slope, CPET_interpretation]
sources:
  - 09_來源摘要/Poole_2020_anaerobic_threshold.md
  - 09_來源摘要/Beaver_Wasserman_Whipp_1986_V_slope_method.md
  - 09_來源摘要/Physiological_model_of_CO2_output_during_incremental_exercise.md
  - 09_來源摘要/Hirakoba_1996_excess_CO2_lactate_prediction.md
  - 09_來源摘要/Yunoki_1999_excess_CO2_kinetics.md
  - 09_來源摘要/Stringer_Wasserman_Casaburi_1995_VCO2_VO2_heavy_constant_work.md
  - 09_來源摘要/Juarez_2024_CPET_in_heart_failure.md
  - 09_來源摘要/Pezzuto_Agostoni_2023_CPET_pulmonary_hypertension.md
source_tier: 1
evidence_level: consensus
confidence: high
contested: false
contradictions: []
---

# Gas Exchange Threshold（GET）

## 一句話定義

GET 是在 ramp/incremental CPET 中，**V̇CO₂ 相對 V̇O₂ 出現非線性上升而不伴隨 frank hyperventilation** 的代謝率點，作為 [[Lactate_Threshold]] 的非侵入替代。

## 核心機制

### 操作定義（Beaver, Wasserman & Whipp 1986：V-slope method）

1. 以 V̇CO₂（y）對 V̇O₂（x）作圖（V-slope plot）。
2. 找出斜率自 <1 上凸到 >1 的 breakpoint。
3. 驗證「非 frank hyperventilation」：
   - End-tidal PCO₂（PETCO₂）此時仍**維持或略升**（不降）。
   - Ventilatory equivalent for O₂（V̇E/V̇O₂）**開始上升**。
   - Ventilatory equivalent for CO₂（V̇E/V̇CO₂）**仍穩定或略降**。
   - 此為 **isocapnic buffering region**，介於 LT 與 respiratory compensation point（RCP）之間。
4. 以 **V̇O₂ 表達** GET（不用 power/speed，因後者對 ramp-slope 敏感）。

### 為何 V-slope 比單看 ventilatory equivalents 更重要

- 它直接利用 **V̇CO2 對 V̇O2** 的關係找 breakpoint。
- 相對較不受呼吸型態與 chemosensitivity 影響。
- 也較能把 GET 與更高強度的 RC / RCP 分開。

### 機制

- 運動 >LT 後 muscle/blood HCO₃⁻ 緩衝 H⁺ → 釋放 extra CO₂。
- 此 extra CO₂ 排出，但動脈 PCO₂ 尚未下降（carotid body 對 pH 的反應相對慢）。
- 形成一段通氣增加卻 PCO₂ 恆定的 window → isocapnic buffering。
- 進一步上升至 RCP 後才出現 frank hyperventilation（PCO₂ 下降）。

### constant-work corroboration（Tier 3）

- [[../09_來源摘要/Stringer_Wasserman_Casaburi_1995_VCO2_VO2_heavy_constant_work]] 顯示：
  - heavy / very heavy constant-work exercise 中，`VCO2` 相對 `VO2` 的上翹約出現在 `40–50 s`
  - 並與 lactate 上升、standard bicarbonate 下降高度同步
- 這不能取代 ramp CPET 的 GET operational definition，
  但很有力地支持了 **buffering physiology** 這條機制線。

### 歷史性補充模型（Tier 3）

- Yano 1997 嘗試用 non-lactic V̇CO2、excess V̇CO2、PvCO2 與 PaCO2 來解釋 incremental exercise 時的 CO2 output。
- Hirakoba 1996 則在 constant exercise 顯示：excess CO2 與 blood lactate accumulation 高度相關，但在 100% AT 會高估 lactate rise。
- Yunoki 1999 進一步顯示：在短時 intensive exercise 中，excess V̇CO2 甚至可先出現負值、並在運動後才達峰，表示它明顯落後 lactate production，且受 CO2 stores 與 hyperventilation 影響。
- 這個模型可作 mechanistic teaching aid，說明高強度時 V̇CO2 同時受 venous CO2 transport、lactate-related buffering 與 hyperventilation 影響。
- 但它不是當代 GET operational definition，也不取代 V-slope 與 ventilatory equivalent framework。

### GET vs LT

- GET 略早於 LT 的真正動脈血 [La⁻] 上升點，差距來自非 bicarbonate 緩衝貢獻（Stringer 1992）。
- 臨床上差異不顯著。
- GET **效率更高的核心優勢**：non-invasive + effort-independent + 可 breath-by-breath。

### 失效情境（false negative / 解讀陷阱）

- **Ramp 太慢**：sensitivity 下降，V-slope breakpoint 不清。
- **Ramp 太快**：CO₂ storage dynamics 可讓 GET 與真實 LT 解離（Ward & Whipp 1992）。
- **無 isocapnic buffering region**：
  - 高海拔（周邊化學受器過敏）。
  - McArdle disease（無 glycolytic acidosis，但可有 hyperventilatory response）。
  - 嚴重 HF / COPD 未達 LT 即中止運動。
- **Ramp duration**：8–12 分鐘仍可當實務預設，但不是硬規則；較短或較長的 protocol 仍可能有效，前提是解讀時知道 protocol 對 breakpoint 的影響。

## 臨床表現

### 臨床應用（Tier 1 證據）

### 1. 整合性生理功能評估
- GET 絕對值 <1 L/min 或 <40% predicted V̇O₂max → 通常視為臨床異常。
- GET/V̇O₂max 隨年齡上升，女性更明顯（平均 80 歲女性 GET ≈ 64% predicted V̇O₂max）。

### 2. 訓練與復健處方
- 以 GET 為 heavy intensity 下界。
- 超過 GET 的 training 能有效誘發 LT/mitochondrial adaptation。
- 大量 olympic endurance 表現位於 >CP 範圍，僅 GET 不足以完整定位（見 [[Critical_Power]]）。

### 3. 術前風險分層（major abdominal / thoracic surgery）
- GET <11 mL/kg/min → 術後死亡風險 ↑ 4–5×（Older 1999）。
- GET <8 mL/kg/min → cardiovascular death ~8%（vs GET >14 幾乎為零）。
- GET <10.1 mL/kg/min → 廣泛併發症預測力優於 V̇O₂peak、V̇E/V̇CO₂ slope、BMI、cardiac risk index、creatinine 等（West 2016，OR 7.56; 95% CI 4.44–12.86）。
- GET <11.1 mL/kg/min → 大腸直腸手術術後死亡 AUC 0.79。

### 4. 心衰預後
- GET <11 mL/kg/min → 死亡風險 ↑ ~4×（Gitt 2002）。
- GET <8.5 或 indeterminable → 再升高（Agostoni 2013）。

### Juarez 2024：HF 中 VO2 at AT 是 prognostic marker，但不是 specific diagnosis

- Juarez et al. 2024 使用 `anaerobic threshold` 表述；在本 wiki 中應優先對應到 [[Gas_Exchange_Threshold]] / VO2 at AT 的 operational interpretation，而不要把它解讀成「肌肉缺氧點」。
- 來源描述：peak VO2 >=20 mL/kg/min、VE/VCO2 slope <30、absence of EOV、VO2 at AT >11 mL/kg/min 可形成較佳 prognosis pattern。
- 來源也描述：peak VO2 <10 mL/kg/min、VE/VCO2 slope >=36、presence of EOV、VO2 at AT <11 mL/kg/min 可形成 very poor prognosis pattern。
- 若未達 maximal effort，oxygen uptake efficiency slope <1.4 與 VO2 at AT <9 mL/kg/min 可提示 poor prognosis。
- VO2 at AT 不具 disease specificity；lung disease、anemia、myopathies、general deconditioning 皆可使 threshold 受影響。

### Pezzuto & Agostoni 2023：PH 中 AT 周邊的 VE/VCO2 / PETCO2 pattern 比單一 breakpoint 更重要

- PH / PAH 來源使用 `anaerobic threshold` 表述；本 wiki 解讀時仍應保留 GET / AT 的 operational caveat。
- PAH 中 VE/VCO2 與 VE/VO2 可在 ramp 初期不呈正常下降；moderate PAH 可 flat，severe PAH 可上升。
- VE/VCO2 slope 可能 steep 到難以辨識 respiratory compensation point 的 normal upward deflection。
- High VE/VCO2 plus low PETCO2 at AT increases likelihood of pulmonary vascular disease；both normal makes PH unlikely in the cited framework。
- 來源引用 ESC/ERS risk anchors：peak VO2 >15 mL/kg/min and VE/VCO2 slope <36 = low risk；peak VO2 11-15 and VE/VCO2 slope 36-44 = intermediate risk；peak VO2 <11 and VE/VCO2 slope >44 = high risk。
- 這些 cutoffs 屬 PH-specific risk stratification，不可直接套用到 HF、COPD 或一般 exercise prescription。

### 5. 其他響應性驗證
- Cardiac resynchronization therapy → GET 上升（Auricchio 2002）。
- Endurance training in chronic HF / lung disease → GET 上升（Casaburi 1991、Kiilavuori 1996）。
- Acute 減少 muscle O₂ delivery → GET 下降（Koike & Wasserman 1992）。

### 常見錯誤

- 只看 V̇E 而不看 V-slope → 常誤判（Poole 直接點名 Wasserman 1964 原始 ventilatory approach 的問題）。
- 將 GET 標示為「anaerobic threshold」並解讀為「肌肉缺氧」→ 機制誤用（見 [[Anaerobic_Threshold_概念史]]）。
- 把 RCP 或 deoxygenation break point 當作 CP 的替代 → 無效替代（Broxterman 2018）。

## 評估方式

- 目前頁面尚未整理出 History、Physical examination、Scale / test、Imaging / lab 的實際用法。

## 治療原則

- 本頁以概念或來源為主；若要進入真正 treatment plan，需連回對應臨床頁。

## 臨床決策點

- 什麼情況要治療？先看是否真的改變 pain、function、safety、participation 或訓練輸出。
- 什麼情況要轉介？遇到 red flags、診斷不確定、需要程序性介入或超出本頁可處理範圍時。
- 什麼情況不該做？當證據不足、機制不合、風險高於預期收益，或結果不會改變決策時。

## 限制與未定論

- 目前頁面尚未明確寫出證據限制、教材未講清楚處或不同來源可能衝突之處。

## 理解缺口

- Gas Exchange Threshold（GET） 和最相近、最常被混用的概念差在哪？
- 這個指標或概念反映的是直接機制，還是只是 operational proxy？
- 在什麼測試條件或族群下，這個概念最容易被錯用或外推失真？
- 目前缺少完整評估框架：History、Physical examination、Scale / test、Imaging / lab 仍需補強。
- 目前缺少明確處置順序：何時觀察、何時介入、何時轉介仍需補強。

## 臨床使用版

- 若要把 Gas Exchange Threshold（GET） 用在 bedside 或運動處方，先確認它回答的是哪一個機制或強度邊界，再決定能否改變評估與處置。
- 若這個概念無法改變你的臨床決策，就不要只為了名詞完整而硬套到病人身上。

## 來源

### 來源摘要連結

- [[09_來源摘要/Poole_2020_anaerobic_threshold]]
- [[09_來源摘要/Beaver_Wasserman_Whipp_1986_V_slope_method]]
- [[09_來源摘要/Physiological_model_of_CO2_output_during_incremental_exercise]]
- [[09_來源摘要/Hirakoba_1996_excess_CO2_lactate_prediction]]
- [[09_來源摘要/Yunoki_1999_excess_CO2_kinetics]]
- [[09_來源摘要/Stringer_Wasserman_Casaburi_1995_VCO2_VO2_heavy_constant_work]]
- [[09_來源摘要/Juarez_2024_CPET_in_heart_failure]]
- [[09_來源摘要/Pezzuto_Agostoni_2023_CPET_pulmonary_hypertension]]

### 證據標記

- 來源層級：1
- evidence_level：consensus
- confidence：high

## 相關頁面

### 相關頁面

- [[09_來源摘要/Poole_2020_anaerobic_threshold]]
- [[09_來源摘要/Beaver_Wasserman_Whipp_1986_V_slope_method]]
- [[09_來源摘要/Physiological_model_of_CO2_output_during_incremental_exercise]]
- [[09_來源摘要/Hirakoba_1996_excess_CO2_lactate_prediction]]
- [[09_來源摘要/Yunoki_1999_excess_CO2_kinetics]]
- [[09_來源摘要/Stringer_Wasserman_Casaburi_1995_VCO2_VO2_heavy_constant_work]]
- [[Anaerobic_Threshold_概念史]]
- [[V_Slope_Method]]
- [[Lactate_Threshold]]
- [[Critical_Power]]
- [[Exercise_Intensity_Domains]]
- [[VO2_Kinetics]]
- [[VO2_Slow_Component]]
- [[CPET_Protocol_Design]]
- [[VO2max_Measurement]]
- [[CPET_in_Heart_Failure]]
- [[CPET_in_Pulmonary_Hypertension]]
