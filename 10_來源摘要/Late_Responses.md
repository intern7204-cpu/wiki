---
title: Late Responses
created: 2026-05-11
updated: 2026-05-11
type: source_summary
domain: [PMR, methodology, electrodiagnosis, neurophysiology]
tags: [EDX, NCS, late_responses, F_response, F_estimate, H_reflex, axon_reflex, A_wave, proximal_segment, GBS, S1_radiculopathy, reinnervation, textbook]
source_path: 'C:\原始資料\Late Responses\Late Responses.md'
source_tier: 1
evidence_level: textbook_chapter
confidence: high
contested: true
contradictions:
  - Prolonged F response 不能特異定位 radiculopathy；motor nerve 任何位置的 lesion、長肢長或 distal slowing 都可造成。
  - Normal F response 無法排除 radiculopathy；對 EMG-confirmed S1 radiculopathy 的 sensitivity 約 4-8%。
  - 老年人雙側 absent H reflex 不必然病理，常與年長者常見的 absent ankle reflex 對應。
  - Axon reflex (A wave) 並非真正 reflex；以「latency 與 configuration 在多次刺激下完全一致」與 F response 區分，這個辨識點很重要因為 A wave 容易被誤認為 F response。
---

# Source Summary: Late Responses

## Source Type

- 電生理診斷 textbook 第 4 章；內容涵蓋 F response、F estimate、H reflex 與 axon reflex (A wave)。
- 本輪僅以這篇單一來源 ingest，未混入 disease-specific diagnostic criteria、repetitive nerve stimulation、blink reflex 或本來源以外的其他 late-response 章節。

## Reliability Level

- 在本 wiki 對 EDX textbook chapter 的層級中屬 Tier 1。
- 強項：late response circuitry、normative values（median / ulnar / peroneal / tibial F latencies、tibial-soleus H latency 與 H/M ratio）、F estimate 公式，以及「late response vs routine NCS」的概念邊界。
- 引用一篇診斷產率研究（Mauricio et al., 2014），提供 tibial F response 與 F estimate 對 EMG-confirmed S1 radiculopathy 的 sensitivity 數據。
- 限制：本來源不提供 Guillain-Barré syndrome、polyneuropathy、S1 radiculopathy、sciatic neuropathy、lumbosacral plexopathy 或中樞性 H/M ratio 變化的完整 disease-specific diagnostic criteria。

## One-Sentence Summary

Late responses（F response、H reflex、axon reflex / A wave）以「antidromic backfire」、「Ia-mediated monosynaptic reflex」與「collateral branch 折返」三種不同 circuitry 把 NCS 延伸到 distal segment 以外；當 routine NCS normal 時，prolonged late response 可暗示 proximal slowing 或 reinnervation，但 site / disease specificity 低，prolonged late response 本身不能診斷 radiculopathy 或 plexopathy。

## Core Concepts Extracted

### Concept: F response 與 F estimate

#### One-Sentence Definition

F response 是 distal supramaximal motor stimulation 後，極小比例的 anterior horn cells 經 antidromic backfire 產生的晚期 pure-motor potential；它測整條 motor nerve（含 distal segment），F estimate 則用 distal motor latency、conduction velocity 與 limb length 校正測得的 minimal F latency。

#### Known Facts

