---
title: Skiba et al. 2015 — Intramuscular determinants of the ability to recover work capacity above critical power
created: 2026-04-25
updated: 2026-05-08
type: source_summary
domain: [CPET, exercise_physiology, methodology]
tags: [W_prime, PCr, 31P_MRS, 1H_MRS, carnosine, critical_power, recovery, W_BAL, original_article]
source_tier: 3
evidence_level: limited
confidence: medium
contested: true
contradictions:
  - Bulk [PCr] recovers ~6× faster than W' (T1/2 ≈ 39 s vs 232 s) under the same conditions, so W' should not be treated as a pure phosphocreatine store.
  - τ_PCr and interpolated τ_W' are not significantly correlated (r = 0.38, p = 0.28); D[PCr] (oxidative reserve, not bulk [PCr]) is what closely tracks the modelled W' recovery.
  - Single-leg knee-extension W' recovery appears statistically linear, while whole-body W' recovery is curvilinear; the authors propose summed-microscopic-linear → macroscopic-curvilinear, but this is hypothesis-level only.
  - The novel chemical-kinetics derivation (τ_W' = W'_0 / D_CP) replaces the empirical Skiba 2012 τ-fit but inherits assumptions of homogeneous diffusion and tank-like reactant behavior that are biologically implausible.
---

# Source Summary: Skiba et al. 2015 — Intramuscular determinants of the ability to recover work capacity above critical power

## Source Type

- 類型：original research article（human single-leg knee-extension exercise + 31P-MRS / 1H-MRS spectroscopy）。
- 出處：*Eur J Appl Physiol*（Received 2014-07-10；Accepted 2014-11-08；Springer 2014 / 印 2015）。
- 作者：Skiba PF, Fulford J, Clarke DC, Vanhatalo A, Jones AM。
- 原始檔：`C:\原始資料\s00421-014-3050-3\s00421-014-3050-3.md`。
- 通訊：A. M. Jones（University of Exeter）；Communicated by D. C. Poole。
- 補充材料：Appendix 1（chemical-kinetics derivation）、Appendix 2（microscopic-linear, macroscopic-curvilinear simulation）。

## Reliability Level

- 來源層級：3（依 wiki source_tier 慣例：original research article 標 3，與 Ferguson 2010、Caen 2021、Lievens 2024 同級）。
- 對應 AGENTS.md §4 第 5 級（original research article）。
- evidence_level：limited（n=10、single-leg knee-extension only、最早 W' time-point 為 60 s、carnosine R² 受單一 outlier 影響顯著）。
- confidence：medium。
- contested：true（W' 與 [PCr] 是否同源仍未定論；單腳模式的 linear 結果與 whole-body curvilinear 結果之間需橋接假說）。

## One-Sentence Summary

在 10 位健康受試者的 single-leg knee-extension MRI 模型中，**bulk `[PCr]` recovery 比 `W'` recovery 快約 6 倍（T1/2 ≈ 39 s vs 232 s）；但 `D[PCr]`（oxidative reserve, B_C 結束 [PCr] − B_E 耗竭 [PCr]）卻與 chemical-kinetics 推導出的 `W'` recovery 高度相關（r = 0.99）**——這支持 `W'` recovery 與 muscle 的「再可用 oxidative reserve」、而不是 bulk PCr 儲量本身一一對應。

## Core Concepts Extracted

### Concept: Intramuscular determinants of W' recovery（W' vs [PCr] vs pH vs carnosine）

#### One-Sentence Definition

`Intramuscular determinants of W' recovery` 在本研究的操作型定義是：使用 31P-MRS / 1H-MRS 同步追蹤 `[PCr]、[Pi]、pH、carnosine`，並以「conditioning bout / passive recovery / experimental bout」三段式 single-leg 模型，比較 `W'` recovery（以 W_BE / W_BC 估）與這些代謝指標的時間進程，從而判斷哪一條代謝量更接近 `W'` 的實際恢復行為。

#### Known Facts

