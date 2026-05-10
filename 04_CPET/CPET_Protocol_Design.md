---
title: CPET Protocol Design（CPET 測試設計）
created: 2026-04-22
updated: 2026-05-08
type: method
domain: [CPET, methodology]
tags: [CPET, GXT, ramp_protocol, stage_protocol, verification_protocol, self_paced, critical_power, 3_min_all_out]
sources:
  - 10_來源摘要/Beltz_2016_GXT_protocols.md
  - 10_來源摘要/Bentley_Newell_Bishop_2007_incremental_exercise_test_design.md
  - 10_來源摘要/Poole_2020_anaerobic_threshold.md
  - 10_來源摘要/Midgley_2008_VO2max_test_duration.md
  - 10_來源摘要/Chorley_Lamb_2020_CP_W_reconstitution_training.md
  - 10_來源摘要/Poole_Jones_2017_VO2max_verification.md
  - 10_來源摘要/Pettitt_Jamnick_2017_VO2max_verification_commentary.md
  - 10_來源摘要/Lambrick_2009_RPE13_VO2max_prediction.md
  - 10_來源摘要/Wright_2017_3min_allout_CP_validity.md
  - 10_來源摘要/Juarez_2024_CPET_in_heart_failure.md
source_tier: 1
evidence_level: consensus
confidence: high
contested: true
contradictions: []
---

# CPET Protocol Design

## 一句話定義

CPET / GXT protocol 設計的重點，不是套固定模板，而是依測試目標決定 **modality、ramp slope、test duration、averaging、verification 與是否加做 CP/W' 測試**。

## 核心機制

### Modality 選擇

| Modality | 優點 | 限制 |
|----------|------|------|
| Treadmill | V̇O2peak 較高；較接近日常步行/跑步 | workload 不易量化；跌倒風險 |
| Cycle ergometer | workload 可量化；適合結合 CP/W' | V̇O2peak 較 treadmill 低 |
| Arm ergometer | 下肢受限者可用 | 整體 V̇O2peak 較低 |
| Semi-recumbent / supine cycle | 易整合影像與 hemodynamics | kinetics 可能受姿勢影響 |

### Ramp vs step

- **Ramp** 是當代預設方法，較利於觀察 V̇O2、GET、V̇E/V̇CO2 slope。
- **Step protocol** 仍可用於特定臨床問題，但 stage 太長或太短都會影響解讀。

### Stage duration 會改變你量到的是什麼

- 在 trained endurance athletes，**short stages** 常使 PPO 與 threshold 發生時的 work rate 偏高。
- **Longer stages** 較有利於 lactate / ventilatory marker 接近穩定反應，但會讓 PPO 較低。
- 因此若主要目標是 submaximal threshold interpretation，不應只為了追求較高 peak work rate 而把 stage 縮得過短。
- 若主要目標是 performance follow-up，最重要的是把 protocol 固定，而不是跨 protocol 硬比較數值。

### Test duration：8–12 min 不是硬規則

### 歷史來源

- Buchfuhrer 1983 讓「8–12 min」成為常見建議。
- 但 Midgley 2008 指出，這個 dogma 主要建立在非常有限的早期資料上。

### 當代較合理的說法

- **8–12 min 仍可作 practical default**，尤其當你同時想兼顧 V̇O2max、GET 與工作率遞增平滑性時。
- 但它**不是 validity criterion**。
- Midgley 2008 支持的較寬範圍：
  - Cycle ergometer：約 **7–26 min**
  - Treadmill：約 **5–26 min**

### 需要附帶條件

- 短測試前應有 adequate warm-up。
- Treadmill 若 grade 太高（20–25%），低 V̇O2peak 可能是坡度 intolerable，不是因為時間太長。
- 若主要目標是 threshold 與 V̇O2 kinetics，實務上仍建議避免過短或過長的極端設計。
- 在 trained athletes，3-min 甚至 5-min stages 仍可能得到有效 VO2max；但用這種 protocol 推估 LT/VT 或 PPO 時要更小心其方法學偏移。
- Pettitt & Jamnick 2017 也提醒：
  - ramp 的最高 work rate 本身受 protocol duration 影響
  - 因此 ramp slope 應個體化，不宜把 8–12 min 當純結果標籤

### Ramp slope 的實務原則