- F response 是約 1%–5% CMAP 大小的小型 late response；每次刺激所活化的 anterior horn cell 群不同，因此 latency、configuration 與 amplitude 都會略有變動。
- F response 的 circuitry 純為 motor（motor afferent + motor efferent），無突觸，不是 true reflex。
- 在僅影響 sensory nerve 或 sensory root 的病灶下，F response 完全 normal。
- Normal F response latency：上肢（median / ulnar at wrist）約 25–32 ms；下肢（peroneal / tibial at ankle）約 45–56 ms。
- 把刺激移到較近端時，M response 的 latency 增加（如預期），但 F response 的 latency 反而縮短，因為 antidromic 行程變短。
- F response 在 distal stimulation 較容易取得；proximal stimulation 時常與終端 CMAP 重疊而難以辨識。
- F response 設定：supramaximal 刺激、gain 約 200 μV、sweep 5 或 10 ms、cathode 朝近端以避免理論上的 anodal block、刺激頻率 ≤ 0.5 Hz 以避免前一次刺激的影響與疼痛累加。
- 至少需取得 10 個 F responses（最好 rastered），因為每次 F response 都不同，且 normative values 也建立在至少 10 次刺激上。
- F response 測值包含 minimal latency、chronodispersion（max 減 min latency）與 persistence（每幾次刺激產生幾次 F response）。
- Normal F-wave persistence 介於 80%–100%，至少 > 50%；唯一例外是 peroneal F responses，正常人也可能 absent / impersistent。
- 在 sleeping / sedated 病人，F response 可能 absent / impersistent，這在此情境下不必然代表病理。
- Normal chronodispersion 上限：上肢約 4 ms、下肢約 6 ms。
- Minimal F latency 是最可靠的測值；chronodispersion 與 persistence 的 side-to-side 差異偶爾有用。
- Jendrassik (reinforcement) maneuver 可在 F response 不可得時 prime anterior horn cells；但若不必要時做 Jendrassik，可能反而抑制 F response 產生，因為 over-primed motor neuron 在 antidromic backfire 折返時可能仍處 refractory。
- F response 走完整條神經，因此 distal slowing（例如 median neuropathy at wrist）會延長 F response，全身性 conduction slowing（polyneuropathy）也會延長 F response。
- F estimate 公式：F estimate = (2D/CV) × 10 + 1 ms + DL，其中 D 是刺激點到 spinal cord 的距離（cm），CV 是 motor conduction velocity（m/s），DL 是 distal motor latency（ms），10 是 cm 與 m/s 換算為 ms 的係數，1 ms 是實驗所得 anterior horn cell turnaround 時間。
- D 的表面近似：peroneal / tibial 用 xiphoid process 到 ankle 刺激點；median / ulnar 用 C7 spinous process 到 wrist 刺激點。
- 測得的 minimal F latency 通常稍短於 F estimate，因為近端神經因 fiber diameter 較大、temperature 較高，conduction velocity 略快於遠端。
- 若測得 minimal F latency 大於 F estimate，代表近端 segment 的延遲超出 distal latency / CV / 肢長可解釋的範圍。
- 當 distal CMAP amplitude 嚴重下降時，因 F response 僅佔 CMAP 1%–5%，F response 通常不可得或極小難辨；此時 absent F response 不代表 proximal lesion。
- 來源建議：在 absent CMAP 的 motor nerve 不要嘗試取得 F response；在 CMAP amplitude 極低時，也應對 absent F response 保持謹慎。
- F response 只能評估記錄肌肉所對應的 motor root：上肢中常記錄的 median APB / ulnar ADM 為 C8–T1 innervation，因此 F response 只對可能的 C8–T1 radiculopathy 有用；下肢 peroneal / tibial distal muscles 為 L5–S1 innervation。
- 若 radiculopathy 主要影響 sensory root fibers，F response（測 motor）會 normal。
- 小段 demyelination 在跨越整條神經的 F response 中容易被稀釋；只要部分 fastest fibers 仍 normal 就可保留 normal minimal F latency。
- 每塊肌肉至少由兩個（常為三個）myotome 共同支配，因此即使單一 root 嚴重受影響，未受累 myotome 仍可導出 normal F response。
- Mauricio et al. (2014) 顯示 tibial F response 在 EMG-confirmed S1 radiculopathy 的 prolonged 比例僅約 4%；加上 F estimate 也只到約 8%。
- F response 的最大臨床價值：辨識早期 polyradiculopathy（例如 Guillain-Barré syndrome 的 proximal demyelination）、作為 entrapment neuropathy 的 internal control，以及 polyneuropathy 的型態描述。

#### Mechanism Chain

```text
Distal supramaximal motor stimulation
→ orthodromic motor volley → M response (CMAP)
→ antidromic motor volley 沿 axon 上行
→ 小部分 anterior horn cells backfire（約 1 ms turnaround）
→ orthodromic action potentials 沿 axon 下行越過刺激點
→ 約 1%–5% CMAP 大小的 late motor potential = F response
→ 每次刺激活化的 motor neuron 群不同
→ 至少 10 次 rastered stimulations 取 minimal latency / chronodispersion / persistence
```

#### Inferences

- F response 走整條 motor pathway，因此 prolonged F latency 不能特異定位 lesion site，也無法分辨 proximal neuropathy、plexopathy 與 radiculopathy；需要結合 distal NCS、F estimate、side-to-side comparison 與臨床。
- Normal F response 對排除 radiculopathy 的能力很弱：partial myotome 受累、sensory-predominant lesion、segmental demyelination 稀釋與 dual-root muscle innervation 都可保留 normal fastest fiber conduction。
- 報告寫成「prolonged F = radiculopathy」或「normal F = no radiculopathy」都超出此測試所能支持的範圍。

