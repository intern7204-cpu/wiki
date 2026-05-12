---
title: F Response 與 F Estimate 判讀
created: 2026-05-11
updated: 2026-05-11
type: concept
domain: [PMR, methodology, electrodiagnosis]
tags: [EDX, NCS, F_response, F_estimate, late_responses, proximal_segment, GBS, polyradiculopathy, S1_radiculopathy, internal_control]
sources:
  - 10_來源摘要/Late_Responses.md
source_tier: 1
evidence_level: textbook_chapter
confidence: high
contested: true
contradictions:
  - Prolonged F response does not specifically localize to a radiculopathy or plexopathy; any motor-nerve lesion or simply a longer limb can prolong it.
  - Normal F response does not exclude radiculopathy; sensitivity for EMG-confirmed S1 radiculopathy is around 4-8%.
  - Absent F responses in nerves with severely reduced CMAP amplitude do not imply a proximal lesion.
---

# F Response 與 F Estimate 判讀

## One-Sentence Definition

F response 是 distal supramaximal motor stimulation 後，極小比例的 anterior horn cells 經 antidromic-orthodromic backfire 產生的晚期 motor potential；它測整條 motor nerve（含 distal segment），site / disease specificity 低，需要用 F estimate 把 distal motor latency、conduction velocity 與 limb length 校正後再判讀。

## Definition and Boundary

- 本頁只處理 F response 與 F estimate 的 circuitry、measurement、normative reference 與判讀邊界。
- 本頁不取代 [[H_Reflex_臨床用途與限制]] 或 [[A_Wave_Axon_Reflex判讀]]。
- 本頁不建立 Guillain-Barré syndrome、CIDP、entrapment neuropathy、polyneuropathy、radiculopathy 或 plexopathy 的完整 diagnostic criteria。
- 本頁僅引用單一來源：[[../10_來源摘要/Late_Responses]]。

## Why It Matters

- F response 是少數可從 EMG lab routine 測到 proximal segment 的工具之一；當 routine distal NCS normal 時，prolonged F 可提示 proximal demyelination（例如 early GBS）。
- 把 prolonged F latency 直接讀成「radiculopathy」是常見錯誤；F response 走整條 nerve，distal slowing 或 long limb 也會拉長 F latency。
- 把 normal F 當成「排除 radiculopathy」也是常見錯誤；F response 對 radiculopathy 的 sensitivity 很低。
- F response 在 severely reduced CMAP 的 nerve 上常不可得，這時 absent F 沒有 proximal-lesion 意義。

## Preconditions or Conditions

- Stimulation 必須真正 supramaximal；只看 waveform 不夠，需 plateau 後再加 20-25% current。
- 設定：gain 約 200 μV、sweep 5–10 ms、cathode 朝近端、刺激頻率 ≤ 0.5 Hz；至少 10 次 rastered stimulations。
- Distal CMAP amplitude 太低（例如 200 μV 量級）時，absent F 不應解讀為 proximal lesion。
- 病人若 sleeping / sedated，F 可能 absent / impersistent，這不一定是 pathology。
- Peroneal F response 在正常人也可能 absent / impersistent，需特別小心。
- 判讀前需先看 distal motor latency 與 motor conduction velocity；distal slowing 會直接拉長 F latency。
- Limb length（身高）需納入考量；taller patients 的 F latency 較長。

## Mechanism

```text
Distal supramaximal motor stimulation
→ orthodromic motor volley → CMAP (M response)
→ antidromic motor volley up axon → anterior horn cell
→ small population of motor neurons backfires (~1 ms turnaround)
→ orthodromic action potentials descend past stimulation site
→ small late motor potential = F response (1-5% of CMAP amplitude)
→ each stimulation activates a different motor neuron set
→ measure minimal latency, chronodispersion, persistence
```

### F estimate logic

```text
Theoretical minimal F latency
= time stim → spinal cord  +  AHC turnaround  +  time spinal cord → muscle
= (D / CV) × 10  +  1 ms  +  (D / CV) × 10  +  DL_distal-segment-effect-already-in-DL
```

