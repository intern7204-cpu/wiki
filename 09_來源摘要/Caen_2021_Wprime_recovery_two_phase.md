---
title: Caen et al. 2021 — W' recovery kinetics after exhaustion
created: 2026-04-25
updated: 2026-04-25
type: source_summary
domain: [CPET, exercise_physiology, performance_modeling]
tags: [W_prime, recovery, aerobic_fitness, VO2_kinetics, PCr, original_article]
source_tier: 3
evidence_level: limited
confidence: medium
contested: true
contradictions:
  - W' recovery after exhaustive exercise is better described by fast and slow components than by a single universal time constant.
  - Faster VO2 and PCr recovery explain part of short-rest W' reconstitution, but W' recovery cannot be reduced to a single metabolic variable.
---

# Caen et al. 2021 — W' recovery kinetics after exhaustion

## 一句話定義

這篇 whole-body cycling original article 的重點是：**W' recovery 在 exhaustion 後比較像 fast + slow 的 two-phase process，而不是單一 universal recharge constant；短休息時 standard W'BAL 會系統性低估恢復。**

## 核心機制

### 研究設計

- 21 位 physically active men。
- 先用多次 constant-load test 求 CP 與 W'。
- 再做兩個相同的 exhaustive work bouts，中間插入 `30、60、120、180、240、300、600、900 s` recovery。
- 同步量測 breath-by-breath gas exchange，並用 muscle biopsy 評估 MFT distribution。

### 主要發現

### 1. standard W'BAL 對短 recovery 偏慢

- group-derived `W'BAL` recovery time constant 約 `524 s`。
- 對 `W'OBS` 的 fitting RMSE 約 `18.6%`。
- 對所有 `<5 min` recovery 都明顯低估恢復。

### 2. exhaustion 後的 W' recovery 比較像 biexponential

- monoexponential：`tau ≈ 104 s`
- biexponential：`tau1 ≈ 11 s`、`tau2 ≈ 256 s`
- `ΔAICc` 較支持 biexponential model。

### 3. changing VO2 kinetics 解釋了一部分，不是全部

- 用 `W'ADJ` 校正較低的 O2 deficit 後，恢復量仍存在，只是平均比 `W'OBS` 低約 `11%`。
- 代表短休息時更快的 aerobic contribution 有幫助，但不能單獨解釋全部 W' recovery。

### 4. aerobic fitness 比 muscle fiber type 更重要

- `VO2peak` 與 `W'OBS` 有關。
- MFT distribution 在本研究中不是顯著 predictor。

## 臨床表現

### 對 wiki 的直接價值

- 補強 [[../04_CPET/Wprime_Balance_Model]] 的 caveat：單一 `tau` 模型對短 recovery 可能太粗。
- 也補強 [[../05_Exercise_Physiology/PCr_Resynthesis]]：PCr / VO2 recovery 很重要，但 W' recovery 仍是更大的 whole-system construct。

## 評估方式

- 這是 exhaustion-based、whole-body cycling protocol。
- 可用來理解機制與 interval design，不是 routine bedside test。

## 治療原則

- severe-domain interval 不應假設每段 recovery 都遵循同一個簡單 time constant。
- 若處方高度依賴短 recovery，最好在同一 athlete、同一模型內追蹤。

## 臨床決策點

### 這篇真正改變什麼

- 它不是說 `W'BAL` 無效。
- 它是在說：**若把 W' recovery 簡化成單一 universal monoexponential recharge，短休息時很容易失真。**

## 限制與未定論

### 限制 / caveat

- exhaustion 後的 kinetics 不一定等同 partial depletion。
- 只納入年輕男性，external validity 有限。
- `W'ADJ` 仍是 model-based estimate，不是直接量到全部 aerobic contribution。

### frontmatter contradictions

- W' recovery after exhaustive exercise is better described by fast and slow components than by a single universal time constant.
- Faster VO2 and PCr recovery explain part of short-rest W' reconstitution, but W' recovery cannot be reduced to a single metabolic variable.

## 理解缺口

- partial depletion 時，fast phase 會不會同樣明顯？
- aerobic fitness、recovery power、fatigue state 三者各自對 W' recovery 的獨立影響有多大？

## 臨床使用版

- 若你在做 short-rest severe-domain interval 設計，這篇很值得記住。
- 最該保留的訊息不是某個精確秒數，而是：**短 recovery 的 W' 重建常比單一 `tau` 想像得更快，也更複雜。**

## 來源

### 證據標記

- 來源層級：3
- evidence_level：limited
- confidence：medium

### 書目

- Caen K, Bourgois G, Dauwe C, Blancquaert L, Vermeire K, Lievens E, et al.
- *Med Sci Sports Exerc.* 2021;53(9):1911-1921.
- 類型：**original article**
- 來源等級：**Tier 3**
- 可信度：**medium**
- 原始檔：`C:\原始資料\w__recovery_kinetics_after_exhaustion__a_two_phase\w__recovery_kinetics_after_exhaustion__a_two_phase.md`

## 相關頁面

- [[../04_CPET/Wprime_Balance_Model]]
- [[../04_CPET/Training_Prescription_by_CP]]
- [[../05_Exercise_Physiology/PCr_Resynthesis]]
- [[Skiba_2015_intramuscular_determinants_Wprime_recovery]]
