---
type: concept
aliases: [肌酸激酶平衡, 肌酸激酶反應, CK平衡, creatine kinase equilibrium, CK equilibrium, creatine kinase reaction, 肌酸激酶, creatine kinase, CK, 質量作用比, mass action ratio]
tags: [exercise-physiology, metabolism, foundation, mechanism]
sources: [source-McMahon-2002-PCr-resynthesis, source-Whipp-2006-pulmonary-CO2-O2-dissociation]
prerequisites: [ATP（adenosine triphosphate，三磷酸腺苷）, 磷酸肌酸（phosphocreatine, PCr）, 無機磷酸（inorganic phosphate, Pi）]
created: 2026-06-11
updated: 2026-06-11
---

# 肌酸激酶平衡（creatine kinase equilibrium, CK equilibrium）

## 本質（一句話）
肌酸激酶平衡就是「**PCr ＋ ADP ＋ 酸（H⁺） ⇌ ATP ＋ 肌酸**」這條反應，因為它的酵素快得不像話、永遠停在近乎平衡的狀態——於是這條等式像一條繃緊的橡皮筋，把 PCr、ATP、ADP、Pi、酸五個量綁成一個連動體：動其中一個，其餘全跟著調整。它是「PCr 為什麼能瞬間穩住 ATP」「酸為什麼會壓住 PCr 補回」「看不見的 ADP 為什麼還能被算出來」這三件事的共同根。

## 前置概念
- [[ATP|ATP（adenosine triphosphate，三磷酸腺苷）]]
  （這條反應的目的就是補 ATP；先懂 ATP 是即時現金、存量極小、必須邊花邊補。）
- [[Phosphocreatine|磷酸肌酸（phosphocreatine, PCr）]]
  （PCr 是這條反應的另一主角，肌肉的瞬間 ATP 補充包；本頁把「PCr 這顆分子」升級成「PCr 所在的那條被鎖死的反應」。）
- [[Inorganic phosphate|無機磷酸（inorganic phosphate, Pi）]]
  （Pi 雖不直接在 CK 反應式裡，卻和 PCr 鏡像連動、又是下游粒線體控制的訊號；下面會用到。）

## 為什麼會這樣（first-principles 推導）
一步一步來，每步只用前面已建立的事實：

1. **先看反應本身。** 酵素**肌酸激酶（creatine kinase, CK）**催化這條雙向反應（equation 2）：
   $$PCr + ADP + H^+ \rightleftharpoons ATP + 肌酸（creatine）$$
   往右讀＝**放電**：把 PCr 的高能磷酸轉給 ADP、瞬間補成 ATP（順帶吃掉一個 H⁺）。往左讀＝**充電**：用有氧做出來的 ATP 把肌酸重新磷酸化回 PCr（順帶放出一個 H⁺）。同一條反應，兩個方向。

2. **關鍵性質一：這個酵素快到爆。** CK 的催化能力比肌肉**最大 ATP 水解速率還高好幾倍**。意思是：不論系統需要它往哪個方向跑、跑多快，它的產能都綽綽有餘，任何把它推離平衡的擾動，它都**瞬間就拉回平衡**。所以這條反應**永遠維持在近乎平衡（near-equilibrium）**——這點要放慢講：多數代謝反應是「遠離平衡、單向猛跑」的水龍頭，CK 不是；CK 像一個反應極快的天平，你怎麼戳它，它都立刻回到平衡點。一個隨時在平衡的反應，就隨時滿足它的「平衡關係式」。

3. **近平衡 → 一條把五個量鎖死的等式（質量作用比 mass action ratio）。** 化學的鐵律：一個反應在平衡時，產物濃度與反應物濃度的某個特定比值＝一個常數（平衡常數 Keq）。對 CK（忽略 Mg²⁺）這個比值寫成（equation 4）：
   $$Y = \frac{[肌酸][ATP]}{[PCr][ADP][H^+]} \approx K_{eq} \approx 1.66 \times 10^{9}\ \text{mol}^{-1}$$
   （在 pH 7、38°C、離子強度 0.25、1 mmol 游離 Mg²⁺ 的條件下量得）。因為 CK 永遠近平衡，這條 **Y ≈ Keq 隨時都成立**。它就是那條橡皮筋：五個濃度被綁在同一條等式上，誰都不能各自亂跑。下面三個後果全是從這一條等式長出來的。

4. **後果一：PCr 緩衝 ATP（穩住能量現金）。** 肌肉裡 PCr 的存量是 ATP 的 **4–5 倍**，加上 CK 又快——所以你一旦花掉 ATP（[ATP] 想掉、[ADP] 想升），CK 立刻**往放電方向**拆 PCr 來補 ATP，把 [ATP] 拉回去。結果：劇烈運動中 [PCr] 可以掉到剩不足靜息的 30–40%，[ATP] 卻幾乎不動（極少低於靜息的 70%）。這正是 [[ATP|ATP]] 那頁說的「ATP 存量極小卻能維持恆定」的底層機制——**CK 平衡在當那台穩壓器**。