#### Assumptions

- 刺激真的 supramaximal、distal CMAP amplitude 足以期待可測 F response、病人未過度 sedated、刺激頻率夠慢以避免前次刺激干擾。
- 表面測量點（C7 spinous process、xiphoid process）與真實 cord-to-stim 距離有合理近似關係。
- Limb temperature、技術設定與 normative values 都符合 lab 標準。

#### Uncertainties / Limitations

- F response 對病灶位置與疾病的 specificity 都不高。
- F response 對 radiculopathy 本身敏感度低（Mauricio et al. 顯示 S1 radiculopathy 約 4%；加 F estimate 約 8%）。
- Peroneal F response 在正常人也可能 absent / impersistent。
- Sleeping / sedated 病人可能在無病理下也失去 F response。

### Concept: H reflex

#### One-Sentence Definition

H reflex 是用 1 ms 長 duration、submaximal 電刺激選擇性活化 Ia muscle-spindle afferent，經單突觸活化 alpha motor neurons，再由 motor efferent 回到肌肉產生的晚期 motor potential；2 歲以上成人在 routine 條件下只能從 tibial nerve / soleus 穩定取得，是 S1 ankle jerk 的電生理對應物。

#### Known Facts

- H reflex 於 1918 年由 Paul Hoffmann 首次描述。
- H reflex 與 F response 的核心差異：H reflex 有 sensory afferent（Ia muscle spindle）、突觸與 motor efferent。
- 新生兒的 H reflex 可在多條 motor nerve 廣泛取得；超過 2 歲後在 routine 條件下，只能從 popliteal fossa 刺激 tibial nerve、recording soleus 取得。
- 也可從 femoral nerve（記錄 quadriceps）或 median nerve（記錄 flexor carpi radialis）誘發 H reflex，但技術限制大。
- 選擇性活化 Ia 需要使用 1 ms 長 duration 的 submaximal stimulus。
- H reflex 設定：gain 200–500 μV、sweep 10 ms、stimulus duration 1 ms、G1 over soleus（離 gastrocnemius 兩腹會合處 distal 約 2–3 fingerbreadths）、G2 over Achilles tendon、刺激頻率 ≤ 0.5 Hz。
- 最佳 G1 位置：popliteal fossa 至 medial malleolus（內踝後方）連線分八等分中的第 5 或 6 段。
- Cathode 放在近端；刺激由很低強度開始。
- 典型 H reflex 在 ~25–34 ms latency 出現、為 triphasic、肌肉靜息下記錄；latency marker 通常放在 H wave 由 baseline 偏離的第一個正向（向下）轉折。
- 若 H reflex 不可得，可請病人輕度踝關節 plantarflexion 或使用 Jendrassik maneuver 來 prime。
- 隨刺激強度上升：H reflex 增大且 latency 縮短；強度再上升會出現 M response 並逐漸增大，而 H reflex 因近端 antidromic motor volley 的 collision 而縮小。
- 在 supramaximal stimulation 時，H reflex 消失，常被 F response 取代，M response 達最大。
- Normal H reflex latency 上限約 ≤ 34 ms，需依 leg-length / age（或 height）nomogram 校正；同距離下，side-to-side 差 > 1.5 ms 視為顯著。
- H/M ratio = peak-to-peak 最大 H amplitude ÷ peak-to-peak 最大 M amplitude；正常 ≤ 50%。
- H reflex 是 S1 ankle reflex 的電生理對應物：若 ankle reflex 存在，H reflex 應該存在。
- 若 ankle reflex 消失，H reflex 在某些情況仍可能存在。
- 任何會降低 ankle reflex 的 lesion 都可能延長或消失 H reflex，包括 polyneuropathy、proximal tibial neuropathy、sciatic neuropathy、lumbosacral plexopathy 與 S1 nerve root lesion。
- 老年人雙側 absent H reflex 不必然病理，與年長者常見的 absent ankle reflex 一致。
- H/M ratio 增加是 anterior horn cell excitability 升高的粗略指標（例如 upper motor neuron lesion）；adult 在 soleus 以外肌肉測到 H reflex 應提示中樞性 disorder。

#### Mechanism Chain

```text
Submaximal long-duration (1 ms) tibial nerve stimulus in popliteal fossa
→ 選擇性活化 Ia muscle-spindle afferent
→ orthodromic Ia volley 上行至 spinal cord
→ alpha motor neuron 單突觸 excitation
→ orthodromic motor volley 沿 tibial nerve 下行
→ soleus depolarization → H reflex
→ 刺激強度上升加入 M response 與近端 antidromic motor collision
→ supramaximal stimulus 使 H reflex 被 F response 取代
```

