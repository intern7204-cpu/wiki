---
type: concept
aliases: [W prime配對間歇處方, W′配對間歇處方, CP與W prime開間歇處方, 用CP和W撇設定間歇, CP-W prime HIIE prescription, W prime-matched intervals, W prime matched interval prescription, critical power based interval prescription]
tags: [exercise-physiology, critical-power, training, prescription, intermittent]
sources: [source-Miller-2023-fast-start-HIIE]
prerequisites: [Critical power, W prime, Intermittent exercise critical power model, High-intensity interval exercise, Time spent near VO2max]
created: 2026-06-12
updated: 2026-06-12
---

# 用 CP/W′ 開間歇處方（W′-matched interval prescription）

## 本質（一句話）
這是用每個人自己的 [[Critical power|臨界功率（CP）]]和 [[W prime|W′]]來「開」高強度間歇的處方：先決定「這段要消耗多少 W′、在多長時間內消耗」，再換算成「該踩多大功率」（功率 ＝ 要消耗的 W′ ÷ 時長 ＋ CP）；並讓不同的間歇格式都消耗**同量**的 W′，把不同人、不同配方的「極重度域訓練劑量」對齊到同一把個人化的尺上。

## 前置概念
- [[Critical power|臨界功率（critical power, CP）]]
  （處方的「零線」：CP 之下不動用 W′、CP 之上才燒 W′。整個換算以 CP 為基準。先懂 CP 是重度↔極重度的界線。）
- [[W prime|W′（臨界功率以上的有限功容量）]]
  （要被「定量消耗」的那桶能量；這套處方用「消耗多少 W′」當劑量單位。先懂 W′ 是有限、可量的一桶。）
- [[Intermittent exercise critical power model|間歇運動的臨界功率模型]]
  （「>CP 時 W′ 以 (P−CP) 速率被燒」這條，正是把「想燒多少 W′」反推成「該踩多大功率」的依據。先懂這套燒/補帳。）
- [[High-intensity interval exercise|高強度間歇運動（HIIE）]]
  （這套處方是用來開 HIIE 的；先懂 HIIE 是什麼、為什麼要設計參數。）
- [[Time spent near VO2max|接近 VO2max 的時間]]
  （處方想最大化、也用來比較格式好壞的結果指標；先懂這個劑量尺。）

## 為什麼會這樣（first-principles 推導）
1. **先看傳統怎麼開 HIIE 處方，以及它的毛病。** 過去常用 %PPO（最大功率百分比）、%HRmax、%vVO2max（達 VO2max 的速度百分比）、%GET 或 RPE（自覺費力）來設定間歇強度。問題是：這些**相對指標不一定對齊「重度 vs 極重度」的真正生理界線**。同樣是「90% vVO2max」，對 A 可能落在 [[Exercise intensity domains|重度（<CP）]]、對 B 落在極重度（>CP）——於是同一張處方，施加在不同人身上的代謝應變天差地別，劑量不可比、個體變異大。（有研究報告：用 %VO2max 開 HIIE 的依從率只有 ~20%，而用 CP/W′ 開的達 100%，正是因為相對指標常把人放錯區間。）

2. **找一條更好的零線：[[Critical power|CP]]。** CP 是「能穩態 vs 註定力竭」的真正分水嶺（重度↔極重度界線）。只有踩到 CP 之上，才動用 [[W prime|W′]]這桶有限、可量的功容量。把 CP 當零線，「高強度」就有了人人對齊的生理意義。