- Sedentary / frail：5–10 W/min
- 一般 active 成人：10–20 W/min
- 訓練者：20–30 W/min
- Elite：30 W/min 以上，視 modality 與目標調整

### Warm-up 與 baseline

- Cycle 通常至少 3 min unloaded baseline。
- 若要測 [[VO2_Kinetics]]，需要清楚的 baseline 與固定 workload transition。
- 若要提高後續 heavy tolerance，可加入 priming，但需明確寫進 protocol。

### Breath-by-breath averaging

- 過度 smoothing 會模糊 V̇O2 peak 與 GET breakpoint。
- 常用：
  - 5–10 breath rolling average
  - 10 s bin
  - 30 s average（臨床常見，但解析度較低）

### V̇O2max 判定

- 不應只靠 plateau、RER 或 HRmax 單一指標。
- 若目標是確認 max，應優先考慮 [[VO2max_Measurement]] 中的 **verification bout**。
- 若 `VO2max` 是 primary endpoint，Poole & Jones 2017 建議：
  - verification bout 的 work rate 應高於原 ramp peak
  - cycle ergometer 常以 **約 110% ramp peak work rate** 當 practical starting point
  - rest period 可依族群調整，healthy subjects 不一定要很長，patient populations 可較保守
- 若 verification bout 低於或只等於 ramp peak，方法學上就很難真正驗證 ceiling。
- Pettitt & Jamnick 2017 再補一個 practical rule：
  - ramp 與 verification bout 的 peak `VO2` 應放在 measurement variability 內解讀
  - 若超出合理誤差，不只要懷疑 effort，也要檢查 ramp slope / duration 是否需要重設

### 若 maximal test 暫時不適合：submaximal estimation 可作次佳方案

- Lambrick 2009 在 low-fit women 顯示，單次 ramp test 中以 `RPE 13` 的 submaximal data 外推，可得到合理的 `VO2max` estimate。
- 這種做法較適合：
  - 低適能
  - maximal burden 較高
  - 先要一個 practical fitness estimate
  的情境。
- 但輸出應寫成 **estimated VO2max / submaximal prediction**，不能和 direct measured `VO2max` 混用。

### 若目標是 CP / W'

### 選擇 1：CWR

- 研究級金標。
- 需要多次 visits。

### 選擇 2：3-min all-out

- [[Three_Minute_All_Out_Critical_Power_Test]] 單次方便，但 effort 依賴高，且不是 routine clinical CPET substitute。
- Wright 2017 顯示：
  - isokinetic `EP` 可接近 `CP`
  - linear mode 的 `EP` 則可能明顯偏高
  - `WEP` 在兩種模式都低估 `W'`
- 所以 3-min all-out 的 mode、resistance / cadence setup、familiarization、feedback policy 與 effort criteria 必須寫清楚。
- 若有 V̇O2 data，應檢查是否達到 high effort criteria，例如 >95% ramp V̇O2max 且末段沒有 decremental V̇O2 trend。
- 若 prescription 很吃 `W'`，不要用 `WEP` 直接代替。

### 選擇 3：Ramp all-out

- 可在同一 session 同時取得 GET、CP、W'。
- 對運動表現與週期化監測特別實用。

### 族群特別考量

- **HF / COPD / elderly**：以安全性、症狀限制與 hemodynamics 為先，protocol 進展可較慢。
- **Athletes**：若還要處理 severe-domain prescription，可考慮把 CP/W' 測試納入同次或後續 session。
- **Athletes / performance diagnostics**：若同時想看 PPO、LT/VT、VO2max，應先決定哪個變項是主 endpoint，因為單一 protocol 未必能同時最佳化三者。

### Juarez 2024：Heart failure 的 CPET protocol 與報告結構

- HF CPET report 可先分成四組：metabolics（VO2、VCO2、RER）、cardiac（HR、BP）、ventilation（VE、respiratory rate、dead space ventilation）、gas exchange（FiO2、SpO2、pH、PaCO2、PaO2、A-a O2 difference、lactate）。
- Clinical HF CPET 常用 incremental / ramp protocol；來源列出常見 ramp grades 包含 5、7、10、15 W/min，應依 expected exercise tolerance 選擇。
- 來源建議 ramp test 通常瞄準 8-12 min，也提到 6-12 min 可作臨床有效資訊的實務範圍；這應和本頁既有原則合併理解：duration 是設計目標，不是 validity criterion。
- Cycle ergometer 較能提供 linear workload；treadmill 較貼近日常步行，但不容易取得線性 work rate。
- HF interpretation 不能只看 protocol 是否完成；需同步記錄 symptom limitation、ECG、BP、SpO2、RER、VE/VCO2 slope、VO2 at AT、O2 pulse 與是否有 exercise oscillatory ventilation。
- HF patients 常有 pulmonary disease、anemia、sleep apnea、skeletal muscle weakness / wasting 或 deconditioning；protocol 設計與終止原因需能保留這些 differential clues。

