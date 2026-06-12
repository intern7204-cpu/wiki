---
type: concept
aliases: [用過量CO2預測乳酸, 從過量CO2推估乳酸累積, 過量CO2預測血乳酸, 無創乳酸預測, lactate prediction from excess CO2, predicting blood lactate from excess CO2 output]
tags: [exercise-physiology, gas-exchange, acid-base, lactate, methods]
sources: [source-Hirakoba-1996-lactate-prediction-excess-CO2]
prerequisites: [過量二氧化碳（excess CO2 output）, 每單位乳酸的過量CO2（CO2 excess-ΔLa）, 碳酸氫根對乳酸的緩衝（bicarbonate buffering of lactic acid）, 無氧閾值（anaerobic threshold, AT）, 乳酸（lactate / lactic acid）]
created: 2026-06-12
updated: 2026-06-12
---

# 用過量 CO₂ 預測乳酸累積（lactate prediction from excess CO₂ output）

## 本質（一句話）
這是一招「不抽血、光看呼吸」就能估出某趟運動堆了多少血乳酸的方法：先量這趟多吐了多少[[Excess CO2 output|過量 CO₂]]，再除以這個人事先校準好的[[CO2 excess per unit lactate|乳酸換 CO₂ 個人匯率]]，就反推出乳酸累積量。

## 前置概念
- [[Excess CO2 output|過量二氧化碳（excess CO2 output）]]
  （要被量的東西：呼出 CO₂ 裡扣掉純代謝那份、多出來的一截。這招的輸入。）
- [[CO2 excess per unit lactate|每單位乳酸的過量 CO₂（CO₂ excess-ΔLa）]]
  （把過量 CO₂ 換回乳酸的個人匯率；先懂它「同一人穩定、可事先量」，才懂為什麼能拿來換算。）
- [[Bicarbonate buffering of lactic acid|碳酸氫根對乳酸的緩衝]]
  （為什麼過量 CO₂ 和乳酸有可預測的比例關係——中和酸會逼出固定比例的 CO₂。）
- [[Anaerobic threshold|無氧閾值（anaerobic threshold, AT）]]
  （這招只在「強度高過 AT、開始堆乳酸」時才有東西可預測；運動強度也以 %AT 設定。）
- [[Lactate|乳酸（lactate）]]
  （要被預測的目標量。）

## 為什麼會這樣（first-principles 推導）
一步步來，每步只用前面建立的事實：

1. 由 [[Bicarbonate buffering of lactic acid|碳酸氫根緩衝]]：乳酸一堆，它的酸（H⁺）被中和，逼出一批額外 CO₂——這批就是 [[Excess CO2 output|過量 CO₂]]。所以「過量 CO₂」和「乳酸量」之間有因果連動。
2. 由 [[CO2 excess per unit lactate|CO₂ excess-ΔLa]]：這個連動的比例（每 1 mmol/L 乳酸對應多少 mL/kg 過量 CO₂），在同一人身上是個穩定常數，可以事先在一次遞增測試裡量出來。
3. 把 1、2 合起來，反推就成立：如果我知道某趟運動「多吐了多少過量 CO₂（除以體重）」，又知道這個人的匯率，就能把過量 CO₂ 除以匯率，得到乳酸累積量。寫成公式：
   **ΔLa（預測）＝（過量 CO₂ 總量 ÷ 體重）÷ CO₂ excess-ΔLa**
4. 「過量 CO₂ 總量」怎麼量？先定義 **aerobic VCO₂（有氧 CO₂）**＝假如只有有氧代謝、這個 VO₂ 下「該有」的 CO₂；它由這個人在 AT 以下（還沒堆乳酸）那段的 VCO₂-VO₂ 迴歸線讀出。運動中每一刻的「總 VCO₂ 減掉 aerobic VCO₂」就是當下的過量，把它從頭到尾**積分**起來，就是這趟的過量 CO₂ 總量（圖上＝總曲線高出有氧線的那塊面積）。
5. Hirakoba 等人實測驗證：八位受試者做 100%／120%／150% AT 的 4 分鐘定功率運動，過量 CO₂（除體重）隨乳酸累積一路升高，兩者高度相關（r＝0.939）；用公式算出的預測乳酸與實測乳酸也非常吻合（r＝0.954，n=20，估計標準誤 SEE＝1.47 mmol/L）。
6. 所以結論：在超過 AT 的定功率運動裡，光靠呼吸氣體就能估出血乳酸堆了多少——把抽血換成了一台氣體分析儀。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：在 AT 以上的定功率運動中，血乳酸的累積量可由「過量 CO₂ ÷ 個人匯率」預測，準度（r＝0.954、SEE≈1.47 mmol/L）與舊的 CO₂ 平衡法（Clode & Campbell 1969，r＝0.97、誤差約 ±1 mmol/L）相當，但程序簡單得多。可用於運動處方時無創評估代謝負荷。
- **背後的推理／證據**：舊的 CO₂ 平衡法要在每段運動前後做 CO₂ 重複呼吸量混合靜脈 P_v̄CO₂、還要假設一個肌肉呼吸商（RQm 0.90–0.95，但 Beaver-Wasserman 指出它人際間從 0.84 變到 1.02）和一條 CO₂ 解離曲線斜率（0.40–2.10 mL·mmHg⁻¹·kg⁻¹，差五倍），步驟繁複又帶假設。本法把這些全換成「一條 sub-AT VCO₂-VO₂ 迴歸線 ＋ 一個事先量好的個人匯率」，所以「簡單、可實作」。

