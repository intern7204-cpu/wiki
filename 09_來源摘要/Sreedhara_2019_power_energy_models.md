---
title: Sreedhara et al. 2019 — A Survey of Mathematical Models of Human Performance Using Power and Energy
created: 2026-04-25
updated: 2026-04-25
type: source_summary
domain: [CPET, exercise_physiology, methodology]
tags: [critical_power, W_prime, performance_modeling, mathematical_model, review_article]
source_tier: 1
evidence_level: emerging
confidence: high
contested: true
contradictions:
  - Different CP/W' model forms can yield similar CP but materially different W' estimates from the same data.
  - Group-derived recovery models do not fully capture intra-individual variability or individual W' recovery kinetics.
---

# Sreedhara et al. 2019 — A Survey of Mathematical Models of Human Performance Using Power and Energy

## 一句話定義

這篇 review article 的核心價值，不是再證明 CP model 多有名，而是把整個 power-based performance modeling 的優缺點攤開來看：**two-parameter CP model 最實用，但 W'、recovery 與 intra-individual variability 仍是大缺口**。

## 核心機制

### 這篇回顧整理了什麼

- 兩參數 CP/W' model
- three-parameter 與 exponential model
- CWR、ramp、3-min all-out 等估計 protocol
- W' recovery model 的現況與限制

### 1. two-parameter CP model 最流行，但不是完美

- `P = CP + W'/t` 易懂、可計算、應用最廣。
- 主要問題：
  - `t -> 0` 時 `P -> infinity` 不合理
  - 「CP 可無限維持」也只是理論近似
  - 同一組資料用不同線性化或擬合方式，W' 可能差很多

### 2. CP 比 W' 穩定，W' 更容易漂移

- review 明確指出：不同模型往往得到相近 CP，但 **W' estimate 比較不穩**。
- 這使得跨研究或跨 protocol 比較 W' 時必須保守。

### 3. protocol 本身就會改變估計值

- CWR 是傳統金標，但耗時、受 predicting trial duration 影響。
- 3MT 有實用性，但也受設備、procedure 與 individual variability 影響。
- ramp-based approaches 可節省時間，但 W' 可能低估或高估。

### 4. recovery model 仍不足

- 現有模型大多聚焦於 >CP 的 W' expenditure。
- recovery in sub-CP domain 的模型較少，且需要 refinement 才能真實支援 real-time optimization。
- 作者明講：若要把 model 用於 performance optimization，必須更好處理 W' recovery。

### 5. intra-individual variability 是現有模型的盲點

- 這篇文獻反覆強調 **IIV**。
- group average parameter 對 individual prescription 幫助有限。
- 若不處理 IIV，就容易把 test-to-test noise 誤讀成真實 adaptation。

## 臨床表現

### 對現有 wiki 的意義

- 這是 [[../04_CPET/Wprime_Balance_Model]] 與 [[../04_CPET/CP_Test_Reliability]] 很重要的上游 review。
- 也能補強 [[../04_CPET/Critical_Power]] 內「模型不等於生理真相」的 caveat。

## 評估方式

### 對 testing 的方法學提醒

- protocol、cadence、fitting approach 都會影響 CP/W' output。
- 若研究或臨床要 longitudinal follow-up，最好先定義：
  - 用哪種 protocol
  - 用哪種 model fit
  - 如何處理 IIV

## 治療原則

- 本頁以概念或來源為主；若要進入真正 training prescription，需連回主題頁。

## 臨床決策點

### 核心 caveat

- 這篇回顧支持 CP model 的實用性，但不支持把任一數學形式當成唯一正確生理定律。
- 對 W' recovery，作者立場很清楚：目前 models 還不夠成熟。

## 限制與未定論

### frontmatter contradictions

- Different CP/W' model forms can yield similar CP but materially different W' estimates from the same data.
- Group-derived recovery models do not fully capture intra-individual variability or individual W' recovery kinetics.

## 理解缺口

- 若 CP 相近但 W' 差很多，哪一種情境最容易讓訓練處方失真？
- IIV 要怎麼在臨床或 field testing 中被實際納入？

## 臨床使用版

- 若你要用 CP/W' 做實務決策，先固定測試 protocol 與 model form，再談追蹤。
- 對 W' 的解讀要比 CP 保守，尤其在跨研究或跨設備比較時。

## 來源

### 證據標記

- 來源層級：1
- evidence_level：emerging
- confidence：high

### 書目

- Sreedhara VSM, Mocko GM, Hutchison RE.
- *Sports Medicine - Open.* 2019;5:54.
- 類型：**review article**
- 來源等級：**Tier 1**
- 可信度：**high**
- 原始檔：`C:\原始資料\Sreedhara et al. Sports Medicine- Open\Sreedhara et al. Sports Medicine- Open.md`

## 相關頁面

- [[../04_CPET/Critical_Power]]
- [[../04_CPET/Wprime_Balance_Model]]
- [[../04_CPET/CP_Test_Reliability]]
- [[../04_CPET/Training_Prescription_by_CP]]
