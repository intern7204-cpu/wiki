---
type: concept
aliases: [粒線體呼吸控制, 呼吸控制, respiratory control, mitochondrial respiratory control, ADP control, ADP控制, 氧化磷酸化調控, oxidative phosphorylation regulation, 粒線體ATP合成調控, adenine nucleotide translocase, ANT]
tags: [exercise-physiology, metabolism, mechanism, foundation]
sources: [source-Kemp-1993-PCr-resynthesis-control, source-McMahon-2002-PCr-resynthesis, source-Korzeniewski-2013-VO2-PCr-off-kinetics]
prerequisites: [細胞呼吸（cellular respiration）, ATP（adenosine triphosphate，三磷酸腺苷）, 無機磷酸（inorganic phosphate, Pi）]
created: 2026-06-11
updated: 2026-06-12
---

# 粒線體呼吸控制（mitochondrial respiratory control）

## 本質（一句話）
粒線體不是隨時開到最大、也不是固定一檔，而是「**你花掉多少能量，它就回頭被催出多少**」——肌肉每用掉一份 ATP 都會留下 ADP，而升高的 ADP 正是那個自動把粒線體油門踩下去的訊號。

## 前置概念
- [[Cellular respiration|細胞呼吸（cellular respiration）]]
  （粒線體用氧氣把食物氧化、產出 ATP，這條路叫氧化磷酸化；本頁談的是「這條路的速率由什麼控制」。）
- [[ATP|ATP（adenosine triphosphate，三磷酸腺苷）]]
  （花 ATP＝把它折成 ADP＋Pi；先懂「ATP 存量極小、必須邊花邊補」，才懂為什麼需要一個自動調速機制。）
- [[Inorganic phosphate|無機磷酸（inorganic phosphate, Pi）]]
  （ADP 與 Pi 是同一個「付錢動作」一起放出的兩個訊號；下面會用到 Pi 這條平行線索。）

## 為什麼會這樣（first-principles 推導）
一步一步來，每一步只用前面已建立的事實或常識：

1. 由 [[ATP|ATP]]：肌肉裡存的 ATP 只夠幾秒，所以**用掉的速率必須隨時被補上**。補 ATP 的耐久主力是粒線體的氧化磷酸化（[[Cellular respiration|細胞呼吸]] 那條路）。問題來了：粒線體怎麼知道「現在該補多快」？靜止時補慢一點、衝刺時補快一點——這個「該補多快」的資訊，必須有個訊號傳給粒線體。

2. 先找那個訊號。每次 ATP 被花掉，就變成 **ADP（雙磷酸腺苷，就是 ATP 少一個磷酸）＋ 一個游離磷酸（[[Inorganic phosphate|Pi]]）**。所以：**花得愈兇 → ADP 與 Pi 累積得愈多**。反過來，ADP／Pi 的濃度就是一個現成的「能量被花了多少」的計量器——它天生就帶著「需求有多高」的資訊。

3. 關鍵一步：**粒線體就是用 ADP 當油門訊號的。** ADP 要先被運進粒線體內膜（負責這趟運送的是一個叫**腺嘌呤核苷酸轉位酶（adenine nucleotide translocase, ANT）**的搬運蛋白——這裡只給一句 gloss：它把外面的 ADP 換進去、把做好的 ATP 換出來），ADP 一進去就驅動氧化磷酸化把它做回 ATP。所以**外面 ADP 愈多，這台機器轉得愈快**。這就叫「呼吸控制（respiratory control）」：呼吸（粒線體耗氧產能）的速率被 ADP 牽著走。

4. 但這個「ADP 愈多轉愈快」不是直線到底，而是**會飽和**——這點要放慢講。想像粒線體像一個收件處理員：桌上待辦（ADP）堆得愈高，他做得愈快；但他有個**體能上限**，待辦堆到某個程度後，再多堆也快不上去了，他就維持在最高速。用生化的話講，速率對 [ADP] 是一條**雙曲線（hyperbolic，亦即米氏 Michaelis–Menten 飽和曲線）**：
   - 低 [ADP] 時，速率幾乎正比於 [ADP]（待辦不多，多一件就多做一件）；
   - 高 [ADP] 時，速率逼近一個最高值 **Vmax**（已經全速，再多待辦也沒用）。
   - 描述「轉到一半速時需要多少 ADP」的數字叫 **Km**（半飽和濃度）；本文獻在人前臂肌量到 **Km ≈ 30 μmol/L 細胞水**，**Vmax ≈ 40 mmol/L 細胞水/分鐘**。

