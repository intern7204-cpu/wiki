---
type: source
tags: [exercise-physiology, critical-power, W-prime, reconstitution, intermittent, pacing-optimization]
created: 2026-06-11
---

# 來源：Modeling the Recovery of W′ in the Moderate to Heavy Exercise Intensity Domain

## 出處
Sreedhara VSM, Ashtiani F, Mocko GM, Vahidi A, Hutchison RE. *Medicine & Science in Sports & Exercise* 2020;52(12):2646–2654. DOI: 10.1249/MSS.0000000000002425.
（Clemson University 機械工程 ＋ Furman University 健康科學；原始檔：`C:\原始資料\Modeling the Recovery of W' in the Moderate to Heavy Exercise Intensity Domain\`）

## 核心主張
在 CP 以下的恢復裡，**恢復功率（P_rec）比恢復時長（t_rec）更左右 W′ 補多少**；且既有的固定-τ 模型（SK2＝Skiba 雙條件式、BAR＝Bartram 修正）在「半力竭消耗 ＋ 競技業餘車手」這組條件下**高估**了實測 W′ 餘量——這與 elite 受試者上常見的「低估」方向相反，凸顯回填模型需依個人/族群與消耗型態個別化；並示範用個人化 CP/W′ 回填模型 ＋ 最佳控制做即時配速最佳化，把 18 km 計時賽縮短 55 s。

## 研究設計（一眼看懂）
- 7 名競技業餘車手（4 男 3 女，V̇O₂peak 平均 51.9 mL/kg/min）。各做：斜坡測試（定 V̇O₂peak、GET、P_GET）、2–4 次 [[3-minute all-out test|3MT]] 定 CP/W′、9 次間歇測試。
- 間歇測試＝**全因子 3×3 設計**：先一段 **2 分 @CP4**（CP4＝預計 4 分力竭的功率，設計成耗掉約 **50% W′**＝**半力竭**，非完全榨乾）→ 一段恢復（P_rec：低 L≈20 W、中 M＝0.9 P_GET、高 H＝P_GET+0.5(CP−P_GET)；t_rec：2/6/15 min）→ 一段 **3 分全力**。
- W′ 回填量 E_rec ＝（A₁＋A₃−W′）/W′，A₁/A₃＝前/後兩段超 CP 的功（圖 1）。
- 另有 1 名受試者做「自選配速 vs 最佳配速」18 km 計時賽對照（最佳控制＋動態規劃求每 100 m 目標功率）。

## 本份新增／更新的概念
- [[Critical power pacing optimization]]（**新增**）——以個人化 CP/W′/回填模型＋最佳控制／動態規劃，算出最小化完成時間的逐段功率配置；本研究實證 vs 自選配速省 55 s。
- [[W prime reconstitution]]（**更新**）——新增「**恢復功率 > 恢復時長**」（P_rec 有顯著主效應、t_rec 無）、半力竭消耗下回填在 2–15 min 內**未必呈指數**、以及消耗型態（半力竭 vs 完全力竭）會改變回填輪廓。
- [[W prime balance model]]（**更新**）——新增「SK2、BAR 在半力竭＋業餘車手下**高估** A₃」與 elite 上「低估」**方向相反**的對照；強化「誤差方向取決於族群與消耗型態、需 sub-CP 個別化模型」。
- [[Power-duration relationship plasticity]]（**更新**）——新增 CP 的**個體內變異**（intra/inter-trial；0.9 CP 的「恢復」竟在淨耗 W′）與「先前**重度**（非全力）運動可**抬高** CP/W′」（Miura 2009、priming）——與 Black 2023「全力運動**壓低** CP」互補、方向相反。

## 與既有知識的關係
- **補充**：把 W′ 回填的決定因子從「恢復端的 D_CP＋時長」「工作端的消耗速率（Caen 2019）／時間結構（Skiba 2014）」再擴一筆——**在 sub-CP 恢復裡，強度（P_rec）的影響大於時長（t_rec）**，且把回填研究從「完全力竭後」延伸到「半力竭後」。
- **矛盾（已在相關頁「易誤解之處」標出）**：本研究說 SK2/BAR **高估**回填；而 [[source-Caen-2019-work-recovery-reconstitution]]、[[source-Lievens-2024-partial-depletion]]、Bartram 2018 在各自條件下說這類模型**低估**回填。兩邊都對——方向取決於**受試族群（業餘 vs 菁英）＋消耗型態（半力竭 vs 完全力竭）＋設備**，這正是「需要個人化、可變 τ」的最強論據。另本研究 t_rec **無**顯著主效應，與 Caen 2019、Ferguson 2010「時長愈長補愈多」相左（作者歸因於半力竭的 CP4 起點與 CompuTrainer 設備）。
- **一致**：CP/W′ 並非固定常數（呼應 [[Power-duration relationship plasticity]]）；回填需個人化參數（呼應 Bartram 2018、Caen 2019、Skiba 2014/2015）。

## 關鍵數字
- E_rec（W′ 回填％，表 2）：t_rec=2 min 時 L 33.7%／M 19.0%／H 3.3%；6 min 時 L 40.6%／M 31.5%／H 6.5%；15 min 時 L 39.0%／M 19.2%／H **−15.5%**（高功率恢復反而淨耗 W′）。P_rec×t_rec 交互 P=0.004（η²=0.52）；P_rec 在每個 t_rec 都顯著、t_rec 在每個 P_rec 都不顯著。
- 模型偏差：A₃ 顯著小於 W′_SK2（P=0.035）與 W′_BAR（P=0.015）；平均預測誤差 A₃−SK2 = −1.31±1.84 kJ、A₃−BAR = −1.60±1.97 kJ（負＝模型估得比實測高＝高估）。
- 模型 τ 式：SK2 τ=W′₀/D_CP；BAR τ=2287.2·D_CP^(−0.688)；SK1（eq.2）τ_W′=546·e^(−0.01·D_CP)+316。
- 最佳化（表 3，1 名受試者，18 km）：自選 34:08 → 最佳 33:13（**−55 s**）；最佳策略全程在 CP 上下振盪、W′bal 到終點被花到約 0；自選策略約 5 km 後落在 CP 以下、終點 W′bal 補回滿（剩一桶沒用完）。
- CP 變異：subject 7 四次 3MT 的 CP 由 295→327 W 單調上升（被排除分析）；subject 3、5 的疲勞態 CP_ft 顯著高於新鮮態 CP_fr（prior heavy exercise 像額外暖身）。

## 限制
- 樣本小（n=7，最佳化僅 n=1）；P_rec-L 目標 20 W 因滾阻校準無法達成，實際 75–90 W。P_GET 估在 0.81 CP（偏高，可能 V̇O₂ mean response time 未校），使 H 端逼近/超過真實 CP→部分「恢復」其實在 CP 之上。CompuTrainer 與 Lode 功率/TTE 有差。最佳化僅假設回填只依 P_rec、未計空氣阻力與下坡滑行、測試間隔 >4 週。
