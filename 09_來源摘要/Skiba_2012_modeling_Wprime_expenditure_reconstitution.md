---
title: Skiba et al. 2012 — Modeling the Expenditure and Reconstitution of Work Capacity above Critical Power
created: 2026-04-25
updated: 2026-05-08
type: source_summary
domain: [CPET, exercise_physiology, methodology]
tags: [W_prime, Wprime_BAL, critical_power, intermittent_exercise, VO2_slow_component, original_article, modeling, integral_form]
source_tier: 3
evidence_level: limited
confidence: medium
contested: true
contradictions:
  - This is the seminal paper that introduced the W'BAL integral-form equation, but its empirical τ_W' was iteratively fit by forcing W'BAL = 0 at exhaustion — a circular boundary that bakes the assumption into the parameter rather than testing it.
  - The empirical regression τ_W' = 546·exp(−0.01·D_CP) + 316 is fit only to S20 / S_M / S_H (recovery < CP) data from 7 male cyclists; it does not generalize to recovery ≥ CP, to other modalities, or to populations with very different aerobic fitness (subject 4 outlier with VO2max > 5 L/min showed no τ change S20→S_M).
  - Modeled W' balance correlates with the rise in VO2 above CP (r² = 0.82–0.96), but this association does not prove a mechanistic identity between W' and VO2 slow component or fiber-type recruitment.
  - Subsequent work (Skiba 2015, Skiba & Clarke 2021) replaced this empirical τ formula with τ_W' = W'_0 / D_CP and flagged dimensional ambiguity (du vs dt) in the original integral form.
---

# Source Summary: Skiba et al. 2012 — Modeling the Expenditure and Reconstitution of Work Capacity above Critical Power

## Source Type

- 類型：original research article（human cycle-ergometer experimental study + race-data simulation）。
- 出處：*Med Sci Sports Exerc* 2012;44(8):1526–1532。
- 作者：Skiba PF, Chidnok W, Vanhatalo A, Jones AM。
- 投稿 2011-09，accepted 2012-02。
- DOI：10.1249/MSS.0b013e3182517a80。
- 原始檔：`C:\原始資料\modeling_the_expenditure_and_reconstitution_of.15\modeling_the_expenditure_and_reconstitution_of.15.md`。
- 與 companion article（Chidnok et al. 2012, *Med Sci Sports Exerc* 44(5):966–976）共用 protocol；本來源僅單獨處理 Skiba 2012 modeling 部分，未混入 Chidnok 2012 / 2013 的 31P-MRS 資料。

## Reliability Level

- 來源層級：3（依 wiki source_tier 慣例：original research article 標 3，與 Ferguson 2010、Skiba 2015、Caen 2021、Lievens 2024 同級）。
- 對應 AGENTS.md §4 第 5 級（original research article）。
- evidence_level：limited（n = 7 male recreational athletes、僅 cycle ergometer、固定 60 s / 30 s interval、`τ_W'` 採用 iterative fit 至 W'BAL = 0 的 boundary condition）。
- confidence：medium。
- contested：true（W' 物理意義仍未定論；本研究的 empirical τ 公式已被 Skiba 2015 / Skiba & Clarke 2021 / Sreedhara 2020 / Bartram 2018 多篇後續研究改寫或標出限制）。

## One-Sentence Summary

