---
type: concept
aliases: [質子抑制醣解, 氫離子抑制醣解, 酸抑制無氧醣解, 醣解的質子抑制, proton inhibition of glycolysis, H+ inhibition of glycolysis, acidosis inhibits glycolysis, pH inhibition of glycolysis]
tags: [exercise-physiology, metabolism, mechanism, glycolysis]
sources: [source-Korzeniewski-2015-VO2-slow-component-mechanisms]
prerequisites: [乳酸（lactate）與它的產生, 細胞內 pH（intracellular pH, pHi）]
created: 2026-06-12
updated: 2026-06-12
---

# 質子對醣解的抑制（proton inhibition of glycolysis）

## 本質（一句話）
無氧醣解一邊產能、一邊放出酸（H⁺），而這份累積的酸會**反過來把醣解這條路自己踩慢**——所以醣解愈跑、愈酸，就愈被自己放出的酸卡住，是一個會自我設限的剎車。

## 前置概念
- [[Lactate|乳酸（lactate）與它的產生]]
  （要懂這個剎車，先懂被剎的是什麼：無氧醣解把葡萄糖拆到一半擠出 ATP，副產乳酸與 H⁺。本頁講的就是那份 H⁺ 回頭抑制這條路。）
- [[Intracellular pH|細胞內 pH（intracellular pH, pHi）]]
  （「酸」在量化上就是 H⁺ 濃度上升、pHi 下降；先懂 pHi 是肌纖維內部的酸度、靜息≈7.0、劇烈運動會掉到 6.2–6.7。）

## 為什麼會這樣（first-principles 推導）
一步一步來，每步只用前面的事實：

1. 由 [[Lactate|乳酸]]：運動一強，肌肉走無氧醣解這條捷徑快速補 ATP，副產物是乳酸**加上**氫離子（H⁺）。H⁺ 一多，肌纖維內部就變酸（[[Intracellular pH|pHi]] 下降）。這是起點：**醣解製造酸。**
2. 現在反過來問：這份酸對「醣解這條路本身」有沒有影響？答案是有——而且是**抑制**。醣解不是一條勻速的管子，它有幾個「限速關卡」（速度由它們決定的酵素）：最關鍵的是 **glycogen phosphorylase（肝醣磷解酶，負責把肝醣拆出來餵進醣解）** 與 **phosphofructokinase（PFK，磷酸果糖激酶）**。實驗（試管裡）顯示：**H⁺ 一多，這兩個關卡酵素的活性就被壓低**。關卡被卡住，整條醣解就慢下來。
3. 用白話收束第 2 步：醣解的「龍頭」與「主閘門」這兩道關卡怕酸。它們自己生產線放出的酸愈積愈多，這兩道關卡就愈關愈小，整條醣解的流量（產 ATP 與產乳酸的速率）就被自己拖慢。**這就是「質子抑制醣解」**：H⁺ 是醣解的產物，又是醣解的剎車——典型的負回饋。
4. 這不是只在試管裡成立。在**完整的人體肌肉、重度運動下**也被驗證過（這一步最該記，因為它把試管現象搬進了真實運動）：
   - 給受試者吃 **NH₄Cl（氯化銨，會讓身體變酸）** → 肌肉與血漿的**乳酸反而下降**。為什麼？因為人為先把環境弄酸，醣解被抑制得更兇，產乳酸更少。
   - 給受試者吃 **NaHCO₃（碳酸氫鈉，會讓身體變鹼）** → 乳酸**上升**。因為先把酸中和掉、解除了剎車，醣解放開跑，產乳酸更多。
   - 一降一升，方向完全符合「酸抑制醣解」的預測。
5. 一個關鍵但容易反直覺的推論（放慢）：既然醣解被酸抑制，**酸愈多 ≠ 醣解愈兇**。剛好相反——你看到很酸，可能正是因為醣解已經被踩慢、產酸速率正在往下掉。所以「絕對有多酸」和「醣解此刻跑多快」是兩件事，後面在 [[Bioenergetic mechanism of the VO2 slow component|慢成分機制]] 會用到這個區別。
6. 生理上的意義：這個剎車是一個**保護機制**。如果醣解完全不怕酸、一路狂跑，肌肉會被自己產的酸淹到無法運作。靠「產物（H⁺）回頭抑制生產」，身體把酸化限制在還能撐住的範圍內。

