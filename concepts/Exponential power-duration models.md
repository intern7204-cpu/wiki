---
type: concept
aliases: [指數型功率持續時間模型, 指數功率時間模型, 指數型表現模型, exponential power-duration models, exponential performance models, Ward-Smith model, Peronnet-Thibault model, Weyand model, 全曲線模型]
tags: [exercise-physiology, critical-power, modelling, performance, endurance]
sources: [source-Sreedhara-2019-power-models-survey]
prerequisites: [Critical power, W prime, Time constant, VO2max]
created: 2026-06-12
updated: 2026-06-12
---

# 指數型功率–持續時間模型（exponential power–duration models）

## 本質（一句話）
這是一整類「不用雙曲線、改用**指數衰減函數**去描述整條功率–時間曲線」的模型——功率從一個**有限**的最大值隨時間平滑衰減到一個可持續基準；它們一口氣補掉兩參數 [[Critical power|CP]]模型的兩個破綻（短衝刺端 P 不再無限、也不假設 CP 能永遠維持），常用來預測從短跑到馬拉松的成績。

## 前置概念
- [[Critical power|臨界功率（critical power, CP）]] 與 [[W prime|W′]]
  （指數模型是兩參數雙曲線的替代方案；先懂雙曲線的兩個參數與它的破綻。）
- [[Time constant|時間常數 τ]]
  （指數衰減「快慢」用 τ（或衰減率 k＝1/τ）描述；先懂指數逼近與 τ。）
- [[VO2max|最大攝氧量（VO2max）／最大有氧功率（MAP）]]
  （這些模型的「可持續下漸近線」常等同最大有氧功率（MAP）；先懂 VO2max/MAP 是有氧上限。）

## 為什麼會這樣（first-principles 推導）
1. **先點出兩參數模型的兩個破綻。**
   - **破綻①**：t→0 時 P→∞（已由 [[Three-parameter critical power model|三參數模型]]加一個 Pmax 漸近線修掉一種）。
   - **破綻②**：它假設 [[Critical power|CP]] 能**無限**維持，但實證上 CP 大約只能撐**不到一小時**（呼應 durability、[[Power-duration relationship plasticity|可塑性]]）。

2. **另一條路：不修雙曲線，整條改用「指數衰減」描述。** 直覺是「功率從一個最高值，隨時間指數地掉向一個可持續基準」。一般形式：
   $$P(t) = P_{\text{aer}} + (P_{\max} - P_{\text{aer}}) \cdot e^{-k \cdot t}$$
   - **P_aer**（≈CP 或最大有氧功率 MAP）：有氧能撐住的可持續功率，是指數的**下漸近線**。
   - **P_max**：t＝0 的瞬間最大功率——**有限**，自動補掉破綻①。
   - **k**（或 τ＝1/k）：功率隨時間衰減的快慢（[[Time constant|時間常數]]）。

3. **這族模型的成員，其實是同一個指數形式的變體：**
   - **Ward-Smith（1985）**：從**熱力學第一定律**出發，把功率拆成無氧項（指數衰減）＋有氧項（恆定 R，類比 CP），預測 100 m–10,000 m 徑賽。
   - **Hopkins**：跑步機**坡度**版 I_t ＝ I_∞ ＋ (I_0−I_∞)·e^(−t/τ)，與上式同構（I_∞ 類比 CP、I_0 類比 Pmax）。
   - **Weyand**：全力騎車 3–300 s，P(t) ＝ P_aer ＋ (P_mech max − P_aer)·e^(−k·t)。
   - **Morton 指數版**：全力跑步 P(t) ＝ CP ＋ (P_max − CP)·e^(t/k)。
   把衰減常數取倒數、變號，這幾個式子可以互相轉換——它們是「同一個指數骨架」的不同寫法。

4. **Péronnet-Thibault（更精緻，直接處理破綻②）。** 為預測 **60 m 到全程馬拉松**，它的關鍵假設是「最大有氧功率（[[VO2max|MAP]]）只能維持約 **7 分鐘**（T_MAP≈420 s），而非無限」；超過 T_MAP 後，**有氧與無氧能力都隨 ln(時間) 下降**。它把無氧容量 A、MAP、衰減項 E 等拆開建模，能估世界紀錄成績到**平均絕對誤差 0.73%（男）／1.27%（女）**。「MAP 撐不過幾分鐘、之後隨距離衰退」正是兩參數「CP 無限」假設的修正。

5. **共同優點。** 比兩參數模型**更準**，尤其在「極短的衝刺端」（有限 Pmax）與「極長的耐力端」（可持續功率會衰退），因為它們天生 bound 住 Pmax、又不假設 CP 無限。