5. **後果二：酸（H⁺）會反過來卡住 PCr 補回——這條要慢講，是本頁最重要的一步。** 看反應式：**充電（補 PCr）這個方向會放出 H⁺**。所以如果細胞**已經很酸**（[H⁺] 已經很高），就等於「產物端已經堆滿了 H⁺」，依勒沙特列原理（Le Chatelier，產物多就反過來壓抑正向反應），這會**反過來阻止再多做 PCr**——這叫**終產物抑制（end-product inhibition）**。一句話：**肌肉愈酸，把 PCr 補回去就愈吃力**。而且因為運動後 [ADP] 在前段就先恢復、酸卻要更久才退，這份 H⁺ 的阻力主要落在 **PCr 補回的後段（慢段）**。這就是 [[Phosphocreatine resynthesis|PCr 再合成]] 為什麼是「先快後慢、慢段被 pH 限速」的機制根。（酸本身怎麼來、怎麼退，見 [[Intracellular pH|細胞內 pH]]。）

6. **後果二之延伸（CO₂ 端）：運動起始的「淨拆 PCr」會吸掉 H⁺，使肌肉暫時變鹼、扣住一點 CO₂。** 運動一開始是淨**放電**方向（PCr→ATP，等式由左往右），這個方向**消耗一個 H⁺**（量化係數 γ≈0.5）。H⁺ 被吸走 → 肌肉內、乃至運動肌靜脈血**暫時鹼化**（Wasserman 1997 量到靜脈端短暫鹼化）。而由碳酸氫根化學（見 [[Body CO2 stores]]），環境一變鹼，平衡就把 CO₂ 多**留在組織裡**少放出——於是有一小部分代謝產的 CO₂ 在運動起始被「暫時扣留」。這是 CK 平衡在**氣體交換**上的後果：它是 [[Muscle-to-lung gas exchange dissociation|肌肉到肺 V̇CO₂ 起始落後]]的次要來源之一（主因仍是 CO₂ 高容量倉庫的延遲）。

7. **後果三：看不見的 ADP，可以用這條等式反算出來。** 後面會看到，量肌肉代謝物的主力工具 [[Phosphorus-31 magnetic resonance spectroscopy|³¹P-MRS]] 量得到 ATP、PCr、Pi，卻**量不到自由 ADP**（它濃度太低、又多半結合在蛋白上）。但既然 Y ≈ Keq 把五個量鎖死，只要其他幾個量到、再給定 H⁺，第五個（ADP）就能用 equation 4 **反解出來**。這點極其要緊：**整個領域之所以能談「[ADP] 控制粒線體呼吸」（見 [[Mitochondrial respiratory control|粒線體呼吸控制]]），靠的就是這招——文獻裡的 [ADP] 從來不是直接量到的，是從 CK 平衡算出來的。** 它既是強大工具，也是一個**假設層**：萬一 CK 沒真的在平衡、或 Keq 取值有偏差，算出的 [ADP] 就跟著有偏差。

## 文獻怎麼說 vs 為什麼這樣說
- **主張**：CK 反應在運作中維持近乎平衡，其質量作用比 Y 約等於 Keq≈1.66×10⁹ mol⁻¹；這條近平衡關係(a)使 PCr 緩衝並穩住 [ATP]、(b)使 pHi 透過 H⁺ 影響 [PCr] 與 PCr 再合成、(c)使無法直接偵測的自由 [ADP] 可被計算。
- **背後的推理／證據**：(1) CK 的催化能力**數倍於**肌肉最大 ATP 水解速率（Newsholme、Wegener）——酵素遠快於系統其他變化，反應就沒機會偏離平衡，故近平衡（McGilvery & Murray、Matthews 的 ³¹P-NMR 飽和轉移研究均支持 CK 維持近平衡）。(2) 多份研究量到肌肉 pHi 與 CK 質量作用比**強相關**（Sahlin 等 r=0.92、p<0.01；另一研究 r=0.85），直接證明「pH 一動、CK 平衡狀態就跟著動，從而決定 [PCr]」。(3) 既然平衡式鎖死五個量，給定可量的四個就能反解第五個——這是計算 [ADP] 的方法論基礎。

