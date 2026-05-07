---
title: Ferguson et al. 2010 — Effect of recovery duration from prior exhaustive exercise on the parameters of the power-duration relationship
created: 2026-04-25
updated: 2026-05-08
type: source_summary
domain: [CPET, exercise_physiology, methodology]
tags: [W_prime, recovery, critical_power, lactate, VO2_recovery, fatigue_metabolites, original_article]
source_tier: 3
evidence_level: limited
confidence: medium
contested: true
contradictions:
  - Post-exhaustion CP is essentially unchanged across 2 / 6 / 15 min recovery, while W' recovers curvilinearly — argues against W' as a simple finite energy store with a single recharge constant.
  - W' recovery half-time (~234 s) is much slower than VO2 recovery (~74 s) and much faster than blood [L−] recovery (~1366 s); neither single proxy can stand in for W' recovery on its own.
---

# Source Summary: Ferguson et al. 2010 — Effect of recovery duration from prior exhaustive exercise on the parameters of the power-duration relationship

## Source Type

- 類型：original research article（human cycle-ergometer experimental study）。
- 出處：*J Appl Physiol* 108:866–874, 2010；DOI 10.1152/japplphysiol.91425.2008。
- 作者：Ferguson C, Rossiter HB, Whipp BJ, Cathcart AJ, Murgatroyd SR, Ward SA。
- 原始檔：`C:\原始資料\ferguson-et-al-2010-effect-of-recovery-duration-from-prior-exhaustive-exercise-on-the-parameters-of-the-power-duration\effect of recovery duration from prior exhaustive exercise on the parameters of the power duration.md`

## Reliability Level

- 來源層級：3（依 wiki source_tier 慣例：original research article 標 3，與 Beaver 1986、Caen 2021、Lievens 2024 同級）。
- 對應 AGENTS.md §4 第 5 級（original research article）；frontmatter 數字僅為內部 tier 標示，與 §4 文字描述對齊但編號不直接相同。
- evidence_level：limited（n=6 男性、單一 cycling 模式、recovery power 僅 20 W）。
- confidence：medium。
- contested：true（W' 物理意義仍未定論；本研究以 kinetic 三比較反對單純「儲能耗竭」模型）。

## One-Sentence Summary

在 6 位健康男性 cycle ergometer 模型中，**exhaustive supra-CP conditioning bout 後 `CP` 幾乎不變、`W'` 隨 `2 / 6 / 15 min` 的 20-W recovery 曲線式回到 `~37% / 65% / 86%`，且 `W'` recovery 速度比 `VO2` 慢、比 blood lactate 快**——支持 `W'` 並不是單一可被 PCr 或 lactate proxy 完全取代的能量儲槽。

## Core Concepts Extracted

### Concept: Post-exhaustion W' recovery kinetics (與 VO2 / blood lactate 同步比對)

#### One-Sentence Definition

`W' recovery` 是指在 supra-CP exercise 達 limit of tolerance 後，**接續恢復期間 P-tLIM 雙曲線重建時所對應的 `W'` 數值如何隨 recovery duration 與 recovery power 回升**；本研究以 `2 / 6 / 15 min` of 20-W recovery 取得對應 W' 估計值，並同步比較 `VO2` 與 blood `[L−]` 的恢復曲線。

#### Known Facts

- 受試者：6 位 recreationally active healthy men；24 ± 4.2 yr；179.6 ± 7.5 cm；86.5 ± 15.3 kg。
- 測試：cycle ergometer（Excalibur Sport, Lode），breath-by-breath gas exchange（mass spectrometry + turbinometry），fingertip capillary `[L−]`（Analox GM-7）。
- Protocol 1：25 W/min ramp → 量 `VO2peak`、estimated `θL`（gas exchange criteria）。
- Protocol 2：四段不同強度 constant-load tests，3–12 min 範圍，依 `P = (W'/tLIM) + CP` 線性回歸求 `CP` 與 `W'`（`R² > 0.996`）。
- Protocol 3：先做一段 exhaustive `WR6` conditioning bout（≈ 6 min 預測耗竭強度），再插入 `2 / 6 / 15 min` 之 `20-W` recovery，再做三段 supra-CP constant-load tests 重建 post-conditioning P-tLIM。
- Group means (Protocol 1–2)：
  - `VO2peak` ≈ `3.82 ± 0.55 L/min`；`θ̂L` ≈ `1.87 ± 0.35 L/min`（≈ `49 ± 5% VO2peak`）。
  - `CP` ≈ `212 ± 34 W`；`W'` ≈ `21.60 ± 5.16 kJ`；`WR6` ≈ `269 ± 34 W`；`[L−]LIM` ≈ `10.14 ± 0.97 mM`；`VO2max` ≈ `3.78 ± 0.56 L/min`。