- 受試者：10 位 healthy recreationally trained subjects（4F、6M；age `22 ± 7 yr`；height `1.71 ± 0.1 m`；body mass `71.8 ± 15.4 kg`）；3 位有 strength/power training 經驗，其餘為 endurance 取向；非高度訓練者。
- Phase 1（physiology lab）：3–5 段 single-leg knee-extension protocols to exhaustion（90–600 s）；以 metronome 維持 `40 extensions / min`；以 work（`m × g × h`）對 time 線性回歸求 CP（slope）與 W'（y-intercept）；線性度 `r² = 0.99–1.0`。
- Phase 2（1.5T MRI bore）：執行 4 次 trials，每次 conditioning bout（B_C）at `WR180`（預估 180 s 耗竭）→ passive 1 / 2 / 5 / 7 min recovery（leg fully extended on scanner bed）→ experimental bout（B_E）at the same `WR180` to exhaustion。
- W' recovery 估計：`W' recovery = work in B_E / work in B_C`（基於 Ferguson 2010 證實 prior exhaustion 不變動 CP）。
- 31P-MRS 採樣：每 12 s 一筆，spectral width 1500 Hz；以 jMRUI / AMARES fit `[Pi]、PCr、α/β/γ-ATP、PDE` peaks；intracellular pH 由 `Pi` 對 `PCr` 的 chemical shift 估。
- 1H-MRS：right rectus femoris voxel `20 × 30 × 50 mm`、PRESS、TR 2000 ms / TE 31 ms / 96 averages；以 water peak 為內標。
- Group means：CP `8.1 ± 2.79 W`；W' `1.14 ± 0.93 kJ`（單腳 absolute power 自然遠低於 cycle ergometer）。
- W' recovery：group mean `T1/2 = 232 ± 108 s`，個體範圍 `135–426 s`；group 線性回歸 `r = 0.99, p = 0.0009`；CUSUM 與 runs test 均不偏離線性。
- 60 s 時 W' 已恢復 `57%`，420 s 時恢復 `96%`。
- [PCr] recovery：group mean `T1/2 = 39 ± 16 s`（abstract 寫 `38 s`）；single exponential fit `r² = 0.99`、`τ ≈ 57 s`。
- B_C 結束時與 B_E 耗竭時的 `[PCr]、[Pi]、pH` 在所有 4 個 recovery 條件下 **無顯著差異**（`p = 0.98 / 0.31 / 0.07`）；代表耗竭的 metabolic endpoint 大致一致。
- `τ_[PCr]` 與 interpolated `τ_W'` **無顯著相關**（`r = 0.38, p = 0.28`）。
- W' 第二回合可用量 vs `D[PCr]`（B_C 結束 [PCr] − B_E 耗竭 [PCr]）`r = 0.99, p = 0.005`。
- 模型驗證：以新推導 `τ_W' = W'_0 / D_CP` 重算 Skiba 2012 的 7 名受試者 × 3 條件 → 與既有 `τ_W'` 線性相關 `r = 0.84, p = 0.001`；Passing–Bablok 顯示 systematic（`y intercept 288, 95% CI 235–350`）但非 proportional（`slope 0.79, 95% CI 0.59–1.26`）的偏差。
- 個體層次：模型 vs 觀測 `W'` 線性回歸 6/10 顯著（`r = 0.96–0.99`，`p = 0.01–0.03`，允許 non-zero intercept）；強迫 zero intercept 時 10/10 顯著（`r = 0.88–0.98`）。
- 沒有 carnosine 與 minimal pH / pH at exhaustion / pH 變化的相關。
- carnosine 與 `W' T1/2`：inverse curvilinear regression `R² = 0.55`；剔除單一 outlier 後 `R² = 0.80`。
- pH 與 `W'` 強度本身：在 B_C 與 B_E 中皆無顯著相關。

#### Mechanism Chain

1. supra-CP single-leg knee-extension 至耗竭 → muscle `[PCr]` 大幅降、`[Pi]` 升、pH 下降；同時 W' 被定義為被消耗。
2. Passive recovery 期間 leg 不再做 work：
   - `[PCr]` 由粒線體 oxidative phosphorylation 主導重建；single exponential T1/2 ≈ 39 s。
   - 但「下一段可動員的 W'」並不只看 bulk `[PCr]` 是否回到高水準，而看「再次 work 從目前 [PCr] 出發到耗竭點的可動員量」，亦即 `D[PCr]`。
