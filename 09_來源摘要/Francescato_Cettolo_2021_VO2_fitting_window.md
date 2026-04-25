---
title: Francescato & Cettolo 2021 — Influence of the fitting window on the O2 uptake kinetics at the onset of moderate intensity exercise
created: 2026-04-25
updated: 2026-04-25
type: source_summary
domain: [CPET, methodology, exercise_physiology]
tags: [VO2_kinetics, fitting_window, moderate_intensity, monoexponential, breath_by_breath, original_article]
source_tier: 3
evidence_level: limited
confidence: medium
contested: true
contradictions:
  - A fixed 20-second removal window is not a neutral preprocessing choice; it can materially change the estimated tau.
  - The shortest estimated tau alone is not sufficient, because parameter precision degrades when the fitting window is shifted too far.
---

# Francescato & Cettolo 2021 — Influence of the fitting window on the O2 uptake kinetics at the onset of moderate intensity exercise

## 一句話定義

這篇 original article 的核心訊息是：**moderate-intensity `VO2` kinetics 的 `tau` 會被 fitting window 明顯改變，固定移除前 20 秒並不是中性選擇。**

## 核心機制

### 研究設計

- 25 位 healthy adults 的 moderate-intensity step exercise breath-by-breath `VO2` data。
- 另建立 `10^4` 個 simulated biexponential responses。
- 對每條曲線都用 monoexponential model 重複擬合 `61` 次：
  - 每次把起始資料多移除 `1 s`
  - 從 `0 s` 一直到 `60 s`
- 比較四種決定移除時窗的方法：
  - `20 s-w`
  - `Min-tau`
  - `Min-ASEtau`
  - `Mixed`

### 主要發現

### 1. fitting window 會實質改變 `tau`

- 在真實資料與 simulated data 中，
  `tau` 的最低點都大約出現在移除 `~35 s` 時。
- 與幾乎不移除資料相比，該處估到的 `tau` 約可低 **30%**。

### 2. precision 並不會一路跟著變好

- `ASE` 大致到 `~35 s` 以前都還算穩定。
- 再往後移除，`ASE` 會明顯惡化。
- 也就是：
  - 移太少，容易把 phase 1 混進去
  - 移太多，又會讓估計變不穩

### 3. `Mixed` method 在 simulated data 的表現最好

- 傳統 `20 s-w` 方法的 coverage 約 `85%`。
- `Mixed` method 可提升到約 `92%`。
- 代表只靠「固定 20 秒」或「只挑最短 tau」都不是最佳折衷。

## 臨床表現

### 對 wiki 的直接價值

- 這篇主要補強 [[../04_CPET/VO2_Kinetics]] 的方法學部分：
  - `tau` 不是只由 physiology 決定
  - preprocessing 也會改變 `tau`
- 也能補強 curve-fitting workflow 的設計邏輯：
  - fitting window 要被視為 **model assumption**
  - 不是例行小設定

## 評估方式

### 方法學重點

- 這篇處理的是 **moderate-intensity fundamental component**。
- 核心重點不是推翻 monoexponential fitting，
  而是要求：
  - 起始資料移除規則要更透明
  - fitting window 不要靠習慣硬設

## 治療原則

- practical take-home：
  - 若你在比較不同研究或不同 software 的 `tau`，
    先問 fitting window 怎麼設。

## 臨床決策點

### 這篇真正改變什麼

- 它不是在說 `20 s` 一定錯。
- 它是在說：
  - **`20 s` 只是慣例，不是物理常數。**

## 限制與未定論

### 限制 / caveat

- moderate-intensity data 為主，不可直接外推到 heavy / severe exercise。
- simulated response 的生成本身有模型假設。
- 比的是 parameter recovery，不是臨床結局。

### frontmatter contradictions

- A fixed 20-second removal window is not a neutral preprocessing choice; it can materially change the estimated tau.
- The shortest estimated tau alone is not sufficient, because parameter precision degrades when the fitting window is shifted too far.

## 理解缺口

- 在 heavy / severe domain，最佳 fitting window 是否相同？
- 不同 preprocessing 與 binning strategy 之間會怎麼交互影響 `tau`？

## 臨床使用版

- 如果你把 `tau` 當成重要輸出，就不能把 fitting window 當成背景設定。
- 先把 preprocessing 規則寫清楚，再談 physiology。

## 來源

### 證據標記

- 來源層級：3
- evidence_level：limited
- confidence：medium

### 書目

- Francescato MP, Cettolo V.
- *Influence of the fitting window on the O2 uptake kinetics at the onset of moderate intensity exercise.*
- 類型：**original article**
- 來源等級：**Tier 3**
- 可信度：**medium**
- 原始檔：`C:\原始資料\francescato-cettolo-2021-influence-of-the-fitting-window-on-the-o2-uptake-kinetics-at-the-onset-of-moderate-intensity\influence of the fitting window on the o2 uptake kinetics at the onset of moderate intensity.md`

## 相關頁面

- [[../04_CPET/VO2_Kinetics]]
- [[../04_CPET/CPET_Protocol_Design]]
- [[Zacca_2019_VO2FITTING_software]]
