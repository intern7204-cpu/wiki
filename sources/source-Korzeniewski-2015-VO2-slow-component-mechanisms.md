---
type: source
tags: [exercise-physiology, metabolism, VO2-kinetics, slow-component, glycolysis, computer-model, in-silico]
created: 2026-06-12
---

# 來源：Possible mechanisms underlying slow component of V̇O₂ on-kinetics in skeletal muscle

## 出處
- Korzeniewski B, Zoladz JA. *Possible mechanisms underlying slow component of V̇O₂ on-kinetics in skeletal muscle.* **Journal of Applied Physiology** 2015; 118(10): 1240–1249. First published March 12, 2015; doi:10.1152/japplphysiol.00027.2015.
- 作者單位：B. Korzeniewski（Faculty of Biochemistry, Biophysics and Biotechnology, Jagiellonian University, Kraków, Poland）；J. A. Zoladz（Dept. of Muscle Physiology, University School of Physical Education, Kraków, Poland）。
- 原始檔：`C:\原始資料\Possible mechanisms underlying slow component of VO2 on-kinetics in skeletal muscle\`（內文＋ Fig.1–6 六張模擬／擬合圖；圖內容於正文逐一描述）。
- 體例：**理論／電腦模擬（in silico）研究**，非人體實驗。沿用與已 ingest 的 [[source-Korzeniewski-2013-VO2-PCr-off-kinetics|Korzeniewski & Zoladz 2013（off-kinetics）]] 同一個含無氧醣解的骨骼肌生物能量學動力學模型（Korzeniewski & Liguzinski 2004），對中等與重度運動的 rest-to-work（on）轉換做模擬。本份是該系列的 **on-kinetics／慢成分** 篇，與 2013 的 off-kinetics 篇互補。

## 核心主張
重度運動（>乳酸閾值）的 **VO2 慢成分** 主要由兩個機制生成：(1)**新機制**——運動中累積的 H⁺ 漸進抑制無氧醣解（伴隨肌酸激酶 CK 供能緩慢衰退），無氧 ATP 供應的缺口由氧化磷酸化（OXPHOS，受 Pi、ADP 升高驅動）接手 → VO2 在固定功率下續漲；(2) 運動中「額外 ATP 用量」漸增（疲勞致肌纖維效率下降、ATP/功率比上升），進一步放大慢成分。不排除 (3) P/O 比下降的小貢獻，但歸為待研究。關鍵推論：**慢成分大小正比於「醣解被抑制的程度」而非絕對酸度**；**乳酸是標記非肇因**；慢成分**不必靠招募 Type II 纖維**即可生成。

## 本份新增／更新的概念

**新增（3 頁，依依賴順序）**
- [[Proton inhibition of glycolysis]]（新增）——質子對醣解的抑制：H⁺ 在 glycogen phosphorylase 與 PFK 兩個限速步驟抑制醣解，是會自我設限的剎車；完整人體證據＝NH₄Cl 致酸↓乳酸、NaHCO₃ 致鹼↑乳酸（Sutton 1981）。慢成分機制一的核心地基。
- [[P over O ratio|P/O ratio]]（新增）——P/O 比：每消耗一份氧產出幾個 ATP＝有氧產能的偶聯效率；質子漏拉低它；運動時質子漏佔 VO2 僅 ~1.2%，故 P/O 下降對慢成分貢獻有限。
- [[Bioenergetic mechanism of the VO2 slow component]]（新增）——本份 headline：以「ATP 產生＝ATP 消耗」鐵律，把醣解抑制＋CK 緩降＋額外 ATP 用量（±P/O 下降）串成「缺口轉嫁給有氧→VO2 漲」的統一機制；含「慢成分 ∝ 醣解抑制程度而非酸度」「乳酸標記非肇因」「不必招募新纖維」三個關鍵推論。

**更新（5 頁）**
- [[VO2 slow component]]（更新）——把成因從「以 Type II 招募為主（Gaesser 1996）」補上機制版的對立／互補觀點：in silico 顯示醣解被酸抑制＋纖維內效率下降即足，招募非必要；連到新機制頁。
- [[Exercise efficiency]]（更新）——補上「用量端」效率損失：運動中 ATP/功率比漸增（疲勞與低效率為一體兩面，Grassi），與「產能端」P/O 下降區分。
- [[Parallel activation of oxidative phosphorylation]]（更新）——補 on-transition 用法：本模型用 τ(ON)=3 s、p=0.5 的 ESA 驅動 on 轉換；ESA 強度（p）改變會調節慢成分與 τVO2（訓練升 ESA→加快動力學、縮慢成分）。
- [[Metabolic stability]]（更新）——補上「額外 ATP 用量降低代謝物（ADP/PCr/Pi）穩定性、對 pH 影響小」；「強化無氧醣解→PCr/Pi 穩定性↓（CK 平衡位移）、ADP 穩定性略↑」。
- [[Lactate]]（更新）——補上「H⁺ 回頭抑制醣解（保護性負回饋）」這層，連到 [[Proton inhibition of glycolysis]]；強化「乳酸為標記非肇因」。

## 與既有知識的關係
**一致／補充／深化，與既有頁面無直接矛盾，但與 Gaesser 1996 對「慢成分成因」的側重不同（互補而非牴觸）。**
- 與 [[source-Korzeniewski-2013-VO2-PCr-off-kinetics|2013 off-kinetics 篇]] 同模型、互補：2013 講「運動結束後」VO2 與 PCr 的反向關係（由 τ(OFF)），本份講「運動進行中」VO2 為何漂升（由醣解抑制＋ATP 用量）。兩篇共用 [[Parallel activation of oxidative phosphorylation]]。
- 與 [[VO2 slow component]] 既有結論（乳酸相關非肇因、不必額外招募纖維、效率下降）**高度一致**，本份補上「為什麼」的肌內生物能量學機制。
- 與 [[Critical Pi threshold and positive feedback model]] 呼應：兩者都把「Pi/ADP 升高→驅動 VO2／疲勞」放在核心；本份把上游再往前推到「無氧供應下滑造成缺口」。

**須標注的張力／誠實面**：
1. **in silico、半定量**：作者明言旨在「展示一般效應」而非精確定量；質子抑制醣解的精確分子動力學（Eq.2）只是半定量近似。
2. **新機制（質子抑制醣解→慢成分）為模型預測**，雖有 Sutton 1981（致酸↓乳酸）與 Zoladz 1998（NH₄Cl 致酸↑慢成分）等人體間接支持，但「醣解抑制直接造成慢成分」未被直接量測證實。
3. **P/O 下降**證據兩面：質子漏佔比小＋肺 VO2-PCr 緊密反向 → 不支持；但 Cannon「VO2 與總 ATP 合成不相關」→ 暗示有些影響。歸為待研究。
4. **與 Gaesser 1996 的側重差異**：傳統綜述把慢成分主因放在「Type II 纖維漸進招募」；本份證明招募非必要條件（離體全招募狗肌仍有慢成分樣反應）。兩說並存：招募可貢獻、非必要。
5. **模型局限**（作者自列）：無法區分「已working纖維疲勞」與「招募低效纖維」；NADH 供應當黑箱；未含 Pi trapping（故無法解釋某些研究中 Pi 恆定）；假設醣解自運動起始即活化（部分研究指有延遲）。

## 與 wiki pending 的關係
- 收束既有 pending：[[VO2 slow component]] 的「成因機制」先前主要靠 Gaesser 1996 的現象學歸納；本份補上肌內生物能量學的機制層，並把它接到 [[Parallel activation of oxidative phosphorylation]]、[[Creatine kinase equilibrium]]、[[Mitochondrial respiratory control]] 這條已建好的 bioenergetics 主幹。
- 新留白（見 index.md pending）：①「質子抑制醣解直接造成慢成分」的**人體直接驗證**（同步量肌內醣解流量＋muscle VO2）仍缺；②**P/O 比運動中是否真下降**未定論，需 ingest 線粒體偶聯／質子漏專論深化 [[P over O ratio|P/O ratio]]；③「ATP 用量增加（用量端效率損失）」的分子機制（哪些疲勞代謝物、如何抬高 ATP/力比）仍粗略，可接肌肉疲勞／收縮效率專論；④`Bioenergetic Mechanisms Linking VO2 Kinetics and Exercise Tolerance`（原始資料尚存）可把本份的慢成分機制接到運動耐受／CP。