#### Inferences

- 延遲或消失的 H reflex 對「整條 S1 sensory-motor arc 的完整性」敏感，而非特異於 S1 root pathology；陽性 finding 必須結合其餘 EDX 與臨床才能定位。
- 對單側 lesion，把症狀側與無症狀側比較，比 absolute reference 更有用，前提是 stim–record 距離一致。
- 在 adult 從 soleus 以外肌肉常規記錄到 H reflex，應視為「考慮中樞性興奮性改變」的線索，而不是描述為 normal variant。

#### Assumptions

- 刺激脈寬真的是 1 ms 且強度維持 submaximal；否則選擇性 Ia activation 會失敗。
- 比較兩側時 stim–record 距離保持一致。
- 病人 temperature、normative tables 與 electrode placement 與 lab 標準相符。

#### Uncertainties / Limitations

- 在 adult，H reflex 在 routine 條件下只能測 tibial-soleus；無法 screen 所有 motor segments。
- 老年人 absent ankle reflex / H reflex 本身不代表疾病。
- H reflex 定位差：polyneuropathy、proximal tibial neuropathy、sciatic neuropathy、lumbosacral plexopathy 與 S1 radiculopathy 都可造成延長或消失。

### Concept: Axon reflex (A wave)

#### One-Sentence Definition

Axon reflex（A wave）是在 reinnervated 或 demyelinated 神經中，antidromic 行程經過 collateral branching point 折返、orthodromically 回到肌肉產生的小型晚期 motor potential；它以「每次刺激 latency 與 configuration 完全一致」與每次都會略有變動的 F response 區分，是 reinnervation 或（較少見的）急性 demyelination 的 marker，並非真正的 reflex。

#### Known Facts

- 「Axon reflex」名稱不是嚴格意義上的 reflex；它沒有突觸、也沒有 sensory afferent。
- 在 rastered trace 上，A wave 通常出現在 M response 與 F response 之間，且每次刺激能完美 superimpose（latency / configuration 不變）。
- 相對地，F response 每次刺激 latency 與 configuration 都略變，無法完美 superimpose。
- 在大多數要研究的神經中，axon 通常在很靠近肌肉處才分支，且分支點位於 distal 刺激點以遠。
- Reinnervated 神經中，collateral sprouting 可在 distal 刺激點以近形成新的分支點。
- 在 reinnervated 神經施以 submaximal stimulation 時，antidromic action potential 可越過近端的 branching point，然後 orthodromically 沿分支下行到肌肉，產生 A wave。
- Supramaximal stimulation 下，分支內的 antidromic volley 通常會與 orthodromic A wave 互相 collision，使 A wave 消失。
- A wave 通常出現在 M response 之後、F response 之前，因為其行進路徑短於 F response 的 circuit；在極少數情況下，若 collateral fiber 傳導極慢，A wave 可出現在 F response 之後。
- A wave 主要與 axonal-loss 後 reinnervation 相關，但也可見於 demyelinating neuropathy；最經典是 Guillain-Barré syndrome 病程前幾日。
- 早期 GBS 中 A wave 的成因仍有爭議；本來源推測可能源自發炎與 demyelination 處的 ephaptic spread（相鄰纖維間直接電性擴散）。
- A wave 也可能反映 distal stimulation 並未真正 supramaximal。

#### Mechanism Chain

```text
Distal nerve stimulation（常為 submaximal 或 reinnervated 神經）
→ antidromic volley 上行 axon
→ 抵達近端 collateral branching point
   （此分支結構通常於 collateral sprouting / reinnervation 後形成）
→ action potential 進入分支纖維
→ orthodromically 下行越過原刺激點到肌肉
→ 產生 latency / configuration 穩定的小型 late motor potential = A wave
→ supramaximal stimulation 通常透過分支內 antidromic collision 消除 A wave
```

### Demyelination 變體

```text
發炎 / demyelination 處（例如 early GBS）
→ 鄰近纖維間 ephaptic spread（推測機制）
→ trace 上 latency 穩定的晚期 potential 與 collateral-sprout A wave 難以區分
→ 在 EDX 上仍歸為 A wave
```

#### Inferences

