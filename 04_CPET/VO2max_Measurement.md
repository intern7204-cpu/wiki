---
title: V̇O₂max 測量與判定
created: 2026-04-22
updated: 2026-04-25
type: method
domain: [CPET, methodology]
tags: [VO2max, VO2peak, plateau, verification_protocol, HRmax, RER, test_duration]
sources:
  - 10_來源摘要/Beltz_2016_GXT_protocols.md
  - 10_來源摘要/Bentley_Newell_Bishop_2007_incremental_exercise_test_design.md
  - 10_來源摘要/Midgley_2008_VO2max_test_duration.md
  - 10_來源摘要/Poole_Jones_2017_VO2max_verification.md
  - 10_來源摘要/Pettitt_Jamnick_2017_VO2max_verification_commentary.md
  - 10_來源摘要/Lambrick_2009_RPE13_VO2max_prediction.md
  - 10_來源摘要/Juarez_2024_CPET_in_heart_failure.md
source_tier: 1
evidence_level: consensus
confidence: high
contested: true
contradictions:
  - VO2peak should not be used as interchangeable with VO2max when objective validation of maximal aerobic capacity matters.
  - Secondary criteria such as HRmax, RER, or blood lactate cannot serve as universal stand-alone VO2max validation rules.
  - Agreement between ramp and verification bouts should be interpreted against measurement variability and protocol design, not as a purely binary plateau substitute.
---

# V̇O₂max 測量與判定

## 一句話定義

**V̇O2max** 是個體可達的最高氧氣攝取率；若某次測試只拿到最高觀察值、但未證明已達真正上限，應報為 **V̇O2peak**。

## 核心機制

### V̇O2max vs V̇O2peak

- **V̇O2max**：有 plateau 或 verification 等證據支持已達生理上限。
- **V̇O2peak**：該次測試中的最高值，但不保證已到真正上限。
- Poole & Jones 2017 的核心主張更嚴格：
  - 若研究或臨床問題要的是真正 ceiling，不能只用 `V̇O2peak` 這個標籤掩蓋「其實沒有驗證」。

### 傳統次級標準的問題

| 指標 | 常見 cut-off | 限制 |
|------|--------------|------|
| Plateau | ΔV̇O2 ≤ 150 mL/min | 出現率很不穩定 |
| HRmax | 接近公式預測值 | 公式誤差大 |
| RER | ≥1.10 或 1.15 | 受努力與族群影響 |
| Blood lactate | ≥8 或 10 mM | 變異很大 |
| RPE | ≥17 | 主觀性高 |

結論：**任何單一次級標準都不夠。**
- Poole & Jones 2017 直接提醒：這些次級標準可能造成 **30–40%** 的真實 `V̇O2max` 低估，尤其在 test-naive、elderly、children 與 clinical populations 更明顯。

### Test duration 的當代解讀

### 反對論點

- 傳統上常把「8–12 min」視為 valid V̇O2max 的必要條件。

### 反駁

- Midgley 2008 指出，這主要追溯到 Buchfuhrer 1983 的極有限資料。
- 後續研究顯示：
  - cycle test 約 **7–26 min**
  - treadmill 約 **5–26 min**
  也都可能得到 valid V̇O2max。

### 結論

- **8–12 min 可以保留作預設設計，但不能當硬性判生死的標準。**
- 若測試略短或略長，不能單憑 duration 就否定結果。

### Protocol purpose 會改變 duration 的最佳化方向

- 在 trained endurance athletes，較長 stage 可改善 LT/VT 等 submaximal marker 的解讀，但可能降低 PPO。
- 因此「對 threshold 最好的 protocol」與「對 VO2max / peak work rate 最好的 protocol」不一定相同。
- 若目標是 longitudinal comparison，應優先維持相同 protocol，而不是跨 protocol 追求名義上的最佳 duration。

### Verification protocol（當代較佳做法）

### 流程

1. 做完 GXT。
2. 休息 5–15 min（或 protocol 指定的短暫 active recovery）。
3. 再做一段 supramaximal constant-load bout。
4. 若 verification V̇O2peak 沒超過原 GXT 的合理誤差範圍，則支持原值為 V̇O2max。
- Poole & Jones 2017 常用的 practical starting point 是：
  - **約 110%** 的 ramp test peak work rate
  - 重點不是死守 110%，而是 verification bout 必須 **高於** 原 ramp test 的最高 work rate
- Pettitt & Jamnick 2017 補了一個實務 caveat：
  - ramp 與 verification bout 的 peak `VO2` 可用 measurement variability 來解讀
  - practical 例子是差異約在 `3%` 內即可接受
  - 若差異超出，除了懷疑 effort，也要回頭檢查 ramp slope 與 duration 是否設計失當

### 意義

- 對 cycle test 特別重要，因 plateau 缺失很常見。
- 對臨床或病患族群，也常比死守 plateau 更實際。
- 若 verification bout 的 work rate 沒有高於原 ramp peak，技術上就無法真正驗證 ceiling。
- 若 verification 沒通過，下一步不一定只是「判定失敗」；
  有時更合理的是重設 ramp slope，讓下一次 ramp duration 回到較合適範圍。

