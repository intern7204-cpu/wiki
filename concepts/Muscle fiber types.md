---
type: concept
aliases: [肌纖維類型, 肌肉纖維類型, 慢縮肌, 快縮肌, 第一型纖維, 第二型纖維, Type I, Type II, slow twitch, fast twitch, muscle fiber types]
tags: [exercise-physiology, muscle, foundation]
sources: [source-Poole-2016-critical-power, source-Gaesser-1996-slow-component, source-McMahon-2002-PCr-resynthesis, source-Molmen-2024-mitochondrial-capillary-training]
prerequisites: [細胞呼吸（cellular respiration）, 乳酸（lactate / lactic acid）與它的產生]
created: 2026-06-10
updated: 2026-06-12
---

# 肌纖維類型（muscle fiber types：Type I / Type II）

## 本質（一句話）
肌肉裡的纖維分兩大類：**慢縮、耐久、靠有氧（Type I）**和**快縮、有力但易累、偏靠醣解（Type II）**——同一塊肌肉是這兩類按比例混在一起，比例決定它擅長耐力還是爆發。

## 前置概念
- [[Cellular respiration|細胞呼吸（cellular respiration）]]
  （兩類纖維的根本差別在「有多依賴有氧產能」；先懂有氧產能。）
- [[Lactate|乳酸（lactate）與它的產生]]
  （快縮纖維偏走醣解、較易產乳酸；先懂這條無氧捷徑。）

## 為什麼會這樣（first-principles 推導）
1. 肌肉要做兩種很不同的事：有時要「持久、省力」（站、走、慢跑），有時要「瞬間爆發大力」（衝刺、舉重）。同一種纖維很難兩者都最佳，於是演化出分工。
2. **Type I（慢縮，slow twitch）**：收縮慢、力量小，但**粒線體多、微血管密、耐久不易累**。它高度依賴有氧產能（[[Cellular respiration|細胞呼吸]]），清乳酸能力強。負責低強度、長時間的工作。
3. **Type II（快縮，fast twitch）**：收縮快、力量大，但**粒線體相對少、偏靠醣解（[[Lactate|無氧]]捷徑）、容易累**。又細分為 IIa（介於中間、還算耐久）與 IIb/IId/x（最快、最有力、最不耐久、最偏醣解）。負責高強度、短時間的爆發。
4. 招募順序（很重要，連到 [[Critical power|CP]]）：身體用力時**先招募 Type I**，強度愈高才**逐步招募 Type II**。所以在低強度只用到耐久的慢縮纖維；到了高強度（尤其超過 [[Critical power|CP/CS]]），愈來愈多易累、低氧化效率的快縮纖維被拉進來——這正是高強度運動 [[Exercise efficiency|效率]]變差、[[VO2 slow component|VO2 慢成分]]、容易力竭的纖維層級原因之一。支持這條的原始證據：高強度運動第 4–7 分鐘的肌電（iEMG）隨 VO2 一起上升（Shinohara & Moritani），且 Type II 纖維比例愈高者踩車的 VO2 成本愈高、效率愈低（Coyle 等）；快縮纖維本身的 VO2 動力學也較慢、粒線體含量較少。
5. 比例因人因肌而異：人類比目魚肌（soleus）約 88% Type I（天生耐久），股直肌約只有 35%；菁英耐力選手股四頭可達 70% Type I，爆發型選手可能低到 40%，極度不活動者甚至 30%。而且**深層纖維 Type I 較多**，所以高強度時被招募的較淺層纖維偏向 Type II。
6. 血流控制也分型（連到 [[Microvascular O2 delivery|微血管 O₂ 輸送]]）：Type II 纖維的微血管對舒張訊號較不敏感、交感收縮較強，導致它們的「O₂ 供給/利用比」較低、組織氧分壓較低——這讓它們在高強度運動時更吃緊。
7. **恢復也分型：Type I 補回 [[Phosphocreatine|PCr]] 較快。** 同一次衝刺後，慢縮（Type I）纖維 60 秒內把 PCr 補回約 92% 靜息值，快縮（Type II）只回到約 66%（Tesch；Casey 一致）——因為 Type I 毛細血管多、粒線體密、氧化酵素活性高，補 PCr 的有氧供應更足（補 PCr 純靠有氧，見 [[Phosphocreatine resynthesis|磷酸肌酸再合成]]）。反過來，Type II **靜息存的 PCr 較多**（約多 55%）卻補得慢——「存得多」與「補得快」剛好相反。這也是「間歇運動偏重 Type I 恢復能力」的纖維根。（caveat：Dawson 用反覆衝刺卻沒測到 PCr 恢復速率與 CS 活性相關，提醒這條相關在劇烈、低 pH 條件下會被攪混，見 [[Oxidative reserve]] 易誤解 #5。）

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Poole 等人指出，超過 [[Critical power|CS]] 的運動會**優先把血流導向低氧化的 Type II 纖維**（大鼠資料：>CS 時白肌血流暴增 >100%，紅肌僅 <30%）；這些纖維在更低的微血管氧分壓下運作，且其血流高度依賴 nNOS 來源的一氧化氮。疾病（如心衰）會增加 Type II 纖維比例與對它們的依賴，惡化運動耐受。
- **背後的推理／證據**：證據來自大鼠不同纖維型肌肉的血流（放射標記微球）與去氧合（NIRS）量測，以及人類肌肉切片的纖維比例。纖維型決定了血流分配、氧分壓、乳酸與疲勞行為，是把「全身運動表現」拆到「肌肉層級機制」的關鍵變數。

