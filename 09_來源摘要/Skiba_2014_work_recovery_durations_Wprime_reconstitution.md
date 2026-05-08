---
title: Skiba et al. 2014 — Effect of Work and Recovery Durations on W' Reconstitution during Intermittent Exercise
created: 2026-04-25
updated: 2026-05-08
type: source_summary
domain: [CPET, exercise_physiology, training, methodology]
tags: [W_prime, W_BAL, recovery_duration, work_duration, interval_structure, VO2_slow_component, microintervals, original_article]
source_tier: 3
evidence_level: limited
confidence: medium
contested: true
contradictions:
  - The W'BAL model is robust on average (mean W' underprediction −1.6 ± 1.06 kJ across 6 conditions) but systematically underpredicts W'_ACT in protocols with shorter work intervals (60-30 → 20-30) or shorter recovery intervals (20-30 → 20-10), so the empirical τ_W' = f(D_CP) does not capture interval-structure effects.
  - Two protocols with identical work/recovery ratio = 2 and identical mean power (60-30 vs 20-10) yielded markedly different W'_ACT (7.35 vs 8.27 kJ), so total work or mean power alone cannot stand in for the actual stress imposed.
  - The "limit work to ≤ 20 s, recovery 10–20 s for best subsequent CWR performance" practical recommendation is a single-study, recreational-athlete observation; it should not be treated as a universal microinterval prescription, and the 6-trial / 2-week design produced an unavoidable training effect (CP +18 W ≈ 9%, VO2peak +8%).
  - The D_VO2 vs W'_ACT correlation (r = 0.79; r² = 0.63) was authors-flagged as possibly over-leveraged by a single outlier, so its quantitative strength is uncertain.
---

# Source Summary: Skiba et al. 2014 — Effect of Work and Recovery Durations on W' Reconstitution during Intermittent Exercise

## Source Type

- 類型：original research article（human cycle-ergometer experimental study）。
- 出處：*Med Sci Sports Exerc* 2014;46(7):1433–1440。
- 作者：Skiba PF, Jackman S, Clarke D, Vanhatalo A, Jones AM。
- 投稿 2013-10，accepted 2013-11；DOI 10.1249/MSS.00000000000000226。
- 原始檔：`C:\原始資料\effect_of_work_and_recovery_durations_on_w_.20\effect_of_work_and_recovery_durations_on_w_.20.md`。
- 注：本來源在 Sreedhara 2020 / Skiba & Clarke 2021 / Skiba 2015 等後續論文中以「Skiba et al. 2013」引用（指 Skiba 2013 biconditional / SK2 model 的 Appendix 1 公式）；但本論文正式發表年份為 2014；wiki 沿用「Skiba 2014」命名。

## Reliability Level

- 來源層級：3（依 wiki source_tier 慣例：original research article 標 3，與 Ferguson 2010、Skiba 2012、Skiba 2015、Caen 2021、Lievens 2024 同級）。
- 對應 AGENTS.md §4 第 5 級（original research article）。
- evidence_level：limited（n = 11 recreational athletes、cycle only、recovery power 固定 20 W、6 trials 全在 2 週內完成且伴隨可量測的 training effect、未做 fiber-type / MRS / biopsy 驗證）。
- confidence：medium。
- contested：true（W'BAL 模型整體可用但對 interval architecture 不敏感；fitted τ_W' 在 iterative boundary 假設下很可能過度擬合；recommended「limit work ≤ 20 s, recovery 10–20 s」屬實務建議而非機制定論）。

## One-Sentence Summary

在 11 位 recreational athletes 的 cycle ergometer 模型中，Skiba 等人讓受試者先以 6 種不同 work / recovery 結構的 intermittent exercise 耗掉約 50% 預測 `W'BAL`、再做一段 super-severe constant-work-rate 跑到 exhaustion；發現 **`W'BAL` 整體 underprediction 約 `−1.6 ± 1.06 kJ`、`Tlim` underprediction 約 `−27 s`，但短 work 或短 recovery 條件下 `W'_ACT` 系統性高於 model 預測（最大差 `−2.78 kJ`）；同時 `VO2_start − VO2peak` 差（`D_VO2`）與 `W'_ACT` 正相關（r = 0.79，作者標記可能受單一 outlier 拉動）**——支持 W' 不僅由總工作量決定，也受 interval structure 對 priming / VO2 baseline / fatigue metabolite 的影響。

