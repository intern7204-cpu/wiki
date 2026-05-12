---
title: RNS Protocol 與技術陷阱
created: 2026-05-11
updated: 2026-05-11
type: concept
domain: [PMR, methodology, electrodiagnosis, neuromuscular_medicine]
tags: [EDX, RNS, repetitive_nerve_stimulation, protocol, technical_factors, temperature, supramaximal_stimulation, immobilization, acetylcholinesterase_inhibitor, facial_RNS, spinal_accessory_nerve, postexercise_facilitation, postexercise_exhaustion]
sources:
  - 10_來源摘要/Repetitive_Nerve_Stimulation.md
source_tier: 1
evidence_level: textbook_chapter
confidence: high
contested: true
contradictions:
  - RNS technical setup is not a minor detail; it can create false decrements, false increments, and false-negative studies.
  - Facial RNS is technically fragile because CMAP amplitudes are small and facial muscles cannot be immobilized well.
  - Cold limb and acetylcholinesterase inhibitors can reduce decrement and hide an NMJ disorder.
---

# RNS Protocol 與技術陷阱

## One-Sentence Definition

RNS protocol 與技術陷阱，是用溫度、固定、supramaximal stimulation、nerve / muscle selection、exercise timing、藥物狀態與 needle EMG confounder control，確保 RNS decrement / increment 是 neuromuscular junction physiology 而非 artifact。

## Definition and Boundary

- 本頁只處理 RNS acquisition、protocol sequence 與 technical validity。
- RNS 的 physiology 判讀見 [[RNS_Decrement_Increment判讀]]。
- 本頁不提供 myasthenia gravis、Lambert-Eaton myasthenic syndrome 或 botulism 的完整診斷流程。
- 本頁僅引用單一來源：[[../10_來源摘要/Repetitive_Nerve_Stimulation]]。

## Why It Matters

- RNS 對 movement、stimulus intensity、temperature 與 timing 很敏感；技術問題可直接變成 false diagnosis。
- Neuromuscular junction disorders 常影響 proximal、facial、bulbar muscles，但這些部位的 RNS technical difficulty 較高。
- RNS 判讀若沒有 needle EMG confounder control，可能把 denervation / reinnervation 或 myotonia 造成的 decrement 誤認為 primary NMJ disorder。

## Preconditions or Conditions

- 先明確 clinical question：myasthenia gravis、Lambert-Eaton myasthenic syndrome、botulism 或 broader fatigability / proximal weakness / bulbar / ocular concern。
- 檢查前確認 acetylcholinesterase inhibitor status；若無 medical contraindication，最好停用 3-4 小時。
- Recording site temperature 至少 33°C。
- Recording electrodes、stimulator 與 limb 必須盡量固定。
- 每次 RNS 前確認 supramaximal stimulation，而不是只看 CMAP 在 normal range。
- 先做 routine motor NCS，確定受測 nerve 的 baseline response 可解讀。

## Mechanism

```text
疑似 NMJ disorder
→ 選 clinically weak or relevant muscle
→ warm to >=33°C
→ immobilize electrodes / stimulator / limb
→ verify supramaximal stimulation
→ routine motor NCS baseline
→ rest 3-Hz RNS
→ brief exercise repair / facilitation
→ prolonged exercise exhaustion
→ low CMAP 時看 postexercise increment
→ needle EMG 檢查 denervation / myotonia confounders
→ 報告 technical limitations and physiology
```

## Observable Patterns

- Resting slow RNS：3-Hz RNS at rest，5-10 impulses，重複三次，每次間隔約 1 分鐘。
- Normal response：第 1 到第 4 response 間 <10% decrement。
- Reproducible >10% decrement：做 10 秒 maximal voluntary exercise 後，立即重複 3-Hz RNS，檢查是否 repair。
- No decrement or <10% decrement：做 1 分鐘 maximal voluntary exercise，立即與 1、2、3、4 分鐘後重複 3-Hz RNS，檢查 postexercise exhaustion。
- Prolonged exercise 後若出現 significant decrement，可再做 10 秒 maximal voluntary exercise 後立即 RNS，檢查 facilitation repair。
- Baseline CMAP amplitude low：做 10 秒 maximal voluntary exercise 後立即 supramaximal stimulation，尋找 abnormal increment。
- Exercise 超過 10 秒或 exercise 後不立即刺激，可能錯過 increment。
- Study selection：至少一條 distal motor nerve 與一條 proximal motor nerve；優先測 clinically weak muscles。
- Common nerves：ulnar、median、spinal accessory、facial。
- Source 偏好 spinal accessory nerve / upper trapezius 作為 proximal study，因 nerve 表淺、常可 supramaximal stimulation，且可用肩部下壓降低 movement。
- Facial RNS 的問題是 baseline CMAP 小與肌肉難固定；1 mV baseline CMAP 只要 0.1 mV drop 就是 10% decrement，容易 false positive。
- Slow RNS frequency：2 或 3 Hz；頻率太高會 calcium accumulation，太低會讓 mobilization store 補足 primary store。
- Rapid RNS：30-50 Hz，5-10 秒 train，但疼痛且難耐受；只有不能配合 exercise 時才使用。
- Slow train：5-10 pulses，兼顧 comfort 與足以看出 decrement。

