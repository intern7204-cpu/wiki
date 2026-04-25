---
title: Skiba et al. 2015 — Intramuscular determinants of the ability to recover work capacity above critical power
created: 2026-04-25
updated: 2026-04-25
type: source_summary
domain: [CPET, exercise_physiology, methodology]
tags: [W_prime, PCr, 31P_MRS, carnosine, critical_power, recovery, original_article]
source_tier: 3
evidence_level: limited
confidence: medium
contested: true
contradictions:
  - W' recovery is much slower than bulk PCr recovery, so W' should not be treated as a pure phosphocreatine store.
  - Chemical-kinetics analogies can help model W' recovery, but they oversimplify heterogeneous muscle physiology.
---

# Skiba et al. 2015 — Intramuscular determinants of the ability to recover work capacity above critical power

## 一句話定義

這篇 original article 用 `31P-MRS` / `1H-MRS` 顯示：**W' recovery 與 intramuscular energetics 有關，但 W' 恢復明顯慢於 bulk PCr recovery，因此 W' 不能簡化成單一 PCr tank。**

## 核心機制

### 研究設計

- 10 位 healthy recreationally trained subjects。
- single-leg knee-extension exercise。
- 先估 CP 與 W'。
- 在 MRI scanner 內做到 supra-CP exhaustion。
- 休息 1、2、5、7 分鐘後再做第二 bout。
- 同步量測：
  - `[PCr]`
  - `[Pi]`
  - pH
  - carnosine
  - modeled W' recovery

### 主要發現

### 1. W' recovery 與新 derivation model 高相關

- 研究中的 novel derivation 對 W' recovery 的預測和實測值相當接近。
- 支持 W' recovery 確實可被某種 curvilinear kinetics 近似。

### 2. [PCr] recovery 明顯快於 W' recovery

- `[PCr]` recovery half-time 約 **38 s**
- `W'` recovery half-time 約 **232 s**

費曼式理解：
- 肌肉內大宗的 PCr 補回來很快，
- 但可再次動員的 `W'` 沒有跟著同速恢復。
- 所以：
  - `W' ≠ pure PCr store`
  - 至少不是用一個簡單等號就能互換

### 3. D[PCr] 比單看 bulk [PCr] kinetics 更貼近 W' recovery

- 可用 work bout 開始與 exhaustion 時 `[PCr]` 差值的 recovery 去描述和 W' 的關聯。
- 這比較像是在說：
  - 和 W' 相關的不是「PCr 有沒有回到很高」
  - 而是「又有多少 oxidative reserve 能被再動員」

### 4. pH 關聯不強，carnosine 可能有角色

- pH recovery 與 W' recovery 沒有明確直接相關。
- carnosine 濃度與 `W' t1/2` 呈 inverse curvilinear relationship。
- 這代表 buffering-related traits 可能參與，但證據仍屬 exploratory。

## 臨床表現

### 對 wiki 的直接價值

- 補強 [[../04_CPET/Wprime_Balance_Model]] 與 [[../05_Exercise_Physiology/PCr_Resynthesis]] 的分界。
- 最重要的訊息是：
  - W' recovery 和 muscle oxidative/metabolic state 有關
  - 但不能把 W' 直接縮成 PCr 一個變數

## 評估方式

- 這是研究級 MRS 方法，不是 routine clinical assessment。
- 適合用來理解 mechanism，不適合直接變成 bedside algorithm。

## 治療原則

- 對 training 的意義：
  - interval recovery 不應只用「PCr 回補快」做過度簡化
  - 真正的 severe-domain work capacity restoration 牽涉更大的系統層次

## 臨床決策點

### 這篇真正改變什麼

- 它不是否定 PCr 的重要性。
- 它是在修正一個過度簡化：
  - `W' = PCr`
  - 這個等式太粗糙

## 限制與未定論

### 限制 / caveat

- 單腳 knee-extension，外推到 whole-body exercise 要保守。
- sample size 小。
- model 與 spectroscopy interpretation 都帶有假設。

### frontmatter contradictions

- W' recovery is much slower than bulk PCr recovery, so W' should not be treated as a pure phosphocreatine store.
- Chemical-kinetics analogies can help model W' recovery, but they oversimplify heterogeneous muscle physiology.

## 理解缺口

- 什麼樣的 intramuscular composite 最接近 W' 的真正生理對應？
- carnosine / buffering traits 對 W' recovery 的貢獻在全身運動中有多大？

## 臨床使用版

- 若你要用費曼方式解釋 W' recovery，這篇很好用。
- 最該記住的是：**PCr 很重要，但 W' 不是 PCr 的別名。**

## 來源

### 證據標記

- 來源層級：3
- evidence_level：limited
- confidence：medium

### 書目

- Skiba PF, Fulford J, Clarke DC, Vanhatalo A, Jones AM.
- *Eur J Appl Physiol* 2015;115:1-15.
- 類型：**original article**
- 來源等級：**Tier 3**
- 可信度：**medium**
- 原始檔：`C:\原始資料\s00421-014-3050-3\s00421-014-3050-3.md`

## 相關頁面

- [[../04_CPET/Wprime_Balance_Model]]
- [[../05_Exercise_Physiology/PCr_Resynthesis]]
- [[Skiba_2012_modeling_Wprime_expenditure_reconstitution]]
- [[Chidnok_2013_intermittent_exercise_PCr_CP]]
