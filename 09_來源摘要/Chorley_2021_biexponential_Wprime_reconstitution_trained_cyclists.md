---
title: Chorley et al. 2021 — Bi-exponential modelling of W' reconstitution kinetics in trained cyclists
created: 2026-04-25
updated: 2026-04-25
type: source_summary
domain: [CPET, exercise_physiology, training]
tags: [W_prime, recovery, biexponential, trained_cyclists, ramp_test, original_article]
source_tier: 3
evidence_level: limited
confidence: medium
contested: true
contradictions:
  - In trained cyclists after repeated maximal ramp exercise, a bi-exponential model fit W' reconstitution better than a mono-exponential model, but this does not prove a universal two-phase recovery law.
  - Repeated bouts mainly slowed the slow component rather than changing component amplitudes, reinforcing that W' recovery is context and state dependent.
---

# Chorley et al. 2021 — Bi-exponential modelling of W' reconstitution kinetics in trained cyclists

## 一句話定義

這篇 original article 的核心訊息是：**在 trained cyclists、 repeated maximal ramp context 下，`W'` reconstitution 比 monoexponential 更像 fast + slow 兩相，而且第二次 recovery 主要是 slow component 變慢。**

## 核心機制

### 研究設計

- 10 位 trained cyclists。
- 以 repeated ramp-to-limit protocol 測 `W'` reconstitution。
- recovery duration 橫跨 `15–360 s`，受試者完成 `5–9` 次測試。
- 比較：
  - monoexponential
  - biexponential

### 主要發現

### 1. group mean data 明顯偏向 biexponential

- bi-exponential model 的 fit 優於 monoexponential。
- group mean 的 adjusted `R^2` 幾乎接近 `1.0`。
- 代表在這個 protocol 下，用單一 `tau` 描述 `W'` 回補過程太粗。

### 2. 第一段 recovery 可拆成 fast + slow 兩部分

- fast component amplitude 約 `50.7%`
- slow component amplitude 約 `49.3%`
- 第一段 recovery：
  - `tau_FC ≈ 21.5 s`
  - `tau_SC ≈ 388 s`

### 3. repeated bout 後主要是 slow component 變慢

- 第二段 recovery 的 fast component 變化不大。
- 但 slow component `tau` 拉長到約 `716 s`。
- 也就是：
  - repeated maximal ramp 後，
  - 變慢的主要不是一開始那一小段快恢復，
  - 而是後面的 slow phase。

### 4. 個體差異很大

- individual parameter variation 明顯。
- 這支持：
  - 不宜把 group-derived `tau` 直接當 universal physiology

## 臨床表現

### 對 wiki 的直接價值

- 這篇直接補強 [[../04_CPET/Wprime_Recovery]]：
  - trained cyclists + repeated maximal ramps 的確可見 two-phase behavior
- 也補強 [[../04_CPET/Wprime_Balance_Model]]：
  - short-rest 與 repeated-bout 情境下，單一固定 `tau` 會太粗

## 評估方式

### 方法學重點

- 這篇是 **trained cyclists** 且是 **repeated ramp-to-limit** 設計。
- 它最適合回答的是：
  - high-performance context 下，
  - `W'` 在 repeated maximal depletion 後怎麼回來
- 不應直接外推到：
  - partial depletion
  - 臨床病人
  - 非 cycling modality

## 治療原則

- practical take-home：
  - 若 session 含 repeated severe efforts，
    後段 slow recovery 變慢要被納入設計考量。

## 臨床決策點

### 這篇真正改變什麼

- 它不是推翻 Lievens 2024。
- 它是在補上另一種情境：
  - **repeated maximal ramp / trained cyclist** 情境下，
    biexponential 確實有更強支持。

## 限制與未定論

### 限制 / caveat

- sample size 小。
- 族群集中在 trained cyclists。
- 需要多次 visits，外部效度有限。

### frontmatter contradictions

- In trained cyclists after repeated maximal ramp exercise, a bi-exponential model fit W' reconstitution better than a mono-exponential model, but this does not prove a universal two-phase recovery law.
- Repeated bouts mainly slowed the slow component rather than changing component amplitudes, reinforcing that W' recovery is context and state dependent.

## 理解缺口

- 在其他 modality 或較低訓練程度族群是否仍同樣支持 biexponential？
- depletion 程度、recovery power 與 repeated-bout effect 會怎麼交互影響 FC / SC？

## 臨床使用版

- 如果你處理的是 trained cyclists 的 repeated severe efforts，這篇很重要。
- 但它回答的是特定情境，不是 universal `W'` recovery law。

## 來源

### 證據標記

- 來源層級：3
- evidence_level：limited
- confidence：medium

### 書目

- Chorley A, Bott RP, Marwood S, Lamb KL.
- *Bi-exponential modelling of W' reconstitution kinetics in trained cyclists.*
- 類型：**original article**
- 來源等級：**Tier 3**
- 可信度：**medium**
- 原始檔：`C:\原始資料\s00421-021-04874-3\s00421-021-04874-3.md`

## 相關頁面

- [[../04_CPET/Wprime_Recovery]]
- [[../04_CPET/Wprime_Balance_Model]]
- [[../04_CPET/Training_Prescription_by_CP]]
