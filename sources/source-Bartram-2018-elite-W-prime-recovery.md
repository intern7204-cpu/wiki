---
type: source
tags: [exercise-physiology, critical-power, W-prime, recovery, modelling, elite-athletes]
created: 2026-06-11
---

# 來源：Accuracy of W′ Recovery Kinetics in High Performance Cyclists – Modelling Intermittent Work Capacity

## 出處
- 作者：Jason C. Bartram, Dominic Thewlis, David T. Martin, Kevin I. Norton
- 期刊：*International Journal of Sports Physiology and Performance*（IJSPP）
- 接受日期：2017-09-27；正式刊出 2018（13(6):724–728）
- DOI：10.1123/ijspp.2017-0034
- 原始檔：`C:\原始資料\Accuracy of W' Recovery Kinetics in High Performance Cyclists\`（接受版手稿，未經出版社排版）
- 隸屬：University of South Australia（ARENA）／Cycling Australia 高效能單位／Australian Institute of Sport

## 核心主張
現行的 SKIBA 2（[[Differential W prime balance model|W′BAL·ODE 微分版]]）回填時間常數，是在次菁英族群上校的，**用在菁英車手身上會系統性低估他們的 W′ 回填速率**；應改用本研究的菁英版冪函數 τ_W′＝2287.2·D_CP^(−0.688)，並最終走向個人化的 τ。

## 本份新增／更新的概念
- [[Bartram tau for W prime reconstitution]]（**新增**）：本份的主角概念頁——SKIBA 2 框架內的菁英 τ 重標定。內容：四位世界級車手、五檔恢復強度（D_CP 0/50/100/150/200 W）的間歇到力竭；以 D_CP 0 檔定義 **W′TRAINING**（訓練情境下可表達的 W′，平均 6.2 kJ）取代「力竭＝W′=0」；用 solver 反推 modified τ；結果 modified τ 對 SK2 τ 負偏差 112±46 s（p=0.0001）、未改 ODE 預測 W′ 平均低 3540 J；菁英 τ–D_CP 冪函數 R²=0.433；機制臆測（EPOC、絕對 CP、個人化）。
- [[Differential W prime balance model]]（更新）：補上「BAR＝對菁英重標定的 SK2 τ」這層；Bartram 證 ODE 公式對菁英低估回填。
- [[W prime reconstitution]]（更新）：補上「回填速率還受訓練狀態左右——同一 D_CP 下菁英補得比次菁英快」（推導與易誤解各一條）。
- [[W prime balance model]]（更新）：把先前只間接出現的 BAR τ 公式接上其**原始來源**；強化「固定-τ 公式（SK1/SK2/BAR）誤差方向隨族群翻轉」的論述。
- [[Oxidative reserve]]（更新）：補上反例——「絕對 D_CP 相同 ≠ 絕對氧化儲備相同到足以拉平回填」；matched D_CP 不足以 normalise 不同體能者的回填速率。

## 與既有知識的關係
**一致／補強，無實質矛盾。** 本份把 wiki 裡長期被間接引用、卻沒有來源頁的「BAR（Bartram τ）」補齊源頭：

- 與 [[Differential W prime balance model|ODE]]、[[Integral W prime balance model|INT]] 一致——BAR 不是新模型，是 ODE 框架內換一條 τ 公式（論文 Table 1 並列 SKIBA 1 積分式與 SKIBA 2 微分式原型）。
- 與 [[source-Sreedhara-2020-recovery-W-prime-domain|Sreedhara 2020]] 形成關鍵對照：Bartram（菁英＋完全榨乾）看到 SK2/BAR **低估**回填；Sreedhara（業餘＋半力竭）看到 SK2/BAR **高估**回填。兩者合起來證明「固定-τ 公式的誤差方向隨族群與消耗型態翻轉」——強化「sub-CP 恢復需個別化模型」的結論（已寫入 [[W prime balance model]] 推導第 13 點與易誤解 #7）。
- 與 [[source-Lievens-2024-partial-depletion|Lievens 2024]] 一致：Lievens 把 Skiba-1/Skiba-2/**Bartram** 三個固定-τ 模型一起檢驗，發現部分消耗後三者皆低估——本份正是 Bartram 模型的出處。
- 與 [[Oxidative reserve|氧化儲備]] 框架形成有意義的張力（非矛盾）：Skiba 用「matched D_CP＝matched 氧化儲備」當作以 D_CP normalise 的理由；Bartram 數據顯示這個 normalise **不完全**——同 D_CP 下菁英仍補得更快，提示氧化儲備之外還有訓練相關因素（EPOC 等）。
