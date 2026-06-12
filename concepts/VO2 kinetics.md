---
type: concept
aliases: [VO2動力學, 攝氧動力學, 耗氧動力學, 氧攝取動力學, 攝氧反應, VO2 kinetics, oxygen uptake kinetics, VO2 on-kinetics, tau VO2, τVO2, VO2時間常數, phase II, 基礎相, fundamental phase, functional gain, VO2增益]
tags: [exercise-physiology, VO2-kinetics]
sources: [source-Goulding-2021-VO2-kinetics-tolerance, source-Goulding-2022-determinants-of-CP, source-Cooper-2022-geometric-tau, source-Korzeniewski-2013-VO2-PCr-off-kinetics, source-Burnley-2011-priming-power-duration, source-Zhang-1991-fitness-VO2-VCO2-kinetics, source-Goulding-2023-priming-VO2-kinetics, source-Ma-2010-VO2-kinetics-equation-clarification]
prerequisites: [耗氧量（VO2, oxygen uptake）, 細胞呼吸（cellular respiration）, 時間常數（exponential time constant, τ）]
created: 2026-06-11
updated: 2026-06-12
---

# VO2 動力學（VO2 kinetics）

## 本質（一句話）
VO2 動力學講的不是「耗氧量爬到多高」，而是「當你的出力**突然**跳高時，耗氧量**多快**跟上來」——跟得愈快，向無氧備援借的能量愈少、肌肉內部被擾動得愈小。

## 前置概念
- [[VO2|耗氧量（VO2, oxygen uptake）]]
  （VO2＝用氧速率＝代謝率；本頁談的是它「隨時間怎麼變」。）
- [[Cellular respiration|細胞呼吸（cellular respiration）]]
  （有氧產能必須用氧，所以「供能跟不跟得上」會表現成「VO2 升不升得上」。）
- [[Time constant|時間常數（exponential time constant, τ）]]
  （VO2 的上升是指數式逼近，用 τ 來量它多快；先懂 τ 是「快慢」而非「高度」。）

## 為什麼會這樣（first-principles 推導）
1. 由 [[VO2|VO2]]：VO2 是用氧速率，也就是有氧產能的速率。先前的頁談的是「強度愈高、VO2 愈高」這個**高度**問題。
2. 現在換一個問題：當出力**瞬間**從低跳到一個固定的高功率時，VO2 是**多快**到達那個新需求？運動一開始，ATP 需求幾乎瞬間跳高（見 [[ATP|ATP]]），但 VO2 **沒辦法**瞬間跟上。
3. 為什麼 VO2 不能瞬間跳？因為有氧引擎要被「催」起來：血流要增加、氧要送到、粒線體酵素要活化，都需要時間。**更底層地說，粒線體是被 ADP／Pi 這些「能量花掉的訊號」牽著走的（[[Mitochondrial respiratory control|粒線體呼吸控制]]）——訊號得先累積起來，才能把粒線體催到位，所以 VO2 是「指數逼近」而非「瞬間到位」。** 於是 VO2 **平順地逼近**新的需求值——一個指數式上升（見 [[Time constant|τ]]）。描述它快慢的數字，就是 **τVO2（VO2 的時間常數）**。
4. 這個上升分成幾個**相（phase）**（這是本頁的解剖圖，放慢看）：
   - **Phase I（心動相，cardiodynamic，最初 ~15–20 秒）**：嘴邊量到的 VO2 先小升一下，純粹是因為「血流變快、回到肺的血變多」，**而運動肌肉那邊剛產生的缺氧血都還沒流到肺**。它反映的是「肌肉到肺的血液運送延遲」，**還不是肌肉的代謝**。
   - **Phase II（基礎相／主相，fundamental，~從 20 秒起的指數上升）**：真正重要的一段。這段指數上升**緊跟著肌肉自己的耗氧**，用 τVO2 來描述。要量「VO2 動力學多快」，量的就是這一段的 τ。
   - **Phase III（穩態，steady state）**：VO2 爬到任務需要的值、**穩住不動**（中等強度的情況）。但若強度超過重度，VO2 不會乾淨地穩住，而是冒出 [[VO2 slow component|VO2 慢成分]]——那是另一回事，連過去看。

   （要把這三相寫成**一條可擬合的數學式**，標準做法是「靜息基準＋三段指數（A₀ 心動相、A₁ 基礎相、A₂ 慢成分），各段有自己的振幅 A、時間常數 τ 與時間延遲 TD」——即 Barstow/Scheuermann 模型。注意這條式子要寫成**分段**才符合「各相到自己的時刻才登場」的本意，否則三項相加只是一條平滑曲線；正確寫法與這個容易被忽略的陷阱見 [[Multi-exponential model of VO2 kinetics|VO2 動力學的多指數模型]]。）
