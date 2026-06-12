---
type: concept
aliases: [KODE W prime balance model, W prime balance KODE, W′BAL KODE, W′BAL·KODE, KODE模型, W撇KODE模型, K-ODE W prime model, functional CP elevation model]
tags: [exercise-physiology, critical-power, modelling]
sources: [source-Skiba-Clarke-2021-W-prime-balance-mathematics]
prerequisites: [Differential W prime balance model, 臨界功率／臨界速度（critical power / critical speed, CP/CS）, Power-duration relationship plasticity]
created: 2026-06-11
updated: 2026-06-11
---

# W′BAL 的 KODE 版本（W′BAL·KODE：帶常數 K 的微分模型）

## 本質（一句話）
這是把 [[Differential W prime balance model|W′BAL·ODE（微分版）]] 動一個小手腳——在恢復項前面乘上一個常數 K——用來把「**間歇運動會讓 [[Critical power|CP]] 暫時升高**」這件已被觀察到、但原模型假設不存在的事，硬塞進模型裡的一個探索性改法。

## 前置概念
- [[Differential W prime balance model|W′BAL·ODE（微分版）]]
  （KODE 就是 ODE 加一個常數 K；先懂 ODE 的回填式 dW′/dt=(1−W′/W′₀)(CP−P) 長什麼樣、τ＝W′₀/D_CP 怎麼來。）
- [[Critical power|臨界功率（critical power, CP）]]
  （K 的物理意義是「功能性地把 CP 墊高」；先懂 CP 是什麼、為什麼模型平常把它當固定常數。）
- [[Power-duration relationship plasticity|功率–持續時間關係的可塑性]]
  （CP 並非鐵打不變——間歇/暖身可抬高、全力榨乾會壓低；KODE 處理的正是「抬高」這個方向。）

## 為什麼會這樣（first-principles 推導）
一步一步來：

1. **先看一個對不上的觀察。** Skiba & Clarke 比較同一位受試者的 [[Integral W prime balance model|INT]] 與 [[Differential W prime balance model|ODE]] 預測（60 秒超 CP 工作＋30 秒 @20 W 恢復、做到力竭），發現 **ODE 比 INT 提早約 300 秒就預測力竭**（ODE 算 W′ 掉到 0 太快）。問題是：實際選手撐得比 ODE 預測的久。ODE 哪裡太悲觀了？

2. **一個可能的生理解釋：間歇運動把 CP 墊高了。** 每段恢復後，下一段工作起始時的基線 [[VO2|VO₂]] 已被前一段抬高（[[Priming effect|預熱效應]]），於是「可持續輸出的天花板」CP 在間歇過程中其實**比靜態量到的高**。Soares-Caldeira（2012）實測：用 30 秒恢復的間歇方案，CP 平均功能性**升高約 28%**。CP 一旦更高，(P−CP) 變小、W′ 掉得慢，就能撐更久——這正好可以解釋為什麼選手比 ODE 預測撐得久。

