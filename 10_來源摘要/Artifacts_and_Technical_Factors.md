---
title: Artifacts and Technical Factors
created: 2026-05-10
updated: 2026-05-11
type: source_summary
domain: [PMR, methodology, electrodiagnosis]
tags: [EDX, NCS, EMG, artifact, technical_factors, temperature, supramaximal_stimulation, co_stimulation, electrode_placement]
source_path: 'C:\原始資料\Artifacts and Technical Factors\Artifacts and Technical Factors.md'
source_tier: 1
evidence_level: textbook_chapter
confidence: high
contested: true
contradictions:
  - 技術上不準確的資料無法靠後續判讀補救。
  - 低 amplitude、慢速、延長 latency 或 proximal amplitude drop 可能是 technical artifact，而非真正的 neuropathy。
---

# Source Summary: Artifacts and Technical Factors

## Source Type

- 電生理診斷 textbook chapter；內容涵蓋 NCS / needle EMG 的 artifact 與 technical factors。
- 本輪僅以這篇單一來源 ingest，未混入 anomalous innervation、routine nerve-specific protocol 或 disease-specific EDX criteria 等其他章節。

## Reliability Level

- 在本 wiki 對 textbook clinical chapter 的層級中屬 Tier 1。
- 強項：technical validity、artifact 辨識、temperature 校正、刺激 / 記錄 setup，以及 false-positive / false-negative 的預防。
- 限制：本來源不是 disease-specific guideline；abnormal 型態仍須與臨床—電生理 correlation 一起判讀。

## One-Sentence Summary

EDX 判讀的可信度只取決於資料品質：temperature、age、height、impedance、filter、刺激充足性、co-stimulation、electrode placement、距離測量與顯示設定，任一都能製造假性的 neuropathy、entrapment、axonal loss、demyelination 或 conduction block。

## Core Concepts Extracted

### Concept: EDX 技術假象與品質控制

#### One-Sentence Definition

EDX technical quality control 是有系統地辨識與校正會扭曲 NCS / EMG 波形的生理與非生理因素，再賦予生理性診斷。

#### Known Facts

- EDX 的價值取決於正確收集與正確判讀資料。
- 若資料技術上不準確，後續判讀無法補救。
- EDX 訊號是微伏到毫伏級的小型生物電訊號。
- 不辨識技術因素會造成 type I error 與 type II error；本章特別強調 type I error 的危害，因為會把正常人標為異常並引發不必要檢查或治療。
- 來源列出的「生理因素」包括 temperature、age、height、proximal vs distal nerve segment 與 anomalous innervation。
- 「非生理因素」包括 electrode impedance mismatch / 60-Hz 干擾、filter、averaging、stimulus artifact、cathode 位置、supramaximal stimulation、co-stimulation、electrode placement、antidromic vs orthodromic recording、recording electrode 與 nerve 的距離、active-reference 電極距離、limb position / 距離測量，以及 sweep speed / sensitivity。

#### Mechanism Chain

```text
小型 EDX 訊號
→ 生理或技術扭曲
→ latency / velocity / amplitude / duration / morphology 變化
→ 假性的 axonal loss、demyelination、entrapment、conduction block 或 normal study
→ 若未辨識並校正技術因素就會誤診
```

#### Inferences

- 技術品質不是文書細節，而是診斷推理鏈的一部分。
- 與臨床定位不吻合的 waveform pattern，應在升級診斷前先做技術 review。

#### Assumptions

- EDX lab 能量測 limb temperature、調整刺激 / 記錄 setup，並在必要時重做或調整位置。
- 操作者同時理解電生理與 volume conduction 的 artifact。

#### Uncertainties / Limitations

- 部分技術扭曲難以完全校正，特別是 portable ICU 檢查、edema、嚴重疾病或極端解剖變異情境。

### Concept: Temperature 與生理修飾因素

#### One-Sentence Definition