- Conditioning bout：tolerable duration `366 ± 21 s`；`VO2peak` 與 control 不顯著差異；`[L−]LIM` ≈ `10.11 ± 1.02 mM`。
- Post-conditioning CP（與 control 比較，`P = 0.922`）：
  - 2-min Rec：`213 ± 36 W`；6-min Rec：`213 ± 34 W`；15-min Rec：`213 ± 36 W`。
- Post-conditioning W'（與 control 比較，`P = 0.001`）：
  - 2-min Rec：`7.8 ± 1.4 kJ`（`37 ± 5%` of control）。
  - 6-min Rec：`14.1 ± 3.7 kJ`（`65 ± 6%`）。
  - 15-min Rec：`18.5 ± 4.6 kJ`（`86 ± 4%`）。
- Interpolated half-times：
  - `W'` recovery：`t1/2 = 234 ± 32 s`。
  - `VO2` recovery：`t1/2 = 74 ± 2 s`。
  - blood `[L−]` recovery：`t1/2 = 1,366 ± 799 s`（依 6→15 min 段外推）。
- 「Baseline」 VO2 在 conditioning 結束後仍升高，並逐步下降：`1.37 ± 0.20`（2 min）、`1.06 ± 0.12`（6 min）、`0.87 ± 0.13 L/min`（15 min），均高於 control 20-W baseline `0.74 ± 0.08 L/min`。
- 殘留 `[L−]`：2 min `10.00 ± 0.91 mM`、6 min `9.09 ± 1.28 mM`、15 min `6.43 ± 1.58 mM`；即使 15 min 仍顯著高於 pre-exercise。
- Post-conditioning P-tLIM 仍維持 hyperbolic（`R² > 0.994`），CP/W' SE 維持 `< 3 W` / `< 1.25 kJ`。
- 所有 bout 結束時 `VO2peak` 與 `[L−]LIM` 大致與 control 相當（meeting `VO2max` criterion）。

#### Mechanism Chain

1. supra-CP exercise 持續耗 `W'` → 達 `tLIM` 時 `W' ≈ 0`，並伴 `VO2peak`、高 `[L−]`、可能的 `Pi / K+ / H+ / oxidative stress` 累積。
2. 進入 20-W recovery：因 `power < CP`，可進行 net aerobic energy transfer → `W'` 開始重建；同時 `VO2` 由 `VO2peak` 退向接近 baseline、blood `[L−]` 緩慢由 muscle/blood 清除。
3. 三條曲線各有自己的恢復時間尺度：
   - `VO2` recovery 反映 muscle O2 consumption / PCr resynthesis 為主的快動力學（intramuscular `[PCr]` 在 fatigue 後常以「fast + slow」雙相恢復；`VO2` 也對應 fundamental + slow component 的 off-kinetics）。
   - blood `[L−]` recovery 受 MCT1/MCT4 transport、free diffusion、相鄰氧化纖維 / 心臟 / 肝臟攝取再氧化、與 buffering 共同決定，速度遠慢於 PCr / `VO2`。
   - `W'` recovery 介於兩者之間且呈 curvilinear，提示 multiple parallel processes 共同決定 supra-CP 可用容量的回補。
4. 當下一段 supra-CP test 開始時，剩下的 `W'` 決定該段 `tLIM`；CP 不變代表「sustainable 上限」未受影響，`W'` 才是 prior fatigue 的承擔者。

#### Inferences

