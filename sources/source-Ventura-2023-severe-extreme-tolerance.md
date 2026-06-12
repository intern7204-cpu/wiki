---
type: source
tags: [exercise-physiology, critical-power, exercise-tolerance, intensity-domains, methods]
created: 2026-06-12
---

# 來源：Prediction of Exercise Tolerance in the Severe and Extreme Intensity Domains by a Critical Power Model

## 出處
- 檔名：`Prediction of Exercise Tolerance in the Severe and Extreme Intensity Domains by a Critical Power`（C:\原始資料）
- 作者：Thiago Pereira Ventura, Fernando Klitzke Borszcz, Diego Antunes, Fabrizio Caputo, Tiago Turnes
- 出處：*Journal of Human Kinetics*（投稿 2023-01-30、接受 2023-04-05、出版 2023-10-27）
- 機構：Federal University of Santa Catarina／Santa Catarina State University，Florianópolis，Brazil

## 核心主張
[[Critical power|臨界功率（CP）]] 與 [[W prime|W′]] 用**三次**預測試驗配適時，能準確預測 severe 域與 severe/extreme 邊界（[[Maximal intensity for VO2max attainment|IHIGH]]、IHIGH+5%）的力竭時間；但這個能力在 [[Extreme intensity domain|extreme（極限強度）域]]會**退化**——平均雖未顯著偏離，異質變異卻顯示「撐愈久高估愈多」，且只用兩次試驗配適會顯著高估短時間運動的耐受。

## 研究設計（一句話）
19 名業餘車手，做多次定功率力竭測試求 CP/W′（95/100/110% PPO），再以 Turnes 2016 逼近法定出 [[Maximal intensity for VO2max attainment|IHIGH]]（severe 域上緣，達 VO2max）與 IHIGH+5%（extreme 域下緣），把四種 CP 模型（CPhyp / CPlinear / CP1/time / 兩試驗 CPlinear(95,110)）預測的 t_lim 與實測值用 [[Bland-Altman agreement analysis|Bland-Altman]] 比較。

## 關鍵數據
- CP 三模型 211–213 W（SEE ~4.5%、R²≈0.97–0.996）；W′ 19.4–20.3 kJ（SEE **14–17%**，超過建議的 10%）。
- IHIGH 功率 344±52 W、實測 t_lim 155±30 s；IHIGH+5% 功率 371±53 W、實測 t_lim 120±26 s。
- IHIGH 的 VO2peak（3.72 L/min）＝ VO2max（3.75）；IHIGH+5% 的 VO2peak（3.50）**顯著較低，無人達 VO2max**。
- IHIGH：三/兩試驗模型預測均無顯著差（同質變異，預測穩健）。
- IHIGH+5%：兩試驗模型顯著高估（129 vs 120 s，p=0.04）；三試驗模型平均無顯著差，但**全部呈異質變異**（撐愈久高估愈多）。
- 個體一致性界線（LoA）兩域都寬（±15–22%）。

## 本份新增／更新的概念
- [[Maximal intensity for VO2max attainment]]（新增）— IHIGH：力竭前仍能達 VO2max 的最高強度＝severe/extreme 邊界；逼近法操作定義；非鋒利閾值（Iannetta 2022）。
- [[Extreme intensity domain]]（新增）— 極限強度域（>IHIGH）：力竭太快、VO2max 達不到、W′ 未耗竭；CP 模型在此高估且愈高愈不準；機制未解。
- [[Critical power model fitting]]（新增）— 兩參數 CP 模型的三種線性化（雙曲線／功–時間／功率–倒數時間）、預測試驗數（2 vs 3）、CP 準 vs W′ 不準的 SEE 對比。跨多篇 W′ 文獻隱含使用、此前無專頁。
- [[Bland-Altman agreement analysis]]（新增）— 跨領域方法頁：偏倚、一致性界線、同質/異質變異；「相關 ≠ 一致」。
- [[Exercise intensity domains]]（更新）— 易誤解 #5 用 IHIGH 把 CP 之上精確切成 severe/extreme，釐清四分法術語。
- [[Critical power]]（更新）— 易誤解 #9：t_lim 公式準確範圍有上限、進 extreme 域高估；CP SEE vs W′ SEE。
- [[W prime]]（更新）— 易誤解 #8：「力竭＝W′＝0」只在 severe 域成立，extreme 域 W′ 未耗竭。
- [[VO2 slow component]]（更新）— 易誤解 #8：慢成分 80–110 s 才疊加，extreme 域力竭太快使其來不及發展、VO2 達不到頂。

## 與既有知識的關係
- **補充**：把 wiki 原本的三區間（中等/重度/極重度）精化為四區間（多出 [[Maximal intensity for VO2max attainment|IHIGH]] 與 [[Extreme intensity domain|extreme]]），填補了 [[Exercise intensity domains]] 易誤解 #5（Miller 2023 已點出「extreme zone」但無專頁）與 [[Critical power]] t_lim 公式適用範圍的缺口。
- **一致**：與 [[Metabolic milieu at task failure|力竭時固定代謝終點]]、[[W prime|W′＝0 假設]] 一致——本份正是指出該假設在 extreme 域破功的邊界。
- **方法層延伸**：[[Critical power model fitting]] 與 [[Bland-Altman agreement analysis]] 補上既有方法層（[[Overfitting]]、[[Akaike information criterion]]）旁邊的兩塊基礎工具，供整個 CP/表現預測文獻共用。
- **開放問題**：extreme 域**為何**力竭（W′ 未乾、VO2max 未達時的決定機制）仍未解；本份僅以「異質變異暗示無氧代謝主導」與單關節研究的「extreme 專屬較小 W′」指方向。
