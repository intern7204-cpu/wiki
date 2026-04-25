---
title: Korzeniewski & Zoladz 2013 — Slow VO2 off-kinetics in skeletal muscle is associated with fast PCr off-kinetics
created: 2026-04-25
updated: 2026-04-25
type: source_summary
domain: [exercise_physiology, CPET, methodology]
tags: [VO2_off_kinetics, PCr, recovery, oxidative_phosphorylation, theoretical_model, original_article]
source_tier: 3
evidence_level: limited
confidence: medium
contested: true
contradictions:
  - This is an in silico skeletal-muscle model, not a direct human validation study.
  - Pulmonary VO2 off-kinetics should not be assumed to directly mirror intramuscular VO2 or PCr recovery kinetics.
---

# Korzeniewski & Zoladz 2013 — Slow VO2 off-kinetics in skeletal muscle is associated with fast PCr off-kinetics

## 一句話定義

這篇 theoretical original article 提出一個反直覺但重要的觀點：**在 skeletal muscle level，較慢的早期 VO2 off-kinetics 反而可能伴隨較快的 PCr recovery；兩者不是天然同步的鏡像。**

## 核心機制

### 研究設計

- 使用 skeletal muscle bioenergetic computer model。
- 模擬 moderate 與 heavy exercise 後 recovery。
- 核心操弄變數是 oxidative phosphorylation 平行活化衰減時間 `τ(OFF)`。

### 主要發現

### 1. VO2 off 與 PCr off 可呈 inverse relation

- 當 `τ(OFF)` 變大時：
  - 早期 muscle VO2 off-kinetics 變慢
  - PCr resynthesis 反而變快
- 反過來說：
  - 若 VO2 一停下來就掉很快
  - PCr recovery 反而可能比較慢

費曼式理解：
- 運動後要補回 PCr，需要 oxidative phosphorylation 繼續工作。
- 如果氧化系統的 activation 很快關掉，
  - VO2 會看起來掉得很快
  - 但補 PCr 的 ATP 來源也跟著變少
- 所以「VO2 掉快」不一定是「恢復快」。

### 2. 對同一 PCr depletion，oxygen debt 總量可相同

- 不同 `τ(OFF)` 下，早期與晚期 VO2 off 形狀會變。
- 但若工作期間 PCr decrease 相同，整體 recovery 期的 oxygen debt integral 可相同。

### 3. pulmonary 與 muscle kinetics 不該直接混成同一件事

- 作者特別提醒，muscle-level VO2 / PCr kinetics 與 pulmonary VO2 off-kinetics 未必一致。
- 尤其 heavy exercise 時，blood transport 與 whole-body recovery 會讓肺端訊號更複雜。

## 臨床表現

### 對 wiki 的直接價值

- 可補強 [[../04_CPET/VO2_Kinetics]] 與 [[../05_Exercise_Physiology/PCr_Resynthesis]] 的 recovery caveat。
- 重點不是把模型當真相，而是避免錯誤推論：
  - `VO2 off faster = PCr recovers faster`
  - 這個等號並不穩

## 評估方式

- 這篇是 mechanistic in silico study。
- 用來產生假說與整理概念很好，但不能直接當 human validation。

## 治療原則

- 不直接提供 treatment algorithm。
- 主要用於修正機制推論與測量詮釋。

## 臨床決策點

### 這篇真正改變什麼

- 它迫使我們把「recovering oxygen consumption」與「restoring intramuscular high-energy phosphate」分開看。
- 也提醒不要把 pulmonary off-kinetics 過度簡化成肌肉內部發生的單一步驟。

## 限制與未定論

### 限制 / caveat

- model assumptions 很重。
- 並非直接量測 human working muscle。
- `τ(OFF)` 的生理對應仍屬推論。

### frontmatter contradictions

- This is an in silico skeletal-muscle model, not a direct human validation study.
- Pulmonary VO2 off-kinetics should not be assumed to directly mirror intramuscular VO2 or PCr recovery kinetics.

## 理解缺口

- 哪些人類資料最能直接驗證 muscle VO2 off 與 PCr off 的 inverse relation？
- 在 clinical CPET 裡，pulmonary recovery kinetics 最多能替代哪些肌肉內部資訊？

## 臨床使用版

- 若你看到 recovery VO2 掉很快，不要立刻推論「肌肉恢復一定快」。
- 先問：你量到的是肺、血液系統，還是 muscle intracellular energetics？

## 來源

### 證據標記

- 來源層級：3
- evidence_level：limited
- confidence：medium

### 書目

- Korzeniewski B, Zoladz JA.
- *J Appl Physiol* 2013;115:605-612.
- DOI: 10.1152/japplphysiol.00469.2013
- 類型：**original article**
- 來源等級：**Tier 3**
- 可信度：**medium**
- 原始檔：`C:\原始資料\korzeniewski-zoladz-2013-slow-v̇o2-off-kinetics-in-skeletal-muscle-is-associated-with-fast-pcr-off-kinetics-and\korzeniewski-zoladz-2013-slow-v̇o2-off-kinetics-in-skeletal-muscle-is-associated-with-fast-pcr-off-kinetics-and.md`

## 相關頁面

- [[../04_CPET/VO2_Kinetics]]
- [[../05_Exercise_Physiology/PCr_Resynthesis]]
- [[../04_CPET/VO2_Slow_Component]]
