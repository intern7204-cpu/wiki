---
type: concept
aliases: [VO2慢成分, 攝氧量慢成分, 耗氧量慢成分, 氧耗慢相, VO2 slow component]
tags: [exercise-physiology, VO2-kinetics]
sources: [source-Gaesser-1996-slow-component, source-Poole-2021-AT-controversy, source-Poole-2016-critical-power, source-Goulding-2021-VO2-kinetics-tolerance, source-Skiba-2014-work-recovery-durations, source-Korzeniewski-2015-VO2-slow-component-mechanisms, source-Burnley-2011-priming-power-duration, source-Ventura-2023-severe-extreme-tolerance, source-Goulding-2023-priming-VO2-kinetics, source-Ma-2010-VO2-kinetics-equation-clarification]
prerequisites: [耗氧量（VO2, oxygen uptake）, 運動效率（exercise efficiency / economy）, 肌纖維類型（muscle fiber types）, 運動單位招募（motor unit recruitment）]
created: 2026-06-10
updated: 2026-06-12
---

# VO2 慢成分（VO2 slow component）

## 本質（一句話）
VO2 慢成分就是「強度夠高時，固定不變的運動負荷下，耗氧量**不肯停在預期的穩定值、反而繼續慢慢往上漂**的那一段額外攝氧」——它代表運動變得愈來愈「不划算」（[[Exercise efficiency|效率]]在掉）。

## 前置概念
- [[VO2|耗氧量（VO2, oxygen uptake）]]
  （慢成分是 VO2 隨時間變化的一種行為；先懂 VO2 是什麼、怎麼隨強度走。）
- [[Exercise efficiency|運動效率（exercise efficiency / economy）]]
  （慢成分的本質就是「每瓦的氧價上漲、效率下滑」；先懂效率＝每瓦攝氧成本。）
- [[Muscle fiber types|肌纖維類型（muscle fiber types）]]
  （慢成分最被看好的機制是「招募效率較差的 Type II 纖維」；先懂纖維分型與招募。）

## 為什麼會這樣（first-principles 推導）
1. 先看「正常」情況：在**中等強度**下給一個固定負荷，[[VO2|VO2]] 會在約 2–3 分鐘內快速爬到一個穩定值，然後就**穩住不動**——身體找到了「這個負荷需要這麼多氧」的穩態。這種乾淨、單一指數式的上升，叫「快成分」。
2. 但把強度拉到**重度**（heavy）以上、同樣維持固定負荷時，會多出一個現象：VO2 到了原本該穩住的時間點，卻**沒穩住，而是繼續以較慢的速度往上漂**。這多出來、遲來的一段攝氧，就是「VO2 慢成分」。文獻上把它精確定義為「**運動第 3 分鐘之後仍持續上升的那部分 VO2**」，且通常在運動開始後 **80–110 秒**才疊加上來。
3. 為什麼會漂上去？因為同一份外在功率，身體愈做愈「貴」——需要動用效率較差的肌纖維、招募更多運動單位、維持離子與代謝平衡的額外成本上升，於是「產生同樣的功」要燒掉愈來愈多的氧。換句話說，**[[Exercise efficiency|運動經濟性]]在變差**：中等強度時每瓦約 9–11 mL O₂/min，跨過閾值後這個成本顯著上升。
4. 關鍵分界：慢成分**只在超過 [[Lactate threshold|乳酸閾值]]（T_Lac）的強度才出現**，與「絕對代謝率多高」無關。所以「有沒有慢成分」本身就成了一個辨別運動強度區間的指標——它是 [[Exercise intensity domains|重度區間]] 的招牌特徵之一。Henson 等人用不同體能的人證明了這點：對體能差的人，75 W 已在 T_Lac 之上、出現慢成分；對體能好的人同樣 75 W 仍在 T_Lac 之下、沒有慢成分。
5. 兩個區間的不同命運（這裡放慢，是最容易混的地方）：
   - **重度（heavy，T_Lac ~ 功率-時間漸近線 W_a）**：慢成分在運動早期（約第 3–10 分鐘）發展最快，但**最終會在約 20 分鐘內趨於穩定**，VO2 停在一個升高的次大值（約 60–85% VO2max），運動可持續相當久。
   - **極重度／嚴重（severe，> W_a）**：慢成分**不再趨於停止，而是一路把 VO2 推到最大值（[[Critical power|臨界功率]] 之上）**，與乳酸的一路上升、力竭同步發生。極端情況下，這份「額外的」VO2 可達 **1.0–1.5 L/min**。
