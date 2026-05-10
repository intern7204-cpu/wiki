---
title: Lievens et al. 2024 — Characterizing the Exponential Profile of W' Recovery Following Partial Depletion
created: 2026-04-25
updated: 2026-05-06
type: source_summary
domain: [CPET, exercise_physiology, performance_modeling]
tags: [W_prime, recovery, partial_depletion, monoexponential, biexponential, W_BAL, original_article]
source_tier: 3
evidence_level: limited
confidence: medium
contested: true
contradictions:
  - Exhaustion-derived biexponential W' recovery should not be directly generalized to partial depletion.
  - Fixed universal tau values remain insufficient across depletion levels and individual aerobic fitness.
---

# Source Summary: Lievens et al. 2024 — Characterizing the Exponential Profile of W' Recovery Following Partial Depletion

## Source Type

- Original research article.
- Journal: *Medicine & Science in Sports & Exercise*.
- Citation: Lievens M, Ghijs M, Bourgois JG, Vermeire KM, Bourgois G, Colosio AL, Boone J, Caen K. *Characterizing the Exponential Profile of W' Recovery Following Partial Depletion.* 2024;56(9):1770-1781.
- DOI: 10.1249/MSS.0000000000003468.
- 原始檔：`C:\原始資料\characterizing_the_exponential_profile_of_w_.24\characterizing_the_exponential_profile_of_w_.24.md`

## Reliability Level

- Evidence tier: Tier 3 original article.
- 可信度：medium。
- 理由：設計直接針對 partial W' depletion，protocol 細緻且有 model-complexity penalty；但樣本數小（n = 9）、全為 healthy young men，且 W' depletion 是 CP model 推估而非直接量測。

## One-Sentence Summary

在 partial W' depletion（25% / 75%）後，這篇研究沒有支持「一定要用 biexponential model」來描述 W' recovery；但它強化了另一個重點：固定 universal tau 不足，W' recovery 需要納入 depletion state、recovery intensity 與個體 aerobic fitness。

## Core Concepts Extracted

### Concept: Partial W' Depletion Recovery Kinetics

#### One-Sentence Definition

Partial W' depletion recovery kinetics 指 W' 尚未完全耗盡時，後續可用 work capacity above CP 如何在短至中等 recovery interval 中恢復。

#### Known Facts

- 受試者為 9 位 healthy young men；多為每週有 recreational 或 competitive sports activity 的 physical education students。
- 研究先以 ramp incremental test 與 3-5 次 constant-load trials 估算 CP 與 W'。
- Experimental trials 設計為兩段 P4 work bouts：WB1 用 1 或 3 分鐘造成理論上的 25% 或 75% W' depletion；recovery 為 30、60、120、300 或 600 秒，強度固定在 90% GET；WB2 做到 exhaustion，以估算 W'OBS。
- W'OBS 用 monoexponential 與 biexponential models 擬合，且各自測試 free amplitude 與 fixed amplitude。
- Biexponential fits 的 RMSE 較低，但在 free amplitude fits 中，AICc favor monoexponential；fixed amplitude fits 則 DEP25% favor monoexponential、DEP75% favor biexponential。
- DEP25% 與 DEP75% 的 mean W'OBS 高度相關（r = 0.92）。
- W'OBS 與 VO2peak、CP、GET 呈正相關（r = 0.67-0.77）。
- Monoexponential tau 在 DEP25% 約 32 s、DEP75% 約 82 s，但作者指出 tau 不能單獨代表 recovery speed，因為 amplitude 也不同。
- Initial 30 s recovery 的 W'OBS change 在 DEP25% 與 DEP75% 相近（約 +21% vs +23%）。
- 既有 Skiba-1、Skiba-2、Bartram models 不能準確描述本研究 temporal W' recovery profile。
- DEP25% 後 W'OBS 可超過理論 100%，10 分鐘後平均最多約 +11%，作者以 WB2 的 aerobic priming / higher relative aerobic contribution 解釋。
- DEP75% 後 model fit plateau 約在 83% W' recovery，提示 large depletion 可能妨礙後續 high-intensity capacity 完全恢復。
- Perceived W' recovery 平均比 W'OBS 低約 25%，表示受試者主觀上低估了恢復程度。

#### Mechanism Chain