5. τVO2 的差距可以很大——**約 10 倍**：菁英耐力運動員快到 τ≈12 秒，年長 COPD 病人慢到 τ≈120 秒。對照之下，「**增益（gain）**」——每瓦功率對應約 10 mL/min 的 VO2——在不同人之間幾乎固定（約 9–11）。**所以人跟人之間差的主要不是「增益（爬多高）」，而是「τ（爬多快）」。**
6. 什麼決定 τVO2？主要在**肌肉內部**：粒線體密度（即 [[Mitochondrial respiratory control|呼吸控制]] 的 Vmax，密度愈高、同樣需求只需較低 ADP 訊號就追上、τ 愈小）、產能酵素被活化的程度（鈣離子驅動的 [[Parallel activation of oxidative phosphorylation|each-step activation／平行活化]]，前饋愈強、τ 愈小）、以及由 [[Phosphocreatine|磷酸肌酸／CK]] 緩衝的 ADP 回饋。在年輕健康者，**送氧（O₂ delivery）通常不是限制**；但在年長者與慢性病，送氧就可能變成限制。此外 [[Muscle fiber types|Type I 纖維]] 的 VO2 動力學比 Type II 快。

   補一點 on/off 的對照（接 Korzeniewski 2013）：上面講的都是「on（運動開始）」那一面。運動**結束**也有對應的 off-kinetics（VO2 怎麼降回基線）。實測上 **on 通常比 off 快**（Rossiter 2002），而恢復期 VO2 怎麼降，被前饋活化的衰減時間 [[Parallel activation of oxidative phosphorylation|τ(OFF)]] 牽動，並與 PCr 補回速率**反向**耦合（見 [[Inverse VO2-PCr off-kinetics relationship|反向關係]]）。另須留意：**肌肉 VO2 與嘴邊量到的肺 VO2**，在中等運動動力學相近，但**重度運動會脫鉤**（血流運送延遲、恢復期心肺仍高），所以拿肺 VO2 去推肌肉的 off 動力學要小心。

   再補一點「同一個人、不同強度」與「不同人、同相對強度」的對照（接 Zhang & Wasserman 1991）：τVO2 不是一個人身上的單一數字——**相對強度愈高（愈接近個人最大能力），on-kinetics 愈慢**。在遞增的固定步階測試裡，低強度時 VO2 乾淨地「階梯狀」跳到新穩態，但愈往高強度、這個階梯愈鈍；**體能差的人在最大能力的上半段（>50%），VO2 階梯甚至整個消失**（被慢成分與無氧供能填補抹平）。而在**相同的相對強度**下比較，**體能愈好、動力學愈快**（到 75% 反應時間 To.75 與 [[VO2max|peak VO2]] 負相關 r≈−0.75～−0.90），意思是同樣吃力時有氧 ATP 通量相對無氧更高——這正是 [[Metabolic stability|代謝穩定性]]的另一面。順帶一提，CO₂ 排出走的是**不同**的時間曲線（[[VCO2 kinetics|VCO2 動力學]]）——它在高強度反而不變慢，原因見該頁。
