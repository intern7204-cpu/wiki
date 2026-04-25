---
title: Kemp, Taylor, Radda 1993 — Control of Phosphocreatine Resynthesis during Recovery from Exercise
created: 2026-04-22
updated: 2026-04-24
type: source_summary
domain: [exercise_physiology, muscle_metabolism]
tags: [PCr, phosphocreatine, oxidative_phosphorylation, ADP, 31P_MRS, recovery, mitochondrial_function]
source_tier: 1
evidence_level: consensus
confidence: high
contested: false
contradictions: []
---

# Kemp, Taylor & Radda 1993 — Phosphocreatine Resynthesis after Exercise

## 一句話定義

運動後 **PCr resynthesis 動力學**（用 ³¹P MRS 實測）反映淨 oxidative ATP 合成率；恢復時 **R（PCr resynthesis rate）對 [ADP] 呈 hyperbolic 關係（Km ≈ 30 µmol/L 細胞水、Vmax ≈ 40 mmol/L/min）**，對 [Pi]/[PCr]/[creatine] 呈 **線性** 關係，可用於活體評估粒線體功能。

## 核心機制

### 核心概念

### PCr recovery 是 oxidative ATP synthesis 的 in vivo 指標

- Recovery 期間：
  - 無外在 mechanical work
  - [ATP] 恆定
  - Glycogenolysis 已停
- 故 PCr resynthesis rate（R, mmol·L⁻¹·min⁻¹）= 淨 oxidative ATP 合成率（基礎率 0.8 mmol·L⁻¹·min⁻¹ 之上）。

### 兩個主要控制假說（粒線體 ATP 合成）

1. **ADP control**：cytosolic [ADP] 在 adenine nucleotide translocase 作用；hyperbolic Michaelis-Menten 關係；常將 [Pi] 納入。
2. **Free energy control**：線性受 free energy of ATP hydrolysis（ΔG）控制；常用於 submaximal 範圍。

ΔG' = ΔG°' + RT·ln{[ADP]·[Pi]/[ATP]}

### 重要生化約束

Creatine kinase 平衡公式：
`[ADP]/[ATP] = {([total Cr]/[PCr]) − 1} · (1/K) · 10^pH`

因此 [PCr]、[ADP]、pH **強烈相關**；[PCr + Pi] 在運動期間近似恆定。

### 主要發現

### 1. R 對 [ADP] 呈 hyperbolic

- **Km ≈ 30 µmol/L cell water**
- **Vmax ≈ 40 mmol·L⁻¹·min⁻¹**（human forearm fds）
- 人類 gastrocnemius 類似；犬 gracilis ~35；大鼠 leg ≥50 mmol·L⁻¹·min⁻¹。
- 關係在整個 recovery 過程維持。

### 2. R 對 [Pi] 呈線性

- [Pi] 與 [PCr]、[creatine] 藉 CK 平衡緊密相關 → 也呈線性。
- ΔG vs [Pi]：near-linear；ΔG vs [ADP]：non-linear。
- 在 recovery 中 [ADP] 回復快於 [Pi]（PCr halt-time ~0.9 min，ADP halt-time ~15 s）。

### 3. 疾病狀態的異常模式

| 疾病 | [ADP] 恢復行為 | [PCr] τ |
|------|----------------|---------|
| 正常 | ~30 µmol/L peak | 0.9 min |
| 糖原分解障礙（McArdle） | 極高（~105 µmol/L）；pH 不降 | 快 |
| 高血壓 | 較高 [ADP] | 變長 |
| 甲狀腺功能低下 | 較高 [ADP] | 變長 |
| 甲狀腺功能亢進 | 較低 [ADP] | 較快 |
| 嚴重粒線體肌病 | [ADP] 特高，PCr τ > 100 s | **顯著慢** |
| 肌強直性肌病 | 較高 [ADP] | 變長 |

→ PCr recovery τ 是 **in vivo 粒線體功能的敏感度量**，臨床 mitochondrial myopathy 診斷與研究用。

### 方法學

- ³¹P MRS；1.9 T、2.5 cm 單圈 surface coil。
- 運動肌：**right flexor digitorum superficialis**（前臂）、部分 gastrocnemius 研究。
- 運動任務：bulbsqueeze 或 weight pull。
- 取樣密度：恢復前 4 × 16-scan（第一 data point at t = 0.27 min）；之後 4 × 32-scan；最後 2 × 64-scan。
- 關鍵計算：
  - [Pi]、[PCr]：來自 Pi/β-ATP 與 PCr/β-ATP 訊號比（假設 [ATP] = 8.2 mmol/L cell water）。
  - 細胞內 pH：Pi 相對於 PCr 的化學位移：`pH = 6.75 + log[(δ − 3.27)/(5.69 − δ)]`
  - [ADP]：由 CK 平衡計算（假設 total Cr = 42.5 mmol/L、K = 1.66×10⁹/mol）。