Temperature、age、height 與 limb segment 差異會改變 NCS / EMG 參數，必須先納入 baseline 才能下生理性的疾病判讀。

#### Known Facts

- 來源把 temperature 描述為最重要的生理因素。
- 較冷的肢體會 slow conduction velocity、prolong distal latency，並提高 CMAP / SNAP 的 amplitude / duration；SNAP 受影響更大。
- 在約 21–34°C 範圍內，每降 1°C 約 slow conduction velocity 1.5–2.5 m/s、prolong distal latency 約 0.2 ms。
- Cool limb 可模仿 polyneuropathy、distal entrapment neuropathy，或讓 axonal neuropathy 進入 demyelinating 範圍的 slowing。
- 應紀錄 distal limb temperature；理想情況維持在 32–34°C。
- 嚴重 cooling 時，即使皮溫已改變，nerve 內部 temperature 可能需要 20–40 分鐘才能 equilibrate。
- 若無法 warming，可使用 correction factor，但來源較偏好 warming / rewarming，因 correction factor 多由正常神經導出。
- 足月新生兒的 conduction velocity 約 25–30 m/s 為正常；同樣速度在 adult 則屬 demyelinating range。
- 大約 1 歲時 conduction velocity 達 adult 的 75%、3–5 歲達 adult range。
- 60 歲以上 adult 的 conduction velocity 每 10 年約下降 0.5–4.0 m/s。
- SNAP amplitude 隨高齡明顯下降；老年人下肢 distal sensory 缺失或極小者需謹慎判讀。
- 較高個子的人因 nerve 較長 / tapered，加上 distal cooling，conduction velocity 通常較慢。
- 下肢 conduction velocity 通常比上肢慢，屬正常。
- Late responses 需用 height 或 limb-length 為基礎的 normal values。

#### Mechanism Chain

```text
較冷 / 較年長 / 較高 / distal limb 情境
→ channel kinetics、myelin / axon 群、神經長度或 limb 溫度改變
→ slower velocity、longer latency、改變 amplitude / duration
→ 若用不適合的 norms 判讀，便會 mimic 疾病
```

#### Inferences

- 出現高 amplitude、長 duration 的 sensory response 加上 slow conduction velocity 時，應在診斷 demyelination 前先排除 temperature artifact。
- Pediatric 與 geriatric 判讀不能僅用 single adult normal table，無視年齡 context。

#### Assumptions

- 報告中能取得 temperature 與 age / height 的 norms，或可以明確標註與校正。

#### Uncertainties / Limitations

- Temperature correction 公式不一定適用所有病態神經。

### Concept: 刺激 / 記錄 artifact

#### One-Sentence Definition

刺激與記錄 setup 可直接製造假性 latency、amplitude、conduction velocity 與 conduction block 型態。

#### Known Facts

- Electrode impedance mismatch 可讓 60-Hz 干擾蓋過小型 SNAP 或 fibrillation potential。
- Active 與 reference 電極阻抗匹配能達到 common mode rejection。
- Filter 可降低 noise 但也改變訊號；normative values 應建立在相同 filter 設定下。
- 電子 averaging 透過降低隨機 noise 改善小型 sensory / mixed response。
- Stimulus artifact 可遮蔽 onset、扭曲 amplitude / latency；在小波形或短距離 study 中尤為明顯。
- 減少 stimulus artifact 的方法：把 ground 放在 stimulator 與 recording 之間、降低阻抗 mismatch、使用 coaxial cable、最佳化 stimulator 位置、降低刺激強度、調整 anode 角度、增加距離、分離 cable。
- 去極化從 cathode 開始；cathode 應朝向 active recording electrode。
- 反接 cathode / anode 可使 distal latency 延長約 0.3–0.4 ms、sensory conduction velocity 慢約 10 m/s，模仿 polyneuropathy 或 distal entrapment。
- Supramaximal stimulation 的標準作法：增加電流到 amplitude plateau，再加約 25%。
- 一旦 potential 進入 normal range 即停止加流是常見錯誤。
- 距離端 submaximal 刺激可 mimic axonal loss；近端 submaximal 刺激可 mimic conduction block。
- Co-stimulation 可讓低 amplitude 看起來正常、製造假 conduction block、模仿 anomalous innervation，或反過來掩蓋真正 conduction block。
- Recording electrode 與 nerve 的距離強烈影響 sensory / mixed amplitude；edema 或電極偏離 nerve 可降低或消失 sensory response。
- Active 與 reference 電極距離過短會造成 cancellation，使 sensory amplitude 下降；sensory / mixed studies 偏好 3–4 cm 距離。
- 在 elbow 伸直下測 ulnar across-elbow distance 會低估真正 nerve length，造成假性 slowing。
- 各刺激位置的 limb position 應盡量一致。
- Sweep speed 與 sensitivity 影響 onset latency 測量；同一條神經 study 內應保持一致。

