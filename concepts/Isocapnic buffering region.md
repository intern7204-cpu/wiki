---
type: concept
aliases: [等二氧化碳緩衝區, 等碳酸緩衝區, 恆碳酸緩衝期, 等CO2緩衝期, isocapnic buffering, isocapnic buffering region]
tags: [exercise-physiology, gas-exchange, ventilation, thresholds]
sources: [source-Poole-2021-AT-controversy, source-Peronnet-2006-CO2-hyperventilation]
prerequisites: [乳酸閾值（lactate threshold, LT）, 呼吸代償點（respiratory compensation point, RC）]
created: 2026-06-10
updated: 2026-06-11
---

# 等二氧化碳緩衝區（isocapnic buffering region）

## 本質（一句話）
等二氧化碳緩衝區就是「乳酸閾值之後、呼吸代償點之前那一段強度區間：身體已經在多呼吸排掉緩衝產生的 CO₂，但呼吸還剛好讓血中 CO₂ 分壓**維持恆定**」——這段「CO₂ 不掉」的窗口，正是用氣體交換確認真的踩到乳酸閾值的關鍵證據。

## 前置概念
- [[Lactate threshold|乳酸閾值（lactate threshold, LT）]]
  （這個緩衝區從 LT 開始；先懂 LT 在標什麼。）
- [[Respiratory compensation point|呼吸代償點（respiratory compensation point, RC）]]
  （這個緩衝區在 RC 結束；先懂 RC 是什麼。）

## 為什麼會這樣（first-principles 推導）
1. 先回顧兩條鏈：過了 [[Lactate threshold|LT]]，乳酸的 H⁺ 被 [[Bicarbonate buffering of lactic acid|碳酸氫根中和]]，放出 [[Excess CO2 output|過量 CO₂]]；身體把這份多出來的 CO₂ 呼掉，於是通氣（VE）相對於 [[VO2|VO2]] 開始增加。
2. 關鍵問題：通氣增加，會不會把血中 CO₂ 分壓（PCO₂）也拉低？在 LT 到 RC 之間，答案是**幾乎不會**——通氣增加的幅度，剛好等於要排掉那份額外 CO₂ 所需，**不多也不少**，所以動脈與呼氣末 PCO₂ 維持恆定（iso-capnic ＝「等-CO₂」）。
3. 為什麼能恰好維持恆定？因為此時通氣是被「多出來的 CO₂」拉著走（被動跟隨代謝），還沒進入「主動猛呼吸去壓低 pH」的階段。頸動脈體（carotid body）對血液變酸的神經反應相對慢，所以在這段窗口裡，通氣只夠排掉 CO₂、還來不及過度換氣。
4. 再往上到 [[Respiratory compensation point|RC]]：酸堆到緩衝快擋不住，身體開始**主動過度換氣**壓低 PCO₂——這時 PCO₂ 才終於開始下降，等碳酸窗口就此關閉。所以這段窗口的兩端，正好是 LT（開始）與 RC（結束）。
5. 它為什麼有用？因為它是**驗證 [[Gas exchange threshold|氣體交換閾值（GET）]]真偽的內部對照**：如果 V-slope 上看到一個轉折，又伴隨「PCO₂ 維持恆定（等碳酸）＋呼氣末 PO₂ 開始上升」的窗口，就能確認這個轉折真的是 LT（乳酸緩衝），而不是別的東西假冒的（例如測試前過度換氣造成的偽閾值）。沒有等碳酸窗口，GET 的解讀就站不住。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Poole 等人指出，LT 與呼吸代償之間的窗口稱為「等碳酸緩衝區」——此區間內通氣相對 VO2 不成比例上升、呼氣末與動脈 PO₂ 上升，但 PCO₂ 維持穩定。等碳酸緩衝的存在與在逐增運動中的辨識，正是用氣體交換判定「代謝性酸中毒開始（即 LT）」的依據。
- **背後的推理／證據**：邏輯是「排他驗證」。GET 偵測到的「過量 CO₂」可能來自兩種原因——乳酸緩衝（真 LT），或單純過度換氣壓低 PCO₂（假的）。等碳酸（PCO₂ 不降）這個條件正好排除了第二種：既然 PCO₂ 沒掉，過量 CO₂ 就不是過度換氣造成的，只能是緩衝造成的。所以「有等碳酸窗口」＝「這是真 LT」。