- 因 `W'` recovery 比 `VO2` 慢得多，**單一 PCr / VO2 proxy 不足以代表整體 `W'` recovery**：作者推論若 `PCr` 與 `W'` 直接等價，則需引入比 `PCr` 慢的額外回補機制（如 fatigue-metabolite clearance、glycogen-dependent excitation-contraction coupling）。
- W' 與 `VO2` recovery 雖近似 linear，但 linear 外推會出現「`VO2` 必須先恢復約 60% 才開始有 `W'` recovery」這類不合理推論；作者偏好 curvilinear 通過原點的描述（dashed-dotted 曲線）。
- `CP` 對 prior exhaustion 不敏感且與 `VO2max` 同樣不變，提示 `CP` 不被 W' depletion 直接拉低，與 anaerobic-energy-transfer-only 解釋不一致；推論 `W'` 也許更像「fatigue induction integrator」而非單一 `anaerobic store`。
- `W'` recovery 比 blood lactate clearance 快，提示 lactate clearance（與可能伴隨的 glycogen repletion）並非 `W'` recovery 的速率決定因素；但 intramuscular `[L−] / [H+]` 的時間進程仍未直接量到，故只能 kinetic-grounds 推論。

#### Assumptions

- WR6 conditioning bout 在 `tLIM` 時 **完全耗盡 W'**，或耗到接近極小限度（作者接受此前提）。
- `W' estimate` 來自 post-conditioning P-tLIM 線性 fit，被視為 **代表 recovery 結束時刻** 的 W'（即假設 post-conditioning bout 中 W' 不再額外恢復，因 supra-CP 期間 `W'` 流向被視為單向）。
- 以 pulmonary `VO2` 作 intramuscular `[PCr]` 與 muscle O2 uptake 的 reasonable proxy（雖經 30 多年文獻支持，仍屬 indirect）。
- 三段 post-conditioning bouts 的 WR 為 control protocol 用過的範圍，並依 W' 下降後的 `tLIM` 範圍（3–12 min）允許微調；隱含 P-tLIM 線性轉換在縮小 `W'` 後仍可用同一線性方法估參數。
- 採 group mean 進行半時間 (t1/2) 內插；曲線形狀沒有被強加成 mono- 或 bi-exponential。

#### Uncertainties / Limitations

- 樣本只有 `n = 6` 健康男性、recreationally active；無女性、青少年、長者、運動員、心肺患者資料。
- 只測 cycling，且 recovery power 固定為 `20 W`；無法外推到不同 mode、不同 active recovery intensity 或 race-specific surges。
- 未量 intramuscular `[PCr]` / `[L−]` / `[H+]` / glycogen，皆以 surrogate 推論；放在 magnetic resonance / biopsy 對照條件下，不確定 surrogate 與 actual intramuscular 速率的耦合度。
- 未做正式 mono- / bi-exponential 模型擬合（n=3 點 / 受試者 / VO2 SNR 太低、避免 training effect 才不延長 protocol）；t1/2 為內插值，不應與 model-derived `tau` 直接比較。
- 「VO2 仍升高」的 baseline 偏移代表 post-conditioning bout 起點的 `VO2 deficit` 較小；作者明文承認 work efficiency 可能改變、無法完全排除。
- 假設 W' 在 conditioning 結束時為零；若實際殘留正向，則 fractional recovery 會被高估。
- 僅一個 conditioning bout intensity（`WR6`）；不同 depletion 程度可能改變 recovery shape（partial vs full exhaustion 的差異未被本文檢驗）。

## Clinically Useful Points

- 把 supra-CP work-and-recovery 視為臨床/復健「intermittent severe-domain」測試或處方時，本研究提醒：**短 recovery（如 `2 min`）後再做 supra-CP work，可能只剩下 control W' 的約 1/3**；用 `平均功率` 或 `總工作量` 代理刺激會嚴重低估後段失能風險。
- `CP` 對 prior exhaustion 高度穩定，可作為「sustainable upper boundary」的較可靠 anchor；但 **不要把 `CP` 不變當作受試者整體尚未疲勞的證據**——`W'` 可在同一時間段大幅縮減。
- 若臨床族群（HF、COPD、frail elderly、neuro）擔心 supra-CP exhaustive paradigm 的安全性，本研究本身不支持把這類 protocol 直接搬到該族群；只可作為 healthy adult cycling reference。
- 解釋病人主觀「短休後仍很喘但工作能力回得不夠」現象時，可用 W'/VO2/lactate 三條時間尺度差異提醒病人與團隊：**呼吸（`VO2`）回得最快，乳酸感最久才走，但實際剩下的 supra-CP 工作預算介於兩者之間**。

