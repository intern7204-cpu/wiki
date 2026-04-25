---
title: Blemker, Brooks, Esser, Saul 2023 — Fiber-type Traps
created: 2026-04-22
updated: 2026-04-24
type: source_summary
domain: [exercise_physiology, muscle_biology]
tags: [muscle_fiber_type, myosin, MHC, oxidative_capacity, CSA, fiber_classification, misconceptions]
source_tier: 1
evidence_level: consensus
confidence: high
contested: false
contradictions: []
---

# Blemker et al. 2023 — Fiber-type Traps

## 一句話定義

「肌纖維型」被過度簡化為 slow/fast、red/white、I/IIa/IIx 的一對一對應系統；實際上 **myosin isoform、oxidative capacity、fiber CSA、force-generating capacity 分別來自不同生理軸**，彼此只部分重疊。三個常見錯誤假設必須釐清。

## 核心機制

### 三個 fiber-type Traps

### Trap 1：將 myosin isoform 與 oxidative capacity 視為等價

**錯誤假設**：type I = slow + oxidative；type IIx/IIb = fast + glycolytic。

**實情**：
- Myosin 決定 **收縮速度**（contraction speed / ATPase activity）。
- Oxidative capacity 由**粒線體密度、SDH、NADH-TR 活性**決定。
- 兩者機制獨立，跨物種 / 肌肉 / 訓練狀態差異大：
  - **人**：MHC IIx 通常低 SDH → 類似「glycolytic」。
  - **大鼠**：MHC IIx 中等 SDH。
  - **小鼠**：MHC IIx 高 SDH → 反而接近「oxidative」行為。
- 同一 fiber type（如 type II）中 oxidative enzyme activity 可跨完整範圍（Nemeth 1980）。
- MHC IIb 在**人類肌肉極少表達**（過去誤標的「IIb」大多實為 IIx）。
- 訓練或 disease 下 fiber 可同時表達多種 MHC（**hybrid fibers**），反映 type transition。

**推論**：稱某肌肉為「oxidative」/「glycolytic」須用**直接代謝測量**（SDH、NADH-TR 或 mitochondrial density），不可僅以 MHC isoform 推論。

### Trap 2：將 fiber CSA 視為 myosin isoform 或 oxidative capacity 的代理指標

**錯誤假設**：fast fibers 大，slow fibers 小（基於「glycolytic fibers 需要較低 surface-to-volume 以少耗能」的理論）。

**實情**：
- 原始 Armstrong & Phelps 1984、Delp & Duan 1996 的 rat hindlimb 數據**不能推至其他肌肉、物種、性別**。
- **小鼠 C57BL/6**（Augusto 2017）：soleus 中 type I 比 type IIa 還大；gastrocnemius 中 type I 比 type IIa 大但比 type IId 小。
- **人類 vastus lateralis**（Jeon 2019）：男性 type IIA > type I；女性 type I 最大 → **性別依賴**。
- CSA **分布**高度重疊：即使平均差異顯著，個別 fiber 的 CSA 範圍跨度大（Encarnacion-Rivera 2020 自動化影像分析）。
- 表層 vs 深層肌腹 CSA 不同 → biopsy 位置偏誤。

**推論**：「fiber 大小預測 fiber type」不可作為單一指標；在人類 biopsy 的 CSA 比較需分性別、肌肉、depth。

### Trap 3：從 myosin isoform 推論 force-generating capacity

**錯誤假設**：fast fibers 產生較大 force。

**實情**：
- **Specific force**（每單位 cross-sectional area 的 force，即 force / PCSA）是 contractile function 的關鍵，但量測複雜。
- Single-fiber 或 skinned-fiber 實驗顯示：同一物種不同肌肉間 specific force 差異**不總是與 MHC isoform 對應**。
- Pennation、optimal fiber length、sarcomere operating range、tendon properties 全部影響 whole-muscle force－不能僅由 fiber type 分布推估。
- 體積外的 architecture 參數（e.g., pennation angle）在不同 muscle 之間差異高達 2–3 倍。

### 分類方法總覽（表 1 作者原表精簡）

| 方法 | 解析度 | 客觀性 | 複雜度 | 推薦用途 |
|------|-------|--------|--------|---------|
| 肌肉顏色（red/white） | Tissue | 主觀 | 低 | 只能描述，不可當 fiber 分類 |
| Myosin ATPase（pH-sensitive） | Fiber | 主觀 | 中 | 配 pH 敏感性做 I / IIa / IIx 區分 |
| **MHC antibody（immunofluorescence）** | Fiber | **客觀** | 低 | **當代 best practice** for MHC |
| SDH activity | Fiber | 主觀 | 中 | oxidative capacity marker |
| NADH-TR | Fiber | 主觀 | 中 | oxidative marker（也含 SR 貢獻） |
| Fiber CSA | Fiber | 客觀 | 高 | morphology only（見 Trap 2） |
| Contraction velocity | Muscle | 客觀 | 高 | functional property |
| Specific force | Muscle / Fiber | 客觀 | 高 | functional property（見 Trap 3） |
| Fatiguability | Muscle | 主觀 | 高 | functional；高度依賴刺激 protocol |

