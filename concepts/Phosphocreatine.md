---
type: concept
aliases: [磷酸肌酸, 肌酸磷酸, PCr, phosphocreatine, creatine phosphate]
tags: [exercise-physiology, metabolism, foundation]
sources: [source-Goulding-2021-VO2-kinetics-tolerance, source-Chorley-2022-bi-exponential-reconstitution, source-Skiba-2015-intramuscular-determinants, source-Kemp-1993-PCr-resynthesis-control, source-McMahon-2002-PCr-resynthesis, source-Chidnok-2013-intermittent-31P-MRS]
prerequisites: [ATP（adenosine triphosphate，三磷酸腺苷）]
created: 2026-06-11
updated: 2026-06-11
---

# 磷酸肌酸（phosphocreatine, PCr）

## 本質（一句話）
PCr 是肌肉的「瞬間 ATP 補充包」——一小桶隨時可動用的磷酸，在毫秒之內把用過的 ADP 充回 ATP，撐住運動最開頭那幾秒，等有氧主引擎慢慢跟上。

## 前置概念
- [[ATP|ATP（adenosine triphosphate，三磷酸腺苷）]]
  （PCr 的全部工作就是「補 ATP」；先懂 ATP 是即時現金、存量極小、必須邊花邊補。）

## 為什麼會這樣（first-principles 推導）
1. 由 [[ATP|ATP]]：肌肉裡的 ATP 只夠幾秒，運動一開始需求瞬間跳高，但有氧的氧化磷酸化要花時間才轉得上來（這段慢就是 [[VO2 kinetics|VO2 動力學]]）。中間這幾秒得有人**立刻**頂上。
2. PCr 就是那個立刻頂上的角色：它是一個**帶高能磷酸**的分子。酵素 [[Creatine kinase equilibrium|肌酸激酶（creatine kinase, CK）]] 把 PCr 的磷酸直接轉給 ADP，瞬間補成 ATP（CK 的催化能力數倍於最大 ATP 水解速率，所以這步幾乎即時、也讓反應永遠近乎平衡——這條平衡把 PCr/ATP/ADP/酸綁成連動體的完整後果見 [[Creatine kinase equilibrium|肌酸激酶平衡]]）：
   $$PCr + ADP \rightleftharpoons 肌酸 + ATP$$
3. 為什麼它最快？因為這是**單一步反應、不需氧氣、不必跑多步代謝**，幾乎是即時的。所以它主宰運動的**最初幾秒**，把「需求瞬間跳高、供給慢慢爬」之間的落差磨平。
4. 代價與後果（關鍵線索）：每用掉一個 PCr，就**釋放一個游離磷酸（Pi）**到細胞裡。所以**PCr 下降和 Pi 上升是同一個反應的兩面**——你看到肌肉 PCr 掉多少，就對應 Pi 升多少。而 Pi 一多會干擾收縮機器（通往 [[Inorganic phosphate|無機磷酸（Pi）與疲勞]]）。換句話說，PCr 既是「買時間的救火隊」，也是「臨界閾值模型裡那個會累積的 Pi 的主要來源」。
5. PCr 在兩個既有概念裡的位置：
   - 它是 [[O2 deficit|氧虧]] 的一部分（運動開頭、VO2 還沒跟上前，向 PCr「借」的那份能量）。
   - 它是 [[W prime|W′]] 的一部分（臨界功率之上那筆有限的非氧化儲備）。
