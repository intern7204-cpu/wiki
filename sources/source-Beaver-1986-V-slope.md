---
type: source
tags: [exercise-physiology, gas-exchange, anaerobic-threshold, methods, classic-paper]
created: 2026-06-10
---

# 來源：A new method for detecting anaerobic threshold by gas exchange（V-slope 法）

## 出處
- **作者**：William L. Beaver, Karlman Wasserman, Brian J. Whipp（Harbor-UCLA Medical Center / UCLA School of Medicine）
- **年份／出處**：*Journal of Applied Physiology* 60(6): 2020–2027, 1986.
- **原始檔**：`C:\原始資料\A new method for detecting anaerobic threshold by gas exchange\`（含 `.md` 全文、`_meta.json`、7 張圖）
- **類型**：原始研究論文（方法學＋10 名健康男性受試者驗證）

## 核心主張
可以**不抽血**、純用呼吸氣體偵測無氧閾值（AT）：把每分鐘 CO₂ 輸出（VCO2）對每分鐘耗氧（VO2）作圖，用電腦化雙段線性迴歸找出曲線「斜率變陡」的拐點——那點標記了乳酸累積後經碳酸氫根緩衝所產生的「過量 CO₂」之起點。此即 **V-slope 法**；它比依賴通氣反應的舊方法更可靠、重現性更好、適用範圍更廣。

## 本份新增／更新的概念
本份是空 wiki 的第一次 ingest，以下概念皆為**新增**（依依賴順序）：

基礎層
- [[Cellular respiration]]（新增：支援 VO2/VCO2/乳酸的前置生化常識）
- [[VO2]]（新增：耗氧量＝代謝率的直接指標，本法的橫軸自變數）
- [[VCO2]]（新增：CO₂ 輸出，含「代謝性＋緩衝性」兩個來源）
- [[Lactate]]（新增：乳酸與無氧醣解，酸 H⁺ 的來源）
- [[Incremental exercise test]]（新增：每分 15 W 遞增至力竭的測試設計）

機制／閾值層
- [[Bicarbonate buffering of lactic acid]]（新增：H⁺ ＋ HCO₃⁻ → CO₂，約 22 mL/meq）
- [[Excess CO2 output]]（新增：扣掉純代謝後多出的那份 CO₂，即偵測訊號）
- [[Lactate threshold]]（新增：血乳酸開始持續上升的點，AT 的血液版）
- [[Anaerobic threshold]]（新增：本份核心；氣體交換 AT 與 LT、HCO₃⁻ 閾值的對應）

方法層
- [[V-slope method]]（新增：本文獻的headline 貢獻，含計算流程與資料整理）
- [[Respiratory compensation point]]（新增：AT 之上、通氣為代償酸中毒而暴衝的第二轉折）

## 與既有知識的關係
- **一致／奠基**：wiki 先前為空，本份建立了 exercise-physiology 領域的**基礎概念層**，後續文獻（如 CPET 總論、Critical Power、VO2 kinetics 等）可直接連回這些頁作為前置概念。
- **內部交叉引用**：[[Anaerobic threshold]] 同時被 [[Lactate threshold]]、[[Excess CO2 output]]、[[V-slope method]]、[[Respiratory compensation point]] 指向，構成本份的中心節點。
- **尚無矛盾**：因為是第一份，無與既有頁衝突之處。唯一需註記的張力是學界對「anaerobic threshold」此命名與機制的長年爭議——已在 [[Anaerobic threshold]] 的「易誤解之處」標明。
  - **後續更新（2026-06-10）**：此爭議已由 [[source-Poole-2021-AT-controversy]]（Poole 2021）補強。Poole 等人否證了「無氧/缺氧」機制，但**不推翻本文獻的方法**——V-slope/GET 偵測技術與所有數據仍然成立，只是對「它在偵測什麼機制」的理解由「缺氧」改為「乳酸緩衝＋[[Lactate appearance and disappearance|Ra/Rd]] 失衡」。本文的「無氧閾值（AT）」一詞在機制面建議改稱 [[Gas exchange threshold|GET]]。

## 關鍵數據（備查）
- 氣體交換 AT（V-slope）平均 VO2 = 1.83 ± 0.30 L/min；估計的 HCO₃⁻ 閾值 = 1.78 ± 0.24 L/min（無顯著差異）。
- 氣體交換 AT 對應「LT 之上約 0.50 ± 0.34 meq/L」。
- RC 點平均 VO2 = 2.51 ± 0.42 L/min（一致高於 AT）；RC ≈ 75% VO2max，AT ≈ 73% RC。
- 重現性：V-slope 變異係數 ≈ 0.023 vs 專家目視 ≈ 0.127（V-slope 明顯更穩）。