## Research-Useful Points

- 是少數同步取得 W' 與其 putative physiologic correlates 的人類研究，常被後續 W' recovery / W'BAL 文獻當作 baseline benchmark（Skiba 2012 / 2015、Caen 2019 / 2021、Lievens 2024 都會引用）。
- 設計上以「post-conditioning P-tLIM 重建」估 W'（而非單一 TTE 推回 `W' = 0`），是處理 W' recovery 的較嚴謹路徑；後續若要重做 partial-depletion 對照，應沿用「重建 P-tLIM」而非單一 bout。
- 提供 `W' / VO2 / [L−]` 三條時間尺度的 group-mean 比對，可作為更高解析度（biopsy / 31P-MRS / arterial-venous L− balance）研究的設計藍本。
- 提示後續研究應該量化：①不同 recovery power 對 `W'` recovery 的影響；②partial vs full exhaustion 的 recovery shape 差；③不同 mode（running、upper-body、wheelchair）；④女性、年齡、訓練狀態與疾病族群。
- W' 恢復「與 fatigue metabolite accumulation/clearance 對應」的假說是一條未被本研究直接量到、但被本文 explicit 支持的研究方向；後續若做 NMR-spectroscopy 追 `Pi`、`H+`、`K+` 動力學可直接接續。

## Conflicts With Existing Knowledge

- 與「`W'` ≡ 一個有限 anaerobic 油箱，耗盡即 exhaustion」衝突：CP 不變、W' 曲線恢復、且 `[L−]LIM`、`VO2peak` 不隨 prior exhaustion 改變，皆與單純 finite-store 解釋不合。
- 與「W' recovery ≈ PCr / VO2 recovery」衝突：`W'` 慢於 `VO2` 約三倍 t1/2，需引入更慢的回補機制。
- 與「W' recovery ≈ lactate clearance」衝突：blood lactate t1/2 ≈ 1366 s，慢於 W' 約 5–6 倍，且兩者間無清楚比例關係。
- 與「prior heavy / supra-CP exercise 會降低 CP」衝突：本研究 CP 在三種 recovery 下皆不變，與 Coats et al. 2003 的 CP 可下降說法不一致；作者明確不採信 Coats 假設。
- 與「W'BAL 等於精確的 anaerobic balance」衝突：本研究強調 W' recovery 是 model-extracted whole-system construct，不是直接量到的儲量。

## Pages That Should Be Created or Updated

- 既有概念頁（已連回本來源摘要，仍應依本輪修正過 reasoning）：
  - `04_CPET/Wprime_Recovery.md`
  - `04_CPET/Wprime_Balance_Model.md`
  - `04_CPET/CP_Wprime_Interval_Design.md`
- 既有相關概念頁（本來源不直接重寫，但 reasoning 可以引用）：
  - `04_CPET/Critical_Power.md`
  - `04_CPET/Training_Prescription_by_CP.md`
  - `04_CPET/CP_Test_Reliability.md`
  - `05_Exercise_Physiology/PCr_Resynthesis.md`
  - `05_Exercise_Physiology/Skeletal_Muscle_Energy_Metabolism.md`
- 不於本輪新建概念頁；本來源核心仍是「post-exhaustion W' recovery kinetics」，現有 `Wprime_Recovery` hub 可承載，不需強行另開 fact-thin 子頁。

## Suggested Tags

`W_prime`、`recovery`、`critical_power`、`lactate`、`VO2_recovery`、`fatigue_metabolites`、`original_article`、`cycle_ergometry`、`P-tLIM`、`single_source_correction`。
