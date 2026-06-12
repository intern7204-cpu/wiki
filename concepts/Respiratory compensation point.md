---
type: concept
aliases: [呼吸代償點, 呼吸補償點, 通氣代償點, RC, RCP, RCT, respiratory compensation point, respiratory compensation threshold]
tags: [exercise-physiology, thresholds, ventilation, gas-exchange]
sources: [source-Beaver-1986-V-slope, source-Poole-2021-AT-controversy, source-Peronnet-2006-CO2-hyperventilation]
prerequisites: [無氧閾值（anaerobic threshold, AT）, 二氧化碳輸出量（VCO2, carbon dioxide output）, 分鐘通氣量（minute ventilation, VE）]
created: 2026-06-10
updated: 2026-06-11
---

# 呼吸代償點（respiratory compensation point, RC）

## 本質（一句話）
呼吸代償點是「運動再加重、酸已經堆到緩衝快擋不住時，身體開始**用力猛呼吸**（過度換氣）來把酸壓回去」的那個更高、更靠後的轉折點——它在 [[Anaerobic threshold|無氧閾值]] 之上，是兩個不同的點。

## 前置概念
- [[Anaerobic threshold|無氧閾值（anaerobic threshold, AT）]]
  （RC 是 AT 之後的第二個轉折；先懂 AT 才懂 RC 在它之上「再發生一次什麼」。）
- [[VCO2|二氧化碳輸出量（VCO2, carbon dioxide output）]]
  （RC 是在「分鐘通氣量對 VCO2」的關係上偵測的；先懂 VCO2。）

## 為什麼會這樣（first-principles 推導）
1. 先補一個詞：[[Minute ventilation|分鐘通氣量（minute ventilation, VE）]]＝每分鐘呼進呼出的氣體總量（呼吸深度 × 呼吸次數）。它代表「你呼吸有多用力」。（完整推導見專頁；本頁只需這一句白話定義。）
2. 由 [[Anaerobic threshold|AT]]：越過 AT 後乳酸與酸持續累積，[[Bicarbonate buffering of lactic acid|碳酸氫根]] 一邊中和、一邊被消耗。中和會放 CO₂，而 CO₂ 本身也是酸性的（溶在血裡形成碳酸）。
3. 一開始（AT 到 RC 之間），通氣（VE）大致「跟著」CO₂ 走——產多少 CO₂，就呼掉多少，VE 對 VCO2 幾乎是一條直線，血液酸鹼還勉強守得住。
4. 但強度再上去，酸堆積到緩衝快撐不住、血開始明顯變酸。身體最後一招：**叫呼吸中樞猛拉高通氣**，靠用力呼掉更多 CO₂（CO₂ 是酸）來把 pH 往回扳。這叫「對代謝性酸中毒的呼吸代償」。
5. 這一猛拉，VE 不再只跟著 CO₂ 線性走，而是**相對於 VCO2 額外暴衝**（進入相對過度換氣）。於是在「VE 對 VCO2」的圖上出現第二個拐點——那就是呼吸代償點（RC）。
6. 怎麼抓 RC？和 [[V-slope method|V-slope]] 抓 AT 同一套幾何招式：把 VE-VCO2 資料分兩段線性迴歸，找斜率明顯變陡的轉折（文中門檻：斜率變化 > 起始斜率的 15%）。找到後，把 RC 的位置「轉印」回 VCO2-VO2 圖，當作 AT 迴歸的**上界**——RC 以上的點要排除，免得污染 AT 的判讀。
7. 重要對比：到了 RC 這個相對過度換氣階段，VCO2 就**不再只反映組織端的代謝與緩衝**了（因為呼吸開始主動多排 CO₂）。所以 RC 以下 VCO2 忠實代表代謝事件、RC 以上不再忠實——這正是為什麼 V-slope 偵測 AT 時必須把 RC 以上切掉。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Beaver 等人在 VE-VCO2 圖上分段迴歸偵測 RC（斜率變化 >15%），並指出 RC 一致地高於 AT（10 人平均：RC 對應 VO2 2.51 L/min，AT 1.83 L/min；RC 約落在 VO2max 的 75%、AT 約落在 RC 的 73%）。某些人（如阻塞性肺病患者）可能根本沒有 RC 點。
- **背後的推理／證據**：RC 之所以「在 AT 之上、且機制不同」，是因為 AT 是**代謝/化學**事件（乳酸→緩衝→過量 CO₂），RC 是**通氣/控制**事件（呼吸中樞為壓酸而過度換氣）。文中特別強調：許多舊方法因為依賴通氣反應，常把 RC 誤當成 AT，導致高估——這也是 V-slope（直接抓代謝端的過量 CO₂）更可靠的反證。