6. 它在哪裡產生？同時量「肺 VO2」與「腿 VO2」的實驗顯示，第 3 分鐘以後 VO2 增量的 **約 86% 來自運動中的腿本身**。所以慢成分主要是**運動肌肉內部**的事，呼吸肌、心臟等肢體外的器官只佔小部分。

### 慢成分是正回饋迴路的「VO2 臉孔」（Goulding 2021）
7. 把慢成分接到機制上：當功率越過 [[Inorganic phosphate|臨界 [Pi]（≈18 mM）]]，疲勞觸發一個「效率下降 → 多燒 ATP → 更多 Pi → 更多疲勞」的 [[Critical Pi threshold and positive feedback model|正回饋迴路]]。慢成分就是這個迴路**多花的氧的可見表現**——效率損失（每瓦要燒更多 ATP）直接讓 VO2 在固定功率下繼續漂升。
8. 一個關鍵的時序證據：**疲勞先出現，慢成分才跟著冒出來**（Cannon 2011：肌肉疲勞先於慢成分），且疲勞大小與慢成分振幅相關——這支持「疲勞當感測器、觸發效率損失」，而不是「慢成分自己憑空發生」。於是慢成分與 [[W prime|W′]] 的正相關（R²≈0.76）有了機制解釋：兩者都是同一個正回饋迴路的產物。

### 肌內生物能量學機制：無氧供應下滑，缺口轉嫁給有氧（Korzeniewski 2015）
8b. 上面（第 7–8 點）說「效率下降→多燒 ATP→VO2 漂升」，但**為什麼**重度運動下效率會下降、有氧為什麼非得多做工？Korzeniewski & Zoladz 用一個含無氧醣解的骨骼肌生物能量學電腦模型（in silico）給出肌內層級的因果：重度運動裡無氧醣解被自己累積的酸踩慢（[[Proton inhibition of glycolysis|質子抑制醣解]]）、[[Creatine kinase equilibrium|CK]] 供能也緩降，這兩條無氧 ATP 來源的缺口，依「ATP 產生＝ATP 消耗」鐵律由 [[Mitochondrial respiratory control|有氧 OXPHOS]] 接手（ADP/Pi 升高催快粒線體）→ VO2 在固定功率下續漲。疲勞造成的「同功多耗 ATP」（用量端效率損失）再放大它。完整推導與三個反直覺推論（慢成分大小 ∝ 醣解被抑制的程度而非絕對酸度；乳酸是標記非肇因；**不必招募新纖維**即可生成慢成分）見 [[Bioenergetic mechanism of the VO2 slow component|VO2 慢成分的生物能量學機制]]。這條機制與下面（第 5 點成因分析）的「乳酸相關非肇因」「不必額外招募纖維」結論一致，但補上了「為什麼」。