6. CK 反應還有「緩衝」作用：它在粒線體和收縮機器之間**搬運能量、並把 ADP 的劇烈起伏壓平**（ADP 正是粒線體的油門訊號，見 [[Mitochondrial respiratory control|粒線體呼吸控制]]）。正因為它在中間當緩衝，CK 的活性會**影響 [[VO2 kinetics|VO2 動力學]] 的快慢**——實驗上抑制 CK 反而讓 VO2 動力學變快，但同時嚴重破壞 ATP 恆定與肌肉出力（代價慘重）。這說明那段「慢」不是缺陷，是保護。
7. 恢復（PCr resynthesis）：運動後，**靠有氧代謝把 PCr 重新充回來**；補回的速率正比於「還缺多少」，所以走一條先快後慢的指數曲線，最高速率封頂在粒線體容量——**完整機制（為什麼純有氧、為什麼是指數、什麼決定速率）已獨立成頁 [[Phosphocreatine resynthesis|磷酸肌酸再合成]]**。這裡只留重點結論：「PCr 充回來的速度」本身就是一個**粒線體（有氧）功能的指標**——充得快代表有氧機能好。實測 PCr 再合成的時間常數約 τ＝25–29 s（小腿約 25 s、股外側肌約 29 s；Skiba 2015 在單腿伸膝量到 t½≈39 s、τ≈57 s，量級一致）；這個數值正好和 [[Bi-exponential W prime reconstitution model|W′ 回填雙指數模型]] 的「快段 τ_FC（≈21 s）」吻合——這是「W′ 回填的快段≈PCr 補回」這個對應的關鍵證據。
   - **但要記得一個分寸（Skiba 2015）**：PCr 補得快（t½≈39 s），[[W prime|W′]] 補得慢得多（t½≈232 s，約 6 倍差），兩者的回補**速度**其實對不上（τ 無顯著相關）。所以 PCr 與 W′ 綁在一起的是「有氧可用**空間**（D_[PCr]，即 [[Oxidative reserve|氧化儲備]]）」這個容量差、不是補回速度——「快段＝PCr」要在這個 nuance 下理解（詳見 [[W prime reconstitution]] 推導第 11 點）。
8. **靜息存量與纖維型差異（補充事實）：** 靜息肌肉的 PCr 約是 ATP 的 **4–5 倍**（存得夠多，才當得了緩衝）；而**快縮（Type II）纖維比慢縮（Type I）多存約 55% 的 PCr**（也多約 42% ATP）。但反過來，Type I **補回** PCr 較快（毛細血管、粒線體、氧化酵素都較多）——「誰存得多」與「誰補得快」是兩回事，後者見 [[Muscle fiber types|肌纖維類型]]。

9. **在間歇運動裡，PCr 隨衝刺/恢復呈「鋸齒狀」升降，是 W′ 能反覆動用的肌內底料（Chidnok 2013）。** 用 ³¹P-MRS 在間歇運動當下連續量 [PCr]：每個超 CP 衝刺段 [PCr] 往下掉、每段降回 CP 以下的休息 [PCr] 往回補，畫出鋸齒。休息愈長補回愈多——這正是「恢復段補桶」這個抽象動作的肌肉實體（PCr 被重新合成回來），也使整場能做的 [[Work done above critical power|超 CP 功]] 超過單次 W′（W>CP 超過 W′ 的量與 [PCr] 回補幅度相關 r=0.61，見 [[W prime reconstitution|W′ 回填]]）。兩個延伸觀察：①整場後段同樣休息時間補回的 [PCr] 愈來愈少（回補變慢，歸因 [[Intracellular pH|pHi]] 下降）；②[PCr] 這種鋸齒動力學與 V̇O₂ 的動力學相似——兩者同受氧化磷酸化的回饋控制（[[Mitochondrial respiratory control|粒線體呼吸控制]]、[[VO2 kinetics|VO2 動力學]]），所以拉長恢復同時鈍化「[PCr] 往力竭低值掉」與「V̇O₂ 往最大值爬」。

## 易誤解之處
1. **PCr 不是「能量主力」，是「時間差的橋」。** 它總量小、只夠幾秒；它的價值在**時機**（補上最開頭的缺口），不在**總量**。把它當成主要能源會誤判——真正耐久的能量來自有氧氧化。
2. **「PCr 下降」和「Pi 上升」講的是同一件事。** 別把它們當兩個獨立現象；它們是 CK 反應的左右兩邊。這也是為什麼用 ³¹P-MRS 量肌肉時，PCr↓ 與 Pi↑ 總是相伴出現。
3. **充回 PCr 需要氧（詳見 [[Phosphocreatine resynthesis|磷酸肌酸再合成]]）。** 雖然「用」PCr 不需氧，但「補」PCr 靠有氧代謝。所以間歇運動能反覆動用 PCr，前提是恢復段有足夠有氧供應——這條也是 [[W prime|W′]] 回填的生理基礎之一。

