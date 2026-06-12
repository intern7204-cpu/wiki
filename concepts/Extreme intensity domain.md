---
type: concept
aliases: [極限強度域, 極限強度區間, 超嚴重域, 超極重度, supra-severe, extreme intensity domain, extreme domain]
tags: [exercise-physiology, thresholds, performance]
sources: [source-Ventura-2023-severe-extreme-tolerance]
prerequisites: [達到VO2max的最高強度（IHIGH）, 臨界功率／臨界速度（critical power / critical speed, CP/CS）, W′（臨界功率以上的有限功容量）, VO2 慢成分（VO2 slow component）]
created: 2026-06-12
updated: 2026-06-12
---

# 極限強度域（extreme intensity domain）

## 本質（一句話）
極限強度域就是「高到連把攝氧量逼到最大值的時間都不夠」的最猛區間——它在 [[Critical power|CP]] 之上的 severe 域**再往上**、過了 [[Maximal intensity for VO2max attainment|IHIGH]] 之後那一段：力竭來得太快，[[VO2max|VO2max]] 還沒到、[[W prime|W′]] 還沒燒乾你就停了，而 CP 那條 t_lim 公式也會開始**高估**你能撐多久。

## 前置概念
- [[Maximal intensity for VO2max attainment|達到 VO2max 的最高強度（IHIGH）]]
  （extreme 域的下界就是 IHIGH；先懂這道分界怎麼來、怎麼量。）
- [[Critical power|臨界功率（CP/CS）]]
  （extreme 域整段都在 CP 之上，且本頁重點是「CP 模型在這裡開始失準」；先懂 CP 與 t_lim 公式。）
- [[W prime|W′（臨界功率以上的有限功容量）]]
  （extreme 域的怪事是「W′ 沒完全耗竭就力竭」；先懂 W′ 是什麼、與「力竭＝W′ 用盡」的假設。）
- [[VO2 slow component|VO2 慢成分（VO2 slow component）]]
  （severe 與 extreme 的分水嶺就是慢成分有沒有時間把 VO2 推到頂；先懂慢成分。）

## 為什麼會這樣（first-principles 推導）
1. 先回到 [[Exercise intensity domains|區間框架]]：以前我們把 [[Critical power|CP]] 之上**統稱**「極重度（severe）」。但 CP 之上其實還藏著一道線——[[Maximal intensity for VO2max attainment|IHIGH]]，於是 CP 之上要再分成兩段。
2. **severe 段（CP ~ IHIGH）**：強度雖在 CP 之上、註定力竭，但你撐的時間**夠長**，讓 [[VO2 slow component|慢成分]] 有時間把 [[VO2|VO2]] 一路推到 [[VO2max|VO2max]]。在這裡，「VO2 抵達最大值」「[[W prime|W′]] 耗盡」「力竭」三件事大致**同時**發生。證據：Murgatroyd 2011 發現 W′ 與慢成分振幅正相關（r²=0.76）——W′ 在 severe 域確實是「被慢成分這個正回饋迴路燒到見底」的那筆能量。
3. **extreme 段（> IHIGH）**：強度高到力竭來得**太快**。
   - [[VO2 slow component|慢成分]] 通常要運動開始後 80–110 秒才疊加上來、再花時間發展；但 extreme 域的力竭時間可能就在這個量級或更短，於是慢成分**來不及充分發展**，VO2 還沒被推到頂，運動就結束了——所以 **VO2max 達不到**（這正是 [[Maximal intensity for VO2max attainment|IHIGH]] 的定義）。
   - 既然力竭發生在 VO2 還沒到頂、慢成分迴路還沒跑完之前，[[W prime|W′]] 也就**沒有完全耗竭**就停了。
4. 這帶出本頁最重要的後果——**CP 模型會在 extreme 域失準**。回想 t_lim = W′/(P−CP) 的隱含假設：**力竭＝W′ 剛好耗盡**（見 [[W prime|W′]] 與 [[Metabolic milieu at task failure|力竭時的代謝終點]]）。但在 extreme 域，你是在 W′ **還沒燒乾**時就力竭的——所以「按 W′ 全部燒完來算的撐多久」會比實際**長**，也就是**模型高估 t_lim**。
5. 這個推論有兩組證據，但結論帶轉折，要放慢看：
   - **單關節（膝伸）運動，Alexander 2019**：extreme 域的力竭時間被 severe 域估的 CP/W′ **高估**；而且 extreme 域有它**自己一筆較小的 W′**（1.7 kJ）遠小於 severe 域的 W′（5.9 kJ）——像是換了一套規則。
   - **全身（自行車）運動，Ventura 2023**：在 extreme 域的**最下緣**（IHIGH+5%），用三次預測試驗配適的 CP 模型，其**平均**預測值與實測**沒有顯著差異**（只有偷工減料的兩試驗模型顯著高估）。換句話說，剛跨過 IHIGH 時，模型還勉強堪用。