1. CP/W' model 把 >CP work 視為消耗 finite W'。
2. 真實 intermittent exercise 常是 partial depletion，而不是每次都把 W' 用到 0。
3. 若直接把 full exhaustion data 的 two-phase recovery 套用到 partial depletion，會假設 recovery shape 不受 prior depletion state 影響。
4. Lievens 2024 的資料顯示 partial depletion 下，biexponential model 未能在 AICc 上穩定勝過 monoexponential。
5. 但固定 tau models 又無法同時處理 DEP25%、DEP75%、recovery intensity 與個體 aerobic fitness 差異。
6. 因此更合理的模型方向不是單純「mono vs biexponential」二選一，而是 dynamic / individualized recovery parameters。

#### Inferences

- Partial W' depletion 應視為 W' recovery modeling 的獨立情境，不能被 full exhaustion recovery 直接代表。
- Short recovery 的 underprediction 可能不只來自 model family，也來自 CP/W' model 對 aerobic contribution onset、priming effect 與 recovery-state carryover 的簡化。
- 對 interval prescription 而言，recovery duration、recovery power、prior depletion level 與 athlete-specific aerobic fitness 都應被明確寫入，不應只用單一 tau 估算所有情境。

#### Assumptions

- 25% 與 75% W' depletion 是由 CP/W' model 推估，並非直接量到的 physiological W' consumption。
- WB2 performance 可作為 W'OBS 的 operational estimate。
- 90% GET recovery intensity 可代表一種 controlled active recovery condition，但不代表所有 recovery power。

#### Uncertainties / Limitations

- 樣本數小，且只有 healthy young men；不能直接外推至 women、elite athletes、older adults、cardiopulmonary disease 或 rehabilitation patients。
- W' 沒有直接量測方法，因此 partial depletion 的精確程度仍有假設。
- 本研究 recovery 固定在 90% GET；更低或更高 recovery power 可能改變 best-fit model。
- Absence of true warm-up before WB1 可能放大 WB2 aerobic priming，讓 DEP25% 後 W'OBS 超過 100%。
- 這篇不是否定 exhaustion 後可能出現 two-phase recovery，而是限制其外推範圍。

## Clinically Useful Points

- 對 rehabilitation 或 clinical exercise prescription，這篇不能直接變成治療建議；它的臨床價值主要在避免把 W'BAL 當成精確生理油箱。
- 若要用 CP/W' 指導 high-intensity interval training，應把 recovery intensity、recovery duration、prior depletion pattern 與個體 aerobic fitness 寫清楚。
- 主觀疲勞感可能低估 W'OBS recovery；但這不等於病人或選手可以忽略 symptoms，因為 acidosis markers recovery 可能慢於 W'OBS。

## Research-Useful Points

- Model comparison 不能只看 RMSE；AICc 等 complexity penalty 會改變 monoexponential vs biexponential 的解讀。
- Future W' models 應納入 dynamic tau 或 individualized parameters，而不是固定 DCP-derived tau。
- Partial depletion recovery 應與 full exhaustion recovery 分開設計研究。
- W'OBS 與 VO2peak、CP、GET 的相關支持 aerobic fitness 是 W' recovery modeling 的關鍵 covariate。

## Conflicts With Existing Knowledge

- 與「W' recovery after exhaustion 是 two-phase，所以 all interval recovery 都應用 biexponential」衝突；本來源顯示 partial depletion 下證據不支持這種直接外推。
- 與「一個固定 tau 可描述不同 depletion level」衝突；本來源顯示固定 tau models 不足。
- 與「W'BAL = 真實剩餘 anaerobic tank」衝突；本來源再次顯示 W'OBS 會受 aerobic priming、model assumptions 與 perceived fatigue mismatch 影響。

## Pages That Should Be Created or Updated

- 新增：[[../04_CPET/Partial_Wprime_Depletion_Recovery]]
- 更新：[[../04_CPET/Wprime_Recovery]]
- 更新：[[../04_CPET/Wprime_Balance_Model]]
- 更新：[[../04_CPET/CP_Wprime_Interval_Design]]

## Suggested Tags

- `#CPET`
- `#exercise_physiology`
- `#critical_power`
- `#W_prime`
- `#W_BAL`
- `#interval_exercise`
- `#performance_modeling`