3. **怎麼把「CP 升高」塞進 ODE？乘一個常數 K。** 最省事的改法：在 ODE 的恢復項前乘上常數 K，放大 (CP−P) 這個驅動回填的差：
   $$\frac{dW'_{BAL}}{dt} = \left(1 - \frac{W'_{BAL}}{W'_0}\right)K(\text{CP} - P),\quad \text{CP} > P$$
   解出來：
   $$W'_{BAL}(t_b) = W'_0 - \left(W'_0 - W'_{BAL}(t_a)\right)e^{-K\left(\frac{CP-P}{W'_0}\right)(t_b - t_a)}$$
   K>1 等於把恢復驅動力放大，效果上**就像 CP 被墊高**了。為了區別，作者把這個版本叫 **W′BAL·KODE**。

4. **一個漂亮的數字巧合。** 要讓 KODE 預測的力竭時點和 INT 對上（補掉那 300 秒落差），所需的 K＝**1.28**——也就是隱含「間歇中 CP 功能性升高 28%」。而這 28% **恰好等於** Soares-Caldeira 量到的群體平均 CP 升幅。這個吻合不是證明，但很有啟發性。

5. **它順帶戳破一個關於 INT 的猜想。** 一直有人不解：[[Integral W prime balance model|INT]] 那條「就算在淨消耗中也持續有一點回填」的假設明明在生理上可疑（見 INT 易誤解 #1、#3），它怎麼還常常預測得不錯？KODE 給了一個可能答案：**INT 的「持續回填」假設之所以好用，未必因為它生理正確，而是因為它間接地『模擬了間歇中 CP 升高』的效果**——兩種改法（INT 的持續回填、KODE 的墊高 CP）在數字上殊途同歸。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：可以在 W′BAL·ODE 的恢復項乘一個常數 K，用來模擬間歇運動中 CP 的功能性升高；K=1.28 能讓 ODE 的力竭預測與 INT 對齊，且這 28% 與實測 CP 升幅吻合。作者把 KODE 當成**值得進一步研究的探索性構造**，不是已驗證的成品。
- **背後的推理／證據**：證據是「ODE 比 INT 早約 300 秒預測力竭」這個落差、加上 Soares-Caldeira 2012 的 28% CP 升幅與所需 K=1.28 的吻合。推理是：若 CP 在間歇中真的升高，把它寫進模型（透過 K）就該補掉那個落差——而所需的 K 剛好對上獨立量到的升幅，支持「ODE 太早力竭，部分是因為它沒把 CP 升高算進去」。

## 易誤解之處
1. **KODE 是「概念驗證」，不是已驗證的實用模型。** 作者只示範「乘個 K 就能對齊、且 K 的值有生理對應」，並未在獨立資料上驗證它能更準地預測表現。把它當成熟工具用是過頭了。
2. **K 是個固定常數，但 CP 升高其實會隨情境變。** 真實的 CP 升幅取決於恢復時長、強度、訓練狀態等；用單一 K 是粗略簡化（和 ODE 用單一 τ 是同類的妥協）。
3. **「CP 升高」與 [[Power-duration relationship plasticity|CP 在全力榨乾後下降]]」是漂移的兩個相反方向，別搞混。** KODE 處理的是間歇/暖身**抬高** CP；而重複 3MT 那種全力榨乾會**壓低** CP（走 adjusted 模型那條路）。同一個「CP 不是常數」可以往兩個方向跑，看你做了什麼。

## 用生活例子再講一次
回到電動車里程表（[[Differential W prime balance model|ODE]] 那頁的比喻）。原本的 ODE 里程表假設「下坡回充的效率是固定的」；但實際上你**邊開邊把引擎熱機了**，回充效率悄悄變好，所以真實里程比里程表估的多。KODE 的做法就是：與其重寫整套回充模型，乾脆在回充速率上乘一個「熱機加成」K（=1.28，加成 28%），讓里程表的估計對上實際——而這個加成值還剛好等於工程師另外量到的「熱機後效率提升幅度」。

（這個類比在哪裡會失準：電動車的「熱機加成」可以實際標定成固定值；而人體 CP 的升高隨方案而變，固定 K 只是占位用的粗估。類比抓得到「不重寫模型、只乘一個加成把已知效應塞進去」的主軸。）

## 換句話說
換句話說，W′BAL·KODE 就是「ODE ＋ 一個常數 K」：把恢復項乘上 K 來模擬「間歇運動會暫時把 [[Critical power|CP]] 墊高」這個 ODE 原本忽略的真實效應。K=1.28（隱含 CP 升 28%）能補掉 ODE「比 INT 早 300 秒力竭」的落差，而 28% 恰好對上實測，還順帶暗示 [[Integral W prime balance model|INT]] 那條可疑的「持續回填」假設之所以好用，可能只是間接模擬了同一件事。它是一個有啟發性、但尚待驗證的探索性改法。

## 來源
- [[source-Skiba-Clarke-2021-W-prime-balance-mathematics]]（W′BAL Models for Enhancing Physiological Understanding: Uncertainties Regarding the CP and W′ Inputs 一節與 Eq.15–16：ODE 比 INT 早約 300 s 預測力竭；在恢復項乘常數 K 得 W′BAL·KODE；K=1.28 使力竭時點對齊 INT、隱含 CP 功能性升 28%、恰合 Soares-Caldeira 2012；並推測 INT「持續回填」之所以好用或因間接模擬了間歇中 CP 升高。）
