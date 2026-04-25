---
title: Zacca et al. 2019 — VO2FITTING: a free and open-source software for modelling oxygen uptake kinetics
created: 2026-04-25
updated: 2026-04-25
type: source_summary
domain: [CPET, methodology, exercise_physiology]
tags: [VO2_kinetics, software, curve_fitting, bootstrap, swimming, modeling, original_article]
source_tier: 3
evidence_level: limited
confidence: medium
contested: true
contradictions:
  - Software can standardize curve fitting, but preprocessing and model choice still require physiological judgment.
  - Internal validation with synthetic data does not prove superiority across all real-world modalities or off-transient analyses.
---

# Zacca et al. 2019 — VO2FITTING: a free and open-source software for modelling oxygen uptake kinetics

## 一句話定義

這篇 original article 介紹 `VO2FITTING`：一個用於 **VO2 kinetics 資料編修、濾波、curve fitting、bootstrap confidence interval** 的 open-source tool；它的價值比較偏 **方法標準化**，不是提出新的生理主理論。

## 核心機制

### 這個工具在做什麼

- 提供一個 Shiny / R-based 的 open-source workflow。
- 功能包含：
  - data editing
  - processing / filtering
  - mono / bi / tri-exponential models
  - logistic model
  - bootstrap parameter interval estimation

### 作者展示了什麼

### 1. synthetic dataset validation

- 用已知參數的 noisy / non-noisy dataset 測試。
- tool 能回推出正確參數。
- 這代表軟體數值流程本身是可用的。

### 2. severe swimming example

- 用 age-group swimmers 的 severe-intensity 400 m swim test 做示範。
- 比較 mono- vs bi-exponential fitting。
- 強調 severe-domain `VO2` kinetics 會有較低 signal-to-noise ratio，model choice 很重要。

### 3. preprocessing 會直接影響 parameter confidence

- 作者與 supporting workflow 都提醒：
  - 去除 aberrant breaths
  - interpolation
  - binning
  - 排除 phase I
  - mono- 或 bi-exponential choice
  - 是否 constraining parameter
- 這些都會改變最終 `tau`、`Asc` 與 confidence interval。

## 臨床表現

### 對 wiki 的直接價值

- 可補強 [[../04_CPET/VO2_Kinetics]] 的方法學段落。
- 這篇最值得留下的是：
  - `VO2 kinetics` 不是只選一條方程式就結束
  - data treatment 本身就是結果的一部分

## 評估方式

- 這不是在證明某一種生理機制。
- 它是在處理「你怎麼把 noisy VO2 data 合理地 fit 出來」。

## 治療原則

- 不直接給 clinical treatment。
- 對研究與 performance diagnostics 的價值大於 routine bedside use。

## 臨床決策點

### 這篇真正改變什麼

- 它不是告訴你新的 physiology。
- 它是提醒你：
  - `tau`、`slow component`、CI
  - 都會受到 preprocessing 與 model choice 影響

## 限制與未定論

### 限制 / caveat

- 內部驗證主要是 synthetic datasets。
- paper 當時版本對 off-transient analysis 尚未完整支援。
- 軟體即使免費開源，也不能取代使用者對 exercise intensity domain 與 kinetics physiology 的判讀。

### frontmatter contradictions

- Software can standardize curve fitting, but preprocessing and model choice still require physiological judgment.
- Internal validation with synthetic data does not prove superiority across all real-world modalities or off-transient analyses.

## 理解缺口

- 不同 modality 下，最佳 preprocessing / fitting workflow 是否應個別化？
- severe-domain 與 off-transient 資料的最佳 CI estimation pipeline 還有哪些 practical gap？

## 臨床使用版

- 若你在做 VO2 kinetics research，這篇是工具與流程文。
- 若你在看結果，先問資料怎麼處理，再看那個 `tau` 有沒有意義。

## 來源

### 證據標記

- 來源層級：3
- evidence_level：limited
- confidence：medium

### 書目

- Zacca R, Azevedo R, Figueiredo P, Vilas-Boas JP, Castro FAS, Pyne DB, Fernandes RJ.
- *Sports* 2019;7(2):31.
- 類型：**original article / software paper**
- 來源等級：**Tier 3**
- 可信度：**medium**
- 原始檔：`C:\原始資料\sports-07-00031-v2\sports-07-00031-v2.md`
- 原始檔：`C:\原始資料\sports7020031\sports7020031.md`（duplicate raw path）

## 相關頁面

- [[../04_CPET/VO2_Kinetics]]
- [[../04_CPET/VO2_Slow_Component]]