7. 為什麼要在意它（往下接的線索，這裡只點到）：τ 愈小（動力學愈快）→ [[O2 deficit|氧虧]] 愈小 → 同樣功率下向無氧備援借得愈少、肌肉內代謝物累積愈少 → [[Metabolic stability|代謝穩定性]] 愈高 → 能維持的最高功率（[[Critical power|CP]]）愈高。這條因果鏈是本文獻的主軸，完整推導在 [[Critical Pi threshold and positive feedback model|臨界閾值模型]] 那頁。
8. τVO₂ 是 CP 的**獨立**決定因子——怎麼證明它不只是「送氧的附帶效果」？關鍵實驗是 **work-to-work（從一個已升高的基礎功率再起跑）**：這會單純地放慢 τVO₂，**而微血管送氧（NIRS）不變甚至改善**，結果 CP 仍隨之下降。能「只動 τ、不動送氧」就改到 CP，就證明利用速率本身是一條獨立的旁路（與[[Convective oxygen delivery|對流]]、[[Diffusive oxygen transport|擴散]]並列；三者交互見 [[Determinants of critical power|臨界功率的決定因子]]）。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Goulding 等人主張，VO2 動力學（τVO2）是一個**被低估、卻比 LT/CP/VO2max 更貼近日常功能**的運動耐受指標。理由：它決定「**任何一次**能量需求增加時，肌肉內部會被擾動多少」，所以從爬樓梯到趕公車這種日常活動，它都比傳統有氧參數更相關，也與生活品質、存活率連動。
- **背後的推理／證據**：VO2 動力學和 LT、CP、VO2max 共用機制（粒線體密度、氧化磷酸化能力、對流與擴散送氧），但它**獨特地捕捉「轉換過程（transient）」**——也就是代謝穩定性。並有 τVO2 與 CP 的強反相關等證據支持（細節在模型頁）。

## 易誤解之處
1. **動力學（τ，快慢）≠ 振幅（gain，高度）。** 這是全頁最關鍵的分辨。τ 講「多快到位」，gain 講「最後爬多高」；人跟人差的主要是 τ。把兩者混在一起，後面所有推論都會走樣。一個具體例證：[[Priming effect|預熱（priming）]]後的「primed state」——**primary（基礎相）振幅升高、慢成分壓低、但 primary 的 τ 多半不變**（Burnley 2011；偶有研究見 τ 變快）。所以「預熱加速了 VO2 動力學」這句話，主要指「有氧的起手貢獻被墊高、慢成分被壓下」，**不一定是 τ 本身變小**——正是 τ 與 gain 必須分開看的活教材。Goulding 2023 把這個分辨推到實用後果：**改 τ 還是改振幅，下游改的是不同的表現參數**（降 τ→[[Critical power|CP]]↑、抬振幅/壓慢成分→[[W prime|W′]]↑），而 τ 能不能被預熱改動又取決於**初始 τ（~25 s 門檻）**——見 [[Mechanisms of the priming effect]] 與 [[Priming effect on the power-duration relationship]]。
2. **Phase I 不是肌肉代謝。** 它是「在嘴邊量氣體」這個測量方式造成的循環假象（血流先變快、肌肉的缺氧血還沒到肺）。正因如此，量 τ 要**避開 Phase I、擬合 Phase II**——傳統做法是重複運動六趟再疊平均以壓雜訊；近年 [[Geometric method for VO2 time constant|幾何法（Cooper & Garfinkel 2022）]]改用 [[Cumulative oxygen uptake|累積攝氧量]]圖的斜率/截距幾何，宣稱單趟即可、且須從升高的基線出發讓 Phase I 可忽略。
3. **「嘴邊的肺 VO2」≠「肌肉耗氧」，但通常很接近。** 肺 VO2 是肌肉耗氧的良好代理，多數情況下兩者動力學貼合；但在某些情境（如仰臥運動，基礎血流低、送氧慢）會**脫鉤**，使肺 VO2 看起來比肌肉慢——讀數據時要留意。
4. **VO2 動力學「慢」不代表「人懶」或「沒用力」。** 它是供能機制被催起來的客觀速率，由肌肉的代謝機能決定（粒線體、酵素活化、送氧），是生理屬性。

## 用生活例子再講一次
把 VO2 動力學想成「踩下油門後，引擎轉速多快爬到巡航 RPM」。反應靈敏的引擎（τ 小）幾乎沒有渦輪遲滯，一下就到位；遲鈍的引擎（τ 大）有明顯的 turbo lag。而在引擎還沒跟上的那段遲滯裡，車子是靠**起步電瓶／慣性**先頂著前進——你向那個備援借的那份能量，就是 [[O2 deficit|氧虧]]。引擎反應愈慢，你借得愈多。