## Core Concepts Extracted

### Concept: Interval architecture（work × recovery duration）對 W' reconstitution 的影響與 W'BAL 模型的條件性失準

#### One-Sentence Definition

`Interval architecture effect on W' reconstitution` 在本研究的操作型定義是：固定 work power（super-severe `P_EXP = P6 + 50% × (P6 − CP)`）、recovery power（20 W）、目標總 depletion（≈ 50% 預測 `W'BAL`），改變 work duration（60 / 40 / 20 s）或 recovery duration（30 / 20 / 10 / 5 s）後，比較 model-predicted `W'BAL`（依 Skiba 2012 經驗 τ 公式）與 follow-up CWR 實測 `W'_ACT`（CWR 期間做於 CP 之上的累積 work），看模型在不同 protocol 下的偏差方向與量。

#### Known Facts

- 受試者：5 位 male（`27.4 ± 6 yr`；`1.84 ± 0.08 m`；`85.2 ± 18 kg`）+ 6 位 female（`25.2 ± 1.6 yr`；`1.67 ± 0.12 m`；`65.3 ± 12.7 kg`）；recreational athletes、非高度訓練；familiar with lab CPET。
- 設備：Lode Excalibur Sport cycle ergometer；Jaeger Oxycon Pro / Triple V breath-by-breath gas exchange。
- 起始測試：30 W/min ramp（→ `VO2max`、`GET`）、3-min all-out test（→ `CP`、`W'`，依 Vanhatalo 2007）。
- Work power（intermittent + CWR 共用）：`P_EXP = P6 + 50% × (P6 − CP)`，即 super-severe domain。
- Recovery power（intermittent 期間）：`20 W`（與 Skiba 2012、Chidnok 2012 一致）。
- 6 trials × 在 2 週內完成、隨機順序、間隔 ≥ 48 h：
  - 變動 work 組（recovery 30 s 固定）：60-30 / 40-30 / 20-30。
  - 變動 recovery 組（work 20 s 固定）：20-30 / 20-20 / 20-10 / 20-5。
  - 注：20-30 同屬兩組。
- intermittent 段預設目標：依 Skiba 2012 Eq 3 算到「達 ~50% 預測 `W'BAL` depletion」即進入 CWR；CWR 至 cadence 跌 > 5 rpm 為 exhaustion。
- 主結果（Table 1，群均 ± SD）：
  - **60-30**：`W'_pred 7.13 ± 2.80 kJ`、`W'_ACT 7.35 ± 3.07 kJ`、`Diff −0.22 ± 1.68`（NS）；`Tlim_pred 121 ± 13 s`、`Tlim_ACT 121 ± 32 s`（NS）；fitted `τ_W' = 403 ± 164 s`；`VO2_start 2753 ± 674 mL/min`。
  - **40-30**：`W'_pred 7.79 ± 2.87`、`W'_ACT 8.98 ± 3.67`、`Diff −1.19 ± 2.02`（W' NS，`Tlim` Diff `−13 s` 顯著）；`τ_W' = 302 ± 145 s`；`VO2_start 2524 ± 687`。
  - **20-30**：`W'_pred 7.74 ± 2.99`、`W'_ACT 9.60 ± 4.0`、`Diff −1.86 ± 1.7`（顯著 `P < 0.01`）；`Tlim` Diff `−29 ± 23 s` 顯著；`τ_W' = 263 ± 91 s`；`VO2_start 2229 ± 554`。
  - **20-20**：`W'_pred 6.96 ± 2.81`、`W'_ACT 9.73 ± 3.88`、`Diff −2.77 ± 1.9`（顯著）；`Tlim` Diff `−46 ± 51 s` 顯著；`τ_W' = 212 ± 114 s`；`VO2_start 2414 ± 567`。
  - **20-10**：`W'_pred 5.49 ± 2.46`、`W'_ACT 8.27 ± 4.43`、`Diff −2.78 ± 2.6`（顯著）；`Tlim` Diff `−46 ± 40 s` 顯著；`τ_W' = 234 ± 119 s`；`VO2_start 2910 ± 700`。
  - **20-5**：`W'_pred 5.28 ± 2.49`、`W'_ACT 6.03 ± 3.03`、`Diff −0.75 ± 1.7`（W' NS，`Tlim` Diff `−12 s` 顯著）；`τ_W' = 337 ± 150 s`；`VO2_start 3333 ± 828`。
  - **整體均值**：`W'_pred 6.76 ± 1.13`、`W'_ACT 8.34 ± 1.42`、`Diff −1.58 ± 1.06 kJ`、`Tlim Diff −27 ± 19 s`、`τ_W' 274 ± 69 s`。
  - 各 trial `VO2peak` 接近恆定（≈ `3436–3493 mL/min`），無顯著差異。
