---
type: concept
aliases: [氧虧, 氧虧損, 氧赤字, oxygen deficit, O2 deficit, accumulated O2 deficit]
tags: [exercise-physiology, VO2-kinetics, metabolism]
sources: [source-Goulding-2021-VO2-kinetics-tolerance, source-Gaesser-1996-slow-component, source-Cooper-2022-geometric-tau]
prerequisites: [VO2 動力學（VO2 kinetics）, ATP（adenosine triphosphate，三磷酸腺苷）, 磷酸肌酸（phosphocreatine, PCr）, 乳酸（lactate / lactic acid）與它的產生]
created: 2026-06-11
updated: 2026-06-11
---

# 氧虧（oxygen deficit, O2 deficit）

## 本質（一句話）
氧虧就是「運動開頭你向身體**借**的那份能量」——因為 VO2 不能瞬間升上來，需求和有氧供給之間的缺口，先由無氧備援（氧庫存、磷酸肌酸、醣解）墊著。

## 前置概念
- [[VO2 kinetics|VO2 動力學（VO2 kinetics）]]
  （氧虧的大小由「VO2 升得多慢」決定；先懂 τVO2。）
- [[ATP|ATP（adenosine triphosphate，三磷酸腺苷）]]
  （缺口要靠補 ATP 的三條路；先懂 ATP 周轉與三條供能路。）
- [[Phosphocreatine|磷酸肌酸（phosphocreatine, PCr）]]
  （墊缺口的主力之一；先懂 PCr 的瞬間補 ATP。）
- [[Lactate|乳酸（lactate）與它的產生]]
  （另一個墊缺口的來源是醣解產乳酸；先懂這條無氧捷徑。）

## 為什麼會這樣（first-principles 推導）
1. 由 [[VO2 kinetics|VO2 動力學]]：運動一開始，ATP 需求**瞬間**跳高，但 VO2 只能以 τVO2 的速度慢慢爬。於是頭幾分鐘，**有氧供能是不足的**。
2. 一定要有東西墊上這個不足，否則人根本動不了。墊的來源是**非有氧**的：庫存的氧（掛在血紅素、肌紅素上或溶解的）、[[Phosphocreatine|PCr]] 分解、以及醣解產 [[Lactate|乳酸]]。Krogh 與 Lindhard（1913）把這段不足命名為「氧虧（O2 deficit）」。
3. 把它量化：若任務能進入穩態，
   $$O_2\ deficit = \Delta\dot{V}O_2 \times \tau_{\dot{V}O2}$$
   ΔVO2＝VO2 總共要升多高，τVO2＝它升得多慢。**跳得愈大、或動力學愈慢，氧虧愈大。**
4. 由於增益（每瓦對應的 ΔVO2）幾乎固定，**特定功率下的氧虧，主要由 τVO2 決定**。動力學快（τ 小）→ 氧虧小 → PCr 少分解、Pi/H⁺/ADP 少累積、乳酸少生——這就是「VO2 升得多快」牽動下游一切的那根槓桿。
5. 氧虧是**必要的、不是壞事**：它是系統「緩緩切入」的緩衝，避免供能機制猛烈過衝。證據是——若強迫 VO2 瞬間反應（實驗上抑制 CK），ATP 恆定與出力反而**嚴重崩壞**。所以這段「先借一下」是保護，不是缺陷。
6. 重要限制（本節的轉折，也是通往模型的關鍵）：氧虧**只有在任務能進入穩態時才算得乾淨**。一旦功率高到造成代謝性酸中毒，運動效率下降（每瓦要燒更多 ATP，見 [[VO2 slow component|慢成分]]），就**沒有單一的 VO2** 可言，氧虧算不準，只能落在增益的上下限之間（約 9～15 mL/min/W）。
7. 後果：因為運動的力竭幾乎都發生在**非穩態**，而氧虧只能在穩態算準，所以**單靠氧虧（以及它背後的 VO2 動力學）無法預測運動表現**。這個「算不準」正是為什麼需要升級成 [[Critical Pi threshold and positive feedback model|臨界閾值與正回饋模型]]——用「肌肉內代謝物有沒有越過臨界」來接手解釋力竭。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Goulding 等人指出，古典的氧虧概念雖抓對了「開頭要借非氧化能量」這件事，但**它本身無法解釋力竭**；要用「臨界閾值＋正回饋」把氧虧概念接到功率-持續時間關係上。
- **背後的推理／證據**：氧虧只能對「達穩態或極快達 VO2max」的功率可靠計算（Ozyener 等甚至量到重度運動的「負累積氧虧」這種矛盾結果）；而力竭發生在非穩態，所以用氧虧預測非穩態耐受「註定失敗」。這個失敗推動了模型的提出。