## 易誤解之處
1. **RC ≠ AT，這是判讀遞增測試最常見的錯。** AT 在前（乳酸開始堆、過量 CO₂ 冒頭），RC 在後（通氣為代償酸中毒而暴衝）。把兩者混為一談，會把閾值估得太高——文中分析 Green 等人之所以報出偏高的「AT 乳酸值」，很可能就是把部分 RC 點誤判成 AT。
2. **RC 是「呼吸」的轉折，AT 是「代謝」的轉折。** 一個量的是 VE 怎麼變，一個量的是 CO₂ 怎麼產生。機制層級不同，別用同一個原因解釋。
3. **不是每個人都有清楚的 RC。** 通氣反應遲鈍者（阻塞性肺病、化學受器不敏感）可能偵測不到 RC——這同時說明：靠通氣反應定閾值的方法在這些人身上會失效，而 V-slope 不受影響。
4. **RC 之上 VCO2 不再純粹代表代謝。** 因為呼吸開始主動多排 CO₂；這就是 V-slope 要把 RC 以上排除的理由。
5. **RC 標記的「第二個、更高的閾值」，很可能就是 [[Critical power|臨界功率（CP）]] 那條線的通氣版臉孔。** Poole 等人（2021）指出，「重度↔極重度」邊界在文獻裡有一大堆名字——AT₂、乳酸轉折點、RCP/RCT、[[Maximal lactate steady state|MLSS]]、疲勞閾值等——它們很可能指向同一個代謝率，而 CP/CS 是其中最能預測力竭、機制最清楚的描述。所以 RC 不只是「呼吸的轉折」，它在區間框架裡對應的是真正關鍵的高位閾值。
6. **RC 之前那段叫 [[Isocapnic buffering region|等二氧化碳緩衝區]]。** 從 [[Lactate threshold|LT]]（AT）到 RC 之間，通氣已相對 VO2 上升、但血中 PCO₂ 維持恆定——這段窗口的存在正是確認下界閾值是「真乳酸緩衝」（而非過度換氣假象）的依據；RC 就是這段窗口的上端終點。
7. **【機制補充｜Péronnet 2006】RC 也可從「身體 CO₂ 庫見底」來看。** 在 RC，[[VCO2|V̇CO₂]] 不再緊跟 V̇E（通氣當量 V̇E/V̇CO₂ 開始上升）。Péronnet 指出這個脫鉤反映 [[Body CO2 stores|身體碳酸氫根庫]]被洩到底——即使 P_aCO₂ 與 pH 已低，也再榨不出更多庫存 CO₂。這與「V̇E 為壓酸而暴衝」是同一現象的兩面（呼吸催更大、但可放的庫存 CO₂ 已枯）；同樣的 V̇CO₂–V̇E 脫鉤也出現在固定高強度久撐時。

## 用生活例子再講一次
延續「泳池變酸、管理員撒小蘇打中和」的比喻：撒小蘇打（緩衝）能擋一陣子，泡沫（CO₂）穩定地冒，管理員還從容（AT 到 RC 之間，VE 跟著 CO₂ 走）。但酸繼續加重、小蘇打快用完、水質明顯變酸時，管理員只好打開大型抽風機猛抽氣、瘋狂換水（猛拉高通氣）——這個「從從容轉成手忙腳亂狂抽風」的時刻，就是呼吸代償點。它明顯發生在「開始冒泡沫」（AT）之後。

（失準之處：抽風機是外加裝置，身體的「過度換氣」是同一套呼吸系統把輸出開到更大；而且有些系統根本沒有這台抽風機，對應到「某些人沒有 RC 點」。）

## 換句話說
換句話說，呼吸代償點是「身體開始拼命多呼吸來壓酸」的那個更高強度轉折。在它之前，呼吸還只是乖乖把代謝產的 CO₂ 排掉；過了它，呼吸變成主動的滅火工具，相對於 CO₂ 暴衝。因為它在 [[Anaerobic threshold|AT]] 之後、機制又不同，偵測 AT 時一定要把 RC 以上切掉——這也是 [[V-slope method|V-slope 方法]] 流程裡先找 RC、再回頭定 AT 的原因。

## 來源
- [[source-Beaver-1986-V-slope]]（Fig. 2B、結果與 Table 2：以 VE-VCO2 分段迴歸偵測 RC，RC 一致高於 AT，並作為 V-slope 偵測 AT 的上界。）
- [[source-Poole-2021-AT-controversy]]（等碳酸緩衝區定義、RCP/RCT 作為 heavy-severe 邊界（≈CP）眾多別名之一。）
- [[source-Peronnet-2006-CO2-hyperventilation]]（§8：RC 處 V̇CO₂–V̇E 脫鉤＝身體碳酸氫根庫耗竭，無法再從碳酸氫根釋放 CO₂。對應易誤解 #7。）
