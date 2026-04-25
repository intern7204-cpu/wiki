---
title: Hirakoba et al. 1996 — Prediction of Blood Lactate Accumulation from Excess CO2 Output during Constant Exercise
created: 2026-04-25
updated: 2026-04-25
type: source_summary
domain: [CPET, exercise_physiology, methodology]
tags: [lactate, excess_CO2, bicarbonate_buffering, constant_exercise, historical_model, original_article]
source_tier: 3
evidence_level: limited
confidence: medium
contested: true
contradictions:
  - Correlation between excess CO2 and blood lactate does not rescue the original anaerobic-threshold dysoxia model as a modern consensus explanation.
  - This constant-work exercise prediction approach is a historical mechanistic supplement, not a replacement for contemporary GET or LT interpretation.
---

# Hirakoba et al. 1996 — Prediction of Blood Lactate Accumulation from Excess CO2 Output during Constant Exercise

## 一句話定義

這篇 original article 嘗試用 **constant exercise 時的 excess CO2 output** 去預測 blood lactate accumulation；結果在較高強度（120% 與 150% AT）相對接近，但在 100% AT 會明顯高估，因此只能當成 historical buffering-based model，不能升格成現代 GET / LT 主框架。

## 核心機制

### 研究設計

- 8 位健康男性。
- 先做 incremental cycle test，估 `AT-VO2` 與 `VCO2-VO2` regression line。
- 再做 3 段各 4 分鐘 constant exercise：
  - 100% AT
  - 120% AT
  - 150% AT
- 用 total `VCO2` 減去作者定義的 aerobic `VCO2`，估算 excess CO2。
- 再用 excess CO2 / body mass 去推算 lactate accumulation。

### 主要發現

### 1. excess CO2 隨強度與 lactate rise 一起上升

- 從 stage I 到 III，Ex CO2 / kg 持續增加。
- measured lactate accumulation 也同步增加。

### 2. predicted lactate 和 measured lactate 高度相關

- `r = 0.954`
- 代表這個簡化模型在高強度下抓到某種一致方向。

### 3. 但在接近 AT 的 stage I 會系統性高估

- 100% AT 時 predicted lactate 顯著高於 measured lactate。
- 120% 與 150% AT 時差距較小。

費曼式理解：
- 作者假設「多出來的 CO2」大多來自 bicarbonate buffering of lactic acid。
- 這在更高強度時比較像樣。
- 但靠近 threshold 時，事情沒有這麼乾淨，模型就開始高估。

## 臨床表現

### 這篇對 wiki 的直接價值

- 可補強 [[../04_CPET/Gas_Exchange_Threshold]] 與 [[../04_CPET/V_Slope_Method]] 的 historical supplement。
- 它說明：`VCO2` 與 lactate 確實有關，但這種關聯不足以把舊的 anaerobic-threshold 機制直接保留下來。

## 評估方式

- 本文方法依賴：
  - 先前 incremental regression line
  - old-style AT framework
  - constant-work design
- 不屬現代 routine CPET 的標準判讀流程。

## 治療原則

- 不適合作為現代 exercise prescription 的主方法。
- 若放進知識庫，較合理的位置是「歷史機制補充」，而不是「現行實務」。

## 臨床決策點

### 這篇真正改變什麼

- 它不是在告訴你新的 threshold gold standard。
- 它真正有用的地方，是讓人看到：buffering-related CO2 excess 和 lactate accumulation 的確有可量化關聯，但這個關聯會受強度區間與模型假設影響。

## 限制與未定論

### 限制 / caveat

- 小樣本、舊 AT framing、cycle ergometer。
- 4 分鐘 constant-work stage 不一定反映更長時間 steady state。
- 「excess CO2 = lactate buffering」本身就是當代已降階的 historical idea。

### frontmatter contradictions

- Correlation between excess CO2 and blood lactate does not rescue the original anaerobic-threshold dysoxia model as a modern consensus explanation.
- This constant-work exercise prediction approach is a historical mechanistic supplement, not a replacement for contemporary GET or LT interpretation.

## 理解缺口

- 接近 LT / GET 時，哪些 CO2 kinetics 讓 prediction 失真？
- 這種 constant-work excess CO2 approach 跟 Yano 1997 的 incremental model 可怎麼互補？

## 臨床使用版

- 若你想教學「為什麼高強度時 VCO2 常跟 lactate rise 一起走」，這篇可以當 historical example。
- 若你想用它取代現代 GET / LT framework，就不對了。

## 來源

### 證據標記

- 來源層級：3
- evidence_level：limited
- confidence：medium

### 書目

- Hirakoba K, Maruyama A, Misaka K.
- *Applied Human Science* 1996;15(5):205-210.
- 類型：**original article**
- 來源層級：**Tier 3**
- 可信度：**medium**
- 原始檔：`C:\原始資料\La prediction from excess CO2\La prediction from excess CO2.md`

## 相關頁面

- [[../04_CPET/Gas_Exchange_Threshold]]
- [[../04_CPET/V_Slope_Method]]
- [[Physiological_model_of_CO2_output_during_incremental_exercise]]
- [[Poole_2020_anaerobic_threshold]]
