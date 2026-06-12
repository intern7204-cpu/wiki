---
type: concept
aliases: [臨界Pi閾值, 正回饋模型, 臨界閾值與正回饋模型, 運動不耐的臨界閾值模型, critical threshold and positive feedback model, critical Pi model, critical threshold model]
tags: [exercise-physiology, fatigue, VO2-kinetics, model, synthesis]
sources: [source-Goulding-2021-VO2-kinetics-tolerance, source-Goulding-2022-determinants-of-CP]
prerequisites: [氧虧（oxygen deficit, O2 deficit）, 無機磷酸（inorganic phosphate, Pi）與肌肉疲勞, 代謝穩定性（metabolic stability）, 肌肉疲勞（fatigue）與任務失敗（task failure）, VO2 慢成分（VO2 slow component）, 臨界功率／臨界速度（critical power / critical speed, CP/CS）, W′（臨界功率以上的有限功容量）]
created: 2026-06-11
updated: 2026-06-11
---

# 臨界 [Pi] 閾值與正回饋模型（critical threshold and positive feedback model）

## 本質（一句話）
這是本文獻的核心大圖：運動耐受由一條因果鏈決定——**你的 VO2 反應有多快，決定了 Pi 在哪個功率越過「臨界」；一越過，疲勞就觸發一個自我餵養的「效率下降」迴路，產生 VO2 慢成分、定出臨界功率（CP）、並燒掉 W′，直到 Pi 達尖峰、力竭為止。**

## 前置概念
這頁是把前面所有零件組起來的「總成頁」，依賴較多，務必先讀齊：
- [[O2 deficit|氧虧（oxygen deficit, O2 deficit）]]（VO2 慢→借得多→代謝物累積）
- [[Inorganic phosphate|無機磷酸（Pi）與肌肉疲勞]]（累積的代謝物、臨界/尖峰 [Pi]）
- [[Metabolic stability|代謝穩定性（metabolic stability）]]（τVO2 接到臨界閾值的概念橋）
- [[Muscle fatigue|肌肉疲勞（fatigue）與任務失敗（task failure）]]（疲勞當「感測器」）
- [[VO2 slow component|VO2 慢成分（VO2 slow component）]]（迴路的「VO2 臉孔」）
- [[Critical power|臨界功率（CP/CS）]] 與 [[W prime|W′]]（本模型要解釋的兩個既有參數）

## 為什麼會這樣（first-principles 推導）
一步一步把鏈接起來（每一步都連到已建立的頁）：

1. **零件回顧**：[[VO2 kinetics|VO2 動力學]] → [[O2 deficit|氧虧]] → 代謝物（[[Inorganic phosphate|Pi]]）累積 → [[Metabolic stability|代謝穩定性]]。τVO2 愈小＝氧虧愈小＝同功率下 Pi 升愈少＝愈穩定。
2. **臨界閾值**：存在一個「擾動程度」——具體化為**臨界 [Pi]≈18 mM**——是「靜止→運動」轉換時你會停在它之下、還是衝過它的分界。而**你在哪個功率衝過它，由 τVO2 決定**：動力學愈快，能到更高功率才衝過。
3. **肌肉怎麼「知道」自己越線了？**（這是模型最巧妙的一步，放慢看）不是靠什麼 Pi 受器或功率受器——而是靠**疲勞**：Pi 升高造成疲勞（每個橫橋出力變小），而疲勞**逼迫用更多 ATP 周轉去維持同一個功率**（效率下降）。於是**疲勞就扮演了控制迴路裡的「感測器」**：它一出現，就等於通報「臨界閾值被越過了」。
   - 先講「效率」一句 gloss：**運動效率＝每瓦外在功率需要燒掉多少 ATP（W/P）**。效率下降＝同樣瓦數要燒更多 ATP。
   - 疲勞為什麼會連動效率下降（最難的一段，講細一點）：[[Muscle fiber types|Type I 纖維]] 只在**低力量/低速度**時效率最高；當它疲勞、收縮速度被拖慢，它的效率會**掉到比 Type II 還低、甚至趨近零**——肌肉開始「自己對抗自己」。再加上招募更多效率較差的 Type II 纖維。所以「疲勞」與「效率下降」是同一枚硬幣的兩面（Grassi 2015）。