5. 那個 Vmax 是什麼？就是**這塊肌肉的粒線體總產能上限**——粒線體愈多、愈健康，Vmax 愈高。所以 Vmax 不是普世常數，而是「這個人、這塊肌肉的有氧機能」的直接量。（後面會看到：在粒線體疾病裡 Vmax 掉下來，正好驗證了這一點。）

6. 還有一條**平行的線索**：速率對 [Pi]（也對 [PCr]、[肌酸]）反而近乎**直線**，不是雙曲線。為什麼同一台機器，對 ADP 是曲線、對 Pi 是直線？因為這些濃度被一條鐵律綁在一起——**[[Creatine kinase equilibrium|肌酸激酶平衡（creatine kinase equilibrium）]]**：PCr＋ADP＋H⁺ ⇌ 肌酸＋ATP 隨時維持平衡，使 [ADP]、[PCr]、[Pi]、pH 互相牽動，不能各自亂跑。在正常肌肉的運作範圍裡，這層約束讓「對 Pi 近乎線性」與「對 ADP 飽和」兩個面貌同時成立、並不矛盾——它們是同一台被約束的機器照出來的兩張臉。（本文獻主張**底層的真正控制變數是 [ADP]**，對 Pi 的線性是約束下的衍生現象。）

7. 把這條控制律的後果收一下（接到 wiki 既有的兩個地方）：
   - **為什麼供能能自動跟上需求**：需求一升，ADP/Pi 一升，粒線體就被催快——這是個**負回饋自動調速**（鍋爐燒得旺、ATP 補得快、ADP 被消掉、訊號回落）。
   - **為什麼會有「跟不上的那一段」（[[O2 deficit|氧虧]]／τ）**：訊號要先**累積**起來才能把粒線體催到位，所以運動一開始粒線體不會瞬間全速，而是隨 ADP/Pi 爬升才漸漸跟上——這段「催起來的延遲」正是 [[VO2 kinetics|VO2 動力學]] 有一個 τ（時間常數）的最底層原因。換句話說，**VO2 為什麼是「指數式逼近」而不是「瞬間到位」，根就在呼吸控制是被代謝物訊號牽著走的。**

8. **但「ADP 回饋」不是控制的全部——還要加一層「前饋」（接 Korzeniewski 2013）。** 上面整條都是**回饋**：先有 ADP/Pi 堆積，才有粒線體加速。可是實測發現一個怪事：從靜息到運動 VO2 能升十幾到三十幾倍，**ADP 卻只升幾倍、pH 幾乎不動**。若粒線體**只**靠 ADP 訊號被推，要把產能拉高那麼多，ADP 就得堆得很高——但沒有。Korzeniewski 的電腦模型主張：一定還有一個**前饋（feed-forward）**機制——肌肉收縮的 Ca²⁺ 訊號**同時直接把氧化磷酸化的每一步都調快一檔**（即 [[Parallel activation of oxidative phosphorylation|平行活化／每步活化]]），讓產能在 ADP 還沒怎麼升之前就先拉高。所以完整圖像是**回饋（ADP/Pi）＋前饋（Ca²⁺ 平行活化）並存**：本頁的 ADP 控制仍對、仍在，只是不必把 ADP 堆得很高——這也是肌肉 [[Metabolic stability|代謝穩定性]] 為何能那麼好的結構原因。這個前饋活化在運動後以一個時間常數 τ(OFF) 退場，而 τ(OFF) 又牽動恢復期 VO2 與 PCr 的動力學（見 [[Inverse VO2-PCr off-kinetics relationship|反向關係]]）。

