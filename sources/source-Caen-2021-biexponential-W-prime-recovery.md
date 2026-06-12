---
type: source
tags: [exercise-physiology, critical-power, W-prime, recovery, modelling, VO2-kinetics, muscle-fiber-type, aerobic-fitness]
created: 2026-06-12
---

# 來源：W′ Recovery Kinetics after Exhaustion: A Two-Phase Exponential Process Influenced by Aerobic Fitness

## 出處
- Caen K, Bourgois G, Dauwe C, Blancquaert L, Vermeire K, Lievens E, Van Dorpe J, Derave W, Bourgois JG, Pringels L, Boone J. *W′ Recovery Kinetics after Exhaustion: A Two-Phase Exponential Process Influenced by Aerobic Fitness.* **Medicine & Science in Sports & Exercise** 2021; 53(9): 1911–1921. doi:10.1249/MSS.0000000000002673（投稿 2020-08、接受 2021-03）。
- Ghent University（Department of Movement and Sports Sciences）、Ghent University Hospital（Center of Sports Medicine／Pathology），Belgium。與 [[source-Caen-2019-work-recovery-reconstitution|Caen 2019]]、[[source-Lievens-2024-partial-depletion|Lievens 2024]] 同一 Ghent 團隊。
- 原始檔：`C:\原始資料\W' Recovery Kinetics after Exhaustion A Two-Phase Exponential Process Influenced by Aerobic Fitness\`（含 7 張圖檔）。
- 體例：原始實驗（21 名活動男性，腳踏車測功儀，氣體交換＋肌肉切片）。

## 核心主張
力竭後的 [[W prime reconstitution|W′ 回填]]在「30 秒～15 分鐘」這麼寬的恢復範圍上，是**雙指數（先快後慢兩段）**而非單指數；而那段「快得超乎預期」的初段，**大半不是 W′ 本身被補回來，而是第二輪運動起始時 [[VO2 kinetics|VO2 動力學]]變快、[[O2 deficit|氧虧]]變小帶來的「有氧優勢」假象**；扣掉這份有氧優勢後，剩下的真回填就接近單指數。整體回填強烈受**有氧體能（V̇O₂peak）**左右，但與**肌纖維型（MFT）分佈**沒測到顯著關聯。

## 本份新增／更新的概念
- [[Aerobic contribution to W prime recovery]]（**新增**）——本份的招牌新概念頁：用「把第二輪 WB2 的氧虧縮小量換算成額外做的機械功（W′ADJ 校正）」證明，表觀回填裡有一塊是有氧前置而非 W′ 復原；30 秒恢復時這塊佔 WB2 表現近 50%；扣掉後 [[Akaike information criterion|AICc]] 不再偏好雙指數。這正是先前 [[Priming effect|預熱效應]]頁、[[W prime reconstitution|回填]]頁多次提到「Caen 2021 的 ~11% 有氧優勢」卻無專頁、無來源的缺口。
- [[Bi-exponential W prime reconstitution model]]（更新）——本份是**完全力竭後、全身運動**雙指數回填的奠基實證（早於同樣結論的 Chorley 2022，且在非車手族群）。補上其參數（τ₁≈11 s、τ₂≈256 s、A≈74.8%、α₁≈33%；單指數 τ=104 s；[[W prime balance model|W′BAL]] τ=524 s 低估）、~70–75% 的平台、「振幅自由 vs 固定 100%」的選擇。
- [[W prime reconstitution]](更新)——新增決定因子「有氧體能」（V̇O₂peak r=0.62、CP r=0.57 與回填正相關，長恢復時差距更大）、有氧優勢造成的回填高估警示、完全 vs 部分消耗的開放問題（與 [[source-Lievens-2024-partial-depletion|Lievens 2024]] 收束）。
- [[W prime multicompartment model]](更新)——把「雙指數明顯勝單指數＝需要多隔間」的一手實證從 Skiba-Clarke 2021（二手）正式接到 Caen 2021；並坐實「採了切片卻沒去配對振幅/τ 與纖維型」這個空缺的出處。
- [[Priming effect]](更新)——把 ~11% 有氧優勢這個一手數據從二手引用升為本來源，並連到新頁 [[Aerobic contribution to W prime recovery]]。

## 與既有知識的關係
**一致／補充為主，對 [[W prime balance model|W′BAL]] 是修正。**
- 與 [[source-Chorley-2022-bi-exponential-reconstitution|Chorley 2022]] **一致且互補**：兩篇各自獨立得到「完全力竭後回填是雙指數」。差別：Chorley 用受訓**車手**、反覆 ramp、低強度（50 W）恢復、重點在「反覆力竭只拖慢慢段 τ_SC」；Caen 用**非車手**、定 PO4min 力竭、90% GET 恢復、8 個時間點、重點在「快段大半是有氧優勢假象」與「有氧體能決定回填」。Caen 投稿更早（2020-08）。
- 與 [[source-Lievens-2024-partial-depletion|Lievens 2024]]（同團隊後作）**互補不衝突**：Caen 證明**完全力竭**後雙指數；Lievens 證明**部分消耗**後單指數即足。Caen 自己在 Discussion 就預示了這點——懷疑部分消耗不會誘發同樣陡的快段，主張用「依當下 W′ 大小變動的 τ」。
- 對 [[W prime balance model|W′BAL（Skiba INT）]] 是**實證修正**：再次證明固定-τ 的 W′BAL 在短恢復（<10 min）系統性**低估**回填（呼應 [[source-Caen-2019-work-recovery-reconstitution|Caen 2019]]、[[source-Bartram-2018-elite-W-prime-recovery|Bartram 2018]]），且把低估的一大部分歸因為模型沒把「第二輪有氧前置變快」算進去。
- 對 Skiba 原始的「兩隔間≈Type I/II 兩群纖維」假說是**未能證實**：MFT 分佈不顯著預測 W′ 回填（也不顯著預測 CP/W′，唯 %Type I 與 CP 擦邊 r=0.45, p=0.053）；作者推測被 V̇O₂peak 大變異或 MFT 同質性不足遮蔽，故非否證、是「沒測到」。

## 關鍵數據
- 受試：21 名活動男性，age 25±2 y，V̇O₂peak 54.4±5.3 mL·min⁻¹·kg⁻¹，CP 269±31 W，W′ 19.2±5.1 kJ。
- 協定：WB1（PO4min，定功率騎到力竭，TTE≈228 s）→ 90% GET 主動恢復（30 s/1/2/3/4/5/10/15 min 隨機）→ WB2（同 PO4min 騎到力竭）。W′_OBS = TTE(WB2)/TTE(WB1)。
- 回填表觀值：30 s 已回 28.6%、10 min 達最高 73.7%、10→15 min 平台（無增）。
- 模型擬合 W′_OBS（振幅自由）：單指數 τ=104±22 s、RMSE 6.4%；雙指數 τ₁=11±10 s、τ₂=256±51 s、A=74.8%、α₁=33%、RMSE 1.7%；ΔAICc=+11.51（偏好雙指數）。W′BAL τ_W′=524±41 s、RMSE 18.6%（低估，<5 min 皆 P<0.002）。
- 有氧優勢（W′ADJ）：WB2 的氧虧一律小於 WB1（恢復愈長差距愈小）；換算的額外功 9.0→5.6 kJ（時間 26→16 s）；W′_OBS 平均高出 W′ADJ 11.0±1.5%；30 s 恢復時這份有氧前置佔 WB2 表現近 50%。扣正後 ΔAICc=−2.86（**不再**偏好雙指數），但 30/60 s 處單指數仍低估 4–6%（故快段非純屬假象，仍含 PCr 復原成分）。
- VO2 恢復（[PCr] 代理）整體快於 W′_OBS（除 30 s 外各點皆較高，2–3 min 內大致補完）；mean VO2 恢復與 mean W′_OBS r=0.47。
- 個體決定因子：W′_OBS 與 V̇O₂peak r=0.62（p=0.003）、與 CP r=0.57；與 PO_peak、GET、%Type I（r=0.31）、其他纖維型皆不顯著。多元迴歸 adj R²=0.53（恢復時長＋V̇O₂peak 顯著、MFT 不顯著）。CV% 個體間=26.9%。

## 侷限（作者自陳＋審稿觀點）
- W′ADJ 是**估算**（用固定 22% 機械效率與 1 L O₂=21.1 kJ 換算），實際有氧貢獻可能略偏離。
- 只測**完全力竭後**、**單一恢復強度（90% GET）**、**腳踏車全身運動**、**年輕活動男性**；部分消耗、不同恢復強度、女性、其他運動模式未涵蓋。
- MFT「不顯著」可能是 V̇O₂peak 大變異遮蔽或 MFT 同質性不足，非真正無關（散見個別時長 %Type I 與 W′_OBS r=0.46–0.58）。
- W′_OBS 以 TTE 比值估，整合了所有中樞＋周邊恢復過程，無法乾淨拆出單一機轉。