## 臨床表現

### 常見錯誤

- 只因 test 不是 8–12 min 就直接否定 V̇O2max validity。
- 不標 averaging method 就比較不同中心數值。
- 用 %HRmax 或 %V̇O2max 直接當 domain 分界。
- 把 CP 測試與 routine frail clinical CPET 混為一談。

## 評估方式

- 目前頁面尚未整理出 History、Physical examination、Scale / test、Imaging / lab 的實際用法。

## 治療原則

- 目前頁面尚未整理出 Non-pharmacologic、Pharmacologic、Injection / procedure、Rehabilitation program 的決策順序。

## 臨床決策點

- 什麼情況要治療？先看是否真的改變 pain、function、safety、participation 或訓練輸出。
- 什麼情況要轉介？遇到 red flags、診斷不確定、需要程序性介入或超出本頁可處理範圍時。
- 什麼情況不該做？當證據不足、機制不合、風險高於預期收益，或結果不會改變決策時。

## 限制與未定論

- 目前頁面尚未明確寫出證據限制、教材未講清楚處或不同來源可能衝突之處。

## 理解缺口

- CPET Protocol Design 量到的是什麼，不是什麼？
- 這個方法最常見的 protocol pitfall 是什麼？
- 如果結果異常，哪些情況不能直接跳到 treatment conclusion？
- 目前缺少完整評估框架：History、Physical examination、Scale / test、Imaging / lab 仍需補強。
- 目前缺少明確處置順序：何時觀察、何時介入、何時轉介仍需補強。

## 臨床使用版

- 若 CPET Protocol Design 不能改變診斷、風險分層或 treatment plan，就不該例行使用。
- 先界定問題、輸入條件與輸出格式，再執行方法，否則結果很容易只有數字沒有決策價值。

## 來源

### 來源摘要連結

- [[10_來源摘要/Beltz_2016_GXT_protocols]]
- [[10_來源摘要/Bentley_Newell_Bishop_2007_incremental_exercise_test_design]]
- [[10_來源摘要/Poole_2020_anaerobic_threshold]]
- [[10_來源摘要/Midgley_2008_VO2max_test_duration]]
- [[10_來源摘要/Chorley_Lamb_2020_CP_W_reconstitution_training]]
- [[10_來源摘要/Poole_Jones_2017_VO2max_verification]]
- [[10_來源摘要/Pettitt_Jamnick_2017_VO2max_verification_commentary]]
- [[10_來源摘要/Lambrick_2009_RPE13_VO2max_prediction]]
- [[10_來源摘要/Wright_2017_3min_allout_CP_validity]]
- [[10_來源摘要/Juarez_2024_CPET_in_heart_failure]]

### 證據標記

- 來源層級：1
- evidence_level：consensus
- confidence：high

## 相關頁面

### 相關頁面

- [[VO2max_Measurement]]
- [[VO2_Kinetics]]
- [[Gas_Exchange_Threshold]]
- [[Critical_Power]]
- [[Three_Minute_All_Out_Critical_Power_Test]]
- [[CP_Test_Reliability]]
- [[Training_Prescription_by_CP]]
- [[Exercise_Intensity_Domains]]
- [[CPET_in_Heart_Failure]]
- [[../10_來源摘要/Beltz_2016_GXT_protocols]]
- [[../10_來源摘要/Bentley_Newell_Bishop_2007_incremental_exercise_test_design]]
- [[../10_來源摘要/Midgley_2008_VO2max_test_duration]]
- [[../10_來源摘要/Chorley_Lamb_2020_CP_W_reconstitution_training]]
- [[../10_來源摘要/Poole_Jones_2017_VO2max_verification]]
- [[../10_來源摘要/Lambrick_2009_RPE13_VO2max_prediction]]
- [[../10_來源摘要/Juarez_2024_CPET_in_heart_failure]]
