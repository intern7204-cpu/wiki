---
type: source
tags: [exercise-physiology, critical-power, modelling, W-prime, performance, methods]
created: 2026-06-11
---

# 來源：The W′ Balance Model: Mathematical and Methodological Considerations

## 出處
- Skiba, P. F., & Clarke, D. C. (2021). *The W′ Balance Model: Mathematical and Methodological Considerations.* **International Journal of Sports Physiology and Performance**, 16(11), 1561–1572. doi:10.1123/ijspp.2021-0205
- 原始檔：`C:\原始資料\The W' Balance Model Mathematical and Methodological Considerations\`（含 Fig.1 二參數 CP 模型、Fig.2 INT vs ODE 行為、Fig.3 菁英多項選手路賽 W′bal、Fig.4 INT 玩壞的兩個極端、Fig.5 INT vs ODE/KODE、Table 1 逐秒計算範例、Table 2 ODE vs Ferguson 實測）。
- 體裁：**敘事性綜述（narrative review）**。作者 Skiba 是 [[Integral W prime balance model|W′BAL·INT]] 的提出者、Clarke 是 [[Differential W prime balance model|W′BAL·ODE]] 的提出者——兩版的原作者合寫的自我盤點。

## 核心主張
W′BAL 模型自 2012 問世後已成為理解與預測高強度間歇運動的重要工具，但成績「好壞參半」，部分肇因於其基礎與計算長期不清。本篇把**積分（INT）與微分（ODE）兩版**的理論基礎、假設、計算、長短處逐一講透：兩版的關鍵差異在於對「W′ 在間歇中如何消耗與回填」抱持**不同假設**（INT 假設消耗中仍持續背景回填；ODE 假設扣補互斥），釐清這點才能正確實作與解讀；再盤點威脅模型效度的幾個基礎問題（輸入 CP/W′ 本身不確定且會漂、與機制模型的鴻溝），並提出改良方向（多隔間、KODE、整合機制模型）。

## 本份新增／更新的概念
- [[Phenomenological vs mechanistic models]]（**新增**）：方法層概念——模型可為「描述/預測準」（現象學）或「重現因果機制」（機制）兩個會互相拉扯的目的而做；「配得準 ≠ 理解了」；引愛因斯坦語。與 [[Overfitting]]、[[Akaike information criterion]] 同層。
- [[Mechanistic power-duration models]]（**新增**）：三類機制性功率–持續時間模型（水力學水箱／生化反應動力學／運動單位），各自的典範級限制（代謝功率 ≠ 機械功率、對分子機制不可知、參數過多估不出），無單一框架適合 W′。
- [[KODE W prime balance model]]（**新增**）：W′BAL·ODE 恢復項乘常數 K 模擬「間歇中 CP 功能性升高」；K=1.28 隱含 CP 升 28%（合 Soares-Caldeira 2012）、補掉 ODE「比 INT 早 300 s 力竭」的落差；暗示 INT 持續回填假設或只是間接模擬 CP 升高。
- [[Integral W prime balance model]]（**更新**）：eq.3 因次不一致、應正寫為卷積（W′_exp 為時間函數）；INT 定義性假設＝消耗中持續背景回填（Broxterman duty cycle、Krustrup 纖維 PCr 回充為佐證）；Fig.4 兩破綻（比二參數模型還慢力竭、力竭後在 CP 騎回血）→ 僅宜用於短暫超 CP；eq.4 通用性不足（Bartram 偏快、Skiba 職業選手偏慢、Galbraith 跑步須個人擬合）。
- [[Differential W prime balance model]]（**更新**）：ODE 定義性假設＝扣補互斥、τ＝(D_CP/W′₀)⁻¹；三長處（免擬合、逐秒重算 D_CP、長段超 CP 勝 INT）、三失準（套 Ferguson 隱含 τ=112 s 為實測 336 s 的 1/3、比 INT 早約 300 s 力竭、對反覆力竭變慢不敏感）；化學動力學均勻假設與異質肌肉牴觸；延伸 KODE。
- [[W prime multicompartment model]]（**更新**）：W′BAL·MULTI 正式卷積式（eq.18 雙指數 k₁/τ₁＋k₂/τ₂）與四假設；Caen 2021 雙指數勝單指數＝需要多隔間，但切片未配對 τ 與纖維型→「隔間≈纖維型」仍未證實；快段 τ₁ 的替代解釋＝磷酸鈣沉澱快速溶解（t½≈10 s）；MULTI 未解 CP/W′ 不確定且繼承 INT 毛病。
- [[W prime balance model]]（**更新**）：INT vs ODE 根本分界（背景回填 vs 互斥）、實務應兩版都跑；輸入層不確定（W′ 誤差 7–46%、力竭非剛好 W′bal=0、CP/W′ 場內外會漂）；未來路線（雙指數→多隔間、借機制模型，但受現象學 vs 機制取捨限制，野外仍改良現象學版）。
- [[Power-duration relationship plasticity]]（**更新**）：補上「CP/W′ 不該被當場內外常數」的建模脈絡，與 KODE 處理 CP 升高方向、和 Black adjusted 處理 CP 降低方向，同屬「CP 非常數」兩端。

## 與既有知識的關係
- **一致／整合（meta-level）**：本篇是 wiki 中 INT／ODE／MULTI／三版本誤差等大量散見論述的**權威統合**，由兩版原作者親自釐清「兩版差在哪個假設」「各自何時玩壞」「該怎麼挑」。不與既有頁面矛盾，而是把它們的關係收束成一張清楚的地圖。
- **修正既有不精確處**：
  - 2012 的 eq.3 被指出**因次不一致**，本篇澄清原意一直是**卷積**（接 Sreedhara 的因次分析），並給出正確式（[[Integral W prime balance model]] 第 9 點）。
  - 把「INT 為何在某些情境意外好用」連到 KODE──INT 的持續回填或許只是**間接模擬了間歇中 CP 升高**（新洞見）。
- **推進的開放問題**：
  - 對 index.md pending ①（把反覆力竭的疲勞拖慢併入動態模型）給出**框架性方向**——多隔間 MULTI 是路徑之一，但 ODE/Morton 的多隔間版尚無人做。
  - 對「W′BAL 的 CP/W′ 輸入不確定／可變 τ／CP 衰減項」這條長期張力，提供了輸入層誤差數字（7–46%）與 KODE 這個具體（但未驗證）的 CP 升高項。
- **仍開放**：KODE 未經獨立驗證、K 為固定常數實則隨情境變；多隔間「隔間≈纖維型」未證實（Caen 切片未配對）；機制模型整合與「野外可即時運算的 CP 衰減/升高式」仍未竟。