## 文獻怎麼說 vs 為什麼這樣說
- **主張**：在活體人類肌肉，粒線體的 ATP 合成速率對 [ADP] 呈**雙曲線（飽和）**依賴（Km≈30 μmol/L），可以解釋所有其他相關性；底層機制是 **ADP 在腺嘌呤核苷酸轉位酶（ANT）上的動力學控制**。
- **背後的推理／證據**：(1) 用 ³¹P-MRS（一種隔著皮膚、用磁振訊號量肌肉內含磷代謝物濃度的非侵入工具）追蹤運動後恢復，把「PCr 補回的速率」當作「氧化 ATP 合成速率」的活體量尺（為什麼能這樣，見 [[Phosphocreatine resynthesis|磷酸肌酸再合成]]）；(2) 量到的速率對 [ADP] 確實是雙曲線、對 [Pi] 是直線；(3) 這個 Km≈30 μmol/L 與**離體粒線體**及**動物肌肉**的數據一致——活體、離體、不同物種對得上，才有底氣說這是真的控制律。
- **要誠實的爭議（[ADP] 控制 vs ΔG_ATP 控制）**：「到底是 [ADP] 控制，還是 **ATP 水解的自由能（ΔG_ATP）**控制」在文獻上長期未定論。ΔG_ATP 是「一份 ATP 此刻實際能放出多少能量」的熱力學量，把 [ATP]、[ADP]、[Pi]、pH 綁在一條式子裡（運動時可從約 −60 降到 −48 kJ/mol）。Kemp 1993 偏 [ADP] 這一邊；McMahon & Jenkins 盤點的證據讓兩造都站得住：Brindle 量到 Pi↔ATP 通量對 [ADP] **線性**（至 90 μmol）；但 Barstow 發現代謝率對 [ADP] 在約 **70% 最大代謝率以上偏離雙曲線**、卻對 ΔG_ATP **全程線性**（r=0.997）→高功率下可能改由 ΔG_ATP 主導。化解之道在 Krause & Wegener：不論主控是哪個，因為 **ΔG_ATP 本身被 [ADP] 牽動**（[ADP]↑ 使 ΔG_ATP 變小），**[ADP] 都居核心**。教學上記住核心圖像即可：**粒線體是被『能量花掉的訊號』牽著走的需求驅動系統**；那個訊號精確該記成 [ADP] 還是 ΔG_ATP，是更細的學術爭點（wiki 長期 pending ① 即此）。

## 易誤解之處
1. **「粒線體被催快」不等於「肌肉缺氧」。** 呼吸控制講的是「ADP 訊號把粒線體油門踩下去」，這在氧氣充足時照樣發生——油門踩深是因為**需求**高，不是因為**缺氧**（見 [[Dysoxia|dysoxia]]）。把「代謝加速」讀成「組織缺氧」是運動生理裡最頑固的老錯誤。
2. **對 ADP 是『雙曲線』，不是『直線』。** 低 ADP 時多一點 ADP 很有用，高 ADP 時幾乎沒用——這個飽和性很重要：它意味著粒線體有個**封頂速度（Vmax）**，這正是 [[VO2max|VO2max]] 與「有氧能力上限」在分子層次的影子。把它想成永遠線性，就會誤以為「ADP 再高還能無限加速」。
3. **Vmax 是「這塊肌肉的有氧上限」，會因人、因訓練、因疾病而變——不是常數。** 粒線體多／健康 → Vmax 高 → 同樣的需求只需較低的 ADP/Pi 就應付得了（代謝被擾動得小，即 [[Metabolic stability|代謝穩定性]] 高）。這條是「練有氧 = 把這台調速機器升級」的根。
4. **呼吸控制（正常調速）≠ [[Critical Pi threshold and positive feedback model|臨界 Pi 正回饋]]（失控）。** 本頁講的是健康的**負回饋**：訊號升、補得快、訊號被壓回去，系統穩定。但在 [[Critical power|CP]] 之上，「補得快」本身要付出效率代價、反而製造更多 Pi，負回饋翻成**正回饋**而失控——那是另一頁的事。先把「正常怎麼穩」搞懂，才看得懂「什麼時候會穩不住」。