## 易誤解之處
1. **「等碳酸」指 PCO₂ 不變，不是 CO₂ 輸出不變。** 這段裡 [[VCO2|VCO2]]（每分鐘呼出的 CO₂ 量）是增加的（因為要排額外 CO₂）；維持恆定的是血中/呼氣末 CO₂ 的**分壓（濃度）**。兩者別搞混。
2. **它是窗口的「過程」，兩端才是「點」。** LT 和 RC 是兩個閾值點；等碳酸緩衝區是夾在中間的一整段強度。長短因人而異（文獻顯示有人短、有人長達 60 瓦）。
3. **沒有等碳酸窗口時 GET 不可信。** 例如高海拔（化學受器被低氧敏化、LT 處就直接過度換氣）或 McArdle 病（無乳酸卻過度換氣），都缺等碳酸窗口，這時 V-slope 看到的「閾值」可能是假的。
4. **它連結但不等於 RC。** 窗口在 RC 結束；RC 是窗口的「上端那個點」，不是窗口本身。
5. **【機制深化｜Péronnet 2006】等碳酸期 V̇CO₂ 上升，是「低 pH 把庫存 CO₂ 頂出」而非「肌肉現做」。** 用 [[Body CO2 stores|身體 CO₂ 庫]]的「兩個旋鈕」看最清楚：這段裡只開了**旋鈕一（加酸）**——血液開始變酸、把碳酸氫根頂成 CO₂ 呼掉，使 [[VCO2|V̇CO₂]] 與 V̇E 相對 VO2 上升；**旋鈕二（[[Exercise hyperventilation|過度換氣]]壓低 P_aCO₂）還沒開**，所以 P_aCO₂ 維持恆定（這就是「等碳酸」）。Péronnet 明指這是「過量 CO₂ 可在 P_aCO₂ 不降下就出現」的第一個原因；要到 [[Respiratory compensation point|RC]] 才把旋鈕二也打開，P_aCO₂ 才開始降、窗口關閉。

## 用生活例子再講一次
想像泳池水質開始變酸（過 LT），管理員打開抽風扇把酸氣（CO₂）排掉。在這段期間，他把抽風量調得「剛好等於酸氣產生量」——排掉多少就補多少，所以池邊空氣的酸氣濃度（PCO₂）一直維持不變。這段「邊排邊維持濃度恆定」的從容階段，就是等碳酸緩衝區。直到水質酸到抽風扇得開到最大、瘋狂超抽（過度換氣），空氣酸氣濃度才終於被抽降——那一刻就是 RC，從容窗口結束。

（失準之處：抽風量「剛好匹配」在比喻裡像是有人手動微調；身體裡這是被動的化學-神經回饋自然達成的，不是誰在精算。）

## 換句話說
換句話說，等二氧化碳緩衝區是夾在 [[Lactate threshold|LT]] 與 [[Respiratory compensation point|RC]] 之間、PCO₂ 維持不變的那段強度窗口。它是「真踩到乳酸閾值」的指紋——因為只有乳酸緩衝（而非過度換氣）才能在排掉額外 CO₂ 的同時讓 PCO₂ 不掉。所以它是判定 [[Gas exchange threshold|GET]] 真偽不可或缺的對照。

## 來源
- [[source-Poole-2021-AT-controversy]]（The gas exchange threshold 節：等碳酸緩衝區定義、Fig. 8、作為 LT 偵測依據、缺窗口時的偽閾值與失效情境。）
- [[source-Peronnet-2006-CO2-hyperventilation]]（§9：等碳酸期 V̇CO₂ 上升＝低 pH 把碳酸氫根庫的 CO₂ 頂出（P_aCO₂ 未降），過度換氣尚未上場。對應易誤解 #5。）
