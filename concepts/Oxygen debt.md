---
type: concept
aliases: [氧債, 氧負債, 償還氧, oxygen debt, O2 debt, recovery oxygen, EPOC（古典前身）]
tags: [exercise-physiology, VO2-kinetics, metabolism]
sources: [source-Cooper-2022-geometric-tau, source-Goulding-2021-VO2-kinetics-tolerance, source-Korzeniewski-2013-VO2-PCr-off-kinetics, source-Wooten-2021-respiratory-buffering-fatigability]
prerequisites: [氧虧（oxygen deficit, O2 deficit）, VO2 動力學（VO2 kinetics）]
created: 2026-06-11
updated: 2026-06-12
---

# 氧債（oxygen debt, O2 debt）

## 本質（一句話）
氧債就是「運動**停下來之後**，身體還繼續多吸的那份氧」——運動一結束需求瞬間降回去，但 VO2 不能瞬間掉下來，於是停手後那段「降不夠快、多用掉」的氧，就是要償還的氧債。

## 前置概念
- [[O2 deficit|氧虧（oxygen deficit, O2 deficit）]]
  （氧債是氧虧的**鏡像**：氧虧在運動開頭借、氧債在運動結束後還。先懂氧虧，氧債只是把它倒過來看。）
- [[VO2 kinetics|VO2 動力學（VO2 kinetics）]]
  （氧債的大小由「VO2 結束後降得多慢」決定，也就是 off-transit 的 τVO2；先懂 τ 是反應的快慢。）

## 為什麼會這樣（first-principles 推導）
1. 由 [[O2 deficit|氧虧]]：運動**開頭**時，VO2 升得慢、跟不上突增的需求，缺口先向無氧備援（氧庫存、[[Phosphocreatine|PCr]]、醣解）借——這份借款叫氧虧。
2. 現在把場景倒過來：運動**結束**那一刻，出力瞬間歸零、ATP 需求瞬間降回靜息。但 VO2 跟下不來——血流、心跳、體溫、酵素活性都還高，得花幾分鐘才平順降回基線（同樣是指數式逼近，見 [[Time constant|τ]]）。
3. 於是停手後那段時間，VO2 仍高於靜息需求，**身體多用掉了一些氧**。這多用掉的氧就是**氧債**。
4. 它「多」在哪？古典理解：身體用這段多吸的氧去**還開頭借的帳**——把 [[Phosphocreatine|PCr]] 補回（這個補回是純有氧、且補回速率正比於缺口的指數過程，見 [[Phosphocreatine resynthesis|磷酸肌酸再合成]]）、清掉累積的代謝物、把被擾動的狀態復原。所以名字才叫「債」：開頭借（deficit），結束還（debt）。
5. 量化上，氧債的算法和氧虧對稱：
   $$O_2\ debt = \delta\dot{V}O_2 \times \tau_{\dot{V}O2(off)}$$
   δVO2＝運動時 VO2 比基線高出多少，τ(off)＝結束後 VO2 降回去有多慢。**降得愈慢（τ 大），償還拖愈久，氧債愈大。**
6. 在理想的中等強度模型裡，**氧債 ≈ 氧虧**（借多少還多少），所以 on-transit 與 off-transit 量到的 τVO2 應該**約略相等**——這個對稱性，正是 [[Geometric method for VO2 time constant|幾何法]] 能「一趟運動同時量到 on-τ 與 off-τ、互相對照」的依據。

7. **一個更深的守恆（接 Korzeniewski 2013）：氧債的「總量」由要補多少 PCr 鎖死，與恢復動力學的「形狀」無關。** 把第 4 點講白：恢復期多吸的氧，主要拿去**有氧地把消耗掉的 [[Phosphocreatine|PCr]] 補回來**（見 [[Phosphocreatine resynthesis|PCr 再合成]]）。要補**同樣多**的 PCr，化學計量上就得用**同樣多**的氧。所以對給定的 PCr 消耗，**氧債（VO2 高於基線的積分）是固定的**——就算 VO2 降回去的曲線形狀差很多也一樣。電腦模型把這點演得很乾淨：改變恢復期前饋活化的衰減時間 [[Parallel activation of oxidative phosphorylation|τ(OFF)]]，VO2 off 可以從「低而長」變成「高而短」，但兩種形狀**面積相同**、氧債不變。換句話說，**δVO2×τ(off) 這個乘積在「同樣 PCr 要還」時是守恆的**：τ(off) 大（降得慢）通常伴隨 δVO2 的時程重分配，總帳不變。

8. **那為什麼「練過的人氧債較小」？不是形狀變了，是『要還的帳本身變小』。** 同樣功率下，訓練者 PCr 掉得比未訓練者少（粒線體多、平行活化強、[[Metabolic stability|代謝穩定性]] 高），**要補的 PCr 少 → 要還的氧少 → 氧債小**。所以氧債大小主要反映「運動中 PCr 被掏空多少」，而非「恢復曲線長什麼樣」。

