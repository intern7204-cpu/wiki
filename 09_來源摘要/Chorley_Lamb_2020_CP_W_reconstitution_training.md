---
title: Chorley & Lamb 2020 — Application of Critical Power, W' and Its Reconstitution for Cycling Training Prescription
created: 2026-04-22
updated: 2026-04-24
type: source_summary
domain: [CPET, exercise_physiology]
tags: [critical_power, W_prime, W_BAL, training_prescription, cycling, 3_min_all_out, ramp_all_out]
source_tier: 1
evidence_level: consensus
confidence: high
contested: false
contradictions: []
---

# Chorley & Lamb 2020 — CP, W' and Reconstitution for Training Prescription

## 一句話定義

CP 是 heavy–severe 強度域的生理邊界，比 functional threshold power（FTP）更科學；W' 與 W'BAL 提供了在 severe 域內**個別化量化**訓練強度與時間的工具。

## 核心機制

### 五個 CP 模型假設（作者明列）

1. 有氧供能對任何時長均為無上限（=CP 可永遠維持）
2. Cycling efficiency 恆定
3. Power 僅受時間限制，t→0 時 P→∞
4. ≤ CP 時 ATP 需求瞬間由有氧完全滿足
5. 衰竭時 W' 完全耗盡（W' = 0 J）

### 假設的實際侷限
- 「CP 永遠可維持」：TTE at CP 實測 20–40 min（Brickley 2002）至 >1 h（Jones 2010）；>80 min heavy cycling 會使 CP 下降（Clark 2019），但補充 CHO 可維持至 120 min。W' 於 40 min 開始下降（各 condition 均有）。
- Efficiency：>80 min 後因 CHO→fat 轉換而下降（更高 metabolic cost）。
- 「t→0 時 P→∞」：三參數模型（Morton 1996）試圖修正但產生過低 CP、過高 W'。
- 「ATP 瞬間匹配」：實際有 τV̇O₂ 延遲 → 測試中部分 W' 被 aerobic onset 延遲耗掉（不易量化）。
- 「exhaustion = W' = 0」：有文獻顯示 TTE 後再追加 30 s all-out 仍能產功 → W' 沒真正耗盡（Black 2017）；受動機、痛感、central fatigue 影響。

### W' Reconstitution 深入

### Skiba W'BAL 模型

見 [[Jones_Vanhatalo_2017_critical_power_concept]]：

`W'BAL(t) = W' − ∫ W'exp · e^(−(t−u)/τW') du`

`τW' = 546 · e^(−0.01 · DCP) + 316`（Skiba 2012 經驗公式）

### Bartram 修正式（2018）

針對 **elite cyclists** 的 Skiba 模型高估偏差：

`τW'_Bartram = 2287.2 · e^(−0.0879 · DCP)`

相比 Skiba 模型，Bartram 在高 DCP（積極 recovery）時 τW' 更短 → 更準確反映精英選手快速 W' 重建。

### Integral form（Skiba 2015 修正）

- 原始 2012 模型假設恆定 CP 與 W'（於一次運動內）。
- 新版加入 CP 隨疲勞下降的修正（需要外部輸入）。

### 生理底層
- W' 恢復與 **PCr resynthesis 動力學**緊密相關（詳見 [[../05_Exercise_Physiology/PCr_Resynthesis]]）。
- 肌內 pH 與 [Pi] 回復也相關；Ca²⁺-handling、Carnosine 等 type 2 fiber 特徵亦影響。
- 多個 interval bout 後期 PCr recovery 變慢 → τW' 非真正恆定。

### 與其他 wiki 頁整合點

- 強化 [[../04_CPET/Critical_Power]]：補 CWR / 3AOT / Ramp all-out 三法比較、FTP vs CP 論述、Bartram 修正。
- 支援 [[../04_CPET/CPET_Protocol_Design]]：ramp all-out 作為**同時測 GET + CP**的高 CP/W' 實務選擇。
- 新建 [[../04_CPET/Training_Prescription_by_CP]]：以此篇作為主幹 source。

## 臨床表現

- 目前頁面尚未整理出可直接辨識的症狀、檢查發現或 red flags。

## 評估方式

### 三種 CP 測試法比較