6. **共同代價。** 參數多很多——要假設或估 P_max、MAP、無氧容量 A、衰減 E、T_MAP、k 等。模型一複雜，這些參數就**難以只靠一支功率計的資料估出來**，野外實用性下降（這正是 [[Phenomenological vs mechanistic models|精簡性 vs 準確度的張力]]：多塞參數更準、卻更難用）。

7. **和雙曲線家族的座標不同：指數模型給不出乾淨的 W′。** 它不用「曲率常數 W′」描述曲線，而是用「振幅 (P_max − P_aer) ＋ 衰減 τ」這組參數。所以把指數模型套到同一筆資料，會得到 CP/Pmax，但 **W′＝NA**（無對應項）——它和 CP/W′ 不是同一套參數系統。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：用指數衰減函數描述整條功率–時間（或速度–時間）曲線，能更準地預測極短到極長距離的成績，並天生 bound 住最大瞬間功率、不假設可持續功率能永遠維持（Péronnet-Thibault 更明確讓 MAP 只撐 ~7 min 後衰退）。代價是參數比兩參數模型多得多。
- **背後的推理／證據**：指數函數天生有「有限的 t＝0 值」與「有限的下漸近線」，剛好對應 Pmax 與可持續功率兩個生理事實，所以在曲線兩端比雙曲線真實。Péronnet-Thibault 能把世界紀錄估到 <1.3% 誤差，是「整條曲線指數描述＋MAP 會衰退」這套假設的有力支持；但同一篇也指出 A、MAP、E 等參數的決定與 BMR、T_MAP 等假設值是其主要限制——準確是用參數數量換來的。

## 易誤解之處
1. **指數模型不是雙曲線的小修，而是換一族函數。** 它通常**給不出乾淨的 W′**（Table 1 裡指數模型 W′＝NA）；別預期能像兩參數那樣讀出一個 W′。
2. **「更準」是用「更多參數」換來的，不等於更懂機制。** 這些多半是現象學或半機制模型（見 [[Phenomenological vs mechanistic models]]）；擬合漂亮不證明抓到了因果。
3. **各模型的「有氧漸近線」（P_aer / R / I_∞ / MAP）與 [[Critical power|CP]] 概念相近，但不必數值相等。** 各自定義與量法不同，別把它們當同一個數。
4. **Péronnet-Thibault 的「MAP 只撐 ~7 分鐘」是個假設參數（T_MAP≈420 s），不是量出來的鐵則。** 它讓模型在超長距離端更真實，但本身是設定值，換個假設結果就會變。

## 用生活例子再講一次
想像手機的放電能力曲線。兩參數模型像在說兩件怪事：「用極短的時間，可以放出無限大的瞬間電流」、又「某個低電流可以永遠用下去」。真實電池比較像指數模型：可放出的功率從一個**有限的峰值**隨時間平滑衰減，掉向一個**較低、可長時間維持**的水平——而且連那個「可持續水平」也撐不了真正的無限久。指數型功率模型，就是用這種「從有限峰值平滑衰減到（會慢慢退的）可持續基準」的曲線，去更真實地描述人從短跑到馬拉松的輸出。

（這個類比在哪裡會失準：電池的放電曲線由電化學決定、相對固定；人的功率–時間曲線會隨訓練、疲勞、運動型態（跑/騎/划）大幅改變，而且還有 [[Power-duration relationship plasticity|可塑性]]——同一個人不同狀態的曲線都不一樣，比電池複雜得多。）

## 換句話說
換句話說，指數型功率–持續時間模型是「用指數衰減函數描述整條 P–t 曲線」的一族模型（Ward-Smith、Hopkins、Weyand、Morton 指數版、Péronnet-Thibault）：功率從有限的 [[Three-parameter critical power model|Pmax]] 平滑衰減到可持續基準（≈[[Critical power|CP]]/[[VO2max|MAP]]）。它們同時補掉兩參數模型的兩個破綻（短端 P 無限、CP 假設無限），能更準預測短跑到馬拉松的成績；代價是參數多、難從現場資料估出，而且**給不出乾淨的 [[W prime|W′]]**——是與 CP/W′ 並列、但座標不同的另一套描述。

## 來源
- [[source-Sreedhara-2019-power-models-survey]]（Modeling Performance Using Power 節 eq.6–8、12–13：Ward-Smith（熱力學第一定律、無氧指數＋有氧 R，100 m–10,000 m）、Hopkins（坡度版 eq.7）、Péronnet-Thibault（eq.8，60 m–全馬、MAP 僅撐 ~7 min（T_MAP≈420 s）、超過後有氧/無氧隨 ln(T) 衰退、世界紀錄誤差 0.73%/1.27%）、Weyand（eq.12，全力騎車 3–300 s）、Morton 指數版（eq.13）；這些式子可互相轉換（k 取倒數變號）；Table 1 顯示指數模型給出 CP/Pmax 但 W′＝NA；alternate 模型更準但參數多、複雜度高。）
