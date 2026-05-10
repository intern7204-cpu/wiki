---
title: EDX 技術假象與品質控制
created: 2026-05-10
updated: 2026-05-10
type: concept
domain: [PMR, methodology, electrodiagnosis]
tags: [EDX, NCS, EMG, artifact, technical_factors, temperature, supramaximal_stimulation, co_stimulation, electrode_placement, anomalous_innervation]
sources:
  - 10_來源摘要/Anomalous_Innervations.md
  - 10_來源摘要/Artifacts_and_Technical_Factors.md
  - 10_來源摘要/Routine_Upper_Extremity_Facial_Phrenic_NCS_Techniques.md
source_tier: 1
evidence_level: textbook_chapter
confidence: high
contested: true
contradictions:
- Technically inaccurate EDX data cannot be fixed by later interpretation.
- Low amplitude, slowed velocity, prolonged latency, and proximal amplitude drop can be artifacts.
- Anomalous innervation is not a technical error, but it belongs in the same pre-diagnostic checklist before pathology is assigned.
---

# EDX 技術假象與品質控制

## One-Sentence Definition

EDX 技術假象與品質控制，是在判讀 NCS / EMG 前系統性確認 temperature、age、height、impedance、filters、stimulation、recording montage、distance、limb position 與 display settings，避免把 technical artifact 誤診為 neuropathy、entrapment、axonal loss、demyelination 或 conduction block。

## Definition and Boundary

- 本頁聚焦 EDX data acquisition validity，不整理特定疾病的 EDX diagnostic criteria。
- 本頁不是 nerve-specific protocol；routine upper / lower extremity NCS 應另頁處理。
- 本頁主要處理 technical artifact；anomalous innervation 另由 [[../10_來源摘要/Anomalous_Innervations]] 補入，作為判讀前需排除的 anatomic variant。

## Why It Matters

- EDX 量到的是 microvolt / millivolt 等級的小訊號；technical setup 本身就能改變 waveform。
- 技術錯誤可造成 type I error 與 type II error；source 特別強調 false-positive diagnosis 可能讓病人被貼上不存在的 disease label，導致不必要檢查與治療。
- 若資料收集不準，後續再精細的 interpretation 也不能補救。

## Preconditions or Conditions

- 每次 EDX 都應先確認 limb temperature、recording electrode quality、ground placement、stimulator orientation、supramaximal stimulation、distance measurement 與 sweep / sensitivity settings。
- 若 waveform 不符合臨床定位或生理預期，先回頭檢查 technical factors，而不是直接升級診斷。
- 對 pediatric、advanced age、extreme height、edema、ICU portable study 或 severe disease，要主動標示 norm / artifact limitation。

## Mechanism

```text
Small EDX signal
→ physiologic factor or technical setup changes
→ latency / velocity / amplitude / duration / morphology distortion
→ false axonal loss, demyelination, entrapment, conduction block, or normal study
→ technical review and correction
→ only then physiologic interpretation
```

## Observable Patterns

- Cool limb：conduction velocity slows、distal latency prolongs、CMAP / SNAP amplitude and duration increase；SNAP effect 通常比 CMAP 明顯。
- Cool limb 若出現 high-amplitude、long-duration SNAP 加 slow conduction velocity，應先懷疑 cooling，而非直接診斷 demyelination。
- Temperature 目標通常維持 distal limb 32-34°C；cooling 對 velocity 的影響約 1.5-2.5 m/s/°C，distal latency 約 0.2 ms/°C。
- Skin temperature 達標不代表 underlying nerve / muscle 已達標；profound cooling 時 nerve temperature 可能需 20-40 分鐘才 equilibrate。
- Advanced age 可降低 conduction velocity 與 SNAP amplitude；older adult 的 low / absent distal sensory response 不可孤立診斷 neuropathy。
- Taller individuals 與 lower extremity nerves 會有較慢 conduction velocity；late responses 需用 height / limb length norms。
- 60-Hz interference 常由 electrode impedance mismatch 造成，會遮蔽小 SNAP 或 fibrillation potentials。
- Lowering high-frequency filter 可減少 noise，但也會降低 recorded amplitude；不同 filter settings 的數值不可直接和不相符 normal values 比較。
- Stimulus artifact 可扭曲 onset latency 與 amplitude，尤其 sensory responses 或 short-distance stimulation。
- Reversed cathode / anode 可讓 distal latency 延長約 0.3-0.4 ms、sensory conduction velocity 慢約 10 m/s，模仿 polyneuropathy 或 distal entrapment。
- Submaximal distal stimulation 可模仿 axonal loss；submaximal proximal stimulation 可模仿 conduction block。
- Co-stimulation 可讓低 amplitude 變正常、製造 false conduction block、模仿 anomalous innervation，或遮蔽 true conduction block。
- Edema 或 recording electrode off nerve 可大幅降低 sensory / mixed response amplitude，甚至造成 absent response。
- Active-reference distance 太短會因 cancellation 降低 sensory amplitude；sensory / mixed studies 常用 3-4 cm。
- Ulnar across-elbow study 若 elbow extended，surface distance 會低估 true nerve length，造成 across-elbow conduction velocity artifactually slow。
- Sensitivity 增加通常會讓 onset latency measurement 變短；sweep speed 降低通常會讓 latency measurement 變長。

