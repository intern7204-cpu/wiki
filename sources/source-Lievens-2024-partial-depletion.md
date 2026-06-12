---
type: source
tags: [exercise-physiology, critical-power, W-prime, recovery, modelling, methodology]
created: 2026-06-11
---

# 來源：Characterizing the Exponential Profile of W′ Recovery Following Partial Depletion

## 出處
- **檔名**：`C:\原始資料\Characterizing the Exponential Profile of W' Recovery Following Partial Depletion\`（正文 .md ＋ 5 張圖 JPEG：Fig 1 回填曲線、Fig 2 兩消耗條件相關、Fig 3 代謝環境、Fig 4 有氧體能相關、Fig 5 SSE 地形圖）
- **作者**：Maarten Lievens, Michael Ghijs, Jan G. Bourgois, Kobe M. Vermeire, Gil Bourgois, Alessandro L. Colosio, Jan Boone, Kevin Caen（Ghent University／Ghent University Hospital, Belgium）
- **出處**：*Medicine & Science in Sports & Exercise*, Vol. 56, No. 9, pp. 1770–1781, 2024. DOI: 10.1249/MSS.0000000000003468
- **類型**：原始實驗研究（n＝9 健康受訓男性、自行車測功儀；先定 CP/W′，再做 10 個實驗 trial：WB1 消耗 25%/75% → 恢復 30/60/120/300/600 s @90% GET → WB2 力竭量回填）

## 核心主張
部分消耗（25%／75%）後的 W′ 回填，**沒有證據需要動用雙指數模型**——以 AICc（準度扣掉參數代價）衡量，單指數即足；既有的固定-τ 模型（Skiba-1、Skiba-2、Bartram）都**低估**回填，未來模型該改用「**可變、個人化的 τ**」（隨工作/恢復強度、消耗程度、個人有氧體能調整）。

## 本份新增／更新的概念
- [[Overfitting]]（新增）——配適誤差會隨參數增加而下降，但可能只是在背雜訊；判斷模型好壞不能只看誤差。本研究 Fig 5 的參數不可辨識是其活範例。
- [[Akaike information criterion]]（新增）——「準度減去複雜度代價」的模型選擇尺；ΔAICc 的正負號慣例；本研究主結論的判準。
- [[Priming effect]]（新增）——前一輪重運動加速次輪 VO2 動力學、降氧虧、省 W′；解釋為何 W′OBS 可超過 100%。
- [[W prime reconstitution]]（更新）——部分消耗 vs 完全力竭、部分消耗單指數即足、最初 30 秒速度與消耗程度無關（~21–23%）、大消耗回填停在 ~83%、感知恢復低估實際約 25%、代謝環境（[La⁻]/pH/[HCO₃⁻]）恢復慢於 W′。
- [[W prime balance model]]（更新）——Bartram 模型 τ 式；Skiba-1/2/Bartram 三者皆低估 W′OBS；固定 τ 跨消耗程度不適用、呼籲個人化可變 τ。
- [[W prime]]（更新）——W′ 回填量與有氧體能（VO2peak/CP/GET）正相關（r＝0.67–0.77）、與 durability 連結、小消耗回填可超 100%（預熱效應）。

## 與既有知識的關係
**一致、補充**，不與既有頁面矛盾。它直接完成 [[source-Chorley-2023-W-prime-dynamic-model|Chorley 2023]] ingest 明列的兩個未解問題之一——「**部分消耗下的回填驗證**」。

一個值得標記的**細緻化（非矛盾）**：Chorley 2023／Caen 2021 在**完全力竭**（W′＝0）後支持雙指數回填；本份顯示在**部分消耗**後雙指數沒有統計上的優勢、單指數即足。兩者**不衝突**，差別在「從多空的桶子開始補」——完全力竭時慢段份量大、雙段才看得出來，部分消耗時資料（N＝5、小樣本）撐不起雙指數的額外參數。此分界已寫入 [[W prime reconstitution]] 推導第 7 點與易誤解 #6、#7，以及 [[Akaike information criterion]] 易誤解 #3。

另也順帶為長期 pending 的方法學缺口補了兩頁通用工具（[[Overfitting]]、[[Akaike information criterion]]），日後任何「模型選擇／配適」類文獻都可連回。