## 用生活例子再講一次
把粒線體想成一個**裝了調速器的抽水馬達**，任務是把水箱（ATP）一直保持滿。你每用掉一瓢水，水位就掉一點（ADP/Pi 升）——而這台馬達的設計是：**水位掉得愈低，它自動轉得愈快**去補。所以你不必手動控制馬達，它會自己跟著「缺多少」調速，這就是呼吸控制。但馬達有個**最高轉速（Vmax）**：水位再低，它也只能到那個上限——而這個上限取決於馬達本身多大台（粒線體多寡、健康程度）。換一台更大的馬達（練出更多粒線體），同樣的用水量只需要它轉到較低的檔位就能跟上，水位幾乎不掉（代謝很穩）。

（這個類比在哪裡會失準：真馬達的「水位低→轉快」是工程師裝的調速器外加上去的；粒線體的「ADP 高→轉快」不是外加裝置，而是化學反應本身的速率就被反應物 ADP 的濃度決定——是反應動力學的內建性質，不是另接的控制迴路。而且真馬達不會「因為水變酸」就變慢，粒線體會。）

## 換句話說
換句話說，粒線體呼吸控制就是「**用得多就補得多**」這條自動調速律：花掉 ATP 會放出 ADP 與 [[Inorganic phosphate|Pi]]，升高的 ADP 驅動粒線體（在 ANT 上）把 ATP 做回來，而且這個驅動是**飽和式**的——低濃度時正比、高濃度時封頂在 Vmax，而 Vmax 就是這塊肌肉的有氧產能上限。這條律有兩個一直會用到的後果：它讓供能能自動追上需求（負回饋穩定），也讓「追上」需要時間（訊號要先累積），後者正是 [[VO2 kinetics|VO2 動力學]] 有 τ、[[O2 deficit|氧虧]] 存在的最底層原因。而把這條律用在「運動後 PCr 怎麼補回來」，就得到一個量活體粒線體功能的乾淨窗口：[[Phosphocreatine resynthesis|磷酸肌酸再合成]]。

## 來源
- [[source-Kemp-1993-PCr-resynthesis-control]]（Introduction 與 "What does oxidation respond to?" 節：兩大控制假說（[ADP] 在 ANT 的動力學控制 vs ATP 水解自由能的線性控制）；氧化速率對 [ADP] 呈雙曲線（Km≈30 μmol/L 細胞水、Vmax≈40 mmol/L/min）、對 [Pi]/[PCr]/[肌酸] 近乎線性；肌酸激酶平衡與 [PCr＋Pi] 守恆兩條系統約束使各代謝物濃度互相牽動；活體 ³¹P-MRS、離體粒線體、動物肌肉三者的 Km 一致；作者偏 [ADP] 動力學控制但聲明其他調節者不能排除。）
- [[source-McMahon-2002-PCr-resynthesis]]（第 8 節「The Role of ADP」：粒線體 ATP 合成受胞質游離 [ADP] 控制（Brindle：Pi↔ATP 通量對 [ADP] 線性至 90 μmol；Kemp 等：對 [ADP] 雙曲線 Km≈30、Vmax≈40）；Barstow 報告代謝率在 ~70% 最大以上偏離 [ADP] 雙曲線、對 ΔG_ATP 線性（r=0.997）→高功率下 ΔG_ATP 可能主導；Krause & Wegener：30 s 游泳使 [ADP] 由 14 升至 156×10⁻⁶ mmol、ΔG_ATP 由 −60.61 降到 −47.90 kJ/mol，不論主控為何 [ADP] 皆居核心。補強 wiki pending ①「[ADP] vs ΔG_ATP 控制」之爭。）
- [[source-Korzeniewski-2013-VO2-PCr-off-kinetics]]（推導第 8 點：純 ADP 回饋無法解釋「VO2 升 13–32× 而 ADP 僅升 3–4.3×、pH 幾不動」，故須加上 Ca²⁺ 驅動的前饋平行活化（每步活化）；回饋＋前饋並存，[ADP] 控制仍在但不必被堆高；前饋以 τ(OFF) 退場、牽動恢復期動力學。完整見 [[Parallel activation of oxidative phosphorylation]]。）