- VO2 trace 形狀：60-30 / 40-30 trial 呈 sawtooth，20-30 開始消失，20-20 / 20-10 / 20-5 完全變成 slow curvilinear rise。
- 變動 work 組：`VO2_start` 隨 work duration 縮短而呈線性下降（60→40→20 s，`r = 0.99, p = 0.07`）。
- 變動 recovery 組：`VO2_start` 隨 recovery duration 縮短而呈線性上升（30→20→10→5 s，`r = 0.99, p < 0.01`）。
- `D_VO2 = VO2peak − VO2_start` 與 `W'_ACT` 相關 `r = 0.79, p < 0.01`（Fig 5）；作者明文標 `r² = 0.63` 並指出可能受單一 outlier 拉動。
- 60-30 vs 20-10 對比（同 work-recovery ratio = 2、同 intermittent 段 mean P）：`W'_ACT` 為 `7.35 vs 8.27 kJ`，後者顯著較高；`τ_W'` 為 `403 vs 234 s`，後者顯著較快。
- 2 週訓練效應：CP 群均增加 `+18 ± 20 W`（顯著，`P < 0.05`）、W' 改變 `−0.6 ± 0.6 kJ`（NS）；CP 與 W' 改變呈 inverse correlation `r = 0.89, p < 0.01`；3-min all-out test 的 `peak VO2` 增加 `+260 ± 223 mL/min`（顯著 `P < 0.01`，約 8%）。
- 隨機化抽樣順序：除第 4 與第 6 session peak VO2 差約 2%（顯著）外，其他 sessions 排序無顯著差異。
- subj 9 outlier：`CP = 366 W`、`τ_W' = 104 s` 在 60-30 條件，比 Skiba 2012 經驗式漸近 316 s 還快超過 200 s；作者建議 well-trained athletes 需「personalized predictive function」。
- 作者實務建議：limit work interval ≤ 20 s、recovery 10–20 s 在本研究 condition 下使後續 CWR 表現最佳。

#### Mechanism Chain

1. supra-CP work 持續耗 W'，同時累積 `Pi` / `H+` / `Ca2+` / 鞏固 Type II fiber recruitment（VO2 slow component 機制）。
2. recovery 期間 `power < CP`，oxidative metabolism 進入 reserve 狀態：(a) PCr resynthesis；(b) 部分 fatigue metabolite 清除；(c) muscle perfusion 持續較高（postexercise hyperemia 推測）。
3. 縮短 work duration（60→40→20 s）→ 每段 supra-CP work 的 metabolite accumulation 較少 → 整段 intermittent 期 `VO2_start` 較低（VO2 sawtooth 退化為 slow curve）→ priming-like 效應使 CWR 開始時 `D_VO2 = VO2peak − VO2_start` 較大 → 可動員的 `W'_ACT` 較多。
4. 縮短 recovery duration（30→20→10→5 s）→ 每段休息不足以完整補回 PCr / 清 metabolite → `VO2_start` 反而升高（recovery 變成連續代謝負荷）→ `D_VO2` 縮小 → 一般預期 `W'_ACT` 也應較低；但實際在 20-20 / 20-10 條件 `W'_ACT` 仍高於 model，作者推論 muscle perfusion 維持較高、fiber-specific O2 delivery 提升、可能 PCr overshoot（Kushmerick 1992、Nevill 1997）。
5. 60-30 與 20-10 比較：總工作 / 總休息相同，但 20-10 的 `W'_ACT` 多 `+0.92 kJ`、`τ_W'` 快約 `170 s`；提示 architecture 改變了 (a) 累積 metabolite 量，或 (b) priming 對 CP / W' 的瞬時提升，或兩者。
6. CP 在 2 週內群均上升 9% 是 unavoidable training effect；隨機化分配可使其在各 trial 之間平均，但不能完全消除單一 trial 的偏差。

