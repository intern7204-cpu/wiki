---
type: source
tags: [exercise-physiology, critical-power, W-prime, 31P-MRS, recovery]
created: 2026-06-11
---

# 來源：Intramuscular determinants of the ability to recover work capacity above critical power

## 出處
- Skiba, P. F., Fulford, J., Clarke, D. C., Vanhatalo, A., & Jones, A. M. (2015). *Intramuscular determinants of the ability to recover work capacity above critical power.* **European Journal of Applied Physiology**, 115(4):703–713. doi:10.1007/s00421-014-3050-3.（線上發表 2014-11-26，紙本 2015。）
- 原始檔：`C:\原始資料\Intramuscular determinants of the ability to recover work capacity above critical power\`（含 .md 全文與 8 張圖）。

## 核心主張
用 ³¹P-/¹H-MRS 直接量肌肉內代謝物，去檢驗「[[W prime|W′]] 回填的生理底料是什麼」：W′ 回填與「PCr 的可用空間（D_[PCr]）」對得極準（r=0.99），但與 PCr 的**回補速度**對不上——指向 W′ 反映的是肌肉的**[[Oxidative reserve|氧化儲備]]**而非單一代謝物濃度；同時從化學動力學第一性原理推出 [[Differential W prime balance model|W′BAL 的微分（ODE）版]]，其 τ=W′₀/D_CP 免擬合。

## 本份新增／更新的概念
- [[Differential W prime balance model]]（新增）——把 W′ 視為反應槽中的化學反應物，推出消耗式 dW′/dt=−(P−CP)、回填式 dW′/dt=(1−W′/W′₀)(CP−P)，解得與 Skiba 2012 經驗式同形、τ_W′=W′₀/D_CP **無需擬合**、可即時、可跨運動型態；新算 τ 與 Skiba 2012 擬合 τ 相關 r=0.84（Appendix 1）。這是後續文獻 W′BAL·ODE 的出處。
- [[Oxidative reserve]]（新增）——W′ 的消耗與回填可能共同反映「當下氧化率與最大氧化率之差」（D_VO2／D_[PCr]）；模型 W′ 回填與 D_[PCr] 回填 r=0.99（p=0.005）。
- [[Muscle carnosine]]（新增）——肌肽濃度與 W′t½ 呈反曲線（R²=0.55），但與 pH 無關→較可能透過鈣敏化而非緩衝酸。
- [[W prime reconstitution]]（更新）——加入：[PCr] 回補比 W′ 快約 6 倍（t½ 39 vs 232 s）的「脫節」；單腿伸膝 W′ 回填近線性 vs 全身近曲線；D_[PCr]（氧化儲備）追蹤 W′ 回填；pH 非 W′ 的決定因子。
- [[W prime balance model]]（更新）——把「微分版（Skiba 2015）」的出處與免擬合 τ 補實，連結新頁 [[Differential W prime balance model]]。
- [[W prime multicompartment model]]（更新）——加入 Appendix 2 的具體機制：若干**線性**回復的微觀單元（運動單位／肌纖維群）相加，可湊出巨觀**曲線**回復；為多隔間假說提供模擬支撐。
- [[Phosphocreatine]]（更新）——本研究單腿伸膝 [PCr] 回補 t½≈39 s（τ≈57 s）、為有氧機能指標、比 W′ 快約 6 倍。
- [[Metabolic milieu at task failure]]（更新）——[PCr]、[Pi]、pH 在 B_C 與 B_E 力竭時無差異，支持「固定代謝終點＝W′ 固定＝力竭時 W′=0」；但 pH 並非 W′ 決定因子。

## 與既有知識的關係
- **補實出處（重要）**：wiki 多頁先前提到「Skiba 2015 微分形式／W′BAL·ODE」，但只透過 Chorley 2023、Black 2023 間接引用，**沒有自己的來源頁與推導頁**。本份正是該 Skiba 2015，補上 [[source-Skiba-2015-intramuscular-determinants|來源頁]] 與 [[Differential W prime balance model|ODE 推導頁]]。
- **一致／延伸**：與 [[Metabolic milieu at task failure]]（力竭固定終點）、[[Phosphocreatine]]（PCr 再合成為有氧指標）、[[W prime reconstitution]]（回填快慢兩段）一致並深化。
- **修正**：對「W′ 回填的快段＝PCr 補回」這個常見對應提出 nuance——W′ 與 D_[PCr]（容量差）強相關，但與 τ_[PCr]（速率）不相關；且 pH 不是 W′ 的決定因子（挑戰 pH-疲勞觀）。
- **方法限制**：n=10、單腿伸膝（小肌群、回填偏線性、取樣最早僅 60 s）、直接量的 W′ 與 D_[PCr] 僅 r=0.93（p=0.06 未達顯著，達顯著的是**模型預測**的 W′）、肌肽曲線受單一離群值影響——結論偏「encouraging hypothesis」而非定論。