## 易誤解之處
1. **這招只在「超過 AT」時有效，且在剛過 AT（低強度）最不準。** Stage I（100% AT）明顯高估（預測 3.19 vs 實測 1.82，p<0.05）；原因是此時肌肉才剛開始靠無氧醣解，過量 CO₂ 很小，方法的解析度不夠把它和有氧 CO₂ 分開。強度愈高反而愈準（Stage III 預測 12.74 vs 實測 12.19，差僅 0.55）。
2. **整體偏向「高估」乳酸，且有兩個系統性原因。** (a) aerobic VCO₂ 是用**遞增測試**的迴歸線估的，但 Yano 1987 指出同一 VO₂ 下定功率運動的 VCO₂ 比遞增時高，所以用遞增線會**低估** aerobic VCO₂ →**高估**過量 CO₂；(b) 過量 CO₂ 裡混了一小份是[[Exercise hyperventilation|過度換氣]]為代償代謝性酸中毒吹掉的 CO₂，不全是緩衝乳酸那份。兩者都把預測值往上推。
3. **起始那一分鐘 aerobic VCO₂ 反而高於總 VCO₂（過量算出來是負的）。** 運動最初新產的 CO₂ 先被存進[[Body CO2 stores|組織 CO₂ 庫]]（[[Respiratory exchange ratio|R]] 暫時下凹），使這段嘴巴量到的 VCO₂ 偏低。這是 [[Excess CO2 output kinetics|過量 CO₂ 的時間軸延遲]]在預測上的體現；4 分鐘的定功率時間夠長，整段積分才把這個起始虧損蓋過去。
4. **個別誤差不小（−1.71 ~ +4.05 mmol/L），且和受試者、和功率都無關。** 群體平均很準，不代表用在某一個人某一趟就準。誤差來源（個人的遞增 vs 定功率迴歸線差距、個人過度換氣強弱）因人而異，作者自陳機制仍待釐清。
5. **【機制重估｜Péronnet 2006】「過量 CO₂＝被緩衝的乳酸新生 CO₂」是經典 Wasserman 學派語言，機制上要打折讀。** 嚴格說那批 CO₂ 是從[[Body CO2 stores|身體碳酸氫根庫]]放出的既存 CO₂、非肌肉現做（[[Nonmetabolic CO2|非代謝 CO₂]] 已被否證），且過量 CO₂ 與乳酸只**鬆散**相關。本法之所以還能用，是因為在**夠長的定功率**運動裡、把過量 CO₂ **積分**起來時，它與乳酸累積的**總量**仍對得相當好（這也是 Yunoki 1999、Stringer 1995 一致的發現）——但要當成「乳酸的可靠替身」、不是「肌肉新生了這麼多 CO₂」的字面量。

## 用生活例子再講一次
想像你想知道一場派對喝掉多少酒，但不想一杯杯數。你發現「垃圾桶裡的空瓶蓋數量」和喝酒量很穩定地成比例。於是你先在一場已知喝多少的派對校準出「每喝一瓶 → 丟幾個瓶蓋」（個人匯率），之後任何一場只要數瓶蓋、除以匯率，就估得出喝了多少。過量 CO₂ 就是身體的「瓶蓋」——緩衝乳酸時順手丟出來的可數副產物；先校準匯率，之後光數它就能反推乳酸。

（失準之處：瓶蓋和喝酒量幾乎一對一、乾淨；過量 CO₂ 卻有一部分被存進庫、一部分被過度換氣多吹出來，還受「用遞增線估有氧基準」的偏差污染——所以這招在低強度會失準、整體偏高估，對應上面易誤解 #1–2。）

## 換句話說
換句話說，這招把「抽血驗乳酸」換成「看呼吸算面積」：先畫出某人「純有氧該吐多少 CO₂」的基準線，運動時超出基準的那塊面積就是過量 CO₂；再用這個人事先量好的「乳酸換 CO₂ 匯率」一除，就還原出血乳酸堆了多少。它在高強度準、低強度差，整體略偏高估，是個方便但有系統偏差的估算法。

## 來源
- [[source-Hirakoba-1996-lactate-prediction-excess-CO2]]（全文核心：公式 ΔLa,predicted＝Ex CO₂·mass⁻¹ ÷ CO₂ excess-ΔLa；Table 2 三段強度預測 vs 實測（Stage I 高估 p<0.05、II/III 無顯著差、Stage III 差 0.55）；Fig 2 過量 CO₂ vs ΔLa r＝0.939、Fig 3 預測 vs 實測 r＝0.954 SEE 1.47；Discussion 對比 Clode-Campbell 法、兩個高估來源、個別誤差 −1.71~4.05。）
