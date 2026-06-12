---
type: concept
aliases: [微血管氧分壓, 微血管氧輸送, 氧供需比, QO2/VO2, PmvO2, 肌肉血流分配, microvascular O2 delivery, microvascular PO2]
tags: [exercise-physiology, vascular, muscle, mechanism]
sources: [source-Poole-2016-critical-power, source-Goulding-2021-VO2-kinetics-tolerance, source-Goulding-2022-determinants-of-CP, source-Goulding-2023-priming-VO2-kinetics]
prerequisites: [耗氧量（VO2, oxygen uptake）, 肌纖維類型（muscle fiber types：Type I / Type II）]
created: 2026-06-10
updated: 2026-06-11
---

# 微血管 O₂ 輸送（microvascular O₂ delivery：QO₂/VO₂ 與 PmvO₂）

## 本質（一句話）
這講的是「肌肉每一小區，氧氣**送進來的速率（QO₂）**和**用掉的速率（VO₂）**之間的比值，決定了該區微血管的氧分壓（PmvO₂）——而這個壓力，掌控著肌肉細胞拿不拿得到足夠氧、進而影響它撐多久」。

## 前置概念
- [[VO2|耗氧量（VO2, oxygen uptake）]]
  （VO₂ 是「用氧速率」這一端；先懂它。）
- [[Muscle fiber types|肌纖維類型（Type I / Type II）]]
  （不同纖維型的供需比與氧分壓差很多；先懂纖維分型。）

## 為什麼會這樣（first-principles 推導）
1. 任何一小塊運動中的肌肉，氧氣有兩股流：**供給 QO₂**（血流把含氧血送進來的速率）與**消耗 VO₂**（粒線體用掉氧的速率）。兩者的比值 **QO₂/VO₂** 決定了組織端還「剩多少氧」——也就是微血管氧分壓 PmvO₂。
2. 直覺：供給相對消耗愈足（QO₂/VO₂ 高）→ PmvO₂ 高 → 血液到細胞的氧氣壓力梯度大 → 細胞容易拿到氧。反之比值低 → PmvO₂ 低 → 細胞拿氧吃緊。（這是 Fick 定律：氧通量正比於壓力梯度。）
   - 把運送拆乾淨會更清楚（Goulding & Marwood 2022）：本頁的「供給 QO₂」其實是兩棒接力——先有 [[Convective oxygen delivery|對流送氧]]（心輸出 × CaO₂，把含氧血整批運到微血管），再有 [[Diffusive oxygen transport|擴散送氧]]（Fick 擴散定律 V̇O₂=DO₂×ΔPO₂，把氧滲進細胞）。PmvO₂ 正是這兩棒的交會點：它既是對流的「成果」，又是擴散的「推力來源」（ΔPO₂ 的微血管端）。
3. 關鍵：**即使整體 VO₂ 沒變，只要 PmvO₂ 被壓低，細胞要驅動同樣的粒線體產能，就得提高 ADP、NADH 等代謝訊號**——也就是代謝調控變吃力。所以微小的氧分壓變化會放大成明顯的代謝後果。這解釋了為什麼吸低氧氣體會傷害運動耐受，即使心輸出代償讓肌肉 VO₂ 不變。
4. 纖維型造成供需比差異（連到 [[Muscle fiber types|纖維型]]）：Type II（快縮）纖維的微血管對舒張訊號較不敏感、交感收縮較強 → QO₂/VO₂ 較低 → PmvO₂ 較低 → 抽取更多血中氧、組織氧壓更低。Type I 則相反。
5. 為什麼這對 [[Critical power|CP]] 之上特別重要？因為超過 [[Critical power|CS]]，身體**優先把血流導向低氧化的 Type II 纖維**（大鼠：>CS 時白肌血流暴增 >100%，紅肌 <30%）。這些纖維在低 PmvO₂ 下運作，正是 [[VO2 slow component|VO2 慢成分]]「多花的那份氧」與容易力竭的血管層級來源。
6. 控制血流的主角是一氧化氮（NO，一種讓血管舒張的訊號分子）：
   - **eNOS**（血管內皮型）：靠血流剪力驅動，在低強度（<CS）主要供應 Type I 與高氧化纖維。
   - **nNOS**（神經型，位在肌纖維內）：在高強度（>CS）負責把血流灌進高醣解的 Type IIb/d/x 纖維。
   - 因為 Type II 纖維的低 PmvO₂、低 pH 環境，**有利於把硝酸鹽/亞硝酸鹽（nitrate/nitrite）還原成 NO**——這解釋了為什麼**膳食硝酸鹽（如甜菜根汁）補充**能特別有效提升 Type II 的血流與氧分壓、加速 VO₂ 動力學、改善 >CP 的運動耐受。
7. 收縮型態也能調 PmvO₂、進而改 CP：縮短**工作週期**（收縮短、放鬆多）→ 放鬆空檔血流灌得多 → QO₂↑、PmvO₂↑ → VO₂ 可更高、CP 上升（手握實驗：CP ↑~30%、耐受時間延長 ~150%）。這對 CP 極低的心衰病人是「靠調整收縮節律改善功能」的希望。