### 起始 VO2 愈低，可用的 W′ 愈多（Skiba 2014）
9. 把慢成分的觀念用在**間歇運動**上，會冒出一個實用的量：當你做完一段間歇、緊接著要做定功率運動時，你**進入這段定功率那一刻的 VO2（VO2start）**已經被前面的間歇墊高了多少？墊得愈高，代表慢成分／VO2 漂升已經吃掉一塊「離 VO2max 的距離」。把這段剩餘距離記成 D_VO2 ＝ VO2peak − VO2start（你還能往上漲的空間）。
10. Skiba 2014 量到：**D_VO2 與後續定功率運動可用的 [[W prime|W′]] 線性正相關（r＝0.79、r²＝0.63）**——也就是**進入時的 VO2 基準愈低（D_VO2 愈大），後面能掏出來的 W′ 就愈多**。為什麼？因為 VO2start 低代表慢成分還沒怎麼發展、效率還沒掉、那個「效率損失↔疲勞」的正回饋迴路還沒被點燃，於是 CP 以上的備用功容量還留得比較完整。這把第 7–8 點的「慢成分＝正回饋迴路的 VO2 臉孔」從連續運動延伸到間歇：**間歇切得愈碎、VO2 漂得愈少→W′ 留得愈多**（接 [[W prime reconstitution|回填]] 第 10 點與 [[Priming effect|預熱效應]]）。注意 Skiba 的散點（圖 5）有一個離群點可能讓回歸線被槓桿放大，作者自陳此點。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Gaesser 與 Poole 主張，「VO2 隨功率線性升到最大」是教科書的**迷思**——這只在乳酸閾值以下成立；閾值之上會疊加一個慢成分，代表「超出 sub-T_Lac 能量學所預測值」的**額外能量需求**。後續 Poole 等人進一步用慢成分界定運動強度區間（中等：快速單指數、乳酸不升；重度：出現慢成分、放大振幅、拖慢反應、降低效率、乳酸升高）。
- **背後的推理／證據（最該放慢的「成因」分析）**：作者逐一檢查被提出的機制，得到一個「相關但非肇因」的清單——
  1. **乳酸／酸中毒：相關，但不是肇因。** 慢成分大小雖與血乳酸上升高度相關，但多條證據反駁因果：注腎上腺素可大幅升乳酸卻不改 VO2；把 L-乳酸灌進電刺激的狗肌使肌肉乳酸 >9 mM，VO2 仍不升；跑步時可見明顯慢成分而血乳酸幾乎不變。所以乳酸是**伴隨現象**，不是原因。
  2. **通氣（呼吸肌做功）：佔比小（約 ~23%）。** 重度運動通氣可增 20–60 L/min，依每升氧成本估算，只能解釋慢成分的兩成多。
  3. **腎上腺素：基本排除。** 把腎上腺素灌到超大運動的血中濃度，VO2 不受影響；β-阻斷也不削減慢成分。
  4. **溫度（Q10 效應）：有爭議，傾向排除。** 理論上肌溫升 1°C 可佔不少，但實測到肌溫上升而腿 VO2 不變、升體溫不增肺 VO2 的反例。
  5. **鉀離子：時間對不上。** 血鉀在運動最初升一下就穩了，而 VO2 還在繼續漲。
  6. **[[Motor unit recruitment|運動單位招募]]（最被看好的機制）：招募效率較差的快縮（[[Muscle fiber types|Type II]]）纖維。** iEMG 隨第 4–7 分鐘 VO2 一起上升；Type II 纖維比例愈高者踩車 VO2 成本愈高、[[Exercise efficiency|效率]]愈低；快縮纖維本就較不經濟、VO2 動力學較慢。把「效率下降」直接連到「被迫拉進效率差的纖維」。Goulding 2023 補上證據深度與限制：預熱使次輪頭 2 min iEMG ↑~19%（Burnley 2002）、³¹P-MRS 顯示氧化 ATP 成本↑而 PCr/醣解供能↓（Layec），但也有研究未見 iEMG 變化，加上雙極表面 EMG 取樣小、訊號相消無法精確還原招募——故「招募改變」**有支持但未完全釘死**，完整機制與限制見 [[Motor unit recruitment]]。
- **訓練的影響**：耐力訓練會**加快運動起始的 VO2 動力學**，並**壓低慢成分**——且這個適應**在頭 2 週內就出現**，之後幾週不再顯著進步。機制未定，但同樣最可能是「招募較少快縮纖維／招募氧化能力較高的快縮纖維」加上各型纖維粒線體含量增加。降乳酸、降通氣都被證明**不是**主因（訓練後即使用注腎上腺素把乳酸補回去，VO2 也不變）。
- **臨床應用**：對 VO2max 或最大通氣（MVV）有不可逆天花板的病人（心臟或通氣受限），提升表現的唯一辦法是**把 T_Lac 往上推、縮小慢成分**——讓 VO2-功率關係在更大的功率範圍維持線性、降低 >T_Lac 的氧（與通氣）需求。

