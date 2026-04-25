---
title: Ferguson et al. 2010 — Effect of recovery duration from prior exhaustive exercise on the parameters of the power-duration relationship
created: 2026-04-25
updated: 2026-04-25
type: source_summary
domain: [CPET, exercise_physiology, methodology]
tags: [W_prime, recovery, critical_power, lactate, VO2_recovery, original_article]
source_tier: 3
evidence_level: limited
confidence: medium
contested: true
contradictions:
  - Post-exhaustion CP remained stable while W' recovered curvilinearly, arguing against W' as a simple finite energy store.
  - VO2 recovery was much faster and lactate recovery much slower than W' recovery, so neither alone can serve as the full physiologic surrogate for W'.
---

# Ferguson et al. 2010 — Effect of recovery duration from prior exhaustive exercise on the parameters of the power-duration relationship

## 一句話定義

這篇 original article 是 W' recovery 的經典研究之一：**exhaustion 後 CP 幾乎不變，但 W' 會隨 recovery duration 曲線式回來，而且速度慢於 VO2 recovery、快於 lactate recovery。**

## 核心機制

### 研究設計

- 6 位 recreationally active healthy men。
- 先用 ramp 與多次 constant-load tests 求：
  - `CP`
  - `W'`
  - `VO2max`
- 再做 exhaustive supra-CP conditioning bout，
  中間穿插 `2 / 6 / 15 min` recovery，
  之後重建 postconditioning `P-tLIM` relationship。
- 同步比較：
  - `W'` recovery
  - `VO2` recovery
  - blood lactate recovery

### 主要發現

### 1. CP 幾乎不受 prior exhaustion 影響

- control `CP ≈ 212 W`
- conditioning 後不管 recovery `2 / 6 / 15 min`，`CP` 都維持約 `213 W`

### 2. W' 則高度依賴 recovery duration

- recovery `2 min`：`W'` 約回到 **37%**
- recovery `6 min`：約 **65%**
- recovery `15 min`：約 **86%**

### 3. W' recovery 是 curvilinear

- interpolated `t1/2 ≈ 234 s`
- 說明它不像單一瞬間補滿，也不像簡單 linear refill

### 4. W' recovery 介於 VO2 與 lactate recovery 之間

- `VO2` recovery `t1/2 ≈ 74 s`
- `W'` recovery `t1/2 ≈ 234 s`
- lactate recovery `t1/2 ≈ 1366 s`
- 這很關鍵，因為它否定兩個過度簡化：
  - `W' = VO2 / PCr proxy`
  - `W' = lactate / H+ clearance`

## 臨床表現

### 對 wiki 的直接價值

- 這篇直接補強 [[../04_CPET/Wprime_Recovery]] 與 [[../04_CPET/Wprime_Balance_Model]]。
- 它也是把 `W'` 從「單一 anaerobic tank」拉回 whole-system construct 的關鍵 paper。

## 評估方式

### 真正的方法學訊息

- prior exhaustive exercise 之後，`P-tLIM` 仍然保有 hyperbolic 結構。
- 變的主要是 `W'`，不是 `CP`。
- 所以對 intermittent severe exercise 來說，recovery design 主要是在改變 **可用的 W'**。

## 治療原則

- 若你在設計 severe-domain intervals，不能用 `VO2` recovery 或 lactate recovery 其中一條線直接代替 `W'` recovery。
- 較合理的說法是：
  - W' recovery 受多個恢復過程共同限制

## 臨床決策點

### 這篇真正改變什麼

- 它不是只在說 `W'` 會回來。
- 它是在說：**W' recovery 有自己的時間尺度，而且和 VO2、lactate 都不同。**

## 限制與未定論

### 限制 / caveat

- sample size 小。
- 只有 healthy men。
- 以 pulmonary `VO2` 當 PCr proxy，本身仍是間接推論。
- exhaustion paradigm 不一定等同 partial depletion。

### frontmatter contradictions

- Post-exhaustion CP remained stable while W' recovered curvilinearly, arguing against W' as a simple finite energy store.
- VO2 recovery was much faster and lactate recovery much slower than W' recovery, so neither alone can serve as the full physiologic surrogate for W'.

## 理解缺口

- 如果 recovery power 不是 20 W，而是更接近 real-world active recovery，這些 kinetics 會怎麼變？
- 這種 classic exhaustion paradigm 能外推到 team-sport surges 到什麼程度？

## 臨床使用版

- 如果你要一句最重要的話：**CP 大致留著，先回來的是 VO2，最慢的是 lactate，中間那條才比較像 W'。**

## 來源

### 證據標記

- 來源層級：3
- evidence_level：limited
- confidence：medium

### 書目

- Ferguson C, Rossiter HB, Whipp BJ, Cathcart AJ, Murgatroyd SR, Ward SA.
- *Effect of recovery duration from prior exhaustive exercise on the parameters of the power-duration relationship.*
- *J Appl Physiol.* 2010;108:866-874.
- DOI: 10.1152/japplphysiol.91425.2008
- 類型：**original article**
- 來源等級：**Tier 3**
- 可信度：**medium**
- 原始檔：`C:\原始資料\ferguson-et-al-2010-effect-of-recovery-duration-from-prior-exhaustive-exercise-on-the-parameters-of-the-power-duration\effect of recovery duration from prior exhaustive exercise on the parameters of the power duration.md`

## 相關頁面

- [[../04_CPET/Wprime_Recovery]]
- [[../04_CPET/Wprime_Balance_Model]]
- [[../05_Exercise_Physiology/PCr_Resynthesis]]