### 微血管供氧是 CP 的「獨立決定因子」（Goulding 2021）
8. 一個重要區分：[[VO2 kinetics|τVO2]] 與「微血管供氧」是**兩個獨立**影響 [[Critical power|CP]] 的因子。證據：吸高氧（hyperoxia）用 NIRS 量到肌肉含氧（oxy-[Hb+Mb]）上升、CP 也上升，**即使 τVO2 在常氧與高氧之間沒變**——表示供氧本身（不透過改變動力學）就能抬高 CP。
9. 為什麼合理：依 [[Critical Pi threshold and positive feedback model|臨界閾值模型]]，提高肌內氧壓會減緩 [PCr] 分解與 [ADP]、[[Inorganic phosphate|無機磷酸 Pi]] 的累積（三者與吸入氧濃度 FiO₂ 成反比），於是同一代謝率下 Δ[Pi] 較小、較不易越過臨界 [Pi]、CP 因而上升。這個效應在低 PmvO₂ 的 Type II 肌肉特別明顯——也呼應本頁「>CP 血流導向 Type II」與膳食硝酸鹽的舞台。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Poole 等人主張，>CP/CS 運動的生理底層與「骨骼肌的呼吸控制」緊密相連；CP 對 O₂ 輸送高度敏感（hyperoxia 升、hypoxia 與血流阻斷降）。他們提出 Type II 纖維的低 PmvO₂＋nNOS 依賴，是膳食硝酸鹽改善 severe 強度耐受的機制基礎。
- **背後的推理／證據**：大鼠分纖維型血流量測（微球）、微血管氧分壓量測、選擇性 nNOS 抑制劑（S-methyl-L-thiocitrulline）實驗（Fig. 4）。顯示 >CS 血流不成比例導向 Type II，且該增量被 nNOS 阻斷選擇性消除——直接連起「纖維型→血流控制→NO 來源」這條鏈。

## 易誤解之處
1. **PmvO₂ 看的是「供需比」，不是「血流絕對量」。** 血流再大，若消耗也大，PmvO₂ 不一定高。決定組織氧壓的是 QO₂/VO₂ 的比，不是 QO₂ 單獨。
2. **PmvO₂ 微降也很要緊。** 不必降到 [[Dysoxia|缺氧（dysoxia）]] 那麼低，光是壓低就會讓代謝調控變吃力（需更高 ADP/NADH）。這和「沒有 dysoxia」並不矛盾——是「還沒缺氧、但氧壓下降已有代謝代價」。
3. **硝酸鹽補充為何「挑」Type II 起作用？** 因為 Type II 的低氧壓、低 pH 環境才有利亞硝酸鹽還原成 NO；在氧氣充足的 Type I，這條非酵素途徑用不上。所以效果集中在高強度、Type II 被大量招募時。
4. **整體血流（bulk Q）看不到分配的不均。** 不同纖維區的血流差異可達一個數量級，但用整條肢體的總血流量測會把它平均掉、變「隱形」。
5. **「送氧被改善」不等於「送氧是主謀」——以預熱為例（Goulding 2023）。** [[Priming effect|預熱]] 確實升高微血管供氧（NIRS 量到 total[heme]、O₂ 飽和度↑、灌流不均↓），很容易讓人以為「預熱靠改善送氧而加速 VO2 動力學」。但這是**伴隨（coincident）非必要**：在導管動脈血流不變時整體 VO2 動力學照樣變快，且年輕健康者單獨升送氧（高氧、促紅血球生成素、加壓）根本不改 τVO2——既然送氧本來就不是 τ 的限制，升它也改不了 τ。送氧改善較可能真正貢獻的，是 τ 本來就大、送氧確為瓶頸的族群（年長、慢性病）。完整裁決見 [[Mechanisms of the priming effect]]。

## 用生活例子再講一次
把運動中的肌肉想成一座有很多攤位的市場，氧氣是貨。每個攤位（肌肉小區）的「庫存壓力」（PmvO₂）由「進貨速度（QO₂）÷ 賣貨速度（VO₂）」決定。生意普通的耐久攤（Type I）進貨順、庫存足。但一到旺季（>CP），調度員把貨車優先派去「火爆但庫存吃緊的快攤（Type II）」——這些攤賣得猛、進貨相對跟不上，庫存壓力低，隨時可能缺貨。調度靠的是 NO 這個「交通號誌」，而對快攤特別有效的捷徑補給，就是硝酸鹽。

（失準之處：市場貨物可囤積；氧氣幾乎不能儲存，是即時供需，所以供需比一失衡，後果立刻反映在代謝上。）

## 換句話說
換句話說，肌肉每一小區的氧夠不夠，看的是「送氧速率 ÷ 用氧速率」這個比值，它決定微血管氧分壓 PmvO₂；壓力一低，細胞驅動產能就更吃力。超過 [[Critical power|CP]] 時血流被優先導向低氧壓的 [[Muscle fiber types|Type II 纖維]]，這是效率下降與力竭的血管根源，也是膳食硝酸鹽能改善高強度耐受的舞台。

## 來源
- [[source-Poole-2016-critical-power]]（Vascular control above CP/CS 整節：QO₂/VO₂、PmvO₂、纖維型血流分配、eNOS/nNOS、硝酸鹽、工作週期對 CP 的影響、Fig. 4。）
- [[source-Goulding-2021-VO2-kinetics-tolerance]]（微血管供氧為獨立於 τVO2 的 CP 決定因子：hyperoxia 經 NIRS 升肌氧並升 CP 而 τVO2 不變；機制經臨界 [Pi]（[PCr]/[ADP]/[Pi] 與 FiO₂ 反比）。）
- [[source-Goulding-2022-determinants-of-CP]]（§2.1–2.2：把「供氧」明確拆成 [[Convective oxygen delivery|對流]] 與 [[Diffusive oxygen transport|擴散]] 兩個獨立步驟；PmvO₂ 為兩者交會點。）
- [[source-Goulding-2023-priming-VO2-kinetics]]（易誤解 #5：§3.3 預熱升高微血管供氧（NIRS total[heme]/飽和度↑）但為伴隨非必要——送氧不變仍見效、年輕健康者單獨升送氧不改 τVO2；送氧較可能貢獻於 τ 大、送氧為瓶頸的族群。）
