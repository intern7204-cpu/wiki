---
type: concept
aliases: [磷-31磁振頻譜, 磷磁振頻譜, 磷核磁共振, 31P-MRS, 31P-NMR, ³¹P-MRS, ³¹P-NMR, 31P磁振頻譜, phosphorus-31 magnetic resonance spectroscopy, phosphorus NMR, P-31 MRS]
tags: [exercise-physiology, methodology, measurement]
sources: [source-McMahon-2002-PCr-resynthesis]
prerequisites: [磷酸肌酸（phosphocreatine, PCr）, 無機磷酸（inorganic phosphate, Pi）, ATP（adenosine triphosphate，三磷酸腺苷）]
created: 2026-06-11
updated: 2026-06-11
---

# 磷-31 磁振頻譜（³¹P-MRS / ³¹P-NMR）

## 本質（一句話）
³¹P-MRS 是一種「隔著皮膚、不抽血也不切片，就能即時量到活肌肉**內部**含磷代謝物（PCr、Pi、ATP）濃度、還能順便算出細胞內酸度」的工具——它把運動生理對「肌肉裡此刻正發生什麼」的研究，從一針一針的切片**快照**，升級成可以連續看的**直播**。

## 前置概念
- [[Phosphocreatine|磷酸肌酸（phosphocreatine, PCr）]]
- [[Inorganic phosphate|無機磷酸（inorganic phosphate, Pi）]]
- [[ATP|ATP（adenosine triphosphate，三磷酸腺苷）]]
  （這三個含磷分子正是 ³¹P-MRS 量得到的主角；先懂它們是什麼，才懂這台機器在量什麼、量到的變化代表什麼。）

## 為什麼會這樣（first-principles 推導）
一步一步來：

1. **先講要解決的問題。** 想知道運動與恢復時肌肉裡的 PCr、Pi、ATP、酸怎麼變，傳統只能**切片（needle biopsy）**——會痛、一次只取一個時間點、無法連續、取樣本身還擾動肌肉。要研究「動力學」（東西**隨時間怎麼變**），急需一個**非侵入、能連續量**的辦法。³¹P-MRS 就是那個辦法。

2. **物理基礎（給一句 gloss 就好）。** 某些原子核天生帶磁性；磷的主要同位素 **³¹P** 就是。把它放進強磁場，這些核會像小磁針一樣排好隊；用特定頻率的無線電脈衝去「敲」它，它會先吸收、再放出同頻率的訊號被線圈接收。**關鍵的一招**：同樣是 ³¹P，**處在不同的化學分子裡**，周圍電子環境不同，感受到的局部磁場略有差異，於是它共振的頻率會**略微偏移**——這個偏移叫**化學位移（chemical shift）**。所以一張頻譜上，不同含磷分子會各自落在**不同位置**：峰的**位置**告訴你「這是哪個分子」，峰的**面積**告訴你「它有多少」。

3. **於是量得到什麼。** 肌肉的 ³¹P 頻譜上有幾個清楚的峰：PCr 一個、Pi 一個、ATP 三個（對應 ATP 上的三個磷）。每個峰面積正比於該分子的相對濃度。所以 **PCr↓、Pi↑ 這種變化可以即時讀出**（而且因為 [[Creatine kinase equilibrium|CK 平衡]]，PCr 掉多少就對應 Pi 升多少，兩者必相伴）。把這條曲線沿時間追下去，就得到 [[Phosphocreatine resynthesis|PCr 再合成]] 的動力學。

4. **量不到 ADP——但能『算』出來。** 自由 ADP 的濃度太低（低於約 1 mmol/L，沉在訊號雜訊裡），又多半結合在蛋白上（NMR 只看得到自由溶在水裡的），所以頻譜上**沒有 ADP 峰**。但由 [[Creatine kinase equilibrium|CK 平衡]]：只要量到 ATP／PCr／Pi（推得肌酸與 H⁺），就能用平衡式**反算 [ADP]**。這就是為什麼整個領域談得了「[ADP] 控制粒線體呼吸」（[[Mitochondrial respiratory control]]）——那個 [ADP] 是 ³¹P-MRS ＋ CK 平衡**算**出來的，不是直接量到的。

5. **順手還量到細胞內酸度（pHi）——這招很妙。** Pi 這個峰的**位置（化學位移）會隨酸度移動**：因為 Pi 的解離狀態（pKa）恰好落在生理 pH 附近，pH 一變、Pi 的帶電形態跟著變、化學位移就變。而 PCr 的峰位置幾乎不隨 pH 動（它的 pKa 遠離生理 pH）。所以**只要量「Pi 峰與 PCr 峰之間的間距」，就能換算出 pHi**（equation 7）。一台機器同時給你代謝物濃度**＋**細胞內酸度（[[Intracellular pH|pHi]]），這正是它在運動生理學如此好用的原因。

6. **相對濃度 vs 絕對濃度。** 頻譜直接給的是「彼此相對」的量（PCr 是 ATP 的幾倍）。要換成**絕對**值（mmol/L）得額外加一串假設：[ATP]＝8.2 mmol/L 細胞水、總肌酸＝42.5、PCr＋Pi＝42.2、這些化合物均勻分布、且運動中總肌酸不變。所以看到一篇論文給「絕對濃度」，要記得它扛著這些假設。

