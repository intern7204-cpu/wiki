---
title: V-Slope Method（V-slope 法）
created: 2026-04-23
updated: 2026-04-25
type: method
domain: [CPET, methodology]
tags: [V_slope, gas_exchange_threshold, anaerobic_threshold, ramp_test, breakpoint_detection]
sources:
  - 09_來源摘要/Beaver_Wasserman_Whipp_1986_V_slope_method.md
  - 09_來源摘要/Poole_2020_anaerobic_threshold.md
  - 09_來源摘要/Physiological_model_of_CO2_output_during_incremental_exercise.md
  - 09_來源摘要/Hirakoba_1996_excess_CO2_lactate_prediction.md
  - 09_來源摘要/Yunoki_1999_excess_CO2_kinetics.md
  - 09_來源摘要/Stringer_Wasserman_Casaburi_1995_VCO2_VO2_heavy_constant_work.md
source_tier: 1
evidence_level: consensus
confidence: high
contested: true
contradictions:
  - Historical models that partition VCO2 into non-lactic and excess components may be mechanistically useful, but they do not replace standard V-slope GET detection.
---

# V-Slope Method（V-slope 法）

## 一句話定義

V-slope method 是在 incremental CPET 中，以 **V̇CO2 對 V̇O2** 的 breakpoint 來偵測 [[Gas_Exchange_Threshold]] 的方法。

## 核心機制

### 核心概念

- 在較低強度時，V̇CO2 與 V̇O2 大致線性。
- 當 lactate / H+ 增加並由 HCO3- 緩衝時，會額外產生 CO2。
- 這使 V̇CO2 相對 V̇O2 的斜率出現上移 breakpoint。

### 操作流程

1. 取得 breath-by-breath 或適度 averaging 後的 V̇O2 與 V̇CO2。
2. 以 V̇CO2（y 軸）對 V̇O2（x 軸）作圖。
3. 找出由較低斜率轉為較高斜率的 breakpoint。
4. 以 ventilatory equivalents、PETCO2 與臨床語境做交叉驗證。

### 為何比單看 ventilatory equivalents 更穩

- 較不受呼吸型態與 chemosensitivity 直接干擾。
- 不必只靠 panel visual judgement。
- 能較清楚區分：
  - GET / AT：V̇CO2 開始相對上升，但尚未 frank hyperventilation
  - RC / RCP：之後更高強度的 ventilatory compensation 點

### 方法學重點

- 最適合用在 ramp / incremental CPET。
- averaging 過重會模糊 breakpoint；過少則 noise 太大。
- 仍需回頭看 PETCO2、V̇E/V̇O2、V̇E/V̇CO2，不能把圖上的折點當自動真值。

### constant-work physiological corroboration（Tier 3）

- [[../09_來源摘要/Stringer_Wasserman_Casaburi_1995_VCO2_VO2_heavy_constant_work]] 用 arterial lactate / bicarbonate data 顯示：
  - heavy exercise 時 `VCO2` 相對 `VO2` 的上翹，確實和 buffering-related blood chemistry 同步
- 這支持 V-slope 背後不是單純圖形技巧，
  而是有實際 acid-base physiology 對應。

### 歷史性補充模型（Tier 3）

- Yano 1997 曾把 V̇CO2 拆成 non-lactic V̇CO2 與 excess V̇CO2。
- Hirakoba 1996 則把 constant exercise 的 excess CO2 拿來預測 lactate accumulation，顯示在較高強度時相關性不錯，但低一點強度就容易高估。
- Yunoki 1999 又指出：短時間 intense exercise 的 excess V̇CO2 kinetics 可明顯延後於 lactate rise，且會被 CO2 storage 與 postexercise hyperventilation 扭曲。
- 該模型強調：
  - non-lactic V̇CO2 與 mixed venous CO2 pressure 有關
  - excess V̇CO2 與 lactate rise、PaCO2 下降與 hyperventilation 有關
- 這有助於理解高強度時 V̇CO2 不只反映單一來源，但不應取代標準 GET / V-slope 判讀。

## 臨床表現

### 臨床與研究重要性

- 是 [[Gas_Exchange_Threshold]] 最常用的非侵入偵測法。
- 讓 GET 可在不抽血下納入 routine CPET。
- 在研究上有助於把 LT、GET、RCP 分成不同層次的 breakpoint。

## 評估方式

- 目前頁面尚未整理出 History、Physical examination、Scale / test、Imaging / lab 的實際用法。

## 治療原則

- 目前頁面尚未整理出 Non-pharmacologic、Pharmacologic、Injection / procedure、Rehabilitation program 的決策順序。

## 臨床決策點

- 什麼情況要治療？先看是否真的改變 pain、function、safety、participation 或訓練輸出。
- 什麼情況要轉介？遇到 red flags、診斷不確定、需要程序性介入或超出本頁可處理範圍時。
- 什麼情況不該做？當證據不足、機制不合、風險高於預期收益，或結果不會改變決策時。

## 限制與未定論

### 限制 / 爭議

- 本質上仍是 breakpoint detection，受 protocol、noise 與判讀者影響。
- 不可把 V-slope 偵測到的 GET 誤當成 [[Critical_Power]] 或 true sustainability boundary。
- 歷史上名稱常沿用 AT，但當代不應再把其機制解讀成 muscle dysoxia。
- Yano 1997 這類 mechanistic model 可作教學補充，但仍屬 Tier 3，不能升格成主框架。

## 理解缺口

- V-Slope Method（V-slope 法） 量到的是什麼，不是什麼？
- 這個方法最常見的 protocol pitfall 是什麼？
- 如果結果異常，哪些情況不能直接跳到 treatment conclusion？
- 目前缺少完整評估框架：History、Physical examination、Scale / test、Imaging / lab 仍需補強。
- 目前缺少明確處置順序：何時觀察、何時介入、何時轉介仍需補強。

## 臨床使用版

- 若 V-Slope Method（V-slope 法） 不能改變診斷、風險分層或 treatment plan，就不該例行使用。
- 先界定問題、輸入條件與輸出格式，再執行方法，否則結果很容易只有數字沒有決策價值。

## 來源

### 來源摘要連結

- [[09_來源摘要/Beaver_Wasserman_Whipp_1986_V_slope_method]]
- [[09_來源摘要/Poole_2020_anaerobic_threshold]]
- [[09_來源摘要/Physiological_model_of_CO2_output_during_incremental_exercise]]
- [[09_來源摘要/Hirakoba_1996_excess_CO2_lactate_prediction]]
- [[09_來源摘要/Yunoki_1999_excess_CO2_kinetics]]
- [[09_來源摘要/Stringer_Wasserman_Casaburi_1995_VCO2_VO2_heavy_constant_work]]

### 證據標記

- 來源層級：1
- evidence_level：consensus
- confidence：high

## 相關頁面

### 相關頁面

- [[Gas_Exchange_Threshold]]
- [[Anaerobic_Threshold_概念史]]
- [[Lactate_Threshold]]
- [[Critical_Power]]
- [[VO2max_Measurement]]
- [[../09_來源摘要/Beaver_Wasserman_Whipp_1986_V_slope_method]]
- [[../09_來源摘要/Poole_2020_anaerobic_threshold]]
- [[../09_來源摘要/Physiological_model_of_CO2_output_during_incremental_exercise]]
- [[../09_來源摘要/Hirakoba_1996_excess_CO2_lactate_prediction]]
- [[../09_來源摘要/Yunoki_1999_excess_CO2_kinetics]]
- [[../09_來源摘要/Stringer_Wasserman_Casaburi_1995_VCO2_VO2_heavy_constant_work]]
