---
type: concept
aliases: [CP與W prime的個體內變異, 臨界功率的日間變異, 個體內變異, intra-individual variability, IIV, day-to-day variability of critical power, CP W prime reliability, CP測量可靠度]
tags: [exercise-physiology, critical-power, methods, measurement, performance]
sources: [source-Sreedhara-2019-power-models-survey]
prerequisites: [Critical power, W prime, 3-minute all-out test, Critical power estimation protocols, Overfitting]
created: 2026-06-12
updated: 2026-06-12
---

# CP 與 W′ 的個體內變異（intra-individual variability, IIV）

## 本質（一句話）
[[Critical power|CP]]和 [[W prime|W′]]不是「量一次就定」的固定身體常數——**同一個人不同天（甚至同一天不同趟）測，數字會擺動**，這叫個體內變異（IIV）；而現有方法給的「標準誤」量的是「這次擬合貼不貼」、不是這種日間擺動，所以要真正抓住 IIV，得在不同天重複測、看數字本身晃多大。

## 前置概念
- [[Critical power|臨界功率（CP）]] 與 [[W prime|W′]]
  （IIV 講的就是這兩個參數的可靠度；先懂它們是什麼。）
- [[Critical power estimation protocols|CP/W′ 的估計協定]]
  （IIV 是「同協定、跨天」的擺動，要和「跨模型/協定」的分歧分清；先懂協定怎麼估。）
- [[3-minute all-out test|三分鐘全力測試（3MT）]]
  （IIV 對 3MT 特別關鍵——單次 3MT 連標準誤都給不出；先懂 3MT 怎麼量。）
- [[Overfitting|過度配適]]
  （順帶懂「標準誤＝貼合度」這層：SEE 是擬合殘差的度量，與 IIV 不同。）

## 為什麼會這樣（first-principles 推導）
1. **先點破一個常見預設。** 我們常把一個人的 CP/W′ 當成「他的身體常數」，量一次就拿去開處方、配速、評估訓練。但**同一個人不同天、甚至同一天不同趟**，測出來的 CP/W′ 會擺動——這叫 **intra-individual variability（IIV，個體內變異）**。它是真實的生理/狀態波動（睡眠、飲食、動機、暖身、設備差異…），不是儀器讀不準。

2. **分清兩種「不確定」（這步是全頁關鍵，放慢）：**
   - **SEE（standard error of estimation，標準誤）**：你用幾個力竭點擬合一條雙曲線，擬合會給每個參數一個標準誤。它量的是「**這條線貼這幾個點貼得好不好**」（goodness of fit，貼合度）。
   - **IIV（個體內變異）**：同一個人**重複整套測試多次**，每次得到一組 (CP, W′)，這些組之間的**跨次擺動**。
   兩者根本不同：SEE 是「一次擬合內部的殘差」，IIV 是「跨測試的真實波動」。一條擬合可以 SEE 很小（點都壓在線上），但這個人改天再測整組數字就跳掉了——**SEE 完全抓不到這個**。綜述的核心觀察是：現有所有方法只給 SEE，**沒有任何一個能量化 IIV**。

3. **那怎麼抓 IIV？得在不同天重複整套測試。**
   - **CWR 版**：每個功率的力竭測試重複多次，各擬合一組 CP/W′，再平均得 grand mean，並看這些組擺動多大（綜述 Fig. 5）。
   - **時間試驗版**：Triska 讓人做 3、7、12 分鐘全力 TT，每種重複三次（含一次熟悉），各算 CP/W′。結果：**CP 的 ICC＝0.95、變異係數 CV＝2.6%；W′ 的 ICC＝0.94、CV＝8.2%**。注意 **W′ 的 CV 是 CP 的三倍多**——W′ 不只跨模型飄（見 [[Critical power estimation protocols]]），跨天也飄得更厲害。

4. **3MT 的 IIV 特別要當心。** 單次 3MT 連 W′ 的 SEE 都給不出來（W′ 是「面積」、不是擬合）。而兩次 3MT 的 Bland-Altman 分析顯示，CP 的 95% 一致界限約 **±15 W**——而 **15 W 的 CP 差，攤到 3 分鐘＝2700 J 的 W′ 差**。所以拿單次 3MT 的 CP/W′ 直接開處方，等於沒把這個擺動算進去。

5. **為什麼這對實務很重要（綜述的論點）：**
   - **評估訓練成效**：你說「訓練後 CP 升了 5 W」，但若光是 IIV 就有 ±15 W，這 5 W 很可能只是噪音。**要先知道 IIV，才知道「真的進步」必須超過多少**。
   - **開處方／配速**：叫人「剛好踩在 CP」，但他的 CP 帶 ±15 W，他可能其實已落在 CP 之上（[[Exercise intensity domains|生理反應完全不同]]）。Burnley 正是在 **CP±15 W**（≈跳出 IIV 範圍）做測試，才看得出「CP 之下穩態 vs CP 之上力竭」的乾淨對比。
   - **個人化模型**：群體平均模型忽略 IIV，無法精準評估個人；綜述因此把「開發能量化 IIV 的方法」列為頭號研究機會。