6. 怎麼調和「該失準」與「最下緣還堪用」？關鍵是**邊界不是一個鋒利的點，而是一段漸變帶**（[[Maximal intensity for VO2max attainment|IHIGH]] 非鋒利閾值；Pethick「相變而非閾值」）。剛跨過 IHIGH 時，W′ 幾乎還是全用掉的、行為跟 severe 域差不多，所以模型還準；**愈往 extreme 域深處走，模型愈不準**。Ventura 用「異質變異（heteroscedasticity）」抓到了這個趨勢：在 IHIGH+5%，撐得愈久的人被高估得愈多（見 [[Bland-Altman agreement analysis|Bland-Altman 一致性分析]]）——這正是「模型開始系統性偏掉」的指紋，雖然平均還沒到統計顯著。
7. 還沒解的問題：既然 extreme 域力竭時 [[W prime|W′]] 沒燒乾、[[VO2max|VO2max]] 也沒到，那**到底是什麼決定了你在 extreme 域力竭**？Ventura 的異質變異暗示「無氧代謝的主導性」在此更吃重，可能是一套**不同於 W′ 耗竭**的機制（呼應 Alexander 的「extreme 有自己的較小 W′」）。這仍是開放問題。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：extreme（supra-severe）是一個**獨立的強度域**，位於 IHIGH 之上；CP 模型對它的力竭預測能力會下降，且愈往高強度愈差。從三次預測試驗導出的 CP/W′，可以預測「邊界附近」的耐受，但深入 extreme 域後應謹慎；只用兩次試驗配適的模型尤其會高估短時間運動的耐受。
- **背後的推理／證據**：核心證據是 IHIGH+5% 時**無人達 VO2max**（VO2peak 顯著低於 VO2max），證明它與 severe 域生理性質不同；加上 [[Bland-Altman agreement analysis|Bland-Altman]] 在 IHIGH+5% 顯示**異質變異**（而 IHIGH 是同質變異），以及單關節研究（Alexander 2019）裡 extreme 高估且擁有較小的專屬 W′。這些一起支持「extreme 是另一套規則的區間」。

## 易誤解之處
1. **extreme ≠ severe（≠ 本 wiki 過去說的「極重度」）。** 本 wiki 早期把 [[Critical power|CP]] 之上**全部**叫「極重度（severe）」。嚴格的四分法裡，CP 之上要再切：CP→[[Maximal intensity for VO2max attainment|IHIGH]] 是 severe（仍達 VO2max），>IHIGH 才是 extreme（達不到 VO2max）。本頁的「極限強度」專指後者。
2. **「達不到 VO2max」不是有氧弱，是時間不夠。** extreme 域力竭太快，VO2 還在爬升就被打斷；不是攝氧能力下降。
3. **邊界不是刀切的點。** IHIGH 是漸變帶（相變），所以「一過 IHIGH 模型就崩」是錯的——是「最下緣還堪用、愈深入愈不準」。
4. **別把「平均預測還準」當成「個別預測也可靠」。** Ventura 在 IHIGH 與 IHIGH+5% 的個體一致性界線都很寬（±15–22%）；平均偏倚小不代表對某一個人準（見 [[Bland-Altman agreement analysis|Bland-Altman]]）。
5. **兩試驗配適在 extreme 域更危險。** 只用兩個功率點配 CP/W′ 的模型，在 IHIGH+5% 顯著高估了 t_lim——短時間、高強度運動的處方尤其別省這個成本（見 [[Critical power model fitting|CP 模型配適]]）。

## 用生活例子再講一次
把運動強度想成跑步距離。**severe 域**像 1500 公尺：很拚、註定要力竭，但時間夠長，身體有機會把引擎催到最高轉速（VO2max），最後是「油箱（W′）見底＋引擎到頂＋力竭」一起發生。**extreme 域**像 100 公尺衝刺：太快結束了，引擎根本來不及催到最高轉速你就到終點/力竭了，油箱裡其實還剩油。如果你硬用「1500 公尺那套油耗公式」去算 100 公尺能跑多久，會算得太樂觀（高估）——因為那套公式假設你會把油燒乾，但短跑根本沒燒到底。

（失準之處：跑步距離是外在固定的；強度域是用生理反應（達不達得到 VO2max）定義的內在分界，且 severe↔extreme 的界線會因人、因運動型態而移。）

## 換句話說
換句話說，極限強度域是 [[Critical power|CP]] 之上、再過了 [[Maximal intensity for VO2max attainment|IHIGH]] 的那一段超高強度：力竭快到 [[VO2max|VO2max]] 來不及達到、[[W prime|W′]] 來不及燒乾。因為 CP 的 t_lim 公式假設「力竭＝W′ 用盡」，而 extreme 域違反了這個假設，公式就會高估你能撐多久——不過邊界是漸變的，所以剛跨進去（IHIGH+5%）時平均預測還勉強堪用，愈往深處愈失準，而「extreme 域到底為何力竭」仍是未解之謎。

## 來源
- [[source-Ventura-2023-severe-extreme-tolerance]]（全文：extreme 域為獨立 supra-severe 域、IHIGH+5% 無人達 VO2max；三試驗 CP 模型在 IHIGH+5% 平均無顯著差、兩試驗顯著高估；IHIGH 同質變異 vs IHIGH+5% 異質變異；引 Alexander 2019（膝伸 extreme 高估、專屬較小 W′＝1.7 vs 5.9 kJ）、Murgatroyd 2011（W′↔慢成分 r²=0.76）、Pethick 2020（相變非閾值）。）