## 文獻怎麼說 vs 為什麼這樣說
- **主張／建議**：Cooper 與 Garfinkel 用 off-transit 的氧債來算第二個 τVO2，並指出 on-τ 與 off-τ「應該約略相等」，可作為單趟測量的內部一致性檢核。
- **背後的推理／證據**：他們先前用六趟重複的固定功率方案，實測到 on-τVO2 與 off-τVO2 有良好一致性（Markovitz 2004）。理由是同一個有氧系統「上去」和「下來」的時間尺度相近，所以借與還的曲線形狀對稱。

## 易誤解之處
1. **氧債（debt，結束後）≠ 氧虧（deficit，開頭）。** 兩者算法對稱、理想下數值相近，但發生在運動的**兩端**，方向相反，別混。
2. **古典「氧債」≠ 現代 EPOC，數量上對不齊。** 古典假設「還的氧＝借的氧、且純粹用來補無氧帳」；但現代量到**運動後過量耗氧（excess post-exercise oxygen consumption, EPOC）**常**大於**開頭的氧虧，因為恢復期還多燒了氧在升高的體溫、心肺作功、荷爾蒙、再合成等「額外開銷」上，不只是還債。所以「氧債」是抓對方向的古典概念、但別把它當成 EPOC 的精確等值。（EPOC 尚無獨立頁，日後可建。）
3. **氧債大不代表「欠很多、很糟」。** 它只反映 off-transit 動力學的慢快，是生理屬性，不是運動失敗的指標。
4. **「VO2 降得慢」不等於「氧債大」。** 直覺以為 VO2 拖著降就是多吸了氧、債大。但由推導第 7 點，恢復動力學的**形狀**（快降慢尾 vs 慢降快收）不改變**面積**；氧債由「要補多少 PCr」決定，不由 τ(off) 的大小決定。把「降得慢」直接讀成「債大」會誤判——尤其在比較不同 [[Parallel activation of oxidative phosphorylation|τ(OFF)]] 的肌肉時。
5. **「氧債（總量）」和「恢復動力學（速率）」是同一條 off-曲線的兩種讀法，別當成一回事。** 氧債讀的是**面積**（多吸了多少氧）；[[Gas exchange recovery kinetics|氣體交換恢復動力學]]讀的是**形狀／速率**（τ(off)、ORI＝ΔV̇/τ），拿來當「復原得多快」的指標。有氧訓練能加快恢復動力學（Wooten 2021：VO2-off τ 48→45 s、ORI 變大）；但這主要反映「掉得快」、不直接等同「氧債變小」（氧債的增減取決於運動中 PCr 被掏空多少，見上面推導第 8 點）。要量恢復**能力**用恢復動力學，要算恢復**耗氧量**用氧債。

## 用生活例子再講一次
把運動想成開暖氣的房間：開暖氣（運動）時房間慢慢變熱，關掉暖氣（停手）後房間**不會瞬間變冷**，餘溫還會撐一陣才慢慢降回室溫。那段「關了還在散的熱」就像氧債——系統有慣性，下來和上去一樣需要時間。關得愈久暖、餘溫拖愈長（τ 大），就像氧債愈大。

（這個類比在哪裡會失準：房間餘溫只是被動散熱；氧債是身體**主動**多吸氧去做補 PCr、清代謝物、恢復體溫等工作，不是單純的被動冷卻——這也是為什麼真實 EPOC 會比「純還債」更大。）

## 換句話說
換句話說，氧債是 [[O2 deficit|氧虧]] 的收尾鏡像：運動一停、需求歸零，但 VO2 降不夠快，停手後那段多吸的氧就是要償還的債，大小約等於 δVO2×τ(off)。理想中等強度下借與還相當，所以 on-τ ≈ off-τ——這個對稱讓單趟運動能同時量到兩個 τ 並互相驗證。現代量到的恢復耗氧（EPOC）通常更大，因為恢復不只還債、還有額外開銷。

## 來源
- [[source-Cooper-2022-geometric-tau]]（Step 2-3 與 APPENDIX：off-transit τVo2(off)=(A3−A2)/(B2−B3)=氧債/δVO2；on-τ 與 off-τ「應約略相等」、引 Markovitz 2004 之六趟實測一致性。）
- [[source-Goulding-2021-VO2-kinetics-tolerance]]（氧虧/氧債作為 VO2 動力學鏡像的概念背景；deficit↔debt 區分。）
- [[source-Korzeniewski-2013-VO2-PCr-off-kinetics]]（RESULTS／DISCUSSION：恢復期 VO2 高於基線的積分（＝氧債）對給定 PCr 消耗守恆、與 τ(OFF) 無關——因同樣的 PCr 要還同樣多的氧；VO2 off 初段快則後段慢、初段慢則後段快，兩形狀同面積（Figs.1–2）；訓練者氧債較小因 PCr 掉得少（ref 5、8）。）
- [[source-Wooten-2021-respiratory-buffering-fatigability]]（Table 3：VO2-off 單指數擬合 τ 48.1→44.7 s、振幅 1413→1685 ml/min；off-kinetics（速率）作為恢復能力指標、AET 後加快。對應易誤解 #5；恢復速率框架見 [[Gas exchange recovery kinetics]]。）
