---
type: source
tags: [exercise-physiology, metabolism, VO2-kinetics, recovery, computer-model, in-silico]
created: 2026-06-12
---

# 來源：Slow V̇O₂ off-kinetics in skeletal muscle is associated with fast PCr off-kinetics—and inversely

## 出處
- Korzeniewski B, Zoladz JA. *Slow V̇O₂ off-kinetics in skeletal muscle is associated with fast PCr off-kinetics—and inversely.* **Journal of Applied Physiology** 2013; 115(5): 605–612. First published June 20, 2013; doi:10.1152/japplphysiol.00469.2013.
- 作者單位：B. Korzeniewski（Faculty of Biochemistry, Biophysics and Biotechnology, Jagiellonian University, Kraków, Poland）；J. A. Zoladz（Dept. of Muscle Physiology, University School of Physical Education, Kraków, Poland）。
- 原始檔：`C:\原始資料\Slow VO2 off-kinetics in skeletal muscle is associated with fast PCr off-kinetics—and inversely\`（內文＋ APPENDIX 完整動力學模型，附 Fig.1、Fig.2 兩張模擬圖，已單獨檢視）。
- 體例：**理論／電腦模擬（in silico）研究**，非人體實驗。使用 Korzeniewski & Liguzinski（2004）含無氧醣解的骨骼肌生物能量學動力學模型（含氧化磷酸化、醣解、肌酸激酶、ATP 利用、NADH 供應、質子外流），對中等與重度運動的 on/off 轉換做模擬。

## 核心主張
運動後骨骼肌的 **VO2 離線動力學（off-kinetics）初段** 與 **PCr 離線動力學** 呈**反向**：VO2 初段降得愈快、PCr 補得愈慢，反之亦然。兩者由同一個上游參數——**氧化磷酸化平行活化在恢復期的衰減時間 τ(OFF)**——共同決定。此外，恢復期 VO2 高於基線的積分（＝**氧債**）對給定的 PCr 消耗**守恆**，與 τ(OFF) 無關（同樣的 PCr 要還同樣多的氧）；τ(OFF) 夠大時出現 **PCr 恢復過衝**；運動「開始（on）」時 VO2 與 PCr 近鏡像對稱，「結束（off）」時則為上述反向關係（on/off 不對稱）。

## 本份新增／更新的概念

**新增（3 頁，依依賴順序）**
- [[Parallel activation of oxidative phosphorylation]]（新增）——氧化磷酸化的平行活化／每步活化：Ca²⁺ 驅動的**前饋**機制，直接把 OXPHOS 每一步同時調快，補足純 ADP 回饋（解釋「VO2 升 13–32× 而 ADP 僅升 3–4.3×」的代謝穩定）；以 τ(ON)、τ(OFF) 刻畫開與關。**這是 [[VO2 kinetics]] 先前以 gloss 帶過、無專頁的「each-step activation」之完整頁。**
- [[Inverse VO2-PCr off-kinetics relationship]]（新增）——VO2 與 PCr 離線動力學的反向關係：本份 headline；τ(OFF)↑→VO2 off 初段變慢、PCr off 變快；氧債守恆；on 對稱 vs off 反向；肌肉 vs 肺 VO2 脫鉤。
- [[Phosphocreatine recovery overshoot]]（新增）——磷酸肌酸恢復過衝：τ(OFF) 夠大時 PCr 暫時超過靜息值，伴隨肌肉酸化（Zoladz 2010）；τ(OFF) 偏大的招牌。

**更新（4 頁）**
- [[Mitochondrial respiratory control]]（更新）——補上「ADP 回饋非全部、須加 Ca²⁺ 前饋平行活化」一層；回饋＋前饋並存，[ADP] 控制仍在但不必被堆高（推導新增第 8 點）。回應 wiki pending ①「呼吸控制機制」。
- [[Oxygen debt]]（更新）——補上氧債對給定 PCr 消耗守恆（與 τ(OFF) 無關、形狀變面積不變）、訓練者氧債小是因 PCr 掉得少；新增易誤解「VO2 降得慢≠氧債大」。
- [[VO2 kinetics]]（更新）——把「each-step activation／平行活化」gloss 連到新頁；補 on/off 不對稱（on 較快）、肌肉 vs 肺 VO2 重度運動脫鉤、off 與 PCr 反向耦合。
- [[Phosphocreatine resynthesis]]（更新）——補上 τ(OFF) 為 PCr off 速率的上游決定因子（τ(OFF)↑→補更快）、與 VO2 反向耦合、過衝（推導新增第 10 點）。

## 與既有知識的關係
**一致／補充／深化，無直接矛盾，但補上一個關鍵的機制層。** 本 wiki 先前的 OXPHOS 控制主要建立在 Kemp 1993／McMahon 2002 的**回饋（ADP/Pi）**觀點上；本份補上**前饋（平行活化）**這一層，兩者並存（非推翻）。與 [[Phosphocreatine resynthesis]] 的「補 PCr 純有氧」一致，並把它接到「恢復期 VO2 殘餘高度」上。與 [[Oxygen debt]] 的「δVO2×τ(off)」一致，並加上「總量由 PCr 消耗鎖死」的守恆。

**須標注的張力／誠實面**：
1. **這是電腦模型（in silico）、半定量**：作者明言旨在「廣泛半定量重現多種肌肉/物種/條件」，非精確擬合單一實驗。核心反向關係「**VO2 off 愈快 PCr off 愈慢**」作者自陳**文獻未曾提出或實驗證實**，屬有力但待驗的機制預測。
2. **依賴平行活化假設**：反向關係需要「平行活化＋非瞬間的 τ(OFF)」；純回饋模型（Meyer、Kushmerick、Wu）產生不出。平行活化的分子身分仍未完全釘死。
3. **肌肉 vs 肺 VO2**：反向關係在**肌肉**層級；實測常見的**肺** VO2 off 受循環干擾，Rossiter 2002 量到「肺 VO2 off τ 與 PCr off τ 接近」看似相左，實為被糊掉的肺 VO2，不直接反駁肌肉層級預測。

## 與 wiki pending 的關係
- 推進 pending ①（[[Mitochondrial respiratory control]] 的呼吸控制機制）：在「[ADP] vs ΔG_ATP」之外，補上「回饋 vs 前饋」這條更上層的機制軸。
- 收掉一個長期 gloss 缺口：[[VO2 kinetics]] 的「each-step activation／平行活化」終於有專頁。
- 新留白（見 index.md pending）：①平行活化的分子身分／Ca²⁺ 如何活化每一步，需 ingest 粒線體呼吸控制專論；②反向關係的**人體實驗驗證**仍缺；③原始資料尚有 `Bioenergetic Mechanisms Linking VO2 Kinetics and Exercise Tolerance`、`Muscle metabolic responses during high-intensity intermittent exercise measured by ³¹P-MRS` 可把本份的 off-kinetics 接到間歇 W′／運動耐受。
