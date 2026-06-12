---
type: source
tags: [exercise-physiology, VO2-kinetics, modeling, math]
created: 2026-06-12
---

# 來源：Clarifying the equation for modeling of V̇O2 kinetics above the lactate threshold

## 出處
- Ma S, Rossiter HB, Barstow TJ, Casaburi R, Porszasz J.
- *Journal of Applied Physiology* (1985) 2010 Oct;109(4):1283–1284.
- DOI: [10.1152/japplphysiol.00459.2010](https://doi.org/10.1152/japplphysiol.00459.2010) ｜ PMID: 20940444
- 文類：Letter to the Editor（致編輯短信，非原始研究）。
- 原始檔：`C:\原始資料\Clarifying the equation for modeling of VO2 kinetics above the lactate threshold\`
- 出處核實：依 PubMed 記錄（DOI 與 PMID 如上）；原檔頁尾「1284」與作者署名一致。

## 核心主張
描述「超過乳酸閾值時 VO2 隨時間上升」的標準三相多指數模型（Barstow & Molé 1991 → Scheuermann 2001），若照字面把各段指數**直接相加**，數學上是一條單一平滑曲線、而非作者文字與圖所描述的「各相在各自時間延遲後依序登場」的**分段函數**；用赫維賽德階梯函數 H(t−TD) 當開關乘在每段前面（式 8），即可還原分段本意——這純是寫法與實作的釐清，不更動模型的任何生理解釋。

## 本份新增／更新的概念
- [[Heaviside step function]]（新增）——數學前置：時間到某刻才從 0 跳成 1 的「開關函數」；式 6 定義、式 7–8 示範用法。
- [[Multi-exponential model of VO2 kinetics]]（新增，headline）——VO2 三相（A₀ 心動相／A₁ 基礎相／A₂ 慢成分）的標準擬合式、「相加≠分段」的陷阱、赫維賽德修正式。
- [[VO2 kinetics]]（更新）——在 Phase I/II/III 解剖後補上「寫成數學式」的標準模型與分段陷阱的指標連結；新增 source。
- [[VO2 slow component]]（更新）——易誤解新增一條：慢成分＝擬合式第三段指數 A₂ 項（τ₂、TD₂≈80–110 s），須分段；新增 source。

## 與既有知識的關係
- **一致、純補強，無矛盾**。本份不碰生理機制爭議（心動相/基礎相/慢成分的成因見 [[VO2 kinetics]]、[[VO2 slow component]]），只把這些頁長期以「Phase I/II/III、τVO2、增益」定性描述的 VO2 上升曲線，補上其背後**標準數學模型**的精確形式與一個容易被忽略的數學陷阱。
- 作者群與既有來源高度相關：Harry B. Rossiter、Thomas J. Barstow 都是本 wiki VO2 動力學線（Goulding、Korzeniewski、Whipp 等）反覆引用的同領域核心人物；本份把那條主線缺的「擬合式本身怎麼寫」補齊。
- 連帶補上一個跨領域數學前置 [[Heaviside step function]]，未來任何「分段／延遲後啟動」的動力學模型（CO₂ 輸出、通氣、心率、肌內磷酸等）都可複用。