## Clinical / Research Implication

- RNS report 應記錄：temperature、nerve / muscle、baseline CMAP、stimulation frequency、pulse number、是否 supramaximal、exercise duration、postexercise timing、AChE inhibitor status 與 technical limitations。
- RNS abnormality 應以 reproducibility 和 physiology pattern 支持，不應只用單一次 trace。
- 若 facial RNS abnormal 但 technical quality 差，應在報告中明確標示 uncertainty。
- 若同一肌肉 needle EMG 有 denervation 或 myotonia，該肌肉 RNS decrement 不應直接推論為 primary NMJ disorder。

## Fact

- RNS 不需特殊設備，但 poorly tolerated in some patients 且 technical problems 會影響 reliability / validity。
- RNS measurements are made on the CMAP, which sums individual MFAPs.
- Immobilization 是 RNS 最大 technical problem。
- Submaximal stimulation 可製造 artifactual decrement 或 increment。
- Cold limb 可 diminished decrement，造成 false-negative。
- Acetylcholinesterase inhibitors 可 diminished decrement。
- Proximal nerves 在 postsynaptic NMJ disorders 中 yield 較高，但 technical difficulty 較高。
- Facial RNS 較容易因小 CMAP 與 movement 造成 false positive。
- Rapid RNS 很痛；能合作時，brief maximal voluntary exercise 是較佳替代。
- Needle EMG 必須評估 proximal and distal muscles，尤其 clinically weak muscles。

## Inference

- RNS protocol 本身就是 diagnostic reasoning 的一部分；若 protocol 不可信，decrement / increment 的病理意義就不能成立。
- 對 RNS 而言，「可重現」與「符合 NMJ physiology」比單次數值超過 cutoff 更重要。

## Assumption

- 檢查者能即時判斷 CMAP stability、stimulation adequacy 與 electrode movement。
- 病人能理解並配合 10 秒或 1 分鐘 maximal voluntary contraction；若不能，需改用 rapid RNS 或標示限制。

## Uncertainty

- 本來源未提供所有 nerve / muscle 的 protocol-specific normal values。
- ICU、infant、coma、severe weakness、疼痛或 cognitive impairment 會限制 voluntary exercise protocol。
- AChE inhibitor 停用若 medically contraindicated，不能為了檢查強行停藥。

## Limitations and Misreadings

- 誤讀：「RNS 技術細節只是操作問題。」正確是 technical validity 直接決定 RNS 是否可判讀。
- 誤讀：「Facial RNS 最接近 ocular/bulbar symptoms，所以最可靠。」正確是 facial CMAP 小且難固定，false-positive 風險高。
- 誤讀：「Cold limb 只影響 routine NCS。」正確是 cold limb 會 diminished NMJ decrement，可能漏掉 myasthenia gravis。
- 誤讀：「Pyridostigmine 不影響 RNS。」正確是 acetylcholinesterase inhibitors 可減少 decrement，除非 contraindicated 通常需檢查前停 3-4 小時。
- 誤讀：「Low CMAP 時看 decrement 即可。」正確是 low baseline CMAP 時應找 postexercise increment，尤其 presynaptic NMJ disorder。
- 誤讀：「有 decrement 就不需要 needle EMG。」正確是 denervation / myotonia 也可造成 decrement，needle EMG 是 confounder control。

## Links

- [[RNS_Decrement_Increment判讀]]
- [[電生理診斷醫學]]
- [[EDX_定位導向檢查流程]]
- [[EDX_技術假象與品質控制]]
- [[NCS_軸突損失與脫髓鞘判讀]]
- [[../10_來源摘要/Repetitive_Nerve_Stimulation]]
