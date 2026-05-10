---
title: Muscle Fiber Types（肌纖維分類）
created: 2026-04-23
updated: 2026-04-24
type: concept
domain: [exercise_physiology, muscle_biology]
tags: [muscle_fiber_type, myosin, MHC, oxidative_capacity, CSA, specific_force, hybrid_fibers]
sources:
  - 10_來源摘要/Blemker_2023_fiber_type_traps.md
  - 10_來源摘要/Hargreaves_Spriet_2020_muscle_energy_metabolism.md
  - 10_來源摘要/Smith_2023_exercise_metabolism_adaptation_skeletal_muscle.md
source_tier: 4
evidence_level: consensus
confidence: high
contested: true
contradictions: []
---

# Muscle Fiber Types（肌纖維分類）

## 一句話定義

「muscle fiber type」不是單一軸線，而是至少包含 **myosin heavy chain（MHC）isoform、oxidative capacity、fiber cross-sectional area（CSA）、specific force** 等彼此只部分相關的屬性集合。

本頁是多來源 composite page；Blemker et al. 2023/2024 的單一來源拆頁見 [[Muscle_Fiber_Type_Traps]]。

## 核心機制

### 核心概念

### 1. MHC / myosin isoform 分類

- 最穩定、最可重現的 fiber typing 方式，是用 **MHC antibody / immunofluorescence** 區分 type I、IIa、IIx。
- 這個分類回答的是**收縮速度**問題，不直接回答代謝、fatigue resistance 或 force 大小。
- 人類幾乎不表達真正的 **MHC IIb**；舊文獻中的 human type IIb 多半實為 **IIx**。
- 訓練、disuse、disease 狀態可出現 **hybrid fibers**，代表轉換中的表型，而不是分類失敗。

### 2. Oxidative capacity 分類

- 代謝屬性應用 **SDH、NADH-TR、mitochondrial density、respiratory capacity** 直接評估。
- 同一 MHC 類別內，oxidative capacity 可呈現寬廣連續分布。
- 因此「fast = glycolytic、slow = oxidative」只是一種歷史性粗略印象，不是可普遍套用的生理定律。

### 3. CSA 與 force 不是 MHC 的直接替身

- Fiber CSA 受肌肉部位、物種、性別、年齡、loading history、disease 與 biopsy depth 影響。
- Whole-muscle force 受 **PCSA、pennation angle、fiber length、sarcomere operating range、tendon properties** 共同決定。
- 單靠 fiber type 分布，不能可靠推回整塊肌肉的 force-generating capacity。

### 三個常見陷阱

Blemker et al. 2023/2024 的完整單一來源拆解見 [[Muscle_Fiber_Type_Traps]]。

### Trap 1：把 MHC 與 oxidative capacity 視為同一件事

- Blemker 2023 明確指出：MHC 反映 contraction speed，oxidative capacity 則來自 mitochondrial / enzyme 系統。
- 在不同物種與不同肌肉，MHC IIx 的 oxidative phenotype 可以差很多。
- 結論：若研究問題是代謝能力，就必須量代謝；不能只量 MHC。

### Smith 2023：fiber type 是 myonuclear、mitochondrial 與 metabolic continuum

- Human torso / limb muscles 主要表達 MyHC type I、type IIA、type IIX；MyHC 主要決定 contraction speed，不足以單獨定義 metabolic phenotype。
- Full fiber phenotype 需要 excitation-contraction machinery、ATP supply、motor unit innervation 與 myonuclear synchrony 配合。
- Human 與 rodent data 不可直接等同：rodent type IIA 常是最 oxidative，human type I 常是最 oxidative；human fibers 整體也比 rat / mouse fibers 更慢。
- Human vastus lateralis 的 hybrid fibers 可由小於 10% 到 40%；true hybrid fibers 在 type I、I/IIA、IIA、IIA/IIX、IIX 之間呈 mechanical / metabolic continuum。
- Healthy human vastus lateralis 的 pure type IIX 通常小於 1%；sedentary behavior 可增加 hybrid / pure IIX fibers，exercise 常降低 hybrid content 並使 phenotype 遠離 IIX。
- Aging、metabolic health、training status、biological sex 與 anatomical location 都可改變 fiber properties；aging-associated mitochondrial impairment 甚至可造成 glycolytic shift 而不一定伴隨 MyHC 改變。

### Trap 2：把 fiber CSA 當作 fiber type 的代理指標

- 早期 rat 資料常見「fast fibers 較大」，但在 mouse 與 human 資料並不普遍成立。
- 同一肌肉內不同 depth、不同 sex，CSA 排序都可能改變。
- 結論：影像、histology、biopsy 若只報平均 CSA，不能直接宣稱 fiber type 改變。