（這個類比在哪裡會失準：汽車的「最終巡航轉速」和「爬上去多快」是兩個獨立旋鈕，這點抓得很準；但人體的 τ 還會被纖維型、送氧、酵素活化等多重因素同時影響，不像引擎那樣單純由機械決定。）

## 換句話說
換句話說，VO2 動力學是「耗氧量追上突增需求的速度」，用 τVO2 這個時間常數量化：Phase I 是測量造成的循環假象，Phase II 的指數上升才真正反映肌肉耗氧、是要量的那段，Phase III 是穩態。人跟人之間差的主要是「多快（τ）」而非「多高（gain）」；而 τ 愈小、向無氧備援借得愈少（[[O2 deficit|氧虧]] 愈小）、肌肉愈穩定——這就是為什麼這個「速度」會一路牽動運動耐受。

## 來源
- [[source-Goulding-2021-VO2-kinetics-tolerance]]（"VO2 kinetics and the O2 deficit" 節：phase I/II、τVO2、gain≈10 mL/min/W 近乎恆定而 τ 可變 ~10 倍（12 s↔120 s）、決定 τ 的肌內因素與送氧角色、纖維型；Figure 1。）
- [[source-Goulding-2022-determinants-of-CP]]（§2.3 Oxygen Utilisation：work-to-work 單獨放慢 τ 而送氧不變仍降 CP，證明 τVO₂ 為獨立於送氧的 CP 決定因子；Murgatroyd τ 可解釋達 90% CP 變異。）
- [[source-Cooper-2022-geometric-tau]]（τVO2 量測方法學：傳統需重複六趟疊平均，幾何法以 cumVO2 圖單趟求 τ；佐證「量 τ 須避開 Phase I 擬合 Phase II」「τ 與 VO2max 反相關、訓練變短、心肺疾病變長」。）
- [[source-Burnley-2011-priming-power-duration]]（易誤解 #1：primed state 的指紋＝primary 振幅↑、慢成分↓、primary τ 多半不變——「動力學被預熱」主要靠墊高有氧起手貢獻與壓低慢成分，未必改 τ，是 τ vs gain 須分開看的實例。）
- [[source-Korzeniewski-2013-VO2-PCr-off-kinetics]]（決定 τ 的「酵素活化程度」＝平行活化前饋；on/off 不對稱（on 較快）；肌肉 t₀.₆₃on 模型值（中等 20.0 s、重度 15.2 s）與肺 τp（15–40 s、均 25.5 s）相符範圍；肌肉 vs 肺 VO2 在重度運動因血流延遲脫鉤；off-kinetics 受 τ(OFF) 牽動、與 PCr 反向耦合。）
- [[source-Goulding-2023-priming-VO2-kinetics]]（易誤解 #1 補充：把「基礎相振幅 vs τ」的分離推到表現後果（降 τ→CP↑、抬振幅/壓慢成分→W′↑）、初始 τ~25 s 門檻決定預熱能否縮 τ；Fig. 1 對 cardiodynamic/fundamental/slow 三相的標準刻畫。詳見 [[Mechanisms of the priming effect]]、[[Priming effect on the power-duration relationship]]。）
- [[source-Zhang-1991-fitness-VO2-VCO2-kinetics]]（§6 後的相對強度／體能對照：四個 3 分鐘相對強度步階下 VO2 To.75 53→94 s 顯著變慢、不適者上半相對強度 VO2 階梯消失；同相對強度下 To.75 與 peak VO2 負相關 r≈−0.75～−0.90；對照 [[VCO2 kinetics|VCO2]] 不隨強度變慢。）
- [[source-Ma-2010-VO2-kinetics-equation-clarification]]（Phase I/II/III 寫成數學式的標準模型（Barstow & Molé 1991 雙指數→Scheuermann 2001 加心動相 A₀ 的三指數），以及「三項相加並非分段函數」的釐清；完整推導見 [[Multi-exponential model of VO2 kinetics]]。）
