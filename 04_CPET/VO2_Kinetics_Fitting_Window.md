---
title: VO2 Kinetics Fitting Window
created: 2026-05-05
updated: 2026-05-05
type: concept
domain: [CPET, exercise_physiology, methodology]
tags: [VO2_kinetics, fitting_window, phase_1, phase_2, monoexponential_model, breath_by_breath]
sources:
  - 10_來源摘要/Francescato_Cettolo_2021_VO2_fitting_window.md
source_tier: 3
evidence_level: limited
confidence: medium
contested: true
contradictions:
  - Fixed 20-second removal is common, but this source shows it is not a neutral default.
  - Selecting the shortest tau alone can over-shift the fitting window and worsen parameter precision.
---

# VO2 Kinetics Fitting Window

## 一句話定義

VO2 kinetics fitting window 是決定要從 breath-by-breath VO2 onset data 中移除多少起始資料，再用 monoexponential model 估計 phase 2 time constant 的方法學設定；它會實質改變 `tau`，因此不是背景小參數。

## 核心機制

### 來源支持的事實

- Francescato & Cettolo 2021 分析 25 位 healthy adults 的 moderate-intensity step exercise breath-by-breath VO2 responses。
- 同一篇來源另外建立 `10^4` 個 simulated biexponential responses。
- 每條 response 都用 monoexponential model 重複 fitting `61` 次。
- 每次 fitting 從起始資料中移除不同長度的 `Delta Tr`，從 `0 s` 到 `60 s`，每次增加 `1 s`。
- 研究比較四種決定 removal window 的方法：`20 s-w`、`Min-tau`、`Min-ASEtau`、`Mixed`。
- 在 experimental data 與 simulated data 中，minimum estimated `tau` 大約都出現在 `Delta Tr ~= 35 s`。
- 該處估到的 `tau` 約比 `Delta Tr ~= 0 s` 低 `30%`。
- `ASE` 在 `Delta Tr ~= 35 s` 前相對穩定；超過此範圍後明顯惡化。
- simulated data 中，`20 s-w` method 對 `tau` 的 coverage 約 `85%`，`Mixed` method 約 `92%`。

### 推論

- 如果 fitting window 太早開始，phase 1 cardiodynamic component 會混入 phase 2 fitting，使 `tau` 被估得較慢。
- 如果 fitting window 往後移太多，可用資料減少並增加不穩定估計，讓 confidence interval 或 ASE 惡化。
- 因此 fitting window 是一個 model assumption，會改變 physiology inference，而不只是 software setting。

### 假設

- 本頁假設使用者的目標是估計 moderate-intensity fundamental phase 2 VO2 kinetics。
- 本頁假設資料型態是 breath-by-breath pulmonary VO2 onset data，而不是 muscle-level PCr kinetics 或 PRBS protocol。

## 操作邏輯

### 反對論點

固定移除前 `20 s` 已經是常見慣例，足以排除 phase 1；因此不需要每次重新考慮 fitting window。

### 反駁

這篇來源顯示 `tau` 會隨 `Delta Tr` 產生約 `30%` 的差異；而且 `20 s-w` 在 simulated responses 的 coverage 低於 `Mixed` method。這代表 `20 s` 可以是可報告的慣例，但不能被當成中性的生理常數。

另一個錯誤方向是只選最短 `tau`。來源指出 precision 不會無限制改善；當移除範圍太長時，ASE 會惡化。因此最短 `tau` 不是自動最佳，必須同時看 precision。

### 結論

在 VO2 kinetics analysis 中，fitting window 應被明確報告，並和 model choice、phase 1 exclusion、parameter precision 一起解讀。

## 評估方式

### 最低報告欄位

- exercise intensity domain：本來源只直接支持 moderate-intensity onset。
- transition design：step exercise，非 ramp、PRBS 或 off-transient recovery。
- data type：breath-by-breath pulmonary VO2。
- baseline definition。
- phase 1 / early data removal rule：例如 fixed `20 s`、minimum `tau`、minimum `ASEtau` 或 mixed criterion。
- fitting model：本來源分析 monoexponential fitting。
- parameter precision：至少報告 ASE 或 confidence interval。

### 常見誤讀

- 把 `tau` 當成純 physiology，不檢查 preprocessing。
- 把 `20 s` 當作 universal phase 1 duration。
- 只挑最小 `tau`，忽略 confidence interval / ASE。
- 把 moderate-intensity 的 fitting rule 直接外推到 heavy、severe 或 patient cohorts。

## 臨床與研究意義

- 研究比較不同 paper 的 `tau` 時，必須先確認 fitting window 是否一致。
- 同一個 raw VO2 response 可因不同 `Delta Tr` 得到不同 `tau`；因此跨研究差異不一定全是 physiology。
- 在 clinical CPET 或 rehabilitation research 中，若 `tau` 被用來推論 oxidative response speed，preprocessing rule 必須先透明。

## 限制與未定論

### 來源限制

- 來源主要處理 healthy adults 的 moderate-intensity exercise。
- simulated data 由 biexponential model 生成，仍含模型假設。
- 研究重點是 parameter recovery 與 fitting behavior，不是 clinical outcome。
- 沒有直接證明同一方法適用於 heart failure、pulmonary hypertension、frailty、children 或 trained athletes。

### 不確定

- heavy / severe domain 的最佳 fitting window 是否相同仍不確定。
- off-transient VO2 recovery 的 fitting window 是否可沿用本邏輯仍不確定。
- 不同 binning、outlier removal、interpolation 與 ensemble averaging 對 fitting window 的交互作用仍需另查來源。

## 臨床使用版

如果 `tauVO2` 會影響你的判讀，先問三件事：

1. 這是 moderate、heavy 還是 severe domain？
2. phase 1 / 起始資料移除了幾秒，理由是什麼？
3. `tau` 的 precision 如何，是否只因 window 選擇而改變？

若這三點無法回答，不應把 `tau` 當作穩定的個體生理特徵。

## 來源

### 來源摘要連結

- [[10_來源摘要/Francescato_Cettolo_2021_VO2_fitting_window]]

### 相關頁面

- [[VO2_Kinetics]]
- [[CPET_Protocol_Design]]