#### Mechanism Chain

```text
記錄 / 刺激 setup 問題
→ 波形或測量扭曲
→ 假性 amplitude drop、latency shift、slowing、absent response 或 normal 化
→ 錯誤的 axonal loss、demyelination、entrapment、conduction block 或 normal interpretation
```

#### Inferences

- 在診斷 conduction block 前，必須先考慮 submaximal stimulation、distal 或 proximal co-stimulation、anomalous innervation、temporal dispersion 與 nerve-specific normal variant。
- 有 edema 時，下肢 sensory response 缺失的資訊量低於 preserved normal response。

#### Assumptions

- 操作者可調整 stimulator 與 electrode 位置、監看 twitch / 波形 morphology，並在標準設定下重複測量。

#### Uncertainties / Limitations

- 部分 proximal stimulation 位置必然 co-stimulate 鄰近神經；可能需特殊技術。

## Clinically Useful Points

- 一律紀錄並監控 distal limb temperature；可能時維持在 32–34°C。
- 偏好 warming / rewarming，避免單純依賴 temperature correction。
- 對 pediatric、年長、taller patient 與下肢測值，使用對應的 norms。
- 在診斷新疾病前，先把 noise、stimulus artifact、submaximal stimulation、co-stimulation 與 electrode misplacement 列入鑑別。
- Edema 下出現低或缺失的 sensory response，應在報告中明確標示為可能 technical。
- 同一神經 study 內 latency 測量應使用一致的 sensitivity 與 sweep speed。
- 懷疑 conduction block 時，先驗證 supramaximal stimulation、波形 morphology、twitch pattern、co-stimulation、distal response validity 與解剖變異。

## Research-Useful Points

- Artifact 辨識可作為診斷品質控制 intervention 來研究，常用 outcome 包含 false-positive reduction、repeat-study rate 與 clinical management change。
- Temperature 與 edema 是實務修飾因素，自動化 NCS 判讀的訓練資料中應紀錄這些變項。

## Conflicts With Existing Knowledge

- 與「NCS abnormal value 等於疾病」衝突。
- 與「low amplitude 等於 axonal loss」衝突。
- 與「proximal amplitude drop 等於 conduction block」衝突。
- 與「Normal-range amplitude 證明刺激充分」衝突。
- 與「Edema 或高齡下 absent sural response 自動代表 neuropathy」衝突。
- 與「Temperature correction 完全可取代 warming」衝突。

## Pages That Should Be Created or Updated

- Created: [[../09_NCV EMG 周邊神經病變/EDX_技術假象與品質控制]]
- Updated: [[../09_NCV EMG 周邊神經病變/電生理診斷醫學]]
- Updated: [[../09_NCV EMG 周邊神經病變/EDX_定位導向檢查流程]]
- Updated: [[../09_NCV EMG 周邊神經病變/NCS_軸突損失與脫髓鞘判讀]]

## Suggested Tags

#EDX #NCS #EMG #artifact #technical_factors #temperature #supramaximal_stimulation #co_stimulation