## 易誤解之處
1. **「近平衡」不等於「靜止／不流動」。** CK 隨時在雙向猛跑、淨流量可大可小（放電時大量往右、充電時大量往左）；「平衡」指的是兩邊**比值**隨時維持 Keq，不是反應停下來。把平衡讀成靜止，就會以為「PCr 緩衝」是慢吞吞的——其實它是毫秒級的。
2. **論文裡的 [ADP] 是「算」出來的，不是「量」出來的。** 看到 [ADP]≈30 μmol/L 之類數字，要記得它是用 CK 平衡＋一串假設（[ATP]、總肌酸、Keq 等）反推的；它的可信度**繼承**了這些假設。這也是為什麼「[ADP] 控制」與「ΔG_ATP 控制」之爭難分（見 [[Mitochondrial respiratory control]]）——連 [ADP] 本身都是推算值。
3. **酸影響 PCr 是「透過這條等式」，不是 H⁺ 去腐蝕 PCr 分子。** H⁺ 是反應的**參與者**（就站在等式裡），所以它一變，平衡位置就移、[PCr] 跟著移——這是化學平衡的事，不是化學破壞。把它想成「酸把天平往某邊壓」而非「酸把 PCr 溶掉」。
4. **Keq 是「條件常數」。** 1.66×10⁹ 只在特定 pH／溫度／離子強度／Mg²⁺ 下成立；條件變，值就變。教學上記住「有這麼一個大常數把五個量綁在一起」這個圖像即可，不必背數字。

## 用生活例子再講一次
把 CK 平衡想成一台**極靈敏的天平，旁邊站著一個手速快到看不見的店員**。天平兩端是「ATP ＋ 肌酸」對「PCr ＋ ADP ＋ 酸」。店員（CK 酵素）只要看到天平一歪，**瞬間**搬砝碼回到平衡。於是三件事自然發生：你從一端拿走一點 ATP（花掉），店員立刻從 PCr 那端拆磷酸補回 ATP（**PCr 緩衝**）；你往「酸」那一端不斷加重（肌肉變酸），天平就**更難往「多做 PCr」那邊倒**（**酸拖慢 PCr 補回**）；而就算有一顆砝碼（ADP）小到你肉眼看不見，只要其他砝碼重量和平衡點都知道，你就能**反推出它多重**（**算 ADP**）。

（這個類比在哪裡會失準：真天平是「重量相加」的線性平衡，CK 平衡是**化學平衡**——綁住的是濃度的**乘積比**等於常數，不是簡單加總；而且 PCr、ATP、ADP 還同時被別的反應（醣解、氧化磷酸化、ATP 水解）拉扯，不是一台與世隔絕的天平。所以類比抓得到「五個量連動、店員秒回平衡」的主軸，但別把它當成真的算術天平。）

## 換句話說
換句話說，肌酸激酶平衡是「因為 CK 這個酵素快得不像話，PCr ＋ ADP ＋ H⁺ ⇌ ATP ＋ 肌酸 這條反應永遠卡在近平衡」，於是 PCr、ATP、ADP、Pi、酸被一條 Y≈Keq 的等式綁成連動體。這條連動帶來三個一直在用的後果：PCr 能在毫秒間緩衝、穩住 [[ATP|ATP]]；酸（H⁺ 就在等式裡）會反過來卡住 [[Phosphocreatine resynthesis|PCr 補回]]的後段；看不見的 [ADP] 能從等式反算出來，整個「[[Mitochondrial respiratory control|ADP 控制粒線體]]」的研究才得以成立。

## 來源
- [[source-McMahon-2002-PCr-resynthesis]]（第 1、3、4、6 節：CK 催化能力數倍於最大 ATP 水解速率故反應近平衡（equation 2：PCr+ADP+H⁺⇌ATP+肌酸）；質量作用比 equation 4 Y=[肌酸][ATP]/([PCr][ADP][H⁺])≈Keq≈1.66×10⁹ mol⁻¹（pH 7、38°C、離子強度 0.25、1 mmol 游離 Mg²⁺）；近平衡使自由 ADP 雖低於 ³¹P-NMR 偵測閾仍可由平衡式反算；PCr 存量為 ATP 的 4–5 倍＋CK 快→PCr 緩衝 [ATP]（[ATP] 極少低於靜息 70%、[PCr] 可降至 <30–40%）；H⁺ 在質量作用比內→酸限制 PCr 再合成後段，Sahlin 等量到 pHi 與 CK 質量作用比 r=0.92／0.85。）
- [[source-Whipp-2006-pulmonary-CO2-O2-dissociation]]（CO₂ 端後果：質子捕捉式 [PCr]+[ADP]+γ[H⁺]⇌[ATP]+[Cr]+[Pi]，γ≈0.5（Kemp 2005、Kushmerick 1997）；淨拆 PCr 吸 H⁺→肌肉與運動肌靜脈暫時鹼化（Wasserman 1997）→暫扣部分代謝 CO₂。對應推導第 6 步。）