#### Inferences

- **W'BAL 不是「interval-architecture-blind」**：同一 model 在某些結構（60-30 / 20-5）下與實測 W' 一致，在另一些結構（20-30 / 20-20 / 20-10）下系統性低估真實 W'_ACT；推論 Skiba 2012 經驗 τ 公式不足以描述 short-work 或 short-recovery 的 priming 效應。
- **同總量、不同切法 ≠ 同效果**：60-30 vs 20-10 同 ratio、同 mean P 但 `W'_ACT` 差 `+0.92 kJ`；推論 interval prescription 必須明寫 work duration、recovery duration、recovery power，不能只看平均功率。
- **Type II fiber priming 假說一致**：VO2 slow component 在 short-work trial 顯著減弱、VO2_start 降低、`D_VO2` 增大、`W'_ACT` 提升，與 Vanhatalo 2010、Burnley 2011、Jones 2003 的「heavy/severe priming → enhanced subsequent severe-domain performance」相容；但本研究未量 EMG / 31P-MRS / biopsy，無直接 fiber-type 證據。
- **個別化 τ_W' 是必要的**：subj 9（CP 366 W、τ_W' 104 s）已超出 Skiba 2012 經驗式漸近值（316 s），提示 well-trained 個體需 personalized predictive function；後續 Bartram 2018 elite cyclist 公式即此延伸。
- **「short work + short recovery 最佳」的實務建議**有單篇限制：本研究 work power 固定 P6 + 50%(P6−CP)、recovery power 固定 20 W、CWR 為單一 power、樣本為 recreational athletes；不可外推為通用 microinterval 處方。
- **W'BAL = 0 不是物理零點**：本研究 fitted τ_W' 同樣採 W'BAL = 0 at CWR exhaustion 的 boundary（與 Skiba 2012 一致），放大同樣的循環假設限制。

#### Assumptions

