---
title: Skiba & Clarke — The W' Balance Model: Mathematical and Methodological Considerations
created: 2026-04-25
updated: 2026-04-25
type: source_summary
domain: [CPET, exercise_physiology, methodology]
tags: [W_BAL, W_prime, critical_power, intermittent_exercise, review_article]
source_tier: 1
evidence_level: emerging
confidence: high
contested: true
contradictions:
  - Integral and differential W'BAL forms are based on different depletion/recovery assumptions and should not be treated as interchangeable.
  - W'BAL reaching zero is an estimate with uncertainty, not a universally exact physiologic exhaustion point.
---

# Skiba & Clarke — The W' Balance Model: Mathematical and Methodological Considerations

## 一句話定義

這篇 review article 把 W'BAL 從「實用小工具」往上拉到方法學層級：**W'BAL 有用，但 integral form 與 differential form 的假設不同，若混用或過度實體化，會直接導致解讀錯誤**。

## 核心機制

### 1. 為什麼需要 intermittent model

- 傳統 CP/W' model 適合描述 continuous severe-intensity exercise。
- 但真實訓練與比賽常是 intermittent work / recovery，因此需要追蹤 W' remaining。

### 2. W'BAL-INT 與 W'BAL-ODE 不是同一件事

- **integral form**：
  - 假設 recovery 以 convolution 方式持續進行
  - 甚至在 macroscopic depletion 時，也可能有 microscopic recovery
- **differential form**：
  - 假設 depletion 與 recovery 互斥
  - power > CP 時只 depletion，power < CP 時才 recovery

### 3. 兩種形式各有優缺點

- W'BAL-INT：
  - 現場應用廣
  - 但需要估 tau
  - extreme-case simulation 可能出現不合理結果
- W'BAL-ODE：
  - 不需額外 fit tau，計算較直接
  - 但 recovery 可能預測過快，且對 physiology 仍屬簡化

### 4. 輸入值本身就有誤差

- CP 與 W' 的估計誤差會直接 propagated 到 W'BAL。
- 典型誤差尤其在 W' 較大。
- 因此 `W'BAL = 0` 不應被當成精確生理瞬間，而比較像 exhaustion risk zone。

### 5. 作者對 future direction 的主張

- 需更好的 recovery kinetics
- 需更好的 CP/W' input stability
- 需承認 model refinement 與 physiologic realism 之間的 trade-off

## 臨床表現

### 對現有 wiki 的意義

- 這是 [[../04_CPET/Wprime_Balance_Model]] 的主幹來源。
- 也直接影響 [[../04_CPET/Critical_Power]] 與 [[../04_CPET/Training_Prescription_by_CP]] 的 caveat 寫法。

## 評估方式

### 對使用者最重要的方法學提醒

- 先交代你用的是哪一個 W'BAL form。
- 先交代 CP/W' 是如何得到的。
- 別把 model output 包裝成直接量到的 physiologic quantity。

## 治療原則

- 本頁以概念或來源為主；若要進入真正 training prescription，需連回主題頁。

## 臨床決策點

### 核心 caveat

- 作者不是否定 W'BAL。
- 作者真正否定的是「把不同 form 混成同一個東西」以及「把 model output 當絕對真值」。

## 限制與未定論

### frontmatter contradictions

- Integral and differential W'BAL forms are based on different depletion/recovery assumptions and should not be treated as interchangeable.
- W'BAL reaching zero is an estimate with uncertainty, not a universally exact physiologic exhaustion point.

## 理解缺口

- 哪種 intermittent scenario 比較適合 INT，哪種比較適合 ODE？
- exhaustion threshold 到底應該怎麼 operationalize，才不會把 noise 當 physiology？

## 臨床使用版

- 若要在 wiki 中使用 W'BAL，先寫清楚假設與版本，再談應用。
- 對單一數字太有自信，通常就是這個模型最常見的誤用。

## 來源

### 證據標記

- 來源層級：1
- evidence_level：emerging
- confidence：high

### 書目

- Skiba PF, Clarke DC.
- *Int J Sports Physiol Perform.* 2021;16(11):1561-1572.
- 類型：**review article**
- 來源等級：**Tier 1**
- 可信度：**high**
- 原始檔：`C:\原始資料\Mathematics of W'BAL\Mathematics of W'BAL.md`
- 原始檔：`C:\原始資料\ijspp-article-p1561 (1)\ijspp-article-p1561 (1).md`

## 相關頁面

- [[../04_CPET/Wprime_Balance_Model]]
- [[../04_CPET/Critical_Power]]
- [[../04_CPET/Training_Prescription_by_CP]]
- [[Sreedhara_2019_power_energy_models]]
