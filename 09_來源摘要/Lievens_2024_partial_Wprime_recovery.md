---
title: Lievens et al. 2024 — Characterizing the Exponential Profile of W' Recovery Following Partial Depletion
created: 2026-04-25
updated: 2026-04-25
type: source_summary
domain: [CPET, exercise_physiology, performance_modeling]
tags: [W_prime, recovery, partial_depletion, monoexponential, biexponential, W_BAL, original_article]
source_tier: 3
evidence_level: limited
confidence: medium
contested: true
contradictions:
  - Partial W' depletion did not clearly support a biexponential recovery model, unlike exhaustion-based data, so recovery structure may depend on depletion state.
  - Fixed tau values were inadequate across depletion levels, supporting individualized recovery parameters rather than a universal constant.
---

# Lievens et al. 2024 — Characterizing the Exponential Profile of W' Recovery Following Partial Depletion

## 一句話定義

這篇 2024 original article 的核心訊息是：**在 partial W' depletion 條件下，現有資料不支持把 W' recovery 一律寫成 biexponential；但固定 tau 仍然不夠。**

## 核心機制

### 研究設計

- 9 位 healthy young men。
- 先做 ramp test 與 3–5 次 constant-load tests 求 `CP` 與 `W'`。
- 接著做 10 個 experimental trials：
  - `25%` 或 `75%` W' depletion
  - recovery `30 / 60 / 120 / 300 / 600 s`
- 用 monoexponential 與 biexponential model 擬合 `W'OBS`。

### 主要發現

### 1. partial depletion 不像 exhaustion data 那樣明確支持 biexponential

- biexponential 雖然常有較低 RMSE，
  但 `AICc` 在多數情況下不支持它優於 monoexponential。
- 作者結論很直接：
  - **本研究沒有提供充分證據支持 partial depletion recovery 必須用 biexponential 才合理。**

### 2. fixed tau 還是不夠

- `25%` 與 `75%` depletion 的 recovery 行為並不完全一樣。
- 現有用單一固定 `tau` 的 predictive models，不足以同時描述不同 depletion 條件。

### 3. aerobic fitness 與 W' recovery 有關

- `W'OBS` 與：
  - `VO2peak`
  - `CP`
  - `GET`
  呈正相關（約 `r = 0.67–0.77`）。

### 4. 兩種 depletion condition 的個體差異具有一致性

- `DEP25%` 與 `DEP75%` 的 mean `W'OBS` 高度相關（`r = 0.92`）。
- 代表 recoverer 快的人，在不同 depletion 程度下通常都比較快。

## 臨床表現

### 在本 wiki 的直接價值

- 這篇直接補強 [[../04_CPET/Wprime_Recovery]]：
  - **partial depletion** 不應直接照搬 exhaustion-based two-phase story。
- 也補強 [[../04_CPET/Wprime_Balance_Model]]：
  - 單一固定 `tau` 不夠
  - 但也不表示一定要強行上 biexponential

## 評估方式

### 方法學重點

- 作者同時比較：
  - monoexponential
  - biexponential
  - free amplitude
  - fixed amplitude
- 這讓重點更清楚：
  - 不能只看 fit 看起來比較貼，就忽略 model complexity penalty。

## 治療原則

- practical take-home：
  - **先個體化，再談模型複雜化**
- 對多數實務場景，比起強行選 biexponential，先承認 `tau` 需要 individualized 可能更重要。

## 臨床決策點

### 這篇真正改變什麼

- 它不是否定 Caen 2021 exhaustion data。
- 它是在修正外推：
  - **full exhaustion 的 recovery shape，不一定就是 partial depletion 的 recovery shape。**

## 限制與未定論

### 限制 / caveat

- sample size 小。
- 只有 healthy men。
- recovery 設在 `90% GET`，不代表其他 recovery power 也相同。

### frontmatter contradictions

- Partial W' depletion did not clearly support a biexponential recovery model, unlike exhaustion-based data, so recovery structure may depend on depletion state.
- Fixed tau values were inadequate across depletion levels, supporting individualized recovery parameters rather than a universal constant.

## 理解缺口

- 若 recovery power 再低一點或再高一點，partial depletion 的最佳模型會改變嗎？
- 在訓練程度更高的 athletes，partial depletion 是否更接近 two-phase 行為？

## 臨床使用版

- 如果你要處理的是常見 interval session，而不是每次都 fully deplete，這篇很重要。
- 最該保留的訊息是：**partial depletion 不一定要用 two-phase 解，但固定 tau 仍然太粗。**

## 來源

### 證據標記

- 來源層級：3
- evidence_level：limited
- confidence：medium

### 書目

- Lievens M, Ghijs M, Bourgois JG, Vermeire KM, Bourgois G, Colosio AL, Boone J, Caen K.
- *Characterizing the Exponential Profile of W' Recovery Following Partial Depletion.*
- *Med Sci Sports Exerc.* 2024;56(9):1770-1781.
- DOI: 10.1249/MSS.0000000000003468
- 類型：**original article**
- 來源等級：**Tier 3**
- 可信度：**medium**
- 原始檔：`C:\原始資料\characterizing_the_exponential_profile_of_w_.24\characterizing_the_exponential_profile_of_w_.24.md`

## 相關頁面

- [[../04_CPET/Wprime_Recovery]]
- [[../04_CPET/Wprime_Balance_Model]]
- [[../04_CPET/Training_Prescription_by_CP]]

