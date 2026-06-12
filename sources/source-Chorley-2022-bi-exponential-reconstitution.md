---
type: source
tags: [exercise-physiology, critical-power, W-prime, modelling, recovery, fatigue]
created: 2026-06-11
---

# 來源：Bi-exponential modelling of W′ reconstitution kinetics in trained cyclists

## 出處
- 作者：Alan Chorley, Richard P. Bott, Simon Marwood, Kevin L. Lamb
- 年份／期刊：2022, *European Journal of Applied Physiology*, 122:677–689（線上 2021-12-18；DOI: 10.1007/s00421-021-04875-2）
- 原始檔：`C:\原始資料\Bi-exponential modelling of W' reconstitution kinetics in trained cyclists\`
- 註：與已收錄的 [[source-Chorley-2023-W-prime-dynamic-model]] 為**不同論文**。本篇（2022, EJAP）是雙指數 FC/SC 結構的**奠基刻畫**（50 W 固定恢復、變動時長、重複 ramp）；Chorley 2023（EJSE）是在其上建的**動態模型**（納入恢復強度、可上碼表）。

## 核心主張
W′ 回填的時間歷程最好用**雙指數模型**描述——一個快成分（FC，振幅≈50.67%、τ≈21.5 s，對應 PCr 再合成）加一個慢成分（SC，振幅≈49.33%、τ≈388 s，對應血乳酸清除）；以 AICc 判定雙指數優於既有單指數模型。最重要的新發現：**反覆力竭造成的回填變慢，侷限在慢成分（τ_SC 增大），快成分的 τ 與兩段振幅都不變**；且這個變慢程度（Δτ_SC）與有氧體能（V̇O₂max、CP、大腿肌圍、EPOC）負相關。僅用 30 s 與 240 s 兩個恢復時間點即可個人化建模。

## 本份新增／更新的概念
- [[Bi-exponential W prime reconstitution model|W′ 回填的雙指數模型]]（**新增**）——本篇的主概念頁：FC/SC 雙指數結構、AICc 模型選擇（含「資料點要夠多才穩定偏好雙指數」）、FC≈PCr/SC≈乳酸的時間尺度對應、反覆力竭只拖慢慢段、Δτ_SC 與有氧體能負相關、30 s+240 s 兩點建模。填補先前 wiki 多處引用「雙指數（Caen 2021、Chorley 2022）」卻無專頁、無來源的缺口。
- [[W prime reconstitution|W′ 回填]]（更新）——把「反覆力竭使回填變慢」的歸因從籠統的「H⁺ 抑制 PCr」修正為「**侷限於慢段（τ_SC）、快段 τ_FC 不變**」；補上 FC/SC 振幅各約一半、與 W′ 大小相關。
- [[W prime balance model|W′ 平衡模型]]（更新）——把第二代「雙指數」一節的引用（Caen 2021、Chorley 2022）正式接到本來源；補「30 s+240 s 兩點即可校準」的測試負擔簡化。
- [[W prime multicompartment model|W′ 多隔間模型]]（更新）——指出雙指數即「恰好兩個隔間」的實測實例（FC/SC ≈ 快/慢恢復成分），與多隔間「隔間≈纖維群」屬同一種比喻性、待證實的對應。
- [[Phosphocreatine|磷酸肌酸]]（更新）——補 PCr 再合成 τ 的具體數值（股外側肌≈29 s、小腿≈25 s）並標註與雙指數模型 τ_FC≈21.5 s 吻合。

## 與既有知識的關係
- **補充／填補**：把 wiki 多處（[[W prime balance model]] 別名含 `bi-exponential W prime model`、推導第 5 點「雙指數（Caen 2021、Chorley 2022）」）引用卻無來源的雙指數模型補上專頁與出處——解一個 §8 lint 缺口（被多次提到卻無獨立頁）。
- **修正**：[[W prime reconstitution|回填]] 頁原把反覆力竭的變慢歸於「酸抑制 PCr 再合成」（會預期快段變慢）；本篇實測 τ_FC 不變、僅 τ_SC 增大，故修正為「變慢侷限於慢段（清酸/代謝物），非 PCr 段」。兩邊已交叉標註。
- **一致**：FC≈PCr 再合成、SC≈乳酸清除，與 [[Phosphocreatine|PCr]]、[[Lactate|乳酸]]、[[Inorganic phosphate|Pi]] 諸頁的代謝機制相符；雙指數作為「恰兩個隔間」的實測，與 [[W prime multicompartment model|多隔間模型]]（Skiba 2014）的方向一致、互為佐證但各有保留（皆屬待證實的比喻對應）。
- **方法**：以 [[Akaike information criterion|AICc]] 對抗 [[Overfitting|過度配適]]（雙指數 5 參數 vs 單指數 2 參數），方法面與 [[source-Lievens-2024-partial-depletion]] 一致——值得注意兩篇結論方向相反：完全力竭時 AICc 偏好雙指數（本篇），部分消耗時 AICc 偏好單指數（Lievens），共同說明「模型該多複雜要看情境與資料」。