### 正確使用「fiber type」的原則（Brooke & Kaiser 1970 的 50 年前建議）

1. 分類須基於**欲檢測的特定屬性**（收縮速度 OR 代謝 OR 力量 OR 疲勞特性）。
2. 分類須有**實驗或病理上可應用**的價值。
3. 須允許**清楚的類別區分**，避免連續漸變被強行二分。
4. **勿假設不同分類系統可互換**。

### 對既有 wiki 的整合點

### [[../04_CPET/VO2_Slow_Component]] 的 fiber type 解釋要更精準

原有敘述「type 2 fiber recruitment 造成 efficiency 下降」仍正確，但應補：
- 「type 2」在此指 **MHC 分類下的快 fiber**；不等於其 oxidative capacity 低。
- 人類 heavy exercise 徵召順序不能簡化為「先慢後快」（還受 cadence、load、fatigue 影響）。

### [[../05_Exercise_Physiology/Skeletal_Muscle_Energy_Metabolism]]

- 「nutrient partitioning（CHO vs fat）依 fiber type」的敘述要補註：MHC isoform 不完全預測代謝特徵。

### 新建 [[../05_Exercise_Physiology/Muscle_Fiber_Types]]

- 以本篇為主幹，整合 MHC 分類、代謝分類、CSA、force 屬性 的獨立性。

## 臨床表現

- 目前頁面尚未整理出可直接辨識的症狀、檢查發現或 red flags。

## 評估方式

- 目前頁面尚未整理出 History、Physical examination、Scale / test、Imaging / lab 的實際用法。

## 治療原則

- 本頁以概念或來源為主；若要進入真正 treatment plan，需連回對應臨床頁。

## 臨床決策點

- 什麼情況要治療？先看是否真的改變 pain、function、safety、participation 或訓練輸出。
- 什麼情況要轉介？遇到 red flags、診斷不確定、需要程序性介入或超出本頁可處理範圍時。
- 什麼情況不該做？當證據不足、機制不合、風險高於預期收益，或結果不會改變決策時。

## 限制與未定論

- 目前頁面尚未明確寫出證據限制、教材未講清楚處或不同來源可能衝突之處。

## 理解缺口

- 這份來源哪些部分是在建立主框架，哪些部分只是作者的解釋或延伸？
- 若 guideline、review 或新版 textbook 和本來源不同，主幹應如何更新？
- 這份來源最值得直接回填到哪個主題頁，哪些段落不該過度外推？
- 目前缺少完整評估框架：History、Physical examination、Scale / test、Imaging / lab 仍需補強。
- 目前缺少明確處置順序：何時觀察、何時介入、何時轉介仍需補強。

## 臨床使用版

- 若要更新主題頁，先用這份來源建立主框架，再用 guideline / review 校正 treatment threshold 與爭議點。
- 不要把單一 textbook chapter 或單篇文章的語句直接當成全域共識；先看它在整個證據層級中的位置。

## 來源

### 證據標記

- 來源層級：1
- evidence_level：consensus
- confidence：high

### 書目

- Blemker SS, Brooks SV, Esser KA, Saul KR.
- *J Neurophysiol* 2024;131(4):763–777（實際發表 2024，arXiv/preprint 2023 年底；原檔標題標示 2023）。DOI: 10.1152/jn.00337.2023.
- 類型：**perspective / synthesis review**（跨 biomechanics、motor control、cell biology、muscle physiology）。
- 來源層級：**Tier 1**。
- 原始檔：`C:\原始資料\blemker-et-al-2023-fiber-type-traps-revisiting-common-misconceptions-about-skeletal-muscle-fiber-types-with-application\blemker-et-al-2023-fiber-type-traps-revisiting-common-misconceptions-about-skeletal-muscle-fiber-types-with-application.md`

## 相關頁面

### 相關 wiki 頁面

- [[../05_Exercise_Physiology/Muscle_Fiber_Types]]
- [[../05_Exercise_Physiology/Skeletal_Muscle_Energy_Metabolism]]
- [[../04_CPET/VO2_Slow_Component]]
- [[../04_CPET/VO2_Kinetics]]
- [[../04_CPET/Critical_Power]]