## 易誤解之處
1. **慢成分不是「還沒到穩態」。** 中等強度也要花 2–3 分鐘到穩態，但那之後就穩了。慢成分是「過了該穩的時間（第 3 分鐘後）還在漲」，是額外、性質不同的一段，不是單純反應慢。
2. **它不是「O₂ drift」。** 長時間中等運動會見到的緩慢 VO2 上漂（< ~200 mL、乳酸不升）是另一回事；慢成分量值大得多、只在 >T_Lac 出現，且是受控的規律過程，不該叫「drift（漫無方向的漂移）」。
3. **它代表效率變差，不是體能變好。** 同樣功率卻要燒更多氧，是壞消息（更累、更撐不久），不是有氧能力提升。
4. **乳酸是「相關」不是「肇因」。** 慢成分與乳酸時間軸貼合，很容易誤判成乳酸造成 VO2 上升；實驗證據（見上）反駁了因果。
5. **慢成分不一定來自「額外招募新纖維」。** 在纖維一開始就全被招募的情況（電刺激狗肌、[[3-minute all-out test|3 分鐘全力測試]]）仍有大慢成分——所以除了招募，還有**纖維內效率下降**等其他來源。Korzeniewski 2015 的 in silico 模型進一步證明：光靠「醣解被酸抑制＋既working纖維效率下降」就足以生出慢成分，**招募 Type II 纖維非必要條件**（見 [[Bioenergetic mechanism of the VO2 slow component|機制頁]]）。這與 Gaesser 1996 把成因主要歸於 Type II 招募的側重不同——兩說並存：招募**可以**貢獻、但非必要。
6. **慢成分大小與 [[W prime|W′]] 正相關。** 慢成分愈大、W′ 愈大，暗示「效率損失」與「疲勞發展、力竭」之間有內在連結——這是把 W′ 從「純儲備能」重新理解為「整合生物能系統一環」的證據之一。
8. **強度高到 [[Extreme intensity domain|extreme（極限強度）域]]時，慢成分「來不及發展」，VO2 反而到不了頂。** 慢成分通常要運動開始後 80–110 秒才疊加上來、再花時間把 VO2 推向 [[VO2max|VO2max]]。但過了 [[Maximal intensity for VO2max attainment|IHIGH]] 的 extreme 域，力竭來得太快（可能就在這個時間量級內），慢成分**沒有時間充分發展**，於是 VO2 還沒爬到頂運動就結束——這正是 extreme 域「達不到 VO2max」的成因（Ventura 2023）。所以「慢成分把 VO2 推到 VO2max」這個 severe 域的招牌劇情，在更高的 extreme 域反而**演不完**。
9. **慢成分在標準擬合式裡就是「第三段指數（A₂ 項）」。** 把整條 VO2 上升寫成可擬合的數學式時，慢成分對應 Barstow/Scheuermann 模型的第三項 $A_2[1-e^{-(t-TD_2)/\tau_2}]$——A₂ 是慢成分振幅、τ₂ 是它的時間常數、TD₂ 是它約 80–110 s 才登場的那個時間延遲。要注意這條式子須寫成**分段**（慢成分項在 TD₂ 之前嚴格為 0）才符合本意，否則三項相加只是一條平滑曲線、慢成分項在登場前甚至取負值（見 [[Multi-exponential model of VO2 kinetics|多指數模型]]）。
10. **「慢成分振幅（amplitude）」是個被混淆的指標——severe 運動下要看「軌跡（trajectory）」（Burnley 2011）。** 力竭型 severe 運動裡，慢成分振幅＝VO2peak − primary 振幅，所以它**同時被 primary 振幅與 VO2peak 牽動**：若某介入（如[[Priming effect|預熱]]）把 primary 振幅抬高、而 VO2peak 不變，慢成分振幅**必然**變小——但這純粹是算術，**不代表「效率損失」真的少了**。Burnley 2011 量到：表現提升有時伴隨慢成分振幅**沒**降（只降了軌跡）；而慢成分振幅降低也**不**保證表現變好。所以「慢成分振幅小＝效率好＝表現好」是錯的直覺。**慢成分的軌跡（每分鐘漲多少，L·min⁻²）才較能反映「效率損失的速率」**，因為它不依賴 primary 振幅或 VO2peak 的絕對值。（但軌跡也有前提：它假設慢成分隨時間近似線性，實際多為非線性，故只能當「速率指標」而非精確值。）

## 用生活例子再講一次
想像你用固定速度推一台購物車。路面平整時（中等強度），推一陣子就進入省力的巡航狀態，每分鐘耗的力固定。但若路面是濕沙（重度強度），即使你維持同樣速度，輪子愈陷愈深，你得愈出愈多力才維持得住——每分鐘的耗力不再固定，而是緩緩往上爬。那段「明明速度沒變、力氣卻一直多花」的漂移，就是 VO2 慢成分。

（失準之處：濕沙是外在阻力變大；慢成分主要來自身體內部效率下降（肌纖維招募、代謝成本），外在功率其實沒變。）

