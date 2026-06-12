---
type: concept
aliases: [肌肉疲勞, 疲勞, 中樞疲勞, 周邊疲勞, 全身疲勞, 任務失敗, 力竭, fatigue, central fatigue, peripheral fatigue, task failure]
tags: [exercise-physiology, fatigue, foundation]
sources: [source-Poole-2016-critical-power, source-Goulding-2021-VO2-kinetics-tolerance, source-Caen-2019-work-recovery-reconstitution, source-McMahon-2002-PCr-resynthesis]
prerequisites: [細胞呼吸（cellular respiration）]
created: 2026-06-10
updated: 2026-06-11
---

# 肌肉疲勞（fatigue）與任務失敗（task failure）

## 本質（一句話）
疲勞是「運動過程中，肌肉產生力量的能力**持續、暫時地下降**」的動態過程；而任務失敗是「疲勞累積到撐不住、被迫停下」的那一刻——兩者不是同一件事。

## 前置概念
- [[Cellular respiration|細胞呼吸（cellular respiration）]]
  （周邊疲勞很大一部分源自肌肉內代謝環境改變；先懂能量代謝。）

## 為什麼會這樣（first-principles 推導）
1. 先把兩個常被混用的詞分清楚（這是讀整個疲勞文獻的關鍵）：
   - **疲勞（fatigue）**：產力能力**逐漸**下降的過程。它**從運動一開始就在進行**，不是到最後才出現；而且是暫時的（休息會恢復）。
   - **任務失敗（task failure）**：疲勞（或其症狀）累積到讓你**無法再維持目標**、被迫中止的那個**點**。也就是力竭、撐不住的瞬間。
   關鍵：疲勞一直在累積，但只有累積到某個程度才造成任務失敗。「在疲勞」不等於「失敗了」。
2. 疲勞依「發生在神經肌肉接點的哪一側」分三型：
   - **周邊疲勞（peripheral fatigue）**：失力源自**接點遠端、肌纖維內部**——代謝環境變化（[[Lactate|乳酸]]/H⁺、Pi、ADP 累積、磷酸肌酸耗竭、肝醣耗盡影響鈣離子釋放）讓收縮機器本身變弱。（對**短時間高強度**運動，[PCr] 耗竭與 [[Intracellular pH|細胞內 pH（pHi）]] 下降被視為兩大主因——力量與 [PCr] 強相關，酸又透過降低鈣敏感度等弱化收縮；但兩者確切機制仍有爭議，見 [[Intracellular pH]]。）
   - **中樞疲勞（central fatigue）**：失力源自**接點近端、神經系統**——大腦/脊髓送給肌肉的驅動訊號減弱（運動神經元興奮性下降等）。
   - **全身/神經肌肉疲勞（global fatigue）**：上面兩者合起來的總效果，表現為最大自主收縮力（MVC）下降。
3. 哪一型主導，看強度（連到 [[Critical torque|臨界扭矩]]/[[Critical power|CP]]）：
   - **低強度**（如 ≤15% MVC 持續收縮）：以中樞疲勞為主，周邊疲勞有限。
   - **高強度**（≥20% MVC 持續，或 >50% MVC 間歇）：以周邊（代謝性）疲勞為主。
4. 但「低 vs 高」的界線在哪？本文獻的核心發現：這條界線就是 [[Critical torque|臨界扭矩（CT）]]/[[Critical power|CP]]。
   - **低於 CT/CP**：周邊疲勞**仍會發生但很慢**，且肌肉代謝、心肺反應大致穩定。
   - **高於 CT/CP**：周邊疲勞發展**快 4–5 倍**，代謝持續惡化到力竭。
   而且「高於 CT 時的疲勞速率」往回外推**無法預測**「低於 CT 的疲勞」——代表兩邊的疲勞機制本質不同。所以 CP/CT 是一個真正的「疲勞閾值」。
5. 重要細節：在力竭（任務失敗）那一刻，**只要是在 CT/CP 之上，達到的周邊疲勞程度都相同**，與你撐了多久無關——這對應「[[W prime|W′]] 是固定可累積的量」這個概念（見 [[Critical power|CP]]）。