在 7 位 healthy male recreational cyclist 的 60 s severe / 30 s recovery intermittent 模型中，作者首次提出 **W'BAL 連續 integral 方程式**（`W'_bal = W' − ∫₀ᵗ W'_exp · exp(−(t−u)/τ_W') du`），並以 iterative fitting（強制 W'BAL = 0 at exhaustion）求得 `τ_W'`，發現 `τ_W'` 與 `D_CP = CP − P_recovery` 之間呈指數遞減（最佳擬合 `τ_W' = 546·exp(−0.01·D_CP) + 316`，r² = 0.77）；同時 modeled W' 消耗與 VO2 上升高度相關（r² = 0.82–0.96）。

## Core Concepts Extracted

### Concept: W'BAL integral form 模型的提出與經驗 τ_W' = f(D_CP) 公式

#### One-Sentence Definition

`W'BAL integral form` 是 Skiba 2012 提出的連續方程式，用 exponential reconstitution kernel 將 intermittent exercise 中每一段 supra-CP 工作所消耗的 `W'` 在 sub-CP 期間以時間常數 `τ_W'` 指數回補；`τ_W'` 由 `D_CP = CP − P_recovery` 決定（recovery 越低於 CP，回補越快）。

#### Known Facts

- 受試者：7 位 healthy male recreational athletes（age `26 ± 5 yr`；height `1.79 ± 0.06 m`；body mass `81 ± 6 kg`）；非高度訓練者，但已熟悉實驗室 CPET 程序。
- 設備：Lode Excalibur Sport cycle ergometer；breath-by-breath gas exchange（Jaeger Oxycon Pro，Jaeger Triple V turbine）。
- 起始測試：30 W/min ramp（→ `VO2max`、`GET`）、3-min all-out test（→ `CP`、`W'`）；`CP` = ramp 後 final 30 s 平均功率，`W'` = power-time integral above CP。
- Group means（Table 1）：
  - `W' = 21.1 ± 4.7 kJ`（個體 14.3–28 kJ）
  - `CP = 240 ± 56 W`（個體 187–351 W）
  - `VO2max = 4.10 ± 0.778 L/min`（個體 3.19–5.59 L/min）
- 主要 protocol：60 s 工作 at `P_w = P6 + 50% × (P6 − CP)`（即位於 super-severe 區）；30 s recovery at 4 種強度，重複至 exhaustion：
  - **S20**：20 W
  - **S_M**：moderate，0.9 × `P_GET`
  - **S_H**：heavy，`P_GET + 50% × (CP − P_GET)`
  - **S_S**：severe，`P6 − 50% × (P6 − CP)`（仍在 CP 以上）
- 數學框架（Eq 3）：

  `W'_bal(t) = W' − ∫₀ᵗ W'_exp · exp(−(t−u)/τ_W') du`

  其中 `τ_W'` 為 reconstitution time constant（s）。
- Fitting：每秒輸入 W'_exp，並用 iterative process 變動 `τ_W'` 直到 `W'_bal = 0` 在實際 exhaustion 時刻。
- 計算所得 `τ_W'`（Table 2，per recovery condition）：
  - **S20**：`377 ± 29 s`（個體 321–421 s；多數 cluster 370–380 s；subj 4 = 321 s 為最低，此 subj 也是 VO2max > 5 L/min 的 outlier）
  - **S_M**：`452 ± 81 s`
  - **S_H**：`578 ± 105 s`
  - **S_S**：`7056 ± 11 169 s`（極大 SD；個體範圍 596–30 758 s，模型在 P > CP 時失效）
- `τ_W'` 與 `CP` 的相關（per condition）：
  - S20：r² = 0.53，p = 0.06（trend）
  - S_M：r² = 0.64，p = 0.03（significant）
  - S_H：r² = 0.48，p = 0.08（trend）
  - S_S：r² = 0.07，p = 0.56（無相關）
- `τ_W'` 與 `D_CP` 的相關（S20 + S_M + S_H 合併）：
  - 線性 / 非線性回歸均顯示 inverse relationship；r² = 0.67，p < 0.0001。
  - S_S：r² = 0.05，p = 0.55（與 D_CP 無相關，且 D_CP 為負值）。
- 最佳擬合（exponential，nonlinear regression）：
  - `τ_W' = 546 · exp(−0.01 · D_CP) + 316`（r² = 0.77；SE：a = 86.11、k = 0.004、b = 61.8）
  - 作者明文指出 bilinear fit 也能良好描述同組資料。
- modeled W' 消耗 vs VO2 above baseline 的逐 interval 上升：representative subj 2 → S20 r² = 0.91、S_M r² = 0.87、S_H r² = 0.88；group r² 範圍 `0.82–0.96`，p = 0.0002–0.0049。
- Real-world race-data simulation：
  - 一位 competitive amateur cyclist 的 mass start 公路賽 power meter 紀錄。
  - `CP = 227 W`、peak power `409 W`。
  - 用 Eq 4 計算 `τ_W' = 440 s`（取 race 中所有 sub-CP power 平均 = 75 W 作 recovery power、`D_CP` 視為 constant）。
  - 模型顯示選手在兩次 attack 後，當 modeled W' balance 落到 `< 1.5 kJ` 時被迫降功率；55.4 min 退出比賽。
- Two-compartment model（Eq 5）作為未來方向：

  `W'_bal = W' − ∫ [k₁ · exp(−(t−u)/τ₁) + k₂ · exp(−(t−u)/τ₂)] · w(u) du`

  作者把 `τ₁、τ₂` 對應到 Type I / Type II fiber pool，但僅作 hypothesis，未在本研究檢驗。
- 與既有文獻的對照：
  - S20 條件下 `τ_W' = 377 s` 與 Ferguson 2010 推算的 `τ_W' ≈ 336 s` 接近。
  - 與 Bogdanis 1995 報告 30 s sprint power output 恢復 τ ≈ 333 s 接近。
  - VO2 rise 與 W' 消耗的耦合，與 VO2 slow component 的 Type II fiber recruitment 假說相容。

#### Mechanism Chain

1. supra-CP 工作 → muscle ATP demand 高於可由 oxidative metabolism 即時供應 → W' 進入 「expenditure phase」（每秒以 P − CP 速率耗 W'）。
2. 當 power 落到 < CP，oxidative metabolism 進入 「reserve」狀態：muscle 可在 ADP 增加、PCr 補回、acid-base 重整、Type II fiber 解除過度動員等並行過程下，重新累積可動員的 W'。
3. Skiba 2012 假設這個 reconstitution 可被單一 monoexponential kernel 近似：每個被消耗的 joule 各自以 `τ_W'` 指數恢復；總體 W'_bal 是 expended joules 與其各自 recovery curve 的卷積。
4. `τ_W'` 受 `D_CP` 共同決定：recovery power 越接近 CP，oxidative reserve 越小、可用於 W' 重建的「淨能量差」越小，`τ_W'` 越大；越遠離 CP（向 0 W）oxidative reserve 越大，`τ_W'` 越小。
5. 當 recovery power > CP，模型本身不適用：W' 沒有 net 重建，只是 depletion 速率變慢，`τ_W'` 在數學上會發散到非物理值。
6. 與 VO2 slow component 並行：每一個 supra-CP work bout 消耗 W' 同時，pulmonary VO2 的逐 interval 上升似乎反映 fiber recruitment 與工作效率下降，因此 modeled W' 消耗與 VO2 rise 存在 strong correlation；作者推論 W' 與 Type II fiber 動員/疲勞有共同因子，但未量到肌纖維層級資料。

#### Inferences

- **τ_W' 不是單一常數，而是 D_CP 的函數**：不同 recovery power 下 `τ_W'` 從 `~321 s` 到 `> 7000 s` 變化，遠超 measurement noise；任何把單一 group-average τ_W' 套到不同 session architecture 的做法，都會偏估。
- **τ_W' 也與 CP（即 aerobic fitness）部分相關**（r² = 0.48–0.64，視 condition），高 CP / 高 VO2max 個體（subj 4）回補較快；推論 oxidative reserve 是 τ_W' 的主要 mediator，aerobic fitness 越高 oxidative reserve 越大。
- **W' 消耗與 VO2 上升的耦合**支持 W' 與 VO2 slow component 共享 mediator（如 Type II fiber recruitment、metabolic strain）；推論 W' 不僅是「anaerobic 油箱」，但這只是 association，不能直接推 mechanism。
- **模型在 race file 上能標示 W' 接近耗竭的時刻**（< 1.5 kJ 為 perceived impending exhaustion），但這是單一 case 的 retrospective 對應，不能視為 prospective predictor。
- **Two-compartment（Eq 5）方向**為後續 multi-component model（如 Caen 2021 的 fast + slow phase、Lievens 2024 的 partial depletion 雙時間常數）鋪路；但 Skiba 2012 本身未檢驗此 Eq 5。
- 推論 highly aerobically trained 族群（subj 4 outlier）需要 individualized τ；後續 Bartram 2018 為 elite cyclists 提出 `τ = 2287.2 · D_CP^(−0.688)` 即此推論的延伸。

#### Assumptions

- W' 在每段 supra-CP 工作中以 `P − CP` 之恆定速率消耗（線性消耗，與 CP 模型內建假設一致）。
- W' 的回補 follows monoexponential decay；亦即同一 session 內所有被消耗的 joule 共享同一個 `τ_W'`，而 `τ_W'` 在該 session 內是常數。
- W'BAL = 0 在實際 exhaustion 時刻（iterative fit 的 boundary condition）；若 exhaustion 時 W' 並未真正歸零（如 perceived effort 提前停止），則所有 fitted `τ_W'` 都被系統性高估或低估。
- 3-min all-out test 能準確估個體的 CP / W'（依 Vanhatalo 2007 驗證）；本研究未做 4-bout constant-load 對照。
- recovery 期間 power 為固定值（30 s 等強度）；real-world race 中 `D_CP` 變動的影響在本研究只用「group mean recovery power」近似。
- pulmonary VO2 上升能代表 muscle metabolic strain 的時間進程（用 phase II 與 slow component 機制解釋），但本研究未量肌肉 [PCr]、[Pi]、pH。
- 60 s / 30 s interval 結構足以涵蓋 intermittent exercise 行為的代表範圍；其他 work / recovery 比例（如 Caen 2019 的 P4 / P8、Lievens 2024 的 25%/75% depletion）未檢驗。

#### Uncertainties / Limitations

- 樣本 `n = 7` 全為 male recreational athletes、無女性、無 trained athletes、無高齡或臨床族群；外推極為受限。
- 僅 cycle ergometer；不適用 running、rowing、swimming、wheelchair、上肢測試。
- 經驗式 `τ_W' = 546·exp(−0.01·D_CP) + 316` 是 group-fit、多 condition 合併的迴歸；個別個體的 `τ_W'` 範圍極寬（subj 4：321 s；其他多 370–380 s；S_M / S_H 個體 SD 大）。
- iterative fit 強制 W'BAL = 0 at exhaustion，故 `τ_W'` 含 boundary 假設；若實際 exhaustion 並非 W' = 0，則 `τ_W'` 是 effective fit parameter，不是真實 reconstitution 速率。
- 模型不處理 recovery > CP 的情況：`τ_W'` 在 S_S 條件下發散，模型本身在這類 race-realistic 情境失效。
- 與 Sreedhara 2020 的 SK2 / BAR 比較：Sreedhara 顯示 SK2（即 Skiba 2013 的 biconditional version）在 recreational cyclists 會 overpredict W' 回補；Skiba 2012 原版的 integral form 同樣未處理 partial-depletion / 不同 work duration / 不同 recovery duration 的交互作用。
- Skiba & Clarke 2021 指出 Eq 3 在原文中曾有 dimensional ambiguity（du vs dt），需明寫成 convolution integral；後續實作要避免此寫法歧義。
- VO2 上升與 modeled W' 消耗的相關（r² = 0.82–0.96）僅針對 representative subject（subj 2）展示；group-level 個別細節未完整呈現。
- Race-data simulation 為單一 retrospective case；無 prospective 驗證、無 control。
- 「W' 與 Type II fiber pool 連接」推論完全基於文獻引述（VO2 slow component 文獻），本研究未做 EMG、biopsy、MRS。

## Clinically Useful Points

- 對 cycling-based 復健或運動科學處方：本研究確立 **recovery power 是 W' 回補速率的主要旋鈕之一**；同樣 30 s recovery，從 20 W 改到接近 CP，`τ_W'` 可從 `~377 s` 漲到 `~578 s`，意味著「同樣休 30 s」實際可動員的 W' 差很多。
- 對心肺患者 / 復健族群：本研究全為 healthy young male recreational cyclist；`τ_W'`、`CP`、`W'` 的數值或公式都不能直接套到 HF、COPD、frail elderly、neurologic 族群。
- 對 pacing 與比賽策略討論：本研究的 race simulation 顯示「W' < 1.5 kJ 約對應感受性 impending exhaustion」，但這是 retrospective、單一案例；不應作為 bedside 或 wearable device 的 prospective threshold。
- 對運動處方溝通：本研究使 `W'BAL` 不再僅是教科書名詞，而是有 explicit 計算公式的 operational tool；但要對病人 / 選手解釋「這是 model-based estimate，不是真實剩餘油量」。

## Research-Useful Points

- 提供 W'BAL integral form 的「公認原始公式」（Eq 3）與最早期經驗 τ 公式（Eq 4）；後續所有 W'BAL 比較研究（Skiba 2014、Skiba 2015、Bartram 2018、Caen 2019/2021、Sreedhara 2020、Lievens 2024）都以本來源為基線。
- 提供 7 名受試者 × 3 sub-CP recovery condition 的 raw `τ_W'` 個體值（Table 2），可作後續模型驗證的 reference 資料。
- 提出 two-compartment model（Eq 5）作為未來研究方向，明確將 W' 連結 Type I / Type II fiber pool；後續 multi-exponential model（Caen 2021 fast + slow、Lievens 2024 biexp vs monoexp）可視為這個 hypothesis 的延伸。
- 將 modeled W' 與 pulmonary VO2 slow component 的時間耦合具體化（r² 0.82–0.96），為「W' = severe-domain metabolic strain integrator」假說提供初步定量訊號。
- 是 race-realistic application 的早期 demonstration（單案例 retrospective）；後續 race-prediction RCT、wearable real-time W'BAL 的研究框架都可以本來源為起點。
- 為後續 Skiba 2015 提出的 chemical-kinetics 推導（`τ_W' = W'_0 / D_CP`）與 Skiba & Clarke 2021 的 dimensional 修正提供 baseline；本來源是「empirical fit」、後者是「first-principle derivation」，兩者在不同情境互補但不互換。

## Conflicts With Existing Knowledge

- 與「W' 是固定 anaerobic 油箱、與 oxidative function 無關」衝突：本研究顯示 `τ_W'` 隨 `D_CP` 改變（recovery power 越靠近 CP 越慢），且 modeled W' 消耗與 pulmonary VO2 上升強相關，支持 oxidative reserve 是 W' 行為的關鍵決定因素。
- 與「Morton & Billat 2004 的 linear W' depletion / linear reconstitution」衝突：本研究採 curvilinear（exponential）reconstitution，並引用 Ferguson 2010 的 t1/2 = 234 s 為 supporting evidence。
- 與「W'BAL 可外推到任意 recovery power」衝突：本研究明文限制經驗式 `τ_W' = 546·exp(−0.01·D_CP) + 316` 只適用 P_recovery < CP；S_S 條件 `τ_W'` 發散到非物理值。
- 與「同一 group-average τ_W' 適用所有族群」衝突：subj 4（VO2max > 5 L/min）的 τ 在 S20 與 S_M 之間幾乎不變，而其他受試者改變明顯，提示 highly trained 族群需 individualized τ；後續 Bartram 2018 的 elite cyclist 公式正是回應這條限制。
- 與「W'BAL = 0 J 等於精確 exhaustion 秒數」衝突：本研究自身的 fitting 流程強制 W'_bal = 0 at exhaustion，是模型 boundary 而非獨立驗證；race simulation 中的 1.5 kJ 閾值更明確顯示 W'BAL = 0 不是物理零點。

## Pages That Should Be Created or Updated

- 必更新：
  - `04_CPET/Wprime_Balance_Model.md`（補 Skiba 2012 為 integral form 起點、Eq 3 的明確寫法、Eq 4 的 r² = 0.77、`τ_W'` 在 S20 / S_M / S_H / S_S 的具體數值與發散現象、boundary condition 的 iterative fit 假設、subj 4 outlier 對「個別化 τ」的早期提示、race simulation 的 1.5 kJ 閾值僅為 retrospective 單案例）。
  - `04_CPET/Wprime_Recovery.md`（補 `τ_W' ≈ 377 s` for S20 與 Ferguson 2010 的 `336 s`、Bogdanis 1995 的 `333 s` 對齊；補 D_CP 與 τ_W' 的 inverse exponential 關係）。
  - `04_CPET/CP_Wprime_Interval_Design.md`（補 「recovery power 從 20 W 改到接近 CP，τ_W' 從 ~377 s 漲到 ~578 s」這一具體 fact；強化「同樣 30 s recovery 不等於同樣可用 W'」的論點）。
  - `index.md`（更新 Skiba 2012 entry 描述以反映 integral form / 經驗 τ 公式 / 模型限制）。
  - `log.md`（追加本則 correction）。
- 既有相關概念頁（不直接重寫，但 reasoning 可引用）：
  - `04_CPET/Critical_Power.md`、`04_CPET/Training_Prescription_by_CP.md`、`04_CPET/VO2_Slow_Component.md`、`05_Exercise_Physiology/PCr_Resynthesis.md`、`05_Exercise_Physiology/Muscle_Fiber_Types.md`。
- 可考慮（暫不新建）：
  - `04_CPET/Wprime_Recovery_Model_Comparison.md`：整合 Skiba 2012 / 2013 / 2015、Bartram 2018、Sreedhara 2020、Caen 2021、Lievens 2024 的 τ formulation 對照表；待 Skiba 2014（biconditional / SK2 來源）與 Bartram 2018、Sreedhara 2020 也完成 single-source correction 後再決定是否拆出。
- 不於本輪新建獨立概念頁；本來源核心仍是「W'BAL integral form 提出與經驗 τ 公式」單一 concept。

## Suggested Tags

`W_prime`、`W_BAL`、`integral_form`、`critical_power`、`intermittent_exercise`、`tau_W_prime`、`D_CP`、`VO2_slow_component`、`Type_II_fibers`、`race_simulation`、`original_article`、`single_source_correction`。
