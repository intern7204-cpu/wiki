---
title: Karsten et al. 2016 — Comparison of inter-trial recovery times for the determination of critical power and W' in cycling
created: 2026-04-25
updated: 2026-04-25
type: source_summary
domain: [CPET, exercise_physiology, methodology]
tags: [critical_power, W_prime, reliability, intertrial_recovery, time_to_exhaustion, original_article]
source_tier: 3
evidence_level: limited
confidence: medium
contested: true
contradictions:
  - Same-day shortened inter-trial recovery can preserve CP estimates while materially distorting W', so CP and W' should not be assumed to share the same recovery sensitivity.
  - One-day CP testing may be practical when CP is the endpoint, but this does not validate short-recovery W' for interval prescription.
---

# Karsten et al. 2016 — Comparison of inter-trial recovery times for the determination of critical power and W' in cycling

## 一句話定義

這篇 original article 的核心訊息是：**把 CP 測試從 24 h 壓縮到 3 h 甚至 30 min，CP 仍可接近，但 W' 會變得明顯不穩**。

## 核心機制

### 研究設計

- 9 位 moderately trained recreational cyclists。
- 先做 incremental test 取得 `pVO2max`。
- 再用 3 個 time-to-exhaustion constant-work-rate trials（`80%`、`100%`、`105% pVO2max`）估算 CP / W'。
- 比較 3 種 inter-trial recovery：
  - `24 h`
  - `3 h`
  - `30 min`
- 用 `P = W'(1/t) + CP` 線性模型計算 CP 與 W'。

### 主要發現

### 1. CP 對縮短 inter-trial recovery 相對穩定

- `CP24 ≈ 277 W`
- `CP3 ≈ 274 W`
- `CP0.5 ≈ 279 W`
- 相對於 24 h criterion protocol：
  - `3 h` protocol 平均 prediction error 約 `2.5%`
  - `30 min` protocol 平均 prediction error 約 `3.7%`

### 2. W' 明顯比 CP 更受恢復長度影響

- `W'24 ≈ 15.2 kJ`
- `W'3 ≈ 15.0 kJ`
- `W'0.5 ≈ 11.3 kJ`
- 相對於 24 h criterion protocol：
  - `3 h` protocol 平均 prediction error 約 `25.6%`
  - `30 min` protocol 平均 prediction error 約 `32.9%`
- 結論不是 W' 一定顯著下降到每次都看得出來，而是 **agreement 太寬，不夠拿來當可互換輸入值**。

### 3. practical message：one-day CP 可以，one-day W' 要保守

- 若研究或實務目標主要是 `CP`，同日測試有可行性。
- 若後續決策很仰賴 `W'`，短 recovery protocol 不應被當成和傳統 24 h protocol 等價。

## 臨床表現

### 在本 wiki 的直接價值

- 這篇最適合補進 [[../04_CPET/CP_Test_Reliability]]。
- 也直接影響 [[../04_CPET/Training_Prescription_by_CP]]：
  - 若 interval dose 很吃 `W'`，就要先問 `W'` 是怎麼測出來的。

## 評估方式

### 真正要記住的方法學點

- `CP` 與 `W'` 不只生理意義不同，**對測試恢復長度的敏感性也不同**。
- 不要把「同一套測試同時產出 CP 與 W'」誤解成兩者有相同的 measurement robustness。

## 治療原則

- 若只是做 CP-based domain anchoring，可接受較省時的一日 protocol。
- 若要用 `W'` 做 severe-domain interval prescription，應優先採較完整的 recovery 設計，或至少在同一 protocol 內追蹤，不要跨 protocol 混用。

## 臨床決策點

### 這篇真正改變什麼

- 它不是說一日測試全部無效。
- 它是在說：**同樣的 recovery shortcut，對 CP 與對 W' 的傷害不一樣。**

## 限制與未定論

### 限制 / caveat

- sample size 小。
- 受試者是 moderately trained cyclists，不能直接外推到臨床族群。
- protocol A 的 TTE 順序隨機化，但 protocol B / C 由低到高固定，可能殘留順序效應。
- 使用的是單一 `P-1/t` 模型；不同 model form 下數值可能改變。

### frontmatter contradictions

- Same-day shortened inter-trial recovery can preserve CP estimates while materially distorting W', so CP and W' should not be assumed to share the same recovery sensitivity.
- One-day CP testing may be practical when CP is the endpoint, but this does not validate short-recovery W' for interval prescription.

## 理解缺口

- 為什麼 W' 對 inter-trial recovery 的敏感度比 CP 高這麼多？
- 在不同 model family、不同熟悉化程度下，`3 h` 是否仍足以支持 reliable W'？

## 臨床使用版

- 如果你只要 `CP`，這篇支持同日 protocol 的實務吸引力。
- 如果你要 `W'`，這篇提醒你：**省時不等於可互換。**

## 來源

### 證據標記

- 來源層級：3
- evidence_level：limited
- confidence：medium

### 書目

- Karsten B, Hopker J, Jobson SA, Baker J, Petrigna L, Klose A, Beedie C.
- *Comparison of inter-trial recovery times for the determination of critical power and W' in cycling.*
- *J Sports Sci.* 2016.
- DOI: 10.1080/02640414.2016.1215500
- 類型：**original article**
- 來源等級：**Tier 3**
- 可信度：**medium**
- 原始檔：`C:\原始資料\Karstenetal.2016Comparisonofinter-trialrecoverytimes\Karstenetal.2016Comparisonofinter-trialrecoverytimes.md`

## 相關頁面

- [[../04_CPET/CP_Test_Reliability]]
- [[../04_CPET/Training_Prescription_by_CP]]
- [[../04_CPET/Wprime_Recovery]]