7. **為什麼說它是 wiki 的隱形主角。** 前面一整排概念的量測，背後幾乎都是 ³¹P-MRS：[[Phosphocreatine resynthesis|PCr 再合成]] 的 τ、[[Mitochondrial respiratory control|呼吸控制]] 的 Km／Vmax、[[Metabolic milieu at task failure|力竭時與功率無關的固定代謝終點]]、[[Critical power|CP]] 之上 PCr／Pi／pH 惡化至力竭、[[Oxidative reserve|氧化儲備]] 的 D_[PCr]——全靠它。它**非侵入**又能**連續**追蹤（相對於切片的離散快照），才撐得起這些動力學研究。認得這台機器，就認得 wiki 半壁江山的證據來源。

## 文獻怎麼說 vs 為什麼這樣說
- **主張**：³¹P-MRS 可非侵入、連續地量活肌肉的 PCr／Pi／ATP 相對濃度（在假設下亦得絕對濃度），並由 Pi–PCr 化學位移換算 pHi、由 CK 平衡反算 [ADP]。
- **背後的推理／證據**：表面線圈（surface coil）發射並接收 ³¹P 的共振訊號；峰面積∝濃度；ADP／AMP 因結合蛋白＋低於約 1 mmol/L 噪音閾而不可見；Pi 的 pKa≈pHi 使其位移隨 pH 變、PCr 的 pKa 遠離故不變→equation 7 由化學位移 σ 解出 pHi；絕對濃度需上述 5 條假設。
- **誠實的限制**：(1) 絕對濃度扛假設。(2) 劇烈運動時 Pi 峰可能「下衝（undershoot）」沉入雜訊，使 pHi 難判讀。(3) [ADP] 是推算非直讀，繼承 CK 平衡假設。(4) **時間解析度本身會左右結論**——Newcomer 用 0.5 秒解析度發現：即使取恢復前 10 秒的斜率，初始 PCr 再合成速率仍被**低估達 56%**；頭 3 秒與頭 0.5 秒的斜率就已顯著不同。所以不同研究的 τ 不完全可比，要看它的取樣解析度。

## 易誤解之處
1. **³¹P-MRS 看不到 ADP 峰——論文裡的 [ADP] 是『算』的，不是『量』的。** 它靠 [[Creatine kinase equilibrium|CK 平衡]] 反推。這也是「[ADP] 控制 vs ΔG_ATP 控制」之爭難分的一個原因：連 [ADP] 本身都是推算值（見 [[Mitochondrial respiratory control]]）。
2. **它量『相對』濃度最直接；『絕對』濃度（mmol/L）扛著一串假設。** 引用絕對數字時要意識到這層。
3. **『P』是磷，不是萬能窗口。** ³¹P-MRS 只看含磷分子（PCr／Pi／ATP）；看不到不含磷的東西（乳酸、肝醣本體要改用 ¹H／¹³C-MRS）。它是「磷代謝的窗口」，不是「肌肉代謝的全景窗」。
4. **量測解析度會改變你看到的形狀。** 時間解析度不夠，又快又陡的初始 PCr 動力學會被「抹平」而低估——這是為什麼同一現象（初始恢復速率）在不同年代、不同解析度的研究裡數字會飄。

## 用生活例子再講一次
³¹P-MRS 像給肌肉做一場「不開刀的即時體內檢查，而且只查含磷的東西」。把手臂放進磁場、用無線電「敲一下」，肌肉裡每種含磷分子會用自己特定的**音高**回響——PCr、Pi、ATP 各有各的音高（化學位移），回響的**響度**（峰面積）就是它的量。更巧的是，Pi 這個音會隨「水有多酸」而**微微走音**，所以你只要聽 Pi 和 PCr 兩個音差多遠，就能反推出細胞內的酸度。整場你不必抽一滴血、切一塊肉，還能連續錄音、即時看它怎麼變。

（這個類比在哪裡會失準：真做檢查是把樣本取出化驗；MRS 完全在體內、**不取出任何東西**，量的是「磁訊號」而非「化驗結果」，所以它扛的是物理假設（峰面積真的正比於濃度、CK 真的在平衡）而非化驗誤差。而且它有空間與時間解析度上限，太快、太小的變化會被糊掉。）

## 換句話說
換句話說，³¹P-MRS 把含磷代謝物當成「各自發出特定音高的小磁鈴」：放進磁場、用無線電脈衝一敲，PCr、Pi、ATP 各以自己的化學位移回響，峰面積給濃度，Pi 與 PCr 的位移差再換算出 [[Intracellular pH|pHi]]，而看不見的 [ADP] 靠 [[Creatine kinase equilibrium|CK 平衡]] 反算。它非侵入、可連續，所以成了 wiki 一整排肌內動力學概念（[[Phosphocreatine resynthesis]]、[[Mitochondrial respiratory control]]、[[Metabolic milieu at task failure]]、[[Oxidative reserve]]）背後共用的量測工具。

## 來源
- [[source-McMahon-2002-PCr-resynthesis]]（第 3 節：表面線圈機制；PCr／Pi／ATP（三個磷）峰、面積∝相對濃度；ADP／AMP 因結合蛋白＋低於約 1 mmol/L 噪音閾不可見、但可由 CK 平衡 equation 4 反算；Pi 的 pKa≈pHi 故化學位移隨 pH 變、PCr 不變→equation 7 由位移 σ 得 pHi；絕對濃度需 5 條假設（[ATP]＝8.2、總肌酸＝42.5、PCr＋Pi＝42.2 mmol/L 細胞水、均勻分布、運動中總肌酸不變）；第 5 節 Newcomer 以 0.5 s 時間解析度顯示初始 PCr 再合成速率被低估達 56%＝解析度限制。）
