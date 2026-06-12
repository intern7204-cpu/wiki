---
type: source
tags: [exercise-physiology, critical-power, W-prime, 31P-MRS, fatigue, recovery]
created: 2026-06-12
---

# 來源：力竭後恢復強度（<CP vs >CP）決定肌內代謝與耐受——以 ³¹P-MRS 檢驗

## 出處
- Chidnok, W., Fulford, J., Bailey, S. J., DiMenna, F. J., Skiba, P. F., Vanhatalo, A., & Jones, A. M. (2013). *Muscle metabolic determinants of exercise tolerance following exhaustion: relationship to the "critical power".* **Journal of Applied Physiology** 115(2): 243–250. First published 2 May 2013. doi:10.1152/japplphysiol.00334.2013.
- 原始檔：`C:\原始資料\Muscle metabolic determinants of exercise tolerance following exhaustion relationship to the\`
- 機構：University of Exeter（含 Peninsula MRS Research Unit）、Adelphi University、Columbia University。
- 注意：與本 wiki 已 ingest 的 **Chidnok 2013（間歇 ³¹P-MRS）** 是**不同論文**——那篇是 *Am J Physiol Regul Integr Comp Physiol* 305:R1085（間歇 60 s 衝刺夾 18/30/48 s 被動休息）；本篇是 *J Appl Physiol* 115:243（單次力竭後接 <CP / >CP / 被動恢復）。兩篇同團隊、同年、互補。

## 核心主張
力竭後要不要能「恢復並續動」，取決於恢復時的運動強度落在 [[Critical power|CP]] 的**哪一側**：降到 **CP 以下**，肌肉內 [[Phosphocreatine|PCr]]、pH、[[Inorganic phosphate|Pi]]、ADP 會迅速回補、可再撐至少 10 分鐘；維持在 **CP 以上**（即使降 19% 功率），這些代謝物**完全不回補**、只能再撐約 39 秒。CP 因此是一條**肌內代謝閾值**，決定疲勞代謝物累積與高強度運動耐受。

## 實驗設計（一句話看懂）
8 名男性，單腿伸膝運動。先以四趟定功率力竭估出個人 CP（17±4 W）與 W′（~1.52 kJ）。再進磁振掃描儀，用 ³¹P-MRS 即時量肌內代謝物：以 P₃（26±3 W ≈ 153% CP，預計 3 分力竭）踩到力竭（~180 s），**緊接著**隨機分配三種「恢復」之一——被動休息、<CP（13±5 W，heavy 域）、>CP（21±4 W，severe 域、比 P₃ 低 19%），續做 10 分鐘或到力竭。

## 關鍵數據
- **耐受時間**：<CP 與被動恢復皆完成 10 分鐘；>CP 恢復只再撐 **39±31 s**（顯著短）。
- **力竭終點一致**：三條件在初次力竭點的 [PCr]（~38–40% 基線）、pH（~6.7）、[Pi]（~524–586%）、[ADP] 皆無顯著差異 → 印證 [[Metabolic milieu at task failure|力竭時的代謝終點固定]]。W>CP（1.44–1.55 kJ）三條件間無差、且與 W′（1.52 kJ）無差。
- **恢復端的分歧**（恢復 10 分後）：
  - **PCr**：被動回到 96%、<CP 回到 76%、>CP **停在 37%**（幾乎沒動）。
  - **pH**：被動/<CP 回到 7.0；>CP 停在 6.6（＝力竭值）。
  - **Pi**：被動回到 68%、<CP 回到 178%；>CP 停在 545%（＝力竭值）。
  - **ADP**：被動回到 9、<CP 回到 23；>CP 停在 51 μM（＝力竭值）。
- **「力竭後降速還能再擠一段」**：>CP 那 39 s 多做了 0.17±0.18 kJ 的 [[Work done above critical power|W>CP]]，顯著大於 W′ 的 SEE（0.15 kJ）與理論殘留（0.04 kJ），且與初次 t_lim 變異不相關 → 力竭時 W′ 非字面歸零。

## 本份新增／更新的概念
- [[W prime expenditure is rate-limited]]（**新增**）：本份的獨特理論貢獻——古典「W′ not rate-limited」應重新考慮；W′ 最大消耗速率隨剩餘量遞減、W′ 帶協定依賴。
- [[W prime reconstitution]]（**更新**）：補上「>CP 恢復肌內代謝物**完全不回補**、<CP 才回補 PCr/pH/Pi/ADP」的**直接 ³¹P-MRS 證據**——強化「回填只在 CP 以下」由原本多靠全身、間接（Chorley/Caen）升級為單關節直接肌內量測。
- [[Critical power]]（**更新**）：CP 作為**肌內代謝閾值**再添「恢復向」證據——CP 之下不只能穩態、力竭後還能**逆轉回補**代謝物；CP 之上連降速也回補不了。
- [[W prime]]（**更新**）：「桶子大小不隨燒多快而變」需補一句但書——消耗**速率**有上限且隨剩餘量遞減（連到 [[W prime expenditure is rate-limited]]）。
- [[Metabolic milieu at task failure]]（**更新**）：把「力竭終點固定」由定功率/間歇再添一筆——三種恢復條件的初次力竭代謝終點一致。

## 與既有知識的關係
- **一致／強化**：與 Coats 2003（力竭後降至 80% GET / 90% CP / 110% CP，僅 <CP 能續 20 分）、Chidnok 2012（間歇 CP 模型）、Jones 2008（>CP 惡化 / <CP 穩定的 ³¹P-MRS）、Vanhatalo 2010、Skiba 2012/2015 完全一致；是「intensity-dependent W′ recovery」的肌內機制證據。
- **互補**：與已 ingest 的 Chidnok 2013 間歇篇互補——間歇篇證「回填隨被動休息時長階梯式增大」，本篇證「回填的**強度門檻**就是 CP，且 >CP 連降速也不回補」。
- **修正張力**：本篇對 [[W prime|W′]]「不受速率限制的固定一桶」古典定義提出修正（見新頁 [[W prime expenditure is rate-limited]]），但不推翻 W′ 固定性的主用途——協定依賴的差距僅約一成。
- **證據強度警示**：n=8、單腿伸膝小肌群（結論在局部運動最乾淨，全身運動可能因 [[Sensory tolerance limit|感覺耐受極限]] 提前停而不同）、1.5 T、CP/W′ 由四趟定功率估得（帶估計誤差）。