## 換句話說
換句話說，VO2 慢成分是「固定負荷下，耗氧量該停卻不停、繼續往上漂」的現象，精確地說是「第 3 分鐘之後仍持續上升的那段 VO2」。它只在超過 [[Lactate threshold|乳酸閾值]] 後冒出來，約 86% 產生在運動的肌肉裡，是 [[Exercise intensity domains|重度以上強度]] 的指紋，反映運動正變得愈來愈不划算（[[Exercise efficiency|效率]]掉）。在重度它最終會穩住、在 [[Critical power|臨界功率]] 之上則會把 VO2 一路逼到極限。它最被看好的成因是招募效率較差的 [[Muscle fiber types|Type II 纖維]]；乳酸、通氣、腎上腺素、溫度、鉀都被檢查過，多屬伴隨而非肇因。

## 來源
- [[source-Gaesser-1996-slow-component]]（旗艦綜述：定義（>第3分鐘、僅>T_Lac）、歷史（Åstrand & Saltin 1961；非"O₂ drift"）、heavy vs severe 命運、~86% 來自腿、成因逐項分析（乳酸相關非因、通氣~23%、腎上腺素/鉀/溫度排除、快縮纖維招募為主）、訓練 2 週內衰減、臨床應用、極端可達 1.0–1.5 L/min。）
- [[source-Poole-2021-AT-controversy]]（Common threshold concepts：moderate vs heavy 的 VO2 動力學差異；Coincidence 節 Fig. 13 >CP 時 VO2 趨向 VO2max。）
- [[source-Poole-2016-critical-power]]（慢成分=效率損失、與 W′ 正相關、不必靠額外纖維招募、>CP 驅 VO2 至 VO2max。）
- [[source-Goulding-2021-VO2-kinetics-tolerance]]（慢成分為正回饋迴路的「VO2 臉孔」、疲勞先於慢成分（Cannon 2011）、與 W′ 正相關 R²=0.76 的機制解釋。）
- [[source-Skiba-2014-work-recovery-durations]]（推導第 9–10 點：間歇後定功率運動的 D_VO2＝VO2peak−VO2start 與可用 W′ 線性相關 r=0.79、r²=0.63（Fig 5，含單一離群點）；VO2start 愈低＝W′ 儲備愈多；把 VO2SC↔W′ 關係延伸到間歇情境，呼應「最小化 baseline VO2 以保留 W′」。）
- [[source-Burnley-2011-priming-power-duration]]（易誤解 #7：慢成分振幅＝VO2peak−primary 振幅，被 primary 振幅與 VO2peak 連動而易誤導；severe 運動下軌跡（L·min⁻²）才是有意義的指標、但假設近似線性；降低慢成分振幅既非表現提升的必要也非充分條件。）
- [[source-Korzeniewski-2015-VO2-slow-component-mechanisms]]（推導第 8b 點與易誤解 #5：in silico 肌內機制——醣解被酸抑制＋CK 緩降→缺口由 OXPHOS 補→VO2 漂升；額外 ATP 用量放大；不必招募 Type II（離體狗肌證據）；慢成分 ∝ 醣解抑制程度而非酸度；乳酸標記非肇因。完整見 [[Bioenergetic mechanism of the VO2 slow component]]。）
- [[source-Ventura-2023-severe-extreme-tolerance]]（易誤解 #8：慢成分 80–110 s 才疊加，[[Extreme intensity domain|extreme 域]]力竭太快使其來不及發展、VO2 達不到 VO2max——extreme 域「達不到 VO2max」之成因。）
- [[source-Goulding-2023-priming-VO2-kinetics]]（成因分析第 6 點補充：運動單位招募證據深度（Burnley 2002 iEMG ↑~19%、Layec ³¹P-MRS＋EMG）與雙極 EMG 的解讀限制；招募改變為「有支持但未釘死」的慢成分/預熱機制，詳見新頁 [[Motor unit recruitment]]。）
- [[source-Ma-2010-VO2-kinetics-equation-clarification]]（易誤解 #9：慢成分＝Barstow/Scheuermann 擬合式的第三段指數 A₂ 項（振幅 A₂、時間常數 τ₂、時間延遲 TD₂≈80–110 s）；該項須分段（TD₂ 前嚴格為 0）才合本意，詳見 [[Multi-exponential model of VO2 kinetics]]。）