## Clinical / Research Implication

- EDX report 的 limitations 不應只寫「technical difficulty」；應具體標出 temperature、edema、noise、submaximal stimulation risk、co-stimulation risk 或 distance limitation。
- 判讀 conduction block 前，必須先確認 supramaximal stimulation、distal response validity、co-stimulation、anomalous innervation、temporal dispersion 與 nerve-specific normal variants。
- 若 technical factors 已排除但 amplitude pattern 仍反常，下一步應依 nerve map 檢查 anomalous innervation，而不是把所有反常 pattern 都歸為 artifact。
- Routine protocol 本身也會製造 artifact：ulnar elbow straight-line measurement、paired comparison distance mismatch、wrong FDI reference electrode、或 radial motor proximal distance surface error 都會改變判讀。
- 在 edema 中，正常 sensory response 有排除價值；low / absent response 需加 technical caveat。
- 自動化或 AI NCS interpretation 若沒有 temperature、height、age、edema、filter 與 stimulation adequacy metadata，容易把 artifact 當 disease。

## Fact

- EDX studies rely on acquiring and amplifying very small bioelectric signals.
- Correct interpretation requires technically accurate data collection.
- Temperature is the most important physiologic factor in the source.
- Distal limb temperature should be routinely measured and ideally maintained at 32-34°C.
- If warming is not possible, correction factors may be used, but warming / rewarming is preferable.
- Full-term infant conduction velocities can be 25-30 m/s at birth and normal, while adult interpretation would call this demyelinating range.
- Advanced age reduces conduction velocity and SNAP amplitude.
- Supramaximal stimulation requires current increase until response plateau and then roughly 25% additional current.
- Normal-range amplitude does not prove supramaximal stimulation.
- Cathode should face the active recording electrode; distance is measured from cathode to active recording electrode.
- Active and reference recording electrode impedance matching reduces 60-Hz noise through common mode rejection.
- Filter settings change waveform amplitude / duration and must match the normal values being used.
- Recording electrode distance from nerve changes amplitude and can change onset latency through volume conduction.

## Inference

- Technical review should be treated as part of the diagnostic algorithm, not as a pre-analytic footnote.
- When a pattern is physiologically unusual, such as slow velocity with high amplitude sensory response, artifact review should precede disease labeling.
- A repeat or corrected study can be clinically more honest than a forced interpretation from technically compromised data.

## Assumption

- The EDX lab has access to temperature measurement, adjustable stimulation / recording setup, and operator skill sufficient to troubleshoot artifacts.
- Lab normal values are tied to comparable filter, distance, electrode, age, height, and temperature assumptions.

## Uncertainty

- Correction factors for temperature are based mainly on normal nerves and may not apply to all diseased nerves.
- Some proximal stimulation sites inherently co-stimulate adjacent nerves; specialized methods may be needed.
- Edema, ICU environment, pain tolerance, and severe disease may prevent fully ideal acquisition.

## Limitations and Misreadings

- 誤讀：「數值 abnormal 就是 disease。」正確是先確認 technical validity。
- 誤讀：「Low amplitude = axonal loss。」正確是 submaximal stimulation、edema、recording off nerve、filter、co-stimulation 與 conduction block 都要排除。
- 誤讀：「Proximal amplitude drop = conduction block。」正確是先排除 proximal submaximal stimulation、distal co-stimulation、anomalous innervation 與 temporal dispersion。
- 誤讀：「Anomalous innervation 是技術錯誤。」正確是 normal anatomic variant；錯誤在於未辨識而誤診 pathology。
- 誤讀：「Normal value table 可以修正 protocol error。」正確是 normal value table 假設 controlled temperature、standard distance 與正確 technique。
- 誤讀：「Normal-range amplitude 代表刺激夠強。」正確是必須看到 plateau，再增加約 25% current。
- 誤讀：「溫度校正可以完全取代 warming。」正確是 source 偏好 warming / rewarming，因 correction factor 不一定適用 diseased nerve。

## Links

- [[電生理診斷醫學]]
- [[EDX_定位導向檢查流程]]
- [[NCS_軸突損失與脫髓鞘判讀]]
- [[EDX_異常神經支配變異判讀]]
- [[Upper_Extremity_NCS_常規技術與陷阱]]
- [[../10_來源摘要/Anomalous_Innervations]]
- [[EDX_轉介問題設計]]
- [[../10_來源摘要/Artifacts_and_Technical_Factors]]
- [[../10_來源摘要/Basic_Nerve_Conduction_Studies]]
- [[../10_來源摘要/Routine_Upper_Extremity_Facial_Phrenic_NCS_Techniques]]