- W' 在 intermittent 段以 Skiba 2012 經驗 τ 公式 `τ_W' = 546·exp(−0.01·D_CP) + 316` 推算，因此 50% depletion target 本身已內含模型假設。
- recovery 期間 power 固定 20 W；任何 active recovery 不同 intensity 的影響無法在本研究判定。
- W'_ACT 計算採固定 CP（即 CWR 期間 CP 不因 prior intermittent exercise 改變）；雖 Ferguson 2010 在 cycle 長休息後支持 CP 不變，但 priming hypothesis 提到 CP 可能短期上升（Vanhatalo 2010、Miura 2009），因此「CP 不變」對 W'_ACT 的詮釋可能有偏差。
- 3-min all-out test 能準確估 CP / W'，且 study-end 重測得到的群均 `+18 W` 與 W' `−0.6 kJ` 為 systematic training effect 而非 measurement error。
- fitted τ_W' 由 iterative process 強制 W'BAL = 0 at CWR exhaustion；若 CWR 並非完整耗 W'（perceived effort 提早停 / cadence 標準提早觸發），則所有 fitted τ 都帶 boundary 偏差。
- pulmonary VO2 上升與 muscle-level metabolite accumulation 相對應；本研究未直接量 muscle [PCr]、[Pi]、pH、glycogen。
- D_VO2 與 W'_ACT 相關代表 "muscle reserve"，但 r² = 0.63 並含單一 outlier 警告，不是強因果。
- 6 trial × 2 週 design 中，random order 足以平均 training effect 的影響；但實際各 trial 順序 timing 差異仍存在（4 vs 6 session peak VO2 差 2% 顯著）。

#### Uncertainties / Limitations

- 樣本 `n = 11` recreational athletes（5M / 6F）、無 trained athletes、無 elite、無高齡或臨床族群、未做性別分層分析。
- cycle ergometer only；不適用 running、rowing、上肢、wheelchair。
- 6 trials 在 2 週內、CP 群均上升 9%、peak VO2 上升 8%；雖 random order 抵消平均效果，但無法排除個別 trial 的局部偏差。
- recovery power 固定 `20 W`；不同 active recovery（如 0.9 P_GET 或 P_GET）對 short-work / short-recovery effect 的交互未測。
- work power 固定 `P_EXP = P6 + 50%(P6 − CP)`；不同 supra-CP 強度（如 110% CP、CP4）對 interval architecture effect 的影響未測。
- CWR 採同一 work power 為 follow-up；若 CWR 改為更短時間 / 更高 power 或 lower power，priming effect 可能不同。
- D_VO2 與 W'_ACT 相關的 `r² = 0.63` 受單一 outlier 拉動，作者明文承認 over-leveraging；子 group 排除 outlier 後的 r² 未報告。
- 沒有 EMG / 31P-MRS / biopsy / fiber-type 直接證據；fast/slow Type II fiber 假說、PCr overshoot、muscle perfusion 推測均屬 indirect inference。
- 「limit work ≤ 20 s, recovery 10–20 s」實務建議來自 cycle-ergometer recreational athletes；對 runners、 trained athletes、HF / COPD / frail elderly 患者的外推，須其他來源支持。
- subj 9（fast recovery outlier）是個案訊號；推論 elite athletes 需個別化 τ 仍待 Bartram 2018 等獨立樣本驗證。
- iterative fit 共享 Skiba 2012 的 boundary assumption（W'BAL = 0 at exhaustion）；本研究僅報告群均 fitted τ，個體 τ 是否在某些 outlier subject 受到強烈 boundary 拉動未明示。

## Clinically Useful Points

- 對 cycle-ergometer 復健 / 運動處方寫法的提醒：**「總時間相同、平均功率相同、ratio 相同」不等於「同樣 stress」**；同一個 6 min 工作 + 6 min 休息可寫成 60-30 × 6 組或 20-10 × 36 組，後者在本研究中可動員的 W'_ACT 多 ~12%。
- 對 microinterval（如 20-10、15-15）的支持：本研究的 cycle 資料支持 microinterval 在 short-work + short-recovery 下能比 conventional 60-30 protocol 在後續 CWR 段更耐久；但這是 cycle / recreational 實驗結果，不應自動外推到所有運動 mode 與族群。
- 對病人 / 選手溝通：可用本研究 60-30 vs 20-10 的對比，把「為什麼同樣 6 組 1 分鐘工作 + 30 秒休不等於 18 組 20 秒工作 + 10 秒休」說清楚；強調 W'BAL 是 model-based estimate，不是真實剩餘油箱。
- 對 trained athletes 的 caveat：subj 9 的 τ_W' = 104 s 已遠快於 Skiba 2012 經驗式漸近 316 s；高度有氧訓練者套用 group-mean τ 會嚴重低估其實際 work capacity。
- 對心肺族群 / HF / COPD：本研究全為 healthy recreational athletes，supra-CP work 不適合作 routine intervention；不可機械式套用 microinterval 建議。

## Research-Useful Points

- 提供 6 種 work × recovery duration 條件的 W'_pred / W'_ACT / Tlim / fitted τ_W' / VO2_start / VO2peak 的群均 ± SD 表格，可作後續 model-comparison（SK1 vs SK2 vs BAR vs Sreedhara optimal control vs Caen biexponential）的 reference 資料集。
- 60-30 vs 20-10 同 ratio / 同 mean P 的對比，提供「interval-architecture is its own independent dimension」的最直接證據；後續 model 驗證若不能解釋此 9% 差異，應視為 model gap。
- D_VO2 vs W'_ACT 的 `r = 0.79` 連結 VO2 slow component / muscle reserve / fiber recruitment 與 W'_ACT；後續若搭配 EMG / 31P-MRS 可分離 priming 機制。
- subj 9 outlier（τ_W' = 104 s）為 Bartram 2018 elite cyclist 公式（`τ = 2287.2 · D_CP^(−0.688)`）提供前置動機；本來源亦明文呼籲「personalized predictive function」。
- Sreedhara 2020 的 SK2 / BAR overprediction 比較直接以本來源的 fitted τ 為 baseline；任何 W'BAL model 改良都應在本資料集上至少不退步。
- Vanhatalo 2010 hyperoxia 研究與 Miura 2009 priming 研究與本來源的 Type II fiber / CP-prim
ing hypothesis 直接相關；後續 priming + 31P-MRS 設計可由此延伸。

## Conflicts With Existing Knowledge

- 與「W'BAL 模型可獨立於 interval architecture 預測 W'_ACT」衝突：本研究 6 trials 中 3 條（20-30 / 20-20 / 20-10）顯著 underprediction，最大差 `−2.78 kJ`。
- 與「同 mean power、同 ratio = 同效果」衝突：60-30 vs 20-10 在這兩個維度全相同但 `W'_ACT` 差 `+0.92 kJ`、`τ_W'` 快約 `170 s`。
- 與「W' = 一個固定 anaerobic 油箱、與 priming / metabolite 無關」衝突：D_VO2 與 W'_ACT 正相關（r = 0.79）支持「muscle reserve / VO2 baseline / fiber recruitment 影響可動員的 W'」。
- 與「Skiba 2012 的 `τ_W' = 546·exp(−0.01·D_CP) + 316` 為 universal recovery formula」衝突：本研究 6 trials 群均 fitted τ 從 `212 s`（20-20）到 `403 s`（60-30），跨度 `~190 s`；recovery power 都固定 20 W，所以 D_CP 幾乎相同，仍出現顯著差異。
- 與「W'BAL = 0 為精確 exhaustion 秒數」衝突：本研究自身強制 W'BAL = 0 at CWR exhaustion，是 fitting boundary 而非獨立驗證；20-20 / 20-10 條件 W'_ACT 比預測高 ~50%，更顯示 W'BAL = 0 不是物理零點。
- 與「priming exercise 必為 heavy domain 才有效」衝突：本研究 intermittent 段 mean power 多落在 heavy domain，但縮短 recovery 至 5 s 反而使 priming 消失（20-5 trial Diff `−0.75 kJ`，NS），提示 priming dose-response 需精細處方。
- 與「Skiba 2012 經驗式可外推到 trained athletes」衝突：subj 9（CP 366 W、τ_W' 104 s）超出公式漸近 316 s，預示 Bartram 2018 elite cyclist 公式的必要性。