4. **正回饋迴路**：越過臨界 [Pi] → 疲勞 → 更多 ATP 周轉（效率↓）→ 更多 Pi → 更多疲勞 → ……
   - **重度區間（heavy）**：[Pi] 停在「略高於臨界」處；多出來的 ATP 周轉**不足以**讓 Pi 失控 → 迴路**穩下來** → 達到一個（升高的）穩態。
   - **極重度區間（severe）**：[Pi] 持續攀升，迴路以**遞減報酬**自我推進，直到 [Pi] 達**尖峰≈25 mM** → 任務失敗。
   會穩還是會失控，取決於「當下 [Pi] 高出臨界 [Pi] 多少」——這就是 [[Exercise intensity domains|強度區間]] 三段的機制底層。
5. **湧現的結果——這一個機制就長出所有既有參數**：
   - 「剛好還能維持穩定」的那條漸近功率，**湧現**成 [[Critical power|臨界功率（CP）]]。所以 **CP 不是一個基本設定值，而是一個湧現性質**——它是「讓你正好坐在臨界 [Pi] 上」的功率。因此 **CP 受 τVO2 中介**：動力學愈快、CP 愈高。
   - CP 之上，**到達尖峰 [Pi] 的速率**決定可忍受時間；而 CP 之上能做的總功湧現成大致固定的 [[W prime|W′]]（這歸功於第 6 點 Pi 的「遞減報酬」）。效率損失表現成多花的氧，就是 [[VO2 slow component|VO2 慢成分]]。所以**慢成分與 W′ 連動**（慢成分是這個迴路的「VO2 臉孔」）。
6. **由此推出兩個易被忽略的後果**：
   - **CP 不是唯一的功率、也不是唯一的 VO2**，而是「讓你正好達到臨界代謝物累積」的那個點。所以改變效率（例如踩踏頻率），CP 的**瓦數會變、但 CP 處的 VO2 不變**（Barker：不同踏頻 CP 不同、CP 處 VO2 相同）。
   - **間歇運動**可以把尖峰 VO2／Pi 壓在閾值之下而**大幅提高耐受**——功率與代謝負荷被「脫鉤」。極短的工作:恢復比甚至能把波動的 VO2 峰壓在 LT 以下，讓反應變回中等強度的樣子。

## 文獻怎麼說 vs 為什麼這樣說
**這是一個假說／模型，務必把「主張」和「支撐證據」分開看（§11 原則 7）：**
- **主張（假說）**：τVO2 決定運動耐受——它設定「肌肉內代謝物（Pi）累積越過臨界閾值」的功率；一越過，疲勞＋效率損失的正回饋迴路就啟動，產生 VO2 慢成分、並定出 CP 與 W′。
- **支撐證據**：
  1. **電腦模擬（in silico）**：Korzeniewski & Rossiter 的肌細胞生物能模型，用**單一個臨界 [Pi]** 就重現了雙曲線功率-持續時間關係與代謝物／VO2 慢成分；改變供氧也重現預期的 τVO2、CP、耐受變化。
  2. **強相關**：τVO2 與 CP **反相關 R²=0.90**（Murgatroyd，把耐受時間標準化到 6 分鐘後）；VO2 慢成分與 W′ **正相關 R²=0.76**。跨族群（菁英、年長、第一型糖尿病、COPD）關係呈線性。
  3. **急性介入**：在**同一個人**身上加速或減慢 τVO2，CP 就相應上升或下降——而且**有時與送氧改變無關**（如改變基礎功率、prior exercise），證明 τVO2 對 CP 有獨立於送氧的決定作用。
  4. **訓練 vs 未訓練模擬**：同一 ATP 使用率下，未訓練 τ 較慢→出現 [Pi] 慢成分、~8 分力竭；訓練 τ 較快→Pi 穩在臨界之下、呈中等強度行為。
