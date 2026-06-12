---
type: source
tags: [exercise-physiology, critical-power, modelling, W-prime, performance]
created: 2026-06-11
---

# 來源：Modeling the Expenditure and Reconstitution of Work Capacity above Critical Power

## 出處
- Skiba, P. F., Chidnok, W., Vanhatalo, A., & Jones, A. M. (2012). *Modeling the Expenditure and Reconstitution of Work Capacity above Critical Power.* **Medicine & Science in Sports & Exercise**, 44(8), 1526–1532. doi:10.1249/MSS.0b013e3182517a80
- 原始檔：`C:\原始資料\Modeling the Expenditure and Reconstitution of Work Capacity above Critical Power\`（含 4 張圖：Fig.1 W′bal 油表、Fig.2 τ–D_CP 指數、Fig.3 W′ 消耗 vs VO2、Fig.4 路賽 W′ 平衡）。
- 受試者：7 名健康男性（休閒級、非高度訓練；年齡 26±5 yr、體重 81±6 kg）。

## 核心主張
這是**第一篇**把臨界功率（CP）以上那桶有限功容量 W′ 在間歇運動中「消耗＋回填」用一條連續函數即時描述出來的論文——提出卷積積分式 W′_bal（eq.3）與回填時間常數的經驗公式 τ_W′＝546·e^(−0.01·D_CP)+316（eq.4），奠定整個 **W′BAL 模型族**的原型。

## 本份新增／更新的概念
- [[Integral W prime balance model]]（**新增**）：本論文的核心——積分（卷積）版 W′ 平衡模型（W′BAL·INT）。三假設導出 eq.3；迭代反推 τ＋對 D_CP 指數擬合得 eq.4（r²＝0.77）；各恢復條件 τ：S20 377±29、SM 452±81、SH 580±105、SS（>CP）7056 s（非生理）；首次以 "oxidative reserve" 解釋 τ–D_CP 反向關係；模型 W′ 消耗與 VO2 上升相關 r²＝0.82–0.96；真實路賽驗證。
- [[W prime balance model]]（**更新**）：補上 W′BAL 一族的**原始出處**（先前僅由 Black 2023／Skiba 2014/2015 間接描述）；點明 INT 原型現有專頁。
- [[W prime multicompartment model]]（**更新**）：補上「雙隔間改寫 eq.5」的**原始出處**即本論文（先前 line 63 已註明「Skiba 2012 提出」但無來源頁）。
- [[Oxidative reserve]]（**更新**）：補上 "oxidative reserve" 一詞在本文獻的**首次提出**（2012，早於 Skiba 2013/2015 的量化）。
- [[Differential W prime balance model]]（**更新**）：補上它所取代／改寫的「第一代積分式」現有專頁與原始出處。
- [[Intermittent exercise critical power model]]（**更新**）：補上 Morton & Billat 2004 線性間歇式（eq.2）與本文連續化延伸的原始出處連結。

## 與既有知識的關係
- **一致／奠基**：本論文是 wiki 中大量「Skiba 2012／W′BAL·INT／SK／eq.3／eq.4」引用的**真正源頭**，先前一直被後續論文（Black 2023、Skiba 2014/2015、Chorley 2022/2023、Caen 2019、Lievens 2024、Sreedhara 2020）間接描述卻無來源頁。此份補齊原始出處，不與既有頁面矛盾。
- **被後續修正之處（已在相關頁標明）**：
  - eq.4 的**固定群體 τ** → 被 Skiba 2014（系統性低估、個體差異大）、Caen 2019、Lievens 2024 證明不足，催生「可變、個人化 τ」路線。
  - **積分式只能事後算** → 被 Skiba 2015 的 [[Differential W prime balance model|ODE 版]]（τ＝W′₀/D_CP 免擬合、可即時）改寫；ODE 解出與本式同形，等於替本文的經驗式找到第一性原理。
  - **誤差方向**：本文未涉及；後續發現「低估」非定律——Black 2023 在全力榨乾極端下 INT 反而最準、ODE/Morton 高估，Sreedhara 2020 在半力竭＋業餘下 ODE/Bartram 高估。
  - eq.5 **雙隔間**僅為框架 → 由 Skiba 2014/2015 接手發展成 [[W prime multicompartment model]]（仍為待證實假說）。
