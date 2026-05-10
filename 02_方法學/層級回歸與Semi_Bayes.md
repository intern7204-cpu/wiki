---
title: 層級回歸與Semi-Bayes
created: 2026-04-25
updated: 2026-04-25
type: method
domain: [medical_methodology, epidemiology, research]
tags: [hierarchical_regression, semi_Bayes, shrinkage, multiple_comparisons, correlated_exposures]
sources:
  - 10_來源摘要/Witte_Greenland_1994_hierarchical_regression.md
source_tier: 3
evidence_level: limited
confidence: medium
contested: true
contradictions:
  - Hierarchical regression can stabilize noisy estimates, but misspecified second-stage assumptions can also shrink results in the wrong direction.
  - Semi-Bayes modeling does not remove subjectivity; it makes the modeling assumptions more explicit than ordinary regression.
---

# 層級回歸與Semi-Bayes

## 一句話定義

Hierarchical regression / semi-Bayes 的核心，是在第一層 ordinary regression 外，再加一層「相似變數共享資訊」的模型，讓 sparse data 下過度極端的估計被適度 shrink 回較合理的範圍。

## 核心機制

### 費曼式理解

- ordinary regression 像讓 87 個食物各自單獨發言。
- 樣本不夠、暴露彼此又很像時，某些係數會因噪音而吵得非常大聲。
- hierarchical regression 不是叫所有變數講同一句話，而是讓**相似的變數部分借用彼此資訊**。

### two-stage logic

### 第一層

- disease ~ exposures + confounders

### 第二層

- exposure coefficients ~ descriptor variables
- 例如本文用 nutrient composition 描述 food item 的相似性。

### `tau` 是 shrinkage 旋鈕

- `tau` 越小，shrinkage 越強。
- `tau` 越大，結果越接近 ordinary maximum-likelihood estimate。

## 臨床表現

### 研究上什麼時候特別有用

- exposure 很多
- 暴露彼此高度相關
- 樣本數相對於參數太薄
- ordinary regression 已經跑出不太可信的極端 estimate
- 在 occupational exposure、nutrition epidemiology 或 rehab outcome research 這類「變數很多但每個訊號都不厚」的情境，特別值得考慮。

### 它真正解決的是什麼

- 不是替代 causal design。
- 是降低 **implausible instability**。

## 評估方式

### 使用前要先問三件事

- 你要讓哪些變數共享資訊？
- second-stage descriptor 有沒有 domain meaning？
- `tau` 的 sensitivity analysis 做了沒有？

## 治療原則

### 實務使用原則

- ordinary model 與 hierarchical model 最好一起報。
- second-stage structure 要可辯護，不可只是為了讓結果好看。
- shrinkage 後的 estimate 比較穩，不代表自動更接近真相；它只是通常比完全放任噪音更可用。

## 臨床決策點

### 反對論點

- 「這只是把結果往作者想要的方向拉。」

### 反駁

- ordinary regression 也有隱性 prior，只是常被假裝不存在。
- hierarchical / semi-Bayes 的優點，不是沒有主觀性，而是把主觀性變成可檢查、可做 sensitivity analysis 的設定。

### 結論

- 當 many correlated exposures 遇上 sparse data 時，hierarchical regression 常比 stepwise selection 或只看 p value 更合理。

## 限制與未定論

### 目前限制 / 爭議點

- second-stage model 若設錯，shrinkage 可能把 estimate 拉向錯誤方向。
- 它不能修復 measurement error、selection bias 或 poor confounding control。
- 不同 `tau` 設定下結果可能明顯不同，所以 sensitivity analysis 不是可有可無。

### frontmatter contradictions

- Hierarchical regression can stabilize noisy estimates, but misspecified second-stage assumptions can also shrink results in the wrong direction.
- Semi-Bayes modeling does not remove subjectivity; it makes the modeling assumptions more explicit than ordinary regression.

## 理解缺口

- second-stage 應優先建在 biological mechanism、measurement family，還是 pragmatic grouping？
- 哪些研究情境下，hierarchical regression 真能改善 decision-making，而不只是數學上更平滑？

## 臨床使用版

- 若你的問題是「係數太飄、太極端、太不可信」，這個方法值得考慮。
- 若你的 second-stage 結構只是隨意拼貼，hierarchical regression 只會把錯誤估計變得更穩定。

## 來源

### 來源摘要連結

- [[10_來源摘要/Witte_Greenland_1994_hierarchical_regression]]

### 證據標記

- 來源層級：3
- evidence_level：limited
- confidence：medium

## 相關頁面

- [[復健品質與結局指標]]
- [[職業醫學與職業復健]]
- [[../10_來源摘要/Witte_Greenland_1994_hierarchical_regression]]