## 易誤解之處
1. **不是「純慢縮」或「純快縮」的肌肉，是混合比例。** 每塊肌肉都同時含兩類，差別在比例。講「某人快縮肌多」是指比例偏向 Type II。
2. **Type II 不是「壞纖維」。** 它在爆發、高強度時不可或缺；只是耐久差、易累。問題出在疾病讓人「過度依賴」它。
3. **招募是漸進的，由低到高。** 不是低強度只用慢縮、高強度只用快縮；而是隨強度增加，在慢縮的基礎上「疊加」招募快縮。
4. **「額外招募纖維」不是 [[VO2 slow component|VO2 慢成分]] 的唯一原因。** 本文獻指出，在纖維一開始就全被招募的情況（電刺激狗肌、3 分鐘全力測試）仍有慢成分——所以慢成分還有纖維內效率下降等其他來源。
5. **數週–數月的訓練幾乎不改 Type I:Type II 的『比例』——別把『訓練變強』當成『慢縮纖維變多』。** 50 年、425 篇統合迴歸顯示：訓練後 Type I 比例**整體不變**（ET +0.7%、HIT −0.3%、SIT −2.6%，皆 n.s.），只有 ET 與 SIT 之間呈相反「傾向」（ET 偏 →Type I、SIT 偏 →Type II，p=0.041）。真正的 I↔II 轉換可能需要**數年**刻意訓練才測得到（短期訓練多只看到 IIx→IIa）；而「菁英耐力選手 Type I 較多」更可能是**起點基線**（訓練有素者基線 Type I 54.8% > 未訓練 45.2%）而非短期訓練長出來的（Mølmen 2024）。

## 用生活例子再講一次
把肌肉想成一支混編的工班：有一批「耐操的長工」（Type I，做得慢但能做整天、不喊累）和一批「猛但短命的臨時工」（Type II，力氣大、速度快，但很快就累垮）。平常的活只派長工；活愈重，才愈多臨時工被叫上場。臨時工一上，產出衝高但也開始堆問題（乳酸、效率下降、很快撐不住）。一個人「長工多還是臨時工多」，決定他是天生的馬拉松型還是短跑型。

（失準之處：真實纖維不是「兩種人」，而是同一肌肉裡連續分佈的纖維，且訓練能部分改變其代謝特性，不像工班那樣身分固定。）

## 換句話說
換句話說，肌纖維分耐久靠氧的 Type I 與爆發偏醣解的 Type II，按比例混在每塊肌肉裡，並由低到高漸進招募。高強度（>[[Critical power|CP]]）時大量動用易累的 Type II，是運動效率下降、乳酸上升、容易力竭的纖維層級根源；它們的血流與氧分壓特性，也是 [[Microvascular O2 delivery|微血管 O₂ 輸送]] 與營養介入（如硝酸鹽）的作用舞台。

## 來源
- [[source-Poole-2016-critical-power]]（Vascular control above CP/CS 節：纖維型比例、招募順序、>CS 血流優先導向 Type II、nNOS 與纖維型。）
- [[source-McMahon-2002-PCr-resynthesis]]（推導第 7 點，第 4、7 節：Type II（FT）靜息 [PCr] 比 Type I 多約 55%、[ATP] 多約 42%（Fitts 整理）；但 Type I 補 PCr 較快——衝刺後 60 s ST 回補至 92%、FT 僅 66%（Tesch），Casey 一致，因 Type I 毛細血管/粒線體/氧化酵素較多；caveat：Dawson 反覆衝刺未見 PCr 恢復與 CS 相關。）
- [[source-Molmen-2024-mitochondrial-capillary-training]]（易誤解 #5，§3.3.1：訓練不改 Type I 比例（ET +0.7%／HIT −0.3%／SIT −2.6%，皆 n.s.）、ET vs SIT 反向傾向（p=0.041、ET→I/SIT→II）；短期多只見 IIx→IIa、真正 I↔II 轉換需數年；訓練有素者基線 Type I 較高（54.8 vs 未訓練 45.2%）。標出本頁推導第 5 點「比例因人因肌而異」的訓練可塑性邊界。）