### Trap 3：由 MHC 推論 force-generating capacity

- Specific force 並不一定隨 MHC 類別固定排序。
- 若把 fiber type 當成 whole-muscle force 的捷徑，容易忽略 architecture 與 tendon mechanics。
- 結論：MHC 是 contractile phenotype 的一部分，不是 force 的總代理。

### 方法學重點

| 問題 | 較佳指標 | 不應直接替代 |
|------|----------|--------------|
| 收縮速度 | MHC antibody、single-fiber mechanics | SDH、顏色分類 |
| Oxidative capacity | SDH、NADH-TR、mitochondrial markers | MHC 類別 |
| Fiber size | Laminin/dystrophin + image segmentation | MHC 類別 |
| Force | Specific force、architecture、whole-muscle mechanics | MHC 類別或 CSA 單獨 |

## 臨床表現

### 臨床與研究重要性

### 對 exercise physiology

- 解讀 [[Skeletal_Muscle_Energy_Metabolism]] 時，不能把「type 1 / type 2」直接等同於脂肪/醣利用能力。
- 解讀 [[../04_CPET/VO2_Slow_Component]] 時，應寫成「較多快纖維募集可能降低 efficiency」，而不是「type 2 = 一定低氧化能力」。

### 對 biomechanics / modeling

- 用 MRI、ultrasound 或 DTI 推估 fiber type 時，要明確說明那其實是在量 morphology，不是直接量 MHC 或 metabolism。
- 跨物種模型外推若忽略 fiber phenotype 解耦，容易得出錯誤生理結論。

### 對臨床病理

- Aging、neurologic injury、disuse、myopathy 會同時改變 MHC、CSA、oxidative capacity，但三者方向不必一致。
- 因此 biopsy 判讀應盡量把「type shift」「atrophy/hypertrophy」「mitochondrial abnormality」分開描述。

## 評估方式

- 目前頁面尚未整理出 History、Physical examination、Scale / test、Imaging / lab 的實際用法。

## 治療原則

- 本頁以概念或來源為主；若要進入真正 treatment plan，需連回對應臨床頁。

## 臨床決策點

- 什麼情況要治療？先看是否真的改變 pain、function、safety、participation 或訓練輸出。
- 什麼情況要轉介？遇到 red flags、診斷不確定、需要程序性介入或超出本頁可處理範圍時。
- 什麼情況不該做？當證據不足、機制不合、風險高於預期收益，或結果不會改變決策時。

## 限制與未定論

### 目前限制 / 爭議點

- 不同實驗室的 fiber typing 方法與 cutoffs 仍不完全一致。
- Human biopsy 樣本常偏向表層肌腹，代表性有限。
- Hybrid fibers 與連續分布意味著強行二分有時會犧牲真實性。

## 理解缺口

- Muscle Fiber Types（肌纖維分類） 和最相近、最常被混用的概念差在哪？
- 這個指標或概念反映的是直接機制，還是只是 operational proxy？
- 在什麼測試條件或族群下，這個概念最容易被錯用或外推失真？
- 目前缺少完整評估框架：History、Physical examination、Scale / test、Imaging / lab 仍需補強。
- 目前缺少明確處置順序：何時觀察、何時介入、何時轉介仍需補強。

## 臨床使用版

- 若要把 Muscle Fiber Types（肌纖維分類） 用在 bedside 或運動處方，先確認它回答的是哪一個機制或強度邊界，再決定能否改變評估與處置。
- 若這個概念無法改變你的臨床決策，就不要只為了名詞完整而硬套到病人身上。

## 來源

### 來源摘要連結

- [[10_來源摘要/Blemker_2023_fiber_type_traps]]
- [[10_來源摘要/Hargreaves_Spriet_2020_muscle_energy_metabolism]]
- [[10_來源摘要/Smith_2023_exercise_metabolism_adaptation_skeletal_muscle]]

### 證據標記

- 來源層級：4
- evidence_level：consensus
- confidence：high

## 相關頁面

### 相關頁面

- [[Skeletal_Muscle_Energy_Metabolism]]
- [[Muscle_Fiber_Type_Traps]]
- [[Skeletal_Muscle_Metabolic_Flexibility與Exercise_Adaptation]]
- [[PCr_Resynthesis]]
- [[../04_CPET/VO2_Slow_Component]]
- [[../04_CPET/VO2_Kinetics]]
- [[../04_CPET/Critical_Power]]
- [[../10_來源摘要/Blemker_2023_fiber_type_traps]]
- [[../10_來源摘要/Hargreaves_Spriet_2020_muscle_energy_metabolism]]
- [[../10_來源摘要/Smith_2023_exercise_metabolism_adaptation_skeletal_muscle]]
