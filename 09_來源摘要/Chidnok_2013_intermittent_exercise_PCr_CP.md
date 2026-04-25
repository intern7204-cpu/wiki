---
title: Chidnok et al. 2013 — Muscle metabolic responses during high-intensity intermittent exercise measured by 31P-MRS
created: 2026-04-25
updated: 2026-04-25
type: source_summary
domain: [CPET, exercise_physiology]
tags: [critical_power, W_prime, intermittent_exercise, PCr, 31P_MRS, original_article]
source_tier: 3
evidence_level: limited
confidence: medium
contested: true
contradictions:
  - W' tolerance during intermittent exercise is not fixed at the constant-load W' value because partial recovery occurs between bouts.
  - PCr reconstitution correlates with greater W'>CP tolerance, but that does not prove W' is a pure phosphocreatine tank.
---

# Chidnok et al. 2013 — Muscle metabolic responses during high-intensity intermittent exercise measured by 31P-MRS

## 一句話定義

這篇 original article 用 `31P-MRS` 直接顯示：在 intermittent severe exercise 中，**recovery interval 越長，PCr reconstitution 越多，能完成的 `W'>CP` 也越多**；因此 constant-load 的 `W'` 不能直接當成 intermittent exercise 的固定上限。

## 核心機制

### 研究設計

- 9 位 recreationally active 男性。
- single-leg knee-extension severe exercise。
- 先用 4 次 exhaustion test 估 CP 與 W'。
- 再做 60 s work bout，穿插 18 s、30 s、48 s passive recovery，到 exhaustion 為止。
- 同步用 `31P-MRS` 追蹤 `[PCr]`、`[Pi]`、`[ADP]` 與 pH。

### 主要發現

### 1. recovery interval 越長，tolerable duration 越長

- 18 s recovery：`Tlim` 最短。
- 30 s recovery：中間。
- 48 s recovery：最長。

### 2. intermittent `W'>CP` 可大於 constant-load `W'`

- 三個 intermittent protocol 的 `W>CP` 都高於先前 constant-load 算出的 `W'`。
- recovery interval 越長，這個差距越大。
- 這表示 severe work 之間確實發生了部分 `W'` reconstitution。

### 3. PCr reconstitution 與額外可完成工作量有關

- recovery 期間 `[PCr]` 恢復量：48 s > 30 s > 18 s。
- `W>CP` 超過 constant-load `W'` 的幅度，與 recovery 間 `[PCr]` 恢復量正相關。

### 4. exhaustion 時的代謝終點相近

- 不論 recovery interval 長短，達 exhaustion 時都落在相近的 intramuscular metabolic milieu：
  - `[PCr]` 顯著下降
  - `[Pi]` 上升
  - pH 下降
- 這支持 severe-domain intolerance 與某種臨界代謝擾動有關，而不是只由外在時間長短決定。

## 臨床表現

### 這篇對 wiki 的直接價值

- 它給了 [[../04_CPET/Critical_Power]] 與 [[../04_CPET/Wprime_Balance_Model]] 一個 **muscle-metabolic anchor**。
- 也讓 [[../04_CPET/Training_Prescription_by_CP]] 的 interval prescription 更有生理依據：recovery duration 不是休息長短的小細節，而會改變可恢復的 severe-domain work capacity。

## 評估方式

- 這不是 routine clinical test。
- `31P-MRS` 屬 research-grade tool，用來理解 intermittent exercise 下的 intramuscular energetics，而不是日常處方必備檢查。

## 治療原則

- 對訓練設計的實務意義：
  - 不要把 constant-load `W'` 當成 interval session 每組都固定不變的油箱。
  - 若要讓每組都維持相近 metabolic strain，後段可能需要更長 recovery，或降低 work intensity。

## 臨床決策點

### 這篇真正改變什麼

- 它不是把 `W'BAL` 直接證實成真理。
- 它做的是更重要的事：證明 intermittent tolerance 的變化，至少部分和 recovery 期間的 PCr / metabolite restoration 有一致方向。

## 限制與未定論

### 限制 / caveat

- 小樣本、男性、單腳 knee-extension，外推到 cycling / running 要保守。
- recovery 採 passive rest，不等於一般 active recovery 設計。
- PCr correlation 很有說服力，但仍不能把 `W'` 簡化成單一 PCr 儲槽。

### frontmatter contradictions

- W' tolerance during intermittent exercise is not fixed at the constant-load W' value because partial recovery occurs between bouts.
- PCr reconstitution correlates with greater W'>CP tolerance, but that does not prove W' is a pure phosphocreatine tank.

## 理解缺口

- active recovery 與 passive recovery 的代謝回補差異有多大？
- exhaustion 的真正 limiting composite 是 `[PCr]`、`[Pi]`、pH，還是它們與 neural factors 的組合？

## 臨床使用版

- 若你在設計 severe-domain interval，這篇最值得記住的不是某個固定秒數，而是：**recovery 結構會改變可再動員的 work capacity**。
- 若你把它讀成「W' 就是 PCr」，那就讀過頭了。

## 來源

### 證據標記

- 來源層級：3
- evidence_level：limited
- confidence：medium

### 書目

- Chidnok W, DiMenna FJ, Fulford J, Bailey SJ, Skiba PF, Vanhatalo A, Jones AM.
- *Am J Physiol Regul Integr Comp Physiol* 2013;305:R1085-R1092.
- 類型：**original article**
- 來源層級：**Tier 3**
- 可信度：**medium**
- 原始檔：`C:\原始資料\Chidnoketal.AJP2013\Chidnoketal.AJP2013.md`

## 相關頁面

- [[../04_CPET/Critical_Power]]
- [[../04_CPET/Wprime_Balance_Model]]
- [[../04_CPET/Training_Prescription_by_CP]]
- [[../05_Exercise_Physiology/PCr_Resynthesis]]
- [[../05_Exercise_Physiology/Skeletal_Muscle_Energy_Metabolism]]