## Pages That Should Be Created or Updated

- 必更新：
  - `04_CPET/Wprime_Balance_Model.md`（補本來源的 6 trial 結果摘要、整體 W' Diff `−1.6 ± 1.06 kJ`、20-20 / 20-10 的 ~50% underprediction、60-30 vs 20-10 的同 ratio 對比、subj 9 outlier 對個別化 τ 的更強支持、與 Skiba 2012 經驗式的差異）。
  - `04_CPET/Wprime_Recovery.md`（在「interval structure 本身會改變回補表現」段（§8）補上具體數字：60-30 trial fitted τ_W' = 403 s、20-10 trial = 234 s，雖 D_CP 相同（recovery power 都 20 W），仍因 work duration 差異使 τ 差近 170 s）。
  - `04_CPET/CP_Wprime_Interval_Design.md`（補 60-30 vs 20-10 同 ratio / 同 mean P 但 W'_ACT 差 12% 的具體 fact；強化「interval architecture 是處方獨立維度」論點；補「limit work ≤ 20 s, recovery 10–20 s」的單篇證據與外推 caveat）。
  - `index.md`（更新 Skiba 2014 entry 描述以反映 6 trial 結果、整體偏差量、interval architecture independent dimension）。
  - `log.md`（追加本則 correction）。
- 既有相關概念頁（不直接重寫，但 reasoning 可引用）：
  - `04_CPET/Critical_Power.md`、`04_CPET/Training_Prescription_by_CP.md`、`04_CPET/VO2_Slow_Component.md`、`05_Exercise_Physiology/Skeletal_Muscle_Energy_Metabolism.md`、`05_Exercise_Physiology/Muscle_Fiber_Types.md`。
- 可考慮（暫不新建）：
  - `04_CPET/Wprime_Recovery_Model_Comparison.md`：整合 Skiba 2012 / 2014 / 2015、Bartram 2018、Sreedhara 2020、Caen 2021、Lievens 2024 的 τ formulation 對照表；待 Bartram 2018、Sreedhara 2020、Caen 2019 也完成 single-source correction 後再決定。
- 不於本輪新建獨立概念頁；本來源核心仍是「interval architecture 對 W' reconstitution 的影響」單一 concept。

## Suggested Tags

`W_prime`、`W_BAL`、`interval_architecture`、`work_duration`、`recovery_duration`、`microintervals`、`priming_exercise`、`VO2_slow_component`、`D_VO2`、`personalized_tau`、`original_article`、`single_source_correction`。