### 1. Constant Work Rate（CWR；傳統金標）
- 3–7 次 TTE trials 散於不同日，每次 2–15 min 至 exhaustion。
- 三種回歸：非線性 P–t、線性 W–t、線性 P–1/t。
- **主要問題**：
  - TTE 可靠性差，受 learning effect、動機、central fatigue 影響。
  - Short TTE 拉高 CP、降低 W'；long TTE 影響方向相反。
  - Self-paced TT 比 CWR 產生 **更高 CP**（Black 2015：265 vs 250 W）。
- 選擇最佳擬合模型 ≠ 最準的 CP/W'（受測者只會 under-perform 不會 over-perform 自己）。
- 實務負擔重：≥4 次實驗室訪視。

### 2. 3-min All-out Test（Vanhatalo 2007）
- 單次 3 min 全力、固定阻力（使 preferred cadence 下達到預估 CP）。
- CP = 最後 30 s 平均；W' = 上方總功。
- **優勢**：單次、同時可得 GET（搭配預先 ramp）。
- **問題**：
  - Invalid rate 高（未完全耗盡、power 未 plateau）。
  - Cadence 敏感：end cadence 高出 preferred 10 rpm 可顯著改變 CP。
  - 前 80 s 前 V̇O₂ 尚未達 peak → W' 可能被低估。
  - 末 60 s 仍有上下波動 → W' 可能被小幅高估。

### 3. Ramp All-out Test（Murgatroyd 2014；改良：Burnley 2014）
- Ramp（常用 20 W/min）直到 exhaustion → 立即轉入 3 min（或 2 min）all-out 階段。
- CP = all-out 末 30 s 平均；W' = ramp + all-out 超過 CP 的總功。
- **最大優勢**：單一 test 同時得 CP、W'、GET（gas analysis 可在 ramp 中做 V-slope）。
- 失敗率 < 3AOT；motivational burden < CWR。
- 可能微幅 underestimate W'（ramp 起始 aerobic 跟進延遲）。

## 治療原則

### 訓練處方應用

### 傳統 FTP（Functional Threshold Power）的問題
- FTP = 最大 1 h 可維持 power（Allen & Coggan 2010 的騎行訓練語彙）。
- **實測 FTP 與 CP 有 5–10% 差異**；通常 FTP 略低於 CP。
- FTP 是測試便利性產物（單次 20 min × 95%）而非 physiological threshold。
- 以 CP 定位 heavy–severe 邊界更有生理基礎。

### 以 CP/W' 進行訓練分級

| Zone | 定位 | 建議應用 |
|------|------|----------|
| Z1 | <LT/GET | base aerobic |
| Z2 | LT–CP | heavy：提升 LT、mitochondrial |
| Z3 | >CP | severe：提升 V̇O₂max、CP |

### 間歇訓練個別化

利用 W'BAL 模型設計：
- 目標 W' 耗盡比例（如 50%、80%、100%）
- Work power、duration
- Recovery power（越低，τW' 越短，重建越快）
- 間歇次數預測

### 實戰負擔考量
- Ramp all-out 1 次可得 CP、W'、GET → 可作為 6–8 週 mesocycle 前後測。
- 市售功率計（已驗證）+ 訓練日誌估算 CP、preferred cadence → 避免實驗室 preliminary 測試。

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
- 目前缺少 bedside 可辨識表現：症狀、檢查發現或 red flags 仍需補強。

## 臨床使用版

- 若要更新主題頁，先用這份來源建立主框架，再用 guideline / review 校正 treatment threshold 與爭議點。
- 不要把單一 textbook chapter 或單篇文章的語句直接當成全域共識；先看它在整個證據層級中的位置。

## 來源

### 證據標記

- 來源層級：1
- evidence_level：consensus
- confidence：high

### 書目

- Chorley A, Lamb KL.
- *Sports (Basel)* 2020;8(9):123. DOI: 10.3390/sports8090123.
- 類型：**narrative review**（專注於 cycle training prescription 的實務橋樑）。
- 來源層級：**Tier 1**。
- 原始檔：`原始資料/The Application of Critical Power, theWork Capacity/The Application of Critical Power, theWork Capacity.md`

## 相關頁面

### 相關 wiki 頁面

- [[../04_CPET/Training_Prescription_by_CP]]
- [[../04_CPET/Critical_Power]]
- [[../04_CPET/VO2_Kinetics]]
- [[../04_CPET/VO2_Slow_Component]]
- [[../04_CPET/CPET_Protocol_Design]]
- [[Jones_Vanhatalo_2017_critical_power_concept]]
- [[Goulding_2021_VO2_kinetics_exercise_tolerance]]