The textbook collapses this into:

```text
F estimate = (2D / CV) × 10 + 1 ms + DL
where D = distance stim site → spinal cord (cm)
      CV = motor conduction velocity (m/s)
      DL = distal motor latency (ms)
      10 = m/s → ms / cm conversion
```

Surface approximation of D:

- Median / ulnar at wrist → C7 spinous process to wrist stimulation site.
- Peroneal / tibial at ankle → xiphoid process to ankle stimulation site.

## Observable Patterns

- Distal stimulation：F latency 約 25–32 ms（median / ulnar at wrist）、45–56 ms（peroneal / tibial at ankle）。
- Proximal stimulation：M latency 增加，但 F latency 反而縮短，因為 antidromic 行程變短。
- Normal chronodispersion：upper extremities 至 4 ms、lower extremities 至 6 ms。
- Normal persistence：通常 80–100%、最少 > 50%；peroneal F 例外。
- Distal motor latency 延長（例如 median neuropathy at wrist）→ F latency 也延長。
- 全身性 conduction slowing（polyneuropathy）→ F latency 整體延長。
- 多刺激下 F latency / configuration 略變動是常態；穩定不變、latency 一致的晚期 potential 應考慮為 [[A_Wave_Axon_Reflex判讀|axon reflex (A wave)]]。
- 測得 minimal F latency > F estimate：disproportionate proximal-segment slowing。
- 測得 minimal F latency < F estimate（小幅）：常見，因為近端 nerve 速度略快於遠端（fiber diameter 較大、temperature 較高）。
- Severe distal axonal loss（CMAP amplitude 極低）→ F response 常 unobtainable，absent F 不代表 proximal lesion。
- Sleeping / sedated → F response 可變低或消失，無病理意義。
- Peroneal F absent / impersistent in a normal subject 是可被接受的常態。

## Clinical / Research Implication

- 早期 Guillain-Barré syndrome：routine motor NCS 可仍 normal，但 F response 已 prolonged 或 absent，反映 proximal demyelination。這是 F response 最有價值的場景。
- 在 distal entrapment neuropathy（例如 carpal tunnel syndrome），F response 通常 prolonged，可作為 internal control，輔助 acquired demyelination 判讀，但不能單獨定位。
- Polyneuropathy 中 F response 的延長須與 distal motor latency / CV 一起看；單獨 F latency 通常無新訊息。
- Radiculopathy / plexopathy：
  - Upper extremity 只能評估 C8–T1（routinely recorded median APB / ulnar ADM）；C5–C7 radiculopathy 不會在 distal median / ulnar F 上出現。
  - Lower extremity 只能評估 L5–S1（distal peroneal / tibial muscles）。
  - 預設多 myotome dual innervation、segmental demyelination dilution 與 sensory-predominant lesion 都會讓 F latency 維持 normal。
  - Mauricio et al. (2014)：tibial F 對 EMG-confirmed S1 radiculopathy 的 sensitivity 僅約 4%；加上 F estimate 也只到約 8%。
- 不可寫「prolonged F = radiculopathy」也不可寫「normal F = no radiculopathy」。
- Side-to-side comparison 比 absolute reference 更敏感；無症狀側可作 internal control。
- F estimate 的最大臨床價值是在 tall patient、distal slowing 或 borderline F latency 情境下，避免把「身高長 / 遠端慢」誤判為近端病變。

## Fact