### 疲勞當「感測器」：與效率損失是一體兩面（Goulding 2021）
6. 一個更深的角色：在 [[Critical Pi threshold and positive feedback model|臨界閾值模型]] 裡，疲勞被當成控制迴路的**感測器**。因為肌肉沒有「Pi 受器」也沒有「功率受器」，無法直接感測自己越過了臨界閾值；但 [[Inorganic phosphate|Pi]] 升高造成疲勞，而疲勞會**逼迫用更多 ATP 維持同一功率**（效率下降）——於是「疲勞一出現」就等於通報「臨界閾值被越過了」。
7. 由此推出「疲勞↔效率損失是同一枚硬幣的兩面」（Grassi 2015）：疲勞使 [[Muscle fiber types|Type I 纖維]] 在被拖慢時效率掉到比 Type II 還低、肌肉開始「自己對抗自己」，再加上招募效率差的 Type II——這正是 [[VO2 slow component|VO2 慢成分]] 的來源。
8. 在全身運動，這個迴路還疊上 [[Group III-IV muscle afferents|Group III/IV 肌肉傳入神經]]：它們把周邊疲勞回報中樞、收斂驅動，替疲勞發展設上限（阻斷它們可抬高可忍受的尖峰 [Pi]＝放大 [[W prime|W′]]）。把運動肌、呼吸肌與其他來源的這些回饋在中樞**整合**成單一可忍受上限，就是 [[Sensory tolerance limit|感覺耐受極限]]——尤其在全身、長時間運動，任務失敗可能在這個「感覺總帳」爆表時發生，未必等到某塊肌肉自己到達 [[Metabolic milieu at task failure|固定代謝終點]]。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Poole 等人主張 [[Critical power|CP]]/[[Critical torque|CT]] 是「分隔不同疲勞機制的關鍵神經肌肉疲勞閾值」。CP 是「疲勞進展的上界」——它界定了周邊疲勞會開始失控加速的邊界。
- **背後的推理／證據**：Burnley 等人用間歇等長收縮＋電刺激，量出 CT 上下的全身/中樞/周邊疲勞速率。發現 CT 之上周邊疲勞快 4–5 倍、且其速率往下外推預測「<33% MVC 不該有周邊疲勞」（落在 CT 信賴區間內）；但實測 CT 之下仍有緩慢周邊疲勞、且無法由 CT 之上的數據預測——這個「不可外推」正是「兩邊機制不同」的關鍵證據。

## 易誤解之處
1. **疲勞 ≠ 任務失敗。** 疲勞是「逐漸變弱的過程」，從頭就在進行；任務失敗是「撐不住的那一點」。把「累」說成「失敗」會混淆機制討論。
2. **中樞疲勞不是「心理上想放棄」那麼簡單。** 它指神經驅動的客觀下降（可用電刺激量化「自主用力 vs 被電刺激能再擠出的力」之差），是生理現象，不只是意志力。
3. **疲勞型隨強度換檔，且換檔點是 CT/CP，不是某個固定 %MVC。** 很多疲勞研究用固定 %MVC（如 40%）對所有人，但同樣 40% 對某些人在 CT 之上、對某些人在 CT 之下，疲勞行為完全不同——這是該文獻對研究方法的重要提醒。
4. **CT 之下仍有疲勞，只是慢且機制不同。** 不是「低於 CT 就不累」，而是低於 CT 的疲勞緩慢、可被穩態代謝撐住，可能源自肝醣耗竭等非代謝崩潰因素。

## 用生活例子再講一次
把肌肉產力想成手機電量。**疲勞**＝電量一路下降的過程（一開機就在掉）。**任務失敗**＝電量見底、手機關機的那一刻。掉電有兩個來源：**周邊**像「電池本身發熱老化、輸出變弱」（肌肉內代謝），**中樞**像「系統主動調暗螢幕、降頻」（神經減少驅動）。低強度使用時系統靠降頻撐（中樞為主）；高強度狂跑大型 App 時電池直接被榨乾（周邊為主）。而 [[Critical torque|CT]]/[[Critical power|CP]] 就是那個「耗電率從『撐得住』翻成『直線崩』的功耗門檻」。

（失準之處：手機電量耗盡是被動歸零；肌肉的中樞疲勞含主動的保護性調節（可能避免肌肉受傷），不是單純沒電。）

## 換句話說
換句話說，疲勞是「產力能力逐漸下滑」的過程（全程都在發生），任務失敗是「撐不住而中止」的終點；疲勞又分肌肉內的周邊型與神經端的中樞型。哪型主導由強度決定，而切換的界線正是 [[Critical torque|CT]]/[[Critical power|CP]]——在它之上周邊疲勞失速加快，使 CP 成為名副其實的「疲勞閾值」。

## 來源
- [[source-Poole-2016-critical-power]]（Critical torque and fatigue mechanisms 節：fatigue vs task failure 定義、三型疲勞、CT 上下疲勞速率 4–5 倍差異、不可外推。）
- [[source-Goulding-2021-VO2-kinetics-tolerance]]（疲勞作為正回饋迴路的感測器、疲勞↔效率損失一體兩面（Grassi 2015）、Type I 效率交叉、Group III/IV 傳入限制 W′。）
- [[source-Caen-2019-work-recovery-reconstitution]]（推導第 8 點的延伸：把多來源 afferent feedback 整合成 [[Sensory tolerance limit|感覺耐受極限]]，可使全身運動在達到肌內固定代謝終點前提前任務失敗；引 Hureau, Romer & Amann 2018。）
- [[source-McMahon-2002-PCr-resynthesis]]（第 2 節：短時間高強度運動疲勞的兩大主因＝[PCr] 耗竭（力量與 [PCr] 強相關；Casey 報告後續出力與恢復間 [PCr] 回補相關更勝乳酸累積）與 pHi 下降（酸右移力量–鈣曲線、Type I/IIa/IIb 最大力 −12/−25/−44%、抑制 PFK）；兩者確切機制仍爭議（Sahlin 間接假說 vs 反駁）。詳見 [[Intracellular pH]]。）
