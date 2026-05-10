---
title: Skiba et al. 2012 — Modeling the Expenditure and Reconstitution of Work Capacity above Critical Power
created: 2026-04-25
updated: 2026-04-25
type: source_summary
domain: [CPET, exercise_physiology, methodology]
tags: [W_prime, Wprime_BAL, critical_power, intermittent_exercise, VO2, original_article, modeling]
source_tier: 3
evidence_level: limited
confidence: medium
contested: true
contradictions:
  - This seminal paper introduced a practical W'BAL equation, but its fitted tau-W' is protocol- and population-dependent rather than a universal constant.
  - Correlation between modeled W' balance and VO2 rise does not prove that W' is a single anaerobic tank or a direct VO2 surrogate.
---

# Skiba et al. 2012 — Modeling the Expenditure and Reconstitution of Work Capacity above Critical Power

## 一句話定義

這篇 original article 是早期 **W'BAL integral form** 的代表作：作者提出一個連續方程式去追蹤 intermittent exercise 中的 `W'` 消耗與回補，並指出 **recovery power 越低於 CP，W' 回補通常越快**。

## 核心機制

### 研究設計

- 7 位健康男性。
- 先估 `VO2max`、CP、W'。
- 再做 60 s severe work bout + 30 s recovery，重複到 exhaustion。
- recovery 強度分成：
  - 20 W
  - moderate
  - heavy
  - severe

### 主要發現

### 1. 這篇建立了早期 W'BAL 連續方程式

- 核心想法是：
  - 一旦 power > CP，`W'` 開始消耗
  - 一旦 power < CP，`W'` 開始按 curvilinear / exponential 方式回補
- 這讓 intermittent exercise 不再只能用 static `CP + W'/t` 看待。

### 2. tau-W' 和 recovery power 與 CP 的差距有關

- `DCP = CP - recovery power`
- 當 recovery 還在 CP 以下時：
  - `DCP` 越大
  - `tau-W'` 越小
  - 回補越快
- 作者給出一個經典早期經驗式：
  - `tau-W' = 546e^(-0.01DCP) + 316`

### 3. recovery 高到超過 CP 時，幾乎沒有淨回補

- 當 recovery interval 本身就在 CP 以上，
  - 模型會給出非常大的 time constant
  - 實際意義就是：沒有真正的 `W'` recharge，只是消耗速度變慢

### 4. modeled W' balance 與 VO2 rise 有相關

- 作者觀察到 modeled `W'BAL` 與 intermittent exercise 中 `VO2` 上升的時間過程有顯著相關。
- 這支持 `W'` 不只是抽象數學常數，可能和 severe-domain metabolic strain 有關。

## 臨床表現

### 對 wiki 的直接價值

- 這篇是 [[../04_CPET/Wprime_Balance_Model]] 的歷史起點之一。
- 它讓我們知道：
  - W'BAL 最初是為了 intermittent exercise 的實務追蹤而生
  - 不是一開始就有完整 mechanistic proof

## 評估方式

- 這是 original article，不是 field consensus review。
- 它的重要性在於「模型起源」與「實務方程式提出」。
- 但其 `tau-W'` 需要 fitting，外推到其他族群或 protocol 要保守。

## 治療原則

- 對 training prescription 的意義：
  - recovery 強度不是小細節，會直接改變可再動員的 severe-domain work capacity。
- 對 clinical CPET 的意義：
  - 它主要屬 performance / modeling 工具，不是 routine clinical endpoint。

## 臨床決策點

### 這篇真正改變什麼

- 它不是證明「W' 就是一個真實油箱」。
- 它比較像是證明：
  - 若你要追蹤 intermittent severe exercise
  - 一個會考慮回補 kinetics 的模型，比 static W' 概念更實用

## 限制與未定論

### 限制 / caveat

- sample size 小。
- 早期 model 需用 exhaustion data 反推 `tau-W'`。
- real-world physiology 可能比單一 mono-exponential reconstitution 更複雜。

### frontmatter contradictions

- This seminal paper introduced a practical W'BAL equation, but its fitted tau-W' is protocol- and population-dependent rather than a universal constant.
- Correlation between modeled W' balance and VO2 rise does not prove that W' is a single anaerobic tank or a direct VO2 surrogate.

## 理解缺口

- 這個早期 integral form 到哪些情境還夠用，哪些情境已需要 differential / individualized model？
- `W'BAL` 與 `VO2` 的相關，到底反映共同的 severe-domain strain，還是更直接的機制耦合？

## 臨床使用版

- 若你在讀 W'BAL 文獻，這篇是起點。
- 但若你把它讀成「W' 已被完全 mechanistically 定義」，那就超過這篇 paper 真正做到的事。

## 來源

### 證據標記

- 來源層級：3
- evidence_level：limited
- confidence：medium

### 書目

- Skiba PF, Chidnok W, Vanhatalo A, Jones AM.
- *Med Sci Sports Exerc* 2012;44(8):1526-1532.
- DOI: 10.1249/MSS.0b013e3182517a80
- 類型：**original article**
- 來源等級：**Tier 3**
- 可信度：**medium**
- 原始檔：`C:\原始資料\modeling_the_expenditure_and_reconstitution_of.15\modeling_the_expenditure_and_reconstitution_of.15.md`

## 相關頁面

- [[../04_CPET/Wprime_Balance_Model]]
- [[../04_CPET/Critical_Power]]
- [[../04_CPET/Training_Prescription_by_CP]]
- [[Skiba_Clarke_Wprime_balance_model]]