- **狀態**：作者明說這是**需要 in vivo 進一步驗證的假說**，且「單一代謝物」是刻意的簡化（Pi 為 surrogate）。

## 易誤解之處
1. **這是模型／假說，不是已坐實的事實。** 作者自己強調需要更多 in vivo 檢驗。引用時要說「依此模型……」，別當定論。
2. **「單一代謝物 Pi」是替身，不是唯一元兇。** 模型示範的是「一個有致疲勞作用的代謝物越過閾值，就能驅動一整套系統行為」，不是「疲勞只由 Pi 造成」。
3. **CP 是湧現的，不是基本旋鈕；它沒有唯一瓦數或唯一 VO2。** 它是一個「臨界代謝物水準」，透過當下的效率換算成某個功率。改效率，瓦數就變。
4. **快動力學幫忙的方式，不是抬高天花板（VO2max），而是讓你用更小的擾動達到某功率。** 這是和「增加有氧容量」**不同**的一根槓桿——τ 管的是過程，不是上限。
5. **CP 比較像「邊界層」而非剃刀般的閾值。** 模型是單一「嵌合細胞」；真實肌肉是上千條性質連續的纖維，所以 CP 是一段窄的過渡帶（Pethick），整體行為仍與模擬吻合。
6. **若限制其實在別處（呼吸困難、疼痛），尖峰 [Pi] 是力竭的『結果』而非『原因』。** 全身運動還疊加 [[Group III-IV muscle afferents|Group III/IV 傳入神經]] 與通氣／症狀限制。

## 用生活例子再講一次
把它想成一場**債務螺旋**。你的收入在開銷突然跳高時只能慢慢跟上（τ 大＝收入爬得慢）→ 缺口先刷卡墊著（[[O2 deficit|氧虧]]、累積 [[Inorganic phosphate|Pi]]）。只要欠款在某個臨界值以下，你還得起、能穩住（重度）。一旦欠款越過臨界，利息（疲勞）逼你借更多、欠款更高、利息更高……失控（極重度），直到刷爆信用上限（尖峰 [Pi]）、違約（力竭）。**收入爬得愈快（τ 愈小），你能撐起的生活水準愈高（CP 愈高）才開始打螺旋。** 而你刷爆前總共能多花的額度，大致是固定的（[[W prime|W′]]）。

（這個類比在哪裡會失準：金融的利率是人定的、線性的；身體的「利息」是 Pi 對效率的非線性作用（剛越線打擊大、近尖峰遞減），而且這套機制是分子與神經整合的，不是純記帳。類比抓得到「閾值＋正回饋＋固定額度」的骨架，但別把它讀成精確的數字遊戲。）

## 換句話說
換句話說，這個模型把「VO2 動力學」一路接到「為什麼會力竭」：τVO2 設定 Pi 在哪個功率越過臨界；越過後，疲勞當感測器、觸發「效率下降→更多 Pi→更多疲勞」的正回饋——在重度會穩下來、在極重度會跑到尖峰 [Pi] 而力竭。CP、W′、[[VO2 slow component|VO2 慢成分]] 都是這**單一機制湧現**的性質，不是各自獨立的東西。它是個有強力相關與模擬支持、但仍待 in vivo 證實的假說——也是本文獻存在的理由。

## 來源
- [[source-Goulding-2021-VO2-kinetics-tolerance]]（"The critical threshold and positive feedback model"、"Evidence for the critical threshold: τVO2 and critical power"、"Evidence for the positive feedback loop: VO2SC and W'"、整合與結論各節；Figures 2–3；Korzeniewski-Rossiter in silico、Murgatroyd R²=0.90 與 R²=0.76、急性介入、Pethick 邊界層、Group III/IV。）
- [[source-Goulding-2022-determinants-of-CP]]（§3：把 [[Convective oxygen delivery|對流]]／[[Diffusive oxygen transport|擴散]]送氧與 [[VO2 kinetics|τVO₂]] 三條旁路統一接到「臨界 [Pi]」這個共同出口——三者都透過改變起跑時的 Pi 累積速率來決定 CP。）