## 用生活例子再講一次
把 PCr 想成相機的閃光燈電容：主電池（粒線體有氧供能）反應慢，但電容能在你按下快門的瞬間**立刻放出一大股電**點亮閃光，撐過那一瞬，之後再由主電池慢慢把電容充回來。肌肉收縮的頭幾秒就靠這個「電容」頂著，等有氧引擎轉上來。每放一次電，也順帶在系統裡留下「廢渣」（Pi），放太多次廢渣就堆積。

（這個類比在哪裡會失準：相機電容只管供電、不留下會干擾相機的副產物；肌肉的 PCr 一用就釋放 Pi，而 Pi 會反過來干擾收縮，這個「副產物會搞事」是金屬電容沒有的。）

## 換句話說
換句話說，磷酸肌酸是肌肉的瞬間 ATP 補充包：靠肌酸激酶在毫秒間把 ADP 充回 ATP，撐過運動最開頭、有氧引擎還沒跟上的那幾秒。它買來的時間有代價——每用一份就釋放一份 [[Inorganic phosphate|無機磷酸（Pi）]]，所以「PCr 掉」就是「Pi 升」，這正是後面 [[Critical Pi threshold and positive feedback model|臨界閾值模型]] 裡那個會累積的疲勞訊號的來源。

## 來源
- [[source-Chorley-2022-bi-exponential-reconstitution]]（推導第 7 點：引用的 PCr 再合成 τ 數值（van den Broek 股外側肌≈29 s、Haseler 小腿≈25 s）與其雙指數 W′ 回填快段 τ_FC≈21.5 s 吻合，作為「FC≈PCr」對應的依據。）
- [[source-Goulding-2021-VO2-kinetics-tolerance]]（"VO2 kinetics and the O2 deficit" 節：PCr 分解屬受質層次磷酸化、構成 O2 deficit；CK 緩衝 ADP 回饋、抑制 CK 加速 VO2 動力學卻損害出力；PCr 與 Pi 的鏡像關係見 "critical threshold" 節。基礎生化屬通識，建檔以支援 [[O2 deficit]]、[[Inorganic phosphate]]、[[W prime]]。）
- [[source-Skiba-2015-intramuscular-determinants]]（推導第 7 點：³¹P-MRS 量單腿伸膝 [PCr] 再合成為單指數、t½≈39 s（τ≈57 s），與其他文獻 25–29 s 量級一致；PCr 為有氧機能指標；並指出 [PCr] 補回比 W′（t½≈232 s）快約 6 倍、τ 不相關，故 PCr 與 W′ 綁定的是 D_[PCr] 容量差（[[Oxidative reserve|氧化儲備]]）而非速率。）
- [[source-Kemp-1993-PCr-resynthesis-control]]（推導第 7 點與易誤解 #3：PCr 再合成的控制機制——恢復期 R＝淨氧化 ATP 合成、對 [ADP] 雙曲線/對 [Pi] 線性故近單指數、Vmax≈40 mmol/L/min＝粒線體容量、低 pH 拖慢；完整推導移至獨立頁 [[Phosphocreatine resynthesis]]。）
- [[source-McMahon-2002-PCr-resynthesis]]（第 1、4 節：CK 催化能力數倍於最大 ATP 水解速率→PCr 緩衝 [ATP]（運動中 [PCr] 可降至 <30–40%、[ATP] 極少低於靜息 70%）；靜息 [PCr]≈4–5×[ATP]；Fitts 整理快縮纖維比慢縮多約 55% PCr／42% ATP。CK 別名已移至 [[Creatine kinase equilibrium]]。）
- [[source-Chidnok-2013-intermittent-31P-MRS]]（推導第 9 點：間歇運動中 ³¹P-MRS 量到 [PCr] 鋸齒狀升降（衝刺掉、休息補）、休愈久補愈多、整場後段回補變慢（歸因 pHi 下降）；恢復期 [PCr] 回補是 W′ 反覆動用的肌內基礎、與 W>CP 超過 W′ 的量相關 r=0.61；[PCr] 動力學與 V̇O₂ 動力學相似（皆受氧化磷酸化回饋控制）。）