### 對既有 wiki 的整合

- 強化 [[../04_CPET/Critical_Power]] 的「W' 底層機制」與「W'BAL 時間常數」段落。
- 強化 [[../04_CPET/VO2_Kinetics]] 的「mitochondrial capacity 與 τV̇O₂ 連結」。
- 新建 [[../05_Exercise_Physiology/PCr_Resynthesis]]：以此為主幹。

## 臨床表現

### 臨床與研究意義

### 1. 實驗診斷用途
- PCr 恢復 τ 顯著延長 → 粒線體功能異常（高靈敏性）。
- 運動後 [ADP] peak 特別高而 pH 不降 → glycogenolytic defect（McArdle、myophosphorylase 缺失）。
- 用於區分 primary mitochondrial myopathy vs secondary metabolic abnormality。

### 2. 與 exercise physiology 的連接

- **W' reconstitution 底層機制**：W' 恢復半時 ~234 s（Ferguson 2010；[[Jones_Vanhatalo_2017_critical_power_concept]]），PCr 恢復半時 ~54–74 s → PCr 先恢復，W' 追隨但更慢（顯示 W' 不等同於 PCr 單獨儲備，但強相關）。
- **V̇O₂ kinetics** 的 τV̇O₂（Phase 2）~25–45 s，與 PCr 動力學時間常數相近 → 強化 τV̇O₂ 作為 mitochondrial capacity 的反映（Grassi 1996、[[../09_來源摘要/Gaesser_Poole_1996_VO2_slow_component]]）。
- **Critical power** 在 >CP 運動中 [PCr] 持續下降、不達 steady state → 與 Goulding-Rossiter critical [Pi] 假說一致（[[Goulding_2021_VO2_kinetics_exercise_tolerance]]）。

### 3. 對訓練適應的詮釋
- Endurance training → PCr resynthesis τ ↓（更快恢復）。
- 這與粒線體密度上升、mitochondrial ADP sensitivity 增加 一致。

## 評估方式

- 目前頁面尚未整理出 History、Physical examination、Scale / test、Imaging / lab 的實際用法。

## 治療原則

- 本頁以概念或來源為主；若要進入真正 treatment plan，需連回對應臨床頁。

## 臨床決策點

- 什麼情況要治療？先看是否真的改變 pain、function、safety、participation 或訓練輸出。
- 什麼情況要轉介？遇到 red flags、診斷不確定、需要程序性介入或超出本頁可處理範圍時。
- 什麼情況不該做？當證據不足、機制不合、風險高於預期收益，或結果不會改變決策時。

## 限制與未定論

### 限制

- [ADP] 與 [PCr]、pH 的強制約束使 **完全分離獨立控制因子**在 in vivo 實驗非常難（需要 pH 能自由變動的情境，如 glycogenolytic 疾病）。
- MRS 訊號平均了全肌 fiber 分布，不能區分個別 fiber 或 motor unit。
- 單一實驗室、單一肌肉（fds）資料佔多數。
- 2.5 cm surface coil 的深度與空間解析度有限。

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

- Kemp GJ, Taylor DJ, Radda GK.
- *NMR in Biomedicine* 1993;6(1):66–72. DOI: 10.1002/nbm.1940060111.
- 類型：**research review with integrated data analysis**（Oxford MRC Biochemical & Clinical MR Unit 多實驗資料整合分析）。
- 來源層級：**Tier 1**（方法學 + 機制經典 review）。
- 原始檔：`原始資料/PHOSPHOCREATINE RESYNTHESIS AFTER EXERCISE/PHOSPHOCREATINE RESYNTHESIS AFTER EXERCISE.md`

## 相關頁面

### 相關 wiki 頁面

- [[../05_Exercise_Physiology/PCr_Resynthesis]]
- [[../05_Exercise_Physiology/Skeletal_Muscle_Energy_Metabolism]]
- [[../04_CPET/Critical_Power]]
- [[../04_CPET/VO2_Kinetics]]
- [[../04_CPET/VO2_Slow_Component]]
- [[Goulding_2021_VO2_kinetics_exercise_tolerance]]
- [[Jones_Vanhatalo_2017_critical_power_concept]]