## 易誤解之處
1. **氧虧（deficit）≠ 氧債／EPOC（debt）。** 氧虧是運動**開頭**借的；[[Oxygen debt|氧債（O2 debt）]]／運動後過量耗氧（EPOC）是運動**結束後**償還的。一個在前、一個在後，別混。兩者算法對稱（氧債＝δVO2×τ(off)），理想中等強度下約略相等——這個對稱正是 [[Geometric method for VO2 time constant|幾何法]] 能用單趟運動同時量到 on-τ 與 off-τ 並互相驗證的依據。
2. **欠氧虧不代表肌肉缺氧。** 每次強度一升，人人都會產生氧虧——這是正常的「先頂著」，連輕鬆運動都有，**不是組織缺氧**（見 [[Dysoxia|dysoxia]]）。
3. **墊缺口的備援是有限容量的。** PCr、肝醣、氧庫存相對於「持續運動數分鐘」的需求都很小——足以撐過開頭的轉換，但撐不起整場運動。
4. **氧虧算不準 ≠ 氧虧不存在。** 高強度時氧虧其實更大，只是因為效率下滑、沒有單一 VO2，所以「量不準」；不是「沒有缺口」。
5. **古典上「W′ ≈ 氧虧」，但別把兩者畫等號。** Gaesser 與 Poole 指出，功率-時間雙曲線的曲率常數 [[W prime|W′]]（>W_a 能多做的有限功）最初就是被想成「等於氧虧」——一個有限的能量庫（磷酸原、靜脈/肌紅素氧庫存、無氧醣解）。更值得記的是：對所有「快速動力學會衝破 VO2max」的超 W_a 功率，氧虧 ＝ VO2max × τ，**與功率無關**（都一樣大）——這個「氧虧與功率獨立」正是雙曲線 W-t 關係的理論根基。但現代理解認為 W′ 不是單純的固定無氧儲備（見 [[W prime|W′]]），所以「W′＝氧虧」只是歷史起點、不是定論。

## 用生活例子再講一次
把起步想成在斜坡上用手排車起步：引擎（有氧）還沒輸出足夠扭力前，你得靠**半離合、溜一點、用慣性**（無氧備援）把車先撐住、推出去。引擎反應愈慢（τ 大），你愈得多踩離合、多借慣性——借的這份，就是氧虧。等引擎轉上來（VO2 到穩態），就不用再借。

（這個類比在哪裡會失準：汽車半離合借的是機械慣性、可以一直溜；身體的 PCr／醣解備援是有限的化學儲備，墊一陣可以、墊整場不行，而且醣解墊久了會留下酸這種「帳單」。）

## 換句話說
換句話說，氧虧是運動開頭、VO2 還沒追上需求時，向氧庫存／[[Phosphocreatine|PCr]]／醣解借來墊缺口的那份能量，大小約等於 ΔVO2×τVO2——動力學愈慢、借得愈多。它是必要的緩衝，但只有在穩態才算得準，所以單靠它無法解釋力竭，必須交棒給以肌肉內 [[Inorganic phosphate|Pi]] 累積為核心的 [[Critical Pi threshold and positive feedback model|臨界閾值模型]]。

## 來源
- [[source-Goulding-2021-VO2-kinetics-tolerance]]（"VO2 kinetics and the O2 deficit" 與 "The O2 deficit and exercise intensity" 節：Krogh-Lindhard 命名、Equation 1（O2 deficit=ΔVO2×τVO2）、氧虧為必要緩衝（CK 抑制反例）、僅穩態可靠計算、無法預測非穩態表現、增益 9–15 區間。）