- 「在 rastered traces 上 latency / configuration 穩定」是把 A wave 與變動的 F response 區分的實務關鍵。
- 在慢性 axonal neuropathy 中，A wave 可作為 reinnervation 的一個訊號；在早期 GBS 中是多項支持線索之一，但都不能用於定位。
- 在原本沒有 A wave 的 nerve 上突然出現新的 A wave，常是「distal stimulation 並非真正 supramaximal」的品質警訊，而非新的病理發現。

#### Assumptions

- 取得足夠的 supramaximal stimulation 與 rastered acquisition，足以比較多次刺激間 latency / configuration 是否穩定。
- 解讀者能在進入臨床判讀前先正確區分 M response、A wave 與 F response。

#### Uncertainties / Limitations

- 早期 GBS 中 A wave 的具體機制（ephaptic spread）為來源推測，未獲確認。
- 來源未提供 A wave 對 reinnervation / demyelination 的 yield、sensitivity、specificity 等量化數據。
- 「supramaximal 後仍持續存在的 A wave」應優先解讀為 demyelination、reinnervation 或刺激不足，需依整體 EDX context 判斷，無單一規則。

## Clinically Useful Points

- 當 routine distal NCS normal 但 late response 異常時，應考慮 proximal lesion，這是 late response 最有價值的場景。
- F response 在 routine motor NCS 仍 normal 時即出現 prolonged / absent，可協助辨識早期 polyradiculopathy（例如 GBS 的 proximal demyelination）。
- F response 對 radiculopathy 與 plexopathy 本身敏感度低；報告應避免「prolonged F = radiculopathy」或「normal F = no radiculopathy」此類定位主張。
- F estimate 校正 distal latency、conduction velocity 與 limb length；對高個子、distal slowing 或 borderline F latency 比 raw F latency 更有意義。
- 若 ankle reflex 存在，H reflex 應該存在；若 ankle jerk 消失，absent H reflex 可見於 polyneuropathy、tibial / sciatic neuropathy、lumbosacral plexopathy 或 S1 radiculopathy。
- 老年人雙側 absent H reflex 常為正常老化變異；不可單獨用此 finding 診斷 radiculopathy。
- 在 routine F response trace 中出現 A wave，表示 reinnervation、demyelination 或 distal stimulation 不夠 supramaximal；以「multiple stimulations 下 latency / configuration 完全一致」為實務辨識點。

## Research-Useful Points

- Late response 透過間接 circuit 把 NCS 延伸到 proximal segment；其測量假設（supramaximal、慢速刺激、≥ 10 次刺激、距離近似、normative nomogram）會限制 late response 數據在跨 lab 整合時的可比較性。
- Mauricio et al. 對 EMG-confirmed S1 radiculopathy 的 yield（tibial F ≈ 4%、加 F estimate ≈ 8%）可作為 radiculopathy testing meta-analysis 或 quality-improvement project 的 sensitivity benchmark。
- A wave 可在 axonal recovery 的長期追蹤中作為 reinnervation 進行的 marker，並在 GBS 早期作為一個電生理線索。

## Conflicts With Existing Knowledge

- 與「prolonged F response = radiculopathy」衝突。
- 與「normal F response 排除 radiculopathy」衝突。
- 與「absent H reflex = S1 radiculopathy」衝突。
- 與「雙側 absent H reflex 一定異常」衝突。
- 與「M response 之後任何 stable 晚期 potential 都是 F response」衝突。
- 與「H reflex 只測 proximal nerve」衝突。

## Pages That Should Be Created or Updated

- Created: [[09_NCV EMG 周邊神經病變/F_Response_F_Estimate判讀]]
- Created: [[09_NCV EMG 周邊神經病變/H_Reflex_臨床用途與限制]]
- Created: [[09_NCV EMG 周邊神經病變/A_Wave_Axon_Reflex判讀]]
- Updated: [[09_NCV EMG 周邊神經病變/NCV_EMG_周邊神經病變總覽]]
- Updated: [[09_NCV EMG 周邊神經病變/電生理診斷醫學]]
- Updated: [[09_NCV EMG 周邊神經病變/EDX_定位導向檢查流程]]
- Updated: [[09_NCV EMG 周邊神經病變/NCS_軸突損失與脫髓鞘判讀]]
- Updated: [[09_NCV EMG 周邊神經病變/Lower_Extremity_NCS_常規技術與陷阱]]
- Updated: [[09_NCV EMG 周邊神經病變/Upper_Extremity_NCS_常規技術與陷阱]]

## Suggested Tags

- EDX
- NCS
- late_responses
- F_response
- F_estimate
- H_reflex
- axon_reflex
- A_wave
- proximal_segment
- GBS
- S1_radiculopathy
- reinnervation