## 文獻怎麼說 vs 為什麼這樣說
- **主張**：累積的 H⁺ 會在 glycogen phosphorylase 與 PFK 這兩個限速步驟抑制（無氧）醣解；這個抑制在完整人體肌肉的重度運動中確實發生、且程度顯著。
- **背後的推理／證據**：(1) 試管研究直接量到 H⁺ 壓低這兩個酵素的活性（Connet & Sahlin；Trivedi & Danforth 等經典生化）；(2) 更關鍵的**完整肌肉**證據是 Sutton 等人的酸鹼操弄實驗——NH₄Cl 致酸使肌肉/血漿乳酸下降、NaHCO₃ 致鹼使乳酸上升，方向與「酸抑制醣解」一致；(3) Korzeniewski & Zoladz 把這條抑制寫進電腦模型（醣解速率乘上 H⁺_rest/H⁺ 這個隨酸度遞減的因子），用來解釋 [[VO2 slow component|VO2 慢成分]]。

## 易誤解之處
1. **「很酸」不等於「醣解很旺」。** 這是本頁最反直覺的點：因為酸會剎醣解，所以高酸度反而常伴隨「醣解流量正在下降」。把「肌肉很酸」直接讀成「現在無氧產能正全力運轉」是錯的。
2. **被抑制的是「醣解的速率」，不是「乳酸被清掉」。** 剎車作用在「產」這一端（少產乳酸/少產酸），不是讓已經產出的乳酸消失。乳酸的清除是另一回事（見 [[Lactate appearance and disappearance|Ra/Rd]]）。
3. **抑制是漸進、部分的，不是開關。** H⁺ 只把醣解「部分」壓低、隨酸度連續變化；醣解不會被酸完全關死，所以 pHi 還會繼續慢慢往下掉，只是流量被往下拉。

## 用生活例子再講一次
想像一台會排廢氣的發電機放在密閉小房間裡。它一發電就排廢氣（H⁺），廢氣愈濃，這台機器的進氣口就愈被嗆到、轉速被迫降下來。於是它不會一路全速到把房間塞爆，而是「愈排愈喘、愈喘轉愈慢」，自己把自己限制在一個還能運轉的廢氣濃度。發電機＝無氧醣解，廢氣＝H⁺，「被自己廢氣嗆到而降速」＝質子抑制醣解。

（這個類比在哪裡會失準：發電機被嗆是物理性缺氧進氣；醣解被抑制是 H⁺ 直接改變兩個酵素的活性，是化學調節，不是「進料不足」。而且醣解的「進料」是肝醣/葡萄糖，並不缺。）

## 換句話說
換句話說，無氧醣解放出的酸會回頭卡住醣解自己的限速酵素（glycogen phosphorylase、PFK），形成一個「愈跑愈酸、愈酸愈慢」的負回饋剎車。完整人體實驗用「人為致酸→乳酸降、人為致鹼→乳酸升」證實了它。關鍵後果是：高酸度往往代表醣解**正在被踩慢**，而醣解流量下降後空出來的 ATP 缺口，必須由有氧路徑（[[Mitochondrial respiratory control|氧化磷酸化]]）補上——這正是 [[Bioenergetic mechanism of the VO2 slow component|VO2 慢成分]] 的機制起點。

## 來源
- [[source-Korzeniewski-2015-VO2-slow-component-mechanisms]]（INTRODUCTION 與 DISCUSSION："glycogen phosphorylase 與 phosphofructokinase 被 H⁺ 抑制（in vitro，ref 7）"；Sutton 1981（ref 41）NH₄Cl 致酸↓乳酸、NaHCO₃ 致鹼↑乳酸；模型以 v_GLYC = k_GLYC·ADP·(H⁺_rest/H⁺)（Eq.2）描述抑制；"glycolysis inhibition by H⁺ 可為防止過度酸化的保護機制"。）