- F response 是 1–5% CMAP amplitude 的 pure-motor late potential，無 synapse、不是 true reflex。
- F response 每次 stimulation 都會略微改變，因為每次活化的 anterior horn cell 群不同。
- Sensory-only lesion 不影響 F response。
- Normal F latency：median / ulnar at wrist 約 25–32 ms；peroneal / tibial at ankle 約 45–56 ms。
- Proximal stimulation → F latency 縮短。
- F response 設定：supramaximal stimulation、cathode proximal、gain 200 μV、sweep 5–10 ms、≤ 0.5 Hz、至少 10 rastered stimulations。
- Normal chronodispersion ≤ 4 ms（upper） / ≤ 6 ms（lower）；persistence > 50%（peroneal 可例外）。
- Minimal F latency 是最可靠的測值；chronodispersion / persistence 的 side-to-side 差異偶可幫忙。
- F estimate = (2D/CV) × 10 + 1 ms + DL；surface D 使用 C7–wrist（上肢）與 xiphoid–ankle（下肢）。
- Measured minimal F latency 通常略短於 F estimate，因近端速度略快。
- Distal slowing、global slowing 都會延長 F latency。
- F response 1%–5% 來自 CMAP；severely low CMAP 時通常無 F、absent F 沒病理意義。
- Mauricio et al.：tibial F 對 EMG-confirmed S1 radiculopathy 的 sensitivity ≈ 4%；加 F estimate ≈ 8%。
- Jendrassik (reinforcement) 可在 F response 不可得時 prime motor neurons；但若已可得就不該做，因 over-priming 可能反讓 F response 不出現。

## Inference

- Reporting language 應寫成「prolonged F responses, consistent with distal slowing in median neuropathy at the wrist」或「prolonged F responses out of proportion to distal latency / CV / limb length, suggesting proximal slowing」，而不是直接寫「proximal lesion」。
- Normal F response 不應寫成「rules out radiculopathy」，較合理是「does not provide evidence of proximal motor demyelination affecting recorded muscles」。
- F estimate 應視為 baseline-correction tool，不是 stand-alone diagnostic threshold。

## Assumption

- Lab 有正確 normative tables、temperature control、supramaximal stimulation 程序與測距方法。
- Surface 測量點（C7 spinous process、xiphoid process）與真實 cord-to-stim 距離有合理近似關係。
- 若需要 Jendrassik，操作者能判斷何時該用、何時該避免。

## Uncertainty

- F response 對 radiculopathy / plexopathy 的特異性與敏感度都低。
- Sleeping / sedated patient 的 absent F 是 false positive 還是 technical issue 不易明確切割。
- Peroneal F absent / impersistent 是 normal variant，但邊界沒有絕對 cutoff。
- Borderline 延長的 F latency 是否真為 proximal lesion，常需配合 needle EMG、H reflex、ultrasound 與臨床。

## Limitations and Misreadings

- 誤讀：「Prolonged F latency = radiculopathy。」正確是 prolonged F 可來自 distal slowing、polyneuropathy、long limb 或 proximal lesion。
- 誤讀：「Normal F latency = 排除 radiculopathy。」正確是 partial fiber involvement、sensory-predominant lesion、segmental demyelination dilution 與 dual myotome innervation 都可保留 normal F。
- 誤讀：「Absent F = proximal lesion。」正確是 severely low CMAP、sleeping / sedated patient、normal peroneal 都可有 absent F。
- 誤讀：「Stable, identical-latency 晚期 potential 也是 F response。」正確是它較可能是 [[A_Wave_Axon_Reflex判讀|axon reflex (A wave)]]。
- 誤讀：「F response 是 reflex。」正確是它沒有 synapse，是 antidromic backfire，純 motor。
- 誤讀：「Jendrassik maneuver 是常規步驟。」正確是僅在 F response 不可得時使用；不必要時可反讓 F response 消失。
- 誤讀：「F latency 比 F estimate 小代表異常。」正確是 measured F 通常稍短於 F estimate，因近端速度略快。

## Links

- [[NCV_EMG_周邊神經病變總覽]]
- [[電生理診斷醫學]]
- [[EDX_解剖與神經生理基礎]]
- [[EDX_定位導向檢查流程]]
- [[NCS_軸突損失與脫髓鞘判讀]]
- [[H_Reflex_臨床用途與限制]]
- [[A_Wave_Axon_Reflex判讀]]
- [[Upper_Extremity_NCS_常規技術與陷阱]]
- [[Lower_Extremity_NCS_常規技術與陷阱]]
- [[../10_來源摘要/Late_Responses]]