3. 化學動力學類比（Appendix 1）：把 `W'` 視為一個反應槽中的反應物，dW'/dt 在耗竭期 ≈ −(P − CP)，恢復期 ≈ (1 − W'/W'_0)(CP − P) → 解析解 `W'(t) = W'_0 − W'_exp · exp(−D_CP · t / W'_0)`，亦即 `τ_W' = W'_0 / D_CP`。
4. 微觀 linear → 巨觀 curvilinear（Appendix 2）：若每條被招募的 fiber 或 motor unit 各自呈線性恢復，且 `W'_0` 與貢獻比例 `f_i` 在族群間異質，則加總後可形成觀察上的 curvilinear macroscopic recovery；單腳 small-muscle-mass 模式下，因為動員元件較少，可看到偏 linear 的形態。
5. carnosine 與 `W' T1/2` 的 inverse 關係，作者推論可能透過 Ca²⁺ sensitization、SR Ca²⁺ release、力 - 鈣關係調整等機制，而非單純 buffering（因 carnosine 對 pH 的 buffering 貢獻 < 15%）。

#### Inferences

- **`W' ≠ pure [PCr] tank`**：因 bulk `[PCr] T1/2 ≈ 39 s` 而 `W' T1/2 ≈ 232 s`，且 `τ_[PCr]` 與 `τ_W'` 不相關（`r = 0.38`）。
- **`W'` recovery 可能對應「再可用的 oxidative reserve」**（即 `D[PCr]` / `D VO2`），而不是「PCr 已經回到高位」；此推論延伸自 D[PCr] 與 model-predicted W' 的 r = 0.99 相關。
- **本研究的 single-leg 線性 W' recovery 與 whole-body 曲線形 W' recovery 的差異**，最簡單的解釋是 60 s 之前的 curvilinear 段未被取樣；備援解釋是「微觀線性、巨觀曲線」。兩者都是模型/取樣推論，不是直接觀察到的早期 dynamics。
- **carnosine 可能透過 Ca²⁺ sensitization / 力 - 鈣關係參與 `W'` 恢復，而非透過 pH buffering**；因 pH 與 W' 在本資料各層級皆不相關。
- 新 `τ_W' = W'_0 / D_CP` 推導，因為不需要對個別資料 fitting，理論上比 Skiba 2012 的經驗式 `τ_W' = 546 e^(−0.01·D_CP) + 316` 更可一般化；但 Passing–Bablok 顯示有 systematic offset，提示在實務上仍需以 individualized data 校準。

#### Assumptions

- prior exhaustion 不會改變 CP（沿用 Ferguson 2010）；因此 B_C 與 B_E 之間任何 work capacity 差異被歸給 `W'`。
- B_E 開始時 `W' = work_BE / work_BC × W'_0`；此 fractional definition 假設 W' 在 B_E 中以與 B_C 相同的方式被消耗。
- `WR180` 在 B_E 仍正確估計（即 prior exhaustion 不改變 power-tLIM 關係的形狀）。
- pulmonary VO2 / surface coil 量到的 PCr 訊號可代表 muscle metabolic state；但 surface coil 主要敏感的是 `rectus femoris`，異質性與其他協同肌可能未被完全表徵。
- 化學動力學模型假設 `W'` 反應物在「muscle tank」內 free diffusion 與 equal distribution；作者本人在 Discussion 中明文承認 muscle 是 spatially heterogeneous，這是 known violation。
- W' recovery 假定 60 s 後採樣足夠捕捉曲線形狀；但 60 s 已有 57% 恢復，故曲線早段資料缺。
- 線性 vs 曲線 best-fit 比較使用 group mean；個體層次的 within-subject 動力學被群體化，可能掩飾個體曲線特徵。
- Phase 1 用 work 對 time 的線性回歸求 CP / W'，與 cycle ergometer 常用的 `P` 對 `1/tLIM` 形式不同；不同模式間的 W'、CP 值不可直接互換。

#### Uncertainties / Limitations

- 樣本 `n = 10`，4F/6M、young recreationally active；無女性次群體分析、無 trained athletes、無心肺族群、無高齡。
- 模式為 single-leg knee-extension（small muscle mass、`CP ≈ 8.1 W`、`W' ≈ 1.14 kJ`）；外推到 cycling、rowing、running、whole-body 須極為保守。
- 最早 `W'` time-point 為 60 s；早期 curvilinear dynamics 無法在本資料判定。
- 採用 passive recovery（leg 完全靜止），與 field 與 cycle 研究中的 active recovery（20 W、`P_GET` 等）不同；recovery power 對 `τ_W'` 的影響在本研究中無法估。
- carnosine vs `W' T1/2` `R² = 0.55`，且 `R²` 提升到 0.80 仰賴剔除單一 outlier；屬 exploratory。
- 化學動力學假設 free diffusion / homogeneous reactant，作者已承認 muscle 為異質結構；模型成功不等於 mechanism 已成立。
- 個體 `τ_W'` 範圍 `135–426 s`，inter- / intra-individual variability 大；`τ_W' = W'_0 / D_CP` 在個體層次仍需 case-by-case 校準。
- pH、`[Pi]`、carnosine 等次發現受 sample size 限制；獨立樣本驗證仍缺。
- 模型 vs 觀測的線性相關，作者強調「不等於 W' 與 PCr 的真實 mechanistic identity」。

## Clinically Useful Points

- 對 high-intensity interval prescription 的影響：**`PCr` 看起來「回得很快」≠ `W'` 同步回來**；「短休息呼吸看起來緩過來」與「下一段可上 supra-CP 工作預算」不是同一件事。
- 對運動處方解釋：若教練 / 選手以「PCr 已回 80%」當作下一組 readiness 的代理，本研究結果反對此粗略換算；個體差異 `135–426 s` 提醒 single-formula 處方有風險。
- 對 rehabilitation cycling 解釋：本資料來自 single-leg knee-extension 的小肌群模式；應用到 hemiparesis、孤立膝伸展訓練時可作 mechanistic 框架，但全身復健與本資料相距遠，不可機械式套 `T1/2`。
- 對營養 / 補充劑討論（β-alanine / carnosine）：本研究只提供 inverse curvilinear 訊號（`R² = 0.55–0.80`、單一 outlier 敏感），不可外推為「補 carnosine 就會加速 `W'` 恢復」；應仍以 supplementation RCT 為主軸。

## Research-Useful Points

- 提供罕見的 in vivo MRS 同步量測 `[PCr]、[Pi]、pH、carnosine` 與估計 `W'` 的人類資料集，可作後續 small-muscle-mass kinetics 驗證的 reference benchmark。
- `D[PCr]` 概念（B_C 結束 [PCr] − B_E 耗竭 [PCr]）作為 `W' recovery` 的比 `τ_[PCr]` 更敏感的 surrogate；後續 31P-MRS 研究設計可直接採用。
- 新 `τ_W' = W'_0 / D_CP` 推導免去 fitting，可用於 race-strategy / interval-design 模擬；但建議與 Sreedhara 2020 的 SK2 / BAR overprediction 結果並讀。
- 「微觀線性、巨觀曲線」假說（Appendix 2）為 multi-fiber / multi-muscle 異質性建模提供了一條 testable 路徑；後續可結合 fiber-type-distribution biopsy / DTI 等量測檢驗。
- 提供 carnosine 與 `W' T1/2` 的初探資料；後續 β-alanine supplementation RCT + 31P/1H-MRS 可重新檢驗 mechanism（Ca²⁺ vs pH）。
- 本研究與 Ferguson 2010（whole-body cycling）的 W' T1/2 一致（皆 232–234 s），是 cross-modality conserved kinetics 的有力訊號；但個體 single-leg 線性與 whole-body 曲線形差異仍待解釋。

## Conflicts With Existing Knowledge

- 與「W' = 一個 PCr / anaerobic 油箱」衝突：bulk `[PCr]` 比 `W'` 快約 6×，且 `τ_[PCr]` 與 `τ_W'` 不相關。
- 與「`W'` recovery 可用單一 universal `tau` 完整描述」衝突：本研究個體 T1/2 範圍 `135–426 s`，且 `τ_W'` 受 `D_CP` 與 `W'_0` 共同決定。
- 與「`W'` recovery 在 small muscle 與 whole-body 完全相同」衝突：本研究 group mean 為線性、whole-body（Ferguson 2010、Skiba 2012）為曲線形，需以 Appendix 2 微觀 - 巨觀模型 / 取樣不足解釋。
- 與「pH 是 W' 主要 mediator」衝突：pH at exhaustion / pH recovery / pH 變化 與 `W'` 無相關。
- 與「Skiba 2012 的 empirical `τ_W' = 546 e^(−0.01·D_CP) + 316` 為 universal recovery formula」衝突：作者自己引入的新推導（`τ_W' = W'_0 / D_CP`）顯示 systematic offset（Passing–Bablok intercept ≈ 288 s），代表舊式不該外推到不同 modality。
- 與「W'BAL 是直接量到的真實剩餘油箱」衝突：本研究反覆強調 `W'` recovery 為 model-extracted、whole-system construct。

## Pages That Should Be Created or Updated

- 必更新：
  - `04_CPET/Wprime_Recovery.md`（補 T1/2 個體範圍、新 τ 推導、D[PCr] / oxidative reserve 與 W' 的關係、單腳 - 全身差異 caveat）。
  - `04_CPET/Wprime_Balance_Model.md`（補新 `τ_W' = W'_0 / D_CP` derivation、Passing–Bablok systematic offset、carnosine 為 exploratory）。
  - `05_Exercise_Physiology/PCr_Resynthesis.md`（補 D[PCr] 概念、bulk [PCr] vs D[PCr] 對 `W'` 的不同預測力）。
  - `index.md`（更新 Skiba 2015 entry 描述）。
  - `log.md`（追加本則 correction）。
- 可考慮（暫不新建）：
  - `04_CPET/Wprime_Recovery_Model_Comparison.md`（整合 Skiba 2012 / 2015、Bartram 2018、Sreedhara 2020 的不同 τ 形式；待後續多一輪 correction 後再決定是否拆出）。
  - `05_Exercise_Physiology/Carnosine_and_Muscle_Performance.md`（待 β-alanine supplementation RCT 來源 ingest 後再評估）。
- 不於本輪新建獨立概念頁；本來源核心仍是「intramuscular determinants of W' recovery」單一 concept，現有 hub 可承載。

## Suggested Tags

`W_prime`、`PCr`、`31P_MRS`、`1H_MRS`、`carnosine`、`critical_power`、`recovery`、`W_BAL`、`oxidative_reserve`、`single_leg_knee_extension`、`original_article`、`single_source_correction`。