6. **收束。** CP/W′ 是帶**兩種不確定**的估計：跨模型/協定的分歧（W′ 尤甚，見 [[Critical power estimation protocols]]）＋跨天的 IIV。SEE 只管前者的「貼合度」，至今沒人能常規量化後者。在能可靠量化 IIV 之前，個人化處方與表現最佳化的精度都受限——這是這篇綜述貫穿始終的主旨。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：CP 與 W′ 都帶有個體內的日間變異（IIV），現有方法（CWR 擬合的 SEE、單次 3MT）抓不到它；需要重複測試（或新方法）來量化 IIV，否則訓練成效評估與個人化表現最佳化的精度都受限。
- **背後的推理／證據**：SEE 是「擬合殘差」、IIV 是「跨測試波動」，定義上就不同，所以 SEE 小不蘊含跨天穩定。Triska 重複 TT 的可靠度（CP CV 2.6%、W′ CV 8.2%）與兩次 3MT 的 Bland-Altman（CP ±15 W ⇒ W′ 2700 J）**直接量到**這種波動的大小；而沒有任何現成模型把 IIV 納入參數估計，這就是「需要新方法」的依據。

## 易誤解之處
1. **SEE（標準誤）≠ IIV（個體內變異）。** SEE 小只代表這一次擬合貼得好，不代表這個人改天測還是同一組數字。把 SEE 當成「可靠度」是常見錯誤。
2. **CP/W′ 不是固定身體常數。** 它除了跨模型飄（見 [[Critical power estimation protocols]]），還跨天飄；而且 **W′ 飄得比 CP 更厲害**（CV 8.2% vs 2.6%）。
3. **「訓練後 CP 升了 X 瓦」要先比對 IIV 才算數。** 若 X 落在 IIV 範圍內（如 <±15 W），可能只是當天狀態波動，不是真進步。
4. **單次 3MT 的數字別當鐵。** 它給不出 W′ 的標準誤，且 CP 帶約 ±15 W（≈2700 J W′）的趟間擺動；要更可靠就得重複或改用多趟協定。
5. **IIV 是真實波動，不是「儀器測不準」。** 它來自睡眠、飲食、動機、暖身、纖維狀態等真實因素，是這個人本身的性質，值得被量化，而不是被當成該消去的雜訊。

## 用生活例子再講一次
量體重最好懂。同一個人一天內早晚、餐前餐後體重會差個一兩公斤——這就是 IIV（你的體重本來就在一個範圍內擺動）。而一台體重計的「精度規格（±0.1 kg）」像 SEE：它只說「這台秤這一次讀數穩不穩」，完全沒告訴你「你今天的體重本來就會在一兩公斤內晃」。想知道「我這週是不是真的瘦了」，你不能只看一次讀數，得固定條件、量很多次、看擺動範圍——否則很容易把某天的波動誤當成減重成功。量 CP/W′ 完全一樣：擬合的 SEE 是「秤準不準」，IIV 才是「你本來就會晃多少」，要評估訓練成效得先知道後者。

（這個類比在哪裡會失準：體重 IIV 的來源（水分、食物）相對單純好懂；CP/W′ 的 IIV 來源複雜得多——中樞動機、暖身程度、肌纖維與代謝狀態都會影響，所以更難「固定條件」消去，也更需要專門方法去量化。）

## 換句話說
換句話說，CP 與 W′ 帶著「同一個人跨天會擺動」的個體內變異（IIV），而這和「一次擬合貼不貼」的標準誤（SEE）是兩回事——SEE 小不代表改天測還一樣。要抓 IIV 得重複整套測試（Triska：CP CV 2.6%、W′ CV 8.2%；3MT 兩次 CP 差 ±15 W＝2700 J W′）。這件事直接影響你能不能判斷「訓練真的有效」、能不能精準地把人放在對的強度——在能常規量化 IIV 之前，個人化處方與最佳化的精度都有天花板。這是 [[source-Sreedhara-2019-power-models-survey|本綜述]]反覆強調的核心缺口。

## 來源
- [[source-Sreedhara-2019-power-models-survey]]（Limitations of the Protocols、Research Opportunities（Table 2「Natural variability within an individual」「Influence of mathematical modeling on W′」）與 Conclusions：SEE 量 goodness of fit 而非 IIV、需重複 CWR/TT 求 grand mean（Fig. 5）；Triska 重複 3/7/12 min TT 之 ICC 0.95/0.94、CV 2.6%/8.2%（CP/W′）；3MT Bland-Altman CP ±15 W ⇒ 2700 J W′、單次 3MT 無法得 W′ 標準誤；現有模型皆未納入 IIV，限制個人化處方與表現最佳化。）