3. **把劑量單位從『功率/速度』換成『消耗多少 W′』。** 由 [[Intermittent exercise critical power model|間歇 CP 模型]]：在 CP 之上，W′ 以速率 (P − CP) 被消耗。所以「一段 t 秒、功率 P 的工作」總共燒掉的 W′ ＝ (P − CP) × t。反過來，**若我想在 t 秒內恰好燒掉 ΔW′ 的 W′，需要的功率就是**
   $$P = \frac{\Delta W'}{t} + CP$$
   這就是處方公式：給定「想消耗的 W′」與「時長」，直接算出該設多大功率。

4. **為什麼用「消耗的 W′」當劑量特別好用？** 因為它讓不同形狀的區間可以被公平比較：兩個區間就算時長不同、功率分配不同（一個前高後低、一個等功率），**只要消耗掉的 ΔW′ 一樣，它們施加的「極重度域代謝應變」在理論上就相同**。這正是 Miller 2023 用來配平 [[Fast-start pacing|fast-start]] 與等功率兩種格式的手法：兩者每個工作區間都恰好消耗 **60% 的 W′**（W′target）——
   - **等功率（SPHIIE）**：把 60% W′ 在 3 分鐘內**均勻**燒掉（每分鐘 33.3%）→ 固定功率。
   - **快起步（FSHIIE）**：第 1 分鐘燒掉 50% W′target、第 2、3 分鐘各 25% → 前段功率高、後段降。
   兩者總消耗相同，只差「怎麼分配」。

5. **個人的 CP 與 W′ 哪裡來？** 用 [[3-minute all-out test|3 分鐘全力測試（3MT）]]一次測得：CP ＝ 最後 30 秒的平均功率；W′ ＝ 前 150 秒「高出 CP」所做的功（W′ ＝ 150 × (p150 − CP)）。有了個人 (CP, W′)，處方公式才有數可代。

6. **這套處方換來什麼（Miller 2023 的結果）：**
   - 兩種 W′-matched 格式的 [[Time spent near VO2max|≥90% VO2max 時間]]都達 ~25–26%，落在文獻（Buchheit & Laursen 2013，2–5 min 跑步間歇 13–26%）的**高端**——暗示用 CP/W′ 開處方比傳統相對指標更能把人推進並維持在近上限區。
   - 也正因為配平了 W′ 消耗，[[Fast-start pacing|fast-start]] 與等功率之間**沒有**近上限時間的差異（見該頁）——這個「無差異」本身就是處方有效配平劑量的證據。

7. **但配平 W′ 消耗不等於配平一切（重要限制，放慢講）。** 同樣消耗 60% W′，不保證每個人都落在 [[Exercise intensity domains|極重度域]]裡的**同一個次區間**。極重度域可再細分（文獻常分 Z1、Z2、與 extreme zone）：[[W prime|W′]]較**小**的人，「60% W′」攤到 3 分鐘所需的功率（ΔW′/t + CP）相對其 CP–VO2max 跨距可能更高，於是落在更高的次區間；W′ 大的人則落在較低次區間。所以「W′ 配平」對齊了**總消耗劑量**，卻未必對齊**強度落點**——這也是 Miller 把「沒有控制 severe 次區間」列為限制、並推測「若再把人配進同一次區間，fast-start 與等速或許會分出差異」的原因。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：用個人化的 CP 與 W′ 來設定 HIIE 的工作功率（P ＝ ΔW′/t ＋ CP），並以「消耗相同的 W′」來配平不同間歇格式，比用 %PPO/%HRmax/%vVO2max/RPE 等傳統相對指標更貼合生理、更可比、依從性更高。
- **背後的推理／證據**：理由有三層——①[[Critical power|CP]]是真正的重度↔極重度界線，當零線才能讓「高強度」對齊到人人相同的生理意義；②[[Intermittent exercise critical power model|間歇 CP 模型]]給出 W′ 消耗速率 ＝ P − CP，使「想燒多少 W′」可反推功率；③以 W′ 消耗當劑量單位，能讓不同時長/分配的區間公平對照。實證上，W′-matched 處方使近上限時間落在文獻高端，且配平後 fast-start 與等速無差異——兩者都支持「W′ 消耗確實是有效的劑量配平變數」。

## 易誤解之處
1. **配平 W′ 消耗 ≠ 配平強度落點。** 同樣燒 60% W′，W′ 大小不同的人可能落在極重度域的不同次區間（Z1/Z2/extreme），個體實際強度仍可能不齊（見推導第 7 點）。「劑量一樣」不蘊含「強度一樣」。
2. **公式 P ＝ ΔW′/t ＋ CP 假設 CP/W′ 已知且穩定。** 但兩者都有日間變異、會在疲勞下漂移（[[Power-duration relationship plasticity|功率–持續時間關係的可塑性]]）；用一次 [[3-minute all-out test|3MT]]量到的值開往後的處方，本身帶估計誤差。
3. **「同 60% W′ 消耗」鎖的是劑量，不是功率。** 正因為功率沒被鎖死，[[Fast-start pacing|fast-start]] 與等功率才能用不同的功率軌跡、相同的 W′ 消耗被公平比較——別把「W′ 配平」誤解成「功率也一樣」。
4. **這是「極重度域」的處方邏輯，前提是工作段真的 >CP。** 公式裡的 (P − CP) 要為正才有意義；若把目標功率設在 CP 以下，根本不燒 W′，這套劑量框架就不適用。

## 用生活例子再講一次
給體型差很多的兩個人開重量訓練處方，不會叫他們「都舉 50 公斤」——對壯漢太輕、對新手太重，劑量根本不可比。聰明的做法是「都舉各自最大肌力的 70%」，把劑量對齊到**每個人自己的尺標**。用 CP/W′ 開間歇處方就是同個精神：不用「都踩 300 瓦」，而用「都消耗掉自己 W′ 的 60%」當那把個人化的尺；至於要在幾分鐘內、用什麼功率曲線把這 60% 燒掉，就是可以再變化的處方細節。

（這個類比在哪裡會失準：1RM 是一個靜態的力量上限，舉一下就過去了；而 W′ 是會在組間[[W prime reconstitution|回填]]、消耗速率還隨強度變的「動態油桶」——所以「%W′ 消耗」比「%1RM」多了時間維度與回填，沒有重訓那麼一翻兩瞪眼。）

## 換句話說
換句話說，這套處方把間歇的劑量從「踩多少瓦/多快」改成「消耗掉自己 W′ 的多少比例」：以 [[Critical power|CP]]為零線、用 P ＝ ΔW′/t ＋ CP 反推工作功率，並讓不同格式消耗同量 [[W prime|W′]]，從而把「極重度域訓練劑量」對齊到每個人的個人尺上。好處是更貼生理、更可比、依從性高，量到的[[Time spent near VO2max|近 VO2max 時間]]也落在文獻高端；但它對齊的是**總消耗**，不保證對齊**強度落點**（W′ 大小不同→可能落在不同次區間），且吃 CP/W′ 會漂移這個假設。

## 來源
- [[source-Miller-2023-fast-start-HIIE]]（Introduction：傳統相對指標（%PPO/%HRmax/%vVO2max/%GET/RPE）的對齊問題、CP 為「新黃金標準」疲勞閾值、W′ 界定極重度域可做的功、CP/W′ 處方依從率 100% vs %VO2max 的 20%；Materials and Methods：處方公式（W′ to deplete ÷ interval length）＋ CP、60% W′target、FSHIIE（首分鐘 50%、後兩分各 25%）vs SPHIIE（每分鐘 33.3%）、以 3MT 取 CP（末 30 s 均功率）與 W′（150×(p150−CP)）；Discussion：W′-matched 使 ≥90% VO2max 時間落在文獻高端、未控制 severe 次區間（Z1/Z2/extreme zone）為限制、W′ 不同者同 ΔW′ 可能落在不同次區間。）