### 若 maximal test 不適合：submaximal estimation 是 fallback，不是替身

- [[../10_來源摘要/Lambrick_2009_RPE13_VO2max_prediction]] 在 low-fit women 顯示：
  - 單次 ramp test 中，做到 `RPE 13` 的 submaximal data 就可能合理估計 `VO2max`
  - 而且 `RPE` 可能比 `HR alone` 更有幫助
- 但這類方法的正確定位是：
  - **estimated cardiorespiratory fitness**
  - 不是已被 verification 的 true `VO2max`
- 若研究或臨床問題需要 ceiling，仍應優先回到 maximal test + verification framework。

### Juarez 2024：HF 中多數情況應報 peak VO2，而不是硬稱 VO2max

- HF patients 常因 cardiac output reserve、pulmonary comorbidity、muscle fatigue、deconditioning 或 symptom limitation 而無法達到 true VO2max；臨床報告常用 peak VO2。
- 解讀 peak VO2 前要先確認 effort quality；RER >1.0-1.1 支持 maximal physiologic effort。
- HR >85% predicted 可輔助判斷 effort，但在 beta blockers 或 chronotropic incompetence 下可靠性下降。
- 來源整理的 HF risk anchors 包含：peak VO2 <14 mL/kg/min 為 poor prognosis marker；beta blocker patients 可用 <12 mL/kg/min；peak VO2 <=10 mL/kg/min 屬最差 prognosis pattern；% predicted peak VO2 <50% 也提示 poor prognosis。
- Peak VO2 >=20 mL/kg/min 若合併 VE/VCO2 slope <30、absence of EOV、VO2 at AT >11 mL/kg/min，來源描述為較佳 prognosis pattern。
- 這些 cutoffs 是 review-level risk stratification anchors；advanced HF / transplant decisions 仍需 current guideline、center policy、comorbidity 與 full clinical picture。

### 實務流程

1. 校正 flow 與 gas。
2. 取得穩定 baseline。
3. 根據族群與目標選擇 individualized ramp。
4. 記錄 peak symptoms、ECG、BP、HR、SpO2。
5. 必要時加做 verification。
6. 報告時明確標示：
   - V̇O2peak 數值
   - 是否通過 verification
   - 最終應報 V̇O2max 或僅報 V̇O2peak

### 報告重點

- absolute 與 relative V̇O2
- % predicted
- peak work rate / speed
- HR response 與 HR recovery
- symptoms / limitation category
- 若有 verification，必須寫進 report

### 常見 pitfalls

- 只因無 plateau 就一律否定 max。
- 只因 duration 不在 8–12 min 就判 invalid。
- 沒寫 averaging method。
- 用 220-age 當唯一 HRmax 參照。
- 把 submaximal prediction 直接報成 measured `VO2max`。

## 臨床表現

- 目前頁面尚未整理出可直接辨識的症狀、檢查發現或 red flags。

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

- V̇O₂max 測量與判定 量到的是什麼，不是什麼？
- 這個方法最常見的 protocol pitfall 是什麼？
- 如果結果異常，哪些情況不能直接跳到 treatment conclusion？
- 目前缺少完整評估框架：History、Physical examination、Scale / test、Imaging / lab 仍需補強。
- 目前缺少明確處置順序：何時觀察、何時介入、何時轉介仍需補強。

## 臨床使用版

- 若 V̇O₂max 測量與判定 不能改變診斷、風險分層或 treatment plan，就不該例行使用。
- 先界定問題、輸入條件與輸出格式，再執行方法，否則結果很容易只有數字沒有決策價值。

## 來源

### 來源摘要連結

- [[10_來源摘要/Beltz_2016_GXT_protocols]]
- [[10_來源摘要/Bentley_Newell_Bishop_2007_incremental_exercise_test_design]]
- [[10_來源摘要/Midgley_2008_VO2max_test_duration]]
- [[10_來源摘要/Poole_Jones_2017_VO2max_verification]]
- [[10_來源摘要/Pettitt_Jamnick_2017_VO2max_verification_commentary]]
- [[10_來源摘要/Lambrick_2009_RPE13_VO2max_prediction]]
- [[10_來源摘要/Juarez_2024_CPET_in_heart_failure]]

### 證據標記

- 來源層級：1
- evidence_level：consensus
- confidence：high

## 相關頁面

### 相關頁面

- [[CPET_Protocol_Design]]
- [[VO2_Kinetics]]
- [[Critical_Power]]
- [[Gas_Exchange_Threshold]]
- [[CPET_in_Heart_Failure]]
- [[Exercise_Intensity_Domains]]
- [[../10_來源摘要/Beltz_2016_GXT_protocols]]
- [[../10_來源摘要/Bentley_Newell_Bishop_2007_incremental_exercise_test_design]]
- [[../10_來源摘要/Midgley_2008_VO2max_test_duration]]
- [[../10_來源摘要/Poole_Jones_2017_VO2max_verification]]
- [[../10_來源摘要/Lambrick_2009_RPE13_VO2max_prediction]]
- [[../10_來源摘要/Juarez_2024_CPET_in_heart_failure]]
