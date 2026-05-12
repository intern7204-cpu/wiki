# Wiki Log

> 時序紀錄，append-only。
> 格式：`## [YYYY-MM-DD] <action> | <subject>`
> Actions: ingest | synthesis | query | lint | create | update | correction | archive | delete
> log.md 超過 500 條時 rotate 成 `log-YYYY.md`。

## [2026-04-22] create | 知識百科初始化
- 建立 SCHEMA.md、index.md、log.md
- 建立資料夾：00_總覽、01_核心概念、02_方法學、03_疾病與臨床主題、04_CPET、05_Exercise_Physiology、06_Gait_Biomechanics、07_Pediatric_Development、08_工具與Workflow、09_來源摘要
- 原始資料盤點：
  - 根目錄：Poole 2020 anaerobic threshold review（1）
  - 執行功能/：4 份（Harvard working papers × 2、Smart but Scattered 科普書、What is EF 網頁）
  - 聯合評估與教養/：32 份（UpToDate × 22+1、台灣聯評手冊、CDC milestone、Hanen/Plan B 教養手冊、cognitive control.pdf、E001016.pdf 待判類）
- 尚未 ingest 任何內容

## [2026-04-22] ingest | Poole et al. 2020 — The anaerobic threshold: 50+ years of controversy (J Physiol)
- 類型：review article（Tier 1）
- 來源頁建立：09_來源摘要/Poole_2020_anaerobic_threshold.md
- 新建主幹頁 6：
  - 04_CPET/Anaerobic_Threshold_概念史.md
  - 04_CPET/Lactate_Threshold.md
  - 04_CPET/Gas_Exchange_Threshold.md
  - 04_CPET/Critical_Power.md
  - 04_CPET/Exercise_Intensity_Domains.md
  - 05_Exercise_Physiology/Lactate_Shuttle.md
- index.md 更新（Total pages: 0 → 7）
- 交叉連結完成（每頁至少 4 個 wikilinks）
- 無與既有內容衝突（先建骨架）
- 核心立場：
  1. 「anaerobic threshold」作為機制描述應淘汰；lactate shuttle 為新典範
  2. LT / GET 仍是 moderate→heavy 邊界，臨床價值高（術前風險、HF 預後）
  3. Heavy→severe 真正邊界為 critical power (CP/CS)，非 AT/GET

## [2026-04-22] ingest | 5 篇 CPET / exercise physiology reviews
來源檔（皆 Tier 1 review，原始資料層已有 .md 格式）：
1. Goulding, Rossiter, Marwood, Ferguson 2021. ESSR. "Bioenergetic Mechanisms Linking V̇O2 Kinetics and Exercise Tolerance"
2. Jones & Vanhatalo 2017. Sports Med. "The 'Critical Power' Concept: Applications to Sports Performance with a Focus on Intermittent High-Intensity Exercise"
3. Gaesser & Poole 1996. ESSR. "The Slow Component of Oxygen Uptake Kinetics in Humans"
4. Beltz et al. 2016. J Sports Med. "Graded Exercise Testing Protocols for the Determination of VO2max: Historical Perspectives, Progress, and Future Considerations"
5. Hargreaves & Spriet 2020. Nature Metabolism. "Skeletal muscle energy metabolism during exercise"

新建 5 篇來源摘要頁：
- 09_來源摘要/Goulding_2021_VO2_kinetics_exercise_tolerance.md
- 09_來源摘要/Jones_Vanhatalo_2017_critical_power_concept.md
- 09_來源摘要/Gaesser_Poole_1996_VO2_slow_component.md
- 09_來源摘要/Beltz_2016_GXT_protocols.md
- 09_來源摘要/Hargreaves_Spriet_2020_muscle_energy_metabolism.md

新建 5 篇主題頁：
- 04_CPET/VO2_Kinetics.md（三相結構、τV̇O₂、O₂ deficit、與 CP 關聯）
- 04_CPET/VO2_Slow_Component.md（heavy/severe 特徵、多因子機制、與 W' 關聯）
- 04_CPET/CPET_Protocol_Design.md（modality、ramp、verification、self-paced、族群考量）
- 04_CPET/VO2max_Measurement.md（V̇O₂max vs V̇O₂peak、plateau、verification flow、誤差來源）
- 05_Exercise_Physiology/Skeletal_Muscle_Energy_Metabolism.md（三路徑、雙階段調控、Lactate、訓練適應、ergogenic）

強化既有頁：
- 04_CPET/Critical_Power.md：新增 τV̇O₂–CP 機制連結段、W'BAL 模型、intermittent exercise 區段、W' 非獨立 anaerobic capacity 的釐清
- 04_CPET/Lactate_Threshold.md、Gas_Exchange_Threshold.md、Exercise_Intensity_Domains.md、Anaerobic_Threshold_概念史.md：補反向連結

index.md 更新：Total pages 7 → 16。

關鍵整合觀點（跨 5 篇 + Poole 2020）：
- V̇O₂ kinetics 不是次要指標；τV̇O₂ 透過 critical [Pi] 決定 CP（Goulding-Rossiter 假說）
- CP 是 emergent system property，非固定生理常數
- W' 非「anaerobic capacity」，反映 critical→peak [Pi] 的積分容量
- GET/LT 為 moderate→heavy 邊界；CP 為 heavy→severe 邊界
- V̇O₂max 判定應以 verification protocol 搭配次級標準，而非單靠 plateau 或 RER
- Lactate 已確立為代謝中樞與信號分子，Hargreaves-Spriet 與 Brooks shuttle theory 一致

## [2026-04-23] ingest | 5 篇 CPET / exercise physiology Tier 1 來源（Batch 3）
- Batch: 3
- Selected files:
  1. Blemker et al. — Fiber-type traps: revisiting common misconceptions about skeletal muscle fiber types
  2. Chorley & Lamb 2020 — The Application of Critical Power, the Work Capacity above Critical Power (W'), and Its Reconstitution
  3. Kemp, Taylor, Radda 1993 — Control of Phosphocreatine Resynthesis during Recovery from Exercise
  4. Midgley et al. 2008 — Does an Incremental Exercise Test for Valid VO2max Determination Really Need to Last Between 8 and 12 Minutes?
  5. Oliveira, Boppre, Fonseca 2024 — Polarized Versus Other Training Intensity Distribution Regimens and Endurance Performance
- 類型與層級：
  - Blemker：perspective / synthesis review，Tier 1
  - Chorley & Lamb：narrative review，Tier 1
  - Kemp：research review with integrated data analysis，Tier 1
  - Midgley：narrative review，Tier 1
  - Oliveira：systematic review + meta-analysis，Tier 1
- 說明：前一輪已存在 5 篇來源摘要頁，但尚未完成主題頁、index 與 log 接軌；本批已回頭核對原始 Markdown 並正式完成整合。
- 新建主題頁 4：
  - 04_CPET/Training_Prescription_by_CP.md
  - 05_Exercise_Physiology/Muscle_Fiber_Types.md
  - 05_Exercise_Physiology/PCr_Resynthesis.md
  - 05_Exercise_Physiology/Training_Intensity_Distribution.md
- 既有頁更新：
  - 04_CPET/Critical_Power.md
  - 04_CPET/CPET_Protocol_Design.md
  - 04_CPET/VO2max_Measurement.md
  - 04_CPET/Exercise_Intensity_Domains.md
  - 04_CPET/VO2_Kinetics.md
  - 04_CPET/VO2_Slow_Component.md
  - 05_Exercise_Physiology/Skeletal_Muscle_Energy_Metabolism.md
- 明確修正 / 衝突標示：
  1. 「8–12 min」從 obligatory validity rule 下修為 practical default；Midgley 2008 支持更寬的 valid duration range。
  2. 「type 2 recruitment = 低 oxidative capacity」標示為過度簡化；MHC 與 oxidative capacity 不可互推。
  3. 「W' = anaerobic capacity」標示為不精確；改為有限 work capacity above CP / metabolite tolerance 的 operational construct。
  4. Polarized training 的優勢限於 V̇O₂peak、短期介入與高度訓練族群；非全面 superiority。
- index.md 更新：Total pages 16 -> 26
- Pending files（next-batch candidates；本回合未讀）：
  - Exercise Test Design and Analysis
  - CRITICAL POWER AND EXERCISE TOLERANCE
  - Exercise and sports cardiology
  - Reliability of critical power testing
  - beaver-et-al-1986-a-new-method-for-detecting-anaerobic-threshold-by-gas-exchange

## [2026-04-23] create | 08_工具與Workflow/知識百科_健康檢查流程
- 新建 workflow page：08_工具與Workflow/知識百科_健康檢查流程.md
- 定義 lint / health check 分三階段：wiki 結構掃描、知識健康度掃描、raw verification queue
- 新增明確限制：每次 health check 若需回查原始文件，單一回合最多只讀 5 個 raw files
- index.md 更新：Total pages 34 -> 35

## [2026-04-23] ingest | CPET protocol / CP methodology / sports cardiology（Batch 4）
- Batch: 4
- Selected files:
  1. Exercise Test Design and Analysis
  2. CRITICAL POWER AND EXERCISE TOLERANCE
  3. Exercise and sports cardiology
  4. Reliability of critical power testing
  5. beaver-et-al-1986-a-new-method-for-detecting-anaerobic-threshold-by-gas-exchange
- 類型與層級：
  - Bentley/Newell/Bishop：review article，Tier 1
  - Jones/Vanhatalo/Burnley/Morton/Poole：review article，Tier 1
  - Thompson/Baggish：textbook chapter，Tier 1
  - Triska et al.：original article，Tier 3
  - Beaver/Wasserman/Whipp：original article，Tier 3（historical methodological foundation）
- 新建來源摘要頁 5：
  - 09_來源摘要/Bentley_Newell_Bishop_2007_incremental_exercise_test_design.md
  - 09_來源摘要/Jones_Vanhatalo_Burnley_Morton_Poole_2010_CP_exercise_tolerance.md
  - 09_來源摘要/Thompson_Baggish_exercise_sports_cardiology.md
  - 09_來源摘要/Triska_2017_CP_reliability.md
  - 09_來源摘要/Beaver_Wasserman_Whipp_1986_V_slope_method.md
- 新建主題頁 3：
  - 04_CPET/V_Slope_Method.md
  - 04_CPET/CP_Test_Reliability.md
  - 03_疾病與臨床主題/Sports_Cardiology_概論.md
- 既有頁更新：
  - 04_CPET/Critical_Power.md
  - 04_CPET/CPET_Protocol_Design.md
  - 04_CPET/Gas_Exchange_Threshold.md
  - 04_CPET/Anaerobic_Threshold_概念史.md
  - 04_CPET/VO2max_Measurement.md
  - 04_CPET/Training_Prescription_by_CP.md
  - 04_CPET/Exercise_Intensity_Domains.md
- 明確整合 / 衝突標示：
  1. CP 再次明確界定為 heavy-severe boundary；LT/GET 與 V̇O2max 不可替代 CP。
  2. V-slope method 作為 GET 的歷史性方法學奠基被補入，但其原始「anaerobic」命名不等於當代仍接受舊機制。
  3. TT-derived CP/W' reliability 僅作方法學補充；以 familiarization 與 protocol control 為前提，不可外推成普遍金標。
  4. Incremental stage duration 會系統性改變 PPO 與 threshold work rate；protocol choice 必須回到主 endpoint。
- index.md 更新：Total pages 26 -> 34
- housekeeping：
  - 移除非知識頁 scaffold：`知識百科/歡迎.md`
  - 移除空白頁：`知識百科/未命名.md`
- Pending files：
  - 本回合未再擴大候選盤點，以遵守單回合最多 5 份原始文件限制。
  - 下一批需重新依來源優先級、主題缺口與更新性排序選定候選。

## [2026-04-23] create | 08_工具與Workflow/wiki_health_check.py
- 新建可執行 lint / health-check 腳本：08_工具與Workflow/wiki_health_check.py
- 新建測試：08_工具與Workflow/tests/test_wiki_health_check.py
- 產出最新報告：08_工具與Workflow/health_check_report_latest.md
- 腳本目前可檢查：orphan pages、weak links、broken links、index completeness、frontmatter、oversized pages、contradiction candidates、raw backlog、5-file raw verification queue
- 驗證：`python3 08_工具與Workflow/tests/test_wiki_health_check.py` 通過

## [2026-04-23] update | frontmatter normalization（contradictions）
- 批次補齊 34 個頁面的 frontmatter 欄位：`contradictions: []`
- 範圍：03_疾病與臨床主題、04_CPET、05_Exercise_Physiology、09_來源摘要
- 重新執行 health check 後，`frontmatter_issues` 已由 34 降為 0
- 最新報告已重寫：08_工具與Workflow/health_check_report_latest.md

## [2026-04-23] create | 08_工具與Workflow/Wiki_Health_Check_腳本
- 新建腳本說明頁：08_工具與Workflow/Wiki_Health_Check_腳本.md
- 與 08_工具與Workflow/知識百科_健康檢查流程.md 建立雙向 wikilink，修正 orphan page
- index.md 更新：Total pages 35 -> 36
- 重新執行 health check 後，`orphans` 已由 1 降為 0；`broken_links` 維持 0

## [2026-04-23] create | 08_工具與Workflow/知識百科_健康檢查_分級與輸出
- 新建分頁：08_工具與Workflow/知識百科_健康檢查_分級與輸出.md
- 將 health check 主工作流的 Phase 3 細節、issue 分級、標準輸出格式與執行節奏拆出，降低主頁長度
- index.md 更新：Total pages 36 -> 37
- 重新執行 health check 後，`oversized_pages` 已由 1 降為 0

## [2026-04-23] update | contradiction candidate cleanup
- 調整 wiki_health_check.py 的 contradiction 掃描規則：
  - `type: workflow` 不再列入 contradiction candidate
  - generic method caveats / section labels（如 `限制 / 爭議`、`invalid test`、`true boundary`）不再視為未標示衝突
  - 改以較窄的 unresolved-conflict patterns（如 `conflicting findings`、`results are mixed`、`仍有爭議`、`存在爭議`）判定
- 新增測試覆蓋 workflow false positive 與 generic limitation heading false positive
- 重新執行 health check 後，`contradiction_candidates` 已由 11 降為 0
- 最新報告已重寫：08_工具與Workflow/health_check_report_latest.md

## [2026-04-23] ingest | PM&R foundational assessment / electrodiagnosis / spasticity / sensory rehabilitation（Batch 5）
- Batch: 5
- Candidate ranking（依近期新增 + 同主題相關性 + 來源優先級排序）：
  1. The physiatric history and physical examination
  2. Examination of the pediatric patient
  3. Electrodiagnostic medicine
  4. Spasticity
  5. Auditory, vestibular, and visual impairments
- Selected files（本回合實際讀取 5/5）：
  1. The physiatric history and physical examination
  2. Examination of the pediatric patient
  3. Electrodiagnostic medicine
  4. Spasticity
  5. Auditory, vestibular, and visual impairments
- 類型與層級：
  - Barker/Cui/Kasitinon：textbook chapter，Tier 1，可信度 high
  - Miller/Talley/Miller：textbook chapter，Tier 1，可信度 high
  - Seidel/Andary/Dillingham：textbook chapter，Tier 1，可信度 high
  - Francisco/Li：textbook chapter，Tier 1，可信度 high
  - Lew/Hall/Gustafson：textbook chapter，Tier 1，可信度 high
- 新建來源摘要頁 5：
  - 09_來源摘要/The_physiatric_history_and_physical_examination.md
  - 09_來源摘要/Examination_of_the_pediatric_patient.md
  - 09_來源摘要/Electrodiagnostic_medicine.md
  - 09_來源摘要/Spasticity.md
  - 09_來源摘要/Auditory_vestibular_and_visual_impairments.md
- 新建主題頁 7：
  - 01_核心概念/ICF_功能框架.md
  - 02_方法學/電生理診斷醫學.md
  - 03_疾病與臨床主題/PMR_評估總論.md
  - 03_疾病與臨床主題/Spasticity_概論.md
  - 03_疾病與臨床主題/感覺障礙復健總論.md
  - 06_Gait_Biomechanics/步態評估總論.md
  - 07_Pediatric_Development/小兒復健評估.md
- 明確標示的 field-level conflict / caveat：
  1. Spasticity 不等於所有 muscle tightness；需區分 reflex hyperexcitability、weakness、co-contraction、contracture 與 peripheral stiffness。
  2. Lance definition 保留歷史地位，但現代 framing 已擴展到 muscle length dependence、abnormal synergies 與 peripheral muscle change。
  3. Vestibular rehabilitation 對 peripheral vestibular disorder 證據強；對 central vestibular disorder 證據較弱，不能混為一談。
  4. EDX normal study 應表述為「no electrodiagnostic evidence of」，不代表完全排除臨床診斷。
- index.md 更新：Total pages 37 -> 49
- Pending files（下一批待處理）：
  - The Physiatric History and Physical Examination handbook
  - Traumatic brain injury
  - Stroke rehabilitation
  - Spinal cord injury
  - Lower limb amputation and gait

## [2026-04-23] ingest | neurorehabilitation disease frameworks / amputation rehabilitation（Batch 6）
- Batch: 6
- Candidate ranking（承接上一批 pending list，依近期新增 + 同主題相關性 + 來源優先級排序）：
  1. The Physiatric History and Physical Examination handbook
  2. Traumatic brain injury
  3. Stroke rehabilitation
  4. Spinal cord injury
  5. Lower limb amputation and gait
- Selected files（本回合實際讀取 5/5）：
  1. The Physiatric History and Physical Examination handbook
  2. Traumatic brain injury
  3. Stroke rehabilitation
  4. Spinal cord injury
  5. Lower limb amputation and gait
- 類型與層級：
  - Shyu/Liang：textbook chapter，Tier 1，可信度 high
  - Wagner/Franzese/Weppner：textbook chapter，Tier 1，可信度 high
  - Yochelson/Dennison/Kolarova：textbook chapter，Tier 1，可信度 high
  - Escalon/Marzloff/Bryce：textbook chapter，Tier 1，可信度 high
  - Lovegreen/Murphy/Stevens：textbook chapter，Tier 1，可信度 high
- 新建來源摘要頁 5：
  - 09_來源摘要/The_Physiatric_History_and_Physical_Examination_handbook.md
  - 09_來源摘要/Traumatic_brain_injury.md
  - 09_來源摘要/Stroke_rehabilitation.md
  - 09_來源摘要/Spinal_cord_injury.md
  - 09_來源摘要/Lower_limb_amputation_and_gait.md
- 新建主題頁 4：
  - 03_疾病與臨床主題/創傷性腦損傷復健總論.md
  - 03_疾病與臨床主題/中風復健總論.md
  - 03_疾病與臨床主題/脊髓損傷復健總論.md
  - 03_疾病與臨床主題/下肢截肢復健總論.md
- 既有頁更新：
  - 03_疾病與臨床主題/PMR_評估總論.md
  - 06_Gait_Biomechanics/步態評估總論.md
- 明確標示的 field-level conflict / caveat：
  1. TBI 的 GCS mild / moderate / severe 分級仍有用，但不足以代表 injury heterogeneity 與長期功能預後。
  2. Stroke rehabilitation 中「越早 mobilization 越好」不是普遍真理；ICH 在 first 24 hours 的 very early mobilization 可能有害。
  3. SCI 的 complete injury 定義以 S4-S5 sacral sparing 為準，不等於「病灶以下完全沒有任何功能」的直覺說法。
  4. 下肢截肢不是保留愈遠端愈好；partial foot / distal preservation 在某些情況下長期功能反而不如較近端但力學較佳的 level。
- index.md 更新：Total pages 49 -> 58
- Pending files（下一批待處理）：
  - Rehabilitation of swallowing disorders.pdf 的副本
  - Neurogenic bowel Dysfunction and rehabilitation
  - Neurogenic lower urinary tract dysfunction.pdf 的副本
  - Psychological assessment and intervention in rehabilitation
  - Quality and outcome measures for medical rehabilitation

## [2026-04-23] ingest | dysphagia / bowel-bladder management / rehab psychology / quality metrics（Batch 7）
- Batch: 7
- Candidate ranking（承接上一批 pending list，依近期新增 + 同主題相關性 + 來源優先級排序）：
  1. Rehabilitation of swallowing disorders.pdf 的副本
  2. Neurogenic bowel Dysfunction and rehabilitation
  3. Neurogenic lower urinary tract dysfunction.pdf 的副本
  4. Psychological assessment and intervention in rehabilitation
  5. Quality and outcome measures for medical rehabilitation
- Selected files（本回合實際讀取 5/5）：
  1. Rehabilitation of swallowing disorders.pdf 的副本
  2. Neurogenic bowel Dysfunction and rehabilitation
  3. Neurogenic lower urinary tract dysfunction.pdf 的副本
  4. Psychological assessment and intervention in rehabilitation
  5. Quality and outcome measures for medical rehabilitation
- 類型與層級：
  - Singer/Aihara/Gonzalez-Fernandez：textbook chapter，Tier 1，可信度 high
  - Rodriguez/Goetz/Stiens：textbook chapter，Tier 1，可信度 high
  - Goetz/Klausner：textbook chapter，Tier 1，可信度 high
  - Carter/Lewis：textbook chapter，Tier 1，可信度 high
  - Yang/Grover/Raval：textbook chapter，Tier 1，可信度 high
- 新建來源摘要頁 5：
  - 09_來源摘要/Rehabilitation_of_swallowing_disorders.md
  - 09_來源摘要/Neurogenic_bowel_dysfunction_and_rehabilitation.md
  - 09_來源摘要/Neurogenic_lower_urinary_tract_dysfunction.md
  - 09_來源摘要/Psychological_assessment_and_intervention_in_rehabilitation.md
  - 09_來源摘要/Quality_and_outcome_measures_for_medical_rehabilitation.md
- 新建主題頁 5：
  - 03_疾病與臨床主題/吞嚥障礙復健總論.md
  - 03_疾病與臨床主題/神經性腸道功能障礙復健.md
  - 03_疾病與臨床主題/神經性下泌尿道功能障礙.md
  - 02_方法學/復健心理社會評估與介入.md
  - 02_方法學/復健品質與結局指標.md
- 既有頁更新：
  - 03_疾病與臨床主題/PMR_評估總論.md
  - 03_疾病與臨床主題/中風復健總論.md
  - 03_疾病與臨床主題/創傷性腦損傷復健總論.md
  - 03_疾病與臨床主題/脊髓損傷復健總論.md
  - 03_疾病與臨床主題/下肢截肢復健總論.md
- 明確標示的 field-level conflict / caveat：
  1. 吞嚥 bedside screening 不能排除 silent aspiration；absence of gag reflex 也不是可靠 predictor。
  2. NBD 的臨床目標常是 social continence，不是恢復完全「正常」排便；supraconal 與 infraconal 也不能共用同一 bowel care recipe。
  3. NLUTD 不能只看 symptom 或 PVR；OAB 與 detrusor overactivity 不是同一件事，urologic safety 需靠 urodynamics 與 upper tract surveillance 判讀。
  4. psychological adjustment 不是線性 grief stage 模型；routine suicide risk 與 family burden assessment 不能省略。
  5. outcome、process、performance measure 不可混用；value 也不等於只壓低單一服務成本。
- index.md 更新：Total pages 58 -> 68
- Pending files（下一批待處理）：
  - Rehabilitation and prosthetic restoration in upper limb amputation
  - Practical aspects of impairment rating and disability determination
  - Occupational medicine and vocational rehabilitation
  - Interprofessional Team-Based Care
  - Celebrating Sociocultural Diversity in the Exam Room and Addressing Racism and Bias

## [2026-04-23] update | lint / health check 工作流
- 更新頁面：08_工具與Workflow/知識百科_健康檢查流程.md
- 更新頁面：08_工具與Workflow/Wiki_Health_Check_腳本.md
- 新建頁面：08_工具與Workflow/知識百科_衝突處理規則.md
- index.md 更新：Total pages 68 -> 69
- 補強內容：明確列出 6 類固定 health check 目標（孤立頁、缺交叉連結、stale、未標示矛盾、missing core topics、raw backlog）
- 將衝突處理規則獨立成 companion workflow page，避免主工作流頁超過 200 行
- 腳本說明頁同步對齊目前已實作的檢查項目名稱

## [2026-04-24] lint | 全知識百科 health check
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- pages_scanned: 69
- 結果摘要：orphan 0、weak links 0、broken links 0、index missing 0、frontmatter issues 0、oversized pages 0、stale candidates 0、contradiction candidates 0、missing core topics 0
- raw backlog: 177
- raw verification queue（5-file cap）:
  1. Achilles tendinopathy - UpToDate.md
  2. Ankle sprain in adults_ Evaluation and diagnosis - UpToDate.md
  3. Ankle sprain in adults_ Management - UpToDate.md
  4. Clinical assessment of walking and running gait - UpToDate.md
  5. 精選鞋子/Cut in half_ ASICS GT 1000 12 Review.md
- 本回合未回讀 raw 內容；僅完成 wiki-level lint 與 verification queue 排序

## [2026-04-24] lint | raw verification queue 深度回查（5 files）
- 實際回讀 raw files 5/5：
  1. Achilles tendinopathy - UpToDate.md
  2. Ankle sprain in adults_ Evaluation and diagnosis - UpToDate.md
  3. Ankle sprain in adults_ Management - UpToDate.md
  4. Clinical assessment of walking and running gait - UpToDate.md
  5. 精選鞋子/Cut in half_ ASICS GT 1000 12 Review.md
- 驗證結果：
  - 前 4 件為真 Tier 1 backlog（UpToDate / 2025–2026 更新），值得優先 ingest。
  - 其中 Achilles tendinopathy 與兩篇 ankle sprain 已形成足踝運動醫學主題群，但 wiki 目前缺對應來源摘要與主題頁。
  - Clinical assessment of walking and running gait 為高價值 Tier 1，應優先用來擴充 06_Gait_Biomechanics/步態評估總論.md，必要時拆出 walking/running gait 子頁。
  - ASICS GT 1000 12 為 commercial shoe review（RunRepeat），不屬 Tier 1；僅可視為 Tier 2 網站/產品資料，不應與 UpToDate 同層排序。
- 腳本修正：
  - 更新 08_工具與Workflow/wiki_health_check.py 的 backlog tier 推定邏輯，改為讀取 raw file 內容與 source URL，而非只靠檔名 token。
  - 修正後已重跑 health_check_report_latest.md；鞋款 review 由 tier=1 降為 tier=2。
- 深度 health check 結論：
  - 結構性 lint 仍維持 clean。
  - 新增人工判讀重點：06_Gait_Biomechanics 與足踝 / running-injury 子域有明顯 Tier 1 backlog，屬下一輪 ingest 高優先區。

## [2026-04-24] update | ingest 工作流規範
- 新建 workflow page：08_工具與Workflow/知識百科_ingest_工作流.md
- 更新 SCHEMA.md 的 ingest 規則，明確加入：
  - 先列候選、再依來源優先級與主題相關性排序
  - 單批最多選讀 10 份文件
  - 來源類型固定判定為 review article / textbook chapter / UpToDate / 科普書 / 網站資料 / original article
  - ingest 結束後必須留下下一批待處理名單
- 更新 08_工具與Workflow/知識百科_健康檢查流程.md，明確區分：
  - health check raw verification cap = 5 files
  - ingest batch cap = 10 files
- index.md 更新：Total pages 69 -> 70
- 本次僅更新 workflow / schema / index / log；未讀取新一批 raw 內容，也未修改 `C:\原始資料`

## [2026-04-24] update | wiki_health_check Windows 路徑自動判定
- 修正腳本：08_工具與Workflow/wiki_health_check.py
  - CLI 預設路徑不再寫死 `/mnt/c/...`
  - 改為自動偵測 `C:\知識百科` / `C:\原始資料`、WSL `/mnt/c/...`，必要時回退到腳本所在 wiki root
- 修正測試：08_工具與Workflow/tests/test_wiki_health_check.py
  - 測試載入路徑改為相對於測試檔自身解析
  - 新增 default root detection 測試
- 更新文件：08_工具與Workflow/Wiki_Health_Check_腳本.md
  - 執行範例改為 Windows PowerShell 指令
  - 補充路徑自動偵測說明

## [2026-04-24] update | wiki_health_check UTF-8 console output
- 修正腳本：08_工具與Workflow/wiki_health_check.py
  - 直接輸出到 Windows console 前先將 `stdout` reconfigure 為 UTF-8
  - 避免 `V̇O₂` 等字元在 `cp950` console 下觸發 `UnicodeEncodeError`

## [2026-04-24] lint | 全知識百科 health check（post-fix）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python 08_工具與Workflow/tests/test_wiki_health_check.py` → 4 tests passed
  - `python 08_工具與Workflow/wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 70
  - orphan 0
  - weak links 0
  - broken links 0
  - contradiction candidates 0
  - raw backlog: 189
  - raw verification queue: 5
- 說明：
  - 此次結果已確認來自正確的 Windows path 與 UTF-8 console output 修正後執行
  - 本回合僅更新 workflow / schema / health-check tooling，未執行新一批 source ingest

## [2026-04-24] ingest | PM&R orthotics / mobility / exercise / wound care（Batch 8）
- Batch: 8
- Candidate ranking（依來源優先級 + 同主題相關性排序）：
  1. 13 - Lower limb orthoses
  2. 15 - Wheelchairs and seating systems
  3. 16 - Therapeutic exercise
  4. 18 - Physical agent modalities
  5. 20 - Assistive technology and environmental control devices
  6. 12 - Upper limb orthoses and robotics
  7. 14 - Spinal orthoses
  8. 25 - Prevention and management of pressure injuries and chronic ulcers
  9. 17 - Manipulation, traction, and massage
  10. 19 - Integrative medicine in rehabilitation
- Selected files（本回合實際讀取 10/10）：
  1. 12 - Upper limb orthoses and robotics
  2. 13 - Lower limb orthoses
  3. 14 - Spinal orthoses
  4. 15 - Wheelchairs and seating systems
  5. 16 - Therapeutic exercise
  6. 17 - Manipulation, traction, and massage
  7. 18 - Physical agent modalities
  8. 19 - Integrative medicine in rehabilitation
  9. 20 - Assistive technology and environmental control devices
  10. 25 - Prevention and management of pressure injuries and chronic ulcers
- 類型與層級：
  - Upper limb orthoses and robotics：textbook chapter，Tier 1，可信度 high
  - Lower limb orthoses：textbook chapter，Tier 1，可信度 high
  - Spinal orthoses：textbook chapter，Tier 1，可信度 high
  - Wheelchairs and seating systems：textbook chapter，Tier 1，可信度 high
  - Therapeutic exercise：textbook chapter，Tier 1，可信度 high
  - Manipulation, traction, and massage：textbook chapter，Tier 1，可信度 high
  - Physical agent modalities：textbook chapter，Tier 1，可信度 high
  - Integrative medicine in rehabilitation：textbook chapter，Tier 1，可信度 high
  - Assistive technology and environmental control devices：textbook chapter，Tier 1，可信度 high
  - Prevention and management of pressure injuries and chronic ulcers：textbook chapter，Tier 1，可信度 high
- 新建來源摘要頁 10：
  - 09_來源摘要/Upper_limb_orthoses_and_robotics.md
  - 09_來源摘要/Lower_limb_orthoses.md
  - 09_來源摘要/Spinal_orthoses.md
  - 09_來源摘要/Wheelchairs_and_seating_systems.md
  - 09_來源摘要/Therapeutic_exercise.md
  - 09_來源摘要/Manipulation_traction_and_massage.md
  - 09_來源摘要/Physical_agent_modalities.md
  - 09_來源摘要/Integrative_medicine_in_rehabilitation.md
  - 09_來源摘要/Assistive_technology_and_environmental_control_devices.md
  - 09_來源摘要/Prevention_and_management_of_pressure_injuries_and_chronic_ulcers.md
- 新建主題頁 10：
  - 06_Gait_Biomechanics/上肢矯具與復健機器人.md
  - 06_Gait_Biomechanics/下肢矯具總論.md
  - 06_Gait_Biomechanics/脊椎裝具總論.md
  - 03_疾病與臨床主題/輪椅與座位系統總論.md
  - 03_疾病與臨床主題/輔具與環境控制裝置.md
  - 03_疾病與臨床主題/壓力性損傷與慢性傷口復健.md
  - 02_方法學/治療性運動處方.md
  - 02_方法學/徒手治療_牽引與按摩.md
  - 02_方法學/物理因子治療.md
  - 02_方法學/復健整合醫學.md
- 既有頁更新：
  - 03_疾病與臨床主題/PMR_評估總論.md
  - 03_疾病與臨床主題/中風復健總論.md
  - 03_疾病與臨床主題/脊髓損傷復健總論.md
  - 03_疾病與臨床主題/Spasticity_概論.md
  - 06_Gait_Biomechanics/步態評估總論.md
- 明確標示的 conflict / caveat：
  1. Therapeutic exercise 章節仍使用 legacy `anaerobic threshold` 與 `220-age`；可用於 practical exercise prescription，但不取代既有 CPET 現代框架。
  2. Physical agent modalities 應視為 adjunctive tool；acute soft-tissue icing 的高品質 healing evidence 不強，且 prolonged icing 可能干擾部分 healing response。
  3. Manipulation / traction / massage 的效益具 condition specificity；traction 長期證據不穩，HVLA 需明確安全篩檢。
  4. Assistive technology 不等於越新越好；abandonment 常見，user-fit、training 與 follow-up 是核心。
  5. Pressure injury / chronic ulcer management 的主軸是 etiology 與 offloading；不可把 dressing 或 therapeutic footwear 誤當主要治癒機制。
  6. Spinal orthosis prescription 不能只寫 brace 名稱；benign whiplash 的 prolonged soft collar use 沒有長期 outcome 優勢。
  7. Lower limb orthosis prescription 要用 GRF 與 joint moment 語言理解；lateral heel wedge 對 medial knee OA 並非強支持 default 處方。
- index.md 更新：Total pages 70 -> 90
- Pending files（下一批待處理）：
  - 23 - Sexual dysfunction and disability
  - 26 - Vascular diseases

## [2026-04-24] update | wiki_health_check backlog stem normalization
- 修正腳本：08_工具與Workflow/wiki_health_check.py
  - `normalize_stem()` 新增 chapter number prefix 去除（如 `13 - ...`）
  - 去除常見 copy suffix / duplicate marker（如 `的副本`、`(1)`、內嵌 `pdf` token）
- 修正測試：08_工具與Workflow/tests/test_wiki_health_check.py
  - 測試數由 4 增為 5
  - 新增 backlog stem normalization 覆蓋，避免已 ingest 來源被誤列為 raw backlog

## [2026-04-24] lint | 全知識百科 health check（post-ingest）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python 08_工具與Workflow/tests/test_wiki_health_check.py` → 5 tests passed
  - `python 08_工具與Workflow/wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 90
  - orphan 0
  - weak links 0
  - broken links 0
  - contradiction candidates 0
  - raw_backlog: 177
  - raw verification queue:
    1. 00140130412331290899/00140130412331290899.md
    2. 23 - Sexual dysfunction and disability/23 - Sexual dysfunction and disability.md
    3. 26 - Vascular diseases/26 - Vascular diseases.md
    4. Achilles tendinopathy - UpToDate.md
    5. Ankle sprain in adults_ Evaluation and diagnosis - UpToDate.md

## [2026-04-24] ingest | PM&R participation / medicolegal / pediatric care systems（Batch 9）
- Batch: 9
- Candidate ranking（依來源優先級 + 主題相關性排序）：
  1. 23 - Sexual dysfunction and disability
  2. 26 - Vascular diseases
  3. Rehabilitation and prosthetic restoration in upper limb amputation
  4. Occupational medicine and vocational rehabilitation
  5. Interprofessional Team-Based Care
  6. Practical aspects of impairment rating and disability determination
  7. Celebrating Sociocultural Diversity in the Exam Room and Addressing Racism and Bias
  8. Rehabilitation Services Occupational Therapy and Physical Therapy
- Selected files（本回合實際讀取 8/8）：
  1. 23 - Sexual dysfunction and disability
  2. 26 - Vascular diseases
  3. Rehabilitation and prosthetic restoration in upper limb amputation
  4. Occupational medicine and vocational rehabilitation
  5. Interprofessional Team-Based Care
  6. Practical aspects of impairment rating and disability determination
  7. Celebrating Sociocultural Diversity in the Exam Room and Addressing Racism and Bias
  8. Rehabilitation Services Occupational Therapy and Physical Therapy
- 類型與層級：
  - Sexual dysfunction and disability：textbook chapter，Tier 1，可信度 high
  - Vascular diseases：textbook chapter，Tier 1，可信度 high
  - Rehabilitation and prosthetic restoration in upper limb amputation：textbook chapter，Tier 1，可信度 high
  - Occupational medicine and vocational rehabilitation：textbook chapter，Tier 1，可信度 high
  - Interprofessional Team-Based Care：textbook chapter，Tier 1，可信度 high
  - Practical aspects of impairment rating and disability determination：textbook chapter，Tier 1，可信度 high
  - Celebrating Sociocultural Diversity in the Exam Room and Addressing Racism and Bias：textbook chapter，Tier 1，可信度 high
  - Rehabilitation Services Occupational Therapy and Physical Therapy：textbook chapter，Tier 1，可信度 high
- 新建來源摘要頁 8：
  - 09_來源摘要/Sexual_dysfunction_and_disability.md
  - 09_來源摘要/Vascular_diseases.md
  - 09_來源摘要/Rehabilitation_and_prosthetic_restoration_in_upper_limb_amputation.md
  - 09_來源摘要/Occupational_medicine_and_vocational_rehabilitation.md
  - 09_來源摘要/Interprofessional_Team_Based_Care.md
  - 09_來源摘要/Practical_aspects_of_impairment_rating_and_disability_determination.md
  - 09_來源摘要/Celebrating_sociocultural_diversity_in_the_exam_room_and_addressing_racism_and_bias.md
  - 09_來源摘要/Rehabilitation_services_occupational_therapy_and_physical_therapy.md
- 新建主題頁 8：
  - 03_疾病與臨床主題/性功能障礙與身心障礙復健.md
  - 03_疾病與臨床主題/血管與淋巴疾病復健.md
  - 03_疾病與臨床主題/上肢截肢復健總論.md
  - 02_方法學/職業醫學與職業復健.md
  - 02_方法學/障礙評定與失能判定.md
  - 02_方法學/跨專業團隊照護.md
  - 07_Pediatric_Development/文化謙遜與偏誤敏感照護.md
  - 07_Pediatric_Development/兒童OT與PT復健服務.md
- 既有頁更新：
  - 03_疾病與臨床主題/PMR_評估總論.md
  - 03_疾病與臨床主題/創傷性腦損傷復健總論.md
  - 03_疾病與臨床主題/中風復健總論.md
  - 03_疾病與臨床主題/脊髓損傷復健總論.md
  - 03_疾病與臨床主題/下肢截肢復健總論.md
  - 07_Pediatric_Development/小兒復健評估.md
- 明確標示的 conflict / caveat：
  1. Sexual dysfunction in disability 不等於單純 neurologic deficit；只有在造成 distress / quality-of-life impact 時才構成需處理的 disorder framing。
  2. PAD 患者的 exercise 通常是治療而非禁忌；compression 則需依 arterial status 調整。
  3. Impairment rating 不等於 disability 或 participation restriction；醫師也不應越權決定 accommodation reasonableness。
  4. Multidisciplinary parallel care 不等於 interprofessional team-based care；一次性資訊傳遞也不等於 care coordination。
  5. race 不應被當作 biologic risk factor；臨床上更 relevant 的 exposure 是 racism、bias 與 SDOH。
  6. 最先進 myoelectric prosthesis 不一定最適合；device selection 必須回到功能目標、環境、維修可近性與成本。
- index.md 更新：Total pages 90 -> 106
- Pending files（下一批待處理）：
  - Achilles tendinopathy - UpToDate.md
  - Ankle sprain in adults_ Evaluation and diagnosis - UpToDate.md
  - Ankle sprain in adults_ Management - UpToDate.md
  - Clinical assessment of walking and running gait - UpToDate.md
  - 00140130412331290899/00140130412331290899.md

## [2026-04-24] lint | 全知識百科 health check（post-batch-9）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python 08_工具與Workflow/tests/test_wiki_health_check.py` → 5 tests passed
  - `python 08_工具與Workflow/wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 106
  - orphan 0
  - weak links 0
  - broken links 0
  - contradiction candidates 0
  - raw_backlog: 169
  - raw verification queue:
    1. 00140130412331290899/00140130412331290899.md
    2. Achilles tendinopathy - UpToDate.md
    3. Ankle sprain in adults_ Evaluation and diagnosis - UpToDate.md
    4. Ankle sprain in adults_ Management - UpToDate.md
    5. Attention deficit hyperactivity disorder in children and adolescents_ Clinical features and diagnosis (1).md

## [2026-04-24] ingest | foot / ankle / running injury frameworks（Batch 10）
- Batch: 10
- Candidate ranking（依來源優先級 + 主題相關性排序）：
  1. Clinical assessment of walking and running gait - UpToDate
  2. Overview of foot anatomy and biomechanics and assessment of foot pain in adults - UpToDate
  3. Achilles tendinopathy - UpToDate
  4. Ankle sprain in adults: Evaluation and diagnosis - UpToDate
  5. Ankle sprain in adults: Management - UpToDate
  6. Syndesmotic ankle injury (high ankle sprain) - UpToDate
  7. Plantar fasciitis - UpToDate
  8. Forefoot pain in adults: Evaluation, diagnosis, and select management of common causes - UpToDate
  9. Hindfoot pain in adults: Evaluation and diagnosis of common causes - UpToDate
  10. Midfoot pain in adults: Evaluation, diagnosis, and select management of common causes - UpToDate
  11. 00140130412331290899/00140130412331290899.md（暫緩；與本批 foot / ankle 主題相關性較低）
- Selected files（本回合實際讀取 10/10）：
  1. Clinical assessment of walking and running gait - UpToDate
  2. Overview of foot anatomy and biomechanics and assessment of foot pain in adults - UpToDate
  3. Achilles tendinopathy - UpToDate
  4. Ankle sprain in adults: Evaluation and diagnosis - UpToDate
  5. Ankle sprain in adults: Management - UpToDate
  6. Syndesmotic ankle injury (high ankle sprain) - UpToDate
  7. Plantar fasciitis - UpToDate
  8. Forefoot pain in adults: Evaluation, diagnosis, and select management of common causes - UpToDate
  9. Hindfoot pain in adults: Evaluation and diagnosis of common causes - UpToDate
  10. Midfoot pain in adults: Evaluation, diagnosis, and select management of common causes - UpToDate
- 類型與層級：
  - 全部 10 份皆為 UpToDate，Tier 1，可信度 high
- 新建來源摘要頁 10：
  - 09_來源摘要/Clinical_assessment_of_walking_and_running_gait.md
  - 09_來源摘要/Overview_of_foot_anatomy_and_biomechanics_and_assessment_of_foot_pain_in_adults.md
  - 09_來源摘要/Achilles_tendinopathy.md
  - 09_來源摘要/Ankle_sprain_in_adults_Evaluation_and_diagnosis.md
  - 09_來源摘要/Ankle_sprain_in_adults_Management.md
  - 09_來源摘要/Syndesmotic_ankle_injury_high_ankle_sprain.md
  - 09_來源摘要/Plantar_fasciitis.md
  - 09_來源摘要/Forefoot_pain_in_adults_Evaluation_diagnosis_and_select_management_of_common_causes.md
  - 09_來源摘要/Hindfoot_pain_in_adults_Evaluation_and_diagnosis_of_common_causes.md
  - 09_來源摘要/Midfoot_pain_in_adults_Evaluation_diagnosis_and_select_management_of_common_causes.md
- 新建主題頁 6：
  - 06_Gait_Biomechanics/足部解剖與生物力學.md
  - 03_疾病與臨床主題/足部疼痛分區評估.md
  - 03_疾病與臨床主題/Achilles_tendinopathy.md
  - 03_疾病與臨床主題/Ankle_sprain_總論.md
  - 03_疾病與臨床主題/Syndesmotic_ankle_injury.md
  - 03_疾病與臨床主題/Plantar_fasciitis.md
- 既有頁更新：
  - 06_Gait_Biomechanics/步態評估總論.md
- 明確標示的 conflict / caveat：
  1. Adult clinical gait assessment 沒有單一 standardized bedside gold-standard；它是 structured observation，不是 gait-lab substitute。
  2. 對無症狀跑者 routine 把 rearfoot strike 改成 forefoot strike，沒有足夠理由當成 injury-prevention default。
  3. Foot structure 不能單獨決定 injury risk；static arch、dynamic motion 與 load context 必須一起看。
  4. Achilles 問題不應一律叫 tendinitis；midportion 與 insertional disease 的 rehab strategy 也不同。
  5. Acute ankle sprain 多數不需要直接 MRI；Ottawa ankle rules 仍是 early imaging 主軸，brace + rehab 比 prolonged rest 更重要。
  6. High ankle sprain 不是單純比較嚴重的 lateral sprain；grade 2/3 常需更早 orthopedic decision。
  7. Heel spur 不是 plantar fasciitis 的診斷錨點；ESWT、custom orthotics、surgery 也不應被講成 default solution。
- index.md 更新：Total pages 106 -> 122
- Pending files（下一批待處理）：
  - 00140130412331290899/00140130412331290899.md

## [2026-04-24] update | wiki_health_check backlog normalization（UpToDate suffix）
- 修正腳本：08_工具與Workflow/wiki_health_check.py
  - `normalize_stem()` 新增去除 raw filename 尾端 `UpToDate` token
- 修正測試：08_工具與Workflow/tests/test_wiki_health_check.py
  - 補上 `Achilles tendinopathy - UpToDate.md` 對 `Achilles_tendinopathy.md` 的 normalization 覆蓋
- 補反向 wikilink：
  - 06_Gait_Biomechanics/步態評估總論.md → 09_來源摘要/Clinical_assessment_of_walking_and_running_gait.md
  - 03_疾病與臨床主題/足部疼痛分區評估.md → 09_來源摘要/Forefoot / Midfoot / Hindfoot pain summaries

## [2026-04-24] lint | 全知識百科 health check（post-batch-10）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python 08_工具與Workflow/tests/test_wiki_health_check.py` → 5 tests passed
  - `python 08_工具與Workflow/wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 122
  - orphan 0
  - weak links 0
  - broken links 0
  - contradiction candidates 0
  - raw_backlog: 159
  - raw verification queue:
    1. 00140130412331290899/00140130412331290899.md
    2. Attention deficit hyperactivity disorder in children and adolescents_ Clinical features and diagnosis (1).md
    3. Attention deficit hyperactivity disorder in children and adolescents_ Epidemiology and pathogenesis.md
    4. Attention deficit hyperactivity disorder in children and adolescents_ Overview of treatment and prognosis (1).md
    5. Attention deficit hyperactivity disorder in children and adolescents_ Treatment with nonstimulant medications.md

## [2026-04-24] ingest | pediatric ADHD framework（Batch 11）
- Batch: 11
- Candidate ranking（依來源優先級 + 主題相關性排序）：
  1. Attention deficit hyperactivity disorder in children and adolescents: Clinical features and diagnosis - UpToDate
  2. Attention deficit hyperactivity disorder in children and adolescents: Epidemiology and pathogenesis - UpToDate
  3. Attention deficit hyperactivity disorder in children and adolescents: Overview of treatment and prognosis - UpToDate
  4. Attention deficit hyperactivity disorder in children and adolescents: Treatment with stimulant medications - UpToDate
  5. Attention deficit hyperactivity disorder in children and adolescents: Treatment with nonstimulant medications - UpToDate
  6. Cardiac evaluation of patients receiving pharmacotherapy for attention deficit hyperactivity disorder (ADHD) - UpToDate
  7. Sleep in children and adolescents with attention deficit hyperactivity disorder - UpToDate
  8. Attention-Deficit/Hyperactivity Disorder - textbook chapter (Harstad)
  9. Attention-Deficit/Hyperactivity Disorder (ADHD) - textbook chapter (Barbaresi / Fogler)
  10. 00140130412331290899/00140130412331290899.md（暫緩；與本批 pediatric ADHD 主題相關性較低）
- Selected files（本回合實際讀取 9/10）：
  1. Attention deficit hyperactivity disorder in children and adolescents: Clinical features and diagnosis - UpToDate
  2. Attention deficit hyperactivity disorder in children and adolescents: Epidemiology and pathogenesis - UpToDate
  3. Attention deficit hyperactivity disorder in children and adolescents: Overview of treatment and prognosis - UpToDate
  4. Attention deficit hyperactivity disorder in children and adolescents: Treatment with stimulant medications - UpToDate
  5. Attention deficit hyperactivity disorder in children and adolescents: Treatment with nonstimulant medications - UpToDate
  6. Cardiac evaluation of patients receiving pharmacotherapy for attention deficit hyperactivity disorder (ADHD) - UpToDate
  7. Sleep in children and adolescents with attention deficit hyperactivity disorder - UpToDate
  8. Attention-Deficit/Hyperactivity Disorder - textbook chapter (Harstad)
  9. Attention-Deficit/Hyperactivity Disorder (ADHD) - textbook chapter (Barbaresi / Fogler)
- 類型與層級：
  - UpToDate 7 份：Tier 1，可信度 high
  - textbook chapter 2 份：Tier 1，可信度 high
- 新建來源摘要頁 9：
  - 09_來源摘要/Attention_deficit_hyperactivity_disorder_in_children_and_adolescents_Clinical_features_and_diagnosis.md
  - 09_來源摘要/Attention_deficit_hyperactivity_disorder_in_children_and_adolescents_Epidemiology_and_pathogenesis.md
  - 09_來源摘要/Attention_deficit_hyperactivity_disorder_in_children_and_adolescents_Overview_of_treatment_and_prognosis.md
  - 09_來源摘要/Attention_deficit_hyperactivity_disorder_in_children_and_adolescents_Treatment_with_stimulant_medications.md
  - 09_來源摘要/Attention_deficit_hyperactivity_disorder_in_children_and_adolescents_Treatment_with_nonstimulant_medications.md
  - 09_來源摘要/Cardiac_evaluation_of_patients_receiving_pharmacotherapy_for_attention_deficit_hyperactivity_disorder_ADHD.md
  - 09_來源摘要/Sleep_in_children_and_adolescents_with_attention_deficit_hyperactivity_disorder.md
  - 09_來源摘要/Attention_Deficit_Hyperactivity_Disorder.md
  - 09_來源摘要/Attention_Deficit_Hyperactivity_Disorder_ADHD.md
- 新建主題頁 5：
  - 07_Pediatric_Development/ADHD_總論.md
  - 07_Pediatric_Development/ADHD_評估與診斷.md
  - 07_Pediatric_Development/ADHD_治療總論.md
  - 07_Pediatric_Development/ADHD_藥物治療與安全.md
  - 07_Pediatric_Development/ADHD_睡眠與常見共病.md
- 既有頁更新：
  - 07_Pediatric_Development/小兒復健評估.md
  - 07_Pediatric_Development/兒童OT與PT復健服務.md
- 明確標示的 conflict / caveat：
  1. ADHD 不能用單次門診 impression、單一量表、qEEG 或 neuropsychological testing alone 下診斷。
  2. ADHD 不是 normal childhood behavior 被醫療化，也不能被 sugar、food additive 或 poor parenting 單獨解釋。
  3. coexisting condition 是常態；sleep disorder、learning disorder、ASD、language disorder、anxiety、depression 都可能改變診斷與功能表現。
  4. medication 不是整個 treatment plan；PTBM、school accommodation、skills training 與定期 reevaluation 都要並行。
  5. stimulant 常是 first-line，但 routine ECG 不是 blanket rule；targeted cardiovascular history / exam 才是前測核心。
  6. nonstimulant 不是單純比較安全或比較溫和的替代品；起效、BP / HR effect、suicidality 與 sedation 都要個別監測。
  7. insomnia 不應一律怪 stimulant；sleep deprivation、OSA、restless legs / PLMD、rebound effect 都要分清。
- index.md 更新：Total pages 122 -> 136
- Pending files（下一批待處理）：
  - 00140130412331290899/00140130412331290899.md

## [2026-04-24] lint | 全知識百科 health check（post-batch-11）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python 08_工具與Workflow/tests/test_wiki_health_check.py` → 5 tests passed
  - `python 08_工具與Workflow/wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 136
  - orphan 0
  - weak links 0
  - broken links 0
  - contradiction candidates 0
  - raw_backlog: 150
  - raw verification queue:
    1. 00140130412331290899/00140130412331290899.md
    2. Autism Spectrum Disorder/Autism Spectrum Disorder.md
    3. Autism Spectrum Disorder/Autism Spectrum Disorder (ASD).md
    4. Autism spectrum disorder (ASD) in children and adolescents_ Terminology, epidemiology, and pathogenesis.md
    5. Autism spectrum disorder in children and adolescents_ Behavioral and educational interventions.md

## [2026-04-24] ingest | pediatric ASD framework（Batch 12）
- Batch: 12
- Candidate ranking（依來源優先級 + 主題相關性排序）：
  1. Autism Spectrum Disorder — textbook chapter
  2. Autism Spectrum Disorder (ASD) — textbook chapter
  3. Autism spectrum disorder (ASD) in children and adolescents: Terminology, epidemiology, and pathogenesis — UpToDate
  4. Autism spectrum disorder in children and adolescents: Clinical features — UpToDate
  5. Autism spectrum disorder in children and adolescents: Evaluation and diagnosis — UpToDate
  6. Autism spectrum disorder in children and adolescents: Overview of management and prognosis — UpToDate
  7. Autism spectrum disorder in children and adolescents: Behavioral and educational interventions — UpToDate
  8. Autism spectrum disorder in children and adolescents: Pharmacologic interventions — UpToDate
  9. Autism spectrum disorder in children and adolescents: Screening tools — UpToDate
  10. Autism spectrum disorder in children and adolescents: Surveillance and screening in primary care — UpToDate
  11. Autism spectrum disorder in children and adolescents: Complementary and integrative medicine therapies — UpToDate（因 10-file cap 延到下一批）
- Selected files（本回合實際讀取 10/11）：
  1. Autism Spectrum Disorder — textbook chapter
  2. Autism Spectrum Disorder (ASD) — textbook chapter
  3. Autism spectrum disorder (ASD) in children and adolescents: Terminology, epidemiology, and pathogenesis — UpToDate
  4. Autism spectrum disorder in children and adolescents: Clinical features — UpToDate
  5. Autism spectrum disorder in children and adolescents: Evaluation and diagnosis — UpToDate
  6. Autism spectrum disorder in children and adolescents: Overview of management and prognosis — UpToDate
  7. Autism spectrum disorder in children and adolescents: Behavioral and educational interventions — UpToDate
  8. Autism spectrum disorder in children and adolescents: Pharmacologic interventions — UpToDate
  9. Autism spectrum disorder in children and adolescents: Screening tools — UpToDate
  10. Autism spectrum disorder in children and adolescents: Surveillance and screening in primary care — UpToDate
- 類型與層級：
  - textbook chapter 2 份：Tier 1，可信度 high
  - UpToDate 8 份：Tier 1，可信度 high
- 新建來源摘要頁 10：
  - 09_來源摘要/Autism_Spectrum_Disorder.md
  - 09_來源摘要/Autism_Spectrum_Disorder_ASD.md
  - 09_來源摘要/Autism_spectrum_disorder_ASD_in_children_and_adolescents_Terminology_epidemiology_and_pathogenesis.md
  - 09_來源摘要/Autism_spectrum_disorder_in_children_and_adolescents_Clinical_features.md
  - 09_來源摘要/Autism_spectrum_disorder_in_children_and_adolescents_Evaluation_and_diagnosis.md
  - 09_來源摘要/Autism_spectrum_disorder_in_children_and_adolescents_Overview_of_management_and_prognosis.md
  - 09_來源摘要/Autism_spectrum_disorder_in_children_and_adolescents_Behavioral_and_educational_interventions.md
  - 09_來源摘要/Autism_spectrum_disorder_in_children_and_adolescents_Pharmacologic_interventions.md
  - 09_來源摘要/Autism_spectrum_disorder_in_children_and_adolescents_Screening_tools.md
  - 09_來源摘要/Autism_spectrum_disorder_in_children_and_adolescents_Surveillance_and_screening_in_primary_care.md
- 新建主題頁 6：
  - 07_Pediatric_Development/ASD_總論.md
  - 07_Pediatric_Development/ASD_臨床表現.md
  - 07_Pediatric_Development/ASD_評估與診斷.md
  - 07_Pediatric_Development/ASD_篩檢與早期辨識.md
  - 07_Pediatric_Development/ASD_介入與預後.md
  - 07_Pediatric_Development/ASD_藥物與共病管理.md
- 既有頁更新：
  - 07_Pediatric_Development/小兒復健評估.md
- 明確標示的 conflict / caveat：
  1. ASD 不是 vaccine-related disorder，也不能被單一教養理論解釋。
  2. female presentation 與 camouflaging 會延後辨識，不能用 male-biased template 當唯一標準。
  3. screening 不提供 diagnosis；positive screen 的下一步是 referral，不是 watchful waiting。
  4. general developmental screener 不能取代 ASD-specific screener；negative screen 也不能直接排除 later ASD。
  5. diagnostic tool 不能脫離 clinical judgment 單獨使用；ASD 與 language disorder / ID / ADHD / anxiety 邊界要重做 differential。
  6. medication 處理的是 target symptom / comorbidity，不是 core ASD deficit。
  7. sensory integration 與各式熱門療法都不能取代 structured behavioral / educational intervention。
- index.md 更新：Total pages 136 -> 152
- Pending files（下一批待處理）：
  - Autism spectrum disorder in children and adolescents: Complementary and integrative medicine therapies — UpToDate
  - 00140130412331290899/00140130412331290899.md
  - Developmental-behavioral surveillance and screening in primary care - UpToDate.md
  - Developmental Delay and Intellectual Disability/Developmental Delay and Intellectual Disability.md
  - Intellectual disability (ID) in children_ Clinical features, evaluation, and diagnosis.md

## [2026-04-24] ingest | ASD complementary therapy addendum（Batch 13）
- Batch: 13
- Selected files（本回合實際讀取 1/1）：
  1. Autism spectrum disorder in children and adolescents: Complementary and integrative medicine therapies — UpToDate
- 類型與層級：
  - UpToDate 1 份：Tier 1，可信度 high
- 新建來源摘要頁 1：
  - 09_來源摘要/Autism_spectrum_disorder_in_children_and_adolescents_Complementary_and_integrative_medicine_therapies.md
- 既有頁更新：
  - 07_Pediatric_Development/ASD_介入與預後.md
- 明確標示的 conflict / caveat：
  1. complementary therapy 常見，不等於有效。
  2. music therapy 可作 limited-evidence adjunct，但不能取代主幹 program。
  3. leucovorin / folic acid、sulforaphane、TMS / tPCS 目前都不足以 routine recommend。
- index.md 更新：Total pages 152 -> 153
- Pending files（下一批待處理）：
  - 00140130412331290899/00140130412331290899.md
  - Biomechanics of the Foot and Ankle/Biomechanics of the Foot and Ankle.md
  - Biomechanics of the hip, knee, and ankle/Biomechanics of the hip, knee, and ankle.md
  - Blindness and Visual Impairment/Blindness and Visual Impairment.md
  - Cerebral Palsy and Other Motor Disorders/Cerebral Palsy and Other Motor Disorders.md

## [2026-04-24] lint | 全知識百科 health check（post-batch-13）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python 08_工具與Workflow/tests/test_wiki_health_check.py` → 5 tests passed
  - `python 08_工具與Workflow/wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 153
  - orphan 0
  - weak links 0
  - broken links 0
  - contradiction candidates 0
  - raw_backlog: 139
  - raw verification queue:
    1. 00140130412331290899/00140130412331290899.md
    2. Biomechanics of the Foot and Ankle/Biomechanics of the Foot and Ankle.md
    3. Biomechanics of the hip, knee, and ankle/Biomechanics of the hip, knee, and ankle.md
    4. Blindness and Visual Impairment/Blindness and Visual Impairment.md
    5. Cerebral Palsy and Other Motor Disorders/Cerebral Palsy and Other Motor Disorders.md

## [2026-04-24] create | schema 1–8 overview pages
- 新建頁面：
  - 00_總覽/知識百科_基礎規範總覽.md
  - 00_總覽/主題地圖.md
- 目的：
  - 把 schema 第 1 到第 8 點整理成可直接操作的 overview layer。
  - 補上跨資料夾主題導航，降低新頁成為弱連結或孤立頁的機率。

## [2026-04-24] update | index schema-1-to-8 alignment
- 更新檔案：index.md
- 調整內容：
  - 新增 `00_總覽` 區段與 2 個 overview 頁入口。
  - 將索引格式統一為：頁名 + 一句話摘要 + 主題分類 + 重要來源層級。
  - Total pages: 153 -> 155

## [2026-04-24] lint | 全知識百科 health check（post-schema-1-to-8 alignment）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python 08_工具與Workflow/tests/test_wiki_health_check.py` → 5 tests passed
  - `python 08_工具與Workflow/wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 155
  - orphan 0
  - weak links 0
  - broken links 0
  - missing_from_index 0
  - contradiction candidates 0
  - raw_backlog: 139
  - raw verification queue:
    1. 00140130412331290899/00140130412331290899.md
    2. Biomechanics of the Foot and Ankle/Biomechanics of the Foot and Ankle.md
    3. Biomechanics of the hip, knee, and ankle/Biomechanics of the hip, knee, and ankle.md
    4. Blindness and Visual Impairment/Blindness and Visual Impairment.md
    5. Cerebral Palsy and Other Motor Disorders/Cerebral Palsy and Other Motor Disorders.md

## [2026-04-24] ingest | pediatric neurology / CP / vision / foot biomechanics / shoe selection / preterm outcomes（Batch 14）
- Batch: 14
- Selected files（本回合實際讀取 10/10）：
  1. 00140130412331290899/00140130412331290899.md
  2. Biomechanics of the Foot and Ankle/Biomechanics of the Foot and Ankle.md
  3. Biomechanics of the hip, knee, and ankle/Biomechanics of the hip, knee, and ankle.md
  4. Blindness and Visual Impairment/Blindness and Visual Impairment.md
  5. Cerebral Palsy and Other Motor Disorders/Cerebral Palsy and Other Motor Disorders.md
  6. Child Care/Child Care.md
  7. Childhood Obesity/Childhood Obesity.md
  8. Consequences of Preterm Birth/Consequences of Preterm Birth.md
  9. Considerations in the Selection of a Running Shoe/Considerations in the Selection of a Running Shoe.md
  10. Detailed neurologic assessment of infants and children - UpToDate.md
- 類型與層級：
  - original article 1 份：Tier 3，可信度 moderate
  - textbook chapter 8 份：Tier 1，可信度 high
  - UpToDate 1 份：Tier 1，可信度 high
- 新建來源摘要頁 10：
  - 09_來源摘要/Modelling_the_VO2_kinetic_response_to_heavy_intensity_exercise_in_children.md
  - 09_來源摘要/Biomechanics_of_the_Foot_and_Ankle.md
  - 09_來源摘要/Biomechanics_of_the_Hip_Knee_and_Ankle.md
  - 09_來源摘要/Blindness_and_Visual_Impairment.md
  - 09_來源摘要/Cerebral_Palsy_and_Other_Motor_Disorders.md
  - 09_來源摘要/Child_Care.md
  - 09_來源摘要/Childhood_Obesity.md
  - 09_來源摘要/Consequences_of_Preterm_Birth.md
  - 09_來源摘要/Considerations_in_the_Selection_of_a_Running_Shoe.md
  - 09_來源摘要/Detailed_neurologic_assessment_of_infants_and_children.md
- 新建主題頁 7：
  - 06_Gait_Biomechanics/跑鞋選擇原則.md
  - 07_Pediatric_Development/兒童視覺障礙與CVI.md
  - 07_Pediatric_Development/Cerebral_Palsy_總論.md
  - 07_Pediatric_Development/托育與Early_Care_and_Education.md
  - 07_Pediatric_Development/兒童肥胖.md
  - 07_Pediatric_Development/早產兒長期結局.md
  - 07_Pediatric_Development/兒童神經學評估.md
- 既有頁更新：
  - 04_CPET/VO2_Kinetics.md
  - 06_Gait_Biomechanics/足部解剖與生物力學.md
  - 06_Gait_Biomechanics/下肢矯具總論.md
  - 03_疾病與臨床主題/感覺障礙復健總論.md
  - 07_Pediatric_Development/小兒復健評估.md
  - 00_總覽/主題地圖.md
- 明確標示的 conflict / caveat：
  1. Fawkner and Armstrong 2004 使用 TAN / anaerobic threshold 歷史術語；本 wiki 保留為 Tier 3 limited evidence，不覆寫 LT / GET / CP 主框架。
  2. foot structure 與 shoe prescription 都不能只靠靜態 arch label；subtalar、transverse tarsal、timing 與 footwear context 必須一起看。
  3. 多 cushioning 或 motion-control shoe 不是較安全的 routine default；abrupt minimal-shoe transition 也可能增加 loading。
  4. orthosis prescription 不是只選 brace type；GRF、AFO-footwear combination、tuning 與 shank-thigh alignment 都會改變 proximal moment。
  5. pediatric visual impairment 不能只寫 visual acuity；prematurity、brain injury 與 CVI 可能比單純 ocular diagnosis 更影響功能。
  6. CP 雖屬 nonprogressive brain injury，但 musculoskeletal burden 與 phenotype 會隨成長改變；normal MRI 也不排除 CP。
  7. child care / ECE 是 developmental environment，不只是家庭托育安排；structural regulation 不等於 process quality 或 inclusion。
  8. childhood obesity 不是 willpower 問題；weight stigma 會惡化就醫、mental health 與 participation。
  9. preterm follow-up 不能因 early imaging normal 就放鬆；language、learning、behavior 等所謂 minor sequelae 仍可能有高功能負擔。
- index.md 更新：Total pages 155 -> 172

## [2026-04-24] update | wiki_health_check explicit raw-source matching
- 更新檔案：
  - 08_工具與Workflow/wiki_health_check.py
  - 08_工具與Workflow/tests/test_wiki_health_check.py
- 調整內容：
  - health check backlog 判定新增讀取來源摘要內 `原始檔` 路徑的邏輯。
  - 修正作者名摘要檔、匿名數字檔名與原始檔名不一致時的 false positive backlog。
  - 新增測試覆蓋 Windows-style raw path normalization 與 opaque raw filename matching。

## [2026-04-24] lint | 全知識百科 health check（post-batch-14）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python 08_工具與Workflow/tests/test_wiki_health_check.py` → 6 tests passed
  - `python 08_工具與Workflow/wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 172
  - orphan 0
  - weak links 0
  - broken links 0
  - missing_from_index 0
  - contradiction candidates 0
  - raw_backlog: 124
  - raw verification queue:
    1. Developmental Considerations in Deafness/Developmental Considerations in Deafness.md
    2. Developmental Delay and Intellectual Disability/Developmental Delay and Intellectual Disability.md
    3. Developmental Surveillance and Screening/Developmental Surveillance and Screening.md
    4. Developmental and Behavioral Surveillance and Screening/Developmental and Behavioral Surveillance and Screening.md
    5. Developmental-behavioral surveillance and screening in primary care - UpToDate.md

## [2026-04-24] ingest | Developmental and Behavioral Surveillance and Screening
- 類型：textbook chapter
- 來源層級：Tier 1；可信度：high
- 新建：09_來源摘要/Developmental_and_Behavioral_Surveillance_and_Screening.md
- 回寫：07_Pediatric_Development/發展監測與篩檢.md、07_Pediatric_Development/小兒復健評估.md
- 明確標示：surveillance 與 screening 互補，不能互相取代。

## [2026-04-24] ingest | Developmental Considerations in Deafness
- 類型：textbook chapter
- 來源層級：Tier 1；可信度：high
- 新建：09_來源摘要/Developmental_Considerations_in_Deafness.md、07_Pediatric_Development/兒童聽覺障礙與Deafness.md
- 回寫：03_疾病與臨床主題/感覺障礙復健總論.md、07_Pediatric_Development/小兒復健評估.md
- 明確標示：通過 newborn hearing screening 不等於排除 later-onset / progressive hearing loss。

## [2026-04-24] ingest | Developmental Delay and Intellectual Disability
- 類型：textbook chapter
- 來源層級：Tier 1；可信度：high
- 新建：09_來源摘要/Developmental_Delay_and_Intellectual_Disability.md、07_Pediatric_Development/發展遲緩與Intellectual_Disability.md
- 回寫：07_Pediatric_Development/兒童神經學評估.md、07_Pediatric_Development/小兒復健評估.md
- 明確標示：ID 不能只靠 IQ 定義；regression 也不可被當成 static delay。

## [2026-04-24] ingest | Developmental Surveillance and Screening
- 類型：textbook chapter
- 來源層級：Tier 1；可信度：high
- 新建：09_來源摘要/Developmental_Surveillance_and_Screening.md
- 回寫：07_Pediatric_Development/發展監測與篩檢.md
- 明確標示：AAP general developmental screening 與 autism screening 需依節點執行。

## [2026-04-24] ingest | Developmental-behavioral surveillance and screening in primary care
- 類型：UpToDate
- 來源層級：Tier 1；可信度：high
- 新建：09_來源摘要/Developmental_behavioral_surveillance_and_screening_in_primary_care.md
- 回寫：07_Pediatric_Development/發展監測與篩檢.md、07_Pediatric_Development/晚語兒_Late_Talker.md
- 明確標示：positive screen 的下一步是 evaluation / referral，不是被動追蹤。

## [2026-04-24] ingest | Early Intervention
- 類型：textbook chapter
- 來源層級：Tier 1；可信度：high
- 新建：09_來源摘要/Early_Intervention.md、07_Pediatric_Development/Early_Intervention_總論.md
- 回寫：07_Pediatric_Development/發展監測與篩檢.md、07_Pediatric_Development/托育與Early_Care_and_Education.md、07_Pediatric_Development/小兒復健評估.md
- 明確標示：EI eligibility 門檻不等於臨床重要性。

## [2026-04-24] ingest | Emergent literacy including language development
- 類型：UpToDate
- 來源層級：Tier 1；可信度：high
- 新建：09_來源摘要/Emergent_literacy_including_language_development.md、07_Pediatric_Development/早期語言發展與Emergent_Literacy.md
- 回寫：07_Pediatric_Development/托育與Early_Care_and_Education.md
- 明確標示：literacy 從早期語言互動開始，不是入學後才開始。

## [2026-04-24] ingest | Encouraging infant communication and play
- 類型：網站資料 / caregiver manual
- 來源層級：Tier 2；可信度：moderate
- 新建：09_來源摘要/Encouraging_infant_communication_and_play.md
- 回寫：07_Pediatric_Development/早期語言發展與Emergent_Literacy.md
- 明確標示：pilot feasibility study，不可當作 consensus-level intervention proof。

## [2026-04-24] ingest | Exertional Leg Pain in Runners
- 類型：textbook chapter
- 來源層級：Tier 1；可信度：high
- 新建：09_來源摘要/Exertional_Leg_Pain_in_Runners.md、03_疾病與臨床主題/跑者運動性下腿痛.md
- 回寫：06_Gait_Biomechanics/步態評估總論.md、06_Gait_Biomechanics/跑鞋選擇原則.md、06_Gait_Biomechanics/足部解剖與生物力學.md
- 明確標示：shin pain 不能直接等同 MTSS；需保留 CECS / vascular / neurologic differential。

## [2026-04-24] ingest | Expressive language delay ("late talking") in young children
- 類型：UpToDate
- 來源層級：Tier 1；可信度：high
- 新建：09_來源摘要/Expressive_language_delay_late_talking_in_young_children.md、07_Pediatric_Development/晚語兒_Late_Talker.md
- 回寫：07_Pediatric_Development/發展監測與篩檢.md、07_Pediatric_Development/小兒復健評估.md
- 明確標示：`boys talk later`、`雙語所以慢` 都不是延後評估的合理理由。

## [2026-04-24] lint | 全知識百科 health check（post-batch-15）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python 08_工具與Workflow/tests/test_wiki_health_check.py` → 6 tests passed
  - `python 08_工具與Workflow/wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 189
  - orphan 0
  - weak links 0
  - broken links 0
  - missing_from_index 0
  - contradiction candidates 0
  - raw_backlog: 114
  - raw verification queue:
    1. Feeding and Swallowing Disorders/Feeding and Swallowing Disorders.md
    2. Foot biomechanics/Foot biomechanics.md
    3. Foster Care and Adoption/Foster Care and Adoption.md
    4. GaesserandPoole_ESSR1996_Theslowcomponentofoxygenuptakekineticsinhumans/GaesserandPoole_ESSR1996_Theslowcomponentofoxygenuptakekineticsinhumans.md
    5. Hamstring muscle and tendon injuries - UpToDate.md

## [2026-04-24] update | 全知識百科費曼式骨架重構
- 範圍：189 個 Markdown 知識頁
- 排除：`index.md`、`log.md`、`SCHEMA.md`、`08_工具與Workflow/health_check_report_latest.md`
- 動作：統一改寫為「一句話定義 → 核心機制 → 臨床表現 → 評估方式 → 治療原則 → 臨床決策點 → 限制與未定論 → 理解缺口 → 臨床使用版 → 來源 → 相關頁面」
- 保留：frontmatter、來源摘要連結、相關頁面與既有段落內容
- 補上：`理解缺口`、`臨床使用版`、`來源` 與 decision-support framing
- 腳本：`08_工具與Workflow/feynman_restructure.py`
- 備份：`C:\codex files\backup_knowledge_feynman_20260424\知識百科`

## [2026-04-24] ingest | pediatric developmental stages / parenting / trauma / language / feeding（Batch 16）
- Batch: 16
- Selected files（本回合實際讀取 10/10）：
  1. Feeding and Swallowing Disorders/Feeding and Swallowing Disorders.md
  2. Foster Care and Adoption/Foster Care and Adoption.md
  3. Infancy/Infancy.md
  4. Toddlerhood and the Preschool Years/Toddlerhood and the Preschool Years.md
  5. Middle Childhood/Middle Childhood.md
  6. Positive Parenting and Support/Positive Parenting and Support.md
  7. Trauma, Resilience, and Child Development/Trauma, Resilience, and Child Development.md
  8. The Influence of Digital Media on Children and Families/The Influence of Digital Media on Children and Families.md
  9. Language Development and Communication Disorders/Language Development and Communication Disorders.md
  10. Language and Speech Disorders/Language and Speech Disorders.md
- 類型與層級：
  - textbook chapter 10 份：Tier 1，可信度 high
- 新建來源摘要頁 10：
  - 09_來源摘要/Feeding_and_Swallowing_Disorders.md
  - 09_來源摘要/Foster_Care_and_Adoption.md
  - 09_來源摘要/Infancy.md
  - 09_來源摘要/Toddlerhood_and_the_Preschool_Years.md
  - 09_來源摘要/Middle_Childhood.md
  - 09_來源摘要/Positive_Parenting_and_Support.md
  - 09_來源摘要/Trauma_Resilience_and_Child_Development.md
  - 09_來源摘要/The_Influence_of_Digital_Media_on_Children_and_Families.md
  - 09_來源摘要/Language_Development_and_Communication_Disorders.md
  - 09_來源摘要/Language_and_Speech_Disorders.md
- 新建主題頁 9：
  - 07_Pediatric_Development/兒童餵食與吞嚥障礙.md
  - 07_Pediatric_Development/寄養_收養與發展行為照護.md
  - 07_Pediatric_Development/嬰兒期發展.md
  - 07_Pediatric_Development/幼兒與學齡前期發展.md
  - 07_Pediatric_Development/學齡期發展.md
  - 07_Pediatric_Development/正向教養與家庭支持.md
  - 07_Pediatric_Development/創傷_復原力與兒童發展.md
  - 07_Pediatric_Development/數位媒體與兒少發展.md
  - 07_Pediatric_Development/兒童語言發展與Communication_Disorders.md
- 既有頁更新：
  - 03_疾病與臨床主題/吞嚥障礙復健總論.md
  - 07_Pediatric_Development/小兒復健評估.md
  - 07_Pediatric_Development/托育與Early_Care_and_Education.md
  - 07_Pediatric_Development/早期語言發展與Emergent_Literacy.md
  - 07_Pediatric_Development/晚語兒_Late_Talker.md
  - 07_Pediatric_Development/發展監測與篩檢.md
- 明確標示的 conflict / caveat：
  1. feeding disorder 與 dysphagia 不能混用；thickened liquid / IDDSI 不是 physiologic diagnosis。
  2. foster / adoption status 本身不決定 prognosis；postplacement dysregulation 不應直接當 oppositionality。
  3. infancy、preschool、school age 都有各自 stage-specific function；不能只用 milestone 或成績單概括。
  4. discipline 不等於 punishment；parenting advice 若忽略 temperament 與 family context，通常失真。
  5. ACE score 是 risk signal，不是完整 trauma formulation；resilience 也不是孩子單獨扛住的意思。
  6. screen media 不能只看 minutes；content、context、parent mediation 與 displaced activity 同樣重要。
  7. bilingual exposure、`boys talk later`、otitis media 都不是延後 language evaluation 的充分理由。
- index.md 更新：Total pages 189 -> 208
- Pending files（下一批待處理）：
  - Feeding and Swallowing Disorders 之後可承接：Neurodevelopmental and Executive Function and Dysfunction
  - Sensory Processing Disorders
  - Sleep and Sleep Disorders in Children
  - Intellectual Disability
  - The Influence of Digital Media on Children and Families 相關延伸：How-Early-Experiences-Shape-the-Development-of-Executive-Function

## [2026-04-24] lint | 全知識百科 health check（post-batch-16）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 208
  - orphan 0
  - weak links 0
  - broken links 0
  - missing_from_index 0
  - contradiction candidates 0
  - raw_backlog: 90
  - raw verification queue:
    1. Foot biomechanics/Foot biomechanics.md
    2. GaesserandPoole_ESSR1996_Theslowcomponentofoxygenuptakekineticsinhumans/GaesserandPoole_ESSR1996_Theslowcomponentofoxygenuptakekineticsinhumans.md
    3. Hamstring muscle and tendon injuries - UpToDate.md
    4. Hip, Pelvis, and Thigh Injuries in Runners/Hip, Pelvis, and Thigh Injuries in Runners.md
    5. Iliotibial band syndrome - UpToDate.md

## [2026-04-24] update | raw-source path normalization（Gaesser_Poole_1996_VO2_slow_component）
- 更新檔案：
  - 09_來源摘要/Gaesser_Poole_1996_VO2_slow_component.md
- 調整內容：
  - 將 `原始檔` 從相對樣式 `原始資料/...` 改為完整 Windows path `C:\原始資料\...`
  - 目的：讓 wiki_health_check.py 的 explicit raw-source matching 正常辨識已整理來源，消除 false positive backlog

## [2026-04-24] ingest | foot biomechanics / runner hip-thigh pain / hamstring / ITBS（Batch 17）
- Batch: 17
- Phase 3 raw verification queue resolved 5/5：
  1. Foot biomechanics/Foot biomechanics.md
  2. GaesserandPoole_ESSR1996_Theslowcomponentofoxygenuptakekineticsinhumans/GaesserandPoole_ESSR1996_Theslowcomponentofoxygenuptakekineticsinhumans.md
  3. Hamstring muscle and tendon injuries - UpToDate.md
  4. Hip, Pelvis, and Thigh Injuries in Runners/Hip, Pelvis, and Thigh Injuries in Runners.md
  5. Iliotibial band syndrome - UpToDate.md
- 驗證結果：
  - 1 件為既有 summary 的 raw-path false positive：Gaesser_Poole_1996_VO2_slow_component
  - 4 件確認為高價值 Tier 1 backlog，正式 ingest
- 類型與層級：
  - Foot biomechanics：textbook chapter，Tier 1，可信度 high
  - Hamstring muscle and tendon injuries：UpToDate，Tier 1，可信度 high
  - Hip, Pelvis, and Thigh Injuries in Runners：textbook chapter，Tier 1，可信度 high
  - Iliotibial band syndrome：UpToDate，Tier 1，可信度 high
- 新建來源摘要頁 4：
  - 09_來源摘要/Foot_biomechanics.md
  - 09_來源摘要/Hamstring_muscle_and_tendon_injuries.md
  - 09_來源摘要/Hip_Pelvis_and_Thigh_Injuries_in_Runners.md
  - 09_來源摘要/Iliotibial_band_syndrome.md
- 新建主題頁 3：
  - 03_疾病與臨床主題/Hamstring_肌肉與肌腱傷害.md
  - 03_疾病與臨床主題/Iliotibial_Band_Syndrome.md
  - 03_疾病與臨床主題/跑者髖骨盆與大腿疼痛.md
- 既有頁更新：
  - 06_Gait_Biomechanics/足部解剖與生物力學.md
  - 06_Gait_Biomechanics/步態評估總論.md
  - 03_疾病與臨床主題/跑者運動性下腿痛.md
- 明確標示的 conflict / caveat：
  1. foot biomechanics 的 midtarsal locking 與 rigid-lever 敘事都屬過度簡化；實際是 multisegment stiffening 與 foot spring。
  2. hamstring imaging classification 與 return-to-sport timing 不能直接畫等號。
  3. chronic proximal hamstring pain 不能與 acute sprint strain 混成同一種 injury path。
  4. runner hip / pelvis / thigh pain 的 pain location 不可靠，必須保留 bone stress injury 與 referred pain differential。
  5. GTPS 不應預設等同 isolated bursitis；多數更接近 gluteal tendon disorder。
  6. ITBS 不應再只用 friction theory 理解；imaging 也不是典型個案的 routine first-line confirmation。
- index.md 更新：Total pages 208 -> 215

## [2026-04-24] lint | 全知識百科 health check（post-batch-17）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python C:\知識百科\08_工具與Workflow\tests\test_wiki_health_check.py` → 6 tests passed
  - `python C:\知識百科\08_工具與Workflow\wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 215
  - orphan 0
  - weak links 0
  - broken links 0
  - missing_from_index 0
  - contradiction candidates 0
  - raw_backlog: 85
  - raw verification queue:
    1. Influence of Step Rate on Running Mechanics/Influence of Step Rate on Running Mechanics.md
    2. Intellectual Disability/Intellectual Disability.md
    3. Intellectual disability (ID) in children_ Clinical features, evaluation, and diagnosis.md
    4. Intellectual disability (ID) in children_ Evaluation for a cause.md
    5. Intellectual disability (ID) in children_ Management, outcomes, and prevention.md

## [2026-04-24] ingest | step rate / intellectual disability（Batch 18）
- Batch: 18
- Phase 3 raw verification queue resolved 5/5：
  1. Influence of Step Rate on Running Mechanics/Influence of Step Rate on Running Mechanics.md
  2. Intellectual Disability/Intellectual Disability.md
  3. Intellectual disability (ID) in children_ Clinical features, evaluation, and diagnosis.md
  4. Intellectual disability (ID) in children_ Evaluation for a cause.md
  5. Intellectual disability (ID) in children_ Management, outcomes, and prevention.md
- 類型與層級：
  - Influence of Step Rate on Running Mechanics：textbook chapter，Tier 1，可信度 high
  - Intellectual Disability：textbook chapter，Tier 1，可信度 high
  - Intellectual disability (ID) in children_ Clinical features, evaluation, and diagnosis：UpToDate，Tier 1，可信度 high
  - Intellectual disability (ID) in children_ Evaluation for a cause：UpToDate，Tier 1，可信度 high
  - Intellectual disability (ID) in children_ Management, outcomes, and prevention：UpToDate，Tier 1，可信度 high
- 新建來源摘要頁 5：
  - 09_來源摘要/Influence_of_Step_Rate_on_Running_Mechanics.md
  - 09_來源摘要/Intellectual_Disability.md
  - 09_來源摘要/Intellectual_disability_ID_in_children_Clinical_features_evaluation_and_diagnosis.md
  - 09_來源摘要/Intellectual_disability_ID_in_children_Evaluation_for_a_cause.md
  - 09_來源摘要/Intellectual_disability_ID_in_children_Management_outcomes_and_prevention.md
- 新建主題頁 1：
  - 06_Gait_Biomechanics/跑步步頻調整.md
- 既有頁更新：
  - 07_Pediatric_Development/發展遲緩與Intellectual_Disability.md
  - 07_Pediatric_Development/發展監測與篩檢.md
  - 07_Pediatric_Development/小兒復健評估.md
  - 07_Pediatric_Development/兒童神經學評估.md
  - 06_Gait_Biomechanics/步態評估總論.md
  - 03_疾病與臨床主題/Iliotibial_Band_Syndrome.md
  - 03_疾病與臨床主題/跑者運動性下腿痛.md
  - 03_疾病與臨床主題/跑者髖骨盆與大腿疼痛.md
- 明確標示的 conflict / caveat：
  1. step rate modification 應相對於個人 preferred cadence 設定，不存在 universal `180 spm` target。
  2. cadence retraining 只有在 speed 固定時，才真正對 stride mechanics 與 loading 產生預期改變。
  3. 步數增加不等於 cumulative knee load 一定增加；在 selected runner 反而可能下降。
  4. ID 不可只靠 IQ 診斷與分級；adaptive function 與 support need 才是核心。
  5. GDD 是 <5 歲 provisional developmental description，不能直接等同 permanent ID。
  6. regression 不是 stable ID 的自然病程；出現時要擴大 etiologic differential。
  7. unexplained ID 的病因評估不該停在 routine exam；要保留 phenotype-guided targeted testing 與 broad genetic testing。
  8. medication 不應取代 behavioral / environmental intervention 作為 challenging behavior 的預設第一步。
- index.md 更新：Total pages 215 -> 221

## [2026-04-24] lint | 全知識百科 health check（post-batch-18）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python C:\知識百科\08_工具與Workflow\tests\test_wiki_health_check.py` → 6 tests passed
  - `python C:\知識百科\08_工具與Workflow\wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 221
  - orphan 0
  - weak links 0
  - broken links 0
  - missing_from_index 0
  - contradiction candidates 0
  - raw_backlog: 80
  - oversized pages:
    1. 07_Pediatric_Development/發展遲緩與Intellectual_Disability.md
    2. 08_工具與Workflow/知識百科_健康檢查流程.md
    3. 06_Gait_Biomechanics/步態評估總論.md
    4. 07_Pediatric_Development/小兒復健評估.md
    5. 04_CPET/Critical_Power.md
  - raw verification queue:
    1. Knee Injuries in Runners/Knee Injuries in Runners.md
    2. Neurodevelopmental and Executive Function and Dysfunction/Neurodevelopmental and Executive Function and Dysfunction.md
    3. Patellofemoral pain - UpToDate.md
    4. Physiological model of CO2 output during incremental exercise/Physiological model of CO2 output during incremental exercise.md
    5. Polarized vs. Other Training Intensity Distribution Regimens and Endurance Performance/Polarized vs. Other Training Intensity Distribution Regimens and Endurance Performance.md

## [2026-04-24] ingest | runner knee / running gait assessment / executive function / pediatric sleep（Batch 19）
- Batch: 19
- Selected files（本回合實際讀取 5/5）：
  1. Patellofemoral pain - UpToDate.md
  2. Knee Injuries in Runners/Knee Injuries in Runners.md
  3. Running Gait Assessment/Running Gait Assessment.md
  4. Neurodevelopmental and Executive Function and Dysfunction/Neurodevelopmental and Executive Function and Dysfunction.md
  5. Sleep and Sleep Disorders in Children/Sleep and Sleep Disorders in Children.md
- 類型與層級：
  - Patellofemoral pain：UpToDate，Tier 1，可信度 high
  - Knee Injuries in Runners：textbook chapter，Tier 1，可信度 high
  - Running Gait Assessment：textbook chapter，Tier 1，可信度 high
  - Neurodevelopmental and Executive Function and Dysfunction：textbook chapter，Tier 1，可信度 high
  - Sleep and Sleep Disorders in Children：textbook chapter，Tier 1，可信度 high
- 新建來源摘要頁 5：
  - 09_來源摘要/Patellofemoral_pain.md
  - 09_來源摘要/Knee_Injuries_in_Runners.md
  - 09_來源摘要/Running_Gait_Assessment.md
  - 09_來源摘要/Neurodevelopmental_and_Executive_Function_and_Dysfunction.md
  - 09_來源摘要/Sleep_and_Sleep_Disorders_in_Children.md
- 新建主題頁 5：
  - 03_疾病與臨床主題/Patellofemoral_Pain.md
  - 03_疾病與臨床主題/跑者膝部疼痛.md
  - 06_Gait_Biomechanics/跑步步態評估.md
  - 07_Pediatric_Development/Executive_Function_總論.md
  - 07_Pediatric_Development/兒童睡眠與睡眠障礙總論.md
- 既有頁更新：
  - 06_Gait_Biomechanics/步態評估總論.md
  - 06_Gait_Biomechanics/跑步步頻調整.md
  - 03_疾病與臨床主題/跑者運動性下腿痛.md
  - 03_疾病與臨床主題/跑者髖骨盆與大腿疼痛.md
  - 07_Pediatric_Development/ADHD_睡眠與常見共病.md
  - 07_Pediatric_Development/幼兒與學齡前期發展.md
  - 07_Pediatric_Development/學齡期發展.md
  - 07_Pediatric_Development/小兒復健評估.md
  - 07_Pediatric_Development/發展監測與篩檢.md
- 明確標示的 conflict / caveat：
  1. PFP 是 diagnosis of exclusion；Q angle 與 patellar grind test 不應主導診斷與 treatment。
  2. runner knee pain 應先做 region-based differential；過用 special test 與 routine imaging 都會失焦。
  3. running gait analysis 應放在完整 runner evaluation 最後；不存在 universal ideal running form。
  4. cadence / foot strike / cue selection 都必須放在固定速度與症狀情境下解讀。
  5. EF 是 neurodevelopmental function，不可直接等同 ADHD。
  6. medication 可能處理部分 attention-related symptom，但不能當成完整 EF intervention。
  7. pediatric sleep problem 需先做完整 sleep history；teen delayed sleep 不應被當成無害常態。
  8. PSG 與 melatonin 都有明確角色邊界，不能拿來處理所有 pediatric sleep complaint。
- index.md 更新：Total pages 221 -> 231

## [2026-04-24] lint | 全知識百科 health check（post-batch-19）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python C:\知識百科\08_工具與Workflow\tests\test_wiki_health_check.py` → 6 tests passed
  - `python C:\知識百科\08_工具與Workflow\wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 231
  - orphan 0
  - weak links 0
  - broken links 0
  - missing_from_index 0
  - contradiction candidates 0
  - raw_backlog: 75
  - oversized pages:
    1. 07_Pediatric_Development/發展遲緩與Intellectual_Disability.md
    2. 08_工具與Workflow/知識百科_健康檢查流程.md
    3. 07_Pediatric_Development/小兒復健評估.md
    4. 06_Gait_Biomechanics/步態評估總論.md
    5. 04_CPET/Critical_Power.md
  - raw verification queue:
    1. Physiological model of CO2 output during incremental exercise/Physiological model of CO2 output during incremental exercise.md
    2. Polarized vs. Other Training Intensity Distribution Regimens and Endurance Performance/Polarized vs. Other Training Intensity Distribution Regimens and Endurance Performance.md
    3. Quadriceps muscle and tendon injuries - UpToDate.md
    4. Rehabilitation Principles of the Injured Runner/Rehabilitation Principles of the Injured Runner.md
    5. Running injuries of the lower extremities in adults_ Patient evaluation and common conditions - UpToDate.md

## [2026-04-24] ingest | injured runner evaluation / rehabilitation / quadriceps / CO2 model（Batch 20）
- Batch: 20
- Selected files（本回合實際讀取 5/5）：
  1. Rehabilitation Principles of the Injured Runner/Rehabilitation Principles of the Injured Runner.md
  2. Running injuries of the lower extremities in adults_ Patient evaluation and common conditions - UpToDate.md
  3. Quadriceps muscle and tendon injuries - UpToDate.md
  4. Physiological model of CO2 output during incremental exercise/Physiological model of CO2 output during incremental exercise.md
  5. Polarized vs. Other Training Intensity Distribution Regimens and Endurance Performance/Polarized vs. Other Training Intensity Distribution Regimens and Endurance Performance.md
- 類型與層級：
  - Rehabilitation Principles of the Injured Runner：textbook chapter，Tier 1，可信度 high
  - Running injuries of the lower extremities in adults: Patient evaluation and common conditions：UpToDate，Tier 1，可信度 high
  - Quadriceps muscle and tendon injuries：UpToDate，Tier 1，可信度 high
  - Physiological model of CO2 output during incremental exercise：original article，Tier 3，可信度 medium
  - Polarized vs. Other Training Intensity Distribution Regimens and Endurance Performance：已存在來源摘要；本回合完成 raw path normalization，移除 raw backlog false positive
- 新建來源摘要頁 4：
  - 09_來源摘要/Rehabilitation_Principles_of_the_Injured_Runner.md
  - 09_來源摘要/Running_injuries_of_the_lower_extremities_in_adults_Patient_evaluation_and_common_conditions.md
  - 09_來源摘要/Quadriceps_muscle_and_tendon_injuries.md
  - 09_來源摘要/Physiological_model_of_CO2_output_during_incremental_exercise.md
- 新建主題頁 3：
  - 03_疾病與臨床主題/受傷跑者復健原則.md
  - 03_疾病與臨床主題/跑者下肢傷害評估總論.md
  - 03_疾病與臨床主題/Quadriceps_肌肉與肌腱傷害.md
- 既有頁更新：
  - 03_疾病與臨床主題/Patellofemoral_Pain.md
  - 03_疾病與臨床主題/跑者膝部疼痛.md
  - 03_疾病與臨床主題/跑者運動性下腿痛.md
  - 03_疾病與臨床主題/跑者髖骨盆與大腿疼痛.md
  - 06_Gait_Biomechanics/跑步步態評估.md
  - 06_Gait_Biomechanics/跑步步頻調整.md
  - 04_CPET/V_Slope_Method.md
  - 04_CPET/Gas_Exchange_Threshold.md
  - 09_來源摘要/Oliveira_2024_polarized_training_meta_analysis.md
- 明確標示的 conflict / caveat：
  1. injured runner rehab 不應簡化成 pain-free rest；capacity restoration 與 load redistribution 需並行。
  2. gait retraining 是工具，不是萬用替代；cadence、10% rule、ACWR 都應降階為 heuristic。
  3. injured runner evaluation 應從 history、whole-chain exam 與 selective imaging 出發，而不是 routine MRI。
  4. quadriceps complaint 需分 strain、contusion、tendinopathy 與 extensor mechanism failure；complete rupture 為 referral problem。
  5. Yano 1997 屬 historical Tier 3 mechanistic model，可補充 GET / V-slope 理解，但不取代既有主框架。
  6. Oliveira 2024 本輪未新增結論，只修正來源摘要 raw path，排除 false positive backlog。
- index.md 更新：Total pages 231 -> 238

## [2026-04-24] lint | 全知識百科 health check（post-batch-20）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python C:\知識百科\08_工具與Workflow\tests\test_wiki_health_check.py` → 6 tests passed
  - `python C:\知識百科\08_工具與Workflow\wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 238
  - orphan 0
  - weak links 0
  - broken links 0
  - missing_from_index 0
  - contradiction candidates 0
  - raw_backlog: 70
  - oversized pages:
    1. 07_Pediatric_Development/發展遲緩與Intellectual_Disability.md
    2. 08_工具與Workflow/知識百科_健康檢查流程.md
    3. 07_Pediatric_Development/小兒復健評估.md
    4. 06_Gait_Biomechanics/步態評估總論.md
    5. 04_CPET/Critical_Power.md
  - raw verification queue:
    1. Running injuries of the lower extremities in adults_ Risk factors and prevention - UpToDate.md
    2. Sensory Processing Disorders/Sensory Processing Disorders.md
    3. Speech and language impairment in children_ Etiology - UpToDate.md
    4. Speech and language impairment in children_ Evaluation, treatment, and prognosis - UpToDate.md
    5. Sreedhara et al. Sports Medicine- Open/Sreedhara et al. Sports Medicine- Open.md

## [2026-04-25] ingest | pediatric speech / sensory processing / executive function / developmental report workflow（Batch 21）
- Batch: 21
- Selected files（10/10）：
  1. Sensory Processing Disorders
  2. Speech and language impairment in children: Etiology
  3. Speech and language impairment in children: Evaluation, treatment, and prognosis
  4. Cognitive Control
  5. Smart but Scattered
  6. How Early Experiences Shape the Development of Executive Function
  7. Enhancing and Practicing Executive Function Skills with Children from Infancy to Adolescence
  8. HCDC Building Adolescent Core Life Skills
  9. 教孩子跟情緒做朋友
  10. 兒童發展聯合評估綜合報告書操作手冊（111年7月版）
- 類型 / 層級 / 可信度：
  - Sensory Processing Disorders：textbook chapter，Tier 1，可信度 medium
  - Speech and language impairment in children: Etiology：UpToDate，Tier 1，可信度 high
  - Speech and language impairment in children: Evaluation, treatment, and prognosis：UpToDate，Tier 1，可信度 high
  - Cognitive Control：review article，Tier 1，可信度 high
  - Smart but Scattered：科普書，Tier 2，可信度 medium
  - How Early Experiences Shape the Development of Executive Function：網站資料，Tier 2，可信度 medium
  - Enhancing and Practicing Executive Function Skills with Children from Infancy to Adolescence：網站資料，Tier 2，可信度 medium
  - HCDC Building Adolescent Core Life Skills：網站資料，Tier 2，可信度 medium
  - 教孩子跟情緒做朋友：科普書，Tier 2，可信度 medium
  - 兒童發展聯合評估綜合報告書操作手冊（111年7月版）：官方手冊 / 網站資料，Tier 2，可信度 medium
- 新建來源摘要頁 10：
  - 09_來源摘要/Sensory_Processing_Disorders.md
  - 09_來源摘要/Speech_and_language_impairment_in_children_Etiology.md
  - 09_來源摘要/Speech_and_language_impairment_in_children_Evaluation_treatment_and_prognosis.md
  - 09_來源摘要/Cognitive_Control.md
  - 09_來源摘要/Smart_but_Scattered.md
  - 09_來源摘要/How_Early_Experiences_Shape_the_Development_of_Executive_Function.md
  - 09_來源摘要/Enhancing_and_Practicing_Executive_Function_Skills_with_Children_from_Infancy_to_Adolescence.md
  - 09_來源摘要/HCDC_BuildingAdolescentCoreLifeSkills.md
  - 09_來源摘要/教孩子跟情緒做朋友.md
  - 09_來源摘要/兒童發展聯合評估綜合報告書操作手冊_111年7月版.md
- 新建主題 / workflow 頁 3：
  - 07_Pediatric_Development/兒童感覺處理問題與SPD.md
  - 07_Pediatric_Development/Executive_Function_支持策略.md
  - 08_工具與Workflow/兒童發展聯評綜合報告骨架.md
- 更新既有頁面：
  - 07_Pediatric_Development/兒童語言發展與Communication_Disorders.md
  - 07_Pediatric_Development/晚語兒_Late_Talker.md
  - 07_Pediatric_Development/發展監測與篩檢.md
  - 07_Pediatric_Development/小兒復健評估.md
  - 07_Pediatric_Development/Executive_Function_總論.md
  - 07_Pediatric_Development/正向教養與家庭支持.md
  - index.md
  - log.md
- 明確標示的 conflict / caveat：
  1. speech / language impairment 是 presentation，不是單一 diagnosis；formal audiology 不能省。
  2. bilingual exposure 不可當延後評估理由；dominant-language assessment 很重要。
  3. SPD 的 participation framing 可用，但不能把所有 behavior / language complaint 都當 sensory problem。
  4. sensory-based intervention 證據有條件，不能外推成所有 neurodevelopmental complaint 的標準主軸。
  5. EF 與 cognitive control 相關但不完全同義；practical scaffolding 不能取代 formal evaluation。
  6. Smart but Scattered / 教孩子跟情緒做朋友 屬 caregiver-facing Tier 2 資料，可補教學與 coaching，不可當成 consensus treatment guideline。
  7. 聯評 manual 是 reporting / coordination framework，不等於 diagnostic truth 或 treatment efficacy evidence。
- index.md 更新：Total pages 238 -> 251
- 下一批待處理：
  - Running injuries of the lower extremities in adults_ Risk factors and prevention - UpToDate.md
  - Sreedhara et al. Sports Medicine- Open/Sreedhara et al. Sports Medicine- Open.md
  - HCDC_BuildingCoreLifeSkills/HCDC_BuildingCoreLifeSkills.md

## [2026-04-25] ingest | running injury prevention / OA / footwear / W'BAL（Batch 22）
- Batch: 22
- Selected files（10/10）：
  1. Running injuries of the lower extremities in adults: Risk factors and prevention
  2. A Survey of Mathematical Models of Human Performance Using Power and Energy
  3. Accuracy of W' Recovery Kinetics in High Performance Cyclists – Modelling Intermittent Work Capacity
  4. Osteoarthritis and Running
  5. Ankle and Foot Injuries in Runners
  6. Shoes and Shoe Modifications
  7. The Interaction of Foot Strike and Footwear in Runners
  8. The W' Balance Model: Mathematical and Methodological Considerations
  9. Modeling the Recovery of W' in the Moderate to Heavy Exercise Intensity Domain
  10. Time Trials versus Time to Exhaustion Tests: Effects on Critical Power, W' and Oxygen Uptake Kinetics
- 類型 / 層級 / 可信度：
  - Running injuries of the lower extremities in adults: Risk factors and prevention：UpToDate，Tier 1，可信度 high
  - A Survey of Mathematical Models of Human Performance Using Power and Energy：review article，Tier 1，可信度 high
  - Accuracy of W' Recovery Kinetics in High Performance Cyclists – Modelling Intermittent Work Capacity：original article，Tier 3，可信度 medium
  - Osteoarthritis and Running：textbook chapter，Tier 1，可信度 high
  - Ankle and Foot Injuries in Runners：textbook chapter，Tier 1，可信度 high
  - Shoes and Shoe Modifications：textbook chapter，Tier 1，可信度 high
  - The Interaction of Foot Strike and Footwear in Runners：textbook chapter / focused review，Tier 1，可信度 medium
  - The W' Balance Model: Mathematical and Methodological Considerations：review article，Tier 1，可信度 high
  - Modeling the Recovery of W' in the Moderate to Heavy Exercise Intensity Domain：original article，Tier 3，可信度 medium
  - Time Trials versus Time to Exhaustion Tests: Effects on Critical Power, W' and Oxygen Uptake Kinetics：original article，Tier 3，可信度 medium
- duplicate / raw-path housekeeping 2：
  - 09_來源摘要/Goulding_2021_VO2_kinetics_exercise_tolerance.md：將原始檔正規化為 `C:\原始資料\Bioenergetic Mechanisms Linking V̇O2 Kinetics and Exercise Tolerance\...`
  - 09_來源摘要/Jones_Vanhatalo_2017_critical_power_concept.md：保留 `The Critical Power Concept` raw path，並新增 duplicate raw source `C:\原始資料\CP in HIIT\CP in HIIT.md`
- 新建來源摘要頁 10：
  - 09_來源摘要/Running_injuries_of_the_lower_extremities_in_adults_Risk_factors_and_prevention.md
  - 09_來源摘要/Sreedhara_2019_power_energy_models.md
  - 09_來源摘要/Bartram_2018_Wprime_recovery_elite_cyclists.md
  - 09_來源摘要/Osteoarthritis_and_Running.md
  - 09_來源摘要/Ankle_and_Foot_Injuries_in_Runners.md
  - 09_來源摘要/Shoes_and_shoe_modifications.md
  - 09_來源摘要/The_Interaction_of_Foot_Strike_and_Footwear_in_Runners.md
  - 09_來源摘要/Skiba_Clarke_Wprime_balance_model.md
  - 09_來源摘要/Sreedhara_2020_Modeling_Wprime_Recovery.md
  - 09_來源摘要/Karsten_2017_TT_vs_TTE_CP_Wprime.md
- 新建主題頁 4：
  - 03_疾病與臨床主題/跑步傷害風險因子與預防.md
  - 03_疾病與臨床主題/跑步與Osteoarthritis.md
  - 04_CPET/Wprime_Balance_Model.md
  - 06_Gait_Biomechanics/治療性鞋具與鞋修改.md
- 既有頁更新：
  - 03_疾病與臨床主題/跑者下肢傷害評估總論.md
  - 03_疾病與臨床主題/受傷跑者復健原則.md
  - 03_疾病與臨床主題/足部疼痛分區評估.md
  - 06_Gait_Biomechanics/跑鞋選擇原則.md
  - 06_Gait_Biomechanics/跑步步態評估.md
  - 06_Gait_Biomechanics/步態評估總論.md
  - 06_Gait_Biomechanics/下肢矯具總論.md
  - 04_CPET/Critical_Power.md
  - 04_CPET/Training_Prescription_by_CP.md
  - 04_CPET/CP_Test_Reliability.md
  - 04_CPET/VO2_Kinetics.md
  - 04_CPET/VO2_Slow_Component.md
  - index.md
  - log.md
- 明確標示的 conflict / caveat：
  1. shoe-by-foot-type matching、10% rule、isolated stretching 與 routine foot-strike change 都不能當成 injury-prevention default。
  2. moderate-dose running 不應被直接等同 hip / knee OA 惡化；真正要先看的是 prior injury、obesity、symptom response 與 running dose。
  3. FFS / minimal footwear 可作 selected load-redistribution tool，但 transition 過快時會把負荷轉向 Achilles、calf、plantar 與 metatarsals。
  4. therapeutic footwear 重點是 fit、last、volume 與 condition-specific modification；extra-depth / custom molded 不是所有 foot complaint 的預設答案。
  5. W'BAL 是 assumption-sensitive model，不是直接量到的 physiologic tank；integral / differential / athlete-specific forms 不能混用。
  6. elite cyclists 與 competitive cyclists 的 W' recovery 研究方向一致指出：group-derived tau 不應被當成 universal physiology，但 individual equation 也不能直接外推。
  7. TT-derived CP 可接近 TTE-derived CP，但 W' 不可直接當成可互換輸出。
- index.md 更新：Total pages 251 -> 265
- 下一批待處理：
  - Chidnoketal.AJP2013/Chidnoketal.AJP2013.md
  - Exercise/Exercise.md
  - HCDC_BuildingCoreLifeSkills/HCDC_BuildingCoreLifeSkills.md

## [2026-04-25] lint | 全知識百科 health check（post-batch-22）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python C:\知識百科\08_工具與Workflow\wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 265
  - orphan 0
  - weak links 0
  - broken links 0
  - missing_from_index 0
  - stale candidates 0
  - contradiction candidates 0
  - raw_backlog: 44
  - raw verification queue:
    1. Chidnoketal.AJP2013/Chidnoketal.AJP2013.md
    2. Exercise/Exercise.md
    3. HCDC_BuildingCoreLifeSkills/HCDC_BuildingCoreLifeSkills.md
    4. HargreavesSpriet-2020-Nature_Metabolism/HargreavesSpriet-2020-Nature_Metabolism.md
    5. Journal of Sports Medicine - 2016 - Beltz - Graded Exercise Testing Protocols for the Determination of VO2max  Historical (1)/Journal of Sports Medicine - 2016 - Beltz - Graded Exercise Testing Protocols for the Determination of VO2max  Historical (1).md

## [2026-04-25] ingest | CP intermittent metabolism / exercise physiology overview / adult core life skills（Batch 23）
- Batch: 23
- Candidate ranking（承接 post-batch-22 raw verification queue，依來源優先級 + 主題相關性 + backlog impact 排序）：
  1. Exercise/Exercise.md
  2. HargreavesSpriet-2020-Nature_Metabolism/HargreavesSpriet-2020-Nature_Metabolism.md
  3. Journal of Sports Medicine - 2016 - Beltz - Graded Exercise Testing Protocols for the Determination of VO2max  Historical (1)/Journal of Sports Medicine - 2016 - Beltz - Graded Exercise Testing Protocols for the Determination of VO2max  Historical (1).md
  4. Chidnoketal.AJP2013/Chidnoketal.AJP2013.md
  5. HCDC_BuildingCoreLifeSkills/HCDC_BuildingCoreLifeSkills.md
- Selected files（本回合實際讀取 5/5）：
  1. Exercise/Exercise.md
  2. HargreavesSpriet-2020-Nature_Metabolism/HargreavesSpriet-2020-Nature_Metabolism.md
  3. Journal of Sports Medicine - 2016 - Beltz - Graded Exercise Testing Protocols for the Determination of VO2max  Historical (1)/Journal of Sports Medicine - 2016 - Beltz - Graded Exercise Testing Protocols for the Determination of VO2max  Historical (1).md
  4. Chidnoketal.AJP2013/Chidnoketal.AJP2013.md
  5. HCDC_BuildingCoreLifeSkills/HCDC_BuildingCoreLifeSkills.md
- 類型 / 層級 / 可信度：
  - Exercise：textbook chapter，Tier 1，可信度 medium
  - HargreavesSpriet-2020-Nature_Metabolism：review article，Tier 1，可信度 high（duplicate/raw-path verification）
  - Beltz 2016 GXT protocols：review article，Tier 1，可信度 high（duplicate/raw-path verification）
  - Chidnok et al. 2013：original article，Tier 3，可信度 medium
  - HCDC Building the Skills Adults Need for Life：網站資料 / practitioner guide，Tier 2，可信度 medium
- 新建來源摘要頁 3：
  - 09_來源摘要/Exercise_textbook_chapter.md
  - 09_來源摘要/Chidnok_2013_intermittent_exercise_PCr_CP.md
  - 09_來源摘要/HCDC_BuildingCoreLifeSkills.md
- 新建主題頁 1：
  - 05_Exercise_Physiology/運動時氧輸送與換氣.md
- 既有頁更新：
  - 04_CPET/Wprime_Balance_Model.md
  - 04_CPET/Critical_Power.md
  - 04_CPET/Training_Prescription_by_CP.md
  - 02_方法學/復健心理社會評估與介入.md
  - 02_方法學/治療性運動處方.md
  - index.md
- duplicate / raw-path verification：
  - 09_來源摘要/Hargreaves_Spriet_2020_muscle_energy_metabolism.md：確認現有摘要已對應 `HargreavesSpriet-2020-Nature_Metabolism` raw file，本回合不新增結論。
  - 09_來源摘要/Beltz_2016_GXT_protocols.md：確認現有摘要已對應 Hindawi GXT review raw file，本回合不新增結論。
- 明確標示的 conflict / caveat：
  1. intermittent exercise 中的 `W'>CP` 可超過 constant-load `W'`；但這不代表 `W'` 等於單一 PCr tank。
  2. `Exercise` textbook chapter 的 `anaerobic threshold` / `oxygen debt` 屬 legacy teaching label，不取代現代 LT/GET/CP 框架。
  3. exercise limitation 不能被簡化成 lungs-only problem；oxygen delivery、extraction、ventilation 與 symptom perception 需一起看。
  4. adult follow-through failure 不能直接等同 low motivation；stress overload、self-regulatory burden 與 service friction 都可能是主因。
- index.md 更新：Total pages 265 -> 269
- 下一批待處理（暫列 health check queue；仍需下回合重新排序）：
  - La prediction from excess CO2/La prediction from excess CO2.md
  - README.md
  - The Journal of Physiology - 2020 - Poole - The anaerobic threshold  50  years of controversy/The Journal of Physiology - 2020 - Poole - The anaerobic threshold  50  years of controversy.md
  - blemker-et-al-2023-fiber-type-traps-revisiting-common-misconceptions-about-skeletal-muscle-fiber-types-with-application/blemker-et-al-2023-fiber-type-traps-revisiting-common-misconceptions-about-skeletal-muscle-fiber-types-with-application.md
  - bnaa016/bnaa016.md

## [2026-04-25] update | wiki_health_check raw path normalization
- 調整 08_工具與Workflow/wiki_health_check.py：
  - `normalize_raw_reference()` 現在除 absolute raw path 外，也接受既有 wiki 常用的 `原始資料/...` 相對寫法。
- 更新測試：08_工具與Workflow/tests/test_wiki_health_check.py
  - 新增 relative raw-path normalization case
  - 將 explicit raw-source backlog 測試改為模擬真實 `原始資料` 目錄名
- 影響：
  - Hargreaves / Beltz 等既有來源摘要不再被誤判為 raw backlog
  - 後續 health check 對舊頁面 raw-path notation 的容忍度提高

## [2026-04-25] lint | 全知識百科 health check（post-batch-23）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python C:\知識百科\08_工具與Workflow\tests\test_wiki_health_check.py` → 6 tests passed
  - `python C:\知識百科\08_工具與Workflow\wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 269
  - orphan 0
  - weak links 0
  - broken links 0
  - missing_from_index 0
  - stale candidates 0
  - contradiction candidates 0
  - raw_backlog: 36（44 -> 36）
  - raw verification queue:
    1. La prediction from excess CO2/La prediction from excess CO2.md
    2. README.md
    3. The Journal of Physiology - 2020 - Poole - The anaerobic threshold  50  years of controversy/The Journal of Physiology - 2020 - Poole - The anaerobic threshold  50  years of controversy.md
    4. blemker-et-al-2023-fiber-type-traps-revisiting-common-misconceptions-about-skeletal-muscle-fiber-types-with-application/blemker-et-al-2023-fiber-type-traps-revisiting-common-misconceptions-about-skeletal-muscle-fiber-types-with-application.md
    5. bnaa016/bnaa016.md

## [2026-04-25] ingest | excess CO2 historical model / myokines muscle-organ crosstalk（Batch 24）
- Batch: 24
- 使用者要求：再處理 7 份；依 schema，本回合實際只讀取 5/5 raw files，其餘待下批。
- Candidate ranking（承接 post-batch-23 raw verification queue，依來源優先級 + 主題相關性 + backlog impact 排序）：
  1. La prediction from excess CO2/La prediction from excess CO2.md
  2. README.md
  3. The Journal of Physiology - 2020 - Poole - The anaerobic threshold  50  years of controversy/The Journal of Physiology - 2020 - Poole - The anaerobic threshold  50  years of controversy.md
  4. blemker-et-al-2023-fiber-type-traps-revisiting-common-misconceptions-about-skeletal-muscle-fiber-types-with-application/blemker-et-al-2023-fiber-type-traps-revisiting-common-misconceptions-about-skeletal-muscle-fiber-types-with-application.md
  5. bnaa016/bnaa016.md
- Selected files（本回合實際讀取 5/5）：
  1. La prediction from excess CO2/La prediction from excess CO2.md
  2. README.md
  3. The Journal of Physiology - 2020 - Poole - The anaerobic threshold  50  years of controversy/The Journal of Physiology - 2020 - Poole - The anaerobic threshold  50  years of controversy.md
  4. blemker-et-al-2023-fiber-type-traps-revisiting-common-misconceptions-about-skeletal-muscle-fiber-types-with-application/blemker-et-al-2023-fiber-type-traps-revisiting-common-misconceptions-about-skeletal-muscle-fiber-types-with-application.md
  5. bnaa016/bnaa016.md
- 類型 / 層級 / 可信度：
  - La prediction from excess CO2：original article，Tier 3，可信度 medium
  - README.md：raw-root instruction file，非醫學來源，不納入 ingest evidence
  - Poole 2020 controversy duplicate raw .md：review article，Tier 1，可信度 high（duplicate/raw-path verification）
  - Blemker 2023 fiber type traps duplicate raw .md：review article，Tier 1，可信度 high（duplicate/raw-path verification）
  - bnaa016：review article，Tier 1，可信度 high
- 新建來源摘要頁 2：
  - 09_來源摘要/Hirakoba_1996_excess_CO2_lactate_prediction.md
  - 09_來源摘要/Severinsen_Pedersen_2020_myokines_muscle_organ_crosstalk.md
- 新建主題頁 1：
  - 05_Exercise_Physiology/Myokines_與_Muscle_Organ_Crosstalk.md
- 既有頁更新：
  - 04_CPET/Gas_Exchange_Threshold.md
  - 04_CPET/V_Slope_Method.md
  - 05_Exercise_Physiology/Skeletal_Muscle_Energy_Metabolism.md
  - 02_方法學/治療性運動處方.md
  - 09_來源摘要/Poole_2020_anaerobic_threshold.md
  - 09_來源摘要/Blemker_2023_fiber_type_traps.md
  - index.md
- duplicate / raw-path verification：
  - Poole 2020 duplicate raw `.md` 已補登到既有來源摘要，不新增主結論。
  - Blemker 2023 duplicate raw `.md` 已用實際 raw path 取代縮寫占位寫法，不新增主結論。
- 明確標示的 conflict / caveat：
  1. excess CO2 可作歷史性 lactate-buffering 教學模型，但不取代現代 GET / LT operational framework。
  2. myokines 不是單一 magic molecule；IL-6 的 human evidence 最強，其餘多數仍屬 emerging / preclinical evidence。
  3. skeletal muscle 的 systemic effect 可作 rehab / exercise physiology 框架補充，但不能直接把單篇或單路徑外推成臨床共識。
- index.md 更新：Total pages 269 -> 272
- 下一批待處理（依 post-batch-24 health check queue 重新排序）：
  - bnaa024/bnaa024.md
  - ijspp-article-p1561 (1)/ijspp-article-p1561 (1).md
  - kinetics of excess VCO2/kinetics of excess VCO2.md
  - korzeniewski-zoladz-2013-slow-v̇o2-off-kinetics-in-skeletal-muscle-is-associated-with-fast-pcr-off-kinetics-and/korzeniewski-zoladz-2013-slow-v̇o2-off-kinetics-in-skeletal-muscle-is-associated-with-fast-pcr-off-kinetics-and.md
  - korzeniewski-zoladz-2015-possible-mechanisms-underlying-slow-component-of-v̇o2-on-kinetics-in-skeletal-muscle/korzeniewski-zoladz-2015-possible-mechanisms-underlying-slow-component-of-v̇o2-on-kinetics-in-skeletal-muscle.md

## [2026-04-25] update | raw backlog cleanup（README skip + duplicate raw-path registration）
- 調整 08_工具與Workflow/wiki_health_check.py：
  - raw-root `README.md` 視為資料夾說明檔，不列入 raw backlog。
- 更新測試：08_工具與Workflow/tests/test_wiki_health_check.py
  - 新增 raw-root `README.md` exclusion case。
- 來源摘要 raw-path cleanup：
  - 09_來源摘要/Poole_2020_anaerobic_threshold.md：補登 duplicate raw `.md` path。
  - 09_來源摘要/Blemker_2023_fiber_type_traps.md：改用實際 raw `.md` path。
- 影響：
  - raw backlog 不再把非來源 README 當候選。
  - duplicate raw files 改由既有來源摘要顯式吸收，減少重複 backlog。

## [2026-04-25] lint | 全知識百科 health check（post-batch-24）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python C:\知識百科\08_工具與Workflow\tests\test_wiki_health_check.py` → 6 tests passed
  - `python C:\知識百科\08_工具與Workflow\wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 272
  - orphan 0
  - weak links 0
  - broken links 0
  - missing_from_index 0
  - stale candidates 0
  - contradiction candidates 0
  - raw_backlog: 31（36 -> 31）
  - raw verification queue:
    1. bnaa024/bnaa024.md
    2. ijspp-article-p1561 (1)/ijspp-article-p1561 (1).md
    3. kinetics of excess VCO2/kinetics of excess VCO2.md
    4. korzeniewski-zoladz-2013-slow-v̇o2-off-kinetics-in-skeletal-muscle-is-associated-with-fast-pcr-off-kinetics-and/korzeniewski-zoladz-2013-slow-v̇o2-off-kinetics-in-skeletal-muscle-is-associated-with-fast-pcr-off-kinetics-and.md
    5. korzeniewski-zoladz-2015-possible-mechanisms-underlying-slow-component-of-v̇o2-on-kinetics-in-skeletal-muscle/korzeniewski-zoladz-2015-possible-mechanisms-underlying-slow-component-of-v̇o2-on-kinetics-in-skeletal-muscle.md

## [2026-04-25] ingest | W'BAL duplicate cleanup / excess CO2 kinetics / VO2-PCr recovery / VO2 slow component（Batch 25）
- Batch: 25
- 使用者要求：全部做完；依 schema，單一回合仍只可讀取 5 份 raw files，因此本回合實際讀取 5/5，剩餘 backlog 留待下批。
- Candidate ranking（承接 post-batch-24 raw verification queue，依來源優先級 + 主題相關性 + backlog impact 排序）：
  1. bnaa024/bnaa024.md
  2. ijspp-article-p1561 (1)/ijspp-article-p1561 (1).md
  3. kinetics of excess VCO2/kinetics of excess VCO2.md
  4. korzeniewski-zoladz-2013-slow-v̇o2-off-kinetics-in-skeletal-muscle-is-associated-with-fast-pcr-off-kinetics-and/korzeniewski-zoladz-2013-slow-v̇o2-off-kinetics-in-skeletal-muscle-is-associated-with-fast-pcr-off-kinetics-and.md
  5. korzeniewski-zoladz-2015-possible-mechanisms-underlying-slow-component-of-v̇o2-on-kinetics-in-skeletal-muscle/korzeniewski-zoladz-2015-possible-mechanisms-underlying-slow-component-of-v̇o2-on-kinetics-in-skeletal-muscle.md
- Selected files（本回合實際讀取 5/5）：
  1. bnaa024/bnaa024.md
  2. ijspp-article-p1561 (1)/ijspp-article-p1561 (1).md
  3. kinetics of excess VCO2/kinetics of excess VCO2.md
  4. korzeniewski-zoladz-2013-slow-v̇o2-off-kinetics-in-skeletal-muscle-is-associated-with-fast-pcr-off-kinetics-and/korzeniewski-zoladz-2013-slow-v̇o2-off-kinetics-in-skeletal-muscle-is-associated-with-fast-pcr-off-kinetics-and.md
  5. korzeniewski-zoladz-2015-possible-mechanisms-underlying-slow-component-of-v̇o2-on-kinetics-in-skeletal-muscle/korzeniewski-zoladz-2015-possible-mechanisms-underlying-slow-component-of-v̇o2-on-kinetics-in-skeletal-muscle.md
- 類型 / 層級 / 可信度：
  - bnaa024：corrigendum to review article，Tier 1，可信度 high
  - ijspp-article-p1561 (1)：review article duplicate raw .md，Tier 1，可信度 high
  - kinetics of excess VCO2：original article，Tier 3，可信度 medium
  - Korzeniewski & Zoladz 2013：original article / theoretical model，Tier 3，可信度 medium
  - Korzeniewski & Zoladz 2015：original article / theoretical model，Tier 3，可信度 medium
- 新建來源摘要頁 3：
  - 09_來源摘要/Yunoki_1999_excess_CO2_kinetics.md
  - 09_來源摘要/Korzeniewski_Zoladz_2013_VO2_off_PCr_off_kinetics.md
  - 09_來源摘要/Korzeniewski_Zoladz_2015_VO2_slow_component_mechanisms.md
- 既有頁更新：
  - 09_來源摘要/Severinsen_Pedersen_2020_myokines_muscle_organ_crosstalk.md
  - 05_Exercise_Physiology/Myokines_與_Muscle_Organ_Crosstalk.md
  - 09_來源摘要/Skiba_Clarke_Wprime_balance_model.md
  - 04_CPET/Gas_Exchange_Threshold.md
  - 04_CPET/V_Slope_Method.md
  - 04_CPET/Anaerobic_Threshold_概念史.md
  - 04_CPET/VO2_Kinetics.md
  - 04_CPET/VO2_Slow_Component.md
  - 05_Exercise_Physiology/PCr_Resynthesis.md
  - index.md
- duplicate / corrigendum handling：
  - bnaa024 未另建新頁，改併入 `Severinsen_Pedersen_2020_myokines_muscle_organ_crosstalk.md`，明記 corrigendum：IL-6 應為 inhibits appetite。
  - ijspp duplicate raw `.md` 已補登至 `Skiba_Clarke_Wprime_balance_model.md`，不新增主結論。
- 明確標示的 conflict / caveat：
  1. excess CO2 / excess VCO2 與 lactate 有關，但其 kinetics 可延後且受 CO2 stores / hyperventilation 影響，不能當成即時 lactate readout。
  2. VO2 off-kinetics 與 PCr recovery 不必然同步；理論模型顯示兩者可呈 inverse relation，因此 pulmonary recovery signal 不可直接當 muscle recovery 真值。
  3. VO2 slow component 不能被單一路徑解釋；glycolysis inhibition 與 rising ATP cost 是 limited-evidence mechanistic supplement，不取代 Tier 1 field consensus。
- index.md 更新：Total pages 272 -> 275
- 下一批待處理（依 post-batch-25 health check queue 重新排序）：
  - modeling_the_expenditure_and_reconstitution_of.15/modeling_the_expenditure_and_reconstitution_of.15.md
  - nihms-1917261/nihms-1917261.md
  - poole-jones-2017-measurement-of-the-maximum-oxygen-uptake-v̇o2max-v̇o2peak-is-no-longer-acceptable/poole-jones-2017-measurement-of-the-maximum-oxygen-uptake-v̇o2max-v̇o2peak-is-no-longer-acceptable.md
  - s00421-014-3050-3/s00421-014-3050-3.md
  - sports-07-00031-v2/sports-07-00031-v2.md

## [2026-04-25] lint | 全知識百科 health check（post-batch-25）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python C:\知識百科\08_工具與Workflow\tests\test_wiki_health_check.py` → 6 tests passed
  - `python C:\知識百科\08_工具與Workflow\wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 275
  - orphan 0
  - weak links 0
  - broken links 0
  - missing_from_index 0
  - stale candidates 0
  - contradiction candidates 0
  - raw_backlog: 26（31 -> 26）
  - raw verification queue:
    1. modeling_the_expenditure_and_reconstitution_of.15/modeling_the_expenditure_and_reconstitution_of.15.md
    2. nihms-1917261/nihms-1917261.md
    3. poole-jones-2017-measurement-of-the-maximum-oxygen-uptake-v̇o2max-v̇o2peak-is-no-longer-acceptable/poole-jones-2017-measurement-of-the-maximum-oxygen-uptake-v̇o2max-v̇o2peak-is-no-longer-acceptable.md
    4. s00421-014-3050-3/s00421-014-3050-3.md
    5. sports-07-00031-v2/sports-07-00031-v2.md

## [2026-04-25] ingest | VO2max verification / W'BAL origin / intramuscular W' recovery / VO2 kinetics tooling（Batch 26）
- Batch: 26
- heartbeat 指示：依 post-batch-25 health check queue 繼續整理；依 schema，單一回合最多只可讀取 5 份 raw files，因此本回合實際讀取 5/5。
- Candidate ranking（承接 post-batch-25 raw verification queue，依來源優先級 + 主題相關性 + backlog impact 排序）：
  1. modeling_the_expenditure_and_reconstitution_of.15/modeling_the_expenditure_and_reconstitution_of.15.md
  2. nihms-1917261/nihms-1917261.md
  3. poole-jones-2017-measurement-of-the-maximum-oxygen-uptake-v̇o2max-v̇o2peak-is-no-longer-acceptable/poole-jones-2017-measurement-of-the-maximum-oxygen-uptake-v̇o2max-v̇o2peak-is-no-longer-acceptable.md
  4. s00421-014-3050-3/s00421-014-3050-3.md
  5. sports-07-00031-v2/sports-07-00031-v2.md
- Selected files（本回合實際讀取 5/5）：
  1. modeling_the_expenditure_and_reconstitution_of.15/modeling_the_expenditure_and_reconstitution_of.15.md
  2. nihms-1917261/nihms-1917261.md
  3. poole-jones-2017-measurement-of-the-maximum-oxygen-uptake-v̇o2max-v̇o2peak-is-no-longer-acceptable/poole-jones-2017-measurement-of-the-maximum-oxygen-uptake-v̇o2max-v̇o2peak-is-no-longer-acceptable.md
  4. s00421-014-3050-3/s00421-014-3050-3.md
  5. sports-07-00031-v2/sports-07-00031-v2.md
- 類型 / 層級 / 可信度：
  - modeling_the_expenditure_and_reconstitution_of.15：original article，Tier 3，可信度 medium
  - nihms-1917261：pilot original article，Tier 3，可信度 medium
  - poole-jones-2017-measurement-of-the-maximum-oxygen-uptake-v̇o2max-v̇o2peak-is-no-longer-acceptable：review article，Tier 1，可信度 high
  - s00421-014-3050-3：original article，Tier 3，可信度 medium
  - sports-07-00031-v2：methods / software original article，Tier 3，可信度 medium
- 新建來源摘要頁 5：
  - 09_來源摘要/Skiba_2012_modeling_Wprime_expenditure_reconstitution.md
  - 09_來源摘要/Skiba_2015_intramuscular_determinants_Wprime_recovery.md
  - 09_來源摘要/Poole_Jones_2017_VO2max_verification.md
  - 09_來源摘要/Zacca_2019_VO2FITTING_software.md
  - 09_來源摘要/Wooten_2021_excess_VCO2_recovery_fatigability.md
- 既有頁更新：
  - 04_CPET/VO2max_Measurement.md
  - 04_CPET/CPET_Protocol_Design.md
  - 04_CPET/Wprime_Balance_Model.md
  - 05_Exercise_Physiology/PCr_Resynthesis.md
  - 04_CPET/VO2_Kinetics.md
  - index.md
- 明確標示的 conflict / caveat：
  1. 當研究目標是確認 true VO2max 時，VO2peak 不能與 VO2max 互用；secondary criteria 也不能當作普遍有效的驗證規則。
  2. W' recovery 不是 bulk PCr recovery 的簡化替身；Skiba 2015 顯示兩者 time course 差異很大，應避免把 W' 當成單一代謝池。
  3. VO2 kinetics preprocessing 與 model choice 會實質改變 tau / slow component 估計；software standardization 不能取代 physiology judgment。
  4. Wooten 2021 只提供 pilot、indirect excess VCO2 證據，屬 hypothesis-generating，不足以建立臨床或機轉共識。
- index.md 更新：Total pages 275 -> 280
- 下一批待處理（依 post-batch-26 health check queue 重新排序）：
  - sports7020031/sports7020031.md
  - the-real-happy-pill-power-up-your-brain-by-moving-your-body-1/the-real-happy-pill-power-up-your-brain-by-moving-your-body-1.md
  - w__recovery_kinetics_after_exhaustion__a_two_phase/w__recovery_kinetics_after_exhaustion__a_two_phase.md
  - 00001648-199411000-00009/00001648-199411000-00009.md
  - 16 high altitude/16 high altitude.md

## [2026-04-25] lint | 全知識百科 health check（post-batch-26）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python C:\知識百科\08_工具與Workflow\tests\test_wiki_health_check.py` → 6 tests passed
  - `python C:\知識百科\08_工具與Workflow\wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 280
  - orphan 0
  - weak links 0
  - broken links 0
  - missing_from_index 0
  - stale candidates 0
  - contradiction candidates 0
  - raw_backlog: 21（26 -> 21）
  - raw verification queue:
    1. sports7020031/sports7020031.md
    2. the-real-happy-pill-power-up-your-brain-by-moving-your-body-1/the-real-happy-pill-power-up-your-brain-by-moving-your-body-1.md
    3. w__recovery_kinetics_after_exhaustion__a_two_phase/w__recovery_kinetics_after_exhaustion__a_two_phase.md
    4. 00001648-199411000-00009/00001648-199411000-00009.md
    5. 16 high altitude/16 high altitude.md

## [2026-04-25] ingest | W' recovery / hierarchical regression / altitude physiology / exercise-brain translation（Batch 27）
- Batch: 27
- heartbeat 指示：承接 post-batch-26 raw verification queue；依 schema，單一回合最多只可讀取 5 份 raw files，因此本回合實際讀取 5/5。
- Candidate ranking（承接 post-batch-26 raw verification queue，依來源優先級 + 主題相關性 + backlog impact 排序）：
  1. sports7020031/sports7020031.md
  2. the-real-happy-pill-power-up-your-brain-by-moving-your-body-1/the-real-happy-pill-power-up-your-brain-by-moving-your-body-1.md
  3. w__recovery_kinetics_after_exhaustion__a_two_phase/w__recovery_kinetics_after_exhaustion__a_two_phase.md
  4. 00001648-199411000-00009/00001648-199411000-00009.md
  5. 16 high altitude/16 high altitude.md
- Selected files（本回合實際讀取 5/5）：
  1. sports7020031/sports7020031.md
  2. the-real-happy-pill-power-up-your-brain-by-moving-your-body-1/the-real-happy-pill-power-up-your-brain-by-moving-your-body-1.md
  3. w__recovery_kinetics_after_exhaustion__a_two_phase/w__recovery_kinetics_after_exhaustion__a_two_phase.md
  4. 00001648-199411000-00009/00001648-199411000-00009.md
  5. 16 high altitude/16 high altitude.md
- 類型 / 層級 / 可信度：
  - sports7020031：methods / software original article duplicate raw `.md`，Tier 3，可信度 medium
  - The Real Happy Pill：科普書，Tier 2，可信度 medium
  - W' Recovery Kinetics after Exhaustion：original article，Tier 3，可信度 medium
  - Hierarchical Regression Analysis Applied to a Study of Multiple Dietary Exposures and Breast Cancer：methods original article，Tier 3，可信度 medium
  - High Altitude and Flying：textbook chapter，Tier 1，可信度 high
- 新建來源摘要頁 4：
  - 09_來源摘要/Caen_2021_Wprime_recovery_two_phase.md
  - 09_來源摘要/Witte_Greenland_1994_hierarchical_regression.md
  - 09_來源摘要/High_Altitude_and_Flying.md
  - 09_來源摘要/The_Real_Happy_Pill.md
- 新建主題頁 3：
  - 04_CPET/Wprime_Recovery.md
  - 02_方法學/層級回歸與Semi_Bayes.md
  - 05_Exercise_Physiology/高海拔與飛行低氧生理.md
- 既有頁更新：
  - 09_來源摘要/Zacca_2019_VO2FITTING_software.md
  - 04_CPET/Wprime_Balance_Model.md
  - 04_CPET/Training_Prescription_by_CP.md
  - 05_Exercise_Physiology/PCr_Resynthesis.md
  - 05_Exercise_Physiology/運動時氧輸送與換氣.md
  - 02_方法學/治療性運動處方.md
  - index.md
- duplicate / raw-path handling：
  - `sports7020031/sports7020031.md` 已確認為既有 `Zacca_2019_VO2FITTING_software.md` 的 duplicate raw path，已補登到來源摘要，不新增主結論。
- 明確標示的 conflict / caveat：
  1. W' recovery 不能再被簡化成 single universal monoexponential recharge；Caen 2021 支持 exhaustion 後存在 fast + slow phase。
  2. PCr / VO2 recovery 只解釋 W' reconstitution 的一部分，不能把 W' 直接縮成單一 metabolic tank。
  3. hierarchical regression / semi-Bayes 可降低 implausible coefficient instability，但 second-stage structure 與 `tau` 若 misspecified，也會把 estimate 拉錯方向。
  4. 15% oxygen hypoxic challenge 是 practical cabin simulation，不等於真實 hypobaric altitude physiology。
  5. The Real Happy Pill 可用於病人教育翻譯，但不能當成 exercise-brain 效果大小或 treatment hierarchy 的共識級證據。
- index.md 更新：Total pages 280 -> 287
- 下一批待處理（依 post-batch-27 health check queue 重新排序）：
  - Karstenetal.2016Comparisonofinter-trialrecoverytimes/Karstenetal.2016Comparisonofinter-trialrecoverytimes.md
  - LambricketalEJAP2009/LambricketalEJAP2009.md
  - Phosphocreatine Resynthesis After Intense Exercise/Phosphocreatine Resynthesis After Intense Exercise.md
  - The VCO2 VO2 relationship during heavy constant work rate exercise/The VCO2 VO2 relationship during heavy constant work rate exercise.md
  - Wooten et al. Pilot and Feasibility Studies/Wooten et al. Pilot and Feasibility Studies.md

## [2026-04-25] lint | 全知識百科 health check（post-batch-27）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python C:\知識百科\08_工具與Workflow\tests\test_wiki_health_check.py` → 6 tests passed
  - `python C:\知識百科\08_工具與Workflow\wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 287
  - orphan 0
  - weak links 0
  - broken links 0
  - missing_from_index 0
  - stale candidates 0
  - contradiction candidates 0
  - raw_backlog: 16（21 -> 16）
  - raw verification queue:
    1. Karstenetal.2016Comparisonofinter-trialrecoverytimes/Karstenetal.2016Comparisonofinter-trialrecoverytimes.md
    2. LambricketalEJAP2009/LambricketalEJAP2009.md
    3. Phosphocreatine Resynthesis After Intense Exercise/Phosphocreatine Resynthesis After Intense Exercise.md
    4. The VCO2 VO2 relationship during heavy constant work rate exercise/The VCO2 VO2 relationship during heavy constant work rate exercise.md
    5. Wooten et al. Pilot and Feasibility Studies/Wooten et al. Pilot and Feasibility Studies.md

## [2026-04-25] ingest | CP/W' inter-trial recovery / submaximal VO2max estimation / PCr recovery biology / VCO2-VO2 buffering physiology（Batch 28）
- Batch: 28
- 使用者指示：延續上一批；依 schema，本回合實際讀取 5/5 份 raw files，不擴讀。
- Candidate ranking（承接 post-batch-27 raw verification queue）：
  1. Karstenetal.2016Comparisonofinter-trialrecoverytimes/Karstenetal.2016Comparisonofinter-trialrecoverytimes.md
  2. LambricketalEJAP2009/LambricketalEJAP2009.md
  3. Phosphocreatine Resynthesis After Intense Exercise/Phosphocreatine Resynthesis After Intense Exercise.md
  4. The VCO2 VO2 relationship during heavy constant work rate exercise/The VCO2 VO2 relationship during heavy constant work rate exercise.md
  5. Wooten et al. Pilot and Feasibility Studies/Wooten et al. Pilot and Feasibility Studies.md
- Selected files（本回合實際讀取 5/5）：
  1. Karstenetal.2016Comparisonofinter-trialrecoverytimes/Karstenetal.2016Comparisonofinter-trialrecoverytimes.md
  2. LambricketalEJAP2009/LambricketalEJAP2009.md
  3. Phosphocreatine Resynthesis After Intense Exercise/Phosphocreatine Resynthesis After Intense Exercise.md
  4. The VCO2 VO2 relationship during heavy constant work rate exercise/The VCO2 VO2 relationship during heavy constant work rate exercise.md
  5. Wooten et al. Pilot and Feasibility Studies/Wooten et al. Pilot and Feasibility Studies.md
- 類型 / 層級 / 可信度：
  - Karsten 2016：original article，Tier 3，可信度 medium
  - Lambrick 2009：original article，Tier 3，可信度 medium
  - McMahon & Jenkins：review article，Tier 1，可信度 high
  - Stringer / Wasserman / Casaburi 1995：original article，Tier 3，可信度 medium
  - Wooten duplicate raw path：pilot original article duplicate raw `.md`，Tier 3，可信度 medium
- 新建來源摘要頁 4：
  - 09_來源摘要/Karsten_2016_intertrial_recovery_CP_Wprime.md
  - 09_來源摘要/Lambrick_2009_RPE13_VO2max_prediction.md
  - 09_來源摘要/McMahon_Jenkins_PCr_resynthesis_after_intense_exercise.md
  - 09_來源摘要/Stringer_Wasserman_Casaburi_1995_VCO2_VO2_heavy_constant_work.md
- 既有頁更新：
  - 04_CPET/CP_Test_Reliability.md
  - 04_CPET/Training_Prescription_by_CP.md
  - 05_Exercise_Physiology/PCr_Resynthesis.md
  - 04_CPET/Wprime_Recovery.md
  - 04_CPET/VO2max_Measurement.md
  - 04_CPET/CPET_Protocol_Design.md
  - 04_CPET/Gas_Exchange_Threshold.md
  - 04_CPET/V_Slope_Method.md
  - 09_來源摘要/Wooten_2021_excess_VCO2_recovery_fatigability.md
  - index.md
- duplicate / raw-path handling：
  - `Wooten et al. Pilot and Feasibility Studies/Wooten et al. Pilot and Feasibility Studies.md` 已確認為既有 `Wooten_2021_excess_VCO2_recovery_fatigability.md` 的 duplicate raw path，已補登，不新增主結論。
- 明確標示的 conflict / caveat：
  1. same-day shortened inter-trial recovery 可保留 CP，但會明顯扭曲 W'；CP 與 W' 不能假設具有相同 measurement robustness。
  2. RPE 13 submaximal ramp prediction 可作 low-fit 情境下的 practical fallback，但不能與 measured / verified VO2max 混用。
  3. PCr recovery 本身常包含 fast + slow component；單一 tau 是 practical summary，不是完整機制。
  4. heavy constant-work 的 VCO2-VO2 inflection 與 lactate / bicarbonate 變化同步，可支持 buffering physiology，但不取代 ramp CPET 的 GET operational definition。
- index.md 更新：Total pages 287 -> 291

## [2026-04-25] lint | 全知識百科 health check（post-batch-28）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python C:\知識百科\08_工具與Workflow\tests\test_wiki_health_check.py` → 6 tests passed
  - `python C:\知識百科\08_工具與Workflow\wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 291
  - orphan 0
  - weak links 0
  - broken links 0
  - missing_from_index 0
  - stale candidates 0
  - contradiction candidates 0
  - raw_backlog: 11（16 -> 11）
  - raw verification queue:
    1. ajvr-ajvr.2000.61.638/ajvr-ajvr.2000.61.638.md
    2. bf00235176/bf00235176.md
    3. characterizing_the_exponential_profile_of_w_.24/characterizing_the_exponential_profile_of_w_.24.md
    4. ferguson-et-al-2010-effect-of-recovery-duration-from-prior-exhaustive-exercise-on-the-parameters-of-the-power-duration/effect of recovery duration from prior exhaustive exercise on the parameters of the power duration.md
    5. effect_of_work_and_recovery_durations_on_w_.20/effect_of_work_and_recovery_durations_on_w_.20.md

## [2026-04-25] ingest | VO2 kinetics modifiers / W' recovery structure / interval architecture caveats（Batch 29）
- Batch: 29
- 使用者指示：延續上一批；依 schema，本回合實際讀取 5/5 份 raw files，不擴讀。
- Candidate ranking（承接 post-batch-28 raw verification queue）：
  1. ajvr-ajvr.2000.61.638/ajvr-ajvr.2000.61.638.md
  2. bf00235176/bf00235176.md
  3. characterizing_the_exponential_profile_of_w_.24/characterizing_the_exponential_profile_of_w_.24.md
  4. ferguson-et-al-2010-effect-of-recovery-duration-from-prior-exhaustive-exercise-on-the-parameters-of-the-power-duration/effect of recovery duration from prior exhaustive exercise on the parameters of the power duration.md
  5. effect_of_work_and_recovery_durations_on_w_.20/effect_of_work_and_recovery_durations_on_w_.20.md
- Selected files（本回合實際讀取 5/5）：
  1. ajvr-ajvr.2000.61.638/ajvr-ajvr.2000.61.638.md
  2. bf00235176/bf00235176.md
  3. characterizing_the_exponential_profile_of_w_.24/characterizing_the_exponential_profile_of_w_.24.md
  4. ferguson-et-al-2010-effect-of-recovery-duration-from-prior-exhaustive-exercise-on-the-parameters-of-the-power-duration/effect of recovery duration from prior exhaustive exercise on the parameters of the power duration.md
  5. effect_of_work_and_recovery_durations_on_w_.20/effect_of_work_and_recovery_durations_on_w_.20.md
- 類型 / 層級 / 可信度：
  - Geor et al. 2000：original article（animal study），Tier 3，可信度 low
  - Zhang et al. 1991：original article，Tier 3，可信度 medium
  - Lievens et al. 2024：original article，Tier 3，可信度 medium
  - Ferguson et al. 2010：original article，Tier 3，可信度 medium
  - Skiba et al. 2014：original article，Tier 3，可信度 medium
- 新建來源摘要頁 5：
  - 09_來源摘要/Geor_2000_horse_warmup_VO2_VCO2_kinetics.md
  - 09_來源摘要/Zhang_1991_fitness_VO2_VCO2_step_kinetics.md
  - 09_來源摘要/Lievens_2024_partial_Wprime_recovery.md
  - 09_來源摘要/Ferguson_2010_Wprime_recovery_after_exhaustion.md
  - 09_來源摘要/Skiba_2014_work_recovery_durations_Wprime_reconstitution.md
- 既有頁更新：
  - 04_CPET/Wprime_Balance_Model.md
  - 04_CPET/Wprime_Recovery.md
  - 04_CPET/Training_Prescription_by_CP.md
  - 04_CPET/VO2_Kinetics.md
  - index.md
- 明確標示的 conflict / caveat：
  1. exhaustion-based two-phase W' recovery 不能直接外推到 partial depletion；Lievens 2024 只支持「固定 tau 不足」，不支持一律改寫成 biexponential 共識。
  2. prior exhaustion 後 CP 可維持穩定，但 W' 只會曲線式回來，且恢復速度慢於 VO2、快於 lactate；因此 W' 不能縮成單一 physiologic tank。
  3. W'BAL 整體可用，但 interval structure 本身會改變實際可用 W'；相似 predicted depletion 不代表相同 physiologic state。
  4. Zhang 1991 的 step-test kinetics 與 Geor 2000 的 equine warm-up 資料都屬 Tier 3 補充，不可直接升格成 human constant-load kinetics 的主框架。
- index.md 更新：Total pages 291 -> 296

## [2026-04-25] lint | 全知識百科 health check（post-batch-29）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python C:\知識百科\08_工具與Workflow\tests\test_wiki_health_check.py` → 6 tests passed
  - `python C:\知識百科\08_工具與Workflow\wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 296
  - orphan 0
  - weak links 0
  - broken links 0
  - missing_from_index 0
  - stale candidates 0
  - contradiction candidates 0
  - raw_backlog: 6（11 -> 6）
  - raw verification queue:
    1. francescato-cettolo-2021-influence-of-the-fitting-window-on-the-o2-uptake-kinetics-at-the-onset-of-moderate-intensity/influence of the fitting window on the o2 uptake kinetics at the onset of moderate intensity.md
    2. ma-et-al-2010-clarifying-the-equation-for-modeling-of-v̇o2-kinetics-above-the-lactate-threshold (2)/ma-et-al-2010-clarifying-the-equation-for-modeling-of-v̇o2-kinetics-above-the-lactate-threshold (2).md
    3. pettitt-jamnick-2017-commentary-on-measurement-of-the-maximum-oxygen-uptake-v̇o2max-v̇o2peak-is-no-longer-acceptable/pettitt-jamnick-2017-commentary-on-measurement-of-the-maximum-oxygen-uptake-v̇o2max-v̇o2peak-is-no-longer-acceptable.md
    4. s00421-021-04874-3/s00421-021-04874-3.md
    5. the-reliability-and-validity-of-the-3-min-all-out-cycling-7xcudjg120/the-reliability-and-validity-of-the-3-min-all-out-cycling-7xcudjg120.md

## [2026-04-25] ingest | VO2 fitting window / Heaviside kinetics clarification / VO2max verification caveat / trained-cyclist W' biexponential recovery / 3-min all-out validity（Batch 30）
- Batch: 30
- 使用者指示：延續上一批；依 schema，本回合實際讀取 5/5 份 raw files，不擴讀。
- Candidate ranking（承接 post-batch-29 raw verification queue）：
  1. francescato-cettolo-2021-influence-of-the-fitting-window-on-the-o2-uptake-kinetics-at-the-onset-of-moderate-intensity/influence of the fitting window on the o2 uptake kinetics at the onset of moderate intensity.md
  2. ma-et-al-2010-clarifying-the-equation-for-modeling-of-v̇o2-kinetics-above-the-lactate-threshold (2)/ma-et-al-2010-clarifying-the-equation-for-modeling-of-v̇o2-kinetics-above-the-lactate-threshold (2).md
  3. pettitt-jamnick-2017-commentary-on-measurement-of-the-maximum-oxygen-uptake-v̇o2max-v̇o2peak-is-no-longer-acceptable/pettitt-jamnick-2017-commentary-on-measurement-of-the-maximum-oxygen-uptake-v̇o2max-v̇o2peak-is-no-longer-acceptable.md
  4. s00421-021-04874-3/s00421-021-04874-3.md
  5. the-reliability-and-validity-of-the-3-min-all-out-cycling-7xcudjg120/the-reliability-and-validity-of-the-3-min-all-out-cycling-7xcudjg120.md
- Selected files（本回合實際讀取 5/5）：
  1. francescato-cettolo-2021-influence-of-the-fitting-window-on-the-o2-uptake-kinetics-at-the-onset-of-moderate-intensity/influence of the fitting window on the o2 uptake kinetics at the onset of moderate intensity.md
  2. ma-et-al-2010-clarifying-the-equation-for-modeling-of-v̇o2-kinetics-above-the-lactate-threshold (2)/ma-et-al-2010-clarifying-the-equation-for-modeling-of-v̇o2-kinetics-above-the-lactate-threshold (2).md
  3. pettitt-jamnick-2017-commentary-on-measurement-of-the-maximum-oxygen-uptake-v̇o2max-v̇o2peak-is-no-longer-acceptable/pettitt-jamnick-2017-commentary-on-measurement-of-the-maximum-oxygen-uptake-v̇o2max-v̇o2peak-is-no-longer-acceptable.md
  4. s00421-021-04874-3/s00421-021-04874-3.md
  5. the-reliability-and-validity-of-the-3-min-all-out-cycling-7xcudjg120/the-reliability-and-validity-of-the-3-min-all-out-cycling-7xcudjg120.md
- 類型 / 層級 / 可信度：
  - Francescato & Cettolo 2021：original article，Tier 3，可信度 medium
  - Ma et al. 2010：letter / commentary，Tier 3，可信度 medium
  - Pettitt & Jamnick 2017：letter / commentary，Tier 3，可信度 medium
  - Chorley et al. 2021：original article，Tier 3，可信度 medium
  - Wright et al. 2017：original article，Tier 3，可信度 medium
- 新建來源摘要頁 5：
  - 09_來源摘要/Francescato_Cettolo_2021_VO2_fitting_window.md
  - 09_來源摘要/Ma_2010_Heaviside_VO2_kinetics_equation.md
  - 09_來源摘要/Pettitt_Jamnick_2017_VO2max_verification_commentary.md
  - 09_來源摘要/Chorley_2021_biexponential_Wprime_reconstitution_trained_cyclists.md
  - 09_來源摘要/Wright_2017_3min_allout_CP_validity.md
- 既有頁更新：
  - 04_CPET/VO2_Kinetics.md
  - 04_CPET/VO2_Slow_Component.md
  - 04_CPET/VO2max_Measurement.md
  - 04_CPET/CPET_Protocol_Design.md
  - 04_CPET/Wprime_Recovery.md
  - 04_CPET/Wprime_Balance_Model.md
  - 04_CPET/CP_Test_Reliability.md
  - 04_CPET/Critical_Power.md
  - index.md
- 明確標示的 conflict / caveat：
  1. fitting window 不是中性 preprocessing；Francescato 2021 顯示 moderate-intensity `tau` 可因起始資料移除規則改變約 30%。
  2. Ma 2010 是數學式澄清，不是新的 physiology 證據；Heaviside gating 改善的是 delayed-term implementation clarity，不是直接證明某機制較正確。
  3. Pettitt & Jamnick 2017 支持 verification bout，但提醒 ramp 與 VEB 的一致性要放在 measurement variability 與 ramp design 一起解讀，不能只做 binary pass/fail。
  4. Chorley 2021 在 trained cyclists 的 repeated maximal ramps 支持 biexponential `W'` recovery；但這不推翻 Lievens 2024 對 partial depletion 的修正，只是說 recovery shape 受 depletion context 影響。
  5. Wright 2017 顯示 3-min all-out 的 `EP` 與 `WEP` 不能一起視為同等有效；ergometer mode 會改變 `CP` validity，而 `WEP` 在兩種模式都低估 `W'`。
- index.md 更新：Total pages 296 -> 301

## [2026-04-25] lint | 全知識百科 health check（post-batch-30）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python C:\知識百科\08_工具與Workflow\tests\test_wiki_health_check.py` → 6 tests passed
  - `python C:\知識百科\08_工具與Workflow\wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 301
  - orphan 0
  - weak links 0
  - broken links 0
  - missing_from_index 0
  - stale candidates 0
  - contradiction candidates 0
  - raw_backlog: 3（6 -> 3）
  - raw verification queue:
    1. Building Resilience Through Play.md
    2. Why Sleep Matters in Early Childhood Development.md
    3. the_reconstitution_of_w__depends_on_both_work_and.22/the_reconstitution_of_w__depends_on_both_work_and.22.md

## [2026-04-25] ingest | play and resilience / early childhood sleep / W' recovery work-bout dependence（Batch 31）
- Batch: 31
- 使用者指示：延續上一批；依 schema，本回合實際讀取 3/5 份 raw files，不擴讀。
- Candidate ranking（承接 post-batch-30 raw verification queue）：
  1. Building Resilience Through Play.md
  2. Why Sleep Matters in Early Childhood Development.md
  3. the_reconstitution_of_w__depends_on_both_work_and.22/the_reconstitution_of_w__depends_on_both_work_and.22.md
- Selected files（本回合實際讀取 3/5）：
  1. Building Resilience Through Play.md
  2. Why Sleep Matters in Early Childhood Development.md
  3. the_reconstitution_of_w__depends_on_both_work_and.22/the_reconstitution_of_w__depends_on_both_work_and.22.md
- 類型 / 層級 / 可信度：
  - Building Resilience Through Play：educational website / podcast transcript，Tier 2，可信度 medium
  - Why Sleep Matters in Early Childhood Development：educational website / podcast transcript，Tier 2，可信度 medium
  - Caen et al. 2019：original article，Tier 3，可信度 medium
- 新建來源摘要頁 3：
  - 09_來源摘要/Building_Resilience_Through_Play.md
  - 09_來源摘要/Why_Sleep_Matters_in_Early_Childhood_Development.md
  - 09_來源摘要/Caen_2019_Wprime_reconstitution_depends_on_work_and_recovery.md
- 既有頁更新：
  - 07_Pediatric_Development/創傷_復原力與兒童發展.md
  - 07_Pediatric_Development/兒童睡眠與睡眠障礙總論.md
  - 04_CPET/Wprime_Recovery.md
  - 04_CPET/Wprime_Balance_Model.md
  - 04_CPET/Training_Prescription_by_CP.md
  - index.md
- 明確標示的 conflict / caveat：
  1. play 可支持 resilience，但不能被寫成 child 靠自己玩就能恢復；supportive relationship 仍是必要 scaffold。
  2. Why Sleep Matters 是 expert science translation，可補強機制理解與病人教育，但不能取代 pediatric sleep guideline / textbook triage。
  3. Caen 2019 顯示 `W'` recovery 不只取決於 recovery power / duration，也受前一段 work-bout 特性影響；因此 recovery 不能再被簡化成單靠 `DCP` 的 group-derived constant。
  4. current `W'BAL` 對短 recovery 仍傾向低估，尤其在不同 depletion pattern 下更明顯。
- index.md 更新：Total pages 301 -> 304

## [2026-04-25] lint | 全知識百科 health check（post-batch-31）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python C:\知識百科\08_工具與Workflow\tests\test_wiki_health_check.py` → 6 tests passed
  - `python C:\知識百科\08_工具與Workflow\wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 304
  - orphan 0
  - weak links 0
  - broken links 0
  - missing_from_index 0
  - stale candidates 0
  - contradiction candidates 0
  - raw_backlog: 0
  - raw verification queue: none
- 備註：
  - 先前兩個 stale candidates 為 frontmatter `updated` 未同步至 `2026-04-25` 的 metadata 誤判；補齊後已歸零。

## [2026-04-25] synthesis | CP / W' interval design topic reorganization
- 類型：主題重整
- 目標：處理 oversized page，降低 `Training_Prescription_by_CP.md` 與 `Wprime_Balance_Model` / `Wprime_Recovery` 的重複內容。
- 新建主題頁：
  - 04_CPET/CP_Wprime_Interval_Design.md
- 重整內容：
  - 將 severe-domain interval 的 `W'` dose、`W'BAL` 角色、recovery power / duration caveat、interval structure 與 protocol fragility 抽成獨立子頁。
  - `04_CPET/Training_Prescription_by_CP.md` 改回 overview 頁，保留三域處方與三個核心 practical conclusions。
- 交叉連結更新：
  - 04_CPET/Training_Prescription_by_CP.md
  - 04_CPET/Critical_Power.md
  - 04_CPET/Wprime_Balance_Model.md
  - 04_CPET/Wprime_Recovery.md
  - index.md
- index.md 更新：Total pages 304 -> 305

## [2026-04-25] synthesis | Critical_Power page condensation
- 類型：主題重整
- 目標：讓 `Critical_Power.md` 回到概念主頁角色，不再重複承載 `W' recovery` 與 `W'BAL` 的細節頁功能。
- 主要調整：
  - 刪去 `Critical_Power.md` 內大段 `W' reconstitution` 子模型與 athlete-specific recovery 細節。
  - 改成短摘要加導頁，連回：
    - `Wprime_Recovery.md`
    - `Wprime_Balance_Model.md`
    - `CP_Wprime_Interval_Design.md`
  - 同步精簡 frontmatter source list 與部分測試描述，保留 CP 主框架需要的來源。
- 結果：
  - `Critical_Power.md` 行數由 248 -> 214
  - 仍屬 oversized page，但已明顯縮減

## [2026-04-25] lint | 全知識百科 health check（post-topic-reorg）
- 執行腳本：08_工具與Workflow/wiki_health_check.py
- 驗證方式：
  - `python C:\知識百科\08_工具與Workflow\tests\test_wiki_health_check.py` → 6 tests passed
  - `python C:\知識百科\08_工具與Workflow\wiki_health_check.py --wiki C:\知識百科 --raw C:\原始資料 --format markdown --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md`
- 更新報告：08_工具與Workflow/health_check_report_latest.md
- 結果摘要：
  - pages_scanned: 305
  - orphan 0
  - weak links 0
  - broken links 0
  - missing_from_index 0
  - stale candidates 0
  - contradiction candidates 0
  - raw_backlog: 0
  - raw verification queue: none
- oversized pages 變化：
  - `04_CPET/Training_Prescription_by_CP.md` 已退出 oversized list
  - `04_CPET/Critical_Power.md` 由 248 -> 214，仍待後續再拆

## [2026-04-25] update | ingest 工作流規則同步
- 將 ingest 單批上限由 10 改為 5。
- 同步更新：
  - SCHEMA.md
  - 08_工具與Workflow/知識百科_ingest_工作流.md
  - index.md
- 明確區分：ingest 的 5-file cap 與 health check 的 5-file raw verification cap 為不同流程，不可混用。
- 本次僅同步規則，未啟動新一批文件 ingest。

## [2026-04-25] ingest | early childhood stress / serve and return / stability / mattering（Batch 32）
- Batch: 32
- Candidate ranking：
  1. Stress_Disrupts_Architecture_Developing_Brain
  2. Finding the Balance Transforming How We Think About the Body’s Response to Stress in Early Childhood
  3. Serve and Return.md
  4. HCDC-ECSCEE-Stability
  5. Mattering-Paper-center-on-the-developing-child
  6. Webinar_Transcript_Stability
  7. Podcast_ Toxic Stress.md
  8. Mattering-Strategies-
  9. Harvard-Kids-and-Climate-Long-Report_V6
- Selected files（本回合實際讀取 5/5）：
  1. Stress_Disrupts_Architecture_Developing_Brain
  2. Finding the Balance Transforming How We Think About the Body’s Response to Stress in Early Childhood
  3. Serve and Return.md
  4. HCDC-ECSCEE-Stability
  5. Mattering-Paper-center-on-the-developing-child
- 類型 / 層級 / 可信度：
  - Excessive Stress Disrupts the Architecture of the Developing Brain：網站資料 / scientific working paper，Tier 2，可信度 medium
  - Finding the Balance：網站資料 / scientific working paper，Tier 2，可信度 medium
  - Serve and Return：educational website / podcast transcript，Tier 2，可信度 medium
  - From Resources to Routines：網站資料 / scientific working paper，Tier 2，可信度 medium
  - Mattering in Early Childhood：網站資料 / working paper，Tier 2，可信度 medium
- 新建來源摘要頁 5：
  - 09_來源摘要/Excessive_Stress_Disrupts_Developing_Brain.md
  - 09_來源摘要/Finding_the_Balance_2026_early_childhood_stress.md
  - 09_來源摘要/Serve_and_Return.md
  - 09_來源摘要/From_Resources_to_Routines_Stability.md
  - 09_來源摘要/Mattering_in_Early_Childhood.md
- 新建主題頁 4：
  - 07_Pediatric_Development/Toxic_Stress.md
  - 07_Pediatric_Development/Serve_and_Return.md
  - 07_Pediatric_Development/發展環境穩定性.md
  - 07_Pediatric_Development/Mattering_總論.md
- 既有頁更新：
  - 07_Pediatric_Development/創傷_復原力與兒童發展.md
  - 07_Pediatric_Development/嬰兒期發展.md
  - 07_Pediatric_Development/幼兒與學齡前期發展.md
  - 07_Pediatric_Development/托育與Early_Care_and_Education.md
  - index.md
- 明確標示的 conflict / caveat：
  1. `Toxic stress` 指的是 prolonged biologic stress response，不是 adversity event 的同義詞。
  2. `Finding the Balance` 修正了舊 public framing：不是所有 stress 都有害，predictability、timing、individual sensitivity 與 community buffering 都要納入。
  3. `Serve and return` 不是 24/7 刺激，也不是 parent-only；單向 educational media 不能替代 contingent interaction。
  4. `Stability` 不能被簡化成「家裡更有規矩」；housing、food、child care、work schedule instability 會直接破壞 routine。
  5. `Mattering` 不等於 belonging 或 praise；還要有被理解、被需要、能加值的經驗。
- index.md 更新：Total pages 305 -> 314
- 下一批待處理：
  - Podcast_ Toxic Stress.md
  - Webinar_Transcript_Stability
  - Mattering-Strategies-
  - Harvard-Kids-and-Climate-Long-Report_V6
  - FWI_HPM-Strategic-Brief-V4
  - wp15_health_FINALv2

## [2026-04-25] ingest | brain-body lifelong health / toxic stress translation / stability webinar / mattering strategies / place（Batch 33）
- Batch: 33
- Candidate ranking：
  1. wp15_health_FINALv2
  2. Podcast_ Toxic Stress.md
  3. Webinar_Transcript_Stability
  4. Mattering-Strategies-
  5. FWI_HPM-Strategic-Brief-V4
  6. Harvard-Kids-and-Climate-Long-Report_V6
- Selected files（本回合實際讀取 5/5）：
  1. wp15_health_FINALv2
  2. Podcast_ Toxic Stress.md
  3. Webinar_Transcript_Stability
  4. Mattering-Strategies-
  5. FWI_HPM-Strategic-Brief-V4
- 類型 / 層級 / 可信度：
  - Connecting the Brain to the Rest of the Body：review article / scientific working paper，Tier 1，可信度 high
  - Toxic Stress Brain Architects Podcast：網站資料 / podcast transcript，Tier 2，可信度 medium
  - Why Stability Matters Webinar：網站資料 / webinar transcript，Tier 2，可信度 medium
  - Mattering Strategies：網站資料 / practical handout，Tier 2，可信度 medium
  - Place Matters：網站資料 / strategic brief，Tier 2，可信度 medium
- 新建來源摘要頁 5：
  - 09_來源摘要/Connecting_the_Brain_to_the_Rest_of_the_Body.md
  - 09_來源摘要/Toxic_Stress_Brain_Architects_Podcast.md
  - 09_來源摘要/Why_Stability_Matters_Webinar.md
  - 09_來源摘要/Mattering_Strategies.md
  - 09_來源摘要/Place_Matters.md
- 新建主題頁 2：
  - 07_Pediatric_Development/早期發展與終身健康.md
  - 07_Pediatric_Development/發展環境與Place.md
- 既有頁更新：
  - 07_Pediatric_Development/Toxic_Stress.md
  - 07_Pediatric_Development/發展環境穩定性.md
  - 07_Pediatric_Development/Mattering_總論.md
  - 07_Pediatric_Development/正向教養與家庭支持.md
  - 07_Pediatric_Development/文化謙遜與偏誤敏感照護.md
  - 07_Pediatric_Development/創傷_復原力與兒童發展.md
  - 07_Pediatric_Development/托育與Early_Care_and_Education.md
  - index.md
- 明確標示的 conflict / caveat：
  1. health 與 learning 不能再被切成兩條互不相干的 early-childhood 敘事；同一組早期環境會一起 shape brain、immune 與 cardiometabolic systems。
  2. `Toxic stress` 仍然是 biologic response pattern，不是 event label；而且不能只講 child，還要講 adult buffering 與 system-generated load。
  3. `Stability` 不等於完全不變；sleep 也不是家務修飾，而是 developmental infrastructure。
  4. `Mattering` 不是 praise；repair、visibility 與 age-appropriate contribution 都是核心。
  5. `Place` 不能被還原成 family choice，`race` 也不能被誤寫成 biologic exposure；更準確的鏈條是 racism shapes place, and place shapes development.
- index.md 更新：Total pages 314 -> 321
- 下一批待處理：
  - Harvard-Kids-and-Climate-Long-Report_V6

## [2026-04-26] synthesis | 高海拔疾病拆分為單一概念頁（Feynman 骨架）
- 觸發：user 指令「利用費曼式整理骨架整理資料；將原始資料拆成單一概念為單位，每一頁只處理一個概念」
- 來源：09_來源摘要/High_Altitude_and_Flying.md（textbook chapter，Tier 1）
- 既有 05_Exercise_Physiology/高海拔與飛行低氧生理.md 是合併頁，不拆原頁；新建三個臨床單一概念頁聚焦 illness 端：
  - 03_疾病與臨床主題/急性高山症.md（AMS）
  - 03_疾病與臨床主題/高海拔肺水腫.md（HAPE）
  - 03_疾病與臨床主題/高海拔腦水腫.md（HACE）
- 每頁均依 Feynman 骨架展開：一句話定義 → 已知 → 核心機制 → 臨床表現 → 評估方式 → 治療原則 → 臨床決策點 → 限制與未定論 → 理解缺口 → 臨床使用版 → 來源
- 每頁附「我能不能把這段清楚教給住院醫師？」自我檢查與 explicit 理解缺口
- 標記的下一輪補強重點：
  1. AMS 的 biomarker / individual susceptibility prediction 仍缺臨床可用工具
  2. HAPE-susceptible 的 vascular phenotype 分子機制
  3. HACE 與 HAPE 共存的共同 hypoxia signaling pathway
  4. 兒童 AMS / HACE 評估與 paediatric Lake Louise
- 與既有頁面的關係：
  - 不覆寫 05_Exercise_Physiology/高海拔與飛行低氧生理.md（生理 overview 仍由該頁負責）
  - 三個新頁專注於 clinical entity 的單一概念深度，互相 wikilink
  - 與 09_來源摘要/High_Altitude_and_Flying.md frontmatter contradictions 一致
- index.md 更新：Total pages 321 -> 324
- 下一批待處理：
  - Harvard-Kids-and-Climate-Long-Report_V6
  - 高海拔同源來源若有 review / guideline 進入再補強三頁的 evidence 層級

## [2026-04-26] synthesis | 高海拔同源 textbook 第二批單一概念拆分
- 觸發：user 確認繼續從同一份 textbook chapter 拆下一批
- 來源：09_來源摘要/High_Altitude_and_Flying.md（textbook chapter，Tier 1）
- 新建 3 個單一概念頁：
  - 03_疾病與臨床主題/呼吸疾病病人的飛行評估.md（preflight assessment + Hypoxic Challenge Test + BTS guideline 切點）
  - 03_疾病與臨床主題/慢性高山症.md（Monge disease；長期居住者的 acclimatization 失敗表型）
  - 05_Exercise_Physiology/高海拔_acclimatization_機制.md（六軸協同的生理過程，從 chapter 中既有合併頁拆出獨立深度頁）
- 每頁均依 Feynman 骨架 11 段展開 + 「我能不能把這段清楚教給住院醫師？」自我檢查 + explicit 理解缺口
- 與既有頁面的關係：
  - 不覆寫 05_Exercise_Physiology/高海拔與飛行低氧生理.md（生理 overview 仍由該頁負責；新頁是專注機制深度的 sibling）
  - 第一批三頁（AMS / HAPE / HACE）皆已加入慢性高山症與 acclimatization 機制的相關連結
- 標記的下一輪補強重點：
  1. HIF-1α vs HIF-2α 在不同 tissue 的相對角色
  2. Live high, train low 的 dose-response 與 ergogenic 效應大小
  3. Tibetan vs Andean vs Ethiopian 三大 adaptation pathway 的分子比較
  4. 兒童飛行評估（BPD survivor）與 PAH 病人 in-flight 風險
  5. CMS 與 polycythemia vera 的分子層次界線
- index.md 更新：Total pages 324 -> 327
- 下一批待處理：
  - Harvard-Kids-and-Climate-Long-Report_V6
  - 從 textbook chapter 餘下未拆部分：高海拔運動 work capacity 限制（exercise at altitude 段）若獨立成概念頁的價值評估

## [2026-04-26] synthesis | CP 從單一總論拆出三個臨床決策單一概念頁
- 觸發：user 換主題；以同一份 textbook chapter（Cerebral Palsy and Other Motor Disorders）為來源
- 來源：09_來源摘要/Cerebral_Palsy_and_Other_Motor_Disorders.md（textbook chapter，Tier 1）
- 既有 07_Pediatric_Development/Cerebral_Palsy_總論.md 已存在但僅 148 行，相對來源 378 行高度濃縮，未拆出單一臨床決策概念
- 新建 3 個單一概念頁（依 ADHD / ASD 分頁模式）：
  - 07_Pediatric_Development/CP_早期辨識與診斷.md（AACPDM Early Detection care pathway；HINE / GMs / MRI 三軸；< 6 月齡 high risk 工作診斷；normal MRI 不排除）
  - 07_Pediatric_Development/CP_功能分類系統.md（GMFCS / MACS / EDACS / VSS / FCCS / CFCS / VFCS 七系統；usual performance vs capability；多軸獨立評）
  - 07_Pediatric_Development/CP_髖部監測.md（AACPDM Hip Surveillance care pathway；migration percentage；GMFCS-stratified 監測時程；soft tissue vs bony surgery 決策）
- 每頁均依 Feynman 骨架 11 段展開 + 「我能不能把這段清楚教給住院醫師？」自我檢查 + explicit 理解缺口
- 標記的下一輪補強重點：
  1. CP 張力管理（oral / BoNT / ITB / SDR）詳述頁
  2. CP 神經肌肉性脊柱側彎與骨骼健康
  3. CP 呼吸照護共識（Gibson 2021 consensus）
  4. CP 共病與心理社會議題（vision、hearing、sleep、mental health、puberty / sexuality）
  5. CP transition / adult CP
  6. Genetic CP 的當代 panel 與 WES 觸發指引
  7. AAP menstrual management for adolescents with disabilities
- 與既有頁面的關係：
  - 不覆寫 Cerebral_Palsy_總論.md（保留其作為 entry point；新頁是專注單一決策的子頁，類似 ADHD / ASD 的子頁模式）
  - 三新頁互相 wikilink，並都連回 Cerebral_Palsy_總論
- index.md 更新：Total pages 327 -> 330
- 下一批待處理：
  - Harvard-Kids-and-Climate-Long-Report_V6
  - CP 同源 textbook 餘下未拆部分（張力管理、骨骼、呼吸、共病、transition）

## [2026-04-26] synthesis | CP 同源 textbook 第二批單一概念拆分
- 觸發：user 確認繼續從 CP 同源拆下一批
- 來源：09_來源摘要/Cerebral_Palsy_and_Other_Motor_Disorders.md（textbook chapter，Tier 1）
- 新建 3 個單一概念頁：
  - 07_Pediatric_Development/CP_張力管理.md（spasticity vs dystonia 區分；rehab → oral → BoNT/phenol → ITB/SDR 階梯；redistribution 而非 elimination）
  - 07_Pediatric_Development/CP_呼吸照護.md（Gibson 2021 共識 + AACPDM Sialorrhea care pathway；五軸風險：aspiration / scoliosis / clearance 弱 / 感染 / SDB）
  - 07_Pediatric_Development/CP_骨骼健康與骨折.md（AACPDM Osteoporosis care pathway + Novak 2020 traffic light；治療階梯 + bisphosphonate treatment-not-prevention）
- 每頁均依 Feynman 骨架 11 段展開 + 「我能不能把這段清楚教給住院醫師？」自我檢查 + explicit 理解缺口
- 標記的下一輪補強重點：
  1. CP dystonia 的 DBS（deep brain stimulation）candidate selection 與長期 outcome
  2. CP CoughAssist / mechanical airway clearance device 在不同 phenotype 的證據
  3. Standing program 對 BMD 的 dose-response（每天分鐘、累積週數）
  4. Bisphosphonate 兒童期使用對成年骨骼的長期影響
  5. SDR vs ITB 在同一 candidate 的 head-to-head 證據
- 與既有頁面的關係：
  - 不覆寫 Cerebral_Palsy_總論.md；既有總論「CP 子頁」區塊已加入這三新頁
  - 三新頁互相 wikilink，並都連回 Cerebral_Palsy_總論
  - CP 子頁系列（已六頁）：早期辨識 / 功能分類 / 髖部監測 / 張力管理 / 呼吸照護 / 骨骼健康
- index.md 更新：Total pages 330 -> 333
- 下一批待處理：
  - Harvard-Kids-and-Climate-Long-Report_V6
  - CP 同源 textbook 餘下：神經肌肉性脊柱側彎、共病管理（vision / hearing / sleep / mental health / GI / GU / sexuality / puberty）、transition / adult CP、F-Words framework

## [2026-04-26] synthesis | 中風復健 textbook 拆出三個臨床決策單一概念頁
- 觸發：user 換主題；既有 03_疾病與臨床主題/中風復健總論.md 是 136 行 vs 來源 695 行，總論已自承「評估方式 / 治療原則尚未填」
- 來源：09_來源摘要/Stroke_rehabilitation.md（textbook chapter，Tier 1 + AHA/ASA 2016 / 2021 guidelines）
- 新建 3 個單一概念頁：
  - 03_疾病與臨床主題/中風急性期處置與時間窗.md（time is brain；rtPA / thrombectomy / BP 階梯；ischemic vs hemorrhagic 反向邏輯；wakeup stroke / mismatch imaging）
  - 03_疾病與臨床主題/中風次發預防.md（AHA/ASA 2021 mechanism-based 分流；BP/lipid/glycemic/lifestyle/antithrombotic 五軸；DAPT short-course；cryptogenic 的 occult AF 篩查）
  - 03_疾病與臨床主題/偏癱肩痛.md（HSP 五條病因協同；prevention 與 dominant-feature 分流；Botox + NMES + positioning 三主軸；overhead pulley IIIC 不可做）
- 每頁均依 Feynman 骨架 11 段展開 + 「我能不能把這段清楚教給住院醫師？」自我檢查 + explicit 理解缺口 + AHA/ASA evidence level 標註
- 標記的下一輪補強重點：
  1. Tenecteplase vs alteplase 的 head-to-head 證據
  2. AI-assisted stroke imaging 與 minor LVO 處置
  3. Cilostazol 在亞洲 lacunar stroke secondary prevention 的角色
  4. ESUS 的 antithrombotic 決策（NAVIGATE / RE-SPECT 後）
  5. CAA + AF 的兩面 risk 決策框架
  6. CRPS 在 stroke 後的 phenotype-specific evidence
  7. Implantable peripheral nerve stimulator vs surface NMES 的 candidate
- 與既有頁面的關係：
  - 不覆寫 中風復健總論.md（既有總論本就承認 評估 / 治療 兩節 placeholder；新頁直接補上深度）
  - 三新頁互相 wikilink，並都連回 中風復健總論
- index.md 更新：Total pages 333 -> 336
- 下一批待處理：
  - Harvard-Kids-and-Climate-Long-Report_V6
  - CP 同源 textbook 餘下未拆部分
  - Stroke 同源 textbook 餘下：post-stroke seizure / VTE / dysphagia / spasticity / cognition-aphasia rehab / depression / CRPS / 整合 vascular syndromes 速查表

## [2026-04-26] ingest | caregiver health / pediatric primary care translation / climate as developmental environment（Batch 34）
- Batch: 34
- Candidate ranking：
  1. Connecting Health & Learning.md
  2. Self-Care Isn’t Selfish.md
  3. Harvard-Kids-and-Climate-Long-Report_V6
- Selected files（本回合實際讀取 3/3）：
  1. Connecting Health & Learning.md
  2. Self-Care Isn’t Selfish.md
  3. Harvard-Kids-and-Climate-Long-Report_V6
- 類型 / 層級 / 可信度：
  - Connecting Health & Learning：網站資料 / podcast transcript，Tier 2，可信度 medium
  - Self-Care Isn’t Selfish：網站資料 / podcast transcript，Tier 2，可信度 medium
  - Connecting Early Childhood Development to Climate Change：網站資料 / research brief，Tier 2，可信度 medium
- 新建來源摘要頁 3：
  - 09_來源摘要/Connecting_Health_and_Learning.md
  - 09_來源摘要/Self_Care_Isnt_Selfish.md
  - 09_來源摘要/Connecting_Early_Childhood_Development_to_Climate_Change.md
- 新建主題頁 2：
  - 07_Pediatric_Development/照顧者健康與兒童健康發展.md
  - 07_Pediatric_Development/氣候變遷與兒童發展.md
- 既有頁更新：
  - 07_Pediatric_Development/早期發展與終身健康.md
  - 07_Pediatric_Development/正向教養與家庭支持.md
  - 07_Pediatric_Development/發展環境與Place.md
  - index.md
- 明確標示的 conflict / caveat：
  1. `Connecting Health & Learning` 與既有 `Working Paper 15` 同方向，但它是 science-translation podcast，不可拿 lower-tier transcript 取代既有 Tier 1 framework。
  2. `Self-Care Isn’t Selfish` 修正「self-care = 奢侈或自我放縱」；在 pediatric development 脈絡裡，caregiver self-care 比較接近 buffering capacity maintenance。
  3. `Self-Care Isn’t Selfish` 的大量例子來自 COVID-era service delivery；可轉譯其 caregiver-health 原則，但不應把當時的 telehealth / pandemic workflow 當成永恆標準。
  4. `Connecting Early Childhood Development to Climate Change` 反對「climate 只影響未來成人」與「parents 自己保護就夠」兩種縮小框架；但它屬 communications brief，不是 pediatric climate guideline。
  5. climate 相關頁面目前 evidence base 仍以 Tier 2 synthesis / framing brief 為主，因此新建頁明確標為 `emerging`，未把它上調成 Tier 1 clinical consensus。
- index.md 更新：Total pages 336 -> 341
- 下一批待處理：
  - 無同批新候選殘留；本批新加入且同主題最相關文件已處理完畢

## [2026-05-01] correction | workflow restart baseline
- 修正原因：既有 `log.md` 含多次 batch ingest，與現行單一來源原則衝突。
- 本次決策：不刪除既有頁面；保留現況，改採 source-by-source correction 重新開始。
- 新增頁面：
  - 00_總覽/Workflow_重啟與校正基線_2026-05-01.md
- 結構修正：
  - 新增 `.agents/skills/feynman-euclidean-summary/SKILL.md`，與 `AGENTS.md` 指定路徑對齊。
- index.md 更新：
  - 新增 workflow 重啟入口。
  - 加入 restart baseline 提示。
- 待追蹤問題：
  - 過去 batch ingest 建立或大量更新的頁面需逐篇回到原始來源校正。
  - 低層級來源寫入臨床頁面的段落需重新分級。
- 待處理來源：
  - 尚未指定；下一輪依單一來源原則自 `C:\原始資料` 選一篇開始。

## [2026-05-01] correction | Barker, Cui, Kasitinon — The Physiatric History and Physical Examination
- 類型：textbook chapter（Tier 1）
- 修正原因：既有 `PMR_評估總論` 以多來源混合呈現；本輪改回單一來源拆解此 chapter 的核心輸出概念。
- 重新檢查來源：
  - `C:\原始資料\The physiatric history and physical examination\The physiatric history and physical examination.md`
- 新增頁面：
  - `02_方法學/PMR_醫療問題與功能問題清單.md`
- 更新頁面：
  - `09_來源摘要/The_physiatric_history_and_physical_examination.md`
  - `03_疾病與臨床主題/PMR_評估總論.md`
  - `index.md`
- 本輪抽出的直接事實：
  - physiatric H&P 的核心輸出是 `medical problem list + functional problem list`，用來驅動 management plan。
  - initial plan 應明確寫出 impairments、activity limitation、participation/community role dysfunction、relevant medical conditions 與 interdisciplinary goals。
  - functional history 至少涵蓋 mobility、ADLs、IADLs、communication、cognition、work、recreation。
  - psychosocial history 應主動納入 home environment、support system、sexuality、vocation、finances、psychological issues、spirituality。
- 明確標示的限制：
  - 這是 textbook framework，不是比較不同 documentation style 成效的研究。
  - EMR / billing / medicolegal 寫法有 institution-specific 差異，不可把章節格式當唯一標準。
- index.md 更新：
  - Total pages 342 -> 343
- 待處理來源：
  - `The Physiatric History and Physical Examination handbook`（同主題，但本輪未處理）

## [2026-05-01] correction | Shyu & Liang — The Physiatric History and Physical Examination (Handbook)
- 類型：handbook / quick reference（Tier 1）
- 新增頁面：`02_方法學/PMR_H&P_Bedside_Checklist.md`
- 抽出概念：handbook 的真正價值是把 PM&R 的 function-oriented H&P 轉成 bedside 順序，但輸出仍須回到 medical + functional problem list。

## [2026-05-01] correction | Delgado-Lebron et al. — Wheelchairs and Seating Systems
- 類型：textbook chapter（Tier 1）
- 新增頁面：`03_疾病與臨床主題/輪椅處方的四大目標.md`
- 抽出概念：wheelchair prescription 應同時滿足 posture、mobility、pressure management 與 participation，而不是先猜器材型號。

## [2026-05-01] correction | Chen, Kang — Assistive Technology and Environmental Control Devices
- 類型：textbook chapter（Tier 1）
- 新增頁面：`03_疾病與臨床主題/輔具匹配失敗的常見機制.md`
- 抽出概念：AT abandonment 常反映 user-fit、training、follow-up 與 environment mismatch，而不是單純 device 等級不足。

## [2026-05-01] correction | Hryvniak, Duncan, Jenkins — Therapeutic Exercise
- 類型：textbook chapter（Tier 1）
- 新增頁面：`02_方法學/治療性運動處方的最低必要欄位.md`
- 抽出概念：therapeutic exercise 若沒有 screening、FITT、specificity、progression 與族群調整，就還不是完整處方。

## [2026-05-01] correction | Saby, Zappaterra, Aragaki — Occupational Medicine and Vocational Rehabilitation
- 類型：textbook chapter（Tier 1）
- 新增頁面：`02_方法學/Return_to_Work_評估骨架.md`
- 抽出概念：RTW 判讀必須同時看 worker、job demand、employer / policy context 與 workplace modification。

## [2026-05-01] correction | Seidel, Swanson, Hampton — Practical Aspects of Impairment Rating and Disability Determination
- 類型：textbook chapter（Tier 1）
- 新增頁面：`02_方法學/Impairment與Disability的區分.md`
- 抽出概念：impairment rating 是 disability determination 的基石，但 disability 不是單一 impairment percentage 的直線外推。

## [2026-05-01] correction | Shahidullah, Hostutler, Baum — Interprofessional Team-Based Care
- 類型：textbook chapter（Tier 1）
- 新增頁面：`02_方法學/跨專業團隊的共享目標與角色清楚化.md`
- 抽出概念：多人照護若沒有 shared goals、role clarity 與 care coordination，並不等於真正的 team-based care。

## [2026-05-01] correction | Carter & Lewis — Psychological Assessment and Intervention in Rehabilitation
- 類型：textbook chapter（Tier 1）
- 新增頁面：`02_方法學/Disability_Adjustment_評估軸.md`
- 抽出概念：disability adjustment 是非線性 biopsychosocial process，評估不能只看情緒症狀本身。

## [2026-05-01] correction | Yang, Grover, Raval — Quality and Outcome Measures for Medical Rehabilitation
- 類型：textbook chapter（Tier 1）
- 新增頁面：`02_方法學/Outcome_Process_Performance_Measure_區分.md`
- 抽出概念：outcome、process、performance measure 回答不同問題；若混用，quality interpretation 會失真。

## [2026-05-01] correction | Seidel, Andary, Dillingham — Electrodiagnostic Medicine
- 類型：textbook chapter（Tier 1）
- 新增頁面：`02_方法學/EDX_轉介問題設計.md`
- 抽出概念：高品質 EDX 應先定義 clinical question，再決定 NCS / needle EMG 設計。

## [2026-05-01] correction | Francisco & Li — Spasticity
- 類型：textbook chapter（Tier 1）
- 新增頁面：`03_疾病與臨床主題/Spasticity與Contracture的區分.md`
- 抽出概念：臨床 stiffness 至少要分成 reflex hyperexcitability、weakness、co-contraction、contracture 與 peripheral stiffness。

## [2026-05-01] correction | Yochelson, Dennison, Kolarova — Stroke Rehabilitation
- 類型：textbook chapter（Tier 1）
- 新增頁面：`03_疾病與臨床主題/中風復健中的早期動員時機.md`
- 抽出概念：stroke early mobilization 不能脫離 subtype 與 hemodynamic stability，尤其 ICH first 24 hours 不是預設安全。

## [2026-05-01] correction | Wagner, Franzese, Weppner — Traumatic Brain Injury
- 類型：textbook chapter（Tier 1）
- 新增頁面：`03_疾病與臨床主題/TBI_意識障礙與神經行為管理.md`
- 抽出概念：severe TBI rehab 需要 structured assessment 去分清 disorders of consciousness 與 neurobehavioral complication。

## [2026-05-01] correction | Escalon, Marzloff, Bryce — Spinal Cord Injury
- 類型：textbook chapter（Tier 1）
- 新增頁面：`03_疾病與臨床主題/SCI_次級併發症風險框架.md`
- 抽出概念：SCI 的長期 morbidity / mortality 主軸是 pulmonary、autonomic、skin、bowel、bladder 等次級併發症。

## [2026-05-01] correction | Lovegreen, Murphy, Stevens — Lower Limb Amputation and Gait
- 類型：textbook chapter（Tier 1）
- 新增頁面：`03_疾病與臨床主題/下肢義肢_K_Level_處方邏輯.md`
- 抽出概念：K-level 是 prosthetic prescription 的骨架，但不能脫離 residual limb、skin、balance 與真實目標。

## [2026-05-01] correction | Hermansen, McKenty — Rehabilitation and Prosthetic Restoration in Upper Limb Amputation
- 類型：textbook chapter（Tier 1）
- 新增頁面：`03_疾病與臨床主題/上肢義肢匹配決策.md`
- 抽出概念：upper limb prosthetic prescription 是 category matching，不是 technology race。

## [2026-05-01] correction | Rodriguez, Goetz, Stiens — Neurogenic Bowel: Dysfunction and Rehabilitation
- 類型：textbook chapter（Tier 1）
- 新增頁面：`03_疾病與臨床主題/Bowel_Program_的社會性控便目標.md`
- 抽出概念：NBD bowel program 的成功標準是可預測、可接受、time-efficient 的 social continence。

## [2026-05-01] correction | Goetz & Klausner — Neurogenic Lower Urinary Tract Dysfunction
- 類型：textbook chapter（Tier 1）
- 新增頁面：`03_疾病與臨床主題/NLUTD_腎臟保護優先原則.md`
- 抽出概念：NLUTD 先保護 upper tract；symptom 與 PVR 都不能取代對高壓 bladder 的警覺。

## [2026-05-01] correction | Singer, Aihara, Gonzalez-Fernandez — Rehabilitation of Swallowing Disorders
- 類型：textbook chapter（Tier 1）
- 新增頁面：`03_疾病與臨床主題/吞嚥篩檢與Instrumental_Assessment的角色分工.md`
- 抽出概念：screening、CSE、VFSS 與 FEES 位在同一條 dysphagia decision chain 的不同節點，不能互相替代。

## [2026-05-01] correction | Lew, Hall, Gustafson — Auditory, Vestibular, and Visual Impairments
- 類型：textbook chapter（Tier 1）
- 新增頁面：`03_疾病與臨床主題/雙重感覺障礙與復健參與.md`
- 抽出概念：dual sensory impairment 會明顯放大 communication、balance、self-care 與 safety burden，進而壓低 rehab participation。

## [2026-05-01] update | index after 20 sequential single-source runs
- index.md 更新：Total pages 343 -> 363
- 本輪新增頁面：20
- 本輪方法：每次只處理一篇來源，直接落成單一概念頁，不做未標示的跨來源混寫。

## [2026-05-01] correction | Examination of the Pediatric Patient
- 類型：textbook chapter（Tier 1）
- 新增頁面：`07_Pediatric_Development/Play_Based_Pediatric_Examination.md`
- 抽出概念：pediatric exam 從 observation 就開始；play、engagement、language 與 motor pattern 本身就是 exam。

## [2026-05-01] correction | Developmental-behavioral surveillance and screening in primary care
- 類型：UpToDate / topic review（Tier 1）
- 新增頁面：`07_Pediatric_Development/Surveillance與Screening的區分.md`
- 抽出概念：surveillance 是 routine responsibility，screening 是 standardized risk detection；兩者都不能取代 evaluation。

## [2026-05-01] correction | Developmental and Behavioral Surveillance and Screening
- 類型：textbook chapter / review（Tier 1）
- 新增頁面：`07_Pediatric_Development/Primary_Care_Developmental_Surveillance_流程.md`
- 抽出概念：developmental surveillance 是每次健康檢查持續進行的 workflow，不是一次量表。

## [2026-05-01] correction | Feeding and Swallowing Disorders
- 類型：textbook chapter（Tier 1）
- 新增頁面：`07_Pediatric_Development/兒童餵食問題的生理與行為分流.md`
- 抽出概念：pediatric feeding problem 要先分 feeding 與 swallowing，再分 physiologic 與 mealtime-experiential 問題。

## [2026-05-01] correction | Infancy
- 類型：textbook chapter（Tier 1）
- 新增頁面：`07_Pediatric_Development/嬰兒期的狀態調節與互動評估.md`
- 抽出概念：infancy 的核心是 state regulation、attachment、joint attention、play 與 adversity buffer 的同步組裝。

## [2026-05-01] correction | Toddlerhood and the Preschool Years
- 類型：textbook chapter（Tier 1）
- 新增頁面：`07_Pediatric_Development/學齡前期的自我調節與school_readiness.md`
- 抽出概念：school readiness 不只是 preacademic skill，而是 language、regulation、social reciprocity 與 adaptive participation 的整體成熟度。

## [2026-05-01] correction | Middle Childhood
- 類型：textbook chapter（Tier 1）
- 新增頁面：`07_Pediatric_Development/學齡期的同儕歸屬與自我概念.md`
- 抽出概念：middle childhood 的核心任務是 school adaptation、peer belonging、self-regulation 與 self-concept 的同步重組。

## [2026-05-01] correction | Developmental Delay and Intellectual Disability
- 類型：textbook chapter / review（Tier 1）
- 新增頁面：`07_Pediatric_Development/Developmental_Delay_的鑑別起點.md`
- 抽出概念：GDD 是 early-life descriptive diagnosis；鑑別起點要看 adaptive function、軌跡與 regression。

## [2026-05-01] correction | Language and Speech Disorders
- 類型：textbook chapter / review（Tier 1）
- 新增頁面：`07_Pediatric_Development/Speech_Disorder與Language_Disorder的區分.md`
- 抽出概念：晚講話不能只看字數；至少要分 comprehension、expression、play、hearing 與 broader differential。

## [2026-05-01] correction | Language Development and Communication Disorders
- 類型：textbook chapter（Tier 1）
- 新增頁面：`07_Pediatric_Development/兒童語言障礙的臨床分流.md`
- 抽出概念：language disorder 評估要分 phonology、lexicon、syntax、pragmatics、bilingualism 與 disorder differential。

## [2026-05-01] correction | Developmental Considerations in Deafness
- 類型：textbook chapter / review（Tier 1）
- 新增頁面：`07_Pediatric_Development/聽損兒童的發展脈絡評估.md`
- 抽出概念：deaf child outcome 取決於早期辨識、持續 monitoring、家庭支持與 language access，不只看分貝數。

## [2026-05-01] correction | Blindness and Visual Impairment
- 類型：textbook chapter（Tier 1）
- 新增頁面：`07_Pediatric_Development/視覺障礙兒童的功能評估重點.md`
- 抽出概念：pediatric visual impairment 評估需同時看 ocular、optic pathway 與 CVI，而不是只找 refractive error。

## [2026-05-01] correction | Consequences of Preterm Birth
- 類型：textbook chapter（Tier 1）
- 新增頁面：`07_Pediatric_Development/早產兒的長期神經發展風險.md`
- 抽出概念：preterm birth 的長期結局不只 CP；motor、language、learning、behavior 與 sensory 問題有不同浮現時序。

## [2026-05-01] correction | Early Intervention
- 類型：textbook chapter / systems review（Tier 1）
- 新增頁面：`07_Pediatric_Development/Early_Intervention_的時機與核心目標.md`
- 抽出概念：EI 是把發展支持嵌入 child 與 family daily routine 的系統，而不是一張轉介單。

## [2026-05-01] correction | Trauma, Resilience, and Child Development
- 類型：textbook chapter（Tier 1）
- 新增頁面：`07_Pediatric_Development/創傷復原中的保護因子框架.md`
- 抽出概念：child trauma 的結果取決於 trauma 類型、累積 adversity 與 supportive relationship 等保護系統。

## [2026-05-01] correction | Foster Care and Adoption
- 類型：textbook chapter（Tier 1）
- 新增頁面：`07_Pediatric_Development/Foster_Care_的發展風險框架.md`
- 抽出概念：foster care / adoption 的臨床重點是 preadoptive adversity、transition、postadoptive support 與 identity development。

## [2026-05-01] correction | Child Care
- 類型：textbook chapter（Tier 1）
- 新增頁面：`07_Pediatric_Development/Child_Care_品質與發展結果.md`
- 抽出概念：child care 重要的不只是有沒有位子，而是 quality、health-safety integration 與 inclusion。

## [2026-05-01] correction | Celebrating Sociocultural Diversity in the Exam Room and Addressing Racism and Bias
- 類型：textbook chapter（Tier 1）
- 新增頁面：`07_Pediatric_Development/診間中的文化敏感性與偏誤辨識.md`
- 抽出概念：cultural humility、bias awareness 與 structural competency 都應被視為 developmental encounter 的臨床工具。

## [2026-05-01] correction | The Influence of Digital Media on Children and Families
- 類型：textbook chapter（Tier 1）
- 新增頁面：`07_Pediatric_Development/數位媒體對兒童發展的風險分層.md`
- 抽出概念：digital media 風險不只看時數，還要看 content、context、parent mediation 與 displacement effect。

## [2026-05-01] correction | Exercise textbook chapter
- 類型：textbook chapter（Tier 1）
- 新增頁面：`05_Exercise_Physiology/運動時氧供調節的整合視角.md`
- 抽出概念：external power 增加時，VO2、cardiac output、oxygen extraction 與 ventilation 必須同步上調；VO2 不是只代表 lungs。

## [2026-05-01] update | index after second 20 sequential single-source runs
- index.md 更新：Total pages 363 -> 383
- 本輪新增頁面：20
- 本輪方法：每次只處理一篇來源，直接落成單一概念頁，不做未標示的跨來源混寫。

## [2026-05-01] correction | Developmental Considerations in Deafness
- 類型：textbook chapter（Tier 1）
- 修正方式：本輪只讀這一篇來源，但依內容密度拆成多個單一概念頁。
- 更新頁面：
  - `09_來源摘要/Developmental_Considerations_in_Deafness.md`
  - `07_Pediatric_Development/兒童聽覺障礙與Deafness.md`
  - `07_Pediatric_Development/聽損兒童的發展脈絡評估.md`
  - `index.md`
- 新增頁面：
  - `07_Pediatric_Development/新生兒聽力篩檢之後的持續監測.md`
  - `07_Pediatric_Development/Language_Access_作為聽損介入核心.md`
  - `07_Pediatric_Development/發展障礙兒童的聽損遮蔽效應.md`
  - `07_Pediatric_Development/依發展年齡選擇兒童聽力測試.md`
- 本輪抽出的直接事實：
  - newborn hearing screen 只是起點，不排除 delayed-onset 或 progressive hearing loss。
  - cCMV 與 NICU / hyperbilirubinemia / ototoxic exposure 等風險因子需進入後續 surveillance。
  - deaf child 的介入核心是 language access，不是單純 speech-only framing。
  - intellectual disability、CP、ASD、Down syndrome 等族群的 hearing issue 容易被主診斷遮蔽。
  - audiologic evaluation 與認知 / 語言 assessment 都應依 developmental age 與 deaf-informed principle 選工具。
- index.md 更新：
  - Total pages 383 -> 387

## [2026-05-01] correction | Murano, Sawyer, Lipnevich — A Meta-Analytic Review of Preschool Social and Emotional Learning Interventions
- 類型：meta-analysis（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Murano-et-al-2020-preschool-SEL-interventions-copy\Murano-et-al-2020-preschool-SEL-interventions-copy.md`
- 新增頁面：
  - `09_來源摘要/Murano_2020_preschool_SEL_interventions.md`
  - `07_Pediatric_Development/學前SEL介入的分層與情境堆疊.md`
- 更新頁面：
  - `07_Pediatric_Development/學齡前期的自我調節與school_readiness.md`
  - `07_Pediatric_Development/正向教養與家庭支持.md`
  - `index.md`
- 本輪抽出的直接事實：
  - preschool universal SEL 對 social and emotional skills 與 problem behavior 有 small-to-medium overall benefit（grand mean `g = .35`）。
  - targeted SEL 對 at-risk preschoolers 的 overall benefit 較大（grand mean `g = .48`；problem behavior `g = .50`）。
  - 在 universal programs 中，at-risk samples 的 effect size 較小（`g = .21`）than non-at-risk samples（`g = .29`）。
  - intervention program type 解釋 universal effect heterogeneity 的大部分（`R2 = .83`）；`SEL` 不是單一可互換 treatment label。
  - universal preschool SEL 中，parent + teacher、home + school 的情境堆疊效果高於 teacher-only school delivery（`g = .53` vs `g = .28`）。
- 明確標示的限制：
  - program 間比較來自 observational moderator analysis，不能做直接 causal ranking。
  - combined universal analysis 有 publication bias 訊號；trim-and-fill 後 true effect CI 含 0。
  - 多數 cluster-randomized primary study 缺 ICC，部分 effect size 無法完整校正。
- index.md 更新：
  - Total pages 387 -> 389
- 待處理來源：
  - `Child Psychology Psychiatry - 2023 - Nelson - Annual Research Review  Early intervention viewed through the lens of developmental neuroscience`

## [2026-05-01] ingest | Nelson, Sullivan, Engelstad — Annual Research Review: Early intervention viewed through the lens of developmental neuroscience
- 類型：Annual Research Review / high-quality narrative review（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Child Psychology Psychiatry - 2023 - Nelson - Annual Research Review  Early intervention viewed through the lens of\Child Psychology Psychiatry - 2023 - Nelson - Annual Research Review  Early intervention viewed through the lens of.md`
- 新增來源摘要：
  - `09_來源摘要/Nelson_2023_early_intervention_developmental_neuroscience.md`
- 更新頁面：
  - `07_Pediatric_Development/Early_Intervention_的時機與核心目標.md`
  - `index.md`
- 新增頁面：
  - `07_Pediatric_Development/經驗期待型發展與早期介入窗口.md`
  - `07_Pediatric_Development/Caregiving_Quality_作為早期介入靶點.md`
- 發現衝突：
  - early intervention timing 不能被簡化成單一 universal age cutoff。
  - caregiving quality 是重要靶點，但不是 culture-free checklist。
  - early autism biomarker 目前不足以作 individual clinical use。
  - critical period reopening 仍屬 research implication，不能直接寫成 routine care。
- 待追蹤問題：
  - 可另以單一來源建立 adolescent / late intervention window 的獨立概念頁。
  - autism early intervention 的 connectivity framing 可再拆成單一概念頁。
- 待處理來源：
  - 無；下一輪重新依候選與主題缺口排序。

## [2026-05-01] ingest | Roge, Levin, Tsao — Cerebral Palsy
- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Cerebral palsy\Cerebral palsy.md`
- 新增來源摘要：
  - `09_來源摘要/Cerebral_Palsy.md`
- 更新頁面：
  - `07_Pediatric_Development/Cerebral_Palsy_總論.md`
  - `07_Pediatric_Development/CP_早期辨識與診斷.md`
  - `07_Pediatric_Development/CP_功能分類系統.md`
  - `index.md`
- 新增頁面：
  - `07_Pediatric_Development/CP_成人轉銜與老化風險.md`
- 本輪抽出的直接事實：
  - GMA 在 fidgety period 對 2 歲時 CP 的預測力最高，sensitivity 約 95%–100%，specificity 約 89%–98%，最佳評估時間約 12–14 週 corrected age。
  - HINE 在 3 個月 corrected age <57/78 時，對 CP 有 high sensitivity（90%–96%）與 specificity（85%–87%）；<5 個月 corrected age 以 GMA + HINE + MRI predictive validity 最佳。
  - CP 的 function description 不應只寫 GMFCS；本章同時納入 MACS、CFCS、EDACS、VFCS，並以 ICF-CY 補上 activity / participation / environment / personal context。
  - positive ambulation predictor 包括 2 歲前可獨坐、18–24 個月 primitive reflex 少於 3 個、且 absence of visual impairment、intellectual disability、epilepsy。
  - adult CP population 有較高 stroke、myelopathy、dementia、chronic pain、fatigue、depression 與 mobility decline 風險。
- 發現衝突：
  - CP 雖是 nonprogressive disturbance of the developing brain，但 functional decline 與 medical burden 仍可隨生命期累積。
  - higher GMFCS 常伴隨較重共病，但 pain 橫跨所有 disability levels，behavior disorder 反而較常見於較 mild motor disability。
  - imaging 正常或不典型時，仍需考慮 genetic / metabolic mimic，不能單靠 MRI 排除 CP phenotype。
- 待追蹤問題：
  - 可再用單一來源把 CP 的 feeding / pulmonary risk 或 multisystem comorbidity 拆成獨立概念頁。
  - genetic testing 在 CP diagnostic evaluation 的一線 vs 二線定位，之後需要另外用 guideline / review 補強。
- 待處理來源：
  - 無；下一輪重新依候選與主題缺口排序。

## [2026-05-01] ingest | Miller, White, Klamar — Myelomeningocele and Other Spinal Dysraphisms
- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Myelomeningocele and other spinal dysraphisms\Myelomeningocele and other spinal dysraphisms.md`
- 新增來源摘要：
  - `09_來源摘要/Myelomeningocele_and_other_spinal_dysraphisms.md`
- 更新頁面：
  - `index.md`
- 新增頁面：
  - `07_Pediatric_Development/Myelomeningocele_總論.md`
  - `07_Pediatric_Development/MMC_胎兒修補與功能結果.md`
  - `07_Pediatric_Development/MMC_水腦分流與Chiari_II警訊.md`
  - `07_Pediatric_Development/MMC_運動神經功能層級與步行預後.md`
  - `07_Pediatric_Development/MMC_神經性膀胱與腎功能保護.md`
- 本輪抽出的直接事實：
  - fetal ultrasound 是 prenatal MMC diagnosis 的 gold standard，通常在 18–22 週 gestation；maternal serum AFP 在 15–22 週對 open NTD 的 detection rate 約 65%–80%。
  - MOMS trial 中，prenatal repair（<26 週）相較 postnatal repair 可降低 Arnold-Chiari II presence（64% vs 96%）與 shunt placement（40% vs 82%），並改善 motor function 與 independent ambulation。
  - school-age follow-up 顯示 prenatal group 仍有較佳 mobility、ADL 與較低 CIC rate（61.5% vs 87.2%），但 tethered cord release 更常見（27% vs 15%）。
  - MMC hydrocephalus 只有約 10% 在出生時就 clinically obvious，但 85% 會在第一週內表現；symptomatic Chiari II 的 stridor 是 threatened airway sign。
  - up to 98% of children with lumbosacral MMC 有 neurogenic bladder；renal/bladder ultrasound、urodynamics、serum creatinine 應於出生後 3 個月內建立 baseline。
- 發現衝突：
  - prenatal MMC repair 改善多項 child-centered outcome，但同時增加 prematurity、placental / membrane complication 與 maternal hysterotomy risk，不能被寫成無代價升級版。
  - fluent verbal language 會讓人高估 MMC child 的 cognition 與 adaptive understanding；語言表面流暢不等於 neuropsychological intact。
  - OCR 文字多次出現不合理的 `folic acid 400 mg` 一般族群劑量；本輪只保留 folate 對 NTD prevention 的定性角色，不採納該精確數字。
- 待追蹤問題：
  - 可再用單一來源拆出 `MMC_神經性腸道管理`、`MMC_神經心理與school planning`、或 `adult spina bifida transition` 的獨立概念頁。
  - pediatric neuro-urology surveillance interval 與 medication sequencing 之後需要另外用 guideline / review 補強。
- 待處理來源：
  - 無；下一輪重新依候選與主題缺口排序。

## [2026-05-03] ingest | Ackerman et al. — Traumatic Spinal Cord Injury

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Traumatic Spinal Cord Injury\Traumatic Spinal Cord Injury.md`
- 新增來源摘要：
  - `09_來源摘要/Traumatic_Spinal_Cord_Injury.md`
- 新增頁面：
  - `03_疾病與臨床主題/Traumatic_SCI_急性處置與復健銜接.md`
  - `03_疾病與臨床主題/SCI_共病TBI與運動學習調整.md`
- 更新頁面：
  - `03_疾病與臨床主題/脊髓損傷復健總論.md`
  - `03_疾病與臨床主題/SCI_次級併發症風險框架.md`
  - `index.md`
- 本輪抽出的直接事實：
  - Acute traumatic SCI management 包含 airway / resuscitation、selective immobilization、rapid transport、MAP maintenance、CT / MRI indication、realignment、stabilization / decompression 與早期 rehabilitation planning。
  - 本來源指出 steroids are not recommended routinely；僅在 injury 後 8 小時內特定情境考慮。
  - Complete SCI 必須以 S4-S5 sacral sparing、deep anal pressure 與 voluntary anal contraction 判斷，不能用「下肢不能動」取代 ISNCSCI/AIS。
  - Co-occurring TBI 在 spinal injury 中估計約 32.5%，cervical level 約 40.4%，若加入 LOC / PTA 等因素報告率會上升；未辨識時可能被誤解為 noncompliance 或 poor motivation。
  - 約 70% SCI inpatient rehab 期間至少出現一項 nonneurological complication / secondary condition；C1-C4 injury 風險約 2.2 倍。
  - High cervical SCI respiratory complication 風險約 3.3 倍；mechanism 包含 ventilatory muscle weakness、weak cough、secretion retention、atelectasis 與 aspiration risk。
  - SCI first-year UTI incidence 來源報告約 62%；voiding method 會影響 risk，indwelling catheter 最高，volitional voiding 較低。
  - Incomplete SCI >6 months post injury 且已能走者，來源引用的 locomotor CPG 支持 high-intensity gait training，且不建議把 exoskeletal robotics 作為 gait training 預設方法。
- 發現衝突：
  - 「SCI 復健等急性期結束再開始」不符合本來源；來源把 rehabilitation 放在 acute / critical-care stage 即啟動。
  - 「walking recovery 是主要成功指標」過窄；來源更重視 ADL、wheelchair/seating、transfer、equipment、community reintegration 與 quality of life。
  - 「technology 本身造成 recovery」過度簡化；來源強調 technology 只有在 active participation、specificity、repetition、intensity 與 salience 下才可能放大訓練效果。
- 待追蹤問題：
  - 可另用單一來源補強 traumatic SCI 的 guideline-level steroid / MAP / decompression recommendation，避免 textbook chapter 與 guideline 更新不同步。
  - 可再拆出 `SCI_輪椅座位與壓力管理` 或 `SCI_心代謝健康與運動處方` 的單一概念頁。
- 待處理來源：
  - `C:\原始資料\Pain Management\Pain Management.md`
  - `C:\原始資料\pain management Bradley and Daroff's Neurology in Clinical Practice, 52, 753-775.e2\pain management Bradley and Daroff's Neurology in Clinical Practice, 52, 753-775.e2.md`
  - `C:\原始資料\Upper limb pain and dysfunction\Upper limb pain and dysfunction.md`

## [2026-05-03] ingest | Burke-Doe & Johnson — Pain Management

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Pain Management\Pain Management.md`
- 新增來源摘要：
  - `09_來源摘要/Pain_Management.md`
- 新增頁面：
  - `03_疾病與臨床主題/疼痛管理_Biopsychosocial_ICF框架.md`
  - `03_疾病與臨床主題/疼痛評估_OPQRST與多維度量測.md`
  - `03_疾病與臨床主題/慢性疼痛復健的主動化治療框架.md`
- 更新頁面：
  - `02_方法學/復健心理社會評估與介入.md`
  - `02_方法學/物理因子治療.md`
  - `index.md`
- 本輪抽出的直接事實：
  - Pain 是 sensory and emotional experience，不可只用 tissue damage 或 intensity 解釋。
  - Chronic pain 約影響 21% US adults；high-impact chronic pain 約 8%。
  - 來源將 biopsychosocial model 視為理解 pain variability 的 model of choice，並以 ICF 組織 impairment、activity limitation、participation restriction。
  - Pain experience 包含 perceptual、affective、cognitive、behavioral components。
  - Pain history 可用 OPQRST 結構化，且 visceral symptoms 需在 therapist-led treatment 前轉醫師評估。
  - IMMPACT chronic pain outcome domains 包含 pain、physical functioning、emotional functioning、participant improvement / satisfaction、symptoms / adverse events、participant disposition。
  - PROMIS-29 可同時看 depression、anxiety、physical function、pain interference、fatigue、sleep disturbance、social roles / activities 與 NPRS。
  - Chronic pain treatment 不應限於 medical model 或 passive modality；來源將 intervention 分為 physical interventions、cognitive strategies、behavioral manipulations。
- 發現衝突：
  - 「Pain score 就是 pain assessment」不成立；intensity 只是一個維度。
  - 「Biopsychosocial 等於疼痛是心理問題」不成立；它是 biological、psychological、social 的整合 formulation。
  - 「Passive modalities 做久一點就是完整 pain rehab」不成立；來源明確指出 long-term passive use may promote dependence。
- 待追蹤問題：
  - Bradley and Daroff 的神經痛章可作下一輪單一來源，補強 central / peripheral neuropathic pain 與 pharmacologic / neurologic framing。
  - 可另用 guideline-level 來源補 opioid、interventional procedure 與 CRPS 診斷/治療建議。
- 待處理來源：
  - `C:\原始資料\pain management Bradley and Daroff's Neurology in Clinical Practice, 52, 753-775.e2\pain management Bradley and Daroff's Neurology in Clinical Practice, 52, 753-775.e2.md`
  - `C:\原始資料\Upper limb pain and dysfunction\Upper limb pain and dysfunction.md`

## [2026-05-03] ingest | Bradley and Daroff — Pain Management

- 類型：neurology textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\pain management Bradley and Daroff's Neurology in Clinical Practice, 52, 753-775.e2\pain management Bradley and Daroff's Neurology in Clinical Practice, 52, 753-775.e2.md`
- 新增來源摘要：
  - `09_來源摘要/Bradley_Daroff_Pain_Management.md`
- 新增頁面：
  - `03_疾病與臨床主題/慢性疼痛中的Peripheral與Central_Sensitization.md`
  - `03_疾病與臨床主題/神經痛藥物治療框架.md`
  - `03_疾病與臨床主題/CRPS_臨床辨識與治療限制.md`
- 更新頁面：
  - `index.md`
- 本輪抽出的直接事實：
  - Chronic pain 可超過正常 healing，失去 protective role，並形成 disease state。
  - A-delta fibers 傳遞 fast, sharp, well-localized pain；C fibers 傳遞 dull, burning, aching, poorly localized pain。
  - Small-fiber neuropathy 可有 neuropathic pain 但 routine nerve conduction studies 正常。
  - Neuronal plasticity 包含 wind-up、central sensitization 與 longer-term gene alteration。
  - TCA 與 anticonvulsants 是來源中的 neuropathic pain first-line options；SNRI 也有 analgesic evidence。
  - Chronic nonmalignant pain 的 long-term opioid 使用具 tolerance、dependence、addiction、opioid-induced hyperalgesia 風險。
  - CRPS type I 無 definable nerve lesion；type II 有 definable nerve lesion；診斷以 clinical pattern and exclusion of mimics 為主。
- 發現衝突：
  - 「組織癒合後仍痛就是裝痛」不成立；sensitization 可讓 pain 與 tissue injury 不成比例。
  - 「神經痛下一步就是 opioid」不符合本來源；adjuvant analgesics 是較前線策略。
  - 「EMG/NCS 正常排除 CRPS」不成立；來源指出 EMG/NCS 對 CRPS 不敏感。
- 待追蹤問題：
  - Opioid、CRPS diagnosis / treatment、SCS 與 ketamine 需用 guideline / systematic review 補強。
  - Trigeminal neuralgia、poststroke pain、SCI pain、phantom limb pain 可再拆成獨立單一概念頁。
- 待處理來源：
  - `C:\原始資料\Upper limb pain and dysfunction\Upper limb pain and dysfunction.md`
  - `C:\原始資料\Common neck problems\Common neck problems.md`
  - `C:\原始資料\Low back disorders\Low back disorders.md`
  - `C:\原始資料\Chronic pain\Chronic pain.md`

## [2026-05-03] ingest | Baria & Laskowski — Upper Limb Pain and Dysfunction

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Upper limb pain and dysfunction\Upper limb pain and dysfunction.md`
- 新增來源摘要：
  - `09_來源摘要/Upper_Limb_Pain_and_Dysfunction.md`
- 新增頁面：
  - `03_疾病與臨床主題/上肢疼痛與功能障礙評估總論.md`
  - `03_疾病與臨床主題/Rotator_Cuff_Tendon_Disease.md`
  - `03_疾病與臨床主題/上肢急性肌腱與腕韌帶轉介紅旗.md`
- 更新頁面：
  - `index.md`
- 本輪抽出的直接事實：
  - Upper extremity pathology 必須放在 kinetic chain 內判讀。
  - Rehabilitation staging 包含 acute、recovery、functional stages。
  - Rotator cuff disease 包含 tendinopathy、partial tear、chronic full-thickness tear、acute traumatic full-thickness tear。
  - Tendinopathy、partial tear、chronic full-thickness tear 多先以 nonsurgical rehabilitation 處理；acute traumatic full-thickness tear 需 prompt MRI and surgical consult。
  - 來源列出 acute full-thickness rotator cuff tear、pectoralis major tear、distal biceps tear、scaphoid fracture、scapholunate dissociation 需 early surgical referral。
  - Scapholunate injury missed 可進展至 DISI 與 SLAC wrist。
- 發現衝突：
  - 「肩痛都是 rotator cuff tendinitis」不成立；spectrum 與 chronicity 會改變 referral urgency。
  - 「上肢疼痛只看痛點」不符合來源；kinetic chain、compensation、task demand 都會改變治療。
  - 「所有上肢扭拉傷都可先復健數週」不成立；time-sensitive rupture / instability 需及早轉介。
- 待追蹤問題：
  - Adhesive capsulitis、lateral epicondylosis、olecranon bursitis、de Quervain、TFCC 可再分別建立單一概念頁。
  - 急性 scaphoid fracture 與 hand surgery referral criteria 需另用 guideline 或 specialty source 補強。
- 待處理來源：
  - `C:\原始資料\Common neck problems\Common neck problems.md`
  - `C:\原始資料\Low back disorders\Low back disorders.md`
  - `C:\原始資料\Chronic pain\Chronic pain.md`

## [2026-05-03] ingest | DePalma & Ishigami — Common Neck Problems

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Common neck problems\Common neck problems.md`
- 新增來源摘要：
  - `09_來源摘要/Common_Neck_Problems.md`
- 新增頁面：
  - `03_疾病與臨床主題/頸部疼痛評估總論.md`
  - `03_疾病與臨床主題/Cervical_Radiculopathy.md`
  - `03_疾病與臨床主題/Cervical_Myelopathy_紅旗.md`
- 更新頁面：
  - `index.md`
- 本輪抽出的直接事實：
  - Neck pain 需分 axial cervical pain、somatic referred pain、radicular pain、radiculopathy 與 myelopathy。
  - Nonneural cervical structures 可透過 convergence 造成 head / upper limb referral。
  - Cervical radicular pain 與 radiculopathy 不同；radiculopathy 需要 myotomal weakness、sensory disturbance、paresthesia 或 depressed reflex 等 neurophysiologic dysfunction。
  - MRI 是 gold standard，但 asymptomatic abnormalities common，需 clinical correlation。
  - Spurling test highly specific but not sensitive。
  - Cervical myelopathy 可表現為 gait disturbance、UMN signs、hand dysfunction、proprioceptive deficit、bladder change。
- 發現衝突：
  - 「手麻就是 cervical radiculopathy」不成立；somatic referred pain、peripheral nerve、plexus、myelopathy 都需鑑別。
  - 「MRI 有 stenosis 就是病因」不成立；影像需與症狀、exam、EDX 對齊。
  - 「myelopathy 可先做 traction 試試」不符合來源；myelopathy 是 traction contraindication。
- 待追蹤問題：
  - Cervical injection、RFA、surgery timing 需用 current guideline / safety statement 補強。
  - Whiplash 與 cervicogenic headache 可另拆單一概念頁。
- 待處理來源：
  - `C:\原始資料\Low back disorders\Low back disorders.md`
  - `C:\原始資料\Chronic pain\Chronic pain.md`

## [2026-05-03] ingest | Pangarkar et al. — Low Back Disorders

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Low back disorders\Low back disorders.md`
- 新增來源摘要：
  - `09_來源摘要/Low_Back_Disorders.md`
- 新增頁面：
  - `03_疾病與臨床主題/下背痛評估總論.md`
  - `03_疾病與臨床主題/下背痛影像與Red_Flags.md`
  - `03_疾病與臨床主題/Lumbosacral_Radiculopathy.md`
  - `03_疾病與臨床主題/Lumbar_Spinal_Stenosis.md`
- 更新頁面：
  - `index.md`
- 本輪抽出的直接事實：
  - Acute LBP 為 0-4 weeks，subacute 4-12 weeks，chronic >12 weeks。
  - 大多數 acute LBP 預後佳；來源指出 75-90% 在 3-4 週內 recover / return to work。
  - 約 85% care-seeking LBP 為 nonspecific LBP。
  - Acute uncomplicated LBP 不建議 routine MRI；早期 MRI 與較高手術、成本、opioid use、較差 pain 相關。
  - Red flags 是 triage signal，不是 serious pathology 的證明；absence 也不能完全排除 malignancy。
  - Radicular pain 可由 chemical inflammation 驅動，不只是 mechanical compression。
  - Lumbar spinal stenosis 的 clinical core 是 neurogenic claudication，extension / walking 加重、sitting / flexion 改善。
- 發現衝突：
  - 「LBP 先 MRI」不符合本來源；imaging 需有 actionable question。
  - 「disc bulge 就是 pain source」不成立；asymptomatic abnormalities common。
  - 「sciatica 一定是神經被壓到」不完整；inflamed root 可造成 pain。
- 待追蹤問題：
  - Facet-mediated pain、discogenic pain、MBR、ESI、surgery threshold 需另外用 single-source workflow 補強。
  - Red flags 的 diagnostic accuracy 可用 guideline / systematic review 補充。
- 待處理來源：
  - `C:\原始資料\Chronic pain\Chronic pain.md`

## [2026-05-03] ingest | Pham et al. — Chronic Pain

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Chronic pain\Chronic pain.md`
- 新增來源摘要：
  - `09_來源摘要/Chronic_Pain.md`
- 新增頁面：
  - `03_疾病與臨床主題/Nociceptive_Neuropathic_Nociplastic_Pain.md`
  - `03_疾病與臨床主題/慢性疼痛的CBT_CP與Pacing.md`
  - `03_疾病與臨床主題/慢性疼痛Opioid與Buprenorphine風險框架.md`
- 更新頁面：
  - `03_疾病與臨床主題/疼痛管理_Biopsychosocial_ICF框架.md`
  - `03_疾病與臨床主題/疼痛評估_OPQRST與多維度量測.md`
  - `03_疾病與臨床主題/慢性疼痛復健的主動化治療框架.md`
  - `index.md`
- 本輪抽出的直接事實：
  - Chronic pain 在來源中定義為至少 3 個月且超過 normal healing。
  - Pain 可分 nociceptive、neuropathic、nociplastic，且可 overlap。
  - Nociplastic pain 是 altered nociception despite no clear tissue damage / nociceptor activation or somatosensory lesion。
  - CBT-CP improves function, mood, and pain interference；components 包含 physical activity、time-based pacing、relaxation、pleasant activity scheduling、sleep education、cognitive coping。
  - Prolonged rest is not beneficial for chronic pain；exercise / movement therapy 可改善 pain severity、function、QOL。
  - Long-term opioid harms 包含 adrenal insufficiency、respiratory depression、sex hormone disruption、osteoporosis、bowel dysfunction、opioid-induced hyperalgesia、immunosuppression、misuse、dependence、OUD。
  - Buprenorphine 是 partial agonist with ceiling effect and lower overdose risk；Belbuca / Butrans 為 chronic pain FDA-approved formulations。
- 發現衝突：
  - 「Nociplastic pain 等於 psychogenic pain」不成立；它是 altered nociception。
  - 「CBT-CP 是否定疼痛」不成立；它處理 thoughts、emotions、behaviors 與 pain interference 的 loop。
  - 「opioid 有風險所以應立即停藥」不成立；來源明確反對 abrupt discontinuation / rapid taper unless life-threatening overdose concern。
- 待追蹤問題：
  - Opioid taper、buprenorphine transition、OUD diagnosis、cannabis / CBD / benzodiazepine interaction 需用 current prescribing source 補強。
  - Pain bias、placebo / nocebo、sleep / CBT-I 可再拆單一概念頁。
- 待處理來源：
  - `C:\原始資料\Peripheral nerve disorders\Peripheral nerve disorders.md`

## [2026-05-03] ingest | Barnes, Craig, Hearn — Peripheral Nerve Disorders

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Peripheral nerve disorders\Peripheral nerve disorders.md`
- 新增來源摘要：
  - `09_來源摘要/Peripheral_Nerve_Disorders.md`
- 新增頁面：
  - `03_疾病與臨床主題/周邊神經損傷分類與恢復機制.md`
  - `03_疾病與臨床主題/周邊神經病灶定位與EDX_US框架.md`
  - `03_疾病與臨床主題/周邊多發神經病變_典型與非典型型態.md`
- 更新頁面：
  - `02_方法學/電生理診斷醫學.md`
  - `index.md`
- 本輪抽出的直接事實：
  - Seddon classification 分 neurapraxia、axonotmesis、neurotmesis；Sunderland classification 進一步依 connective tissue layer 損傷分級。
  - EDX 可評估 axonal continuity，但不能直接評估 supportive connective tissue integrity。
  - Wallerian degeneration 約 7 天影響 motor axon、約 10 天影響 sensory axon；denervation potentials 通常約 3 週後才出現。
  - Recovery mechanism 包含 remyelination、collateral sprouting、axonal regrowth；axonal regrowth 約 1-5 mm/day，reinnervation viability 約 18-24 個月。
  - Neuromuscular ultrasound 可補 EDX 的 structural gap，尤其是 early trauma、focal compression、nerve discontinuity、postoperative persistent symptoms。
  - Typical polyneuropathy 多為 chronic、length-dependent、symmetric、axonal、sensory-motor pattern；非典型 pattern 需考慮 inflammatory、nutritional、toxic、infectious、vasculitic、hereditary 等病因。
  - GBS nadir 通常在 2-4 週；CIDP 進展至少 2 個月且需多神經 demyelinating-range EDX pattern。
  - Polyneuropathy complications 包含 foot ulceration、Charcot neuroarthropathy、neuropathic pain、dynamic postural instability、falls、deconditioning 與 participation loss。
- 發現衝突：
  - 「急性 nerve injury 的早期 EMG 正常就排除 axonal injury」不成立；EDX abnormality 有時間演變。
  - 「EDX 可以看出所有 nerve structural problem」不成立；connective tissue scaffold / discontinuity 需 clinical、ultrasound 或 surgical correlation。
  - 「diabetes / aging 可解釋所有腳麻」不成立；非典型 pattern 不應被 typical diabetic neuropathy label 掩蓋。
  - 「CIDP 看到單一 entrapment site demyelination 就能診斷」不成立；來源強調需 systemic demyelinating pattern。
- 待追蹤問題：
  - CTS、ulnar neuropathy、fibular neuropathy、GBS、CIDP 可用 guideline / review 各自拆成更細單一概念頁。
  - Neuropathic pain medication safety 可與 existing pain pages 之後做多來源 synthesis，但本輪未混寫。
- 待處理來源：
  - `C:\原始資料\Myopathic disorders\Myopathic disorders.md`

## [2026-05-03] ingest | Cai & Smith — Myopathic Disorders

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Myopathic disorders\Myopathic disorders.md`
- 新增來源摘要：
  - `09_來源摘要/Myopathic_Disorders.md`
- 新增頁面：
  - `03_疾病與臨床主題/Myopathy_診斷框架.md`
  - `03_疾病與臨床主題/Myopathy_復健管理原則.md`
  - `03_疾病與臨床主題/Myopathy_呼吸心臟吞嚥風險.md`
- 更新頁面：
  - `02_方法學/電生理診斷醫學.md`
  - `index.md`
- 本輪抽出的直接事實：
  - Myopathies 是 muscle-fiber dysfunction，症狀可包含 weakness、cramps、rhabdomyolysis、exercise intolerance；主要分 hereditary 與 acquired。
  - 多數 myopathy 為 symmetric proximal weakness 且無 primary sensory symptom，但 FSHD、IBM、distal / metabolic / myotonic disorders 可破壞此典型模式。
  - CK useful but nonspecific；AST / ALT / LDH / aldolase 可因 muscle disease 或 liver dysfunction 升高，GGT 可協助分辨 liver source。
  - Sensory NCS 通常正常；conduction block、temporal dispersion、marked slowing 不符合典型 myopathy，應考慮 neuropathy / demyelinating process。
  - Myopathic EMG 常見 low-amplitude、short-duration、polyphasic MUAP 與 early recruitment；steroid myopathy 可有 normal EMG。
  - MRI / ultrasound 可協助辨識 muscle involvement pattern、severity 與 biopsy target；genetic testing 可確認診斷、預後、organ screening、family counseling 與 targeted therapy eligibility。
  - Myopathy rehabilitation 需每次追蹤 strength / mobility，並處理 exercise safety、contracture prevention、ADL equipment、pain、dysphagia、nutrition、respiratory care。
  - Respiratory muscle weakness 可造成 restrictive lung disease；DMD、myotonic dystrophy、EDMD、select LGMD 等可有 cardiac involvement；IBM / OPMD 等可有 dysphagia risk。
- 發現衝突：
  - 「CK 高就是 inflammatory myopathy」不成立；CK 是 nonspecific muscle injury marker。
  - 「Myopathy 一定是 symmetric proximal weakness」不成立；多個 subtype 有 asymmetric、distal、bulbar、respiratory 或 metabolic trigger pattern。
  - 「肌病復健就是加強肌力」不成立；exercise 必須 disease-specific，DMD 等情境避免 eccentric high-resistance exercise。
  - 「limb weakness 不嚴重就沒有系統風險」不成立；respiratory、cardiac、bulbar involvement 可主導安全性與 mortality。
- 待追蹤問題：
  - DMD、FSHD、IBM、Pompe disease、inflammatory myopathy 需各自用 guideline / review 補強 disease-specific surveillance 與 treatment。
  - Myopathy exercise prescription 的 dose / intensity 仍需專門來源；本輪只保留單一章節支持的安全邊界。
- 待處理來源：
  - `C:\原始資料\Motor neuron diseases\Motor neuron diseases.md`
  - `C:\原始資料\Multiple sclerosis\Multiple sclerosis.md`
  - `C:\原始資料\Degenerative movement disorders of the central nervous system\Degenerative movement disorders of the central nervous system.md`

## [2026-05-03] ingest | Jorgensen, Ketabforoush, Arnold — Motor Neuron Diseases

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Motor neuron diseases\Motor neuron diseases.md`
- 新增來源摘要：
  - `09_來源摘要/Motor_Neuron_Diseases.md`
- 新增頁面：
  - `03_疾病與臨床主題/ALS_診斷框架.md`
  - `03_疾病與臨床主題/ALS_復健呼吸營養與溝通照護.md`
  - `03_疾病與臨床主題/SMA_基因治療後的復健管理.md`
- 更新頁面：
  - `02_方法學/電生理診斷醫學.md`
  - `index.md`
- 本輪抽出的直接事實：
  - MND 可影響 anterior horn cells、cortical motor neurons 或兩者；ALS uniquely involves both UMN and LMN degeneration。
  - UMN signs 包含 spasticity、increased tone、brisk reflexes；LMN signs 包含 weakness、atrophy、fasciculations。
  - 多數 MND 缺乏 overt sensory symptoms，例如 pain、numbness、tingling。
  - EDX 是 identifying LMN loss 與排除 MMN、NMJ disorders、focal radiculomyelopathy 等 mimic 的主要工具。
  - Gold Coast criteria 要求 progressive motor impairment、UMN + LMN in at least one body region 或 LMN in at least two body regions，且 investigations excluding mimics。
  - Multidisciplinary clinics、NIV、PEG、riluzole 在來源中列為可影響 survival / quality of life 的 ALS care components。
  - SMA 與 SMN1 / SMN2 copy number 相關；nusinersen、onasemnogene abeparvovec、risdiplam 改變 disease trajectory，但 rehab / pulmonary / nutrition / orthopedic needs 仍存在。
- 發現衝突：
  - 「MRI 或 lab 可單獨診斷 / 排除 ALS」不成立；來源明確說沒有單一 test 可在有臨床 ALS features 時 rule out ALS。
  - 「fasciculation 等於 ALS」不成立；孤立 fasciculation nonspecific，需結合 weakness 與 EMG denervation。
  - 「supplemental oxygen 是 ALS routine respiratory support」不成立；來源提醒可能 worsen hypercapnia。
  - 「SMA gene therapy 後復健需求消失」不成立；治療後仍需長期 multisystem care。
- 待追蹤問題：
  - ALS / SMA disease-modifying therapy、genetic testing、palliative care timing 與 payer rules 需用 current guideline / prescribing source 更新。
  - ALS exercise dose 與 NIV / PEG threshold 需用專門 guideline 補強。
- 待處理來源：
  - `C:\原始資料\Multiple sclerosis\Multiple sclerosis.md`
  - `C:\原始資料\Degenerative movement disorders of the central nervous system\Degenerative movement disorders of the central nervous system.md`

## [2026-05-03] ingest | Kiernan, Narayan, Shah — Multiple Sclerosis

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Multiple sclerosis\Multiple sclerosis.md`
- 新增來源摘要：
  - `09_來源摘要/Multiple_Sclerosis.md`
- 新增頁面：
  - `03_疾病與臨床主題/MS_診斷與Mimic排除.md`
  - `03_疾病與臨床主題/MS_步態與Spasticity復健框架.md`
  - `03_疾病與臨床主題/MS_Fatigue與Heat_Sensitivity管理.md`
- 更新頁面：
  - `index.md`
- 本輪抽出的直接事實：
  - MS 是 chronic inflammatory neurodegenerative CNS disorder，常造成 young adults 的 nontraumatic disability。
  - Relapse 需 typical CNS demyelinating symptoms lasting at least 24 hours，且無 fever / infection。
  - 2017 McDonald criteria 中 DIS 可由 periventricular、juxtacortical、cortical、infratentorial、spinal cord 五區中至少兩區的 T2 lesions 支持。
  - DIT 可由 follow-up new T2 / gadolinium-enhancing lesion 或 simultaneous enhancing and nonenhancing lesions 支持；CSF oligoclonal bands 可在特定情況 substitute for DIT。
  - MS diagnosis requires no better explanation；NMOSD、ADEM、MOGAD、transverse myelitis、Lyme disease 等 mimic 需排除。
  - Mobility impairment affects about 75% of PwMS；T25FW 20% change 在來源中視為 clinically meaningful。
  - Fatigue 是常見且常 disabling 的 MS symptom；secondary causes 包含 heat、mood / anxiety、sleep、infection、thyroid、anemia、medication。
  - Exercise 在來源引用的 review 中未顯示 increased relapse / adverse events，且可改善 fitness / quality of life。
- 發現衝突：
  - 「MRI 多發 white matter lesions 就是 MS」不成立；clinical fit、DIS / DIT 與 no better explanation 缺一不可。
  - 「OCB 陽性就是 MS」不成立；OCB 可支持 DIT，但不能取代 mimic exclusion。
  - 「MS 因 heat sensitivity 應避免運動」不成立；來源支持 temperature-aware graded exercise。
  - 「DMT 進步後 symptom management 不重要」不成立；來源強調 gait、spasticity、fatigue、bladder / bowel、sexual dysfunction、cognition、dysphagia 等仍需處理。
- 待追蹤問題：
  - DMT 選擇、pregnancy / postpartum management、pediatric MS treatment 與 medication monitoring 需用 current guideline 補強。
  - MS cognition、NLUTD、dysphagia、sexual dysfunction 可各自再拆單一概念頁。
- 待處理來源：
  - `C:\原始資料\Degenerative movement disorders of the central nervous system\Degenerative movement disorders of the central nervous system.md`

## [2026-05-03] ingest | Qutubuddin & Zinoviev — Degenerative Movement Disorders of the Central Nervous System

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Degenerative movement disorders of the central nervous system\Degenerative movement disorders of the central nervous system.md`
- 新增來源摘要：
  - `09_來源摘要/Degenerative_Movement_Disorders_of_the_CNS.md`
- 新增頁面：
  - `03_疾病與臨床主題/Movement_Disorder_現象學分類.md`
  - `03_疾病與臨床主題/Parkinson_Disease_診斷與Mimic排除.md`
  - `03_疾病與臨床主題/Parkinson_Disease_復健與非運動症狀管理.md`
  - `03_疾病與臨床主題/Parkinson_Plus_Syndrome_紅旗.md`
- 更新頁面：
  - `index.md`
- 本輪抽出的直接事實：
  - Movement disorders 是 excessive movement 或 paucity of voluntary / autonomic movement，且 unrelated to weakness or spasticity。
  - Hyperkinetic disorders 包含 RLS、tremor、dystonia、myoclonus、chorea、tics；hypokinetic disorders 包含 PD 與 Parkinson-plus syndromes。
  - Tremor 是 rhythmic oscillatory movement；rest tremor 常見於 PD，action tremor 包含 ET、enhanced physiologic tremor、cerebellar tremor、functional tremor 等。
  - PD 與 substantia nigra pars compacta dopaminergic neuron loss 和 alpha-synuclein Lewy bodies 相關。
  - PD cardinal motor signs 包含 resting tremor、bradykinesia、rigidity、postural instability；diagnosis largely based on clinical assessment。
  - Levodopa remains the most effective drug for PD motor symptoms；interdisciplinary team care 是來源中最有效的 overall approach。
  - PD nonmotor symptoms 包含 psychiatric、cognitive、autonomic、sleep、special sensory symptoms，且是 quality of life、nursing home placement、overall disability 的 major determinants。
  - PSP、MSA、CBGD 可 mimic PD，但 early falls / gaze signs、autonomic failure / cerebellar signs、asymmetric cortical signs 會改變診斷與照護。
- 發現衝突：
  - 「有 tremor 就是 PD」不成立；rest vs action、functional signs、medication 與 ET / cerebellar tremor 都需鑑別。
  - 「PD 可由單一 lab / imaging 確診」不成立；來源明確說目前沒有 definitive lab or imaging。
  - 「levodopa 有效就不需復健」不成立；來源強調 interdisciplinary care、PT、caregiver support 與 nonmotor symptom treatment。
  - 「沒有 vertical gaze palsy 就不是 PSP」不成立；來源提醒 strict reliance on this single sign may delay diagnosis。
- 待追蹤問題：
  - PD / atypical parkinsonism 的 current MDS diagnostic criteria、DBS / FUS selection、exercise dosing、swallowing therapy 與 palliative care 需後續 single-source 補強。
  - RLS、ET、dystonia、HD 可依需要各自拆成單一概念頁。
- 待處理來源：
  - 本輪三篇候選來源已處理完畢；未重新掃描 `C:\原始資料` 全部 backlog。

## [2026-05-03] ingest | Basco et al. — Aging, Dementia, and Disorders of Cognition

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Aging, Dementia, and Disorders of Cognition\Aging, Dementia, and Disorders of Cognition.md`
- 新增來源摘要：
  - `09_來源摘要/Aging_Dementia_and_Disorders_of_Cognition.md`
- 新增頁面：
  - `03_疾病與臨床主題/正常老化與Pathological_Cognitive_Decline.md`
  - `03_疾病與臨床主題/Delirium_Depression_Dementia_鑑別.md`
  - `03_疾病與臨床主題/Dementia_復健與Caregiver支持框架.md`
- 更新頁面：
  - `index.md`
- 本輪抽出的直接事實：
  - Healthy brain aging 可有 cortical volume / thickness change 與 network reorganization，但來源明確指出不必然造成 activity limitation 或 participation restriction。
  - Normal aging 中 memory、language、visuospatial function 可相對穩定；executive function 對 fast、unfamiliar、complex task 較脆弱。
  - Delirium 是 acute attention / awareness / cognition disturbance 且 severity fluctuates，需早期 medical assessment。
  - Depression 在 older adults 可表現為 pain、weakness、headache、agitation、fatigue、appetite / weight change、constipation、sleep problem 與 irritability。
  - Major vs minor neurocognitive disorder 的核心差異是 cognitive decline 是否干擾 everyday independence。
  - Dementia management 需 stage-aware，且 patient-centered care、meaningful engagement、environmental support、OT、exercise、caregiver education 是核心。
- 發現衝突：
  - 「老化等於 dementia」不成立。
  - 「住院或復健中突然變混亂就是 dementia 惡化」不成立；急性波動先想 delirium。
  - 「dementia progressive 所以復健無效」不成立；目標可轉向 safety、ADL/IADL、mobility、caregiver support 與 quality of life。
  - 來源中的 antiamyloid therapy 內容屬 time-sensitive，不能當作 2026 current treatment guidance。
- 待追蹤問題：
  - Dementia prevention、antiamyloid therapy、sleep intervention 與 multidomain risk-reduction 需用 current guideline / systematic review 補強。
  - Dementia stage-specific exercise dosing、severe dementia outcome measurement 可後續拆頁。
- 待處理來源：
  - `C:\原始資料\Brainstem Syndromes\Brainstem Syndromes.md`
  - `C:\原始資料\Movement Dysfunction in Stroke\Movement Dysfunction in Stroke.md`
  - `C:\原始資料\Neurological Rehabilitation\Neurological Rehabilitation.md`

## [2026-05-03] ingest | Brainstem Syndromes

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Brainstem Syndromes\Brainstem Syndromes.md`
- 新增來源摘要：
  - `09_來源摘要/Brainstem_Syndromes.md`
- 新增頁面：
  - `03_疾病與臨床主題/Brainstem_Localization_客觀徵象框架.md`
  - `03_疾病與臨床主題/Brainstem_Ocular_Motor_Syndromes.md`
  - `03_疾病與臨床主題/Brainstem_Stroke_交叉徵象與Locked_In.md`
- 更新頁面：
  - `index.md`
- 本輪抽出的直接事實：
  - Brainstem localization 可利用 cranial nerve nuclei / exiting nerves 的 level-specific anatomy 與 rostrocaudal long tracts。
  - Crossed deficit pattern 是 ipsilateral cranial nerve sign 加 contralateral long tract motor / sensory finding。
  - INO 來自 MLF lesion；intact convergence 支持 isolated MLF lesion 而非 CN III / medial rectus / NMJ problem。
  - Dorsal midbrain / Parinaud syndrome 包含 upgaze palsy、light-near dissociation、convergence-retraction nystagmus 與 lid retraction。
  - Vertebrobasilar lesions 可 patchy and rostrocaudal，不一定符合單一 transverse eponymic syndrome。
  - Locked-in syndrome 通常涉及 basis pontis；quadriplegia 與 speech loss 可伴 preserved consciousness，eye movement / blinking 可能是唯一 voluntary control。
- 發現衝突：
  - 「brainstem syndrome 先背 eponym」不成立；來源優先採 objective signs。
  - 「isolated complete ophthalmoplegia 一定是 focal brainstem lesion」不成立；來源指出通常是 extraaxial。
  - 「locked-in syndrome 是 coma」不成立；reticular activating system 可 preserved。
- 待追蹤問題：
  - Posterior circulation acute stroke imaging、thrombolysis / thrombectomy、BP 與 antithrombotic decision 需 current stroke guideline 補強。
  - Brainstem dysphagia、communication access for locked-in syndrome 可後續拆頁。
- 待處理來源：
  - `C:\原始資料\Movement Dysfunction in Stroke\Movement Dysfunction in Stroke.md`
  - `C:\原始資料\Neurological Rehabilitation\Neurological Rehabilitation.md`

## [2026-05-03] ingest | Quiben & McNeal — Movement Dysfunction in Stroke

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Movement Dysfunction in Stroke\Movement Dysfunction in Stroke.md`
- 新增來源摘要：
  - `09_來源摘要/Movement_Dysfunction_in_Stroke.md`
- 新增頁面：
  - `03_疾病與臨床主題/Stroke_Movement_Dysfunction_Impairment_Model.md`
  - `03_疾病與臨床主題/Poststroke_Spasticity與Hypertonicity區分.md`
  - `03_疾病與臨床主題/Poststroke_Movement_Reeducation與Compensation.md`
- 更新頁面：
  - `index.md`
- 本輪抽出的直接事實：
  - Stroke rehabilitation intervention 應由 movement / activity limitations 指導，而不是由 stroke diagnosis 本身決定。
  - Primary impairments 包含 neurologic weakness、altered muscle activation、initiation / cessation / sequencing / timing / force 問題、sensory loss 與 tone change。
  - Secondary impairments 包含 cardiopulmonary deconditioning、alignment / mobility problem、soft tissue shortening、pain 與 edema。
  - Spasticity 是 passive state 下 velocity-dependent reflex；hypertonicity 與 spasticity 不應當作同義詞。
  - 來源明確指出 spasticity 造成 atypical movement pattern 的舊觀念已被反駁。
  - Undesirable compensation 可造成 learned nonuse、secondary impairment、unsafe movement 與未來 recovery barrier。
- 發現衝突：
  - 「abnormal movement 都是 spasticity 造成」不成立。
  - 「硬就是 spasticity」不成立；需分 reflex、contracture、pain、edema、alignment、co-contraction 與 peripheral stiffness。
  - 「只要 task 完成，compensation 就沒有問題」不成立；需看 safety、impaired-side activation 與 long-term recovery。
- 待追蹤問題：
  - BoNT-A / phenol / intrathecal baclofen 等介入需 current guideline、藥品標示與 patient-specific contraindication 補強。
  - Poststroke aerobic training dose、upper-limb recovery prediction、pain/edema protocol 可後續拆頁。
- 待處理來源：
  - `C:\原始資料\Neurological Rehabilitation\Neurological Rehabilitation.md`

## [2026-05-03] ingest | Dobkin — Neurological Rehabilitation

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Neurological Rehabilitation\Neurological Rehabilitation.md`
- 新增來源摘要：
  - `09_來源摘要/Neurological_Rehabilitation.md`
- 新增頁面：
  - `02_方法學/Neurorehabilitation_目標設定與Team_Based_Care.md`
  - `02_方法學/Neurorehabilitation_Outcome_Measurement.md`
  - `02_方法學/Neurorehabilitation_Motor_Learning與Plasticity.md`
- 更新頁面：
  - `index.md`
- 本輪抽出的直接事實：
  - Neurorehabilitation training 目標是降低 physical / cognitive impairments 與 related disabilities / activity limitations，以增加 functional independence and HRQoL。
  - Movement / skill training 是 active learning and self-management process，包含 motivation、guidance、goal setting、progressive practice、feedback 與 social support。
  - Interdisciplinary team care 應以 functional outcome problem-solving 為核心，而非 discipline-bound 平行處理。
  - Outcome measurement 層級包含 pathophysiology / impairment、disability / functional activity、handicap / participation 與 HRQoL。
  - FIM / BI 主要測 ADL assistance，且 FIM 有 floor / ceiling 與 sensitivity limitations。
  - Robotics、FNS、noninvasive stimulation、BCI、wearables 與 telerehab 在來源中多屬 adjunct，不等於自動優於 dose-matched task practice。
- 發現衝突：
  - 「有多職類就等於 team-based care」不成立；需 shared goals and coordinated strategies。
  - 「單一 ADL score 可代表全部 outcome」不成立。
  - 「新科技自然比傳統復健好」不成立；需看 dose、feedback、task relevance、access、measurement 與 patient-centered outcome。
- 待追蹤問題：
  - Robotics、BCI、tDCS、pharmacologic adjunct、telerehabilitation 與 wearable protocol 需 current systematic review 補強。
  - Neurorehabilitation service setting、AFO prescription、self-management intervention 可後續拆頁。
- 待處理來源：
  - 本輪四篇候選來源已處理完畢；未重新掃描 `C:\原始資料` 全部 backlog。

## [2026-05-03] ingest | Kline-Quiroz & Jones — Cancer Rehabilitation

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Cancer Rehabilitation\Cancer Rehabilitation.md`
- 新增來源摘要：
  - `09_來源摘要/Cancer_Rehabilitation.md`
- 新增頁面：
  - `03_疾病與臨床主題/Cancer_Rehabilitation_總論.md`
- 更新頁面：
  - `index.md`
- 本輪抽出的直接事實：
  - Cancer rehabilitation 應整合於 oncology care continuum，目標包括維持 / 恢復功能、減少 symptom burden、提高 independence 與 quality of life。
  - 來源列出 preventive、restorative、supportive、palliative 四種 phase-specific rehabilitation goals。
  - 常見 cancer-related impairments 包括 fatigue、cognitive impairment、lymphedema、CIPN、pain、radiation fibrosis、bone metastasis。
  - Bone metastasis rehab 需用 SINS、Mirels criteria、platelet count 與 oncology plan 做 safety framing。
- 發現衝突：
  - 「癌症復健只適用末期或 palliative care」不成立。
  - 「骨轉移等於完全不能復健」不成立；需依 fracture / spinal instability risk 調整。
- 待追蹤問題：
  - Cancer-related fatigue、CIPN、lymphedema、bone metastasis rehabilitation precautions 可後續拆頁。
- 待處理來源：
  - `C:\原始資料\Cancer Rehabilitation\Cancer Rehabilitation.md` 已完成本輪單一來源 ingest。

## [2026-05-03] ingest | Oh-Park, Choudry & Shah — Geriatrics

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Geriatrics\Geriatrics.md`
- 新增來源摘要：
  - `09_來源摘要/Geriatrics.md`
- 新增頁面：
  - `03_疾病與臨床主題/高齡復健與Frailty框架.md`
- 更新頁面：
  - `index.md`
- 本輪抽出的直接事實：
  - Sarcopenia 與 falls、fractures、physical disability、mortality 相關。
  - EWGSOP2 以 muscle strength 為 sarcopenia case finding 重點；來源列出 hand grip、chair rise、gait speed、SPPB 等指標。
  - Falls risk 可分 environmental、physical、mental、pharmacologic contributors。
  - Age-Friendly 4Ms 包含 Medication、Mentation、Mobility、What Matters。
- 發現衝突：
  - 「gait disorder 是 aging 必然結果」不成立。
  - 「高齡復健只是低強度成人復健」不成立；polypharmacy、delirium、falls、goals 必須納入。
- 待追蹤問題：
  - Sarcopenia screening、falls prevention、Age-Friendly 4Ms 可後續拆成單一概念頁。
- 待處理來源：
  - `C:\原始資料\Geriatrics\Geriatrics.md` 已完成本輪單一來源 ingest。

## [2026-05-03] ingest | Sinaki, Wermers & Prideaux — Osteoporosis

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Osteoporosis\Osteoporosis.md`
- 新增來源摘要：
  - `09_來源摘要/Osteoporosis.md`
- 新增頁面：
  - `03_疾病與臨床主題/Osteoporosis_復健與骨折預防.md`
- 更新頁面：
  - `index.md`
- 本輪抽出的直接事實：
  - WHO osteoporosis definition 以 T-score -2.5 或更低為主。
  - Peak adult bone mass 約在 30-35 歲達成；之後 bone remodeling 可逐漸產生 net bone loss。
  - 常見 osteoporotic fracture 包括 vertebral、hip、distal forearm。
  - Moderate-intensity resistance training 與 impact exercise 可降低 vertebral fracture risk，但 exercise recommendations must be individualized。
- 發現衝突：
  - 「osteoporosis exercise 就是一般 strengthening」不成立；spinal loading direction、BMD、fracture history 與 fall risk 都要納入。
  - 「沒有痛就沒有 vertebral fracture」不成立；部分 vertebral fractures 可 subclinical。
- 待追蹤問題：
  - Osteoporotic vertebral fracture rehab、back extensor training、pharmacologic guideline 需後續補強。
- 待處理來源：
  - `C:\原始資料\Osteoporosis\Osteoporosis.md` 已完成本輪單一來源 ingest。

## [2026-05-03] ingest | Marcotte & Kumar — Pelvic Floor Disorders

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Pelvic floor disorders\Pelvic floor disorders.md`
- 新增來源摘要：
  - `09_來源摘要/Pelvic_Floor_Disorders.md`
- 新增頁面：
  - `03_疾病與臨床主題/Pelvic_Floor_Disorders_復健總論.md`
- 更新頁面：
  - `index.md`
- 本輪抽出的直接事實：
  - Pelvic floor disorders occur in both sexes。
  - PFM dysfunction categories 包括 increased tone、pain、decreased tone、coordination disorder。
  - PFPT 是 pelvic floor myofascial pain 的 first-line rehabilitation treatment。
  - Internal pelvic floor exam 需要清楚說明、consent、privacy、chaperone 與可停止權利。
- 發現衝突：
  - 「pelvic pain 一定是 gynecologic / visceral problem」不成立。
  - 「所有 pelvic floor dysfunction 都做 Kegel」不成立。
- 待追蹤問題：
  - Pelvic floor myofascial pain、pudendal neuralgia、chronic pelvic pain rehabilitation 可後續拆頁。
- 待處理來源：
  - `C:\原始資料\Pelvic floor disorders\Pelvic floor disorders.md` 已完成本輪單一來源 ingest。

## [2026-05-03] ingest | Hsieh, Mao & Lu — Rehabilitation of Common Rheumatological Disorders

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Rehabilitation of common rheumatological disorders\Rehabilitation of common rheumatological disorders.md`
- 新增來源摘要：
  - `09_來源摘要/Rehabilitation_of_Common_Rheumatological_Disorders.md`
- 新增頁面：
  - `03_疾病與臨床主題/Rheumatic_Disease_復健總論.md`
- 更新頁面：
  - `index.md`
- 本輪抽出的直接事實：
  - Rheumatic diseases 包含 immune-related 與 nonimmune-related musculoskeletal disorders。
  - OA 的核心 features 包含 pain、limited morning stiffness、reduced function、crepitus、restricted movement、bony hypertrophy。
  - Symptomatic knee OA diagnosis 應主要基於 clinical findings；影像異常可無症狀。
  - Rheumatic disease rehab 包含 evaluation、patient education、exercise、orthoses、modalities、assistive devices 與 environmental modification。
- 發現衝突：
  - 「x-ray 有 OA 所以痛一定是 OA」不成立。
  - 「rheumatic disease rehab 只是物理因子止痛」不成立。
- 待追蹤問題：
  - OA rehab、RA rehab、AS rehab、septic arthritis red flags 可後續拆頁；DMARD / biologic 需 current guideline。
- 待處理來源：
  - `C:\原始資料\Rehabilitation of common rheumatological disorders\Rehabilitation of common rheumatological disorders.md` 已完成本輪單一來源 ingest。

## [2026-05-03] ingest | Whiteson, Cohen & Prilik — Chronic Medical Conditions

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Chronic medical conditions Pulmonary disease, organ transplantation, and diabetes\Chronic medical conditions Pulmonary disease, organ transplantation, and diabetes.md`
- 新增來源摘要：
  - `09_來源摘要/Chronic_Medical_Conditions_Pulmonary_Disease_Organ_Transplantation_and_Diabetes.md`
- 新增頁面：
  - `03_疾病與臨床主題/慢性肺病Pulmonary_Rehabilitation.md`
- 更新頁面：
  - `index.md`
- 本輪抽出的直接事實：
  - Pulmonary rehabilitation 是 evidence-based、multidisciplinary、comprehensive intervention。
  - Chronic lung disease 可分 obstructive、restrictive、pulmonary vascular、hypoventilation patterns。
  - COPD 是 PR 最常見 referral reason。
  - Diaphragmatic breathing 在 COPD 可能增加 work of breathing and dyspnea。
  - Transplant 與 diabetes rehab 需 disease-specific exercise safety and monitoring。
- 發現衝突：
  - 「PR 只有 treadmill / aerobic conditioning」不成立。
  - 「COPD 一律教 diaphragmatic breathing」不成立。
- 待追蹤問題：
  - Solid organ transplant rehab、diabetes exercise safety、oxygen logistics 可後續拆頁。
- 待處理來源：
  - `C:\原始資料\Chronic medical conditions Pulmonary disease, organ transplantation, and diabetes\Chronic medical conditions Pulmonary disease, organ transplantation, and diabetes.md` 已完成本輪單一來源 ingest。

## [2026-05-03] ingest | Bartels, Prince & Supervia — Acute Medical Conditions

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\28 Acute medical conditions Cardiopulmonary disease, medical frailty, and renal failure\28 Acute medical conditions Cardiopulmonary disease, medical frailty, and renal failure.md`
- 新增來源摘要：
  - `09_來源摘要/Acute_Medical_Conditions_Cardiopulmonary_Disease_Medical_Frailty_and_Renal_Failure.md`
- 新增頁面：
  - `03_疾病與臨床主題/急性醫療虛弱與Early_Mobilization.md`
- 更新頁面：
  - `index.md`
- 本輪抽出的直接事實：
  - Frailty results in decreased mobility and functional decline；mobility 應在 medical settings 中被優先保護。
  - Cardiac rehabilitation 是 evidence-based secondary prevention program，非單純 aerobic exercise。
  - Aerobic prescription 包含 intensity、duration、frequency、specificity。
  - Immobility 有 multisystem functional consequences；renal failure / dialysis 會增加特殊 debility and safety issues。
- 發現衝突：
  - 「frailty 所以應預設臥床」不成立。
  - 「cardiac rehabilitation 只是運動課」不成立。
- 待追蹤問題：
  - Cardiac rehab、renal failure rehab safety、ICU-acquired weakness 可後續拆頁。
- 待處理來源：
  - `C:\原始資料\28 Acute medical conditions Cardiopulmonary disease, medical frailty, and renal failure\28 Acute medical conditions Cardiopulmonary disease, medical frailty, and renal failure.md` 已完成本輪單一來源 ingest。

## [2026-05-03] ingest | Twichell — Burns

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\27 burn\27 burn.md`
- 新增來源摘要：
  - `09_來源摘要/Burns.md`
- 新增頁面：
  - `03_疾病與臨床主題/Burn_Rehabilitation_總論.md`
- 更新頁面：
  - `index.md`
- 本輪抽出的直接事實：
  - Burn severity 由 size、depth、etiology 與 associated injury 決定。
  - Certified burn-center transfer criteria 包含高風險部位、inhalation injury、TBSA thresholds、full-thickness burns、electrical / chemical burns。
  - Burn rehab 應從 admission 開始，並延續到 inpatient、outpatient、long-term survivorship。
  - Burn complications 包括 hypermetabolism、dysphagia、cognitive concerns、pruritus、neuropathy、HO、amputation、hypertrophic scar、contracture。
- 發現衝突：
  - 「burn wound 沒好所以不能復健」不成立。
  - 「burn pain management 只靠 opioid」不成立；來源支持 multimodal analgesia and nonpharmacologic adjuncts。
- 待追蹤問題：
  - Postburn contracture prevention、hypertrophic scar、postburn pruritus / pain、electrical burn rehab 可後續拆頁。
- 待處理來源：
  - `C:\原始資料\27 burn\27 burn.md` 已完成本輪單一來源 ingest。

## [2026-05-03] ingest | McMullen, Meron & De Luigi — Sports Medicine and Adaptive Sports

- 類型：textbook chapter（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\Sports medicine and adaptive sports\Sports medicine and adaptive sports.md`
- 新增來源摘要：
  - `09_來源摘要/Sports_Medicine_and_Adaptive_Sports.md`
- 新增頁面：
  - `03_疾病與臨床主題/Sports_Medicine與Adaptive_Sports_總論.md`
- 更新頁面：
  - `index.md`
- 本輪抽出的直接事實：
  - Team physician 負責 medical eligibility、injury care、RTP、emergency preparedness、training oversight、supervision、liability protection。
  - Event administration 需要 chain of command、EAP、equipment、protocols、environmental assessment 與 communication。
  - Training principles 包含 specificity、individuality、periodization、overload、tapering。
  - Full RTP 需要無痛、flexibility / strength / proprioception 正常、sport-specific mechanics and skills 可重現。
  - Adaptive sports medicine 需 classification、equipment 與 disability-cause injury patterns。
- 發現衝突：
  - 「pain-free 就能 RTP」不成立。
  - 「adaptive sports 只是一般 sports medicine 加 disability label」不成立。
- 待追蹤問題：
  - RTP framework、sports concussion、team physician/EAP、adaptive sports injury patterns 可後續拆頁。
- 待處理來源：
  - `C:\原始資料\Sports medicine and adaptive sports\Sports medicine and adaptive sports.md` 已完成本輪單一來源 ingest。

## [2026-05-03] ingest | Burke-Doe & Johnson — Impact of Drug Therapy on Patients Receiving Neurological Rehabilitation

- 類型：textbook chapter（Tier 1；藥物資訊 time-sensitive，confidence moderate）
- 重新檢查來源：
  - `C:\原始資料\Impact of Drug Therapy on Patients Receiving Neurological Rehabilitation\Impact of Drug Therapy on Patients Receiving Neurological Rehabilitation.md`
- 新增來源摘要：
  - `09_來源摘要/Impact_of_Drug_Therapy_on_Patients_Receiving_Neurological_Rehabilitation.md`
- 新增頁面：
  - `02_方法學/Neurorehabilitation_藥物效應與治療時機.md`
- 更新頁面：
  - `index.md`
- 本輪抽出的直接事實：
  - Pharmacokinetics 包含 absorption、distribution、metabolism、elimination。
  - Pharmacodynamics 關注 drug effects and mechanisms。
  - Disease、age、diet、gender、genetics、drug interactions 可改變 drug response。
  - PD medication timing、antiseizure drug sedation / ataxia、antihypertensive orthostasis、anticoagulant bleeding risk 都會影響 therapy safety and performance。
- 發現衝突：
  - 「復健人員不用管藥物」不成立；藥物會改變 participation、safety、learning、outcome interpretation。
  - 「看到副作用就由 rehab clinician 自行停藥」不成立；應回報 prescriber / pharmacist。
- 待追蹤問題：
  - Parkinson medication timing、antiseizure medication and motor learning、cardiovascular medication safety 可後續拆頁；所有藥物資訊需 current drug reference。
- 待處理來源：
  - `C:\原始資料\Impact of Drug Therapy on Patients Receiving Neurological Rehabilitation\Impact of Drug Therapy on Patients Receiving Neurological Rehabilitation.md` 已完成本輪單一來源 ingest。

## [2026-05-03] ingest | WHO guidelines on parenting interventions

- 類型：WHO guideline（Tier 1）
- 重新檢查來源：
  - `C:\原始資料\WHO guidelines on parenting interventions\WHO guidelines on parenting interventions.md`
- 新增來源摘要：
  - `09_來源摘要/WHO_guidelines_on_parenting_interventions.md`
- 新增頁面：
  - `07_Pediatric_Development/Parenting_Interventions_防止兒童不當對待與強化親子關係.md`
- 更新頁面：
  - `07_Pediatric_Development/正向教養與家庭支持.md`
  - `index.md`
- 本輪抽出的直接事實：
  - WHO 2022 guideline 對 0-17 歲 parents / caregivers 的 parenting interventions 提出五項 strong recommendations。
  - Guideline 使用 WHO guideline development process、GRADE、systematic reviews、narrative review 與 WHO-INTEGRATE considerations。
  - 主要 outcomes 包含 child maltreatment、harsh / negative parenting、positive parenting、child externalizing / internalizing problems、parental mental health 與 parenting stress。
  - Effective components 包括 nonviolent discipline、positive reinforcement、proactive parenting、parental self-management、child-led play、empathy building 與 skill practice。
  - Serious maltreatment 或嚴重 parent-child conflict 時，應考慮 specialized parenting intervention 加上 child protection service intervention。
- 發現衝突：
  - 「parenting intervention 只是一次性教養建議」不成立。
  - 「strong recommendation 代表每個 outcome 都是 high-certainty evidence」不成立；adolescent LMIC 與 humanitarian settings 多項 outcome 仍為 low / very low certainty。
  - 「parenting program 可以取代 poverty reduction、public health 或 child protection」不成立。
- 待追蹤問題：
  - indicated parenting interventions and child protection interface、adolescent-focused parenting intervention、humanitarian settings parenting support、cultural adaptation and fidelity 可後續拆頁。
- 待處理來源：
  - `C:\原始資料\WHO guidelines on parenting interventions\WHO guidelines on parenting interventions.md` 已完成本輪單一來源 ingest。

## [2026-05-03] ingest | Nurturing Care Practice Guide

- 類型：WHO / UNICEF practice guide（Tier 2）
- 重新檢查來源：
  - `C:\原始資料\nurturing care practice guide\nurturing care practice guide.md`
- 新增來源摘要：
  - `09_來源摘要/Nurturing_Care_Practice_Guide.md`
- 新增頁面：
  - `07_Pediatric_Development/Nurturing_Care_健康與營養服務整合.md`
- 更新頁面：
  - `07_Pediatric_Development/Caregiving_Quality_作為早期介入靶點.md`
  - `07_Pediatric_Development/照顧者健康與兒童健康發展.md`
  - `index.md`
- 本輪抽出的直接事實：
  - Nurturing care 包含 good health、adequate nutrition、safety and security、opportunities for early learning、responsive caregiving 五個 interrelated components。
  - Guide 聚焦 health / nutrition services 中常被忽略的 responsive caregiving、early learning、safety and security，以及 caregiver well-being。
  - Managers 可透過 facility accessibility、play / counselling spaces、protocol adaptation、training / mentoring、caregiver participation policy、humanitarian adaptation 與 referral mapping 支持 nurturing care。
  - Providers 可在 antenatal、postnatal、well-child、sick-child、inpatient、home visit 與 nutritional rehabilitation 接觸中觀察、示範、稱讚、coaching 與 problem-solving。
  - Guide 使用 universal、targeted、indicated 三層 support；developmental milestone assessment 若沒有 referral network and indicated support，效果可能不足。
- 發現衝突：
  - 「健康與營養服務只需管 growth、vaccine、illness」不成立。
  - 「nurturing care support 等於發衛教單」不成立；來源強調 provider observation、modeling、coaching 與 caregiver practice。
  - 「問 milestone 就完成 developmental care」不成立；來源明確指出若 referral networks 與 indicated support 不足，單純要求 primary care providers assess milestones unlikely to be effective。
- 待追蹤問題：
  - responsive caregiving in clinical encounters、playbox / waiting-room developmental intervention、nutritional rehabilitation and early learning、zero separation / family-centred neonatal and inpatient care 可後續拆頁。
- 待處理來源：
  - `C:\原始資料\nurturing care practice guide\nurturing care practice guide.md` 已完成本輪單一來源 ingest。

## [2026-05-03] ingest | WHO — Caregiver Skills Training Adaptation and Implementation Guide

- 類型：WHO implementation / adaptation guide（Tier 2）
- 重新檢查來源：
  - `C:\原始資料\Adaptation and implementation guide\Adaptation and implementation guide.md`
- 新增來源摘要：
  - `09_來源摘要/Caregiver_Skills_Training_Adaptation_and_Implementation_Guide.md`
- 新增頁面：
  - `07_Pediatric_Development/Caregiver_Skills_Training_CST_在地化與Implementation_Fidelity.md`
- 更新頁面：
  - `index.md`
- 本輪抽出的直接事實：
  - CST intended audience 是 2-9 歲、有 developmental delays or disabilities 的兒童照顧者；child 不必已有正式 diagnosis。
  - CST 標準 course structure 是 9 group sessions 加 3 home visits，由 trained and supervised non-specialist facilitators 執行。
  - Adaptation 應先做 recommended / essential changes，並記錄 rationale；重大結構改變需 consultation、documentation 與 evaluation。
  - Core components 包含 key messages / tips、group activities、home visits、guided practice、goal-setting、home practice、teaching methods、facilitator-to-participant ratio、session sequence 與 target population boundary。
  - Implementation planning 需處理 service mapping、legal / child protection framework、transportation、childcare、scheduling、caregiver involvement、stigma 與 local resource list。
- 發現衝突：
  - 「CST 只是家長衛教單」不成立。
  - 「文化在地化等於任意改教材」不成立。
  - 「fidelity 等於不能在地化」不成立。
  - 「縮短課程一定等效」不成立；來源要求保留 foundational sessions 與 core components，重大結構改變需評估。
- 待追蹤問題：
  - CST facilitator guide、participant guide、home visit guide 可後續逐篇單一來源 ingest。
  - CST 與 ASD early intervention、developmental delay waiting-period support、caregiver well-being module 可後續拆頁。
- 待處理來源：
  - `C:\原始資料\Facilitators’ guide\Facilitators’ guide.md`
  - `C:\原始資料\Participants’ guide\Participants’ guide.md`
  - `C:\原始資料\Home visit guide for facilitators\Home visit guide for facilitators.md`

## [2026-05-03] ingest | WHO — Caregiver Skills Training Facilitators' Guide

- 類型：WHO facilitators' guide / implementation manual（Tier 2）
- 重新檢查來源：
  - `C:\原始資料\Facilitators’ guide\Facilitators’ guide.md`
- 新增來源摘要：
  - `09_來源摘要/Caregiver_Skills_Training_Facilitators_Guide.md`
- 新增頁面：
  - `07_Pediatric_Development/CST_Facilitator_Delivery_Model_引導式練習與Home_Practice_Loop.md`
- 更新頁面：
  - `07_Pediatric_Development/Caregiver_Skills_Training_CST_在地化與Implementation_Fidelity.md`
  - `index.md`
- 本輪抽出的直接事實：
  - Facilitators' guide 必須搭配 practical training and supervision 使用；reading the guide is not enough。
  - Session 2-9 的一般結構包含 wellness activity、review key messages / tips、home practice discussion、caregiver story、group teaching、facilitator demonstration、role-play、coaching / feedback、home-practice planning 與 close。
  - CST 是 caregiver-mediated intervention，目標是把 strategies integrated into everyday life。
  - Home practice between group sessions is considered essential；caregivers are asked to practise skills daily。
  - Session progression：engagement → shared engagement routines → communication → small-step adaptive skills → challenging behaviour prevention / alternatives → self-care and problem-solving。
  - Challenging behaviour 被整理為 get access、get attention、avoid/stop something、get a sensation 四種功能；且部分 behavior 可源於 physical or medical reasons，不能以 punishment 處理。
- 發現衝突：
  - 「看完手冊即可執行 CST」不成立。
  - 「CST 是家長觀念課」不成立；來源反覆要求 demonstration、role-play、coaching、feedback and home practice。
  - 「home practice 是可有可無」不成立。
  - 「behavior module 是處罰不乖」不成立；來源採 regulation、antecedent、function、prevention、replacement 的邏輯。
- 待追蹤問題：
  - CST shared engagement routines、communication to request/share、challenging behaviour function-based response 可後續拆成單一概念頁。
  - Participants' guide 與 Home visit guide for facilitators 仍需逐篇單一來源 ingest。
- 待處理來源：
  - `C:\原始資料\Participants’ guide\Participants’ guide.md`
  - `C:\原始資料\Home visit guide for facilitators\Home visit guide for facilitators.md`

## [2026-05-03] ingest | WHO — Caregiver Skills Training Home Visit Guide for Facilitators

- 類型：WHO home visit guide / facilitator manual（Tier 2）
- 重新檢查來源：
  - `C:\原始資料\Home visit guide for facilitators\Home visit guide for facilitators.md`
- 新增來源摘要：
  - `09_來源摘要/Caregiver_Skills_Training_Home_Visit_Guide_for_Facilitators.md`
- 新增頁面：
  - `07_Pediatric_Development/CST_Home_Visit_Model_個別化Goal_Setting與Guided_Practice.md`
- 更新頁面：
  - `07_Pediatric_Development/Caregiver_Skills_Training_CST_在地化與Implementation_Fidelity.md`
  - `07_Pediatric_Development/CST_Facilitator_Delivery_Model_引導式練習與Home_Practice_Loop.md`
  - `index.md`
- 本輪抽出的直接事實：
  - Home visit guide 必須搭配 specific training and supervision 使用；reading the guide is not enough。
  - CST standard course structure 是 9 group sessions 加 3 home visits，由 trained and supervised non-specialist facilitators 執行。
  - Home visit 1 在 session 1 前，聚焦 family introduction、child / caregiver needs assessment、caregiver interview、FCI、CCI and establishing goals。
  - Home visit 2 preferably 在 session 5 和 session 6 之間，聚焦 re-evaluate goals、review home practice、guided practice、coaching and demonstration。
  - Home visit 3 在 session 9 後，聚焦 re-evaluate longer-term goals、consolidate selected strategies、select routines and support independent practice。
  - CCI 每次 home visit 使用；FCI 在 home visit 1 obligatory、home visit 3 optional；兩者皆為 12-minute clinical tools。
  - Goal-setting 依 caregiver interview 與 CCI / FCI observations 設定 child targets、caregiver targets and target routines。
  - Coaching 是 adult learning methodology，facilitator 在 caregiver-child interaction 中主動支持、調整或示範，支持量依 caregiver confidence、facilitator certainty and child response 調整。
  - Home visits include assessment of additional family needs, including child / caregiver health, caregiver mental health, potential child maltreatment and material deprivation。
- 發現衝突：
  - 「CST home visits 是可有可無的追蹤」不成立。
  - 「CCI / FCI 是正式 developmental diagnosis」不成立。
  - 「Goal-setting 就是照 caregiver long-term hope 寫目標」不成立；來源要求依 current skills 設定 small next steps。
  - 「Coaching 等於旁觀或完全由 facilitator 接手」不成立；來源要求依 needs 給 right amount of support。
  - 「發現 neglect / abuse 時 facilitator 自己處理即可」不成立；來源要求 consult supervisor and referral。
- 待追蹤問題：
  - CST CCI / FCI observation、coaching support levels、safeguarding and referral boundary、communication requesting/sharing goals 可後續拆成單一概念頁。
- 待處理來源：
  - `C:\原始資料\Participants’ guide\Participants’ guide.md`

## [2026-05-03] ingest | WHO — Caregiver Skills Training Participants' Guide

- 類型：WHO participants' guide / caregiver-facing workbook（Tier 2）
- 重新檢查來源：
  - `C:\原始資料\Participants’ guide\Participants’ guide.md`
- 新增來源摘要：
  - `09_來源摘要/Caregiver_Skills_Training_Participants_Guide.md`
- 新增頁面：
  - `07_Pediatric_Development/CST_Caregiver_Strategy_Practice_日常Routines與Home_Practice.md`
- 更新頁面：
  - `07_Pediatric_Development/Caregiver_Skills_Training_CST_在地化與Implementation_Fidelity.md`
  - `07_Pediatric_Development/CST_Facilitator_Delivery_Model_引導式練習與Home_Practice_Loop.md`
  - `07_Pediatric_Development/CST_Home_Visit_Model_個別化Goal_Setting與Guided_Practice.md`
  - `index.md`
- 本輪抽出的直接事實：
  - Participants' guide 是給參與 WHO CST 的 caregivers 使用，內容涵蓋 group sessions 1-9。
  - Guide 包含 illustrated key messages and tips、goal-setting activities、questions to check learning，以及 local resources template。
  - 若 caregiver 想自行學習而沒有 local CST course，來源導向 WHO eLearning CST，不是把 PDF guide 當作完整替代。
  - CST target audience 是 2-9 歲、具 developmental delays or disabilities 的兒童 caregivers；child 不必已有 formal diagnosis。
  - CST designed structure 是 9 group sessions and 3 home visits，由 trained and supervised non-specialist facilitators 執行。
  - Sessions 1-2 聚焦 getting / keeping children engaged；Session 3 聚焦 play and home routines；Sessions 4-5 聚焦 communication；Session 6 聚焦 small steps and levels of help；Sessions 7-8 聚焦 challenging behaviour；Session 9 聚焦 caregiver well-being、problem-solving and ongoing practice。
  - Home practice 反覆要求 caregiver 選擇 everyday routines、brief practice、review successes / barriers and plan next steps。
  - Challenging behaviour 被整理為 get access、get attention、avoid / stop something、get a sensation，response 需依 reason 調整。
- 發現衝突：
  - 「Participants' guide 可單獨取代 CST course」不成立。
  - 「CST 是一般教養觀念」不成立；來源以 key messages、tips、goal-setting、home practice and learning checks 組織。
  - 「Communication intervention 只能等 spoken words 出現後再做」不成立。
  - 「Challenging behaviour 主要靠 harsh discipline 處理」不成立。
  - 「Caregiver self-care 與 child intervention 無關」不成立。
- 待追蹤問題：
  - CST shared engagement routines、requesting vs sharing communication goals、small-step adaptive skill teaching、function-based challenging behaviour response、caregiver self-care and problem-solving 可後續拆成單一概念頁。
- 待處理來源：
  - WHO CST package 三份核心 guide 已完成本輪序列 ingest；後續可依 log 中待追蹤問題逐頁拆概念。

## [2026-05-03] ingest | WHO — Caregiver Skills Training Introduction

- 類型：WHO introduction to CST package（Tier 2）
- 重新檢查來源：
  - `C:\原始資料\Introduction\Introduction.md`
- 新增來源摘要：
  - `09_來源摘要/Caregiver_Skills_Training_Introduction.md`
- 新增頁面：
  - `07_Pediatric_Development/CST_Package_Architecture_多層教材與Training_Supervision.md`
- 更新頁面：
  - `07_Pediatric_Development/Caregiver_Skills_Training_CST_在地化與Implementation_Fidelity.md`
  - `07_Pediatric_Development/CST_Facilitator_Delivery_Model_引導式練習與Home_Practice_Loop.md`
  - `07_Pediatric_Development/CST_Home_Visit_Model_個別化Goal_Setting與Guided_Practice.md`
  - `07_Pediatric_Development/CST_Caregiver_Strategy_Practice_日常Routines與Home_Practice.md`
  - `index.md`
- 本輪抽出的直接事實：
  - CST package 的 intended audience 是 caregivers of children aged 2-9 years with developmental delays or disabilities，尤其 social / communication delays or impairments。
  - Child 不必已有 formal diagnosis 即可被 referral to CST。
  - CST standard format 是 9 core group sessions and 3 home visits。
  - Group sessions 通常 2.5-3 hours，weekly or every two weeks；home visits 通常 1.5-2 hours。
  - Home visits 排在 group session 1 前、sessions 5/6 之間、final group session 後。
  - CST designed to be delivered by trained non-specialists，並整合在 community-based health and social services network。
  - CST 應作為 stepped care approach 的一部分，先提供 least resource-intensive effective support，再依需求 step up to specialist services。
  - Facilitator supervision 被描述為 essential，至少每次 home visit 後應有 formal check。
  - Field-testing 支持 feasibility、acceptability、relevance、improved parenting skills and caregiver well-being；不可直接過度外推成 definitive efficacy。
- 發現衝突：
  - 「CST 必須等 formal diagnosis 後才能做」不成立。
  - 「CST 是一本手冊或一次家長衛教」不成立。
  - 「Non-specialist delivery 等於不需要 training/supervision」不成立。
  - 「Home visits 可任意刪除但仍維持同一 package」不成立。
- 待追蹤問題：
  - CST stepped-care referral boundary、facilitator supervision fidelity、safeguarding pathway、virtual delivery adaptation 可後續拆成單一概念頁。
- 待處理來源：
  - 需再掃描 `C:\原始資料` 以選定下一篇未處理來源。

## [2026-05-03] correction | Rogers & Vismara — Encouraging infant communication and play

- 修正原因：此來源在 2026-04-24 曾被 ingest，但摘要仍偏舊式 batch 產物；本輪依單一來源與 fact / inference / assumption / uncertainty 分層重新整理。
- 重新檢查來源：
  - `C:\原始資料\Encouraging infant communication and play\Encouraging infant communication and play.md`
- 更新來源摘要：
  - `09_來源摘要/Encouraging_infant_communication_and_play.md`
- 新增頁面：
  - `07_Pediatric_Development/Infant_Cue_Based_Interaction_日常Routines與Communication_Bundles.md`
- 更新頁面：
  - `07_Pediatric_Development/嬰兒期發展.md`
  - `07_Pediatric_Development/嬰兒期的狀態調節與互動評估.md`
  - `07_Pediatric_Development/Serve_and_Return.md`
  - `07_Pediatric_Development/Caregiving_Quality_作為早期介入靶點.md`
  - `07_Pediatric_Development/早期語言發展與Emergent_Literacy.md`
  - `index.md`
- 本輪抽出的直接事實：
  - 來源作者為 Sally J. Rogers and Laurie A. Vismara，manual 屬 ESDM Training Program / MIND Institute / UC Davis Health 脈絡。
  - Manual 來自 2010-2012 年針對 families concerned about possible autism symptoms in infants under 12 months of age 的工作脈絡，並引用 Rogers/Vismara et al. 2014 Infant Start pilot study。
  - 來源明確說 underlying study was not a randomized clinical trial，不能提供 experimental proof that the concepts helped infants。
  - 來源說明 families were largely white, American, and from middle to upper middle socioeconomic status。
  - 來源把 infant cues 分成 seeking more engagement 與 seeking less engagement，並教 caregiver 調整 proximity、pace and affect。
  - 來源把 15 months and younger 的 daily routines 分成 mealtimes、physical care、books、outdoor play、social games and toy play。
  - 來源教 caregiver 透過 active watching、narration、imitation、waiting、responding to sounds、object turn-taking and flexible play 建立互動。
  - 來源把 preverbal communication 放在 gaze、facial expression、gesture、body posture、sound、directed communication and joint attention 的框架中。
  - 來源描述 communication bundles 為 coordinated gaze、voice、gesture、body orientation or facial expression，並用 caregiver response 強化 clearer bundled communication。
- 移除或降級的陳述：
  - 未保留任何把 manual 當作 consensus-level intervention proof 的語氣。
  - 將 manual 的臨床定位降回 caregiver coaching scaffold，而不是 ASD early intervention efficacy evidence。
- 發現衝突：
  - 「more stimulation is always better」不成立；來源要求 cue-matched intensity。
  - 「preverbal communication 只等於 babble or words」不成立。
  - 「brief waiting 等於忽略 infant distress」不成立；來源要求依 infant cue 調整與停止。
  - 「caregiver manual 可取代 developmental evaluation」不成立。
- 仍不確定之處：
  - 哪個 component 對 outcome 最重要仍未被本來源證明。
  - 不同 culture、SES、language、family stress、hearing/vision/motor/medical conditions 下的可用性需要其他來源校正。
- 待處理來源：
  - 若後續要提升 evidence level，應回查 Rogers/Vismara 2014 pilot study、Infant Start 後續研究、ASD early intervention systematic review 或 guideline。

## [2026-05-03] correction | Harvard Center — Building Resilience Through Play

- 修正原因：此來源在 2026-04-25 batch ingest 中已建立來源摘要，但未依單一來源 workflow 完整拆出 Fact / Inference / Assumption / Uncertainty，也尚未建立單一概念頁。
- 重新檢查來源：
  - `C:\原始資料\Building Resilience Through Play.md`
- 更新來源摘要：
  - `09_來源摘要/Building_Resilience_Through_Play.md`
- 新增頁面：
  - `07_Pediatric_Development/Play_作為Resilience_Building_Context.md`
- 更新頁面：
  - `07_Pediatric_Development/創傷_復原力與兒童發展.md`
  - `07_Pediatric_Development/Play_Based_Pediatric_Examination.md`
  - `07_Pediatric_Development/幼兒與學齡前期發展.md`
  - `index.md`
- 本輪抽出的直接事實：
  - 來源是 Harvard Center on the Developing Child 的 Brain Architects podcast transcript，屬 science-translation source。
  - 來源把 resilience 定義為 coping、overcoming hardship/adversity/threat 的能力。
  - 來源明確說 resilience 在 relationships and environments 中被 actively built，不是在 child alone 或 vacuum 中產生。
  - 來源提出三個 developmental principles：supportive relationships、reduce significant sources of stress、build core skills。
  - 來源把 play 描述為 child master environment、test limits、learn strategies、gain control 的 developmental process。
  - 來源舉 infant play 包含 eye contact、smiling、cooing、vocal back-and-forth、handing/grabbing and serve-and-return interaction。
  - 來源討論 play 在 preschool drop-off、hospital procedures、refugee/humanitarian settings、libraries、museums、public spaces and pediatric well visits 的應用。
  - Prescription for Play 範例把 pediatric well visits 中的 play guidance 連到 safe, stable, nurturing relationships。
- 移除或降級的陳述：
  - 未把 play 寫成 trauma treatment protocol 或 intervention efficacy proof。
  - 將 podcast examples 降級為 implementation examples，而不是正式 guideline。
- 發現衝突：
  - 「resilience 是孩子自己撐出來」不成立。
  - 「play 是危機後可有可無的娛樂」不成立。
  - 「成人完全不要介入才叫 play」不成立；來源強調 supportive scaffold。
  - 「更多 academic pressure 可取代 stress 後的 play-based recovery」不成立。
- 仍不確定之處：
  - 不同 play type、dose、duration 對 resilience / stress biology / mental health outcome 的獨立效果需查 primary studies 或 review。
  - Hospital、humanitarian、public-space and prescription examples 需分別回查 outcome evidence。
- 待處理來源：
  - 若要提升證據層級，後續可回查 AAP play clinical report、play therapy / trauma-informed intervention reviews、hospital procedural play studies。

## [2026-05-03] correction | Harvard Center — Why Sleep Matters in Early Childhood Development

- 修正原因：此來源在 2026-04-25 batch ingest 中已建立來源摘要，但未依單一來源 workflow 完整拆出 Fact / Inference / Assumption / Uncertainty，也尚未建立單一概念頁。
- 重新檢查來源：
  - `C:\原始資料\Why Sleep Matters in Early Childhood Development.md`
- 更新來源摘要：
  - `09_來源摘要/Why_Sleep_Matters_in_Early_Childhood_Development.md`
- 新增頁面：
  - `07_Pediatric_Development/Sleep_作為Early_Childhood_Developmental_Infrastructure.md`
- 更新頁面：
  - `07_Pediatric_Development/兒童睡眠與睡眠障礙總論.md`
  - `07_Pediatric_Development/嬰兒期發展.md`
  - `07_Pediatric_Development/幼兒與學齡前期發展.md`
  - `07_Pediatric_Development/Executive_Function_總論.md`
  - `index.md`
- 本輪抽出的直接事實：
  - 來源是 Harvard Center on the Developing Child 的 Brain Architects podcast transcript。
  - 訪談對象 Rebecca Spencer 是 University of Massachusetts Amherst cognitive neuroscience professor，研究 sleep functions、preschool naps and cognition。
  - 來源說 sleep has many roles，包含 immune function、growth、cognitive health、emotional health and broader physical / mental health。
  - 來源把 sleep 描述為 offline processing space，可讓 memory processing 避免與 waking input 衝突。
  - 來源指出 infants / young children 因大量新資訊與 conceptual scaffold 建立而有高 sleep need。
  - 來源說 naps protect memories；habitual nappers 若被迫不睡，memory harm and afternoon emotional reactivity 可明顯。
  - 來源把 many toddlers / preschoolers 的 nap transition 放在 roughly ages 3-5，但 transition 可波動。
  - 來源說 children may be highly sensitive to light；dim light before bedtime 支持 endogenous melatonin release。
  - 來源警告 OTC melatonin product content may not match label，且 melatonin is not a sleeping pill but a clock-setting signal。
  - 來源說 warm sleep environment can fragment sleep and reduce deep sleep，young infants cannot regulate overheating risk alone。
  - 來源指出 childcare / pre-K nap opportunity and sleep-friendly environment 應被視為 learning support。
- 移除或降級的陳述：
  - 未將 podcast 改寫成 pediatric sleep disorder guideline。
  - 未把 melatonin 討論寫成處方建議；僅保留 source-level caution and mechanism framing。
  - 未把 exact temperature / swaddling language 升格為 safe-sleep guideline。
- 發現衝突：
  - 「sleep 是 passive downtime」不成立。
  - 「nap time 自動浪費學習時間」不成立。
  - 「melatonin 是兒童入睡萬用藥」不成立。
  - 「sleep problem 只是 parent discipline issue」不成立；來源納入 light、temperature、childcare、policy and environment。
- 仍不確定之處：
  - Melatonin indication、dose、duration、formulation and safety 需依 guideline / pediatric sleep source。
  - Exact infant safe-sleep environment and swaddling advice 需回查 AAP / guideline-level source。
  - Prenatal circadian disruption 與 offspring sleep / social-emotional outcome 的強度需回查 primary studies。
- 待處理來源：
  - 若要提升 sleep 主幹證據，後續可回查 pediatric sleep guideline、AAP safe sleep guidance、preschool nap primary studies and systematic reviews。

## [2026-05-03] correction | Harvard Center — Self-Care Isn't Selfish

- 修正原因：此來源在 2026-04-25 batch ingest 中已建立來源摘要，但未依單一來源 workflow 完整拆出 Fact / Inference / Assumption / Uncertainty，也尚未建立單一概念頁。
- 重新檢查來源：
  - `C:\原始資料\Self-Care Isn’t Selfish.md`
- 更新來源摘要：
  - `09_來源摘要/Self_Care_Isnt_Selfish.md`
- 新增頁面：
  - `07_Pediatric_Development/Caregiver_Self_Care_作為Child_Stress_Buffering_Capacity.md`
- 更新頁面：
  - `07_Pediatric_Development/照顧者健康與兒童健康發展.md`
  - `07_Pediatric_Development/正向教養與家庭支持.md`
  - `07_Pediatric_Development/Toxic_Stress.md`
  - `07_Pediatric_Development/Nurturing_Care_健康與營養服務整合.md`
  - `index.md`
- 本輪抽出的直接事實：
  - 來源是 Harvard Center on the Developing Child 的 Brain Architects podcast transcript，屬 COVID-era science-translation source。
  - Interviewee Rahil Briggs 是 ZERO TO THREE HealthySteps Program 的 National Director。
  - 來源描述 pediatric primary care 是 reaching young children 的主要系統。
  - 來源說 first three years 約有 12-13 well-child visits，其中 first year 佔很大部分。
  - 來源描述 HealthySteps 是 team-based, evidence-based primary care program，加入 child-development specialist 到 primary care network。
  - HealthySteps 聚焦 birth to three、parent-child relationships、universal screening and tiered intervention。
  - 來源提出 safe, stable, nurturing relationships and routine / predictability 是 healthy families with healthy children 的 key ingredients。
  - 來源說 babies pick up on caregiver stress。
  - 來源建議 caregiver self-care、asking for help、some daily schedule、play time、screen-free time、safe outdoor time and connecting with children when caregivers are in a good place。
  - 來源明確連結 child health、caregiver health and caregiver mental health。
  - 來源討論 diapers、formula、medications、poverty、housing、community violence、air pollution and access barriers 等 social drivers of health。
- 移除或降級的陳述：
  - 未把 podcast 寫成 caregiver mental health guideline 或 parent-training RCT。
  - 未把 COVID-era telehealth service redesign 外推成常態標準。
  - 未把 HealthySteps 的 program 效果細節寫成來源未直接支持的結論。
- 發現衝突：
  - 「self-care 是 indulgence / wellness slogan」不成立。
  - 「child health 可和 caregiver mental health 切開」不成立。
  - 「給 caregiver 更多任務就是支持」不成立；來源邏輯更接近降低 overload 與連結資源。
  - 「telehealth 對 infants/toddlers 一定等同 in-person care」不成立。
- 仍不確定之處：
  - 哪些 caregiver support components 最能改善 child outcome 需回查正式研究。
  - HealthySteps effectiveness、fidelity and implementation needs 需回查 program studies / manual。
  - Caregiver mental health screening 的工具、頻率、referral threshold and safety protocol 需依正式 guidance。
- 待處理來源：
  - 若要提升證據層級，後續可回查 HealthySteps evidence、AAP caregiver depression / social needs screening guidance、integrated pediatric primary care reviews。

## [2026-05-03] correction | Harvard Center — Connecting Health & Learning

- 修正原因：此來源在 2026-04-26 batch ingest 中已建立摘要，但尚未依單一來源 workflow 完整重建 Fact / Inference / Assumption / Uncertainty，也未拆出單一概念頁。
- 重新檢查來源：
  - `C:\原始資料\Connecting Health & Learning.md`
- 更新來源摘要：
  - `09_來源摘要/Connecting_Health_and_Learning.md`
- 新增頁面：
  - `07_Pediatric_Development/Pediatric_Primary_Care_作為Health_Learning_Coordination_Platform.md`
- 更新頁面：
  - `07_Pediatric_Development/早期發展與終身健康.md`
  - `07_Pediatric_Development/照顧者健康與兒童健康發展.md`
  - `07_Pediatric_Development/Primary_Care_Developmental_Surveillance_流程.md`
  - `07_Pediatric_Development/Nurturing_Care_健康與營養服務整合.md`
  - `07_Pediatric_Development/Toxic_Stress.md`
  - `index.md`
- 本輪抽出的直接事實：
  - 來源是 Harvard Center on the Developing Child 的 Brain Architects podcast transcript，屬 science-translation source。
  - 來源將 early experiences，尤其 prenatal period 與出生後最早幾年，連到 lifelong health。
  - Stress response 被描述為 whole-body response，包含 brain、cardiovascular system、immune / inflammatory response 與 metabolic system。
  - Acute stress / inflammation 可有保護功能；persistent / chronic stress 可能造成 wear and tear，並與 chronic disease risk 相關。
  - 來源明確指出 race 是 social construct，racial / ethnic disparities 不應被解釋成 population genetics。
  - 來源把 systemic racism、discrimination 與 chronic adversity 放進 stress exposure 與 upstream prevention 脈絡。
  - 對 severe adversity 而言，來源強調 early window 包含 prenatal period 與 first 2-3 years，但也保留 never too late。
  - Panel 討論主張 children and families do not live in silos；health care 需連結 schools、child care、juvenile justice、parks and recreation、community-based organizations。
  - 來源強調 family voice，尤其 communities of color 與 children with special healthcare needs 的家庭，應參與 system design。
  - 來源以 missed early intervention evaluation 案例說明 transportation / money barrier 可阻斷服務取得，care coordinator 可辨識並處理 barrier。
  - 來源討論 care coordinators / family navigators / child navigators，可協助 health system navigation、SNAP、housing subsidies 等資源連結。
  - 來源指出 access alone is not enough；equitable outcome 需要 unpack practical barriers。
- 移除或降級的陳述：
  - 未把 podcast transcript 升格為 guideline、systematic review 或 formal medical home model。
  - 未把 chronic stress 與 chronic disease 的關聯寫成 deterministic causation。
  - 未把 family navigation / care coordination 寫成已由本來源證實有效的特定 intervention。
  - 未把 prenatal substance exposure 討論擴張成完整 FASD 或 teratology 頁面；僅保留 timing / sensitive period 的說明價值。
- 發現衝突：
  - 「child health and learning 是兩條分開路徑」不成立。
  - 「racial health disparities 可由 genetic race 解釋」不成立。
  - 「missed referral 等於 nonadherence」不成立；需先做 barrier analysis。
  - 「有 access 就自然有 equity」不成立。
- 仍不確定之處：
  - 最佳 pediatric primary care staffing model、navigator scope、payment model 與 fidelity criteria 需回查 implementation studies。
  - Family navigation 對 developmental outcome、care utilization 與 equity gap 的效果需回查正式研究。
  - 此美國 service-delivery framing 轉用到其他 health system 時需重新界定角色邊界。
- 待處理來源：
  - 後續若要提高證據層級，可回查 patient-centered medical home、HealthySteps、integrated behavioral health、SDOH screening/referral、care coordination outcome studies。

## [2026-05-04] ingest | Prime et al. 2023 — Positive Parenting and Early Childhood Cognition

- 新增來源摘要：
  - `09_來源摘要/Prime_2023_positive_parenting_early_childhood_cognition.md`
- 新增頁面：
  - `07_Pediatric_Development/Positive_Parenting_Interventions_對Early_Cognition與Language.md`
- 更新頁面：
  - `07_Pediatric_Development/正向教養與家庭支持.md`
  - `07_Pediatric_Development/Parenting_Interventions_防止兒童不當對待與強化親子關係.md`
  - `07_Pediatric_Development/Caregiving_Quality_作為早期介入靶點.md`
  - `07_Pediatric_Development/早期語言發展與Emergent_Literacy.md`
  - `07_Pediatric_Development/Executive_Function_總論.md`
  - `index.md`
- 本輪抽出的直接事實：
  - 來源為 systematic review / meta-analysis of randomized controlled trials。
  - 來源納入 79 papers，代表 61 independent samples。
  - Included trials 針對 6 歲以下 children 的 positive parenting interventions，並至少有 cognition-related outcome。
  - Outcome domains 分為 mental abilities、language、executive functioning、pre-academics。
  - Mental abilities 顯著改善：`g = 0.46`，95% CI `0.32 to 0.61`，`k = 33`，`n = 5746`。
  - Language 顯著改善：`g = 0.25`，95% CI `0.14 to 0.35`，`k = 30`，`n = 6248`。
  - Executive functioning pooled effect 不顯著：`g = 0.07`，95% CI `-0.09 to 0.23`，`k = 14`，`n = 3628`。
  - Pre-academics pooled effect 為正但不顯著：`g = 0.16`，95% CI `-0.03 to 0.34`，`k = 7`，`n = 2365`。
  - Sensitivity analyses 未實質改變 pooled estimates。
  - 所有 meta-analyses 皆有 significant heterogeneity。
  - Mental abilities analysis 中，higher risk of bias 與較大 effect size 有關。
  - Language analysis 中，較年幼 baseline age 與較大 language effect 有關。
- 移除或降級的陳述：
  - 未把 positive parenting 寫成全面 cognitive enhancer。
  - 未把 mental abilities / language 的 benefit 外推成 direct EF 或 pre-academic improvement。
  - 未把 father involvement moderator 解讀成 causal harm；僅標記研究數少、參與程度不明與同時建模後不穩定。
- 發現衝突：
  - 「positive parenting 對所有 early cognitive domains 都一樣有效」不成立。
  - 「parent coaching 可取代 formal language delay evaluation」不成立。
  - 「general positive parenting 已被證實可直接治療 EF problem」不成立。
- 待追蹤問題：
  - 哪些 active ingredients 最能驅動 mental abilities / language benefit 仍不確定。
  - Mediation analysis 無法 pooled；mechanism 仍需後續研究。
  - EF / pre-academic outcomes 研究數較少且 measurement heterogeneity 較高。
  - Father-inclusive intervention、adolescent parents、caregiver mental health difficulties 與非英語研究仍需補強。
- 待處理來源：
  - `C:\原始資料\247.full\247.full.md`
  - `C:\原始資料\journal.pmed.1003602\journal.pmed.1003602.md`
  - `C:\原始資料\fpsyg-10-02812\fpsyg-10-02812.md`
  - `C:\原始資料\Maroto-Izquierdoetal.2024.RIRforspecialpopulations\Maroto-Izquierdoetal.2024.RIRforspecialpopulations.md`

## [2026-05-04] ingest | Hirve et al. 2023 — Healthcare provider-delivered ECD interventions

- 新增來源摘要：
  - `09_來源摘要/Hirve_2023_HCP_ECD_interventions_cognitive_outcomes.md`
- 新增頁面：
  - `07_Pediatric_Development/HCP_ECD_Interventions_由健康照護者交付的早期發展介入.md`
- 更新頁面：
  - `07_Pediatric_Development/Caregiving_Quality_作為早期介入靶點.md`
  - `07_Pediatric_Development/Nurturing_Care_健康與營養服務整合.md`
  - `07_Pediatric_Development/Pediatric_Primary_Care_作為Health_Learning_Coordination_Platform.md`
  - `07_Pediatric_Development/Early_Intervention_總論.md`
  - `index.md`
- 本輪抽出的直接事實：
  - 來源為 systematic review / meta-analysis，題名為 `Effect of early childhood development interventions delivered by healthcare providers to improve cognitive outcomes in children at 0-36 months: a systematic review and meta-analysis`。
  - 來源使用 `C:\原始資料\247.full\247.full.md`，本輪未混入其他來源。
  - 來源納入 97 papers reporting 42 trials in narrative synthesis，27 trials in meta-analyses。
  - Abstract 報告 42 RCTs with 15,557 infants；results section 報告 15,661 infants in 41 trials，來源內部計數不一致，本輪未自行修正。
  - Eligible HCP-ECD interventions 由 primary-level healthcare providers face-to-face delivered，可透過 home visits、mobile health team visits、clinic visits、child health checks 或 group programmes。
  - Intervention components 分為 responsive caregiving、early learning support、motor stimulation。
  - 40 trials 使用 home visits，2 trials 使用 community clinics。
  - Contacts ranged from 6 to 312，median 25，IQR 9-52。
  - Pooled cognitive outcome at 0-36 months：BSID-III MD 2.65，95% CI 0.61 to 4.70，n = 2482，low certainty。
  - Motor outcome：BSID-III MD 4.01，95% CI 1.54 to 6.48，n = 1437；abstract 與 results section 對 certainty 標示不完全一致。
  - HOME inventory improved：MD 1.37，95% CI 0.29 to 2.45，n = 1534，low certainty。
  - Maternal mental health 沒有明確改善：SMD -0.13，95% CI -0.29 to 0.03，n = 2806。
  - Speech/language、socioemotional、behaviour outcomes 沒有明確改善。
  - No studies reported executive functioning or adaptive functioning outcomes。
  - Subgroup analyses 未顯示 number of contacts、timing、intervention type、HCP type、country income level 或 risk of bias 的明確 differential effect；唯一 signal 是 ECD-predominant interventions。
  - No visit-number dose-response was found。
- 移除或降級的陳述：
  - 未把 HCP-ECD 寫成完整 Early Intervention service system。
  - 未把 visit count 當成有效 intervention dose。
  - 未把 cognitive / motor signal 外推為 language、EF、adaptive function 或 maternal mental health benefit。
  - 未把 low-certainty cognitive evidence 寫成 guideline-level standard of care。
- 發現衝突：
  - 「healthcare contact 次數越多就越能改善 development」不成立；來源未發現 visit-number dose-response。
  - 「HCP-ECD 可取代 caregiver mental health treatment」不成立；maternal mental health 沒有明確改善。
  - 「cognition 有改善就代表 language / EF 也改善」不成立；language outcome 不明確，EF / adaptive function 未報告。
  - 「HCP-ECD 等同 EI」不成立；HCP-ECD 是 health-system delivery model，不是完整 IFSP / therapy / specialist service system。
- 待追蹤問題：
  - HCP-ECD 的 active ingredient 是 responsive caregiving、early learning、motor stimulation、home visiting、provider relationship，還是 ECD-predominant contact time，仍不確定。
  - 是否能外推到 universal well-child care、older preschoolers、developmental disability population 或台灣 health system，需要另外來源。
  - 語言、EF、adaptive function 與 caregiver mental health outcome 需後續更高品質研究或 domain-specific sources。
- 待處理來源：
  - `C:\原始資料\journal.pmed.1003602\journal.pmed.1003602.md`
  - `C:\原始資料\fpsyg-10-02812\fpsyg-10-02812.md`
  - `C:\原始資料\Maroto-Izquierdoetal.2024.RIRforspecialpopulations\Maroto-Izquierdoetal.2024.RIRforspecialpopulations.md`

## [2026-05-04] ingest | Jeong et al. 2021 — Parenting interventions to promote ECD in the first three years

- 新增來源摘要：
  - `09_來源摘要/Jeong_2021_parenting_interventions_ECD_first_three_years.md`
- 新增頁面：
  - `07_Pediatric_Development/Parenting_Interventions_生命前三年ECD與Caregiving_Outcomes.md`
- 更新頁面：
  - `07_Pediatric_Development/正向教養與家庭支持.md`
  - `07_Pediatric_Development/Parenting_Interventions_防止兒童不當對待與強化親子關係.md`
  - `07_Pediatric_Development/Caregiving_Quality_作為早期介入靶點.md`
  - `index.md`
  - `log.md`
- 本輪抽出的直接事實：
  - 來源為 systematic review / meta-analysis of RCTs。
  - 來源使用 `C:\原始資料\journal.pmed.1003602\journal.pmed.1003602.md`，本輪未混入其他來源。
  - Final set included 111 articles representing 102 unique RCTs。
  - Trials implemented across 33 countries：61 trials in HICs，41 trials in LMICs。
  - Included interventions targeted pregnancy through the first 3 years of life and measured at least one ECD outcome。
  - Pooled effects were positive for cognitive development：SMD 0.32，95% CI 0.23 to 0.40。
  - Language development：SMD 0.28，95% CI 0.18 to 0.37。
  - Motor development：SMD 0.24，95% CI 0.15 to 0.32。
  - Socioemotional development：SMD 0.19，95% CI 0.10 to 0.28。
  - Behavior problems decreased：SMD -0.13，95% CI -0.18 to -0.08。
  - Infant-caregiver attachment：SMD 0.29，95% CI 0.18 to 0.40。
  - Parenting knowledge：SMD 0.56，95% CI 0.33 to 0.79。
  - Parenting practices：SMD 0.33，95% CI 0.22 to 0.44。
  - Parent-child interactions：SMD 0.39，95% CI 0.24 to 0.53。
  - Parental depressive symptoms did not significantly improve：SMD -0.07，95% CI -0.16 to 0.02，P = 0.08。
  - 70/102 interventions included responsive caregiving content。
  - Responsive caregiving content showed greater effects on child cognitive development、parenting knowledge、parenting practices、parent-child interactions。
  - Egger's tests suggested small-sample bias for child language development and parent-child interactions。
- 移除或降級的陳述：
  - 未把 parenting intervention 寫成所有 ECD domains 的等量改善。
  - 未把 parenting intervention 寫成 caregiver depression treatment。
  - 未把 home visiting、group、clinic、duration 或 age timing 寫成固定優勢，因為本來源沒有穩定支持。
  - 未把 responsive caregiving 解讀成唯一 active ingredient。
- 發現衝突：
  - 「parenting intervention = 一次性衛教」不成立；來源處理的是 structured programs。
  - 「parenting intervention 可取代 EI / developmental therapy」不成立；本來源只支持 parenting-focused developmental support。
  - 「親職介入會自然改善 caregiver depression」不成立；pooled depressive symptom effect 未顯著。
- 待追蹤問題：
  - Which active ingredients best drive child outcomes remains uncertain。
  - Long-term sustainability、fadeout、booster sessions、cost-effectiveness、father-inclusive design、scale-up fidelity 仍需補強。
  - Local adaptation 與 outcome measurement validity 需後續來源支持。
- 待處理來源：
  - `C:\原始資料\fpsyg-10-02812\fpsyg-10-02812.md`
  - `C:\原始資料\Maroto-Izquierdoetal.2024.RIRforspecialpopulations\Maroto-Izquierdoetal.2024.RIRforspecialpopulations.md`

## [2026-05-04] ingest | Scionti et al. 2020 — Preschool EF cognitive training

- 新增來源摘要：
  - `09_來源摘要/Scionti_2020_preschool_EF_cognitive_training.md`
- 新增頁面：
  - `07_Pediatric_Development/Preschool_EF_Cognitive_Training與Transfer.md`
- 更新頁面：
  - `07_Pediatric_Development/Executive_Function_總論.md`
  - `index.md`
  - `log.md`
- 本輪抽出的直接事實：
  - 來源為 systematic review / meta-analysis。
  - 來源使用 `C:\原始資料\fpsyg-10-02812\fpsyg-10-02812.md`，本輪未混入其他來源。
  - 題名為 `Is Cognitive Training Effective for Improving Executive Functions in Preschoolers? A Systematic Review and Meta-Analysis`。
  - 研究對象為 3-6 歲 preschool children。
  - Final dataset included 27 papers, 32 studies, and 123 EF effect sizes。
  - Overall EF training effect: `g = 0.342`, 95% CI `0.252 to 0.451`, `p < 0.001`。
  - Heterogeneity was significant: `Q(122) = 172.340`, `p < 0.001`。
  - Near EF transfer: `g = 0.352`, 95% CI `0.252 to 0.451`, `p < 0.001`。
  - Far EF transfer: `g = 0.318`, 95% CI `0.186 to 0.449`, `p < 0.001`。
  - Near vs far EF transfer difference was not significant: `p = 0.619`。
  - Non-EF outcomes were not significant overall: `g = 0.169`, 95% CI `-0.047 to 0.383`, `p = 0.122`。
  - Developmental risk status moderated effect size: `p = 0.033`。
  - No-risk samples: `g = 0.291`, 95% CI `0.192 to 0.390`。
  - Low-SES samples: `g = 0.430`, 95% CI `0.219 to 0.641`。
  - ADHD-symptom samples: `g = 0.785`, 95% CI `0.451 to 1.120`。
  - At-risk evidence base was small：ADHD symptoms 4 studies / 8 effects / 112 participants；low SES 4 studies / 7 effects / 651 participants。
  - Child age within the preschool range was not a significant moderator。
  - Active vs passive control did not significantly moderate effects。
  - Group training showed larger effects than individual training。
  - Number of sessions was not significant, but total training length in minutes was significant。
- 移除或降級的陳述：
  - 未把 EF cognitive training 寫成 school readiness、learning、behavior 或 ADHD 的標準治療。
  - 未把 far EF transfer 外推成 non-EF transfer。
  - 未把 ADHD subgroup 的 large effect size 寫成強結論，因為 study number small。
  - 未把 computerized training 寫成優於 non-computerized training。
- 發現衝突：
  - 「EF training 完全沒有 preschool far transfer」不成立；此來源支持 EF task domain 之間的 far transfer。
  - 「EF training 能自然改善 learning / behavior」不成立；此來源 non-EF outcomes 未達顯著。
  - 「EF training 可取代 ADHD / developmental differential」不成立。
- 待追蹤問題：
  - preschool far EF transfer 有多少來自真實 cross-domain EF change，有多少來自 task impurity，仍不確定。
  - 長期維持、ecological validity、classroom participation 與 school achievement outcome 仍需更高品質研究。
  - ASD、language impairment、developmental coordination disorder 與 complex adversity child 尚缺資料。
- 待處理來源：
  - `C:\原始資料\Maroto-Izquierdoetal.2024.RIRforspecialpopulations\Maroto-Izquierdoetal.2024.RIRforspecialpopulations.md`

## [2026-05-04] ingest | Maroto-Izquierdo et al. 2024 — Repetitions in Reserve for special populations

- 新增來源摘要：
  - `09_來源摘要/Maroto_2024_RIR_special_populations.md`
- 新增頁面：
  - `02_方法學/Repetitions_in_Reserve_RIR_阻力訓練強度處方.md`
- 更新頁面：
  - `02_方法學/治療性運動處方.md`
  - `02_方法學/治療性運動處方的最低必要欄位.md`
  - `index.md`
  - `log.md`
- 本輪抽出的直接事實：
  - 來源為 practical narrative review with synthesis of RIR validation literature。
  - 來源使用 `C:\原始資料\Maroto-Izquierdoetal.2024.RIRforspecialpopulations\Maroto-Izquierdoetal.2024.RIRforspecialpopulations.md`，本輪未混入其他來源。
  - 題名為 `Repetitions in Reserve: An Emerging Method for Strength Exercise Prescription in Special Populations`。
  - 來源比較 `%1RM`、velocity-based training、RPE / effort perception 與 RIR 作為 resistance training intensity indicators。
  - `%1RM` 與 X-RM 在 special populations 可能帶來 repeated testing risk、fatigue、recovery burden、inaccuracy and adherence problems。
  - velocity-based training 需要 valid equipment、time investment、exercise-specific force-velocity profile，且不易套用到某些 non-linear / functional exercises。
  - RPE 可跨場域使用，但受熟悉度、提問方式、施測時間、疲勞與 exercise type 影響。
  - RIR 定義為 possible repetitions 與 completed repetitions 的差距。
  - 來源列出三類 RIR scales：ERF scale、RPE-RIR scale、effort character。
  - 來源描述 RIR validation literature mostly comes from non-clinical populations，包括 resistance-trained participants、novices or athletic contexts。
  - 來源明確指出 RIR validity and reliability have not been extensively tested across different special populations。
  - 來源指出 clinical contexts 中應用 RIR 的研究仍 scarce。
  - practical proposal 包含 four effort levels，連結 completed / possible repetitions、RPE 0-10 與 velocity-loss logic。
  - strength example：完成 8RM 負荷但第 6 下停止，等於保留 2 reps before mechanical failure，約 high effort / RPE 7-8/10。
  - muscular endurance example：完成約 half of possible reps，約 moderate effort / RPE 4-6/10。
  - conclusion 主張 RIR promising，但需要 validity、reliability、feasibility、familiarization protocol 與 application standards。
- 移除或降級的陳述：
  - 未把 RIR 寫成 guideline-level standard。
  - 未把 athletic / healthy-subject validity evidence 外推成所有 special populations 已驗證。
  - 未把 RIR 當成完整 therapeutic exercise prescription。
  - 未把 training to failure 或 RIR 0 當成 clinical default。
- 發現衝突：
  - 「resistance training intensity 只能用 %1RM」不成立；RIR 可作為另一種 intensity language。
  - 「RIR 已在所有 special populations 驗證」不成立；來源自己標示證據不足。
  - 「有 RIR 就不需要 safety screening」不成立；RIR 只控制 proximity to failure。
- 待追蹤問題：
  - 不同疾病族群的 target RIR、progression speed、stop criteria 與 adverse event risk 仍需 disease-specific validation。
  - unsupervised home program 中 RIR 的 comprehension、accuracy、safety and adherence 仍不確定。
  - RIR 與 long-term functional outcome、strength gain、symptom flare、participation 的關係仍待研究。
- 待處理來源：
  - 待重新盤點 `C:\原始資料` 中尚未進入單一來源 workflow 的來源。

## [2026-05-04] ingest | WHO 2020 — Improving early childhood development guideline

- 新增來源摘要：
  - `09_來源摘要/WHO_2020_improving_early_childhood_development_guideline.md`
- 新增頁面：
  - `07_Pediatric_Development/WHO_ECD_Guideline_0至3歲Nurturing_Care建議.md`
- 更新頁面：
  - `07_Pediatric_Development/Nurturing_Care_健康與營養服務整合.md`
  - `07_Pediatric_Development/Caregiving_Quality_作為早期介入靶點.md`
  - `07_Pediatric_Development/Early_Intervention_總論.md`
  - `07_Pediatric_Development/照顧者健康與兒童健康發展.md`
  - `index.md`
  - `log.md`
- 本輪抽出的直接事實：
  - 來源為 WHO guideline。
  - 來源使用 `C:\原始資料\9789240002098-eng\9789240002098-eng.md`，本輪未混入其他來源。
  - 題名為 `Improving early childhood development: WHO guideline`。
  - 來源提供 global evidence-informed recommendations on improving ECD。
  - Recommendations intended audience includes policy-makers、development agencies、implementing partners、district and sub-national health managers、health workers and NGOs。
  - Recommendation 1：all infants and children should receive responsive care during the first 3 years；parents and other caregivers should be supported to provide responsive care。
  - Recommendation 1 strength strong；certainty moderate for responsive care。
  - Recommendation 2：all infants and children should have early learning activities with parents and other caregivers during the first 3 years；caregivers should be supported to engage in early learning。
  - Recommendation 2 strength strong；quality moderate for early learning。
  - Recommendation 3：support for responsive care and early learning should be included as part of interventions for optimal nutrition of infants and young children。
  - Recommendation 3 strength strong；quality moderate。
  - Recommendation 4：psychosocial interventions to support maternal mental health should be integrated into early childhood health and development services。
  - Recommendation 4 strength strong；certainty moderate。
  - Early learning intervention evidence included 22 RCTs, mostly HICs。
  - Early learning cognitive effect：SMD 0.20，95% CI 0.01 to 0.39；certainty low。
  - Early learning language effect was not significant：SMD 0.07，95% CI -0.11 to 0.24；certainty low。
  - Early learning motor effect：SMD 0.32，95% CI 0.12 to 0.52；certainty low。
  - Early learning behaviour-problem effect was not significant：SMD -0.25，95% CI -0.54 to 0.04；certainty very low。
  - Caregiving interventions for socioemotional and behavioural development did not receive a recommendation；GDG prioritized future research。
  - Socioemotional / behavioural caregiving evidence came from 10 studies, all HICs。
  - Combined caregiving and nutrition interventions included 18 studies, all LMICs。
  - Combined caregiving and nutrition versus standard care improved cognitive development：SMD 0.57，95% CI 0.32 to 0.82；language：SMD 0.40，95% CI 0.17 to 0.63；motor：SMD 0.40，95% CI 0.26 to 0.53。
  - HAZ and WAZ generally showed no significant benefit；some WHZ comparisons showed benefits。
  - Psychosocial maternal mental health interventions improved maternal anxiety symptoms：SMD -0.51，95% CI -0.72 to -0.30。
  - Psychosocial maternal mental health interventions improved maternal depressive symptoms：SMD -0.70，95% CI -0.92 to -0.47。
  - Child-development outcomes in maternal mental health intervention studies were limited and less consistently measured。
- 移除或降級的陳述：
  - 未把 strong recommendations 寫成所有 child outcomes 都 high-certainty。
  - 未把 early learning intervention 寫成 clearly effective for language or behaviour problems。
  - 未把 nutrition intervention alone 寫成足以改善 ECD。
  - 未把 maternal mental health psychosocial intervention 寫成直接 child developmental treatment。
  - 未把 first-3-years health-sector ECD support 寫成可取代 formal EI、developmental evaluation、child protection 或 specialist mental health referral。
- 發現衝突：
  - 「health / nutrition services 只需處理 biomedical endpoints」不符合 WHO 2020 guideline。
  - 「有做 nutrition 就等於支持 ECD」不成立；guideline 要求 responsive care 與 early learning integration。
  - 「parenting / caregiving intervention 可用單一最佳 programme 解決」不成立；來源明確限制 programme comparisons。
- 待追蹤問題：
  - 2020 guideline 原文規劃五年 review；政策使用前需確認是否已有新版或補充 guidance。
  - Responsive caregiving、early learning 與 socioemotional / behavioural intervention 的 definitions、active ingredients、dose、delivery model、long-term outcomes 仍需研究。
  - Maternal mental health interventions 需要更多 child health and development outcomes。
  - Outcome tools 在不同 sociocultural contexts 的 reliability / validity 仍是主要限制。
- 待處理來源：
  - 重新盤點後排除已處理與明顯 duplicate 來源，再選下一篇最高優先單一來源。

## [2026-05-04] ingest | Muir et al. 2023 — Preschool SR/EF interventions

- 新增來源摘要：
  - `09_來源摘要/Muir_2023_preschool_SR_EF_interventions.md`
- 新增頁面：
  - `07_Pediatric_Development/Preschool_SR_EF_Intervention_Design特徵.md`
- 更新頁面：
  - `07_Pediatric_Development/學齡前期的自我調節與school_readiness.md`
  - `07_Pediatric_Development/Preschool_EF_Cognitive_Training與Transfer.md`
  - `07_Pediatric_Development/Executive_Function_總論.md`
  - `07_Pediatric_Development/學前SEL介入的分層與情境堆疊.md`
  - `index.md`
  - `log.md`
- 本輪抽出的直接事實：
  - 來源為 systematic literature review。
  - 來源使用 `C:\原始資料\s10648-023-09740-6\s10648-023-09740-6.md`，本輪未混入其他來源。
  - 題名為 `Interventions and Approaches Targeting Early Self-Regulation or Executive Functioning in Preschools: A Systematic Review`。
  - 來源遵循 PRISMA-P，並登錄於 PROSPERO。
  - Search performed on 2020-09-28 and re-searched January 2021。
  - Included peer-reviewed English-language intervention studies from 2000 to 2020。
  - Included typically developing preschool children aged 3-6 years in preschool settings。
  - Studies focused exclusively on children with documented disabilities such as Attention Deficit Disorder were excluded。
  - Initial search generated 9115 results；3288 duplicates were identified；641 full texts were obtained；85 studies were included。
  - Included studies sampled 12,595 children。
  - 72 of 85 studies (84.7%) were published between 2015 and 2020。
  - 59 studies (69.4%) targeted EF only；17 targeted SR only；9 targeted both SR and EF。
  - Median intervention dose was 9 hours，but dose ranged from one 15-minute period to year-long curricula。
  - Statistically significant results for at least one outcome were reported in 60 studies (70.6%)。
  - Across 208 evaluated effects, 102 (49.0%) were statistically significant immediately after intervention。
  - Only four studies included follow-up assessments several months after intervention。
  - The review classified interventions into play、social-emotional、curricula / pedagogy、and non-routine activities。
  - Mediated structured play：16 studies；12 reported significant acute effects；26 of 41 evaluated effects were significant。
  - Mindfulness：12 studies；10 reported significant outcomes；17 of 26 evaluated effects were significant。
  - SEL programmes：8 studies；6 reported at least one significant outcome；11 of 23 evaluated effects were significant。
  - Digital task training：9 studies；5 reported at least one significant EF outcome；7 of 21 evaluated effects were significant。
  - Physical activity：12 studies；10 reported at least one significant outcome；14 of 20 evaluated effects were significant。
  - Cognitive challenge was present in all interventions identified as most efficacious。
  - Movement appeared in 53 studies (62.35%)；77.4% of these interventions achieved one or more significant effects。
  - 23 movement-including interventions were classified as highly efficacious, representing 63.88% of all high-efficacy interventions。
  - The review did not conduct meta-analysis due to high intervention heterogeneity and the aim of identifying effective characteristics。
  - Fidelity was often unreported and not evaluated in a common format。
- 移除或降級的陳述：
  - 未把 preschool SR/EF intervention 寫成單一最佳 approach。
  - 未把 cognitive challenge 寫成足以保證 broad transfer。
  - 未把 digital task training 寫成 superior classroom SR/EF intervention。
  - 未把 acute post-test gains 外推為 long-term school readiness 或 participation gains。
  - 未把 typically developing preschool evidence 外推到 ADHD、ASD、ID、language disorder、trauma-exposed 或 complex clinical populations。
- 發現衝突：
  - 「SR/EF 只能靠某一類 programme 改善」不成立；來源顯示各 approach 都有 some potential efficacy。
  - 「movement intervention 只看活動量」不成立；來源較支持 cognitively engaging movement 的設計邏輯。
  - 「teacher-led 就自然可擴散」不成立；teacher PD、coaching、fidelity、ratio、time 與 leadership support 仍是限制。
- 待追蹤問題：
  - Long-term maintenance、fadeout、transfer to participation / academic / classroom outcomes 仍需 follow-up studies。
  - Active component、fidelity reporting、dose、teacher training、coaching 與 implementation burden 需要更清楚報告。
  - Different child baseline、sex、income、language background and other moderators require better demographic reporting。
- 待處理來源：
  - `C:\原始資料\TBI Umphred's Neurological Rehabilitation, 22, 629-670\TBI Umphred's Neurological Rehabilitation, 22, 629-670.md`
  - `C:\原始資料\Sexual Dysfunction in Neurological Disorders\Sexual Dysfunction in Neurological Disorders.md`
  - `C:\原始資料\Lower limb pain and dysfunction\Lower limb pain and dysfunction.md`

## [2026-05-04] ingest | Courtois & Cordeau — Sexual Dysfunction in Neurological Disorders

- 新增來源摘要：
  - `09_來源摘要/Courtois_Cordeau_neurological_sexual_dysfunction.md`
- 新增頁面：
  - `03_疾病與臨床主題/Neurogenic_Sexual_Dysfunction_三層影響框架.md`
- 更新頁面：
  - `03_疾病與臨床主題/性功能障礙與身心障礙復健.md`
  - `index.md`
  - `log.md`
- 本輪抽出的直接事實：
  - 來源為 textbook chapter。
  - 來源使用 `C:\原始資料\Sexual Dysfunction in Neurological Disorders\Sexual Dysfunction in Neurological Disorders.md`，本輪未混入其他來源。
  - 題名為 `Sexual Dysfunction in Neurological Disorders`。
  - 作者為 Frédérique Courtois 與 Dany Cordeau。
  - 章節把 neurological disorders 對 sexual function 的影響分為 primary、secondary、tertiary impacts。
  - Primary impacts 指 neurological lesion 對 sexual function 的直接影響。
  - Secondary impacts 指其他與 sexuality 有關的 body functions 受影響，以及 medication side effects。
  - Tertiary impacts 指 psychosocial aspects 減少 social contacts 並干擾 sexual relationships。
  - Male reflexogenic erection 主要由 genital stimulation 經 S2-S4 mediated。
  - Male psychogenic erection 可經 sacral pathway 或 T11-L2 thoracolumbar pathway。
  - Ejaculation 包含 emission 與 expulsion；emission 主要牽涉 thoracolumbar innervation，expulsion 主要牽涉 sacral spinal segments 與 perineal nerves。
  - Spinal generator of ejaculation 位於 L3-L4。
  - Female sexual response 除 classical arousal / plateau / orgasm / resolution phases 外，也涉及 motivational、emotional、experiential、developmental factors。
  - SCI sexual outcome 受 lesion level 與 completeness 影響。
  - SCI orgasm 可在沒有 ejaculation 的情況下發生；ejaculation / orgasm 伴隨 headache 或 severe hypertension 時需考慮 autonomic dysreflexia。
  - MS sexual dysfunction 常和 desire、genital sensation、arousal / lubrication、erectile / ejaculatory / orgasmic symptoms、fatigue、spasticity、bladder / bowel、pain、medication、mood、cognition、relationship quality 交疊。
  - Stroke 後可能出現 hypoactive sexual desire、reduced intercourse frequency、erectile / ejaculatory dysfunction、decreased lubrication、diminished orgasm、motor limitation、sensory change、pain、fatigue、fear、depression 與 partner dynamics。
  - TBI 可造成 hyposexuality、ED、orgasmic problems、reduced satisfaction，也可造成 inappropriate sexual behavior；pituitary deficits after TBI 在來源中被列為需考慮的 hormonal contributor。
  - PD 可出現 decreased or increased libido、arousal disorder、ED、orgasm dysfunction、hypersexuality 或 compulsive sexual behaviors；dopaminergic therapy 可與 hypersexuality / impulse-control problems 有關。
  - 治療選項涵蓋 ED medications / injections / devices、ejaculation / fertility procedures、lubricants、clitoral vacuum devices、vibrostimulation、positioning、adaptive equipment、pain / fatigue / spasticity planning、medication review、psychosocial intervention、education、peer support、CBT-style strategies 與 relationship counseling。
- 移除或降級的陳述：
  - 未把 textbook chapter 寫成 formal guideline。
  - 未把 neurogenic sexual dysfunction 簡化成 ED。
  - 未把 lesion level 寫成足以單獨預測 sexual outcome。
  - 未把 PDE5 inhibitors、devices 或 procedures 寫成完整 sexual rehabilitation。
  - 未把 female sexual dysfunction 由 male erection / ejaculation framework 直接外推。
  - 未把 novel ED treatments 寫成 neurological populations 的 established routine treatment。
- 發現衝突：
  - 「sexual dysfunction after neurological disorder 主要就是神經路徑斷掉」不完整；來源要求同時看 primary、secondary、tertiary effects。
  - 「psychosocial effects 是附帶問題」不成立；tertiary effects 可直接限制 intimacy、relationship 與 social participation。
  - 「有 pharmacologic ED treatment 就等於完成 rehab」不成立；secondary 與 tertiary barriers 仍需處理。
- 待追蹤問題：
  - 不同 neurological diagnoses 的 sexual dysfunction prevalence 與 intervention evidence 需逐疾病回查更高層級或更新 guideline。
  - Female neurogenic sexual dysfunction 的 condition-specific treatment evidence 仍不足。
  - Stroke lesion-location association、TBI endocrine contribution、PD dopaminergic hypersexuality 的適用條件需更細分。
- 待處理來源：
  - `C:\原始資料\TBI Umphred's Neurological Rehabilitation, 22, 629-670\TBI Umphred's Neurological Rehabilitation, 22, 629-670.md`
  - `C:\原始資料\Lower limb pain and dysfunction\Lower limb pain and dysfunction.md`

## [2026-05-04] ingest | Reina-Guerra — Traumatic Brain Injury

- 新增來源摘要：
  - `09_來源摘要/Reina_Guerra_TBI_Umphred_neurorehabilitation.md`
- 新增頁面：
  - `03_疾病與臨床主題/TBI_ICF照護連續體與Task_Analysis.md`
- 更新頁面：
  - `03_疾病與臨床主題/創傷性腦損傷復健總論.md`
  - `03_疾病與臨床主題/TBI_意識障礙與神經行為管理.md`
  - `index.md`
  - `log.md`
- 本輪抽出的直接事實：
  - 來源為 textbook chapter。
  - 來源使用 `C:\原始資料\TBI Umphred's Neurological Rehabilitation, 22, 629-670\TBI Umphred's Neurological Rehabilitation, 22, 629-670.md`，本輪未混入其他來源。
  - 題名為 `Traumatic Brain Injury`。
  - 作者為 Sandra G. Reina-Guerra。
  - 章節焦點為 moderate to severe TBI rehabilitation；mTBI / concussion 另章處理。
  - TBI 是 sudden external force 導致 normal brain function disruption，需與 stroke、anoxic brain injury 等 acquired brain injuries 區分。
  - TBI mechanisms 包含 direct external force、acceleration-deceleration、blast injury、penetrating injury。
  - Primary injury 是 initial mechanical insult；secondary injury 是 primary injury 後的 biochemical、cellular、physiologic events。
  - Secondary injury contributors 包含 increased ICP、cerebral hypoxia / ischemia、intracranial hemorrhage、electrolyte / acid-base imbalance、infection、seizure、neuroinflammation。
  - Pediatric TBI 的 anatomical / physiologic differences 使 medical management 複雜；developing brain neuroplasticity 不代表預後自然較好。
  - 來源指出 childhood severe TBI 後約 62% 兒童有 lingering cognitive and behavioral difficulties，影響 education 與 social participation。
  - 來源指出 timely and aggressive inpatient rehabilitation 是改善 moderate to severe pediatric TBI functional outcome 的 significant factor。
  - Prognostic indicators 包含 age、clinical severity、pupil reactivity、CT abnormalities、secondary insults、laboratory values、duration of coma、PTA、Time to Follow Commands。
  - 來源明確指出 no single instrument can accurately predict outcomes。
  - CRASH / IMPACT models 可用早期變數預測 outcomes，但被批評未納入 secondary insults 與 treatment response。
  - PTA duration 可作 functional prognostic indicator；來源指出 PTA < 4 weeks 時 severe activity limitation unlikely，PTA > 8 weeks 時 good recovery unlikely by GOS。
  - TBI Model Systems data：moderate to severe TBI 中約 30% within 5 years worsen，約 26% stayed home，約 22% died，仍存活者約 57% 有 moderate to severe disability。
  - 來源引述 five-year unemployment after TBI 為 55%。
  - 章節使用 WHO ICF framework 組織 examination、evaluation、intervention、outcomes across care environments。
  - TBI outcomes 依賴 injury location / severity，也依賴 prior function、support systems、timing and quality of healthcare interventions。
  - Examination / evaluation history 應包含 mechanism / nature of injury、initial GCS、injury date、age、medical interventions、duration of unconsciousness、stage of consciousness、overall recovery progress。
  - RLA I-II / coma or VS 的 examination 偏 body functions；RLA III 可能開始 simple command response；RLA IV-VI 的 agitation / confusion 會 guide examination and interventions；consciousness 改善後轉向 Activities and Participation。
  - Activity limitation 評估需 task analysis；改善 abnormal components 不一定改善 activity limitation，treating impairments 不一定讓病人學會 skill。
  - Skill learning 需要 whole-task practice。
  - Acute priorities 包含 preservation of life and neural tissue、secondary complication prevention、early mobility、arousal / awareness support for DoC。
  - Across settings 要預防 pneumonia、pressure sores、adaptive shortening、disuse atrophy、HO、joint contractures、DVT。
  - Interprofessional rehabilitation 是 moderate to severe TBI comprehensive care 的核心。
  - Sensory stimulation 在 DoC 常用，但 systematic reviews 未建立強證據，限制來自 poor study quality、variable study design、inconsistent outcome measures。
  - Motor rehab 應強調 intense, repetitive, task-oriented training；treadmill training 不明顯優於 overground training。
  - VR evidence in TBI 為 emerging but limited；conventional therapy groups 通常也有類似 outcomes。
  - Visual-vestibular examination should be included after TBI；TBI 可造成 peripheral、central 或 mixed vestibular pathology。
  - Aerobic exercise 可能有 neuroplasticity、physical function、cognition、mood、sleep、secondary health prevention benefit，但 acute timing / intensity 要謹慎。
  - Dual-task deficits 可在 gait speed normal 時仍存在；dual-task training 應依 life-role and environmental demands 具體設計。
  - NBS / TMS / tDCS 為 emerging approaches；TBI 後 seizure risk 與有限 evidence 需謹慎。
- 移除或降級的陳述：
  - 未把 GCS、CT、CRASH / IMPACT 或任何單一工具寫成足以精準預測個人 outcome。
  - 未把 isolated impairment correction 寫成足以改善 activity / participation。
  - 未把 early mobility 寫成不需 medical constraints 的越早越好。
  - 未把 pediatric neuroplasticity 寫成較佳自然恢復保證。
  - 未把 sensory stimulation、VR、robotics、NBS 或 aerobic exercise 寫成高確定性標準治療。
  - 未把 treadmill training 寫成優於 overground gait training。
- 發現衝突：
  - 「TBI rehab 只要依 impairment 列表逐項治療」不成立；來源要求 ICF、phase of recovery、task analysis 與 participation goals。
  - 「直線 gait speed 正常就代表 community mobility 安全」不成立；dual-task 和 environmental demands 仍可能限制 participation。
  - 「兒童 TBI 早期身體恢復好就不需長期追蹤」不成立；後續 developmental and school demands 可揭露長期問題。
- 待追蹤問題：
  - TBI-specific intervention dose、timing、intensity、VR / robotics / NBS / aerobic exercise evidence 需後續用 guideline 或 systematic review 校正。
  - Pediatric TBI long-term school / executive / social participation outcomes 需獨立拆頁。
  - Chronic brain injury / periodic therapy model 需要更高層級來源確認。
- 待處理來源：
  - `C:\原始資料\Lower limb pain and dysfunction\Lower limb pain and dysfunction.md`

## [2026-05-04] ingest | Caldwell, Hamner & Hupe — Lower Limb Pain and Dysfunction

- 新增來源摘要：
  - `09_來源摘要/Caldwell_Hamner_Hupe_Lower_Limb_Pain_Dysfunction.md`
- 新增頁面：
  - `03_疾病與臨床主題/Lower_Limb_Pain_分區定位與高風險分流.md`
- 更新頁面：
  - `03_疾病與臨床主題/跑者下肢傷害評估總論.md`
  - `03_疾病與臨床主題/足部疼痛分區評估.md`
  - `index.md`
  - `log.md`
- 本輪抽出的直接事實：
  - 來源為 textbook chapter。
  - 來源使用 `C:\原始資料\Lower limb pain and dysfunction\Lower limb pain and dysfunction.md`，本輪未混入其他來源。
  - 題名為 `Lower Limb Pain and Dysfunction`。
  - 作者為 Mary E. Caldwell、Troy Hamner、Jessica Hupe。
  - 章節以 history 與 clinical examination 的 sequential process 組織 lower limb pain，而非涵蓋所有可能疾病。
  - Hip pain 可表現為 groin、buttock、lateral hip / greater trochanteric region、low back、thigh pain。
  - Hip pain 可分 anterior、lateral、posterior、medial regions；每區都需考慮 muscle、bone、nerve、tendon pain，尤其 athlete stress fracture / fracture。
  - AVNFH 可有 anterior hip / groin pain 且 weight bearing 變差；早期 plain radiographs 可能正常，MRI / CT 可較早偵測。
  - LCPD 是 pediatric femoral epiphysis idiopathic osteonecrosis，可造成 femoral head deformity 與 premature OA。
  - SCFE 是 adolescent 常見 hip pathology，可表現 hip / groin pain、knee pain、limp 或 painless external-rotation gait；來源建議視為 orthopedic emergency 並 prompt orthopedic referral。
  - GTPS 是 peritrochanteric pain syndrome；bursal inflammation role limited，gluteal tendinopathy、ITB thickening、abductor tendon pathology 更常見。
  - PFP 常見於 active populations，與 patellar tracking、quadriceps / hip abductor dysfunction 有關。
  - Quadriceps / patellar tendon rupture clues 包含 sudden mechanism、palpable defect、inability to extend knee；需 immediate immobilization、avoid weight bearing、surgical referral。
  - Femoral bone stress injury 可像 vague muscle strain；femoral neck tension side stress injury 是 high-risk location。
  - Tibial stress fracture 可因 repeated loading 出現 focal pain；middle anterior tibia `dreaded black line` 有 nonunion / complete fracture risk。
  - Achilles rupture 可表現像被踢到、pop、immediate pain / swelling；active plantarflexion 仍可能存在，因此 Thompson test 重要。
  - Lateral ankle sprains 最常見，常先涉及 ATFL，grade 1-2 常以 early ROM、balance / proprioception、strength progression 管理。
  - OLT 可造成 pain、swelling、locking、stiffness；radiographs 可能漏診。
  - 來源列出 high-risk stress fracture sites：femoral neck tension side、middle anterior tibia、navicular bone、fifth metatarsal Jones fracture、talar dome fracture。
- 移除或降級的陳述：
  - 未把 textbook chapter 寫成 formal guideline。
  - 未把 lower limb pain localization 寫成 tissue diagnosis。
  - 未把 GTPS 簡化成 trochanteric bursitis。
  - 未把 lateral ankle sprain 寫成所有 persistent ankle pain 的最終診斷。
  - 未把 PFP、shin splints、plantar fasciitis 等 common labels 寫成可跳過 high-risk screen 的診斷。
  - 未把 regenerative、injection、bracing 或 shockwave 等處置寫成不需 condition-specific evidence 的標準治療。
- 發現衝突：
  - 「痛在哪裡就是哪個組織受傷」不成立；來源反覆呈現 referred pain 與 mimic。
  - 「lateral hip pain = bursitis」不成立；GTPS 常是 gluteal tendon / ITB / abductor complex 問題。
  - 「ankle sprain 後持續痛只要繼續休息」不成立；需重查 OLT、peroneal pathology、fracture、syndesmosis 或 instability。
- 待追蹤問題：
  - 各單病種的 rehab protocol、return-to-sport criteria 與 imaging threshold 需用 guideline / systematic review 逐篇補強。
  - Pediatric hip pathology、high-risk stress fracture、Achilles rupture 與 ankle sprain 的 formal referral thresholds 需後續高層級來源校正。
  - GTPS、PFP、OLT、plantar fasciitis、MTSS 的 treatment evidence 需避免被 textbook overview 過度外推。
- 待處理來源：
  - 尚未掃描下一篇來源；需從 `C:\原始資料` 重新建立候選清單。

## [2026-05-04] ingest | Egan & Sharples 2023 — Molecular Responses to Acute Exercise

- 新增來源摘要：
  - `09_來源摘要/Egan_Sharples_2023_acute_exercise_molecular_responses.md`
- 新增頁面：
  - `05_Exercise_Physiology/Acute_Exercise_Molecular_Response與Skeletal_Muscle_Adaptation.md`
- 更新頁面：
  - `05_Exercise_Physiology/Skeletal_Muscle_Energy_Metabolism.md`
  - `index.md`
  - `log.md`
- 本輪抽出的直接事實：
  - 來源為 review article。
  - 來源使用 `C:\原始資料\egan-sharples-2023-molecular-responses-to-acute-exercise-and-their-relevance-for-adaptations-in-skeletal-muscle-to\egan-sharples-2023-molecular-responses-to-acute-exercise-and-their-relevance-for-adaptations-in-skeletal-muscle-to.md`，本輪未混入其他來源。
  - 題名為 `Molecular Responses to Acute Exercise and Their Relevance for Adaptations in Skeletal Muscle to Exercise Training`。
  - 作者為 Brendan Egan、Adam P. Sharples。
  - 來源主題是 acute exercise-induced signal transduction、pre- and posttranscriptional regulation、protein translation / degradation，以及這些 molecular responses 和 skeletal muscle training adaptation 的關係。
  - Repeated, episodic bouts of skeletal muscle contraction undertaken as structured exercise training 是 physiological adaptation 的 potent stimulus。
  - Skeletal muscle plasticity 可表現在 muscular size、force、endurance、contractile velocity。
  - Acute exercise signals 來自 neuronal、mechanical、metabolic、hormonal stimuli。
  - Intrinsic signals 包含 Ca2+、ATP / ADP / Pi、redox state、glycogen depletion、pH 下降、intracellular PO2 下降、RONS、temperature、mechanical load / tension、sarcolemmal disruption。
  - Extrinsic factors 包含 catecholamines、TNF-alpha、IL-6、GH、IGF-I、testosterone、glucose、amino acids、free fatty acids，以及 autocrine / paracrine factors。
  - Acute exercise 後 mRNA abundance 可在 recovery 初期 transiently increase，常在約 24 hours 內回到 baseline。
  - MetaMEx 在來源撰寫時包含 66 個 human skeletal muscle transcriptomic datasets，其中包含 13 個 acute aerobic exercise studies 與 8 個 acute resistance exercise studies。
  - Aerobic exercise training 的典型 phenotype 包含 VO2max / performance 改善、submaximal exercise 時 lipid oxidation 比例上升、oxidative capacity 與 mitochondrial biogenesis 增加。
  - Resistance training 的典型 phenotype 包含 hypertrophy、strength、power 與 neural adaptation；MPS / MPB balance 是 hypertrophy 核心之一。
  - Aerobic 與 resistance adaptation 不是完全互斥；不同模式可產生部分重疊 phenotype。
  - Training status 會改變 acute molecular response；訓練後許多 signaling 或 mRNA response 會 attenuate，但不是所有 response 都下降。
  - 來源提出 first bout effect / repeated bout effect：未訓練或不熟悉 exercise mode 時，第一次 response 可能含有大量 generalized stress response。
  - 來源明確指出 acute molecular response 與 chronic training adaptation 的 continuity 尚未完全確立。
  - 來源警告 mRNA abundance 作為 individual adaptive potential 或 protocol responsiveness biomarker 的用途有限。
  - Exercise mimetics / exercise-in-a-pill 無法完整重現 exercise 的 systemic multiorgan effects；目前較合理位置是 adjunct，而非取代 exercise。
- 移除或降級的陳述：
  - 未把 acute mRNA response 寫成 long-term adaptation。
  - 未把 phosphorylation、MPS 或單一 pathway activation 寫成 causal proof。
  - 未把 untrained first bout response 外推為 trained 或 clinical population 的處方規則。
  - 未把 rodent knockout、cell culture 或 pharmacological activation 直接等同 human exercise training。
  - 未把 exercise mimetics 寫成可取代 exercise 的既成臨床策略。
- 發現衝突：
  - 「單次 biomarker 上升就代表 protocol 會有效」不成立；來源把 acute-to-chronic continuity 視為尚未完全驗證的 working model。
  - 「aerobic 和 resistance exercise 是完全分離的分子盒子」不成立；來源指出 adaptation contribution 有重疊且受 stimulus details 影響。
  - 「訓練者和未訓練者的 acute response 可直接比較」不成立；training status、absolute / relative intensity matching 與 threshold-based intensity 都會改變解讀。
- 待追蹤問題：
  - MoTrPAC 或其他 human longitudinal multi-omics data 需後續補強 acute-to-chronic continuity。
  - Molecular biomarkers 是否能預測 functional / clinical response 需另以 longitudinal human evidence 檢查。
  - Rehabilitation populations 的 disease-specific response 不能由此 review 直接推定。
- 待處理來源：
  - 尚未掃描下一篇來源；需從 `C:\原始資料` 重新建立候選清單。

## [2026-05-04] ingest | Chow et al. 2022 — Exerkines in Health, Resilience and Disease

- 新增來源摘要：
  - `09_來源摘要/Chow_2022_exerkines_health_resilience_disease.md`
- 新增頁面：
  - `05_Exercise_Physiology/Exerkines_運動誘發多器官訊號分子.md`
- 更新頁面：
  - `05_Exercise_Physiology/Myokines_與_Muscle_Organ_Crosstalk.md`
  - `index.md`
  - `log.md`
- 本輪抽出的直接事實：
  - 來源為 high-quality review / expert review。
  - 來源使用 `C:\原始資料\Exerkines in health, resilience and disease\Exerkines in health, resilience and disease.md`，本輪未混入其他來源。
  - 題名為 `Exerkines in health, resilience and disease`。
  - 來源發表於 `Nature Reviews Endocrinology` 2022。
  - 來源定義 exerkines 為 response to acute and/or chronic exercise released signalling moieties，透過 endocrine、paracrine、autocrine pathways 作用。
  - Exerkines 不只來自 skeletal muscle；來源列出 skeletal muscle / myokines、heart / cardiokines、liver / hepatokines、WAT / adipokines、BAT / batokines、nervous system / neurokines 等。
  - Exerkines 可包含 cytokines、hormones、neurotransmitters、proteins、nucleic acids、microRNA、mRNA、mitochondrial DNA、lipids、metabolites 與 extracellular-vesicle cargo。
  - IL-6 是 2000 年後最廣泛研究的 myokine；但 acute exercise-induced transient IL-6 與 chronic elevated resting IL-6 不可等同。
  - Exercise response 受 exercise timing、fed-fasting status、post-exercise diet、exercise type、duration、intensity、fitness、genetics、phenotype 影響。
  - HERITAGE data 在來源中被用來說明 training response variability：VO2max response heritability 約 47%，約 20% chronic exercise training non-response for aerobic capacity，7-15% individuals 在部分 cardiometabolic variables 有 adverse response。
  - MoTrPAC 被描述為 NIH-supported effort，用 humans and animals 的 multi-timepoint biospecimen profiling 描述 physical activity molecular transducers。
  - Acute exerkine response 不一定平行 chronic training response。
  - 來源列出 acute exercise classic cytokine responses：IL-6、IL-8、IL-1RA、IL-10。
  - Exerkine research 正從 single-factor measurement 轉向 lipidomics、metabolomics、proteomics、transcriptomics、epigenomics、RNA-seq、methyl-seq、ATAC-seq 等 omics profiling。
  - Extracellular vesicles 被視為 exercise-related inter-organ crosstalk 的重要 carrier，但 plasma-derived vesicle analysis 有 preanalytical / isolation 挑戰。
  - Cardiometabolic candidate exerkines 包含 nitric oxide、VEGF、IL-6、IL-8、FGF21、angiopoietin 1、fractalkine、musclin、myonectin 等。
  - WAT browning 與 irisin-mediated pathway 在 humans 的轉譯仍有爭議。
  - 來源討論 12,13-diHOME、TGFβ2、apelin、follistatin、fetuin-A、BAIBA、fractalkine、GPLD1、clusterin 等 candidate pathways，但 certainty 不一。
  - 來源明確列出 contentious questions：acute vs chronic inconsistency、animal vs human inconsistency、outcome and sampling variability。
  - 來源明確指出 `exercise in a pill` 目前仍是 wishful thinking。
- 移除或降級的陳述：
  - 未把 exerkines 寫成 routine clinical biomarker。
  - 未把 myokines 與 exerkines 當同義詞。
  - 未把 single candidate molecule 寫成 exercise benefit 的主因。
  - 未把 animal / cell model 發現直接外推成人類臨床處方。
  - 未把 exerkine therapeutics 寫成可取代 exercise 的既成治療。
- 發現衝突：
  - 「exercise benefit 可以用某個單一分子解釋」不成立；來源把 exerkines 放在 multi-organ systems response。
  - 「acute exercise 分子上升，chronic training 就也應上升」不成立；來源明確警告 acute / chronic responses 可不一致。
  - 「myokine 就等於 exerkine」不成立；myokine 只是 skeletal muscle-derived subset。
- 待追蹤問題：
  - 需要後續用 MoTrPAC 或其他 human data 更新 exerkine candidate 的 human reproducibility。
  - Exerkine biomarker 的臨床可用性、reference range、sampling protocol 與 outcome mediation 仍未建立。
  - Brain-related exerkines 是否跨越 BBB、或主要經 peripheral immune / complement / coagulation routes 作用，需要更嚴格 human evidence。
- 待處理來源：
  - 尚未掃描下一篇來源；需從 `C:\原始資料` 重新建立候選清單。

## [2026-05-04] ingest | Furrer et al. 2023 — The Molecular Athlete

- 新增來源摘要：
  - `09_來源摘要/Furrer_2023_molecular_athlete.md`
- 新增頁面：
  - `05_Exercise_Physiology/Molecular_Athlete_運動表型連續體.md`
- 更新頁面：
  - `05_Exercise_Physiology/Acute_Exercise_Molecular_Response與Skeletal_Muscle_Adaptation.md`
  - `05_Exercise_Physiology/Training_Intensity_Distribution.md`
  - `index.md`
  - `log.md`
- 本輪抽出的直接事實：
  - 來源為 review article。
  - 來源使用 `C:\原始資料\furrer-et-al-2023-the-molecular-athlete-exercise-physiology-from-mechanisms-to-medals\furrer-et-al-2023-the-molecular-athlete-exercise-physiology-from-mechanisms-to-medals.md`，本輪未混入其他來源。
  - 題名為 `The Molecular Athlete: Exercise Physiology from Mechanisms to Medals`。
  - 作者為 Regula Furrer、John A. Hawley、Christoph Handschin。
  - Human skeletal muscle function and exercise capacity span from inactive individuals to elite athletes。
  - Sedentary lifestyle、low VO2max、unfavorable body composition、low muscle strength 是 chronic disease risk 與 morbidity / mortality predictor。
  - Regular physical activity despite interindividual response variability 仍可降低多種 noncommunicable diseases 風險並提供 therapeutic benefits。
  - Elite athletes 接近 world-record 或 world-leading performance 的族群小於全球人口 0.00006%。
  - Champion endurance athletes 的 VO2max 可為 untrained individuals 的 2-3 倍。
  - Elite endurance phenotype 常見較高 stroke volume、capillary density、mitochondrial density 與 oxidative slow-twitch fiber proportion。
  - VO2max 是 central and peripheral integrated measure，不是單一 organ 或 pathway 指標。
  - Training adaptation 依 progressive overload、specificity、reversibility 與 individuality 原則進行。
  - Periodization 應把 microcycle、mesocycle、macrocycle 與 nutrition、recovery、psychology、skill training 配合。
  - Detraining 會讓 endurance adaptations 在約 7-21 days 開始變化；strength decline 在約 21 days 內較有限但 4 weeks 後更明顯。
  - Concurrent training evidence 多來自 moderately trained 或 untrained populations，且研究難以匹配 total work、stimulus 與 exercise mode。
  - Low muscle glycogen sessions 可能增強部分 mitochondrial biogenesis signals，但 well-trained athletes 的 performance benefit 不穩定。
  - Voluntary whole-body exercise 不等於 isolated muscle contraction；animal / in vitro data 與 human training outcome 之間有 translational gap。
  - Chronic trained muscle 不應被視為 acute exercise bouts 的簡單加總。
  - Non-responder label 需謹慎；對單一 outcome 低反應不代表整體 exercise 無效。
  - Exercise mimetics 目前不能取代 exercise，且某些候選藥物在特定情境可能 attenuate training adaptation。
- 移除或降級的陳述：
  - 未把 elite athlete protocol 寫成 clinical rehabilitation prescription。
  - 未把 VO2max、mitochondrial density、gene 或單一 pathway 寫成 performance 的完整原因。
  - 未把 animal / in vitro mechanism 直接寫成人類 exercise prescription。
  - 未把 exercise mimetic、antioxidant 或 supplement 寫成可取代 training stimulus。
  - 未把 non-responder 當成固定且不可改變的個人特質。
- 發現衝突：
  - 「elite performance 是單一基因或單一 pathway 的結果」不成立；來源將其放在多層次 intrinsic / extrinsic factors。
  - 「TID 標籤本身就是機制」不成立；來源要求把 intensity、periodization、recovery、nutrition 與 physiological outcomes 放回同一框架。
  - 「acute molecular response 累加即可解釋 trained phenotype」不成立；來源明確指出 integration / coordination 仍未完整理解。
- 待追蹤問題：
  - Elite women、masters athletes、underrepresented ethnicities 與 clinical disease populations 的直接機制資料仍需補強。
  - Wearables、AI / machine learning 與 exercise mimetics 的 clinical utility 需要後續逐篇來源檢查。
  - MoTrPAC-like longitudinal human multi-omics data 可用來後續校正 acute-to-chronic integration。
- 待處理來源：
  - 尚未掃描下一篇來源；需從 `C:\原始資料` 重新建立候選清單。

## [2026-05-04] ingest | Goulding & Marwood 2023 — Interaction of Factors Determining Critical Power

- 新增來源摘要：
  - `09_來源摘要/Goulding_Marwood_2023_critical_power_determinants.md`
- 新增頁面：
  - `04_CPET/Critical_Power_生理決定因子.md`
- 更新頁面：
  - `04_CPET/Critical_Power.md`
  - `04_CPET/Exercise_Intensity_Domains.md`
  - `04_CPET/VO2_Kinetics.md`
  - `05_Exercise_Physiology/運動時氧供調節的整合視角.md`
  - `index.md`
  - `log.md`
- 本輪抽出的直接事實：
  - 來源為 review article。
  - 來源使用 `C:\原始資料\s40279-022-01805-w\s40279-022-01805-w.md`，本輪未混入其他來源。
  - 題名為 `Interaction of Factors Determining Critical Power`。
  - 作者為 Richie P. Goulding、Simon Marwood。
  - Critical power 是 power-duration hyperbolic relation 的 asymptote。
  - CP 代表 threshold intensity；超過 CP 後 systemic and intramuscular metabolic homeostasis 不能維持。
  - CP 以下可達 pulmonary VO2、blood lactate、muscle VO2、PCr、Pi、pH、muscle lactate 的 steady state；CP 以上則不行。
  - 常規 CP 測定可使用 3-5 次 high-intensity constant-power tests to task failure，測試時間通常選在 2-15 min。
  - CP 是 aerobic function parameter，可受 oxygen transport and utilization pathway 每一步影響。
  - Oxygen pathway 包含 pulmonary diffusion、convective O2 delivery、capillary-to-mitochondria diffusive O2 delivery、mitochondrial O2 utilization。
  - Convective O2 delivery 可描述為 cardiac output 與 arterial O2 content 的乘積。
  - Hypoxia 可降低 CP，hyperoxia 可提高 CP。
  - Blood flow occlusion / duty-cycle manipulation 支持 CP 依賴 muscle blood flow and O2 delivery。
  - Diffusive O2 transport 由 Fick's law 描述，受 diffusion driving pressure 與 muscle diffusing capacity 影響。
  - Muscle capillarity 與 capillary-to-fiber ratio 和 CP 有關。
  - TauVO2 是 muscle O2 utilization kinetics 的實用讀出；tau 越慢，exercise onset 的 O2 deficit 越大。
  - O2 deficit 會增加 PCr depletion、Pi / ADP / H+ accumulation、fatigue induction 與 efficiency loss。
  - 來源指出 tauVO2、convective O2 delivery、diffusive O2 delivery 對 CP 有 independent but interacting effects。
  - Whole-body CP 還受 muscle fiber-type composition、relative exercising muscle mass、lever mechanics、coordination、localized fatigue 與 motor unit recruitment pattern 影響。
- 移除或降級的陳述：
  - 未把 CP 寫成 lactate threshold 或 anaerobic threshold。
  - 未把 CP 寫成單一器官、單一 metabolite 或單一 energy tank。
  - 未把 pulmonary VO2 kinetics 在所有情境下都等同 muscle kinetics。
  - 未把 hypoxia / hyperoxia 或 acetaminophen-related CP findings 寫成臨床治療建議。
- 發現衝突：
  - 「CP 只是 lactate / ventilatory marker」不成立；來源將其定位為 oxygen transport / utilization 與 recruitment / fatigue 的整合閾值。
  - 「CP 是固定個人常數」不成立；來源顯示 O2 availability、blood flow、diffusion、tauVO2、mode、muscle mass 與 recruitment 都會改變 CP。
  - 「CP 只反映 central cardiopulmonary function」不成立；peripheral diffusion、fiber type、muscle metabolic control 與 motor unit recruitment 同樣進入決定因子。
- 待追蹤問題：
  - HF、COPD、pulmonary hypertension、neuromuscular disease 的 CP determinants 需 disease-specific CPET sources 補強。
  - Clinical rehabilitation 中 CP 測定的安全性、可靠性與實務可行性需另用 protocol / guideline sources 校正。
  - Fiber type / capillarity / recruitment data 不應過度個體化外推。
- 待處理來源：
  - 尚未掃描下一篇來源；需從 `C:\原始資料` 重新建立候選清單。

## [2026-05-04] ingest | Smith et al. 2023 — Exercise metabolism and adaptation in skeletal muscle

- 新增來源摘要：
  - `09_來源摘要/Smith_2023_exercise_metabolism_adaptation_skeletal_muscle.md`
- 新增頁面：
  - `05_Exercise_Physiology/Skeletal_Muscle_Metabolic_Flexibility與Exercise_Adaptation.md`
- 更新頁面：
  - `05_Exercise_Physiology/Skeletal_Muscle_Energy_Metabolism.md`
  - `05_Exercise_Physiology/Muscle_Fiber_Types.md`
  - `05_Exercise_Physiology/Acute_Exercise_Molecular_Response與Skeletal_Muscle_Adaptation.md`
  - `index.md`
  - `log.md`
- 本輪抽出的直接事實：
  - 來源為 review article。
  - 來源使用 `C:\原始資料\nihms-1908393\nihms-1908393.md`，本輪未混入其他來源。
  - 題名為 `Exercise metabolism and adaptation in skeletal muscle`。
  - 作者為 Jonathon A. B. Smith、Kevin A. Murach、Kenneth A. Dyar、Juleen R. Zierath。
  - Final publication 為 `Nature Reviews Molecular Cell Biology. 2023;24(9):607-632. doi:10.1038/s41580-023-00606-x`。
  - Skeletal muscle 是 nutrient storage、energy use 與 locomotion 的主要組織。
  - Physical inactivity 會降低 skeletal muscle insulin sensitivity 與 oxidative capacity。
  - Acute exercise 增加 contracted muscle 的 amino acid transport、glucose transport、postprandial muscle protein synthesis 與 recovery 期間 insulin-stimulated glucose disposal。
  - Training 可提升 skeletal muscle mass、peripheral insulin sensitivity、VO2max 與 strength。
  - Human torso / limb muscles 主要表達 MyHC type I、type IIA、type IIX；MyHC 主要決定 contraction speed，不可直接等同 metabolism。
  - Human 與 rodent muscle physiology 不可直接等同；rodent type IIA 常是最 oxidative，human type I 常是最 oxidative。
  - Human vastus lateralis 的 hybrid fibers 可由小於 10% 到 40%；pure type IIX 在健康 human vastus lateralis 通常小於 1%。
  - Muscle mitochondria 約佔 muscle volume 的 2-10%，依 fiber type 而異。
  - Subsarcolemmal / peripheral mitochondria 與 intermyofibrillar mitochondria 在 location、structure 與 function 上不同。
  - Free ATP 約 20-25 mmol/kg dry mass，只足以支撐 maximal exercise 小於 2 秒。
  - ATP resynthesis speed 大致為 phosphagen system / glycolysis 最快，其次 carbohydrate oxidation，最後是 NEFA oxidation。
  - Exercise onset 前 30-60 秒可出現 oxidative phosphorylation lag。
  - Type II fibers 的 ATP consumption per unit time 約為 type I fibers 的 2.5-4 倍。
  - Higher intensity 下 glycolytic flux 可透過 free carnitine pool depletion 限制 long-chain fatty acid import。
  - Contracting muscle 中 mitochondria 可能不是主要 ROS source；NOX pathways 可能更主要。
  - 多種 exercise modalities 可共同改變超過 400 個 phosphorylation sites、超過 200 個 proteins。
  - Modality divergence 在 recovery 3 小時左右更明顯；resistance exercise 較強化 mTORC1 / p38 MAPK related signaling。
  - Training 可增加 mitochondrial respiration、mitochondrial proteome、capillarization、substrate handling、lactate clearance 與 performance measures。
- 移除或降級的陳述：
  - 未把 metabolic flexibility 簡化為 fat oxidation。
  - 未把 MyHC type 直接寫成 oxidative capacity。
  - 未把 acute mRNA / phosphorylation / epigenetic response 寫成 chronic adaptation 的直接替代指標。
  - 未把 animal / cell model pathway finding 直接外推成人類 clinical prescription。
  - 未把 training-induced acute response attenuation 解讀為 stimulus 失效。
- 發現衝突：
  - 「lactate 是 waste product」不成立；來源採用 lactate / pyruvate 可轉換並可進入 oxidation 的框架。
  - 「type I / type II 可直接代表底物利用」不成立；來源明確把 MyHC、metabolism、mitochondria 與 myonuclear program 分開。
  - 「acute signaling activation 直接等於 long-term adaptation」不成立；來源把 acute-to-chronic 放在 repeated bouts、recovery、training status 與 systems redundancy 下。
- 待追蹤問題：
  - Exercise chrono-therapy、EV miRNA cargo、lactate lactylation、NOX-driven ROS signaling 的 human clinical relevance 仍需後續來源。
  - Biological sex、age、chronotype、ethnicity、training status、metabolic health 與 social gender 的交互作用仍需更完整 human data。
  - AMPK / PGC-1alpha / mTOR 以外的 redundancy 與 compensation 需後續機制來源補強。
- 待處理來源：
  - 尚未掃描下一篇來源；需從 `C:\原始資料` 重新建立候選清單。

## [2026-05-04] ingest | Juarez et al. 2024 — Cardiopulmonary Exercise Testing in Heart Failure

- 新增來源摘要：
  - `09_來源摘要/Juarez_2024_CPET_in_heart_failure.md`
- 新增頁面：
  - `04_CPET/CPET_in_Heart_Failure.md`
- 更新頁面：
  - `04_CPET/CPET_Protocol_Design.md`
  - `04_CPET/VO2max_Measurement.md`
  - `04_CPET/Gas_Exchange_Threshold.md`
  - `index.md`
  - `log.md`
- 本輪抽出的直接事實：
  - 來源為 narrative review。
  - 來源使用 `C:\原始資料\jcdd-11-00070\jcdd-11-00070.md`，本輪未混入其他來源。
  - 題名為 `Cardiopulmonary Exercise Testing in Heart Failure`。
  - 作者為 Michel Juarez、Cristian Castillo-Rodriguez、Dina Soliman、Gaspar Del Rio-Pertuz、Kenneth Nugent。
  - Citation 為 `J. Cardiovasc. Dev. Dis. 2024;11:70. doi:10.3390/jcdd11030070`。
  - CPET in HF measures respiratory gases、heart rate、blood pressure、oxygen uptake、carbon dioxide output、ventilation 與 gas exchange。
  - HF CPET report 可分 metabolics、cardiac、ventilation、gas exchange 四組資訊。
  - Clinical HF CPET 常用 incremental / ramp protocol；ramp grades 可包括 5、7、10、15 W/min，依 expected exercise tolerance 選擇。
  - Cycle ergometer 的 workload linearity 較 treadmill 好。
  - HF patients 常達不到 true VO2max，因此臨床常報 peak VO2。
  - Peak VO2 in HF 與 peak cardiac output、muscle perfusion、oxygen delivery / extraction 有關。
  - VE/VCO2 slope in HF 反映 ventilatory inefficiency，與 dead space ventilation、lung compliance、chemo / metabolic reflex sensitivity、early metabolic acidosis、abnormal pulmonary hemodynamics 相關。
  - VE/VCO2 slope >34-36 可辨識 high-risk HF patients；>=45 屬 high / very poor risk pattern。
  - Peak VO2 <14 mL/kg/min 是 poor prognosis marker；beta blocker patients 可使用 <12 mL/kg/min。
  - Peak VO2 <=10 mL/kg/min、VE/VCO2 slope >=36、EOV presence、VO2 at AT <11 mL/kg/min 形成 very poor prognosis pattern。
  - Excellent prognosis pattern 包含 peak VO2 >=20 mL/kg/min、VE/VCO2 slope <30、absence of EOV、VO2 at AT >11 mL/kg/min。
  - RER >1.0-1.1 可作 maximal physiologic effort 線索，但 HR-based effort assessment 受 beta blockers / chronotropic incompetence 影響。
  - CPET 不能穩定單獨分類 HFrEF vs HFpEF；reduced VO2 可預測兩者 outcomes。
  - HFpEF dyspnea 可涉及 chronotropic reserve、stroke volume reserve、cardiac output reserve、exercise pulmonary hypertension、peripheral O2 extraction 與 pulmonary disorders。
  - Exercise training in HF 可與 BNP / NT-proBNP 下降及 peak VO2 上升相關。
  - CPET 需要 specialized lab、trained personnel 與 expert interpretation。
  - Portable metabolimeters 可連接 laboratory peak VO2 與 ADL oxygen cost；smart watches 可作 daily monitoring adjunct。
- 移除或降級的陳述：
  - 未把本篇 narrative review 當成 HF guideline。
  - 未把 peak VO2 cut-off 寫成單獨 transplant listing rule。
  - 未把 CPET 單獨寫成 HFrEF / HFpEF 分類工具。
  - 未把 smart watches 或 portable metabolimetry 寫成 CPET 替代。
  - 未採用原始 Markdown 中受 OCR 污染的 BNP / HFpEF 數字。
- 發現衝突：
  - 「HF CPET 只看 peak VO2」不成立；來源同時重視 VE/VCO2 slope、AT、RER、EOV、O2 pulse、HR / BP response 與 comorbidity context。
  - 「HF dyspnea 一定主要來自 cardiac impairment」不成立；來源列出 pulmonary disease、anemia、sleep apnea、skeletal muscle weakness / wasting 等可能貢獻。
  - 「wearables 可取代 CPET」不成立；來源將其定位為 monitoring / problem detection adjunct。
- 待追蹤問題：
  - 需用 HF guideline 或 advanced HF / transplant-specific statements 校正 peak VO2、VE/VCO2 slope 與 transplant timing。
  - 需用 pulmonary hypertension CPET 來源處理 PH-specific VE/VCO2 / PETCO2 pattern。
  - miRNA biomarkers、portable metabolimetry 與 wearable workflow 仍需更高品質 clinical utility evidence。
- 待處理來源：
  - `C:\原始資料\jcm-12-05465-v2\jcm-12-05465-v2.md`

## [2026-05-04] ingest | Pezzuto & Agostoni 2023 — CPET in Pulmonary Hypertension

- 新增來源摘要：
  - `09_來源摘要/Pezzuto_Agostoni_2023_CPET_pulmonary_hypertension.md`
- 新增頁面：
  - `04_CPET/CPET_in_Pulmonary_Hypertension.md`
- 更新頁面：
  - `04_CPET/CPET_in_Heart_Failure.md`
  - `04_CPET/Gas_Exchange_Threshold.md`
  - `index.md`
  - `log.md`
- 本輪抽出的直接事實：
  - 來源為 narrative review。
  - 來源使用 `C:\原始資料\jcm-12-05465-v2\jcm-12-05465-v2.md`，本輪未混入其他來源。
  - 題名為 `The Current Role of Cardiopulmonary Exercise Test in the Diagnosis and Management of Pulmonary Hypertension`。
  - 作者為 Beatrice Pezzuto、Piergiuseppe Agostoni。
  - Citation 為 `J. Clin. Med. 2023;12:5465. doi:10.3390/jcm12175465`。
  - PAH 的核心病理是 PVR / mPAP 增加造成 RV afterload mismatch。
  - RV-arterial coupling 是 PAH symptoms、clinical status 與 prognosis 的主要 determinant。
  - PAH effort dyspnea 可來自 RV exercise reserve 不足，導致 CO 無法跟上 metabolic demand。
  - CPET 被來源描述為 functional capacity and mechanisms of exercise limitation 的 gold standard，並可支持 early detection、differential diagnosis、prognostic stratification 與 follow-up。
  - 來源指出 ESC/ERS PH guideline 強調 CPET 在 initial diagnostic phase 與 follow-up 的角色。
  - PAH CPET abnormalities 可分 ventilatory、gas exchange、cardiovascular 三類。
  - PAH patients exercise 時可出現 VD/VT >30%；正常人 exercise 時 VD/VT 應下降。
  - PAH 可呈 high VE/VCO2、high VE/VO2、low PETCO2、positive P(a-ET)CO2、higher P(A-a)O2、reduced peak VO2、low AT、reduced VO2/work slope、low peak HR、low O2 pulse。
  - PAH O2 pulse 可呈 flattened slope，代表 stroke volume augmentation 受限，exercise CO increase 更依賴 HR。
  - PAH patients compared with left HF patients 可有 smaller stroke volume response and steeper HR/VO2 slope。
  - EOV 更常見於 post-capillary PH / HF，而非典型 PAH。
  - High VE/VCO2 plus low PETCO2 increases likelihood of pulmonary vascular disease；both normal makes PH unlikely in the cited framework。
  - In SSc with PAH suspicion，one cited study found peak VO2 threshold 13.8 mL/kg/min sensitivity 87.5% and specificity 74.8%；peak VO2 >18.7 mL/kg/min excluded PAH in that cohort。
  - In CTEPH / CTED study，peak exercise VD/VT >45% had sensitivity 92% and specificity 83%；peak A-a O2 gradient >32 mmHg had sensitivity 92% and specificity 67%。
  - 來源引用 ESC/ERS risk anchors：peak VO2 >15 mL/kg/min and VE/VCO2 slope <36 = low risk；peak VO2 11-15 and VE/VCO2 slope 36-44 = intermediate risk；peak VO2 <11 and VE/VCO2 slope >44 = high risk。
  - Delayed HR recovery <18 beats/min in first post-exercise minute has prognostic value in PAH。
  - CPET in clinical trials requires expertise and standardization。
- 移除或降級的陳述：
  - 未把本篇 review 當作 ESC/ERS guideline 原文。
  - 未把 CPET 寫成 RHC 替代品。
  - 未把 high VE/VCO2 slope 單獨診斷為 PAH。
  - 未把 PAH、PH-LHD、CTEPH、COPD-PH、IPF-PH 的 CPET pattern 混為同一疾病。
  - 未把 borderline PH 的 CPET abnormality 寫成 PAH-specific drug indication。
- 發現衝突：
  - 「PH CPET 只是 low peak VO2」不成立；來源強調 VE/VCO2、PETCO2、VD/VT、O2 pulse、HR response 與 gas exchange pattern。
  - 「PAH 與 HF 的 CPET pattern 可完全互換」不成立；來源指出 PAH 的 stroke volume response 較小、HR/VO2 slope 較陡，EOV 更偏 post-capillary PH / HF。
  - 「CPET 可取代 RHC」不成立；來源將 CPET 放在 diagnostic support、likelihood stratification 與 follow-up。
- 待追蹤問題：
  - 需回查 2022 ESC/ERS PH guideline 原文，確認 CPET cutoffs、indications 與 clinical workflow。
  - Borderline PH / mPAP 20-25 mmHg 的 CPET-guided treatment or observation 尚未確立。
  - PAH clinical trials 的 CPET endpoints 需標準化與 site expertise。
- 待處理來源：
  - 尚未掃描下一篇來源；需從 `C:\原始資料` 重新建立候選清單。

## [2026-05-04] ingest | Ibrahim, Hafner & Rocher 2026 — LLM Warmth, Accuracy, and Sycophancy

- 新增來源摘要：
  - `09_來源摘要/Ibrahim_Hafner_Rocher_2026_warmth_accuracy_sycophancy.md`
- 新增頁面：
  - `08_工具與Workflow/LLM_Warmth_Accuracy_Tradeoff.md`
- 更新頁面：
  - `00_總覽/知識百科_基礎規範總覽.md`
  - `08_工具與Workflow/知識百科_ingest_工作流.md`
  - `index.md`
  - `log.md`
- 本輪抽出的直接事實：
  - 來源為 Nature 2026 original research article，不是醫學 guideline。
  - 來源使用 `C:\原始資料\s41586-026-10410-0\s41586-026-10410-0.md`，本輪未混入其他來源。
  - 題名為 `Training language models to be warm can reduce accuracy and increase sycophancy`。
  - 作者為 Lujain Ibrahim、Franziska Sofia Hafner、Luc Rocher。
  - DOI 為 `10.1038/s41586-026-10410-0`；published online: 2026-04-29。
  - 研究以 SFT 對五個模型進行 warmth fine-tuning：Llama-3.1-8B-Instruct、Mistral-Small-Instruct-2409、Qwen-2.5-32B-Instruct、Llama-3.1-70B-Instruct、GPT-4o-2024-08-06。
  - Evaluation tasks 包含 TriviaQA、TruthfulQA、MASK Disinformation 與 MedQA。
  - Warmth fine-tuning 在研究中使 incorrect response probability 平均上升 7.43 percentage points。
  - 任務層級錯誤率增加包含 MedQA +8.6 pp、TruthfulQA +8.4 pp、Disinfo +5.4 pp、TriviaQA +4.9 pp。
  - Sadness cue 下 warm-original accuracy gap 增至 11.9 pp。
  - Incorrect user beliefs 條件下，warm models 較容易 affirm wrong beliefs。
  - MMLU、GSM8K 與 AdvBench 多數表現未明顯下降，表示常規 benchmark 可漏掉 conversational failure。
  - Response length adjustment 後，warmth fine-tuning 仍使 incorrect response probability 增加 6.99 pp。
  - Cold fine-tuning control 未重現一致 accuracy degradation，支持問題較可能與 warmth-related style change 有關。
- 移除或降級的陳述：
  - 未把本篇 AI original article 當成醫學證據。
  - 未把結果解讀成所有 empathy 或 supportive tone 都會降低 accuracy。
  - 未把單篇研究當成完整 AI deployment guideline。
- 發現衝突：
  - 「語氣只是 style，不影響 substance」不成立；來源顯示 persona / style fine-tuning 可能改變 open-ended factual behavior。
  - 「standard benchmark pass 就代表真實對話安全」不成立；研究中 MMLU / GSM8K / AdvBench 可接近不變，但 conversational QA 與 sycophancy probes 仍惡化。
  - 「high-stakes advice 越 validating 越安全」不成立；vulnerability cues 可能放大 affirming incorrect beliefs 的風險。
- 待追蹤問題：
  - 需補更多 LLM evaluation / sycophancy / medical AI safety 來源，避免單篇 original article 過度外推。
  - 需將 wiki health check 未來納入「錯誤前提未糾正」或「推論寫成事實」的文字型檢查。
  - 若後續有 guideline-level AI safety source，應回來校正本頁。
- 待處理來源：
  - health check raw backlog 中多數 high-priority medical / exercise / pediatric 來源已存在對應摘要；仍需改善 raw-source mapping，避免已處理來源反覆列入 backlog。

## [2026-05-04] ingest | UpToDate — Aphasia: Prognosis and treatment

- 新增來源摘要：
  - `09_來源摘要/Aphasia_Prognosis_and_treatment.md`
- 新增頁面：
  - `03_疾病與臨床主題/Poststroke_Aphasia_預後與恢復.md`
  - `02_方法學/Aphasia_語言治療_劑量與技術.md`
- 更新頁面：
  - `03_疾病與臨床主題/中風復健總論.md`
  - `03_疾病與臨床主題/Stroke_Movement_Dysfunction_Impairment_Model.md`
  - `03_疾病與臨床主題/Poststroke_Movement_Reeducation與Compensation.md`
  - `index.md`
  - `log.md`
- 本輪抽出的直接事實：
  - 來源為 UpToDate topic review；topic last updated 2024-06-03，literature current 2026-04。
  - 來源使用 `C:\原始資料\Aphasia_ Prognosis and treatment.md`，本輪未混入其他來源。
  - Aphasia 出現於 15–38% 的 ischemic strokes。
  - 多數 poststroke aphasia 患者最大改善發生於 first few months，1 年後 plateau。
  - Initial aphasia 嚴重度與長期 deficit 強相關；mild onset 最有可能完全恢復。
  - 1 年 outcome 預測因子（單篇 long-term study）：baseline phonology integrity、younger age、higher Barthel Index、higher educational level、hemorrhagic（vs ischemic）。
  - Right-hemisphere lesion 引起的 aphasia 永久 deficit 通常較輕，與 incomplete language lateralization 一致。
  - Handedness、sex、increasing age 對恢復未顯示一致影響。
  - TBI 引起的 aphasia 病程在小規模研究中與 poststroke 類似。
  - 急性期早期恢復與 language area reperfusion 相關（DWI/PWI）；中後期恢復伴隨 perisylvian 周邊與 contralateral homologous 區域 fMRI activation。
  - SLT 標明 Grade 2C suggestion；review of 10 studies / 864 patients 顯示高強度短期 SLT 優於低強度長期 SLT。
  - 116 人 subacute RCT：2 hr/week 與 5 hr/week 結果相似（與上述 review 不一致）。
  - 沒有單一 SLT 技術被證實優於他者；CIAT、computer-assisted、AAC、tablet apps 為當前研究方向。
  - 藥物（bromocriptine、amphetamine、piracetam、AChEi、memantine、moclobemide）皆無 unequivocal long-term benefit；memantine + CIAT 27 人 RCT 顯示 48 週 sustained benefit。
  - TMS 與 tDCS 顯示部分 naming-level 改善（tDCS Cochrane 顯示 object-naming benefit 但 functional communication 無一致益處）；不屬 routine clinical practice。
  - Poststroke aphasia 患者憂鬱風險升高；moclobemide 90 人 RCT 未顯示優於 placebo；prophylactic antidepressant 不被支持，但需 monitor 並在出現時治療。
- 移除或降級的陳述：
  - 未把 SLT 寫成有強證據；保留 Grade 2C 標籤。
  - 未把任何藥物寫成 routine recommendation。
  - 未把 TMS / tDCS 寫成 routine intervention。
  - 未把單一研究的 Barthel Index、education、phonology 預測因子寫成個體 calculator。
  - 未把「1 年 plateau」寫成「1 年後不可改善」。
  - 未把 right-hemisphere stroke 較輕的群體統計寫成個體保證。
  - 未把 TBI 與 stroke aphasia 預後完全等同。
  - 未把 prophylactic antidepressant 寫成 standard practice。
- 發現衝突：
  - 「SLT dose 越高越好」不成立；高強度短期 review 與 116 人 subacute RCT（2 vs 5 hr/week 相當）結果不一致。
  - 「特定 SLT technique（CIAT、computer-assisted）優於他者」不成立；來源明確指出無 head-to-head 優劣。
  - 「藥物可促進 aphasia recovery」不成立；無 phase III RCT 支持 routine use。
  - 「TMS 抑制 contralateral hemisphere 是唯一機制」過度單一；本來源僅引主流 model，實際有替代理論未被本來源處理。
- 待追蹤問題：
  - Aphasia syndrome subgroup（global、Wernicke、Broca、subcortical anomia）的 dose-response 差異未充分研究。
  - Functional communication outcome 的標準化測量需強化。
  - Memantine + CIAT 27 人正向訊號需更大樣本驗證。
  - Aphasia 患者 depression screen 工具的 validity 需專門驗證。
  - 後續 stroke 系列 UpToDate（Aneurysmal SAH、ICH、Antihypertensive secondary prevention、Stroke etiology / classification、Vascular dementia、Vascular cognitive impairment、Cerebral artery dissection 等）尚未處理。
- 待處理來源：
  - `C:\原始資料\Aneurysmal subarachnoid hemorrhage_ Clinical manifestations and diagnosis.md`
  - `C:\原始資料\Aneurysmal subarachnoid hemorrhage_ Treatment and prognosis.md`
  - `C:\原始資料\Spontaneous intracerebral hemorrhage_ Pathogenesis, clinical features, and diagnosis (1).md`
  - `C:\原始資料\Spontaneous intracerebral hemorrhage_ Acute treatment and prognosis.md`
  - `C:\原始資料\Antihypertensive therapy for secondary stroke prevention.md`
  - `C:\原始資料\Clinical diagnosis of stroke subtypes.md`
  - `C:\原始資料\Stroke_ Etiology, classification, and epidemiology.md`
  - `C:\原始資料\Cerebral and cervical artery dissection_ Clinical features and diagnosis.md`
  - `C:\原始資料\Etiology, clinical manifestations, and diagnosis of vascular dementia.md`
  - `C:\原始資料\Treatment of vascular cognitive impairment and dementia.md`
  - `C:\原始資料\Stroke in patients with atrial fibrillation.md`
  - `C:\原始資料\Sleep-related breathing disorders and stroke.md`
  - `C:\原始資料\Complications of stroke_ An overview.md`

## [2026-05-04] correction | Poole, Rossiter, Brooks & Gladden 2020 — The anaerobic threshold: 50+ years of controversy

- 修正原因：本來源於 2026-04-22 ingest，依使用者 5/1 cutoff 規則屬「之前不算」之列，須依 §6 流程重做。原摘要使用非 skill 模板的 schema（一句話定義 / 核心機制 / 臨床表現 / 評估方式 / ...），缺少 Fact / Inference / Assumption / Uncertainty 分層、缺少 Conflicts With Existing Knowledge 與 Pages That Should Be Created or Updated 段，且包含若干指向不存在頁的連結（[[Lactate_Shuttle]] 等）。
- 重新檢查來源：
  - `C:\原始資料\The Journal of Physiology - 2020 - Poole - The anaerobic threshold  50  years of controversy\....md`（677 行；本輪未混入其他來源）。
  - 重讀全文 §1–§6（intro and brief history、lactate shuttle、GET、coincidence of thresholds、CP、conclusions）與 references。
- 修正頁面：
  - `09_來源摘要/Poole_2020_anaerobic_threshold.md`（依 skill 模板完整重寫，覆蓋舊版）。
  - `index.md`（更新 Poole entry 描述，反映 GET/LT vs CP/CS 雙閾值論）。
  - `log.md`。
- 本輪重新核對的直接事實：
  - 來源為 J Physiol 2021;599(3):737–767 topical review；DOI 10.1113/JP279963；4 位作者：Poole、Rossiter、Brooks、Gladden。
  - Wasserman 1973 的 AT paper 為 J Appl Physiol 史上第 8 高引（1541 citations，2020-09-27）。
  - 反 dysoxia 證據四線：Welch & Stainsby 1967 / Jöbsis & Stainsby 1968 NAD+/NADH 反向；Pagliassotti & Donovan 1990 / Gladden lab elevated [La−] 反向 uptake；Connett 1983–1986 / Richardson 1995–1998 / Mole 1999 PiO2 不破 ~2 mmHg；Whipp & Wasserman 1986 / Poole 1988/1990 heavy 域 [La−] 可達 new steady state。
  - GET <11 mL/kg/min → 4–5× post-surgical mortality（Older 1999）；GET <8 mL/kg/min → ~8% post-surgical CV death（Older 1999）；GET >14 mL/kg/min 幾乎為零（Older 1999）。
  - HF: GET <11 → ~4× death（Gitt 2002）；GET <8.5 mL/kg/min 或 indeterminable → 進一步增加（Agostoni 2013）。
  - 116-人 elective surgery：GET <10.1 mL/kg/min 預測 post-op complication 優於 V̇O2peak / V̇E/V̇CO2 / age / BMI / cardiac risk index / serum creatinine（Snowden 2010）。
  - 723-人 colorectal：GET <11.1 mL/kg/min ROC AUC 0.79；OR 7.56（95% CI 4.44–12.86）（West 2016）。
  - GET 對 ramp rate 不敏感（5 vs 10–15 min）（Agostoni 2005；Bowen 2012）；Buchfuhrer 1983 推薦 ~10 min to maximum tolerance。
  - CP 標準測定：4 或更多 constant-load tests 各 2–15 min 至 exhaustion；single-visit 法包含 3-min all-out（Vanhatalo 2007）、Pettitt 2012、Murgatroyd 2014。
  - t_lim = W'/(P − CP)。
  - CP 解釋 cyclists 17 / 40 km TT >80% performance variance（Smith 1999）；marathon ≈ 96% CS。
  - 25+ LT 偵測方法（Faude 2009）；同一受試者 14 種 LT 範圍 243–338 W（Jamnick 2018）。
  - Broxterman 2018 vs Keir 2018 polemics：本文支持 RCP 與 deoxy-[Hb+Mb] break point **不是** CP / MLSS 有效 surrogate。
  - LT 在年輕健康未訓練者約 ~50% V̇O2max；heavy–severe 邊界 typically ~70% V̇O2max（trained 更高）。
  - 80 歲女性 GET 約占 64% predicted V̇O2max（Neder 1999）。
  - GET sensitive cutoffs 9–11 mL/kg/min ≈ 2.5–3× BMR ≈ RAUSA 跑者 nutritional intake ceiling。
  - Lactate 三大功能：energy substrate、major gluconeogenic precursor、signaling molecule（GPR81 / histone lactylation / TGF-β2 cycle）。
  - Endurance training 增加 muscle MCR（Donovan & Brooks 1983；Bergman 1999b；Dubouchaud 2000 連結 MCT 與 mitochondrial respiration）。
  - 病態 lactataemia（sepsis、cancer、TBI、dengue、hepatitis、pancreatitis）並非 ipso facto 等於 dysoxia。
- 移除或降級的陳述：
  - 舊摘要的「來源層級：1（textbook 等級）」修為「來源層級：4（high-quality narrative review）」，以對齊 CLAUDE.md §4 來源優先序。
  - 舊摘要對「正確的 ramp 時間：通常 8–12 min to exhaustion」改述為原文用語「~10 min to maximum tolerance（Buchfuhrer 1983），且 GET 對 5 vs 10–15 min ramp 不敏感（Agostoni 2005；Bowen 2012）」。
  - 舊摘要直接寫「3-min all-out test（Vanhatalo 2007）」放在「方法學重點」段，現改為 single-visit method 之一並列出 Pettitt 2012、Murgatroyd 2014 的限制（需 sustained max effort、不適 vulnerable 族群）。
  - 舊摘要的「臨床表現 / 評估方式 / 治療原則 / 臨床決策點 / 理解缺口 / 臨床使用版」等段落結構違反 skill 模板，已移除。
  - 舊摘要 link 至 [[04_CPET/Lactate_Threshold]]、[[05_Exercise_Physiology/Lactate_Shuttle]] 等不一致或不存在頁的引用，改為列入 Pages That Should Be Created or Updated 並建議下輪 audit；未自動建立 stub。
- 發現衝突：
  - 「anaerobic threshold 機制（dysoxia / Pasteur effect）成立」不成立；本文以四線證據駁斥。
  - 「lactate 為廢棄產物 / fatigue 主因」不成立；本文以 lactate shuttle theory 與多組織同時 produce/consume 取代。
  - 「lactate 上升 = tissue dysoxia」在 sepsis、TBI、cancer 等情境不成立；本文支持以 Ra/Rd 失衡與 organ-level metabolic state 解釋。
  - 「AT2 / RCT / RCP / MLSS / lactate turnpoint / individual anaerobic threshold / aerobic-anaerobic threshold / fatigue threshold 是不同 entity」不成立；本文主張同一 CP/CS 概念的不同名稱。
  - 「RCP 與 deoxy-[Hb+Mb] break point 是 CP 的 valid surrogate」不成立（Broxterman 2018 立場為本文採納）。
- 待追蹤問題：
  - 5 個 CPET 概念頁需在下輪 audit alignment：`Gas_Exchange_Threshold.md`、`Exercise_Intensity_Domains.md`、`Critical_Power.md`、`VO2_Kinetics.md`、`CPET_Protocol_Design.md`；可能還包括 `V_Slope_Method.md`、`Lactate_Threshold.md`、`Anaerobic_Threshold_概念史.md`、`Training_Prescription_by_CP.md`。
  - 各概念頁是否需補 Fact / Inference / Assumption / Uncertainty 分層，留待下輪逐頁處理。
  - 是否新建獨立 `Lactate_Shuttle` 概念頁，待後續單獨 lactate metabolism 來源（如 Ferguson 2018、Brooks 2018）入庫後再決定。
  - LT–mortality 機制 mediator 仍是 open question；未來 ingest frailty / metabolic flexibility 來源可回填。
  - GET cutoffs 在 pediatric / non-cardiopulmonary disease cohort 的外推性需另來源補。
- 待處理來源：
  - 概念頁 audit 視為下一輪工作項目；外部 raw 待處理來源沿用前一輪 stroke UpToDate 系列清單，未變動。


## [2026-05-04] ingest | UpToDate — Complications of stroke: An overview

- 類型：UpToDate topic review（來源層級 6；topic last updated 2026-02-23；literature review current through 2026-04）。
- 選擇原因：上一輪 `Aphasia: Prognosis and treatment` 後待處理 stroke UpToDate 系列中，本篇可補上 `中風復健總論` 缺少的 complication surveillance 骨架，且與 acute stroke / rehab readiness 高度相關。
- 本輪單一來源：
  - `C:\原始資料\Complications of stroke_ An overview.md`
  - 只讀取此一篇來源；未混入其他來源。
- 新增來源摘要：
  - `09_來源摘要/Complications_of_stroke_an_overview.md`
- 新增頁面：
  - `03_疾病與臨床主題/中風併發症總覽.md`
- 更新頁面：
  - `03_疾病與臨床主題/中風復健總論.md`（補入 complication surveillance 作為 rehab readiness 前置檢查，並加入來源摘要連結）
  - `index.md`（新增來源摘要與概念頁索引；更新總頁數 540 → 542）
  - `log.md`
- 抽出概念：
  - Poststroke complication surveillance：acute stroke rehab 不應只看 motor recovery，必須主動監測 dysphagia、aspiration pneumonia、VTE、UTI、cardiac complications、pulmonary complications、GI bleeding、urinary incontinence、falls、depression 與 neurologic deterioration。
  - Dysphagia–aspiration–pneumonia chain：swallow screening 是 oral medication / food 前的 safety-critical step；dysphagia 與 aspiration 會顯著增加 pneumonia risk。
  - Complication prevention as risk tradeoff：routine prevention 應理解為 routine risk assessment，不是對所有 stroke 病人 blanket 使用 prophylactic antibiotics、stress ulcer prophylaxis 或 catheter。
  - Stroke-heart / neurogenic cardiopulmonary complications：troponin elevation、ECG changes、arrhythmia、takotsubo-like dysfunction、neurogenic pulmonary edema 可能來自 stroke-related autonomic mechanisms，不可簡化為單一 ACS 或 pulmonary diagnosis。
- 本輪直接事實：
  - Medical complications after acute stroke are common and influence outcome。
  - Any in-hospital medical complication was associated with higher 30-day readmission risk（adjusted HR 1.68, 95% CI 1.04–2.73）。
  - Dysphagia compared with no dysphagia increased pneumonia risk（RR 3.17, 95% CI 2.07–4.87）；aspiration compared with no aspiration increased pneumonia risk more strongly（RR 11.56, 95% CI 3.36–39.77）。
  - Formal dysphagia screen was associated with lower aspiration pneumonia risk（adjusted OR 0.10, 95% CI 0.03–0.45；2.4% vs 5.4%）。
  - General prophylactic antibiotics may reduce overall infection but do not reduce mortality or improve functional outcome；intubated acute brain injury RCT showed single-dose ceftriaxone 2 g IV within 12h reduced VAP and 28-day mortality in a specific population.
  - UTI risk is increased by indwelling urinary catheter use and catheter duration；catheters should be avoided when possible.
  - Acute stroke cardiac surveillance includes ECG、troponin、continuous cardiac monitoring for at least first 24h.
- 發現衝突：
  - 無直接推翻既有頁面的衝突。
  - 但 `中風復健總論` 原本對 complication surveillance 的 traceability 不足，已補入新頁與來源摘要連結。
- 移除或降級的陳述：
  - 無；本輪主要是補骨架與來源追溯。
- 待追蹤問題：
  - `吞嚥障礙復健總論` 可於後續用 dysphagia 專門來源重新校正 water swallow、VFSS/FEES、NPO、tube feeding timing 與 aspiration pneumonia prevention。
  - 需後續分 subtype 整理 ischemic stroke、ICH、SAH 的 neurologic deterioration / cardiac-pulmonary risk 差異。
  - `中風併發症總覽` 後續可拆出單一概念頁：stroke-heart syndrome、poststroke UTI/catheter risk、poststroke fall/fracture prevention、poststroke respiratory complication。
- 待處理來源：
  - `C:\原始資料\Aneurysmal subarachnoid hemorrhage_ Clinical manifestations and diagnosis.md`
  - `C:\原始資料\Aneurysmal subarachnoid hemorrhage_ Treatment and prognosis.md`
  - `C:\原始資料\Spontaneous intracerebral hemorrhage_ Pathogenesis, clinical features, and diagnosis (1).md`
  - `C:\原始資料\Spontaneous intracerebral hemorrhage_ Acute treatment and prognosis.md`
  - `C:\原始資料\Antihypertensive therapy for secondary stroke prevention.md`
  - `C:\原始資料\Clinical diagnosis of stroke subtypes.md`
  - `C:\原始資料\Stroke_ Etiology, classification, and epidemiology.md`
  - `C:\原始資料\Cerebral and cervical artery dissection_ Clinical features and diagnosis.md`
  - `C:\原始資料\Etiology, clinical manifestations, and diagnosis of vascular dementia.md`
  - `C:\原始資料\Treatment of vascular cognitive impairment and dementia.md`
  - `C:\原始資料\Stroke in patients with atrial fibrillation.md`
  - `C:\原始資料\Sleep-related breathing disorders and stroke.md`

## [2026-05-04] correction | Hargreaves & Spriet 2020 — Skeletal muscle energy metabolism during exercise

- 類型：high-quality narrative review / landmark review（來源層級 4；Nature Metabolism 2020;2:817–828；DOI 10.1038/s42255-020-0251-4）。
- 選擇原因：使用者要求先做運動生理；exercise physiology raw 候選多數已有舊版 batch ingest，本輪依 5/1 後單一來源 / skill workflow 選 Hargreaves & Spriet 2020 重新整理，因其是 skeletal muscle energy metabolism 的主幹來源。
- 本輪單一來源：
  - `C:\原始資料\HargreavesSpriet-2020-Nature_Metabolism\HargreavesSpriet-2020-Nature_Metabolism.md`
  - 只讀取此一篇來源；未混入其他來源。
- 修正來源摘要：
  - `09_來源摘要/Hargreaves_Spriet_2020_muscle_energy_metabolism.md`（以 repo skill 模板重寫，補 Fact / Inference / Assumption / Uncertainty、Conflicts With Existing Knowledge、Pages That Should Be Created or Updated）。
- 新增頁面：
  - `05_Exercise_Physiology/運動營養與Ergogenic_Aids.md`
- 更新頁面：
  - `05_Exercise_Physiology/Skeletal_Muscle_Energy_Metabolism.md`（加入運動營養 / ergogenic aids 的限制因子判讀入口與來源連結）
  - `index.md`（新增運動營養頁、更新 Hargreaves source-summary 描述、Total pages 542 → 543）
  - `log.md`
- 抽出概念：
  - 三條 ATP resynthesis 路徑的動態協調：PCr、glycolysis、oxidative phosphorylation 不是依序切換，而是從 exercise onset 同時啟動，依 kinetics、power 與 capacity 分工。
  - Exercise intensity and duration determine substrate selection：高強度越依賴 carbohydrate；fat oxidation capacity 大但 rate / transition speed 不足以取代高強度 carbohydrate demand。
  - Dual-stage metabolic control：Ca2+ / epinephrine 作 feed-forward gross control，ADP / AMP / Pi / substrates 作 feedback fine-tuning。
  - Lactate as substrate and signal：lactate 不是 waste；是 oxidative substrate、gluconeogenic precursor、muscle glycogenesis substrate 與 signaling molecule。
  - Metabolic ergogenic interventions must match limiting mechanism：creatine、carbohydrate、caffeine、β-alanine、bicarbonate、nitrate、ketone / high-fat approaches、antioxidants 必須對齊 event demand 與 limitation。
- 本輪直接事實：
  - Intramuscular ATP stores 約 5 mmol/kg wet muscle；900 W all-out 若只靠 stored ATP 估計 <2 s，200 W submaximal 約 15 s。
  - 30-s all-out sprint 中 VO2 可達 70–100% VO2max，最後 5 s 約 50% energy contribution 為 aerobic。
  - Maximal fat oxidation occurs around 60–65% VO2max；80–100% VO2max 時 fuel use shifts to carbohydrate。
  - Carbohydrate loading improves events longer than about 60–90 min；carbohydrate ingestion during prolonged exercise delays but does not prevent fatigue。
  - Creatine increases total muscle creatine by 20–25% and PCr by 10–15% in cited data；long-term safety data remain limited。
  - AMPK role in exercise glucose uptake / fat oxidation appears overstated during exercise；may be more important postexercise and for adaptation.
- 發現衝突：
  - 與「anaerobic first, aerobic later」的階段式教學衝突：本文支持 all systems activate from onset but with different kinetics。
  - 與「lactate is waste / lactate causes fatigue」框架衝突：本文支持 lactate as substrate and signaling molecule；fatigue 更需看 acidosis / ionic disturbance / central-peripheral interaction。
  - 與「fat oxidation 越多越適合 endurance performance」的簡化說法衝突：high-intensity endurance 仍高度依賴 carbohydrate。
  - 與「AMPK controls exercise glucose uptake and fat oxidation」簡化說法衝突：本文明確指出此角色 during exercise 被高估。
- 移除或降級的陳述：
  - 舊摘要的「來源層級：Tier 1」改為「來源層級 4（high-quality review）」以對齊新版 AGENTS.md 來源優先序；其內容仍可作運動代謝主幹框架，但不是 guideline 或 systematic review。
- 待追蹤問題：
  - `運動營養與Ergogenic_Aids.md` 後續若要變成可用處方頁，需另查 IOC consensus、ISSN position stands、ACSM / sports nutrition guideline 等更直接來源。
  - `Lactate_Shuttle.md` 需用 Brooks / lactate shuttle 專門來源重做，避免只靠 Hargreaves & Spriet 和 Poole 2020。
  - `Skeletal_Muscle_Energy_Metabolism.md` 仍需逐步改成完全符合 skill 的 Fact / Inference / Assumption / Uncertainty 結構。

## [2026-05-04] correction | Chow et al. 2022 — Exerkines in health, resilience and disease

- 類型：high-quality narrative / expert review（Nature Reviews Endocrinology 2022;18:273–289；DOI 10.1038/s41574-022-00641-2）。
- 選擇原因：延續 exercise physiology；此來源已在 5/4 建過摘要與 exerkine 概念頁，但需依新版 AGENTS.md 來源層級與單一概念拆頁邏輯補強 methodology / response variability 概念。
- 本輪單一來源：
  - `C:\原始資料\Exerkines in health, resilience and disease\Exerkines in health, resilience and disease.md`
  - 只讀取此一篇來源；未混入其他來源。
- 修正來源摘要：
  - `09_來源摘要/Chow_2022_exerkines_health_resilience_disease.md`（來源層級由 Tier 1 修為 Tier 4 high-quality narrative / expert review；保留其概念整理價值，但不當作 guideline / systematic review）。
- 新增頁面：
  - `05_Exercise_Physiology/Exercise_Response_Variability與Exerkine_研究設計.md`
- 更新頁面：
  - `05_Exercise_Physiology/Exerkines_運動誘發多器官訊號分子.md`（來源層級修為 Tier 4，加入 response variability / study design 連結）。
  - `index.md`（新增 methodology concept；更新 exerkines 與 Chow source-summary 的 Tier / 描述；Total pages 543 → 544）。
  - `log.md`
- 抽出概念：
  - Exercise response variability：同一 exercise label 不等於同一 biological exposure；mode、intensity、duration、timing、feeding state、sampling window、fitness、genetics、phenotype、comorbidity 都會改變 response。
  - Acute vs chronic mismatch：acute exerkine response 不一定平行 chronic training response；recent 24–72h exercise 也會干擾 resting trained-state measurement。
  - Biomarker vs mediator：exerkine association 不等於 causal mediation；candidate exerkine 要成為臨床 target 需 human validation、mechanistic proof 與 patient-relevant outcome linkage。
  - Methodology requirement：exerkine / exercise omics study 需記錄 exposure metadata、sampling context、assay platform、tissue / plasma / EV source 與 phenotype。
- 本輪直接事實：
  - Chow et al. define exerkines as signalling moieties released in response to acute and/or chronic exercise acting through endocrine / paracrine / autocrine pathways。
  - The review states acute exerkine response does not necessarily parallel chronic training response。
  - HERITAGE data cited: aerobic capacity response heritability around 47%；around 20% non-response for improved aerobic capacity；7–15% adverse response in selected cardiometabolic variables。
  - MoTrPAC is cited as NIH-supported large-scale effort to characterize molecular transducers of physical activity。
  - The review states “exercise in a pill” remains wishful thinking。
- 發現衝突：
  - 與「exerkine = myokine」混用衝突；myokine 只是 skeletal muscle-derived subset。
  - 與「acute molecular signal 可直接代表 chronic adaptation」衝突；本來源明確指出兩者不一定平行。
  - 與「animal / cell model 可直接轉譯人類處方」衝突；本來源將 animal-human inconsistency 列為 contentious question。
- 移除或降級的陳述：
  - `Chow_2022_exerkines_health_resilience_disease.md` 與 `Exerkines_運動誘發多器官訊號分子.md` 的 source_tier 由 1 改為 4，以對齊 AGENTS.md 來源優先序。
- 待追蹤問題：
  - 若要把 exerkine 轉成 clinical biomarker / therapeutic target，需後續找 MoTrPAC output、human intervention trials、mediation analyses 與 disease-specific studies。
  - `Myokines_與_Muscle_Organ_Crosstalk.md` 可後續以 Severinsen & Pedersen 2020 單獨重做，與 broader exerkine framework 對齊。

## [2026-05-04] correction | Egan & Sharples 2023 — Molecular responses to acute exercise and skeletal muscle adaptation

- 類型：high-quality narrative / expert review（review article；acute exercise-induced signal transduction and skeletal muscle adaptation）。
- 選擇原因：延續 exercise physiology；此來源是 `Acute_Exercise_Molecular_Response與Skeletal_Muscle_Adaptation` 的主來源，適合依 AGENTS.md + skill 重新整理，避免舊摘要把 acute molecular response 過度當成 chronic adaptation 預測公式。
- 本輪單一來源：
  - `C:\原始資料\egan-sharples-2023-molecular-responses-to-acute-exercise-and-their-relevance-for-adaptations-in-skeletal-muscle-to\egan-sharples-2023-molecular-responses-to-acute-exercise-and-their-relevance-for-adaptations-in-skeletal-muscle-to.md`
  - 只讀取此一篇來源；未混入其他來源。
- 修正來源摘要：
  - `09_來源摘要/Egan_Sharples_2023_acute_exercise_molecular_responses.md`（以 skill 模板重寫，補 Core Concepts、Known Facts、Mechanism Chain、Inferences、Assumptions、Uncertainties / Limitations、Conflicts With Existing Knowledge）。
- 更新頁面：
  - `05_Exercise_Physiology/Acute_Exercise_Molecular_Response與Skeletal_Muscle_Adaptation.md`（source_tier 1 → 4；補 What It Is Not、事實、常見誤用、與 `Exercise_Response_Variability與Exerkine_研究設計` 連結）。
  - `index.md`（更新 Egan source-summary 與 acute molecular response concept 的 Tier / 描述；無新增頁面，Total pages 維持 544）。
  - `log.md`
- 抽出概念：
  - Acute-to-chronic adaptation as a working model：每次 acute exercise 的 transient molecular response 可能在 repeated, progressive, recoverable training exposure 下累積為 protein abundance / activity 與 phenotype，但不是已完全驗證的線性公式。
  - Exercise stimulus specificity and overlap：aerobic、resistance、HIIT、SIT、concurrent training 在 force、velocity、duration、frequency、contraction number、recovery 上不同，但分子與 phenotype response 有重疊，不是互斥盒子。
  - Signals, sensors, transduction, effectors：intrinsic / extrinsic signals 經 sensor proteins / receptors、kinase/phosphatase/PTM/translocation networks，調控 transcription、translation、degradation、organelle remodeling。
  - Training status / first-bout effect / response attenuation：強 first-bout response 可能反映 novelty / damage / stress；training 後 attenuation 可能代表 adaptation，不等於刺激失效。
  - Translational limits and exercise mimetics：exercise 是 multi-organ repeated behavioral exposure，單一 pathway activation 不等於能取代 exercise。
- 本輪直接事實：
  - Repeated, episodic skeletal muscle contraction 是 structured exercise training 的基本 stimulus。
  - Acute exercise signals include neuronal、mechanical、metabolic、hormonal stimuli。
  - Intrinsic signals include Ca2+、ATP/ADP/Pi、redox、glycogen、pH、PO2、RONS、temperature、mechanical load/tension。
  - Exercise categories include aerobic/endurance, resistance/strength, circuit, concurrent, HIIT, SIT, sprint training。
  - Training volume and session characteristics determine type and magnitude of adaptation。
  - The source explicitly states that the acute-to-chronic model is a working model and not fully validated。
- 發現衝突：
  - 與「單次 mRNA / phosphorylation / MPS 上升即可預測 chronic phenotype」衝突。
  - 與「aerobic vs resistance 是完全分離 molecular boxes」衝突；來源支持 overlap / continuum。
  - 與「exercise mimetic 可取代 exercise」衝突；來源支持 adjunct / target discovery，但不支持取代 exercise。
- 移除或降級的陳述：
  - `Egan_Sharples_2023_acute_exercise_molecular_responses.md` 與 `Acute_Exercise_Molecular_Response與Skeletal_Muscle_Adaptation.md` 的 source_tier 由 1 改為 4，以對齊 AGENTS.md 來源優先序。
- 待追蹤問題：
  - `Furrer_2023_molecular_athlete.md` 與 `Smith_2023_exercise_metabolism_adaptation_skeletal_muscle.md` 目前仍在 acute molecular page 中作補充，後續也應逐篇依單一來源修正來源層級與概念邊界。
  - 若要支持 clinical exercise prescription，仍需 disease-specific guideline / trial / consensus；此 review 只能支持 mechanistic literacy。

## [2026-05-04] correction | Poole et al. 2020 — The anaerobic threshold: 50+ years of controversy

- 類型：topical / high-quality narrative review（J Physiol 2021;599(3):737–767；DOI: 10.1113/JP279963）。
- 選擇原因：使用者要求以 exercise physiology 文章開始並由我選一篇完整跑 workflow；此來源是 CPET / exercise physiology 中 AT、LT、GET、CP/CS 邊界混淆的核心整理來源。
- 本輪單一來源：
  - `C:\原始資料\The Journal of Physiology - 2020 - Poole - The anaerobic threshold  50  years of controversy\The Journal of Physiology - 2020 - Poole - The anaerobic threshold  50  years of controversy.md`
  - 只讀取此一篇來源；未混入第二篇 raw source。
- 修正來源摘要：
  - `09_來源摘要/Poole_2020_anaerobic_threshold.md`（標記本輪已更新頁面；來源層級維持 Tier 4 high-quality narrative / topical review）。
- 更新頁面：
  - `04_CPET/Anaerobic_Threshold_概念史.md`（改為單一概念頁；補 Definition / Mechanism / Fact / Inference / Assumption / Uncertainty；source_tier 1 → 4）。
  - `04_CPET/Lactate_Threshold.md`（補 LT 不等於 dysoxia、LT vs CP 邊界與 uncertainty；source_tier 1 → 4）。
  - `04_CPET/Gas_Exchange_Threshold.md`（補 GET 判讀假設、false positive / false negative caveats、clinical cutoff 外推限制；source_tier 1 → 4）。
  - `index.md`（更新 AT / LT / GET 與 Poole source-summary 的描述與 Tier；無新增頁面，Total pages 維持 544）。
  - `log.md`
- 抽出概念：
  - AT 是歷史術語，不應再作為 muscle dysoxia 的機制描述。
  - LT / GET 是 moderate → heavy boundary；CP / CS 才是 heavy → severe / sustainable-vs-unsustainable boundary。
  - Lactate accumulation 代表 Ra > Rd，不等於 tissue oxygenation 不足。
  - GET 必須靠 V-slope 與 isocapnic buffering 支持；pre-test hyperventilation、高海拔、McArdle disease、severe HF / COPD 可能造成錯判或無法判讀。
- 本輪直接事實：
  - Poole et al. 明確主張目前沒有直接證據支持 exercising muscle 在 LT，或 V̇O2max 以下任何 V̇O2，變成 anaerobic / dysoxic。
  - GET <40% predicted V̇O2max 通常被視為 clinically abnormal trigger。
  - GET <11 mL/kg/min 在 heart failure 與部分 perioperative cohorts 中具有 risk signal，但 cutoffs 不可跨族群直接套用。
- 發現衝突：
  - 與「AT = 開始無氧 / 缺氧」的傳統教學衝突。
  - 與「lactate 上升 = fatigue cause / waste product」的簡化說法衝突。
  - 與「用 LT/GET 判定 severe-domain exhaustion」的做法衝突。
- 移除或降級的陳述：
  - `Anaerobic_Threshold_概念史.md`、`Lactate_Threshold.md`、`Gas_Exchange_Threshold.md` 與 `index.md` 中 Poole 2020 相關 Tier 1 標示修為 Tier 4。
- 待追蹤問題：
  - `Exercise_Intensity_Domains.md`、`Critical_Power.md`、`VO2_Kinetics.md`、`CPET_Protocol_Design.md` 後續仍可逐篇做 alignment audit。
  - 若要把 GET cutoffs 用於 disease-specific clinical decision，需另查 guideline、consensus 或 disease-specific cohort / review。

## [2026-05-04] correction | Severinsen & Pedersen 2020 — Muscle-Organ Crosstalk: The Emerging Roles of Myokines

- 類型：high-quality narrative / expert review（Endocrine Reviews 2020;41:594-609）。
- 選擇原因：使用者要求「再一次」跑 exercise physiology workflow；前一輪已把 `Myokines_與_Muscle_Organ_Crosstalk.md` 標記為後續需要用 Severinsen & Pedersen 2020 單獨重做。
- 本輪單一來源：
  - 主文：`C:\原始資料\bnaa016\bnaa016.md`
  - Corrigendum：`C:\原始資料\bnaa024\bnaa024.md`，只用於同一篇文章的圖示修正：IL-6 inhibits appetite，不是 stimulates appetite。
  - 未混入其他研究主文或第二篇 review。
- 修正來源摘要：
  - `09_來源摘要/Severinsen_Pedersen_2020_myokines_muscle_organ_crosstalk.md`（依 skill 模板重寫；source_tier 1 → 4；補 Core Concepts、Fact / Inference / Assumption / Uncertainty）。
- 新增頁面：
  - `05_Exercise_Physiology/Exercise_Induced_IL-6_作為Myokine.md`
- 更新頁面：
  - `05_Exercise_Physiology/Myokines_與_Muscle_Organ_Crosstalk.md`（改成單一概念總頁；移除多來源混寫；source_tier 1 → 4）。
  - `index.md`（新增 IL-6 concept；更新 Myokines 與 Severinsen source-summary 描述；Total pages 544 → 545）。
  - `log.md`
- 抽出概念：
  - Myokines：由 muscle fibers produced / expressed / released，具 autocrine、paracrine 或 endocrine effects。
  - Myokines vs exerkines：myokines 是 muscle-derived subset；exerkines 是 broader exercise-induced multi-organ signals。
  - Exercise-induced IL-6：目前本文中 human evidence 最強的 myokine，與 chronic basal IL-6 elevation 不能混用。
  - Evidence stratification：muscle-brain、muscle-adipose、muscle-liver、muscle-gut、muscle-pancreas、muscle-skin、muscle-cancer axes 的 human support 不同，不可同等陳述。
- 本輪直接事實：
  - 本來源指出 myokinome 已識別超過 650 myokines，但 biological function 只描述約 5%。
  - Human contracting skeletal muscle 可產生並釋放 IL-6 into circulation。
  - IL-6 infusion in humans can improve insulin-stimulated glucose uptake, stimulate IL-1ra / IL-10, and inhibit endotoxin-induced TNF production。
  - Exercise-induced visceral fat loss in abdominally obese humans was abolished by IL-6 receptor blockade in the cited trial。
  - Corrigendum 修正 IL-6 appetite effect：IL-6 inhibits appetite。
- 發現衝突：
  - 與「IL-6 只是不好的 inflammatory marker」衝突；來源支持 exercise-induced transient IL-6 的 context-dependent metabolic / anti-inflammatory role。
  - 與「myokine = exerkine」混用衝突；本文區分 muscle-derived myokines 與 broader exerkines。
  - 與「所有候選 myokines 都已有 clinical biomarker utility」衝突；來源明確指出只有少數 myokines 在 humans 中有明確功能。
- 移除或降級的陳述：
  - `Severinsen_Pedersen_2020_myokines_muscle_organ_crosstalk.md` 與 `Myokines_與_Muscle_Organ_Crosstalk.md` 的 Tier 1 標示修正為 Tier 4 high-quality narrative review。
  - Myokines page 移除 Hargreaves / Chow 作為同頁 source，避免本輪單一來源頁面混寫；改以 Links 連接 broader exerkine / metabolism pages。
- 待追蹤問題：
  - `Exerkines_運動誘發多器官訊號分子.md` 可後續補上 myokines are subset of exerkines 的明確回鏈。
  - 若要把 IL-6 作為 clinical intervention target，需另查 disease-specific IL-6 blockade / exercise interaction studies，不可只用本 review。

## [2026-05-04] correction | Smith et al. 2023 — Exercise metabolism and adaptation in skeletal muscle

- 類型：high-quality narrative / expert review（Nature Reviews Molecular Cell Biology 2023;24(9):607-632；DOI: 10.1038/s41580-023-00606-x）。
- 選擇原因：使用者要求完整跑一次 workflow 並以運動生理文獻開始；本來源是 skeletal muscle exercise metabolism、metabolic flexibility 與 training adaptation 的核心 review，且既有摘要 / 概念頁仍沿用舊版 Tier 1 標示。
- 本輪單一來源：
  - `C:\原始資料\nihms-1908393\nihms-1908393.md`
  - 只讀取此一篇來源；未混入其他 raw source。
- 修正來源摘要：
  - `09_來源摘要/Smith_2023_exercise_metabolism_adaptation_skeletal_muscle.md`（source_tier 1 → 4；補 `Skeletal Muscle Mitochondrial Reticulum` 概念區塊）。
- 新增頁面：
  - `05_Exercise_Physiology/Skeletal_Muscle_Mitochondrial_Reticulum.md`
- 更新頁面：
  - `05_Exercise_Physiology/Skeletal_Muscle_Metabolic_Flexibility與Exercise_Adaptation.md`（source_tier 1 → 4；補 mitochondrial reticulum 連結）。
  - `05_Exercise_Physiology/Skeletal_Muscle_Energy_Metabolism.md`（補 mitochondrial reticulum 作為 subcellular energy distribution / quality control 概念）。
  - `index.md`（新增 mitochondrial reticulum 頁；更新 Smith source-summary 與 metabolic flexibility tier；Total pages 545 → 546）。
  - `log.md`
- 抽出概念：
  - Skeletal muscle mitochondrial reticulum：subsarcolemmal / peripheral mitochondria 與 intermyofibrillar mitochondria 形成能量分配與 quality control 網路。
  - Mitochondrial adaptation 不只看 total mitochondrial content；location、network connectivity、cristae / supercomplex structure 與 organelle contacts 都可能改變 interpretation。
- 本輪直接事實：
  - Mitochondria 約佔 skeletal muscle volume 2-10%，依 fiber type 而異。
  - Subsarcolemmal / peripheral mitochondria 靠近 sarcolemma / capillaries，且有較多 cristae / matrix 與 ETC complex IV。
  - Intermyofibrillar mitochondria 與 myofibrillar matrix、SR、intermyofibrillar lipid droplets 接觸，並具較高 ATP synthase expression 與 surface area-to-volume ratio。
  - Lifelong endurance exercisers in older age 被來源整理為具有較高 mitochondrial density、較複雜與連通的 mitochondrial reticulum，並伴隨較高 OPA1 protein levels。
- 發現衝突：
  - 與「mitochondria 變多」即可完整描述 exercise adaptation 的簡化說法衝突；來源支持 subpopulation / network / location 層級的判讀。
  - 與「mitochondrial content、respiration、reticulum、cristae、supercomplexes 可混用」衝突；本輪拆成不同層級。
- 移除或降級的陳述：
  - `Smith_2023_exercise_metabolism_adaptation_skeletal_muscle.md` 與 `Skeletal_Muscle_Metabolic_Flexibility與Exercise_Adaptation.md` 的 Tier 1 標示修正為 Tier 4 high-quality review。
- 待追蹤問題：
  - `Muscle_Fiber_Types.md` 與 `Acute_Exercise_Molecular_Response與Skeletal_Muscle_Adaptation.md` 仍可後續逐篇檢查是否過度混用 Smith、Blemker、Egan 等來源。
  - 若要把 mitochondrial reticulum 轉成 clinical biomarker 或 exercise prescription，需要 human intervention outcome / disease-specific data，不能只用本 review。

## [2026-05-04] correction | Furrer et al. 2023 — The Molecular Athlete

- 類型：review article。
- 選擇原因：使用者要求「再一次」完整跑 workflow；本來源是 exercise physiology、elite athlete phenotype、training response variability 與 molecular adaptation 的高品質 review，且既有頁面仍沿用舊版 Tier 1 標示。
- 本輪單一來源：
  - `C:\原始資料\furrer-et-al-2023-the-molecular-athlete-exercise-physiology-from-mechanisms-to-medals\furrer-et-al-2023-the-molecular-athlete-exercise-physiology-from-mechanisms-to-medals.md`
  - 只讀取此一篇來源；未混入其他 raw source。
- 修正來源摘要：
  - `09_來源摘要/Furrer_2023_molecular_athlete.md`（source_tier 1 → 4；補 Source Type、Reliability Level、One-Sentence Summary、Core Concepts Extracted）。
- 新增頁面：
  - `05_Exercise_Physiology/Exercise_Training_Response_Low_Sensitivity.md`
- 更新頁面：
  - `05_Exercise_Physiology/Molecular_Athlete_運動表型連續體.md`（source_tier 1 → 4；補 low sensitivity 概念連結）。
  - `index.md`（新增 low sensitivity concept；更新 Furrer source-summary 與 molecular athlete tier；Total pages 546 → 547）。
  - `log.md`
- 抽出概念：
  - Exercise Training Response Low Sensitivity：對特定 stimulus、dose 或單一 outcome 的低反應，不應直接標記為 permanent non-responder。
  - Molecular Athlete：inactive-to-elite performance continuum 是 intrinsic / extrinsic factors、systems physiology 與 molecular networks 的整合，不是單一 VO2max、gene 或 pathway。
- 本輪直接事實：
  - 來源指出 training response 存在 large interindividual variability。
  - 來源引用 Montero and Lundby 的 6-week supervised cycling dose-response study；以 Wmax 定義時，nonresponse 比例隨每週 sessions 增加而下降，4 或 5 sessions/week 時為 0%。
  - 來源主張 non-responder label 需謹慎，較精確說法是 low sensitivity to a given stimulus or outcome。
  - 來源指出 exercise 是多 pathway / multi-organ 的 polypill，單一 outcome 低反應不代表所有 benefits 不存在。
- 發現衝突：
  - 與「non-responder 是固定體質」衝突；來源支持 outcome-specific / dose-specific 解讀。
  - 與「單一 outcome 未改善 = exercise 無效」衝突；來源提醒 exercise 同時影響多個 organs、pathways 與 outcomes。
  - 與「elite athlete 的 high responsiveness 可直接外推到一般人」衝突；來源區分 elite performance 與一般 health-related training response。
- 移除或降級的陳述：
  - `Furrer_2023_molecular_athlete.md` 與 `Molecular_Athlete_運動表型連續體.md` 的 Tier 1 標示修正為 Tier 4 review article。
- 待追蹤問題：
  - 若要建立 disease-specific low-response management algorithm，需另查 guideline、clinical trial 或 disease-specific cohort，不能只用本 review。
  - `Exercise_Response_Variability與Exerkine_研究設計.md` 後續可補回本頁，區分 general training response variability 與 exerkine-specific study design。

## [2026-05-04] ingest | Initial assessment and management of acute stroke

- 類型：UpToDate topic review（literature review current through 2026-04；topic last updated 2026-03-24）。
- 選擇原因：成人 acute stroke first-hours workflow 臨床風險高，來源為最新 UpToDate topic review，且尚無獨立來源摘要。
- 本輪單一來源：
  - `C:\原始資料\Initial assessment and management of acute stroke.md`
  - 只讀取此一篇來源；未修改 `C:\原始資料`。
- 新增來源摘要：
  - `09_來源摘要/UpToDate_initial_assessment_management_acute_stroke.md`
- 新增頁面：
  - `03_疾病與臨床主題/Acute_Stroke_Initial_Assessment與Stabilization.md`
- 更新頁面：
  - `03_疾病與臨床主題/中風急性期處置與時間窗.md`
  - `index.md`
  - `log.md`
- 抽出概念：
  - Acute stroke initial assessment 與 stabilization：first-hours workflow 以 LKW、ABC、glucose / SpO2、NCCT、NIHSS、IVT / EVT triage、BP、swallow、position 與 stroke-unit care 並行處理。
- 本輪直接事實：
  - 多數情境下 history、physical examination、serum glucose、oxygen saturation、noncontrast CT 足以引導 acute therapy。
  - Additional tests 不應在 otherwise indicated 的情境延誤 therapy。
  - Hypoxic patients 補充 oxygen 維持 saturation >94%；nonhypoxic acute ischemic stroke 不 routine 給 oxygen。
  - IVT 前 BP 需 ≤185/110 mmHg；治療後至少 24 小時維持 ≤180/105 mmHg。
  - 未接受 IVT / EVT 的 ischemic stroke 通常不急性降壓，除非 >220/120 mmHg 或有特定 comorbid indication。
  - Oral medication / food 前需做 swallowing assessment；未評估前 NPO。
  - Stable patients after 24 hours mobilization 可能減少 complications；within 24 hours very early mobilization may be harmful。
- 發現衝突：
  - 與「acute ischemic stroke BP 高就要降」衝突；本來源支持 first-hours 避免 reflex lowering。
  - 與「stroke 越早下床越好」衝突；本來源支持 within 24 hours very early mobilization 可能有害。
  - 與「nonhypoxic stroke routine oxygen」衝突；本來源不支持 routine oxygen。
- 待追蹤問題：
  - `中風急性期處置與時間窗.md` 舊有「lacunar / DM：SBP <140」需回查原 guideline / source；本輪 UpToDate 2026 不支持將其當 first-hours generic rule。
  - 若要處理 IVT / EVT 細節，需另行單一來源 ingest reperfusion 專題或 AHA/ASA guideline。

## [2026-05-04] correction | Blemker et al. 2023/2024 — Fiber-type Traps

- 類型：synthesis / perspective review。
- 選擇原因：使用者要求「再一次」跑 exercise physiology workflow；`Blemker_2023_fiber_type_traps.md` 與 `Muscle_Fiber_Types.md` 仍沿用舊版 Tier 1 標示，且前一輪 Smith workflow 已標記 `Muscle_Fiber_Types.md` 後續需逐篇檢查。
- 本輪單一來源：
  - `C:\原始資料\blemker-et-al-2023-fiber-type-traps-revisiting-common-misconceptions-about-skeletal-muscle-fiber-types-with-application\blemker-et-al-2023-fiber-type-traps-revisiting-common-misconceptions-about-skeletal-muscle-fiber-types-with-application.md`
  - 只讀取此一篇來源；未混入 Hargreaves、Smith、Poole 或其他 raw source。
- 修正來源摘要：
  - `09_來源摘要/Blemker_2023_fiber_type_traps.md`（source_tier 1 → 4；改寫為 Source Type、Reliability Level、One-Sentence Summary、Core Concepts Extracted、Fact / Inference / Assumption / Uncertainty 結構）。
- 新增頁面：
  - `05_Exercise_Physiology/Muscle_Fiber_Type_Traps.md`
- 更新頁面：
  - `05_Exercise_Physiology/Muscle_Fiber_Types.md`（source_tier 1 → 4；補 Blemker 單一來源拆頁回鏈）。
  - `index.md`（新增 fiber-type traps concept；更新 Blemker source-summary 與 Muscle Fiber Types tier；Total pages 552 → 553）。
  - `log.md`
- 抽出概念：
  - Muscle Fiber Type Traps：MHC isoform、oxidative capacity、CSA 與 force-generating capacity 是不同測量軸，不能互相當作 surrogate。
  - Muscle Fiber Types：使用 fiber type 時需明確說明分類依據是 MHC、oxidative enzymes、mitochondrial content、CSA、fatiguability、specific force 或 whole-muscle mechanics。
- 本輪直接事實：
  - 來源 abstract 直接列出三個 assumptions：MHC isoform 等同 oxidative capacity、CSA 是 MHC / oxidative capacity surrogate、force-generating capacity 可由 MHC isoform 推論。
  - 來源指出這些 assumptions 會影響 experimental design、computational modeling 與 findings interpretation。
  - 來源指出 metabolic properties across fibers form a continuum，且會受 muscle、species、habitual activity level 與 disease state 影響。
  - 來源 discussion 建議研究者保留 experimental context、使用 precise vocabulary、清楚說明 actual measurement，並承認 fibers exist on a structure-function continuum。
- 發現衝突：
  - 與「type I = slow oxidative、type II = fast glycolytic」的一對一教學簡化衝突；來源支持多軸解讀。
  - 與「CSA 可推論 fiber type」衝突；來源把 CSA 定位為 morphology measurement。
  - 與「whole-muscle force 可由 MHC distribution 推回」衝突；來源強調 architecture、coordination、motor unit recruitment 與 force transmission 等因素。
- 移除或降級的陳述：
  - `Blemker_2023_fiber_type_traps.md` 與 `Muscle_Fiber_Types.md` 的 Tier 1 標示修正為 Tier 4 synthesis / perspective review。
- 待追蹤問題：
  - `Skeletal_Muscle_Energy_Metabolism.md` 仍可後續逐段 audit fiber type 相關語句，避免 MHC 與 oxidative capacity 混用。
  - `VO2_Slow_Component.md` 若以 type II recruitment 解釋效率下降，需補清楚是 recruitment / ATP cost / efficiency 邏輯，不可寫成 type II 必然 low oxidative。

## [2026-05-04] correction | Oliveira et al. 2024 — Polarized vs Other Training Intensity Distributions

- 類型：systematic review with meta-analysis（Sports Medicine 2024；PROSPERO CRD42022365117）。
- 選擇原因：使用者要求「再一次」跑 exercise physiology workflow；`Oliveira_2024_polarized_training_meta_analysis.md` 與 `Training_Intensity_Distribution.md` 仍沿用舊版 Tier 1 標示。
- 本輪單一來源：
  - `C:\原始資料\Polarized vs. Other Training Intensity Distribution Regimens and Endurance Performance\Polarized vs. Other Training Intensity Distribution Regimens and Endurance Performance.md`
  - 只讀取此一篇來源；未混入 Furrer、Poole、CP / threshold review 或其他 raw source。
- 修正來源摘要：
  - `09_來源摘要/Oliveira_2024_polarized_training_meta_analysis.md`（source_tier 1 → 3；改寫為 Source Type、Reliability Level、One-Sentence Summary、Core Concepts Extracted、Fact / Inference / Assumption / Uncertainty 結構）。
- 新增頁面：
  - `05_Exercise_Physiology/Polarized_Training_證據邊界.md`
- 更新頁面：
  - `05_Exercise_Physiology/Training_Intensity_Distribution.md`（source_tier 1 → 3；補 Oliveira 單一來源拆頁回鏈）。
  - `index.md`（新增 polarized training evidence-boundary concept；更新 Oliveira source-summary 與 TID tier；Total pages 553 → 554）。
  - `log.md`
- 抽出概念：
  - Polarized Training 證據邊界：POL 對 VO2peak 有 small superiority，尤其在 <12 weeks intervention 與 highly trained / national-level athletes；但對 TT、TTE、V/P at VT2/LT2 沒有 superiority。
  - Training Intensity Distribution：TID 比較必須先定義 physiological zones 與 outcome，不可只比較 POL / PYR / THR 名稱。
- 本輪直接事實：
  - 來源納入 17 studies，共 437 subjects；14 studies 進入 meta-analysis。
  - POL 對 VO2peak 優於 other TIDs：SMD 0.24，95% CI 0.01-0.48，p=0.040，I2=0%。
  - <12 weeks intervention 中 VO2peak 優勢較明顯：SMD 0.40，95% CI 0.08-0.71，p=0.01。
  - Highly trained / national-level athletes 中 VO2peak 優勢較明顯：SMD 0.46，95% CI 0.10-0.82，p=0.01。
  - TT、TTE、V/P at VT2/LT2 均未顯示 POL superiority。
  - Sex subgroup analysis 因 sex reporting 不足而無法進行。
- 發現衝突：
  - 與「POL 是全面最佳耐力訓練模式」衝突；來源只支持 outcome-specific VO2peak 小幅優勢。
  - 與「VO2peak 提升 = race performance 一定提升」衝突；TT 與 threshold-related outcomes 未顯示 superiority。
  - 與「athlete TID 可直接套到 PM&R / cardiac rehab / pulmonary rehab」衝突；來源納入族群以 athletes / healthy adults 為主，clinical disease populations 需另查來源。
- 移除或降級的陳述：
  - `Oliveira_2024_polarized_training_meta_analysis.md` 與 `Training_Intensity_Distribution.md` 的 Tier 1 標示修正為 Tier 3 systematic review with meta-analysis。
- 待追蹤問題：
  - `Training_Intensity_Distribution.md` 仍需後續逐篇檢查 Poole / Furrer 對 intensity domains、periodization、recovery 的來源歸屬。
  - 若要用 POL 建立 disease-specific rehabilitation prescription，需另查 clinical systematic review 或 guideline。

## [2026-05-04] ingest | Spontaneous intracerebral hemorrhage: Acute treatment and prognosis

- 類型：UpToDate topic review（literature review current through 2026-04；topic last updated 2026-04-29）。
- 選擇原因：
  - `C:\原始資料\Spontaneous intracerebral hemorrhage_ Acute treatment and prognosis.md` 尚無獨立 `09_來源摘要`。
  - 既有 `中風急性期處置與時間窗.md` 已有 ICH 急性期段落，但 BP 目標寫成「SBP 130-150」過度簡化，需要用單一來源修正。
- 本輪單一來源：
  - `C:\原始資料\Spontaneous intracerebral hemorrhage_ Acute treatment and prognosis.md`
  - 只讀取此一篇來源；未混入 ICH diagnosis、secondary prevention、SAH、ischemic reperfusion 或其他 raw source。
- 新增來源摘要：
  - `09_來源摘要/UpToDate_spontaneous_intracerebral_hemorrhage_acute_treatment_prognosis.md`
- 新增頁面：
  - `03_疾病與臨床主題/Spontaneous_ICH_急性抗擴大與Neurocritical_Stabilization.md`
- 更新頁面：
  - `03_疾病與臨床主題/中風急性期處置與時間窗.md`（修正 ICH BP 分層、anticoagulation reversal、platelet transfusion、ICP / surgery、seizure prophylaxis 與早期 prognosis 邏輯）。
  - `index.md`（新增 ICH concept 與 source summary；Total pages 554 → 556）。
  - `log.md`
- 抽出概念：
  - Spontaneous ICH acute anti-expansion and neurocritical stabilization：急性處置重點是 stop antithrombotics、reverse anticoagulation、controlled BP lowering、ICP prevention / monitoring、selected surgery、seizure treatment only when present 與 delayed prognostication。
- 本輪直接事實：
  - Source 將 acute ICH treatment goals 定為 preventing hemorrhage extension、monitoring/managing elevated ICP、managing neurologic and medical complications。
  - Acute ICH 初期所有 anticoagulant / antiplatelet drugs 應停用；anticoagulant reversal 應 immediate and medication-specific。
  - Warfarin-associated ICH source 偏好 4-factor PCC，並搭配 IV vitamin K 維持 reversal。
  - SBP 150-220 mmHg 且 clinically stable：target 140 mmHg，理想上 first hour 達成。
  - SBP >220 mmHg：先快速降到 <220 mmHg，再於 stable 時逐步降到 140-160 mmHg。
  - First hours 應避免 SBP <130 mmHg。
  - 多數 antiplatelet-associated ICH 不 routine platelet transfusion；selected emergency surgery 才可能考慮。
  - 沒有 seizure 的 acute ICH patients 不應 prophylactic antiseizure medication。
  - ICH score / FUNC score 可估 prognosis，但不應在 first day 單獨作為新的 care limitation 依據。
- 發現衝突：
  - 與「ICH 一律快降到 SBP 130-150」衝突；本來源支持依 presenting SBP 分層，且避免 first-hours SBP <130。
  - 與「antiplatelet-associated ICH 應 routine platelet transfusion」衝突；source 指出可能 harm，僅 selected emergency surgery 才考慮。
  - 與「no seizure 也預防性給 antiseizure medication」衝突；source 不支持 prophylaxis。
  - 與「嚴重 ICH 第一日即可用 prediction score 決定撤治療」衝突；source 強調 prognosis uncertainty 與 self-fulfilling outcome risk。
- 待追蹤問題：
  - `Spontaneous intracerebral hemorrhage_ Pathogenesis, clinical features, and diagnosis (1).md` 尚需另行單一來源 ingest。
  - Spontaneous ICH secondary prevention / long-term prognosis 尚需另查來源，不能由本頁外推。
  - 若要把 ICH treatment recommendation 升級為 guideline-grade page，需另行單一來源 ingest AHA/ASA ICH guideline。

## [2026-05-05] ingest | Spontaneous intracerebral hemorrhage: Pathogenesis, clinical features, and diagnosis

- 類型：UpToDate topic review（literature review current through 2026-04；topic last updated 2025-11-21）。
- 選擇原因：
  - `C:\原始資料\Spontaneous intracerebral hemorrhage_ Pathogenesis, clinical features, and diagnosis (1).md` 尚無獨立 `09_來源摘要`。
  - 上一輪已建立 spontaneous ICH acute treatment/prognosis 頁；本篇是同一 ICH 主題中下一個最高相關、尚未處理的 diagnosis / etiology / expansion-risk source。
- 本輪單一來源：
  - `C:\原始資料\Spontaneous intracerebral hemorrhage_ Pathogenesis, clinical features, and diagnosis (1).md`
  - 只讀取此一篇來源；未混入 acute treatment、secondary prevention、SAH、ischemic stroke evaluation 或其他 raw source。
- 新增來源摘要：
  - `09_來源摘要/UpToDate_spontaneous_intracerebral_hemorrhage_pathogenesis_clinical_features_diagnosis.md`
- 新增頁面：
  - `03_疾病與臨床主題/Spontaneous_ICH_診斷與病因分層.md`
- 更新頁面：
  - `03_疾病與臨床主題/Spontaneous_ICH_急性抗擴大與Neurocritical_Stabilization.md`（補 diagnosis concept 交叉連結與來源邊界）。
  - `03_疾病與臨床主題/中風急性期處置與時間窗.md`（補 ICH diagnosis / expansion-risk concept 連結）。
  - `index.md`（新增 ICH diagnosis concept 與 source summary；Total pages 556 → 558）。
  - `log.md`
- 抽出概念：
  - Spontaneous ICH 診斷與病因分層：CT/MRI mandatory confirmation 後，以 hemorrhage location、volume、IVH / edema / herniation、CTA/MRI clues、labs 與 expansion-risk markers 判斷 etiology、severity 與 monitoring / follow-up imaging needs。
- 本輪直接事實：
  - Source 明確指出 clinical characteristics alone cannot distinguish brain hemorrhage and ischemia。
  - Source 明確指出 CT or MRI is mandatory to confirm ICH and exclude ischemic stroke / stroke mimics。
  - ICH injury includes hematoma expansion、perilesional edema and BBB-breakdown-related secondary injury。
  - Major risk factors include older age、hypertension and antithrombotic therapy。
  - Common etiologies include hypertensive vasculopathy、CAA and ruptured vascular malformation；其他包含 venous thrombosis、vasculopathy、tumor、coagulopathy 等。
  - Expansion predictors include shorter time from onset to initial imaging、ICH volume、antiplatelet/anticoagulant use and CTA spot sign。
  - ABC/2 可估算 ICH volume。
  - EEG reserved for seizures or encephalopathy not explained by ICH location/size。
- 發現衝突：
  - 與「頭痛嘔吐才是 ICH」衝突；source 指出 headache/vomiting 常見於 large ICH，但 headache may be absent。
  - 與「CT 只用來排除出血」衝突；source 支持 CT/MRI 同時提供 severity、expansion risk and underlying cause information。
  - 與「lobar ICH = CAA、deep ICH = hypertension」的過度簡化衝突；location 是 clue，不是 definitive diagnosis。
- 待追蹤問題：
  - Spontaneous ICH secondary prevention / long-term prognosis 尚未處理，不能由本 diagnosis source 外推。
  - 若要建立 CAA、AVM、RCVS、cerebral venous thrombosis 等獨立概念頁，需各自回到單一來源。

## [2026-05-05] ingest | Aneurysmal subarachnoid hemorrhage: Clinical manifestations and diagnosis

- 類型：UpToDate topic review（literature review current through 2026-04；topic last updated 2026-03-06）。
- 選擇原因：
  - hemorrhagic stroke cluster 中 ICH treatment / diagnosis 已完成；`Aneurysmal subarachnoid hemorrhage_ Clinical manifestations and diagnosis.md` 是下一篇尚未處理且與急性 hemorrhagic stroke triage 最相關的來源。
  - SAH treatment/prognosis 應在 diagnosis source 之後處理，避免先寫 treatment 而缺少 diagnostic gate。
- 本輪單一來源：
  - `C:\原始資料\Aneurysmal subarachnoid hemorrhage_ Clinical manifestations and diagnosis.md`
  - 只讀取此一篇來源；未混入 aneurysmal SAH treatment/prognosis、unruptured aneurysm、nonaneurysmal SAH 或其他 raw source。
- 新增來源摘要：
  - `09_來源摘要/UpToDate_aneurysmal_SAH_clinical_manifestations_diagnosis.md`
- 新增頁面：
  - `03_疾病與臨床主題/Aneurysmal_SAH_臨床表現與診斷分流.md`
- 更新頁面：
  - `03_疾病與臨床主題/中風急性期處置與時間窗.md`（新增 SAH diagnostic trigger、CT / LP / angiography 分流與來源連結）。
  - `index.md`（新增 SAH diagnosis concept 與 source summary；Total pages 558 → 560）。
  - `log.md`
- 抽出概念：
  - Aneurysmal SAH 臨床表現與診斷分流：sudden or rapid onset severe headache 啟動 SAH evaluation；noncontrast CT first；CT negative 但 suspicion persist 時多數仍需 LP；confirmed SAH 後用 CTA / DSA 找 bleeding source。
- 本輪直接事實：
  - Source 指出 thunderclap headache / sudden-onset severe headache 應評估 SAH。
  - 即使 alert and neurologically intact，也需 immediate evaluation beginning with head CT。
  - Noncontrast head CT 是 SAH diagnosis cornerstone；within 24 hours 可揭露 >90% cases。
  - Normal CT 後若仍高度懷疑 SAH，多數需 lumbar puncture；只有 selected early optimal CT-negative patient 可例外。
  - LP classic findings 包含 elevated opening pressure、CSF RBC 不由 tube 1 到 tube 4 明顯下降、xanthochromia。
  - Confirmed SAH 後需 vascular imaging；DSA resolution 最高且為 gold standard，CTA 越來越常作 first-line vascular test。
  - Initial angiography negative 時，除 selected perimesencephalic pattern 外，多數需 repeat angiography。
- 發現衝突：
  - 與「SAH 一定看起來很病重」衝突；source 指出 substantial proportion 可 awake, alert, neurologically intact。
  - 與「CT negative 就排除 SAH」衝突；source 支持 CT-negative 但 suspicion persist 時多數仍需 LP。
  - 與「CTA 可無條件取代 LP」衝突；source 偏好 standard CT→LP pathway，CTA 主要用於 CT/CSF positive 後找 symptomatic aneurysm。
- 待追蹤問題：
  - `Aneurysmal subarachnoid hemorrhage_ Treatment and prognosis.md` 應作為下一個 SAH treatment/prognosis 單一來源候選。
  - Nonaneurysmal SAH / perimesencephalic SAH 若需獨立頁，需另查單一來源。

## [2026-05-05] correction | Oliveira et al. 2024 polarized training meta-analysis

- 修正原因：使用者要求跑一次完整 exercise physiology literature workflow；掃描後發現本地 exercise physiology / CPET / runner exercise-medicine 來源多已完成來源摘要，因此改採單一來源 correction/update，避免建立重複頁。
- 重新檢查來源：
  - `C:\原始資料\Polarized vs. Other Training Intensity Distribution Regimens and Endurance Performance\Polarized vs. Other Training Intensity Distribution Regimens and Endurance Performance.md`
  - 本輪只讀取此一篇來源；未混入 Furrer、Poole、CP / W'、running injury 或其他 raw source。
- 修正頁面：
  - `09_來源摘要/Oliveira_2024_polarized_training_meta_analysis.md`
  - `05_Exercise_Physiology/Polarized_Training_證據邊界.md`
  - `05_Exercise_Physiology/Training_Intensity_Distribution.md`
  - `index.md`
- 補強內容：
  - highly trained / national-level subgroup 與 shorter intervention duration 可能交纏，不能獨立解讀成高訓練者必然更適合 POL。
  - 多篇研究未完整揭露實際 `%TID`、weekly TRIMP、volume、intensity、frequency；TID label 不能取代 training load 檢查。
  - TT outcome 涵蓋 100 m 到 40 km，生理需求異質；null finding 只能說本 meta-analysis 未顯示 POL superiority。
  - sex reporting 不足，female athlete / sex-specific response 仍不確定。
- 移除或降級的陳述：
  - 未移除頁面；將「highly trained / national-level athletes 中 POL 較有利」降級為受 intervention duration confounding 限制的 subgroup finding。
- 仍不確定之處：
  - POL 在完整 competitive season、injury risk、overreaching、recovery burden、clinical rehabilitation populations 的效應仍需另查單一來源。
- 待處理來源：
  - 若要補 clinical rehabilitation TID，需另找 cardiac / pulmonary / frailty population 的 guideline 或 systematic review。

## [2026-05-05] concept extraction | Francescato & Cettolo 2021 VO2 fitting window

- 修正原因：使用者要求再跑一次完整 exercise physiology literature workflow；掃描 `C:\原始資料` 後，未找到尚未進 wiki 的純 exercise physiology 主文，故改以既有單一來源摘要拆出尚未獨立成頁的單一方法學概念。
- 本輪單一來源：
  - `C:\原始資料\francescato-cettolo-2021-influence-of-the-fitting-window-on-the-o2-uptake-kinetics-at-the-onset-of-moderate-intensity\influence of the fitting window on the o2 uptake kinetics at the onset of moderate intensity.md`
  - 只使用此一篇來源與既有來源摘要；未混入 Zacca、Goulding 等其他 VO2 kinetics sources 作綜合。
- 來源摘要：
  - `09_來源摘要/Francescato_Cettolo_2021_VO2_fitting_window.md` 已存在；本輪未重建摘要，只更新 related page 連結。
- 新增頁面：
  - `04_CPET/VO2_Kinetics_Fitting_Window.md`
- 更新頁面：
  - `04_CPET/VO2_Kinetics.md`（補 fitting window 作為 model assumption 的交叉連結）。
  - `09_來源摘要/Francescato_Cettolo_2021_VO2_fitting_window.md`（補新概念頁連結）。
  - `index.md`（新增 concept；Total pages 560 → 561）。
  - `log.md`
- 抽出概念：
  - VO2 kinetics fitting window：在 moderate-intensity breath-by-breath VO2 onset data 中，phase 1 / 起始資料移除長度會改變 monoexponential `tau` 估計；fitting window 是 model assumption，不是中性背景設定。
- 本輪直接事實：
  - Source 分析 25 位 healthy adults 的 moderate-intensity step exercise VO2 data 與 `10^4` simulated biexponential responses。
  - 每條 response 以 monoexponential model 重複 fitting 61 次，`Delta Tr` 從 0 到 60 秒逐秒增加。
  - `tau` 的 minimum 大約出現在 `Delta Tr ~= 35 s`，約比 `Delta Tr ~= 0 s` 低 30%。
  - ASE 在 `Delta Tr ~= 35 s` 前相對穩定，超過後明顯惡化。
  - simulated data 中 `20 s-w` method 的 `tau` coverage 約 85%；`Mixed` method 約 92%。
- 發現衝突：
  - 與「固定移除前 20 秒就是中性慣例」衝突；本來源顯示 fitting window 可使 `tau` 產生實質差異。
  - 與「選最短 tau 就是最佳」衝突；來源顯示移除過長會讓 precision 惡化。
- 待追蹤問題：
  - heavy / severe domain 的 fitting window 是否可沿用本來源結果，需另查單一來源。
  - patient cohorts、off-transient recovery、binning / outlier removal / ensemble averaging 與 fitting window 的交互作用仍未處理。

## [2026-05-05] ingest | Aneurysmal subarachnoid hemorrhage: Treatment and prognosis

- 類型：UpToDate topic review（literature review current through 2026-04；topic last updated 2025-06-30）。
- 選擇原因：
  - 前一輪 SAH diagnosis ingest 明確留下 `Aneurysmal subarachnoid hemorrhage_ Treatment and prognosis.md` 作為下一個 treatment/prognosis source。
  - 既有 `Aneurysmal_SAH_臨床表現與診斷分流.md` 只處理 diagnosis，急性治療、DCI / vasospasm、ICP / hydrocephalus 與 prognosis 尚未獨立成頁。
- 本輪單一來源：
  - `C:\原始資料\Aneurysmal subarachnoid hemorrhage_ Treatment and prognosis.md`
  - 只讀取此一篇來源；未混入 aneurysmal SAH diagnosis、unruptured aneurysm、nonaneurysmal SAH、ICH 或 ischemic stroke raw source。
- 新增來源摘要：
  - `09_來源摘要/UpToDate_aneurysmal_SAH_treatment_prognosis.md`
- 新增頁面：
  - `03_疾病與臨床主題/Aneurysmal_SAH_急性治療與預後管理.md`
- 更新頁面：
  - `03_疾病與臨床主題/Aneurysmal_SAH_臨床表現與診斷分流.md`（補 treatment/prognosis concept crosslink）。
  - `03_疾病與臨床主題/中風急性期處置與時間窗.md`（補 SAH treatment frame、aneurysm repair、nimodipine、DCI / vasospasm、ICP / hydrocephalus 與不要做的事）。
  - `index.md`（新增 SAH treatment concept 與 source summary；Total pages 561 → 563）。
  - `log.md`
- 抽出概念：
  - Aneurysmal SAH 急性治療與預後管理：ruptured aneurysm SAH 後以 stabilization、antithrombotic reversal、BP control without hypotension、euvolemia、nimodipine、early clipping/coiling、DCI / vasospasm monitoring、ICP / hydrocephalus management 與 long-term morbidity surveillance 串成 neurocritical workflow。
- 本輪直接事實：
  - Source 指出 aneurysmal SAH patients 應在 intensive care setting 接受 hemodynamic、cardiac and neurologic monitoring。
  - Source 指出所有 antithrombotic agents 應停用，所有 anticoagulation 應 reversal until aneurysm is repaired。
  - Source 對 most acute SAH patients 使用 SBP <160 mmHg or MAP <110 mmHg，同時避免 hypotension。
  - Source 指出 hypovolemia 是 ischemic complication risk factor，目標是 euvolemia。
  - Nimodipine 60 mg every four hours orally / NG for 21 days 是 standard of care；source 指出 outcome benefit established，但 vasospasm incidence reduction 不明確。
  - Surgical clipping 或 endovascular coiling 是 prevention of rebleeding 的唯一有效治療，應 as early as feasible，preferably within 24 hours。
  - Rebleeding risk 在 first 24 hours 為 4-14%，maximal risk 在 first 2-12 hours；rebleeding mortality 可高達 70%。
  - DCI occurs in approximately 30%；vasospasm 通常 days 4-14，days 7-8 peak。
  - Aggressive vasospasm treatment 只應在 aneurysm 已 clipping/coiling 後進行；first-line 是 stepwise hemodynamic augmentation。
  - Hypervolemia / triple-H 不應 routine 用於 DCI prevention or treatment。
  - Hydrocephalus affects 20-30%；意識惡化合併 elevated ICP / hydrocephalus 時需 urgent CSF diversion。
  - 30-day mortality approaches 30%；long-term complications 包含 neurocognitive dysfunction、epilepsy、focal deficits、mood/sleep disorders、aneurysm recurrence and late rebleeding。
- 發現衝突：
  - 與「nimodipine = 已證實防 vasospasm」衝突；source 支持 outcome benefit，但不支持 vasospasm incidence 必然下降。
  - 與「tranexamic acid 可 routine 防 rebleeding」衝突；source 不支持 routine antifibrinolytics because poor outcome benefit 未建立。
  - 與「triple-H 是 SAH vasospasm 標準」衝突；source 不 routine prophylactic hemodynamic augmentation，也不 routine hypervolemia。
  - 與「aneurysm secured 前後 vasospasm treatment 一樣」衝突；source 指出 aggressive vasospasm therapy belongs after aneurysm occlusion。
- 待追蹤問題：
  - 若要把 aneurysmal SAH treatment 升級為 guideline-grade page，需另行單一來源 ingest 2023 AHA/ASA aneurysmal SAH guideline 原文。
  - `中風併發症總覽` 可後續補一段 SAH-specific DCI / hydrocephalus / hyponatremia / cardiac complication crosslink。
  - SAH long-term rehabilitation outcome、return to work、cognition / mood / sleep surveillance 需要另查 rehabilitation-focused source。

## [2026-05-06] ingest | Poststroke neuropsychiatric disorders and symptoms

- 類型：UpToDate topic review（literature review current through 2026-04；topic last updated 2025-11-24）。
- 選擇原因：
  - `C:\原始資料\Poststroke neuropsychiatric disorders and symptoms.md` 尚無獨立 `09_來源摘要`。
  - 既有 stroke cluster 已處理 acute stroke、ICH、SAH、aphasia 與 complications；poststroke psychiatric / neurobehavioral surveillance 仍停留在 depression 單點，尚未整理 apathy、anxiety / PTSD、PBA、anger/aggression 與 referral threshold。
- 本輪單一來源：
  - `C:\原始資料\Poststroke neuropsychiatric disorders and symptoms.md`
  - 只讀取此一篇來源；未混入 TMS、vascular cognitive impairment、neuropalliative care、dysphagia 或其他 raw source。
- 新增來源摘要：
  - `09_來源摘要/Poststroke_neuropsychiatric_disorders_and_symptoms.md`
- 新增頁面：
  - `03_疾病與臨床主題/Poststroke_Neuropsychiatric_Disorders_辨識與轉介.md`
- 更新頁面：
  - `03_疾病與臨床主題/中風併發症總覽.md`（補 neuropsychiatric complications as rehab readiness domain）。
  - `03_疾病與臨床主題/中風復健總論.md`（補 depression 以外的 neuropsychiatric surveillance 與 therapy engagement differential）。
  - `03_疾病與臨床主題/Delirium_Depression_Dementia_鑑別.md`（補 poststroke context：問卷分數重疊、acute aggression 先想 delirium）。
  - `index.md`（新增 poststroke neuropsychiatric concept 與 source summary；Total pages 563 → 565）。
  - `log.md`
- 抽出概念：
  - Poststroke neuropsychiatric disorders 辨識與轉介：stroke recovery 中以 functional impairment、safety risk、suicidality、psychosis、dangerous/aggressive behavior、PBA vs depression、apathy vs depression / poor motivation 作為 surveillance 與 referral framework。
- 本輪直接事實：
  - Source 指出 poststroke psychiatric disorders common but under-recognized。
  - Psychiatric symptoms causing functional impairment warrant mental health evaluation。
  - Referral indications include lack of response to initial treatment、suicidal ideation or behavior、psychotic features、impulsive/dangerous/aggressive behavior、adjunctive psychotherapy need、poor judgment with imminent risk and patient interest。
  - Depression is the most common poststroke neuropsychiatric disorder；reported prevalence approximately 25-50 percent across studies。
  - PHQ-2 / PHQ-9 are commonly used for non-aphasic poststroke patients；PHQ-2 >= 3 should lead to PHQ-9 evaluation；ADRS is validated for aphasic patients by behavioral observation。
  - Apathy is reduction or loss of motivation、initiation or goal-directed activity；it can coexist with depression but is not equivalent；no proven therapy exists in the source。
  - Poststroke anxiety can affect approximately 25-33 percent of stroke/TIA patients；GAD-7、GAI、HADS can assist screening with caveats。
  - PTSD is diagnosed only if symptoms persist beyond one month；source cites 2024 systematic review prevalence 17.5 percent after stroke, higher in SAH than ischemic stroke survivors。
  - PBA involves involuntary or inappropriate laughing/crying with affect-mood incongruence；source cites 17 percent prevalence after stroke。
  - PSAA has been reported in 11-35 percent of acute/subacute stroke patients；acute/subacute aggression may be delirium-related。
- 發現衝突：
  - 與「therapy participation 下降 = motivation poor」衝突；source 支持 depression、apathy、anxiety/PTSD、PBA、delirium、pain、sleep、communication/cognition differential。
  - 與「poststroke crying = depression」衝突；source 明確區分 PBA 與 depression。
  - 與「問卷總分可直接診斷 depression/anxiety」衝突；source 指出 stroke sequelae 可拉高 total score，需 item-level review 與 clinical judgment。
  - 與「所有 acute stroke 都應 routine prophylactic SSRI」衝突；source 只支持 selected use and not standard care，且提醒 bleeding / fracture concerns。
- 待追蹤問題：
  - 若要建立 poststroke depression treatment 的 guideline-grade page，需另行單一來源 ingest AHA/ASA poststroke depression scientific statement 或 psychiatry guideline。
  - PBA、poststroke apathy、poststroke anxiety/PTSD、PSAA 可後續視需求各自拆成單一概念頁。
  - `Unipolar depression in adults_ Indications, efficacy, and safety of transcranial magnetic stimulation (TMS...).md` 可作 poststroke depression neuromodulation 的後續候選，但不得與本來源混寫。

## [2026-05-06] ingest | Neuropalliative care of stroke

- 類型：UpToDate topic review（literature review current through 2026-04；topic last updated 2026-04-15）。
- 選擇原因：
  - `C:\原始資料\Neuropalliative care of stroke.md` 尚無獨立 `09_來源摘要`。
  - 近期 stroke cluster 已處理 acute stroke、ICH、SAH、complications 與 poststroke neuropsychiatric surveillance；但 severe stroke 的 goals-of-care、prognostic uncertainty、caregiver support、time-limited trials 與 palliative-hospice distinction 尚未獨立整理。
- 本輪單一來源：
  - `C:\原始資料\Neuropalliative care of stroke.md`
  - 只讀取此一篇來源；未混入 TMS、vascular cognitive impairment、dysphagia topic、AHA statement 或 CMS 原文。
- 新增來源摘要：
  - `09_來源摘要/Neuropalliative_care_of_stroke.md`
- 新增頁面：
  - `03_疾病與臨床主題/Stroke_Neuropalliative_Care與Goals_of_Care.md`
- 更新頁面：
  - `03_疾病與臨床主題/中風復健總論.md`（補 palliative care 可與 acute/rehab 並行、time-limited trial 與 goals-of-care trigger）。
  - `03_疾病與臨床主題/中風併發症總覽.md`（補 palliative/caregiver needs as complication workflow）。
  - `03_疾病與臨床主題/Spontaneous_ICH_急性抗擴大與Neurocritical_Stabilization.md`（補 severe ICH prognosis communication 與 palliative care 並行）。
  - `03_疾病與臨床主題/Aneurysmal_SAH_急性治療與預後管理.md`（補 severe SAH goals-of-care handoff 與 palliative care distinction）。
  - `index.md`（新增 neuropalliative concept 與 source summary；Total pages 565 → 567）。
  - `log.md`
- 抽出概念：
  - Stroke neuropalliative care 與 goals of care：palliative care 可在 stroke presentation 開始且與 acute treatment 並行；核心是 symptom management、functional status、goals of care、advance care planning、shared decision-making、prognostic uncertainty、time-limited trials and caregiver support。
- 本輪直接事實：
  - Source defines neuropalliative care as optimizing symptom management and functional status、addressing goals of care、advance care planning and shared decision-making。
  - Source distinguishes palliative care from hospice；hospice applies when patient is nearing end of life。
  - Source states palliative care can begin at stroke presentation and can be offered concurrently with acute treatment。
  - Primary palliative care is provided by the stroke team；specialist palliative care is provided by multidisciplinary palliative specialists。
  - Serious illness conversation triggers include age 80 or older and hospitalized、patient/family/caregiver request、positive surprise question、mechanical ventilation、predicted major functional/cognitive dependency and long-term artificial nutrition。
  - Source states most patients presenting with stroke do not have applicable advance directives。
  - Source states many severe stroke patients lack decision capacity early and families must use substituted judgment。
  - Source cites 2024 neurocritical care guidance recommending avoidance of premature prognostication after severe stroke。
  - Source states time-limited trials can reduce uncertainty but require a clear follow-up strategy。
  - Dysphagia affects more than 50 percent of acute stroke patients in the source；about 50 percent recover within two weeks and about 15 percent have persistent dysphagia at one month。
- 發現衝突：
  - 與「palliative care = hospice / withdraw treatment」衝突；source 明確支持可與 acute treatment 並行。
  - 與「goals of care = code status」衝突；source 強調 values、treatment goals and shared decision-making。
  - 與「prognostic score 可直接決定撤治療」衝突；source 指出 model should not be primary source for end-of-life decisions。
  - 與「PEG 是單純出院行政需求」衝突；source 把 long-term artificial nutrition 放入 serious illness conversation triggers。
- 待追蹤問題：
  - 若要做 guideline-grade stroke palliative page，需另行單一來源 ingest 2025 AHA scientific statement 或 AAN position statement。
  - Hospice eligibility / CMS criteria 若要實務化，需另行單一來源處理政策原文，不能只靠本 UpToDate 摘要。
  - Poststroke pain 與 dysphagia feeding-tube decision 可後續各自拆成單一概念頁。

## [2026-05-06] correction | Lievens et al. 2024 — Characterizing the Exponential Profile of W' Recovery Following Partial Depletion

- 修正原因：
  - 使用者要求繼續 ingest 一篇運動生理來源。
  - 運動生理 raw candidates 多數已在舊 batch ingest 中登錄；本輪選擇較新的 W' partial depletion recovery 來源，依單一來源 workflow 重建摘要並拆出單一概念頁。
- 本輪單一來源：
  - `C:\原始資料\characterizing_the_exponential_profile_of_w_.24\characterizing_the_exponential_profile_of_w_.24.md`
  - 只完整處理此一篇來源；未混入 Caen 2021、Chorley 2021、Skiba 2014、Bartram 2018 或其他 W' recovery raw source。
- 重新建立來源摘要：
  - `09_來源摘要/Lievens_2024_partial_Wprime_recovery.md`
- 新增頁面：
  - `04_CPET/Partial_Wprime_Depletion_Recovery.md`
- 更新頁面：
  - `04_CPET/Wprime_Recovery.md`（補 partial depletion 專頁連結與 full exhaustion 外推限制）。
  - `04_CPET/Wprime_Balance_Model.md`（補 Lievens 2024 對 W'BAL model family 的限制）。
  - `04_CPET/CP_Wprime_Interval_Design.md`（補 interval prescription 不應用 fixed tau 或 exhaustion model 一體套用）。
  - `index.md`（新增 partial W' depletion recovery concept；Total pages 567 → 568）。
  - `log.md`
- 抽出概念：
  - Partial W' depletion recovery：W' 尚未完全耗盡時，後續 work capacity above CP 的 recovery kinetics；不能直接等同於 full exhaustion 後 W' reconstitution，也不能用單一 fixed tau 跨 depletion state 泛用。
- 本輪直接事實：
  - Source 為 2024 original research article，n = 9 healthy young men。
  - Experimental design 使用 25% 與 75% 理論 W' depletion，recovery durations 為 30、60、120、300、600 秒，recovery intensity 固定在 90% GET。
  - W'OBS 以 WB2 to exhaustion operationally estimated。
  - Biexponential fits 的 RMSE 較低，但 free amplitude models 的 AICc favor monoexponential；fixed amplitude models 中 DEP25% favor monoexponential、DEP75% favor biexponential。
  - DEP25% 與 DEP75% 的 mean W'OBS 高度相關（r = 0.92）。
  - W'OBS 與 VO2peak、CP、GET 呈正相關（r = 0.67-0.77）。
  - 既有 Skiba-1、Skiba-2、Bartram models 未能準確描述本研究 temporal W' recovery profile。
  - DEP25% 後 W'OBS 可超過理論 100%，作者以 WB2 aerobic priming / higher relative aerobic contribution 解釋。
  - DEP75% 後 model fit plateau 約 83%，提示 large depletion 可能妨礙後續 high-intensity capacity 完全恢復。
  - Perceived W' recovery 平均比 W'OBS 低約 25%，代表主觀疲勞與 model-derived work capacity recovery 可能脫鉤。
- 發現衝突：
  - 與「full exhaustion 後 two-phase W' recovery 可直接套到 all interval recovery」衝突；source 限制此一外推。
  - 與「固定 universal tau 足以描述不同 depletion state」衝突；source 支持 individualized / dynamic tau direction。
  - 與「W'BAL 是真實剩餘 anaerobic tank」衝突；source 顯示 W'OBS 受 aerobic priming、model assumptions 與 subjective fatigue mismatch 影響。
- 待追蹤問題：
  - 需要 women、elite athlete、older adults 與 cardiopulmonary disease / rehabilitation populations 的 partial depletion data。
  - 需要不同 recovery power 條件下的 monoexponential vs biexponential model comparison。
  - 後續可挑一篇 W'BAL model methodology source 做單一來源 correction，以清理舊 batch 形成的 model-form 混用風險。

## [2026-05-07] correction | Skiba & Clarke — The W' Balance Model: Mathematical and Methodological Considerations

- 修正原因：
  - 前一輪 `Lievens_2024_partial_Wprime_recovery` 指出後續應處理 W'BAL model methodology source，以清理舊 batch 形成的 model-form 混用風險。
  - 本來源曾在 2026-04-25 batch ingest 中建立摘要；本輪依單一來源 workflow 重新檢查並改寫成正式 source summary。
- 本輪單一來源：
  - `C:\原始資料\Mathematics of W'BAL\Mathematics of W'BAL.md`
  - 只完整處理此一篇來源；未混入 Caen、Bartram、Sreedhara、Lievens 或其他 W' recovery raw source。
  - 舊 batch 曾登錄 duplicate raw file `C:\原始資料\ijspp-article-p1561 (1)\ijspp-article-p1561 (1).md`；本輪不新增第二份摘要。
- 重新建立來源摘要：
  - `09_來源摘要/Skiba_Clarke_Wprime_balance_model.md`
- 更新頁面：
  - `04_CPET/Wprime_Balance_Model.md`（補 INT / ODE model-form 假設、input uncertainty、extreme-case caveat 與 field-use 解讀）。
  - `index.md`（更新日期與 Skiba & Clarke source summary 描述；Total pages 維持 568）。
  - `log.md`
- 抽出概念：
  - W'BAL model-form interpretation：W'BAL 是 intermittent severe-domain exercise 的 assumption-sensitive model family；INT 與 ODE 不是可互換版本，且 `W'BAL = 0 J` 應視為 exhaustion-risk zone 而不是精確生理瞬間。
- 本輪直接事實：
  - Source 為 2021 narrative / methodologic review article，討論 W'BAL theoretical basis、assumptions、calculation methods、strengths、limitations and future directions。
  - W'BAL-INT 是 convolution-style model；其關鍵假設是 expended W' 可隨時間 exponential reconstitution，甚至可在 macroscopic depletion 時存在 microscopic recovery。
  - Source 指出原始 INT equation 曾有 dimensional ambiguity，需明確寫成 convolution integral。
  - Source 指出 INT best practice 需依 athlete 與 exercise mode 估 individualized `tau-W'`。
  - INT 在 extreme simulations 可出現不合理行為，例如 continuous severe trial 下比 two-parameter CP model 更晚 exhaustion，或 exhaustion 後在 CP 立即出現 recovery。
  - W'BAL-ODE 假設 depletion 與 recovery 互斥；power > CP 時 depletion，power < CP 時 recovery。
  - ODE recovery rate 取決於 depleted W' fraction 與 `CP - P`；計算較直接且不需另行 fitting `tau-W'`。
  - Source 的 Ferguson data example 中 ODE implied `tau-W'` 約 112 秒，而 simple exponential fit 約 336 秒。
  - Source 的 interval example 中 ODE 可比 INT 早約 300 秒預測 exhaustion。
  - Source 報告 W' typical error 約 7-20%，且一項 cited report 約 46%；因此 `W'BAL = 0 J` 不應當成 exact exhaustion point。
  - Source 指出 CP / W' 在 within-session 與 between-session 被當成 constant 的假設可能不成立，nutrition、altitude and prior exercise 都可影響。
  - Source 討論 KODE / multicomponent direction，但將其定位為未成熟研究方向，而非已定型實務模型。
- 發現衝突：
  - 與「W'BAL 是真實剩餘 anaerobic tank」衝突；source 支持 model-based estimate。
  - 與「INT / ODE 只是同一模型的不同計算法」衝突；source 明確區分兩者對 recovery / depletion 的 assumptions。
  - 與「更高 goodness-of-fit 即代表更真實 physiology」衝突；source 強調 mathematical fit、physiological realism and field usability 之間有 trade-off。
- 待追蹤問題：
  - 若要實作 W'BAL calculator，需另開工程頁明確選擇 INT、ODE 或其他 model form，並列出 input uncertainty。
  - 若要討論 multicomponent W' recovery，需另行單一來源處理 Caen 2021 或相關原始研究，不可只靠本 review 的二手整理。
  - `Wprime_Balance_Model.md` 仍整合多來源；後續若頁面過長，可拆出 `Wprime_BAL_INT_vs_ODE.md` 作單一概念頁。

## [2026-05-07] correction | Caen et al. 2021 - W' Recovery Kinetics after Exhaustion

- 修正原因：
  - 前一輪 `Skiba_Clarke_Wprime_balance_model` 指出 multicomponent / two-component W' recovery 不可只靠 model review 二手整理。
  - `Caen_2021_Wprime_recovery_two_phase.md` 已存在但屬舊 batch ingest 格式；本輪依單一來源 workflow 重讀原文並重建正式 source summary。
- 本輪單一來源：
  - `C:\原始資料\w__recovery_kinetics_after_exhaustion__a_two_phase\w__recovery_kinetics_after_exhaustion__a_two_phase.md`
  - 只完整處理此一篇來源；未混入 Ferguson 2010、Skiba 2015、Chorley 2021、Lievens 2024、Caen 2019 或其他 W' recovery raw source。
- 重新建立來源摘要：
  - `09_來源摘要/Caen_2021_Wprime_recovery_two_phase.md`
- 新增頁面：
  - `04_CPET/Exhaustion_Based_Two_Phase_Wprime_Recovery.md`
- 更新頁面：
  - `04_CPET/Wprime_Recovery.md`（將 Caen 2021 exhaustion two-phase 內容連到單一概念頁，補 `W'ADJ` 與 changed `VO2` kinetics 限制）。
  - `04_CPET/Wprime_Balance_Model.md`（補 complete-exhaustion two-phase 不是單一 anaerobic tank refill）。
  - `04_CPET/CP_Wprime_Interval_Design.md`（補 exhaustion-based model 不等於 partial-depletion interval model）。
  - `04_CPET/Partial_Wprime_Depletion_Recovery.md`（加入對照連結）。
  - `index.md`（新增 concept page；Total pages 568 → 569；更新 Caen 2021 source summary 描述）。
  - `log.md`
- 抽出概念：
  - Exhaustion-based two-phase W' recovery：complete severe-domain exhaustion 後，`W'OBS` recovery 可呈 fast initial phase 與 slower second phase；但這是 complete-exhaustion cycling protocol 的 operational finding，不可直接當成所有 interval recovery 的通用模型。
- 本輪直接事實：
  - Source 為 2021 original research article，n = 21 physically active young men。
  - Protocol 先估 `CP` 與 `W'`，再做兩個相同 exhaustive work bouts，中間 recovery durations 為 30、60、120、180、240、300、600、900 秒。
  - Recovery power 固定為 90% `GET`。
  - `W'OBS` 以 WB2 TTE / WB1 TTE operationally 估計，假設 WB1 結束時 `W' = 0`。
  - Standard `W'BAL` model 的 `tau` 為 524 ± 41 秒，對 `W'OBS` fitting RMSE 為 18.6%。
  - `W'BAL` 在 30 秒到 5 分鐘 recovery 條件下低估 `W'OBS`。
  - Monoexponential fitting of `W'OBS`：`tau` 約 104 秒，RMSE 6.4%。
  - Biexponential fitting of `W'OBS`：`tau1` 約 11 秒、`tau2` 約 256 秒，RMSE 1.7%；AICc 支持 biexponential。
  - `W'ADJ` 平均比 `W'OBS` 低 11.0% ± 1.5%，代表 changed `VO2` kinetics / reduced `O2` deficit 解釋部分短休息恢復。
  - `W'ADJ` 的 AICc 不再支持 biexponential 優於 monoexponential。
  - `VO2peak` 與 `W'OBS` recovery 正相關；MFT distribution 在主要分析中不是 significant predictor。
- 發現衝突：
  - 與「W' recovery 可用單一 universal tau 完整描述」衝突；source 支持 complete-exhaustion `W'OBS` two-phase behavior。
  - 與「fast phase = anaerobic tank 快速補滿」衝突；source 顯示 enhanced aerobic contribution 解釋部分 short-rest recovery。
  - 與「W' recovery = VO2 / PCr recovery」衝突；source 顯示 `VO2` recovery 多數時間快於 `W'OBS`，W'OBS 仍是 whole-system construct。
  - 與「complete-exhaustion model 可直接套到 partial depletion」衝突；source 明確指出 partial depletion 可能不會產生同樣 steep fast phase。
- 待追蹤問題：
  - 若要清理 W' recovery 舊 batch 來源，可下一輪 correction `Ferguson_2010_Wprime_recovery_after_exhaustion` 或 `Skiba_2015_intramuscular_determinants_Wprime_recovery`。
  - 若要處理 partial-depletion vs exhaustion synthesis，需先完成各來源獨立 correction，再另開 synthesis 頁。
  - `Wprime_Recovery.md` 仍是多來源 hub；若繼續增長，應拆出 `Wprime_Recovery_Model_Comparison.md` 或 `Wprime_Recovery_Physiology.md`。

## [2026-05-08] correction | Beaver, Wasserman & Whipp 1986 - V-slope method

- 修正原因：
  - 使用者要求先以運動生理或 CPET 執行一次完整 workflow。
  - `Beaver_Wasserman_Whipp_1986_V_slope_method.md` 已存在，但屬舊 batch / 簡略格式；本輪依單一來源 workflow 重讀原文並重建正式 source summary。
- 本輪單一來源：
  - `C:\原始資料\beaver-et-al-1986-a-new-method-for-detecting-anaerobic-threshold-by-gas-exchange\beaver-et-al-1986-a-new-method-for-detecting-anaerobic-threshold-by-gas-exchange.md`
  - 只完整處理此一篇來源；未混入 Poole 2020、Stringer 1995、Yano 1997、Hirakoba 1996 或其他 GET / V̇CO2 sources。
- 重新建立來源摘要：
  - `09_來源摘要/Beaver_Wasserman_Whipp_1986_V_slope_method.md`
- 新增頁面：
  - `04_CPET/Respiratory_Compensation_Point.md`
- 更新頁面：
  - `04_CPET/V_Slope_Method.md`（補 Beaver 1986 protocol、data conditioning、two-segment regression、主要數據與 Fact / Inference / Assumption / Uncertainty 分層）。
  - `index.md`（新增 RCP concept；更新 V-slope 與 Beaver source summary 描述；Total pages 569 → 570）。
  - `log.md`
- 抽出概念：
  - V-slope method：incremental CPET 中以 V̇CO2-V̇O2 two-segment breakpoint 偵測 buffering-related excess CO2 output onset 的 gas-exchange method。
  - Respiratory compensation point：高於 GET/AT 的 ventilatory compensation breakpoint；在 Beaver 1986 中以 VE-V̇CO2 slope change 另行偵測，並作為 V-slope AT calculation 的 upper boundary。
- 本輪直接事實：
  - Source 為 1986 Journal of Applied Physiology original research article。
  - 研究對象為 10 位健康男性，19-39 歲。
  - Protocol 使用 cycle ergometer，4 分鐘 unloaded exercise 後以 15 W/min incremental exercise 至 tolerance。
  - Measurement 包含 breath-by-breath V̇O2、V̇CO2、VE、heart rate、PETCO2；另以 arterial catheter 於 rest、unloaded cycling 與 incremental exercise 每 2 分鐘採血分析 lactate / bicarbonate。
  - V-slope analysis 將 V̇CO2-V̇O2 curve 分成兩段 linear regression，以交點作 tentative AT。
  - Data conditioning 包含 regular time interpolation、minimal moving average filtering、PETCO2-related V̇CO2 fluctuation correction、排除 incremental phase 起始約 1 分鐘的 CO2-store distortion。
  - V-slope AT mean V̇O2 為 1.83 +/- 0.30 L/min；panel visual AT mean V̇O2 為 1.85 +/- 0.34 L/min，差異不顯著。
  - V-slope coefficient of variation 為 0.023 +/- 0.006；panel average coefficient of variation 為 0.127 +/- 0.080。
  - V-slope AT 對應 lactate 比 mathematically defined LT 高 0.50 +/- 0.34 meq/L。
  - V-slope AT mean V̇O2 1.83 +/- 0.30 L/min 與 estimated HCO3 threshold 1.78 +/- 0.24 L/min 無顯著差異。
  - RC point mean V̇O2 為 2.51 +/- 0.42 L/min，高於 V-slope AT。
- 發現衝突：
  - 與「anaerobic threshold = muscle dysoxia」衝突；本輪保留 Beaver 1986 operational GET / V-slope method，但不採納舊 dysoxia implication。
  - 與「VE-based threshold alone 足以等同 V-slope GET」衝突；source 指出 ventilation response may lag or obscure metabolic CO2 signal。
  - 與「RCP 可直接等同 GET 或 Critical Power」衝突；source 明確把 RC point 與 V-slope AT 分開，且本來源沒有支持 RCP = CP。
- 待追蹤問題：
  - `Respiratory_Compensation_Point.md` 目前只由 Beaver 1986 支持，後續需用 review / guideline 或 Poole 2020 類來源補齊 RCP、LT2、MLSS、CP/CS 的邊界。
  - `Gas_Exchange_Threshold.md` 仍是多來源 hub；若要進一步 correction，需另選單一來源處理，不能在本輪混寫。
  - 若要做 protocol-level V-slope calculator / reporting checklist，需另開方法頁整理 preprocessing、breakpoint criteria、signal quality 與 reporting minimum fields。

## [2026-05-08] ingest | Goulding et al. 2023 - Priming Exercise and VO2 Kinetics

- 修正原因：
  - 使用者要求自動建立 wiki 執行一次完整 workflow。
  - `C:\原始資料\s40279-023-01832-1\s40279-023-01832-1.md` 尚未在主 wiki 中建立來源摘要；同目錄 `nurturing care practice guide` 已於 2026-05-03 完成 ingest，故本輪不重複處理。
- 本輪單一來源：
  - `C:\原始資料\s40279-023-01832-1\s40279-023-01832-1.md`
  - 只完整處理此一篇來源；未混入 Goulding 2021、Goulding & Marwood 2023、Caen 2021、Skiba / W'BAL 或其他 VO2 kinetics / critical power 來源。
- 新增來源摘要：
  - `09_來源摘要/Goulding_2023_priming_exercise_VO2_kinetics.md`
- 新增頁面：
  - `04_CPET/Priming_Exercise_and_VO2_Kinetics.md`
- 更新頁面：
  - `04_CPET/VO2_Kinetics.md`（補 human priming exercise 的 phase-specific 判讀：`tauVO2`、fundamental amplitude、slow component 不可混成單一「變快」）。
  - `04_CPET/VO2_Slow_Component.md`（補 priming 後 slow component reduction 可能造成 overall kinetics 變快的誤讀風險）。
  - `04_CPET/CP_Wprime_Interval_Design.md`（補 priming performance effect 需以 CP / W' 與 recovery duration 解讀）。
  - `index.md`（新增 concept page 與 source summary；Total pages 569 → 571）。
  - `log.md`
- 抽出概念：
  - Priming exercise effect on VO2 kinetics：prior heavy / severe exercise 會改變後續 exercise onset 的 VO2 phase response；必須分清 `tauVO2` lowering、fundamental amplitude increase 與 `VO2 slow component` reduction。
- 本輪直接事實：
  - Source 為 2023 *Sports Medicine* review article，DOI `10.1007/s40279-023-01832-1`。
  - Priming 後 overall VO2 response 變快，不一定代表 fundamental phase `tauVO2` 降低。
  - 43-study retrospective synthesis 指出 non-primed `tauVO2 <= 25 s` 的 groups 常接近 line of identity；`tauVO2 > 25 s` 的 groups 較常在 bout 2 出現較低 `tauVO2`。
  - Healthy young active upright cycling 中，典型 priming effect 常是 increased fundamental amplitude + reduced slow component，而不一定是 `tauVO2` reduction。
  - Supine / prone exercise、healthy elderly、type 2 diabetes mellitus、heart failure 或 baseline slow kinetics 時，prior heavy exercise 較可能降低後續 `tauVO2`。
  - Residual lactic acidosis 與 increased muscle temperature alone 不是主要因果解釋。
  - Priming 常增加 O2 delivery，但 O2 delivery alone 不足以解釋主要 priming effect。
  - Altered motor unit recruitment 可解釋 fundamental amplitude increase 與 slow component reduction，但 surface EMG evidence 有方法限制。
  - Enhanced intracellular O2 utilization 是作者最支持的機制方向之一；PDH / substrate availability 與 mitochondrial calcium 仍有未定論。
  - Performance effect 取決於 prior exercise intensity、criterion exercise intensity、recovery duration 與兩者相對於 critical power 的位置。
  - 若 priming 降低 `tauVO2`，critical power 較可能增加；若 priming 主要增加 fundamental amplitude 並降低 slow component，`W'` 較可能增加。
- 發現衝突：
  - 與「priming exercise = lactate / acidosis facilitation」衝突；來源認為 lactic acidosis 不是 quantitatively large causal mechanism。
  - 與「warming muscle reproduces priming」衝突；human passive heating evidence 多數不支持相同 pulmonary VO2 kinetics response。
  - 與「O2 delivery alone explains faster kinetics」衝突；來源支持 O2 delivery contributes，但 intracellular utilization 與 motor unit recruitment 更能解釋主要現象。
  - 與「overall mean response time 變短 = tauVO2 變快」衝突；未拆 phase 時此判讀不成立。
  - 與「priming 一定提升 performance」衝突；source 指出 severe priming recovery 太短時可能有害。
- 待追蹤問題：
  - 若要做 priming exercise prescription，需另行整理 intensity、recovery duration、event duration 與 athlete phenotype，不能只靠本 review 的 hypothesis。
  - 若要處理 clinical populations，需另選 heart failure、type 2 diabetes、older adult 或 rehabilitation-specific source 做單一來源 ingest。
  - `VO2_Kinetics.md` 仍是多來源 hub；後續可視情況拆出 `VO2_Kinetics_Phase_Modeling.md` 或 `VO2_Kinetics_Clinical_Interpretation.md`。

## [2026-05-08] ingest | Currier et al. 2023 - Resistance training prescription for strength and hypertrophy

- 本輪單一來源：
  - `C:\原始資料\Resistance training prescription for muscle strength and hypertrophy in healthy adults  a systematic review and Bayesian network meta-analysis\Resistance training prescription for muscle strength and hypertrophy in healthy adults  a systematic review and Bayesian network meta-analysis.md`
  - 只完整處理此一篇來源；未混入 Maroto 2024 RIR special populations、Therapeutic exercise textbook chapter、WHO guideline 或 disease-specific rehab sources。
- 新增來源摘要：
  - `09_來源摘要/Currier_2023_resistance_training_strength_hypertrophy_NMA.md`
- 新增頁面：
  - `05_Exercise_Physiology/Resistance_Training_Load_Set_Frequency_for_Strength_Hypertrophy.md`
- 更新頁面：
  - `02_方法學/治療性運動處方.md`（補 healthy adults resistance training load / set / frequency 框架，並標示不可直接外推至 rehabilitation / chronic disease）。
  - `index.md`（新增 concept page 與 source summary；Total pages 571 → 573）。
  - `log.md`
- 抽出概念：
  - Resistance training load / set / frequency for strength and hypertrophy：healthy adults 中 supervised RTx 可用 load、sets 與 weekly frequency 編碼比較；higher load 更偏 strength optimization，multiple sets / volume 更偏 hypertrophy，但 top-ranked node 不等於唯一可用處方。
- 本輪直接事實：
  - Source 為 2023 *British Journal of Sports Medicine* systematic review + Bayesian network meta-analysis。
  - Search databases 包含 MEDLINE、Embase、Emcare、SPORTDiscus、CINAHL、Web of Science，搜尋至 2022-02-07。
  - Eligible trials 為 randomized trials，研究對象為 healthy adults ≥18 years old，且比較至少 2 個 predefined RTx / CTRL nodes。
  - Excluded populations 包含 athletes、military personnel、persons with comorbidities、injured persons、hospitalised / inpatient / outpatient / rehabilitation patients、long-term care residents、explicitly obese / overweight participants，以及 unsupervised RT。
  - RTx coding 使用 `XY#`：`H` ≥80% 1RM、`L` <80% 1RM；`M` multiset、`S` single set；`1/2/3` 代表 once weekly、twice weekly、至少 3 days/week。
  - Strength NMA included 178 studies, n=5097。
  - Hypertrophy NMA included 119 studies, n=3364。
  - Compared with CTRL，strength posterior SMD range 0.75-1.60，最大估計為 `HM3`。
  - Compared with CTRL，hypertrophy posterior SMD range 0.10-0.66，最大估計為 `HM2`。
  - Between-RTx comparisons 多數不排除 zero；source 報告 91% 的 between-RTx comparisons 其 95% CrI contained zero。
  - Strength top-three probabilities 最高為 `HM3`、`HM2`、`HM1`；hypertrophy top-three probabilities 最高為 `HM2`、`LM1`、`LM2`。
  - Network meta-regression 中 age、training status、proportion female、duration、volitional fatigue、relative weekly volume load、measurement tool / region、publication year 未顯示 obvious modifying effect。
  - Source 明確指出 various RTx 對 health outcomes 的效果 largely unknown。
- 發現衝突：
  - 與「healthy adult RTx ranking 可直接當成 rehabilitation patient prescription」衝突；source 明確排除 chronic disease、injury、rehabilitation 與多個高風險族群。
  - 與「最高排名處方就是唯一正確處方」衝突；多數 between-RTx comparisons credible interval 包含 zero，且 source 強調 preference / feasibility。
  - 與「hypertrophy 必須 high load 或 failure」衝突；source 中 multiple sets / volume 更符合 hypertrophy top ranking，volitional fatigue NMR 未改善 model fit。
  - 與「低負荷 RT 對 strength 沒有價值」衝突；source 支持 lower-load RT compared with no exercise 仍可增加 strength。
- 待追蹤問題：
  - 若要處理 special populations resistance training，需另以 Maroto 2024 或 disease-specific source 做單一來源 ingest / correction。
  - 若要建立 clinical rehabilitation resistance training progression protocol，需額外納入 contraindications、monitoring、pain / fatigue response、technique quality 與 disease-specific precautions。
  - 若要比較 failure、RIR、tempo、rest interval 或 periodization，需另選來源；Currier 2023 的 RTx nodes 未完整納入這些變數。

## [2026-05-08] ingest | Poole & Gaesser 2025 - Oxygen uptake slow component enigma

- 本輪單一來源：
  - `C:\原始資料\Experimental Physiology - 2024 - Poole - Oxygen uptake slow component  Enigma of the  excess  oxygen used during heavy and\Experimental Physiology - 2024 - Poole - Oxygen uptake slow component  Enigma of the  excess  oxygen used during heavy and.md`
  - 只完整處理此一篇來源；未混入 MacDougall 2025 原始研究、Gaesser & Poole 1996 review、Goulding 2021、Korzeniewski 2015 或其他 V̇O2SC / CP sources。
- 新增來源摘要：
  - `09_來源摘要/Poole_Gaesser_2025_VO2_slow_component_enigma.md`
- 更新頁面：
  - `04_CPET/VO2_Slow_Component.md`（補 expert Viewpoint 層級的概念邊界：V̇O2SC 主要來自 exercising muscle，但不應被壓成單一機制）。
  - `index.md`（新增 source summary；Total pages 573 → 574）。
  - `log.md`
- 抽出概念：
  - V̇O2 slow component as a multi-factor muscle efficiency problem：heavy / severe constant-load exercise 中 delayed excess V̇O2 多數來自 exercising muscle；fatigue、biomechanics、fiber contribution、coupling efficiency 與個體差異都可能參與，不宜用單一機制解釋。
- 本輪直接事實：
  - Source 為 *Experimental Physiology* peer-reviewed Viewpoint / expert commentary，citation year 2025，DOI `10.1113/EP092326`。
  - Source 區分 incremental exercise 的近似 linear V̇O2-work rate relation 與 heavy / severe constant-load exercise 的 delayed excess V̇O2。
  - Source 描述 V̇O2SC 通常在 fast kinetics 後、約 2-3 分鐘後變明顯。
  - Heavy exercise 中 V̇O2SC 可在後續穩定；severe exercise 中可把 V̇O2 推向 V̇O2max 並接近 exhaustion。
  - Source 指出極端情況下 V̇O2SC 可達約 1-1.5 L O2/min，侵蝕 muscle efficiency。
  - Source 回顧早期候選原因包含 ventilation、body temperature、blood lactate、catecholamines，但認為以 estimated O2 cost 或 temporal correlation 判斷因果都不足。
  - Source 指出 simultaneous leg muscle V̇O2 與 pulmonary V̇O2 量測曾支持 exercising muscles 佔 V̇O2SC majority，報告為 >80%。
  - Source 將剩餘候選機制列為 fatiguing muscle fibres、additional less efficient fibre recruitment、decreased mitochondrial P:O ratio、less efficient chemical-mechanical coupling。
  - Source 指出 decreased P:O ratio 作為主因似乎 unlikely，且 dog / human evidence 顯示 additional muscle fibre recruitment 不是 V̇O2SC 必要條件。
  - Source 討論 MacDougall et al. 2025：constant external power 下，cycling biomechanics indices 與 quadriceps fatigue 可隨 V̇O2SC 發展而改變。
  - Source 強調 interindividual variability，並反對以單一 driver 解釋所有 V̇O2SC。
- 發現衝突：
  - 與「V̇O2SC 主要是 ventilation / temperature / lactate / catecholamine」衝突；source 支持 exercising muscle 為主要來源。
  - 與「type II fibre recruitment alone explains V̇O2SC」衝突；source 認為 additional fibre recruitment 不一定是必要條件。
  - 與「constant watts = constant muscle input」衝突；source 強調 biomechanics 與 fatigue state 可能改變。
  - 與「找到單一機制就能解釋所有 V̇O2SC」衝突；source 強調 multiple factors and individual variability。
- 待追蹤問題：
  - 若要寫入 MacDougall 2025 的 fatigue / biomechanics 原始資料，需另行單一來源 ingest；本輪只處理 Poole & Gaesser Viewpoint 的二手討論。
  - `VO2_Slow_Component.md` 已是多來源 hub；若後續繼續增長，應拆出 `VO2_Slow_Component_Mechanisms.md` 或 `VO2_Slow_Component_Methodology.md`。
  - 若要討論 HF / COPD 中 V̇O2SC 的臨床影響，需另選 clinical CPET / disease-specific source，不能只靠本 Viewpoint。

## [2026-05-08] correction | Wright et al. 2017 - 3-minute all-out cycling critical power test

- 修正原因：
  - 既有 `Wright_2017_3min_allout_CP_validity.md` 為舊格式，且 source_tier 未依 AGENTS.md 區分 original research article。
  - 既有頁面已提到 3-min all-out 的 EP / WEP 問題，但尚未拆出獨立方法頁。
- 本輪單一來源：
  - `C:\原始資料\the-reliability-and-validity-of-the-3-min-all-out-cycling-7xcudjg120\the-reliability-and-validity-of-the-3-min-all-out-cycling-7xcudjg120.md`
  - 只完整處理此一篇來源；未混入 Vanhatalo 2007、Dekerle 2013、Karsten 2014 或其他 3-min all-out source。
- 重新建立來源摘要：
  - `09_來源摘要/Wright_2017_3min_allout_CP_validity.md`
- 新增頁面：
  - `04_CPET/Three_Minute_All_Out_Critical_Power_Test.md`
- 更新頁面：
  - `04_CPET/CP_Test_Reliability.md`
  - `04_CPET/CPET_Protocol_Design.md`
  - `index.md`（Total pages 574 -> 575；Wright source summary Tier 3 -> Tier 5）
  - `log.md`
- 抽出概念：
  - Three-minute all-out critical power test：用 3 分鐘 all-out cycling 的 final 30 s `EP` 估計 `CP`，但 mode / cadence / resistance setup 會改變 validity，且 `WEP` 不能直接當 `W'`。
- 本輪直接事實：
  - Source 為 2017 *International Journal of Sports Medicine* original research article / accepted manuscript，DOI `10.1055/s-0043-102944`。
  - Participants 為 12 位 male cyclists，age 32 +/- 6.6 years，MAP 349 +/- 36 W，V̇O2peak 4.4 +/- 0.5 L/min。
  - 每位 participant 完成 8 tests：1 ramp test、3 fixed-power CP tests、4 three-minute all-out tests。
  - Original CP protocol 得到 `CP` 244.9 +/- 26.2 W、`W'` 22.7 +/- 5.6 kJ。
  - Isokinetic `EP` 240.9 +/- 23.3 W，與 `CP` 無顯著差異。
  - Linear `EP` 275.1 +/- 41.2 W，顯著高於 `CP`。
  - Isokinetic `WEP` 15.6 +/- 5.6 kJ，linear `WEP` 13.5 +/- 4.7 kJ，兩者都顯著低於 `W'`。
  - EP CoV：isokinetic 1.93%、linear 1.17%；WEP CoV：isokinetic 8.44%、linear 5.39%。
- 發現衝突：
  - Reliable EP 不等於 valid CP estimate；linear EP 在本 protocol reliable but not valid。
  - EP 與 WEP 不能被當成同一組 validity 行為；WEP 在兩種 mode 都低估 `W'`。
  - 12 位 male cyclists 的 original research 不能直接外推至 clinical CPET populations。
- 待追蹤問題：
  - 若要建立完整 3-min all-out consensus，需分別單一來源 ingest Vanhatalo 2007、Dekerle 2013、Karsten 2014 與 alternative load-setting studies。
  - 若要臨床化使用 3-min all-out test，需另找 HF、COPD、older adult 或 low-fit population validation source。

## [2026-05-08] correction | Fawkner and Armstrong 2004 - pediatric heavy-exercise V̇O2 kinetics modeling

- 修正原因：
  - 既有 `Modelling_the_VO2_kinetic_response_to_heavy_intensity_exercise_in_children.md` 為舊格式，且 source_tier 未依 AGENTS.md 區分 original research article。
  - 既有 `VO2_Kinetics.md` 已提到 pediatric caveat，但尚未拆出獨立概念頁。
- 本輪單一來源：
  - `C:\原始資料\00140130412331290899\00140130412331290899.md`
  - 只完整處理此一篇來源；未混入 Fawkner & Armstrong 2003 review、Obert 2000、Williams 2001、adult VO2 kinetics review 或其他 pediatric CPET source。
- 重新建立來源摘要：
  - `09_來源摘要/Modelling_the_VO2_kinetic_response_to_heavy_intensity_exercise_in_children.md`
- 新增頁面：
  - `04_CPET/Pediatric_Heavy_Exercise_VO2_Kinetics_Modeling.md`
- 更新頁面：
  - `04_CPET/VO2_Kinetics.md`
  - `index.md`（Total pages 575 -> 576；Fawkner source summary Tier 3 -> Tier 5）
  - `log.md`
- 抽出概念：
  - Pediatric heavy-exercise V̇O2 kinetics modeling：兒童 heavy-intensity cycling 的 V̇O2 response 多數不能用單一 exponential model 充分描述，但 secondary-component parameters 不宜直接當成穩定生理指標。
- 本輪直接事實：
  - Source 為 2004 *Ergonomics* original research article，DOI `10.1080/00140130412331290899`。
  - Participants 為 62 位 healthy children，35 male、27 female，aged 10-15 years。
  - Protocol 使用 electronically braked cycle ergometer；先做 ramp test 取得 peak V̇O2 與 `T_v-slope`，再做 repeated step transitions。
  - Step work rate designed to elicit 40% of the difference between V̇O2 at `T_v-slope` and peak V̇O2。
  - 每位 participant 至少完成 3 次、通常 4 次 transitions，並平均 breath-by-breath responses。
  - Model 1：single exponential with delay term；Model 2：exponential + linear term；Model 3：double exponential with independent delays；Model 4：phase-2 fitting-window model。
  - F-test 顯示 model 1 best fit in 3/62 participants (5%)，model 2 in 11/62 (18%)，model 3 in 48/62 (77%)。
  - Up to 95% of response profiles were better fitted by model 2 or model 3 than by model 1。
  - Source conclusion：children exercising at 40% delta are likely to express a V̇O2 slow component after a rapid exponential rise。
  - Source warning：secondary exponential parameters should not be relied upon for physiological significance；primary component should be parameterized by identifying slow-component onset and fitting phase 2 alone。
- 發現衝突：
  - 與「children lack V̇O2 slow component during heavy exercise」衝突；本 source 支持 delayed slow-component-like behavior。
  - 與「double-exponential better fit = secondary parameters are physiologically precise」衝突；source 明確警告 secondary parameters confidence intervals and interpretability limitations。
  - 與「單篇 healthy-child cycling study 可直接變成 clinical pediatric CPET rule」衝突；source 不是 clinical validation。
- 待追蹤問題：
  - 若要建立 pediatric V̇O2 kinetics consensus，需另行單一來源處理 pediatric review 或 systematic source。
  - 若要處理 pediatric disease populations，需另找 congenital heart disease、pulmonary disease、obesity、neuromuscular disease 或 cerebral palsy CPET source。
  - `VO2_Kinetics.md` 仍是多來源 hub；若 pediatric CPET 資料增加，應另拆 `Pediatric_CPET_Physiology.md` 或 `Pediatric_CPET_Protocol_Design.md`。

## [2026-05-08] correction | Goulding et al. 2021 - VO2 kinetics and exercise tolerance

- 修正原因：
  - 既有 `Goulding_2021_VO2_kinetics_exercise_tolerance.md` 為舊格式，且 source_tier 未依 AGENTS.md 區分 high-quality mechanistic review。
  - 既有 `VO2_Kinetics.md` 已使用 Goulding 2021 的核心模型，但尚未拆出獨立概念頁。
- 本輪單一來源：
  - `C:\原始資料\Bioenergetic Mechanisms Linking V̇O2 Kinetics and Exercise Tolerance\Bioenergetic Mechanisms Linking V̇O2 Kinetics and Exercise Tolerance.md`
  - 只完整處理此一篇來源；未混入 Goulding & Marwood 2023、Korzeniewski & Rossiter 2020 原文、Goulding 2023 priming review 或其他 VO2 kinetics sources。
- 重新建立來源摘要：
  - `09_來源摘要/Goulding_2021_VO2_kinetics_exercise_tolerance.md`
- 新增頁面：
  - `04_CPET/Critical_Threshold_Positive_Feedback_Model.md`
- 更新頁面：
  - `04_CPET/VO2_Kinetics.md`
  - `index.md`（Total pages 576 -> 577；Goulding 2021 source summary Tier 1 -> Tier 4）
  - `log.md`
- 抽出概念：
  - Critical threshold and positive feedback model：`tauV̇O2` 決定 O2 deficit 與 metabolite accumulation；若超過 critical intramuscular range，fatigue 造成 work inefficiency，使同一 external power 需要更多 ATP turnover，進一步推動 metabolite accumulation、V̇O2SC 與 supra-CP intolerance。
- 本輪直接事實：
  - Source 為 *Exercise and Sport Sciences Reviews* 2021 mechanistic review / hypothesis article，DOI `10.1249/JES.0000000000000267`。
  - Source 明確將 V̇O2 kinetics、O2 deficit、metabolic stability、CP、V̇O2 slow component 與 W' 放入同一機制模型。
  - Steady-state cycle ergometry 中 V̇O2-power gain 約 9-11 mL/min/W。
  - Source 例示 `tauV̇O2` 可從 elite endurance athletes 約 12 s 到 elderly COPD patients 約 120 s。
  - 在達 steady state 的 power outputs，O2 deficit 可近似為 `Delta V̇O2 x tauV̇O2`。
  - O2 deficit-related perturbations 包含 PCr depletion、glycolysis / glycogenolysis、H+、Pi、ADP、K+ 與 Ca2+ handling disturbance。
  - Source 使用 `Pi` 作為 prime candidate metabolite，因其可影響 cross-bridge power stroke、myofibrillar Ca2+ sensitivity 與 SR Ca2+ handling。
  - Source 認為 crossing critical metabolite threshold 後，fatigue 可降低 work efficiency，造成 ATP demand 增加與 metabolite accumulation 正回饋。
  - Source 承認 whole-body CP 可能更像 boundary layer / phase transition，而非單一 sharp threshold。
  - Source 結論明確指出 future in vivo experiments are required to test this hypothesis。
- 發現衝突：
  - 與「O2 deficit 可單獨、線性預測所有 exercise tolerance」衝突；source 指出 non-steady-state exercise 不能可靠用 O2 deficit 單獨預測。
  - 與「W' 是單純 anaerobic tank」衝突；source 將 W' 視為 fatigue / inefficiency / limiting conditions 進展的 finite tolerance。
  - 與「critical threshold 是 routine CPET 可直接量到的 cut-off」衝突；source 的 threshold 主要是 mechanistic model / hypothesis。
- 待追蹤問題：
  - 若要把 `Pi` / critical threshold 模型做成更嚴謹概念頁，需另行單一來源處理 Korzeniewski & Rossiter 2020。
  - 若要臨床應用於 COPD、HF 或 diabetes，需另選 disease-specific CPET / kinetics source 校正。
  - 若要處理 `W'` 與 V̇O2SC 的量化關係，需另行單一來源處理 original intervention studies。

## [2026-05-09] correction | Gaesser and Poole 1996 - V̇O2 slow component and work-rate nonlinearity

- 修正原因：
  - 既有 `Gaesser_Poole_1996_VO2_slow_component.md` 為舊格式，且把 ESSR review chapter 誤標為 Tier 1。
  - 既有 `VO2_Slow_Component.md` 已使用 Gaesser and Poole 1996 的核心框架，但尚未拆出 `constant-load exercise above GET` 的 V̇O2-work rate nonlinearity 概念頁。
- 本輪單一來源：
  - `C:\原始資料\GaesserandPoole_ESSR1996_Theslowcomponentofoxygenuptakekineticsinhumans\GaesserandPoole_ESSR1996_Theslowcomponentofoxygenuptakekineticsinhumans.md`
  - 只完整處理此一篇來源；未混入 Poole and Gaesser 2025、Korzeniewski and Zoladz 2015、Goulding 2021 或其他 V̇O2 kinetics source。
- 重新建立來源摘要：
  - `09_來源摘要/Gaesser_Poole_1996_VO2_slow_component.md`（source_tier 1 -> 4）
- 新增頁面：
  - `04_CPET/VO2_Work_Rate_Nonlinearity_Above_GET.md`
- 更新頁面：
  - `04_CPET/VO2_Slow_Component.md`
  - `index.md`（Total pages 577 -> 578；新增 V̇O2-work rate nonlinearity concept；`VO2_Slow_Component.md` hub 從 Tier 1 降級為 mixed Tier 3 + Tier 4 + Tier 6）
  - `log.md`
- 抽出概念：
  - VO2-work rate nonlinearity above GET：constant-load exercise 高於 GET / LT 後，V̇O2 不再能由 sub-GET linear gain 推估；slow component 讓同一 external work rate 的 oxygen cost 隨時間增加，並形成 heavy / severe domain 判讀核心。
- 本輪直接事實：
  - Source 為 1996 *Exercise and Sport Sciences Reviews* Vol. 24 review chapter，pp. 35-70。
  - Authors 指出常見 V̇O2-work rate linearity 主要適用於低於 lactate threshold 的測試，或快速 incremental exercise。
  - Sustained constant-load exercise 高於 lactate threshold 時，rapid phase 之後會疊加 V̇O2 slow component。
  - Moderate exercise 低於 lactate threshold 時通常約 3 分鐘內達 V̇O2 steady state，gain 約 9-11 mL O2/min/W。
  - Heavy exercise 中 slow component 可延遲穩定；severe exercise 中 V̇O2 與 lactate 無法穩定，V̇O2 可被推向 V̇O2max。
  - Slow component 常操作性定義為運動第 3 分鐘後仍持續上升的 V̇O2，onset 約 80-110 秒後。
  - Slow component 可超過 1.0 L/min；極端情況約 1.0-1.5 L/min。
  - Source 明確區分 high-intensity V̇O2 slow component 與 prolonged moderate exercise 的小幅 oxygen drift。
  - Simultaneous pulmonary and leg V̇O2 evidence 支持 exercising limbs 為主要來源；約 86% of pulmonary V̇O2 increment beyond minute 3 可由 leg V̇O2 increase accounting。
  - Lactate 與 slow component 高度相關，但 source 不支持 lactate 作為充分單一原因。
- 發現衝突：
  - 與「V̇O2-work rate relation 在所有 submaximal constant-load exercise 中全域線性」衝突。
  - 與「oxygen drift 與 V̇O2 slow component 可混用」衝突。
  - 與「lactate 是 V̇O2SC 的單一原因」衝突。
  - 與「fixed %V̇O2max 足以描述 heavy / severe constant-load intensity」衝突。
- 待追蹤問題：
  - 若要建立現代 V̇O2SC mechanism consensus，需另行單一來源處理後續 systematic / mechanistic review。
  - 若要整理 disease-specific CPET implication，需另選 HF、COPD、PAH 或 neuromuscular disease source。
  - `VO2_Slow_Component.md` 已是多來源 hub；若再加入更多來源，應拆出 `VO2_Slow_Component_Mechanisms.md` 或 `VO2_Slow_Component_Methodology.md`。

## [2026-05-09] correction | Stringer Wasserman Casaburi 1995 - heavy constant-work VCO2-VO2 inflection

- 修正原因：
  - 既有 `Stringer_Wasserman_Casaburi_1995_VCO2_VO2_heavy_constant_work.md` 為舊格式，且把 original physiology study 誤標為 Tier 3。
  - 既有 `V_Slope_Method.md` 與 `Gas_Exchange_Threshold.md` 已引用此研究作 constant-work corroboration，但尚未拆出單一概念頁。
- 本輪單一來源：
  - `C:\原始資料\The VCO2 VO2 relationship during heavy constant work rate exercise\The VCO2 VO2 relationship during heavy constant work rate exercise.md`
  - 只完整處理此一篇來源；未混入 Beaver 1986、Poole 2020、Yano 1997、Hirakoba 1996 或其他 V-slope / GET source。
- 重新建立來源摘要：
  - `09_來源摘要/Stringer_Wasserman_Casaburi_1995_VCO2_VO2_heavy_constant_work.md`（source_tier 3 -> 5）
- 新增頁面：
  - `04_CPET/Heavy_Constant_Work_VCO2_VO2_Inflection.md`
- 更新頁面：
  - `04_CPET/V_Slope_Method.md`（補入新概念頁連結；hub 證據標記從 Tier 1 修為 Tier 4 + Tier 5 + historical Tier 3）
  - `04_CPET/Gas_Exchange_Threshold.md`
  - `index.md`（Total pages 578 -> 579；新增 heavy constant-work VCO2-VO2 inflection concept；Stringer source summary Tier 3 -> Tier 5）
  - `log.md`
- 抽出概念：
  - Heavy constant-work VCO2-VO2 inflection：heavy / very heavy constant-work exercise 中，VCO2 相對 VO2 的早期上翹與 arterial lactate rise / standard bicarbonate fall 同步，支持 bicarbonate buffering physiology，但不能取代 ramp CPET GET algorithm。
- 本輪直接事實：
  - Source 為 1995 original physiology study。
  - Participants 為 8 位 healthy non-smoking men，age 26 (6) years，height 1.78 (0.06) m，mass 72.5 (4.4) kg。
  - Protocol 先以 incremental cycle test 決定 LAT，再完成 6-min constant-work cycling bouts：moderate、heavy、very heavy。
  - Mean VO2max 為 3.59 (0.66) L/min，49.1 mL/kg/min。
  - Mean LAT 為 2.05 (0.39) L/min，約 57% VO2max。
  - Mean work rates 為 120 (43)、210 (52)、267 (60) W。
  - Gas exchange 以 breath-by-breath VO2 / VCO2 量測。
  - Arterial blood samples 在最初 160-180 秒每 7.5 秒採樣，之後每 30 秒採樣至運動結束。
  - Heavy / very heavy exercise 中，VCO2 約在 exercise onset 後 40-50 秒相對 VO2 abrupt increase。
  - Heavy / very heavy exercise 中，VCO2 約在 60-90 秒內等於或超過 VO2。
  - Lactate rise 與 standard bicarbonate fall 約在 30-40 秒開始。
  - VCO2-VO2 inflection 的 VO2 與 lactate 增加 1 mmol/L 的 VO2 高度相關，r = 0.90。
  - VCO2-VO2 inflection 的 VO2 與 standard bicarbonate 下降 1 mmol/L 的 VO2 高度相關，r = 0.95。
  - Post-inflection VCO2-VO2 slope 與 lactate rise / bicarbonate fall magnitude 相關，r = 0.79 / 0.80。
  - PaCO2 與 [H+] behavior 不支持 early respiratory alkalosis 作為主要解釋。
- 發現衝突：
  - 與「VCO2-VO2 inflection 只是圖形技巧」衝突；本 source 支持 acid-base physiology 對應。
  - 與「單篇 constant-work healthy-men study 可直接當 clinical ramp GET algorithm」衝突。
  - 與「LAT / AT 字面代表 muscle dysoxia」衝突。
  - 與「heavy exercise 中 early excess VCO2 必然來自 hyperventilation」衝突。
- 待追蹤問題：
  - 若要完整重建 V-slope method，需另行單一來源校正 Beaver 1986。
  - 若要處理 disease-specific VCO2-VO2 interpretation，需另選 HF、COPD、PAH 或 perioperative CPET source。
  - `Gas_Exchange_Threshold.md` 仍混合 review、original method study、historical models 與 disease-specific reviews，未來可拆成 methodology / clinical application 兩頁。

## [2026-05-09] correction | Beaver Wasserman Whipp 1986 - V-slope method original algorithm

- 修正原因：
  - 既有 `Beaver_Wasserman_Whipp_1986_V_slope_method.md` 為舊格式，且把 original method study 誤標為 Tier 3。
  - 既有 `V_Slope_Method.md` 已使用 Beaver 1986 作主幹，但尚未拆出原始 algorithm 的單一概念頁。
- 本輪單一來源：
  - `C:\原始資料\beaver-et-al-1986-a-new-method-for-detecting-anaerobic-threshold-by-gas-exchange\beaver-et-al-1986-a-new-method-for-detecting-anaerobic-threshold-by-gas-exchange.md`
  - 只完整處理此一篇來源；未混入 Stringer 1995、Poole 2020、Yano 1997 或其他 GET / V-slope source。
- 重新建立來源摘要：
  - `09_來源摘要/Beaver_Wasserman_Whipp_1986_V_slope_method.md`（source_tier 3 -> 5）
- 新增頁面：
  - `04_CPET/V_Slope_Method_Original_Algorithm.md`
- 更新頁面：
  - `04_CPET/V_Slope_Method.md`
  - `04_CPET/Gas_Exchange_Threshold.md`
  - `index.md`（Total pages 579 -> 580；新增 V-slope original algorithm concept；Beaver source summary Tier 3 -> Tier 5）
  - `log.md`
- 抽出概念：
  - V-slope method original algorithm：incremental CPET 中，以 VCO2 對 VO2 的 two-segment regression breakpoint 偵測 bicarbonate-buffering-related excess CO2 onset；並用較高強度的 respiratory compensation point 作 upper boundary。
- 本輪直接事實：
  - Source 為 1986 *Journal of Applied Physiology* original method / physiology study。
  - Participants 為 10 位 healthy male volunteers，age 19-39 years。
  - Protocol 為 cycle ergometer，4 min unloaded exercise 後，以 15 W/min incremental exercise 至 tolerance。
  - Measurements 包含 breath-by-breath VO2、VCO2、VE、heart rate、PETCO2。
  - Arterial blood 於 rest、unloaded cycling 與 incremental phase 每 2 min 採樣，分析 lactate 與 bicarbonate。
  - Breath-by-breath data 先 interpolate 成 regular time intervals，並使用 minimal moving average；source 使用 9 s。
  - Authors 建議 filtering 越少越好，避免扭曲 underlying curve shape。
  - Incremental phase 開始後的第 1 分鐘通常排除，因為 CO2 stores 造成 VCO2 kinetics lag VO2。
  - Remaining initial segment 若 slope <0.6 也排除。
  - VCO2-VCO2 noise 可依 PETCO2 fluctuation 作 physiological correction；其目的在減少 ventilation-related VCO2 fluctuation。
  - VCO2-VO2 curve 分成兩段 linear regression，intersection 為 tentative AT。
  - Slope change 必須 >0.1 才接受為 AT，以避免 noise 造成 spurious breakpoint。
  - RCP 由 VE-VCO2 plot 另行偵測；若存在，作為 AT calculation upper boundary。
  - Mean V-slope AT 為 1.83 +/- 0.30 L/min VO2。
  - Mean panel visual AT 為 1.85 +/- 0.34 L/min VO2，差異不顯著。
  - V-slope coefficient of variation 為 0.023 +/- 0.006；panel average coefficient of variation 為 0.127 +/- 0.080。
  - V-slope AT 與 estimated bicarbonate threshold 無顯著差異：1.83 +/- 0.30 vs 1.78 +/- 0.24 L/min VO2。
  - V-slope AT 對應 lactate 比 mathematically defined LT 高 0.50 +/- 0.34 meq/L。
  - RCP 高於 V-slope AT：2.51 +/- 0.42 vs 1.83 +/- 0.30 L/min VO2。
- 發現衝突：
  - 與「VE-only threshold detection 等同 V-slope」衝突；source 明確指出 ventilatory response 可能 lag 或受 chemosensitivity 影響。
  - 與「RCP 可當作 AT / GET」衝突；source 分開偵測 RCP 並將其作為 upper boundary。
  - 與「anaerobic threshold 字面等於 muscle dysoxia」衝突；本輪只保留 operational gas-exchange method。
  - 與「Beaver 1986 是 Tier 3 evidence」衝突；依 AGENTS.md 應為 Tier 5 original research。
- 待追蹤問題：
  - 若要建立現代 automated V-slope implementation，需要另選 software / methods validation source。
  - 若要 disease-specific GET 判讀，需另行單一來源處理 HF、COPD、PAH 或 perioperative CPET source。
  - `V_Slope_Method.md` 仍是多來源 method hub；後續可把 historical CO2 models 和 clinical application 再拆頁。

## [2026-05-09] correction | Yano 1997 - physiological model of CO2 output during incremental exercise

- 修正原因：
  - 既有 `Physiological_model_of_CO2_output_during_incremental_exercise.md` 為舊格式，且把 original physiology model study 誤標為 Tier 3。
  - 既有 `V_Slope_Method.md` 與 `Gas_Exchange_Threshold.md` 已把 Yano 1997 放在 historical model，但尚未拆出單一概念頁。
- 本輪單一來源：
  - `C:\原始資料\Physiological model of CO2 output during incremental exercise\Physiological model of CO2 output during incremental exercise.md`
  - 只完整處理此一篇來源；未混入 Beaver 1986、Stringer 1995、Hirakoba 1996、Yunoki 1999 或其他 VCO2 / GET sources。
- 重新建立來源摘要：
  - `09_來源摘要/Physiological_model_of_CO2_output_during_incremental_exercise.md`（source_tier 3 -> 5）
- 新增頁面：
  - `04_CPET/Incremental_Exercise_VCO2_Partitioning_Model.md`
- 更新頁面：
  - `04_CPET/V_Slope_Method.md`
  - `04_CPET/Gas_Exchange_Threshold.md`
  - `index.md`（Total pages 580 -> 581；新增 incremental exercise VCO2 partitioning concept；Yano source summary Tier 3 -> Tier 5）
  - `log.md`
- 抽出概念：
  - Incremental exercise VCO2 partitioning model：Yano 1997 將 incremental exercise 的 VCO2 概念性分成 non-lactic VCO2 與 excess VCO2，以 PvCO2、PaCO2、blood CO2 dissociation curve 與 lactate-related CO2 excess 解釋高強度時的 VCO2 訊號，但不能取代 GET / V-slope algorithm。
- 本輪直接事實：
  - Source 為 1997 *Ergonomics* original human physiology / model article，DOI `10.1080/001401397188008`。
  - Participants 為 8 位 trained university athletes；raw OCR 的 age SD 顯示不合理，需視為不確定。
  - Mean height 170 +/- 4.58 cm，mean body mass 59 +/- 4.48 kg，mean maximal oxygen uptake 3.52 +/- 0.295 L/min。
  - Protocol 使用 Monark cycle ergometer；0.5 kp 起始、60 rpm，每分鐘增加 0.5 kp。
  - Participants 完成 incremental exercise to exhaustion，另於其他日做到 540 與 1080 kpm/min。
  - Expired gas 用 Douglas bags 於 rest 與 exercise 每分鐘收集；VO2 / VCO2 由 gas concentration 與 ventilation 計算。
  - Mixed venous CO2 pressure 以 CO2 rebreathing technique 估計。
  - PaCO2 由 PETCO2 與 tidal volume regression equation 估計，非直接 arterial sampling。
  - Blood lactate 於 rest、1080 kpm/min 後 5 分鐘與 exhaustion 採 median cubital vein sample。
  - Non-lactic VCO2 與 PvCO2 相關，r = 0.950。
  - VCO2 與 PaCO2 / PvCO2 呈 multiple correlation，r = 0.971。
  - CO2 excess 與 blood lactate increase 相關，r = 0.828。
  - 1080 kpm/min 時，8 位中 3 位觀察到 excess VCO2。
- 發現衝突：
  - 與「excess VCO2 可當作直接 lactate meter」衝突。
  - 與「Yano model 可取代 GET / V-slope algorithm」衝突。
  - 與「AT 字面代表 discrete muscle dysoxia」衝突。
  - 與「Yano 1997 是 Tier 3 evidence」衝突；依 AGENTS.md 應為 Tier 5 original research。
- 待追蹤問題：
  - Hirakoba 1996 與 Yunoki 1999 仍需各自依單一來源 correction，避免 historical VCO2 models 維持舊格式與舊 tier。
  - 若要建立現代 automated V-slope implementation，需另行處理 VO2FITTING 或其他 software / methods validation source。
  - `Gas_Exchange_Threshold.md` 仍混合 methodology、clinical application 與 disease-specific review，未來可拆成 method page 與 clinical CPET application page。

## [2026-05-09] correction | Hirakoba et al. 1996 - excess CO2 prediction of lactate during constant exercise

- 修正原因：
  - 既有 `Hirakoba_1996_excess_CO2_lactate_prediction.md` 為舊格式，且把 original physiology prediction study 誤標為 Tier 3。
  - 既有 `V_Slope_Method.md` 與 `Gas_Exchange_Threshold.md` 已把 Hirakoba 1996 放在 historical model，但尚未拆出單一概念頁。
- 本輪單一來源：
  - `C:\原始資料\La prediction from excess CO2\La prediction from excess CO2.md`
  - 只完整處理此一篇來源；未混入 Yano 1997、Yunoki 1999、Beaver 1986、Stringer 1995 或其他 VCO2 / GET sources。
- 重新建立來源摘要：
  - `09_來源摘要/Hirakoba_1996_excess_CO2_lactate_prediction.md`（source_tier 3 -> 5）
- 新增頁面：
  - `04_CPET/Constant_Work_Excess_CO2_Lactate_Prediction.md`
- 更新頁面：
  - `04_CPET/V_Slope_Method.md`
  - `04_CPET/Gas_Exchange_Threshold.md`
  - `index.md`（Total pages 581 -> 582；新增 constant-work excess CO2 lactate prediction concept；Hirakoba source summary Tier 3 -> Tier 5）
  - `log.md`
- 抽出概念：
  - Constant-work excess CO2 lactate prediction：以先前 incremental test 的 below-AT VCO2-VO2 regression 與個人 CO2 excess-Delta La factor，將 constant exercise 的 integrated excess VCO2 轉成 predicted lactate accumulation；高強度相關性佳，但 near-threshold 100% AT 顯著高估，不能取代 GET / lactate testing。
- 本輪直接事實：
  - Source 為 1996 *Applied Human Science* original human physiology / prediction study。
  - Participants 為 8 位 healthy active male volunteers。
  - Mean age 20.1 +/- 1.2 years，height 170.4 +/- 4.7 cm，body mass 57.0 +/- 5.5 kg。
  - Mean VO2max 58.3 +/- 2.8 mL/kg/min，mean AT-VO2 36.8 +/- 2.5 mL/kg/min。
  - Incremental test：4-min unloaded pedaling 後，每分鐘增加 30 W until exhaustion。
  - Constant exercise：三個 4-min stages，分別為 100%、120%、150% of each subject's AT-VO2。
  - Stage completion：stage I n=8，stage II n=7，stage III n=5。
  - Ex CO2 per body mass across stages：15.36 +/- 8.51、34.15 +/- 16.12、62.87 +/- 4.77 mL/kg。
  - Measured vs predicted Delta La：stage I 1.82 +/- 0.83 vs 3.19 +/- 1.70 mmol/L；stage II 5.58 +/- 3.47 vs 7.09 +/- 3.28 mmol/L；stage III 12.19 +/- 2.36 vs 12.74 +/- 1.83 mmol/L。
  - Stage I predicted lactate significantly exceeded measured lactate；stage II / III no significant difference。
  - Ex CO2 per body mass correlated with measured Delta La，r = 0.939，p < 0.001。
  - Predicted Delta La correlated with measured Delta La，r = 0.954，p < 0.001，SEE 1.47 mmol/L。
  - Individual prediction error ranged from -1.71 to 4.05 mmol/L。
- 發現衝突：
  - 與「excess VCO2 可當作直接 lactate meter」衝突。
  - 與「constant-work excess CO2 prediction 可取代 GET / V-slope algorithm」衝突。
  - 與「AT 字面代表 muscle dysoxia」衝突。
  - 與「Hirakoba 1996 是 Tier 3 evidence」衝突；依 AGENTS.md 應為 Tier 5 original research。
- 待追蹤問題：
  - Yunoki 1999 仍需依單一來源 correction，釐清 excess VCO2 kinetics lag、CO2 stores 與 postexercise hyperventilation。
  - 若要整理 modern excess VCO2 / lactate relationship，需要另行逐篇處理 contemporary validation 或 review source。
  - `Gas_Exchange_Threshold.md` 仍混合 methodology、clinical application 與 disease-specific review，未來可拆成 method page 與 clinical CPET application page。

## [2026-05-09] correction | Yunoki et al. 1999 - excess VCO2 kinetics during and after intensive exercise

- 修正原因：
  - 既有 `Yunoki_1999_excess_CO2_kinetics.md` 為舊格式，且把 original physiology kinetics study 誤標為 Tier 3。
  - 既有 `V_Slope_Method.md` 與 `Gas_Exchange_Threshold.md` 已把 Yunoki 1999 放在 historical model，但尚未拆出單一概念頁。
- 本輪單一來源：
  - `C:\原始資料\kinetics of excess VCO2\kinetics of excess VCO2.md`
  - 只完整處理此一篇來源；未混入 Yano 1997、Hirakoba 1996、Beaver 1986、Stringer 1995 或其他 VCO2 / GET sources。
- 重新建立來源摘要：
  - `09_來源摘要/Yunoki_1999_excess_CO2_kinetics.md`（source_tier 3 -> 5）
- 新增頁面：
  - `04_CPET/Excess_VCO2_Kinetics_Lag_After_Intensive_Exercise.md`
- 更新頁面：
  - `04_CPET/V_Slope_Method.md`
  - `04_CPET/Gas_Exchange_Threshold.md`
  - `index.md`（Total pages 582 -> 583；新增 excess VCO2 kinetics lag concept；Yunoki source summary Tier 3 -> Tier 5）
  - `log.md`
- 抽出概念：
  - Excess VCO2 kinetics lag after intensive exercise：short intensive exercise 中 lactate production 可自運動初期開始，但 pulmonary excess VCO2 會因 CO2 stores、PCO2 change、PCr recovery、lactate diffusion 與 hyperventilation 而延遲，甚至先出現負值再於運動後達峰。
- 本輪直接事實：
  - Source 為 1999 *Japanese Journal of Physiology* original human physiology / kinetics study。
  - Participants 為 6 位 active males who did not train regularly。
  - Mean age 23.0 +/- 1.9 years，height 170.5 +/- 6.1 cm，body mass 66.1 +/- 2.9 kg。
  - Incremental cycle test measured VO2max，mean VO2max 2.7 +/- 0.4 L/min。
  - Wingate maximal power 726 +/- 54 W，mean power 564 +/- 18 W。
  - Intensive tests：40、60、80 秒 cycling bouts；282 +/- 9 W，90 rpm，相當於 50% mean Wingate power。
  - 80-s test power 約等於 incremental-test exhaustion power 的 108 +/- 11.5%。
  - VE、VO2、VCO2、ETCO2 以 breath-by-breath 量測並取 20-s average。
  - Fingertip lactate 於 rest、immediately postexercise、5、10、20、30 min postexercise 採樣。
  - Excess VCO2 定義為 VCO2 minus VO2；total excess CO2 為 exercise start 到 postexercise 10 min 的 excess VCO2 sum。
  - 80-s test 中 excess VCO2 在運動開始後 40 s 達到 peak negative value，之後轉正，於運動後 60 s 達峰，約 postexercise 9 min 回到 zero。
  - 40-s 與 60-s tests 也在運動開始後 40 s 出現 temporary negative excess VCO2，之後約 postexercise 60-80 s 達峰，約 7 與 8 min 回到 zero。
  - ETCO2 上升至 exercise end 後約 20 s，約 postexercise 3 min 回到 pre-exercise value，之後低於 baseline。
  - Peak lactate values at 5 min postexercise：40-s 4.06 +/- 0.47 mM，60-s 6.00 +/- 0.62 mM，80-s 7.74 +/- 0.85 mM。
  - Peak lactate increase 與 exercise duration linear correlation，r = 0.91，p < 0.01。
  - Excess CO2 per body mass 與 lactate increase at 10 min postexercise 相關，r = 0.88，p < 0.01。
- 發現衝突：
  - 與「excess VCO2 可當作 instantaneous lactate meter」衝突。
  - 與「total excess CO2 correlation 等於 VCO2 kinetics 同步於 lactate production」衝突。
  - 與「short intensive exercise model 可取代 GET / V-slope algorithm」衝突。
  - 與「Yunoki 1999 是 Tier 3 evidence」衝突；依 AGENTS.md 應為 Tier 5 original research。
- 待追蹤問題：
  - 若要整理 modern excess VCO2 / lactate relationship，需要另行逐篇處理 contemporary validation 或 review source。
  - 若要處理 recovery-phase VCO2 與 performance fatigability，可接續 Wooten 2021。
  - `Gas_Exchange_Threshold.md` 仍混合 methodology、clinical application 與 disease-specific review，未來可拆成 method page 與 clinical CPET application page。

## [2026-05-09] correction | Wooten et al. 2021 - excess VCO2 and recovery VCO2 as indices of performance fatigability

- 修正原因：
  - 既有 `Wooten_2021_excess_VCO2_recovery_fatigability.md` 混入另一篇 Wooten training paper 的題名、設計與書目。
  - 本輪依單一來源原則，只處理 `Pilot and Feasibility Studies` 2021 這篇 cross-sectional feasibility pilot。
  - 既有 index 將此來源標為 Tier 3；依 AGENTS.md 應標為 Tier 5 original pilot study。
- 本輪單一來源：
  - `C:\原始資料\Wooten et al. Pilot and Feasibility Studies\Wooten et al. Pilot and Feasibility Studies.md`
  - 未混入 `C:\原始資料\nihms-1917261\nihms-1917261.md` 或其他 Wooten training source。
- 重新建立來源摘要：
  - `09_來源摘要/Wooten_2021_excess_VCO2_recovery_fatigability.md`（source_tier 3 -> 5）
- 新增頁面：
  - `04_CPET/Estimated_Excess_VCO2_and_Performance_Fatigability.md`
- 更新頁面：
  - `04_CPET/V_Slope_Method.md`
  - `04_CPET/Gas_Exchange_Threshold.md`
  - `04_CPET/VO2_Kinetics.md`
  - `index.md`（Total pages 583 -> 584；新增 estimated excess VCO2 / performance fatigability concept；Wooten source summary Tier 3 -> Tier 5）
  - `log.md`
- 抽出概念：
  - Estimated excess VCO2 and performance fatigability：以 V-slope AT 作為 estimated excess VCO2 演算法錨點，並用 peak CPET / submaximal CWRT 後的 recovery VCO2 off-kinetics 探索 performance fatigability；目前屬 feasibility-stage research signal，不是 validated clinical biomarker。
- 本輪直接事實：
  - Source 為 2021 *Pilot and Feasibility Studies* original cross-sectional feasibility pilot study。
  - Participants 為 7 位 apparently healthy adults，5 female / 2 male，mean age 30.7 +/- 5.1 years。
  - Visit 1：Bruce protocol peak treadmill CPET、10-min recovery、10-MWT。
  - Visit 2：submaximal CWRT at 80% AT，三個 6-min bouts、8-min active recovery、10-min passive recovery、10-MWT。
  - All subjects completed testing with no adverse events。
  - All subjects achieved RER >= 1.10 and peak HR >= 90% age-predicted during peak CPET。
  - AT was determined by V-slope method。
  - Excess VCO2 was estimated algebraically as total VCO2 area minus estimated metabolic VCO2 area above AT。
  - Excess VCO2 accounted for 61% of variability in VO2 on-kinetic ORI and 62% of variability in PFSS。
  - CPET recovery VCO2-off ORI and Kt accounted for 70% and 73% of variability in VO2 on-kinetic ORI。
  - Submaximal CWRT recovery VCO2-off ORI and Kt accounted for 93% and 96% of variability in performance fatigability in this small sample。
- 發現衝突：
  - 與「excess VCO2 是直接測量到的 buffering chemistry」衝突。
  - 與「estimated excess VCO2 可當 routine performance fatigability biomarker」衝突。
  - 與「AT 字面代表 muscle dysoxia」衝突；本研究的 AT 是 V-slope operational anchor。
  - 與舊 wiki 摘要把本來源和另一篇 Wooten training paper 混寫衝突。
- 待追蹤問題：
  - 若要處理另一篇 Wooten training source，需下一輪獨立 ingest / correction。
  - 需要直接 lactate、bicarbonate、pH 對照研究，才能驗證 estimated excess VCO2 與 acid-base physiology 的關係。
  - `Gas_Exchange_Threshold.md` 仍混合 methodology、clinical application 與 disease-specific review，未來可拆成 method page 與 clinical CPET application page。

## [2026-05-09] ingest | Wooten et al. 2021 - respiratory buffering after aerobic exercise training

- 本輪單一來源：
  - `C:\原始資料\nihms-1917261\nihms-1917261.md`
  - 只完整處理此一篇來源；未混入 `Wooten et al. Pilot and Feasibility Studies` 或其他 excess VCO2 / fatigability sources。
- 新增來源摘要：
  - `09_來源摘要/Wooten_2021_respiratory_buffering_AET_fatigability.md`
- 更新頁面：
  - `04_CPET/Estimated_Excess_VCO2_and_Performance_Fatigability.md`
  - `index.md`（Total pages 584 -> 585；新增 Wooten AET source summary；更新 estimated excess VCO2 concept 摘要）
  - `log.md`
- 抽出概念：
  - Estimated excess VCO2 as a moderator between recovery and performance fatigability：以 V-slope AT 為錨點估算 above-AT excess VCO2，並觀察 4 週 AET 後 recovery off-kinetics 與 fatigability 的關係是否受 excess VCO2 影響；此為 hypothesis-generating moderator signal，不是 validated clinical biomarker。
- 本輪直接事實：
  - Source 為 2021 *Cardiopulmonary Physical Therapy Journal* original single-arm longitudinal pilot study。
  - 59 individuals pre-screened，21 enrolled，20 completed all protocol。
  - Participants median age 52 years，IQR 46-55；11 female / 9 male；median BMI 26.5 kg/m2，IQR 23.1-29.7。
  - Training 為 supervised cycling，4 weeks，4 sessions/week，45 min/session，70 +/- 5% HRR。
  - Adherence 99.7%，只有 one missed session。
  - Peak CPX used cycle ergometry with 25 W/min increments and 60 rpm target cadence。
  - AT determined by V-slope method。
  - Recovery VO2 / VCO2 off-kinetics used mono-exponential fitting after excluding first 20 seconds。
  - Excess VCO2 was estimated as total VCO2 minus estimated metabolic VCO2 above AT。
  - Peak VO2 increased 2181 (705) -> 2484 (832) mL/min；change 304，p = .000。
  - AT-VO2 increased 1270 (401) -> 1360 (423) mL/min；change 89，p = .008。
  - Estimated excess VCO2 increased 2536 (1478) -> 3144 (1680) mL；change 608，p = .001。
  - Pk-Time increased 519 (151) -> 582 (147) seconds；change 63，p = .000。
  - Pk-Watts increased 209 (61) -> 233 (59) W；change 24，p = .000。
  - End1 increased 453 (295) -> 718 (470) seconds；change 265，p = .002。
  - End2 increased 734 (484) -> 1054 (776) seconds；change 321，p < .002，despite 12% higher End2 wattage。
  - VCO2 off-kinetic tau decreased 81.0 (10.9) -> 73.3 (10.6) seconds；p = .009。
  - VCO2 off-kinetic MRT decreased 102.8 (11.2) -> 95.7 (10.5) seconds；p = .015。
  - Recovery-fatigability correlations weakened after covarying estimated excess VCO2。
- 發現衝突：
  - 與「estimated excess VCO2 是直接 lactate / pH / bicarbonate measurement」衝突。
  - 與「correlation attenuation 可直接證明 causal mediation」衝突。
  - 與「single-arm pilot 可當 routine clinical biomarker validation」衝突。
  - 與「這篇 Wooten AET source 可和另一篇 Wooten feasibility source 混寫」衝突。
- 待追蹤問題：
  - 若要建立 excess VCO2 / recovery VCO2 / fatigability synthesis，需逐篇加入直接 lactate、bicarbonate、pH 或 controlled intervention source。
  - `Gas_Exchange_Threshold.md` 仍混合 methodology、clinical application 與 disease-specific review，未來可拆成 method page 與 clinical CPET application page。
  - exercise physiology 待處理候選仍包含 Zone 2 training narrative review、Nuuttila 2026 low-intensity endurance training、Poole_Gaesser_2025 VO2 slow component enigma 等來源。

## [2026-05-09] ingest | Storoschuk et al. 2025 - Zone 2 training narrative review

- 本輪單一來源：
  - `C:\原始資料\Much-Ado-About-Zone-2-A-Narrative-Review-Assessing-the-Efficacy-of-Zone-2-Training-for-Improving\Much-Ado-About-Zone-2-A-Narrative-Review-Assessing-the-Efficacy-of-Zone-2-Training-for-Improving.md`
  - 只完整處理此一篇來源；未混入 Nuuttila 2026、What-Is-Zone-2-Training 或其他 low-intensity training sources。
- 新增來源摘要：
  - `09_來源摘要/Storoschuk_2025_zone2_training_narrative_review.md`
- 新增頁面：
  - `05_Exercise_Physiology/Zone_2_Training_證據邊界.md`
- 更新頁面：
  - `05_Exercise_Physiology/Training_Intensity_Distribution.md`
  - `index.md`（Total pages 585 -> 587；新增 Zone 2 concept 與 Storoschuk source summary）
  - `log.md`
- 抽出概念：
  - Zone 2 Training evidence boundary：Zone 2 是通常位於 LT1 / GET 以下、接近 Fatmax 或可維持 conversation 的低到中等強度工具；目前證據支持其可用性，尤其可能改善 untrained populations 的 FAO capacity，但不支持它是一般人改善 mitochondrial capacity、FAO 或 CRF 的唯一或最佳強度。
- 本輪直接事實：
  - Source 為 2025 *Sports Medicine* narrative review article。
  - Accepted 2025-04-07，published online 2025-06-25。
  - Review target population 為 general population：non-endurance-trained individuals who are insufficiently active or meeting physical activity guidelines。
  - Review did not use a systematic literature search。
  - Articles were obtained by database searches, reference lists, relevant systematic reviews, social-media-shared articles, and literature known to authors。
  - Zone 2 被 operationalized as exercise below LT1 or physiological responses consistent with moderate-intensity domain。
  - Criteria included BLa < 2.0 mmol/L, below ventilatory threshold 1, below Fatmax, or <45% VO2max。
  - Popular claims often define Zone 2 around Fatmax, BLa about 1.7-2.0 mmol/L below LT1, and Talk Test conversational intensity。
  - Review example showed LT1 at 23%, 45%, and 57% of WRpeak across three individuals。
  - The authors found small and inconsistent activation of mitochondrial biogenic signaling after acute Zone 2 exercise。
  - Few studies explicitly investigated Zone 2 training effects on mitochondrial outcomes。
  - The review states that available evidence is mixed for Zone 2 improving mitochondrial capacity。
  - The authors cite meta-analytic evidence suggesting exercise below 60% maximum work rate is not expected to improve mitochondrial content or mitochondrial respiratory capacity。
  - The review argues that exercise above Zone 2 may be superior for inducing mitochondrial adaptations。
  - The review states Zone 2 training appears capable of increasing FAO capacity, likely mainly in sedentary / untrained populations。
  - Only one cited study measured FAO after confirmed Zone 2 training with BLa < 2.0 mmol/L and showed increased FATmax and MFO after 1 year in previously sedentary adults。
  - FATmax-anchored training cannot always be treated as Zone 2 evidence because FATmax can occur above Zone 2 in sedentary populations。
  - Evidence does not convincingly support Zone 2 superiority over higher intensities for FAO。
  - For CRF, higher intensities often produce equal or greater gains；in active / trained individuals they may be required。
- 發現衝突：
  - 與「Zone 2 是改善 mitochondria 的最佳強度」衝突。
  - 與「超過 Zone 2 會失去 mitochondrial benefit」衝突。
  - 與「elite endurance athletes 做很多 low-intensity，所以一般人也應只優先 Zone 2」衝突。
  - 與「Fatmax、LT1、GET、Talk Test、固定 heart-rate zone 是同一件事」衝突。
- 待追蹤問題：
  - Nuuttila 2026 low-intensity endurance training 仍需獨立處理，不能拿來補強本頁結論。
  - `What-Is-Zone-2-Training` 若屬一般網站或教育文章，應排在較後作低層級來源處理。
  - 未來若要做 Zone 2 synthesis，需先逐篇 ingest direct Zone 2 intervention trials 或 systematic reviews。

## [2026-05-09] ingest | Nuuttila et al. 2026 - low-intensity endurance training meta-analysis

- 本輪單一來源：
  - `C:\原始資料\Scandinavian+Med+Sci+Sports+-+2026+-+Nuuttila+-+Effects+of+Low‐Intensity+Endurance+Training+on+Aerobic+Fitness+and+Risk\Scandinavian+Med+Sci+Sports+-+2026+-+Nuuttila+-+Effects+of+Low‐Intensity+Endurance+Training+on+Aerobic+Fitness+and+Risk.md`
  - 只完整處理此一篇來源；未混入 `What-Is-Zone-2-Training`、Matomäki 2025 perspective 或 clinical exercise physiology standards source。
- 新增來源摘要：
  - `09_來源摘要/Nuuttila_2026_low_intensity_endurance_training_meta_analysis.md`
- 新增頁面：
  - `05_Exercise_Physiology/Low_Intensity_Endurance_Training_健康成人證據邊界.md`
- 更新頁面：
  - `05_Exercise_Physiology/Zone_2_Training_證據邊界.md`
  - `05_Exercise_Physiology/Training_Intensity_Distribution.md`
  - `index.md`（Total pages 587 -> 589；新增 Nuuttila source summary 與 LIT healthy adults concept）
  - `log.md`
- 抽出概念：
  - Low-Intensity Endurance Training evidence boundary in healthy working-age adults：LIT 在 healthy sedentary / untrained adults 可改善 aerobic fitness，尤其 VO2max / Pmax；cardiometabolic risk marker effects 較小且異質性較高；upper LIT 可能較有利 VO2max，但不是 Zone 2 universal superiority。
- 本輪直接事實：
  - Source 為 2026 *Scandinavian Journal of Medicine & Science in Sports* systematic review and meta-analysis。
  - Protocol registered at PROSPERO CRD42023469528。
  - Included randomized controlled trials in adults aged 18-65 years。
  - Excluded diagnosed diseases / disorders、cardiometabolic medication、pregnancy、BMI >35 kg/m2、nutrition intervention、ergogenic modalities、pharmacologic agents。
  - LIT eligibility required training exclusively below LT1 / VT1, or <=60% VO2max, <=60% VO2 reserve, <=75% HRmax, or <=60% HRR when thresholds were not used。
  - Search used PubMed and SPORTDiscus, English-language human studies, publication dates before 2023-10-31。
  - 9702 records screened；50 studies included。
  - 54 intervention groups and 50 control groups。
  - 824 participants in intervention groups and 708 in control groups。
  - Participants were mainly sedentary or untrained；no included studies reported trained / competitive athlete results。
  - Mean intervention age 35.5 +/- 12.5 years；control age 33.2 +/- 11.8 years。
  - Exercise intensity was reported by %HRmax in 21 studies, %VO2max in 20 studies, and %HRR in eight studies。
  - Only one study used LT1 or VT1 for exercise intensity determination。
  - Mean training frequency 3.8 +/- 1.1 sessions/week；mean session duration 41 +/- 13 min；mean intervention length 12.2 +/- 5.7 weeks。
  - Risk of bias: 86% some concerns, 14% high risk。
  - Relative VO2max ES 0.94, 95% CI 0.74-1.13。
  - Absolute VO2max ES 0.84, 95% CI 0.36-1.33。
  - Pmax ES 1.09, 95% CI 0.86-1.31。
  - VT1 ES 0.74, 95% CI 0.26-1.22。
  - Cardiometabolic effects were small for total cholesterol, LDL, HDL, triglycerides, SBP and DBP；glucose effect was trivial。
  - Training intensity within LIT was associated with relative and absolute VO2max response; meta-regression supported intensity dependence only for relative VO2max。
  - Sex and baseline BMI did not significantly modify assessed outcomes。
  - GRADE certainty high for VO2max and Pmax, moderate for VT1 / total cholesterol / LDL / DBP, low for HDL / glucose / triglycerides / SBP。
- 發現衝突：
  - 與「低強度 endurance training 對 untrained adults 沒有效」衝突。
  - 與「只有 high intensity 才能改善 cardiometabolic risk markers」衝突。
  - 與「fixed %HRmax / %VO2max 等同 LT1 / VT1」衝突。
  - 與「本來源證明 Zone 2 是 universal optimal intensity」衝突。
- 待追蹤問題：
  - `What-Is-Zone-2-Training` 屬 expert viewpoint / commentary，若要處理需下一輪單一來源 ingest，不能混入本來源。
  - Matomäki 2025 `Why low-intensity endurance training for athletes?` 是 perspective and athlete-focused hypothesis source，需獨立處理。
  - `International Professional Practice Standards for Clinical Exercise Physiology` 是 consensus statement，可作 clinical exercise physiology professional standards 主題的後續來源。

## [2026-05-09] ingest | Reeves et al. 2026 - International Clinical Exercise Physiology Professional Standards

- 本輪單一來源：
  - `C:\原始資料\s40279-026-02407-6\s40279-026-02407-6.md`
  - 只完整處理此一篇 consensus statement；未混入 `What-Is-Zone-2-Training`、Matomäki 2025 perspective 或 Nuuttila 2026 LIT meta-analysis。
- 新增來源摘要：
  - `09_來源摘要/Reeves_2026_clinical_exercise_physiology_professional_standards.md`
- 新增頁面：
  - `02_方法學/Clinical_Exercise_Physiology_Professional_Standards.md`
- 更新頁面：
  - `02_方法學/治療性運動處方.md`
  - `02_方法學/治療性運動處方的最低必要欄位.md`
  - `index.md`（Total pages 589 -> 591；新增 Reeves source summary 與 Clinical Exercise Physiology professional standards concept）
  - `log.md`
- 抽出概念：
  - Clinical Exercise Physiology Professional Standards：以 modified e-Delphi consensus 建立 Clinical Exercise Physiologist 在 health-profession context 中執行 exercise-based care 的最低國際能力框架；核心不是某個 exercise protocol，而是 scope、ethics、documentation、cultural safety、risk management、foundational knowledge、assessment/client management 與 evidence-based intervention delivery。
- 本輪直接事實：
  - Source 為 2026 *Sports Medicine* consensus statement。
  - Accepted 2026-02-03。
  - Objective 是發展 international professional standards for clinical exercise physiologists。
  - Method 為 modified e-Delphi model，包含 online surveys、focus groups、steering committee、expert working group 與 external stakeholder feedback。
  - Steering committee members n = 4。
  - Expert working group recruited n = 21。
  - Round completion：round 1a n = 19；round 1b n = 13；round 2a/b n = 15；round 3 n = 14。
  - Consensus threshold 預設為 80% agreement on 7-9 points of 9-point Likert scale。
  - Final standards 包含 4 domains：professional practice、foundational knowledge、assessment and client management、case formulation and design/delivery of evidence-based interventions。
  - Final standards 包含 20 elements。
  - 18 of 20 final elements reached consensus as core。
  - Reflective practice 與 self-management strategy 未達 80% inclusion threshold，但 steering committee 保留。
  - External stakeholder feedback received from 27 individuals from seven countries。
  - Limitations：majority experts derived from ICSESP network（15/21, 71%）；all but one expert from western countries，可能限制 cultural / regional transferability。
- 發現衝突：
  - 與「exercise prescription 只要 FITT」衝突。
  - 與「clinical exercise delivery 可以不處理 contraindications、risk management、documentation、referral 或 medications effects」衝突。
  - 與「professional standards 等於特定 intervention 療效證據」衝突。
  - 與「international consensus 可直接取代 local licensure / scope of practice」衝突。
- 待追蹤問題：
  - `What-Is-Zone-2-Training` 仍可作下一輪低層級 expert viewpoint 單一來源 ingest。
  - Matomäki 2025 athlete-focused LI training perspective 仍需獨立處理。
  - 若要在台灣臨床制度下使用 Clinical Exercise Physiology standards，需另行整理本地法規、職類邊界與院內治理條件；本來源不能直接回答。

## [2026-05-09] ingest | Sitko et al. 2025 - What Is Zone 2 Training expert viewpoint

- 本輪單一來源：
  - `C:\原始資料\What-Is-Zone-2-Training\What-Is-Zone-2-Training.md`
  - 只完整處理此一篇 expert viewpoint / commentary；未混入 Storoschuk 2025 narrative review、Nuuttila 2026 meta-analysis 或 Matomäki 2025 perspective。
- 新增來源摘要：
  - `09_來源摘要/Sitko_2025_zone2_training_expert_viewpoint.md`
- 新增頁面：
  - `05_Exercise_Physiology/Zone_2_Training_實務定義與監測.md`
- 更新頁面：
  - `05_Exercise_Physiology/Zone_2_Training_證據邊界.md`
  - `05_Exercise_Physiology/Training_Intensity_Distribution.md`
  - `index.md`（Total pages 591 -> 593；新增 Sitko source summary 與 Zone 2 practical definition / monitoring concept）
  - `log.md`
- 抽出概念：
  - Zone 2 practical definition and monitoring：expert panel 將 Zone 2 實務定位於 immediately below LT1 / VT1，並建議用 HR、RPE、breathing / talk cue、lactate、power relative to critical power 與 internal-load drift 監測；此為 prescription / communication framework，不是 superiority evidence。
- 本輪直接事實：
  - Source 為 expert viewpoint / commentary。
  - Expert panel 包含 14 位 applied sport scientists and professional coaches。
  - Expert panel 代表 8 countries。
  - Panel focus 為 cycling。
  - Lead authors used PubMed and MEDLINE to identify relevant peer-reviewed articles on training intensity distribution and zones in cycling。
  - 12 experts reported using a 5-zone model for aerobic intensity distribution。
  - LT1 or VT1 separated zones 1 and 2；LT2 or VT2 / RCP separated zones 2 and 3。
  - Experts located Zone 2 just below LT1 / VT1。
  - Expected profile：blood lactate around 1-2 mmol/L、HR about 70-80% HRmax or 80-90% LT1 HR、Borg RPE around 10、power about 75-80% critical power。
  - Table I-2 described comfortable effort、CR10 RPE 2-3、Borg RPE 9-12、about 67-82% HRmax、conversation with some effort、blood lactate around 1.0-2.0 mmol/L。
  - Experts emphasized monitoring HR and RPE when sessions are prescribed by external load because long sessions can show divergence between internal and external loads。
  - The source identified continuous、variable continuous and interval-based Zone 2 methods。
  - Continuous preferred method was long rides, ideally >2 h。
  - If cardiac drift or fatigue causes HR/RPE to rise disproportionately, the recommendation is to maintain HR/RPE within Zone 2 even if external load must be reduced。
  - Expected adaptations included capillarization、mitochondrial enzymes in type I fibers、metabolic efficiency、modest critical power and VO2max increase、LT1 / VT1 compression toward LT2 / VT2。
  - The source states research is needed to confirm these adaptation hypotheses。
  - The source states expected adaptations are likely not unique to Zone 2 and could also be induced by slightly higher or lower intensities。
- 發現衝突：
  - 與「Zone 2 只要看固定 HRmax 百分比」衝突。
  - 與「長時間 session 只守 external load 就能保證相同 physiological intensity」衝突。
  - 與「Zone 2 adaptations 是獨有的」衝突。
  - 與「expert viewpoint 可證明 Zone 2 優於其他強度」衝突。
- 待追蹤問題：
  - Matomäki 2025 athlete-focused LI training perspective 仍需獨立處理。
  - 若要做 Zone 2 synthesis，需先逐篇加入直接 Zone 2 intervention trials 或 systematic reviews。
  - 若要把 Zone 2 用於 chronic disease / rehabilitation population，需另行處理 disease-specific safety and progression sources。

## [2026-05-09] ingest | Matomäki 2025 - Why low-intensity endurance training for athletes?

- 本輪單一來源：
  - `C:\原始資料\s00421-025-05843-w\s00421-025-05843-w.md`
  - 只完整處理此一篇 perspective / hypothesis article；未混入 Sitko 2025 expert viewpoint、Nuuttila 2026 meta-analysis 或其他 LI / Zone 2 sources 的未標示內容。
- 新增來源摘要：
  - `09_來源摘要/Matomaki_2025_low_intensity_endurance_training_athlete_hypotheses.md`
- 新增頁面：
  - `05_Exercise_Physiology/Low_Intensity_Endurance_Training_運動員假說框架.md`
- 更新頁面：
  - `05_Exercise_Physiology/Training_Intensity_Distribution.md`
  - `index.md`（Total pages 593 -> 595；新增 Matomäki source summary 與 athlete LI hypothesis framework concept）
  - `log.md`
- 抽出概念：
  - Low-Intensity Endurance Training 運動員假說框架：Matomäki 2025 將高階 endurance athletes 大量累積 LI training 的現象描述為 athlete LI paradox，並提出七個非互斥假說：low-stress maintenance、alternative molecular signals、long-term structural remodeling、unmeasured components、psychological need、strengthening HI adaptations、possible replaceability。
- 本輪直接事實：
  - Source 為 2025 *European Journal of Applied Physiology* perspective article。
  - Received 2025-01-09；accepted 2025-05-16；published online 2025-06-27。
  - Source 中 athlete 定義為至少 McKay Tier 3：national-level competition、within 20% of world record、structured and periodized training。
  - Source 指出 high-level endurance athletes 通常將多數 training time 放在 LI zone。
  - Source 指出對已有 training history 的 athletes，單次 LI exercise 通常不如 MI / HI 明顯挑戰 cardiopulmonary system、homeostasis 或 metabolic perturbation。
  - Source 提出七個假說，且明確說明這些 hypotheses are not all mutually exclusive。
  - Source 定義 exercise 為單次 planned endurance session；training 為多次 exercise 長期系統化累積。
  - Source 指出 HI cardiac autonomic recovery 可能超過兩天；typical LI exercise recovery 常低於 24 小時，甚至數小時。
  - Source 將 LI zone 以 physiological thresholds 定義，並指出 HR、velocity 或 race pace anchoring 會改變 training intensity distribution 計算。
  - Source 指出 untrained individuals 沒有同樣 LI paradox，因為 LI training 仍可能充分挑戰 cardiopulmonary system 並改善 VO2max 與 threshold intensity。
- 發現衝突：
  - 與「LI 對 athlete 急性刺激低，所以一定無用」衝突。
  - 與「elite athletes 做很多 LI，所以 LI 必然已被證明最佳或不可替代」衝突。
  - 與「athlete TID 可以直接套用到 untrained adults 或 clinical populations」衝突。
  - 與「Zone 2 / LI popular claim 已有 superiority proof」衝突。
- 待追蹤問題：
  - 若要建立 Zone 2 / LI synthesis，仍需逐篇加入 intervention trials、systematic reviews 或 athlete-specific longitudinal studies。
  - 需要另行整理 high-volume LI 對 durability、recovery ability、movement economy、fat oxidation capacity、threshold intensities 與 mitochondrial mass 的直接證據。
  - 若要應用到 PM&R / cardiopulmonary rehabilitation，需使用 clinical population-specific safety and prescription sources，不能由本 athlete perspective 直接外推。

## [2026-05-09] ingest | UpToDate - Overview of secondary prevention of ischemic stroke

- 本輪單一來源：
  - `C:\原始資料\Overview of secondary prevention of ischemic stroke.md`
  - 只完整處理此一篇 UpToDate topic review；未混入 `Long-term antithrombotic therapy for the secondary prevention of ischemic stroke`、`Antihypertensive therapy for secondary stroke prevention` 或其他 stroke-specific cause topics。
- 新增來源摘要：
  - `09_來源摘要/UpToDate_overview_secondary_prevention_ischemic_stroke.md`
- 新增頁面：
  - 無；本輪更新既有 clinical concept。
- 更新頁面：
  - `03_疾病與臨床主題/中風次發預防.md`
  - `index.md`（Total pages 595 -> 596；新增 UpToDate secondary prevention source summary）
  - `log.md`
- 抽出概念：
  - Ischemic stroke secondary prevention bundle：ischemic stroke / TIA 後應同時處理 antithrombotic therapy、blood pressure reduction、LDL-C lowering therapy、diabetes control、lifestyle modification 與 selected mechanism-specific interventions，而不是只選 antiplatelet 或 anticoagulation。
- 本輪直接事實：
  - Source 為 UpToDate official reprint / topic review。
  - Literature review current through April 2026。
  - Topic last updated 2025-10-13。
  - Topic version 1120 Version 71.0。
  - Most patients with ischemic stroke or TIA should receive antithrombotic therapy、blood pressure reduction、LDL-C lowering therapy 與 lifestyle modification。
  - Major treatable risk factors include hypertension、dyslipidemia、diabetes、smoking、physical inactivity。
  - Source estimates treatment of all major stroke risk factors could reduce recurrent stroke risk by 80 percent compared with no treatment。
  - Noncardioembolic ischemic stroke / TIA long-term antiplatelet options include aspirin 50-100 mg daily、clopidogrel 75 mg daily、aspirin-extended-release dipyridamole 25/200 mg twice daily。
  - Early short-term DAPT is beneficial for select high-risk TIA or minor ischemic stroke and may benefit recently symptomatic intracranial large artery atherosclerosis。
  - Chronic nonvalvular atrial fibrillation after ischemic stroke / TIA should receive long-term anticoagulation with warfarin or DOAC in most patients。
  - 2021 AHA/ASA guideline target cited by the source is office BP <130/80 mmHg for most patients to reduce recurrent stroke and vascular events。
  - Acute ischemic stroke first hours / days should not be treated by rapidly lowering BP to the long-term target because BP may support collateral perfusion。
  - High-intensity statin therapy such as atorvastatin 80 mg/day is used for ASCVD including TIA or ischemic stroke, aiming for LDL-C <70 mg/dL。
  - If LDL-C remains >=70 mg/dL despite maximally tolerated statin therapy, ezetimibe or PCSK9 inhibitor is reasonable。
  - For most patients with diabetes, A1C goal <=7 percent is reasonable。
  - Homocysteine-lowering vitamins are not beneficial for secondary prevention of cardiovascular disease or stroke; routine homocysteine / vitamin screening is not recommended。
- 發現衝突：
  - 與「stroke secondary prevention = antiplatelet」衝突。
  - 與「所有 ischemic stroke 長期都用 DAPT」衝突。
  - 與「acute stroke BP 高就立刻壓到 <130/80」衝突。
  - 與「statin 開立後不用追 LDL-C 或調整」衝突。
  - 與「weight reduction 已直接證明降低 recurrent stroke」衝突。
- 待追蹤問題：
  - `Long-term antithrombotic therapy for the secondary prevention of ischemic stroke` 可作下一輪 antithrombotic-specific 單一來源。
  - `Antihypertensive therapy for secondary stroke prevention` 可作下一輪 BP-specific 單一來源。
  - `Overview of secondary prevention for specific causes of ischemic stroke and transient ischemic attack` 可作 mechanism-specific prevention 單一來源。

## [2026-05-09] ingest | UpToDate - Long-term antithrombotic therapy for the secondary prevention of ischemic stroke

- 本輪單一來源：
  - `C:\原始資料\Long-term antithrombotic therapy for the secondary prevention of ischemic stroke.md`
  - 只完整處理此一篇 UpToDate topic review；未混入 `Early antithrombotic treatment of acute ischemic stroke and transient ischemic attack`、AF oral anticoagulant 專題、BP-specific 專題或 specific-cause secondary prevention 專題。
- 新增來源摘要：
  - `09_來源摘要/UpToDate_long_term_antithrombotic_secondary_prevention_ischemic_stroke.md`
- 新增頁面：
  - `03_疾病與臨床主題/Ischemic_Stroke_Long_term_Antithrombotic_Therapy.md`
- 更新頁面：
  - `03_疾病與臨床主題/中風次發預防.md`
  - `index.md`（Total pages 596 -> 598；新增 long-term antithrombotic source summary 與 antithrombotic concept page）
  - `log.md`
- 抽出概念：
  - Ischemic stroke long-term antithrombotic therapy：post-acute ischemic stroke / TIA 的 antithrombotic selection 應先依 phase 與 mechanism 分流；noncardioembolic long-term default 是 single antiplatelet，而不是 indefinite DAPT；AF/LV thrombus 等才走 anticoagulation pathway；selected nonlacunar systemic atherosclerosis patients 才考慮 aspirin + low-dose rivaroxaban。
- 本輪直接事實：
  - Source 為 UpToDate official reprint / topic review。
  - Literature review current through April 2026。
  - Topic last updated 2026-05-01。
  - Antiplatelet therapy for secondary stroke prevention is reviewed here；acute antithrombotic treatment and primary prevention are separate topics。
  - For noncardioembolic stroke / TIA of atherothrombotic, lacunar, or cryptogenic type, source recommends antiplatelet therapy using aspirin、clopidogrel、or aspirin-extended-release dipyridamole。
  - Source suggests clopidogrel 75 mg daily monotherapy or aspirin-extended-release dipyridamole 25/200 mg twice daily rather than aspirin alone when feasible。
  - Aspirin remains appropriate when clopidogrel or aspirin-extended-release dipyridamole is not affordable, tolerated, or appropriate。
  - Aspirin dose for secondary prevention is recommended as 50-100 mg daily by the source。
  - Cilostazol is a reasonable option for patients of East Asian ethnicity and when other agents are unavailable or not tolerated；non-East Asian data are very limited。
  - For most noncardioembolic stroke / TIA patients, source recommends against long-term aspirin plus clopidogrel because added efficacy is lacking and bleeding risk rises。
  - Carotid endarterectomy patients usually receive aspirin 81-325 mg daily monotherapy started before surgery and continued indefinitely unless anticoagulation is separately indicated。
  - Carotid stenting patients usually receive aspirin plus clopidogrel for 30 days, followed by long-term single-agent antiplatelet therapy。
  - Cryptogenic stroke, including ESUS, is generally not an indication for anticoagulation；antiplatelet therapy is preferred in most such cases。
  - For high-risk noncardioembolic, nonlacunar stroke with systemic atherosclerosis, aspirin plus low-dose rivaroxaban 2.5 mg BID is a reasonable selected option。
  - Routine laboratory or genetic testing for aspirin / clopidogrel resistance after antiplatelet treatment failure has no proven role in this source。
- 發現衝突：
  - 與「minor stroke / high-risk TIA short-term DAPT 有效，所以可以長期 DAPT」衝突。
  - 與「cryptogenic / ESUS 看起來 embolic，所以 routine anticoagulation」衝突。
  - 與「CYP2C19 或 platelet function testing 應成為所有 clopidogrel 使用者的 routine」衝突。
  - 與「所有 post-stroke systemic atherosclerosis 都應 aspirin + rivaroxaban」衝突。
- 待追蹤問題：
  - `Early antithrombotic treatment of acute ischemic stroke and transient ischemic attack` 可另作 acute / short-term DAPT 單一來源。
  - `Atrial fibrillation in adults: Use of oral anticoagulants` 或對應 stroke/AF source 可另作 cardioembolic anticoagulation 單一來源。
  - `Antihypertensive therapy for secondary stroke prevention` 可作下一輪 BP-specific 單一來源。
  - Factor XIa inhibitors 需要日後依 guideline / regulatory update 重新評估，不可由此篇直接視為 routine standard。

## [2026-05-09] concept extraction | Hayes, Goggins, Caldwell - Biomechanics of the Hip, Knee, and Ankle

- 本輪單一來源：
  - `C:\原始資料\Biomechanics of the hip, knee, and ankle\Biomechanics of the hip, knee, and ankle.md`
  - 本來源摘要已存在；本輪不重複建立新 source summary，而是補強既有摘要並拆出 missing concept page。
  - 未混入 `Lower limb orthoses`、`Foot biomechanics`、`Clinical assessment of walking and running gait` 或 running injury sources。
- 補強來源摘要：
  - `09_來源摘要/Biomechanics_of_the_Hip_Knee_and_Ankle.md`
- 新增頁面：
  - `06_Gait_Biomechanics/髖膝踝生物力學與GRF.md`
- 更新頁面：
  - `06_Gait_Biomechanics/下肢矯具總論.md`
  - `index.md`（Total pages 598 -> 599；新增 lower-limb joint biomechanics / GRF concept page）
  - `log.md`
- 抽出概念：
  - 髖膝踝生物力學與GRF：stance phase 中 shank / thigh / foot segment kinematics 決定 GRF 相對於 ankle、knee、hip 的 line of action，進而產生 external joint moments；orthosis-footwear combination 的治療作用不是單純固定，而是同時透過 direct force system 與 indirect GRF manipulation 重新配置這條力學鏈。
- 本輪直接事實：
  - Source 為 textbook chapter，source_tier 1。
  - Source 將 biomechanics 分為 statics 與 dynamics；dynamics 包含 kinematics 與 kinetics。
  - Three-point force system 是控制單一關節 angular motion 的最小力學模型；相鄰兩關節可共享部分 counterforces。
  - GRF 分析需看 point of application、magnitude、line of action。
  - Normal stance phase 中 shank 從 reclined 轉為 inclined；midstance 約 10-12 degrees forward shank inclination 對 stability 重要。
  - Shank 與 thigh inclination 共同決定 GRF 相對於 knee / hip 的 alignment，並影響 external extension / flexion moments。
  - Terminal stance support 需要 ankle plantarflexion / forefoot loading 將 GRF point of application 前移，以協助 knee / hip extension moments。
  - Gastrocnemius contracture 可讓 ankle dorsiflexion 和 knee extension 形成 length competition；允許 dorsiflexion 不一定有利於 knee extension。
  - Footwear 的 pitch、heel design、sole stiffness、sole profile 會影響 orthosis 的 kinematic / kinetic effects。
  - Orthoses must be dynamically tuned；小幅度 orthosis alignment 或 footwear design 改變可顯著影響 gait mechanics。
- 發現衝突：
  - 與「AFO 只是固定 ankle」衝突。
  - 與「hinged AFO 必然比 fixed AFO 更接近正常 gait」衝突。
  - 與「knee hyperextension 直接加強 knee brace 就好」衝突。
  - 與「鞋子只是配件，不屬於下肢矯具處方」衝突。
- 待追蹤問題：
  - 可用 `Lower limb orthoses` 另做 AFO / KAFO prescription-specific concept refinement。
  - 可用 `Clinical assessment of walking and running gait` 另補 bedside gait observation 與 video gait analysis 的評估流程。
  - 若要處理 pediatric CP / neurologic gait，需要逐篇加入 disease-specific orthotic evidence，不能只由本 biomechanics chapter 外推。

## [2026-05-09] concept extraction | Murphy, Lovegreen, Lovegreen - Lower Limb Orthoses | AFO prescription

- 本輪單一來源：
  - `C:\原始資料\13 - Lower limb orthoses\13 - Lower limb orthoses.md`
  - 本來源摘要已存在；本輪不重複建立新 source summary，而是補強既有摘要並拆出 AFO-specific concept page。
  - 未混入 `Biomechanics of the hip, knee, and ankle`、`Clinical assessment of walking and running gait`、`Foot biomechanics` 或 disease-specific AFO outcome studies。
- 補強來源摘要：
  - `09_來源摘要/Lower_limb_orthoses.md`
- 新增頁面：
  - `06_Gait_Biomechanics/AFO處方生物力學.md`
- 更新頁面：
  - `06_Gait_Biomechanics/下肢矯具總論.md`
  - `index.md`（Total pages 599 -> 600；新增 AFO prescription biomechanics concept page）
  - `log.md`
- 抽出概念：
  - AFO prescription biomechanics：AFO 不只是 foot-drop device；它可透過 ankle position、ankle stops、foot plate 與 shoe-ground interaction 改變 GRF 相對於 knee axis 的位置，進而控制 stance phase knee flexion / extension moment。
- 本輪直接事實：
  - Source 為 textbook chapter，source_tier 1。
  - AFO 是跨過 ankle joint、但止於 knee joint 以下的 orthosis。
  - AFO 可用於 biomechanical 或 neurophysiological foot / ankle problem。
  - AFO 提供 dorsiflexion / plantarflexion control，也提供 mediolateral stability。
  - AFO 直接控制 ankle motion，但也會影響 gait 中的 knee control。
  - Foot strike 時，若 GRF 位於 knee 後方，會傾向促進 knee flexion；若 GRF 位於 knee 前方，會協助 knee extension。
  - Foot dorsiflexion 傾向讓 GRF 位於 knee 後方並增加 knee flexion tendency。
  - Foot plantarflexion 傾向讓 GRF 位於 knee 前方並增加 knee extension tendency。
  - 對 quadriceps weakness 且 stance 有 knee collapse tendency 的人，dorsiflexion stop 可調向較 plantarflexed 的 stance position，使 GRF 移到 knee axis 前方以幫助 knee extension。
  - 對 stance phase knee hyperextension 的人，plantarflexion stop 可調整使 ankle 保持較 dorsiflexed，使 GRF 移到 knee 後方，以鼓勵 knee flexion 並減少 hyperextension。
  - Source 提醒 correction of one issue may leave other issues less well attended to；rigid brace 可能保護 wound / fracture，但增加 walking difficulty 與 energy expenditure。
  - Orthotic checkout 需確認 fit、function、comfort、cosmesis；若目標是改善 gait dysfunction，必須重新評估 gait 是否真的達成目標。
- 發現衝突：
  - 與「AFO 只是 foot drop brace」衝突。
  - 與「hinged AFO 一定比 fixed AFO 更好」衝突。
  - 與「dorsiflexion 越多越自然、越好」衝突。
  - 與「knee hyperextension 只能用 knee brace 處理」衝突。
- 待追蹤問題：
  - 可用同一來源另拆 `KAFO stance-control biomechanics`，但本輪未處理，避免把 AFO 與 KAFO 混成同一概念頁。
  - 可用 `Clinical assessment of walking and running gait` 補上 AFO checkout 前後的 observation / video gait analysis workflow。
  - 若要應用到 stroke、CP、SCI 或 peripheral neuropathy，需逐篇加入 disease-specific evidence，不能只由本 textbook chapter 外推療效。

## [2026-05-09] concept extraction | Murphy, Lovegreen, Lovegreen - Lower Limb Orthoses | KAFO stance-control

- 本輪單一來源：
  - `C:\原始資料\13 - Lower limb orthoses\13 - Lower limb orthoses.md`
  - 本來源摘要已存在；本輪不重複建立新 source summary，而是補強既有摘要並拆出 KAFO-specific concept page。
  - 未混入 `Biomechanics of the hip, knee, and ankle`、`Clinical assessment of walking and running gait`、HKAFO / powered exoskeleton 區段或 disease-specific KAFO outcome studies。
- 補強來源摘要：
  - `09_來源摘要/Lower_limb_orthoses.md`
- 新增頁面：
  - `06_Gait_Biomechanics/KAFO站立控制生物力學.md`
- 更新頁面：
  - `06_Gait_Biomechanics/下肢矯具總論.md`
  - `index.md`（Total pages 600 -> 601；新增 KAFO stance-control biomechanics concept page）
  - `log.md`
- 抽出概念：
  - KAFO stance-control biomechanics：KAFO 的 biomechanical target 是在 stance phase 提供 knee-ankle complex stability，同時盡量保留 swing phase knee motion，避免 locked-knee gait 造成 hip hiking、circumduction 或 contralateral vaulting。
- 本輪直接事實：
  - Source 為 textbook chapter，source_tier 1。
  - KAFO 被設計來提供 knee and ankle complex stability during ambulation。
  - KAFO 可能在 loading response 防止 excessive knee flexion，也可能在 midstance-to-terminal stance 防止 knee hyperextension。
  - 理想 KAFO 應提供 required stability while minimally interfering with normal knee and ankle ROM during gait。
  - KAFO 可用於 functional ambulation、exercise，或兩者；部分使用者仍需 wheelchair 作 longer-distance mobility。
  - KAFO ambulation 通常需要 good trunk control 與 upper body strength，因為常搭配 walkers 或 forearm crutches。
  - Posterior offset knee joint 在 swing phase 允許 knee free flexion / extension；stance phase 則藉 posterior offset 讓 orthotic GRF 維持在 knee axis 前方以提供 stability。
  - Stance-control lock mechanisms 在 stance phase lock，但允許 swing phase knee flexion / extension。
  - Dynamic control systems 可在 stance 與 swing phases 提供不同程度的 knee motion control。
  - Traditional locked-knee KAFO 可讓 very unstable knee 的人安全站立與行走，但 swing phase locked knee 會需要 hip hiking、circumduction 或 contralateral vaulting。
  - Source 指出 stance control 與 dynamic knee control units 的 benefits 包含 uneven terrain stability、reduced metabolic costs、減少 hip hiking / circumduction 等 gait deviations，可能降低 back 與 contralateral limb 長期 complications。
- 發現衝突：
  - 與「KAFO 越穩越好」衝突。
  - 與「locked-knee KAFO 只要能站穩就是成功」衝突。
  - 與「stance-control KAFO 可直接套用所有 KAFO 使用者」衝突。
  - 與「KAFO 只是 knee brace，不需要看 ankle-foot component 或 assistive device」衝突。
- 待追蹤問題：
  - 可用 `Clinical assessment of walking and running gait` 補上 KAFO / AFO checkout 前後的 observation / video gait analysis workflow。
  - 若要應用到 stroke、SCI、polio、peripheral neuropathy 或 myopathy，需逐篇加入 disease-specific evidence，不能只由本 textbook chapter 外推療效。
  - HKAFO / reciprocating gait orthosis 與 powered exoskeleton 應另拆概念頁，本輪未處理。

## [2026-05-09] ingest | Dang - Biomechanics of the Foot and Ankle

- 本輪單一來源：
  - `C:\原始資料\Biomechanics of the Foot and Ankle\Biomechanics of the Foot and Ankle.md`
  - 本來源摘要已存在舊短版；本輪依單一來源 workflow 補強為正式 source summary，並拆出 one-concept page。
  - 未混入 `Foot biomechanics`、`Overview of foot anatomy and biomechanics and assessment of foot pain in adults`、running shoe sources 或 disease-specific treatment sources。
- 更新來源摘要：
  - `09_來源摘要/Biomechanics_of_the_Foot_and_Ankle.md`
- 新增頁面：
  - `06_Gait_Biomechanics/足部柔性到剛性轉換.md`
- 更新頁面：
  - `06_Gait_Biomechanics/足部解剖與生物力學.md`
  - `index.md`（Total pages 601 -> 602；新增 foot supple-to-rigid transition concept page）
  - `log.md`
- 抽出概念：
  - 足部柔性到剛性轉換：stance phase 中 foot 由 heel strike 的 supple shock absorber，透過 hindfoot eversion / inversion、transverse tarsal unlocking / locking、plantar aponeurosis / windlass mechanism 與 forefoot loading，轉為 terminal stance 的 rigid lever。
- 本輪直接事實：
  - Source 為 textbook chapter，source_tier 1。
  - Walking gait cycle 中 stance phase 約 62%，swing phase 約 38%。
  - Stance phase 可分為 three intervals：heel strike to foot flat、foot flat to heel rise、heel rise to toe-off。
  - Source 明確指出 foot 是 dynamic structure，不只是 rigid base。
  - Heel strike / loading response 需要 supple foot 來吸收 impact energy；end stance / toe-off 前 foot 需要轉成 rigid structure。
  - Subtalar joint 可被視為 oblique single-axis hinge / torque converter，把 leg rotation 轉換成 hindfoot inversion / eversion。
  - Calcaneus eversion 時，talonavicular / calcaneocuboid axes 較 parallel，transverse tarsal joint 較 flexible / unlocked。
  - Calcaneus inversion 時，這些 axes 較 nonparallel，transverse tarsal joint 較 rigid / locked。
  - Valgus hindfoot 傾向 unlocked and supple midfoot；varus hindfoot 傾向 locked and rigid midfoot；source 特別提醒 advanced adult acquired flatfoot deformity 不能直接套用 congenital pes planovalgus 推論。
  - Medial column 較 rigid，lateral column 較 supple。
  - Metatarsophalangeal break 的 oblique cascade 有助於 heel inversion 時仍讓 metatarsal heads 接觸地面並分散 forefoot load。
  - Plantar aponeurosis 是 heel rise to toe-off 間 longitudinal arch 最重要的 stabilizer。
  - Toe dorsiflexion 會拉緊 plantar aponeurosis，使 metatarsal heads depressed、longitudinal arch elevated，並促進 calcaneal inversion。
  - Posterior calf muscles 控制 tibia 在 fixed foot 上向前移動；weakness 會造成 stride length shortening。
  - Normal walking 中，center of pressure 由 heel 快速前移到 metatarsal region，停留約半個 stance phase，再移向 great toe。
  - Running stance phase 較短、vertical force 可達約 2.5-3 倍 body weight，joint ROM 與 muscle activity demand 增加。
- 發現衝突：
  - 與「foot 是 rigid base」衝突。
  - 與「flatfoot / high arch 靜態標籤足以解釋症狀」衝突。
  - 與「toe-off 是 toes active push-off」衝突。
  - 與「rigid foot 一定比 supple foot 好」衝突。
- 待追蹤問題：
  - `Foot biomechanics` 可另作單一來源，補 modern foot spring / transverse arch / intrinsic muscle model，但不能直接混進本來源結論。
  - `Overview of foot anatomy and biomechanics and assessment of foot pain in adults` 可另作 clinical assessment workflow。
  - 若要處理 plantar fasciitis、hallux valgus、metatarsalgia、diabetic ulcer 或 post-arthrodesis gait，需逐篇加入 disease-specific sources。

## [2026-05-09] ingest | Richie Jr. - Foot biomechanics

- 本輪單一來源：
  - `C:\原始資料\Foot biomechanics\Foot biomechanics.md`
  - 本來源摘要已存在舊版；本輪依單一來源 workflow 補強為正式 source summary，並拆出 one-concept page。
  - 未混入 `Biomechanics of the Foot and Ankle`、UpToDate foot assessment、running shoe sources、orthosis sources 或 disease-specific treatment sources。
- 更新來源摘要：
  - `09_來源摘要/Foot_biomechanics.md`
- 新增頁面：
  - `06_Gait_Biomechanics/足部扭轉彈簧機制.md`
- 更新頁面：
  - `06_Gait_Biomechanics/足部解剖與生物力學.md`
  - `index.md`（Total pages 602 -> 603；新增 foot torsional spring concept page）
  - `log.md`
- 抽出概念：
  - 足部扭轉彈簧機制：closed-chain stance 中 foot plate 先 untwist 以吸收能量與適應地面，再由 plantar aponeurosis、plantar intrinsic muscles、peroneus longus 與 first ray recoil 形成 terminal-stance twist / spring-like push-off。
- 本輪直接事實：
  - Source 為 textbook chapter，source_tier 1。
  - Source 將 talus 下方 foot bones 描述為 lamina pedis / calcaneopedal unit。
  - Open kinetic chain 與 closed kinetic chain 的 foot motion 不同；open-chain pronation / supination 不能直接等同 gait 中的 closed-chain behavior。
  - Closed-chain external leg rotation induces calcaneal inversion；internal leg rotation induces calcaneal eversion。
  - Closed-chain rearfoot and forefoot motions reciprocal coupling：external leg rotation 時 rearfoot supination / forefoot pronation；internal leg rotation 時 rearfoot pronation / forefoot supination。
  - Source 描述 transverse tarsal arch curvature 對 foot stiffness 的重要性，並指出 stiffness 不能只看 medial longitudinal arch。
  - Dynamic foot vault stability 由 plantar intrinsic muscles、plantar aponeurosis 與 plantar ligaments 調節。
  - Passive plantar ligament structures 可儲存 strain energy 並 elastic recoil，形成 foot spring。
  - Foot 在 stance 前半段 untwists 以吸收能量、分散衝擊與適應地面，之後 recoil / twists into rearfoot inversion and forefoot pronation。
  - Source 指出 arch height 在 final 15% of stance 明顯增加。
  - Source 指出 first ray 約從 terminal stance 開始到 pre-swing 結束有 15 degrees plantarflexion。
  - Heel rise 對應 maximal plantar fascia tensile strain 與 peak intrinsic muscle activity。
  - Peroneus longus 參與 first ray stiffening，並協助 load 從 lateral 轉向 medial、經 first MTP joint 參與 windlass mechanism。
  - Source 明確指出 windlass mechanism alone 不能完整解釋 terminal stance / pre-swing arch elevation and shortening。
- 發現衝突：
  - 與「foot propulsion = simple rigid lever」衝突。
  - 與「arch height alone explains foot function」衝突。
  - 與「windlass mechanism alone explains arch raising」衝突。
  - 與「open-chain foot ROM 可直接外推到 closed-chain gait」衝突。
  - Source 內部對 triceps surae / plantarflexor activity around pre-swing 的描述不完全一致，因此本輪只標記 uncertainty，不把 calf timing 寫成硬結論。
- 待追蹤問題：
  - 可另拆 `posterior tibialis transverse-plane stabilizer`，但本輪未處理，避免把 muscle moment analysis 混入 foot spring 概念頁。
  - 可另拆 `first ray terminal-stance stiffness`，但本輪未處理。
  - 若要應用到 adult acquired flatfoot deformity、plantar fasciitis、hallux valgus、metatarsalgia、diabetic neuropathy 或 post-arthrodesis gait，需逐篇加入 disease-specific sources。

## [2026-05-09] ingest | Approach to Nerve Conduction Studies, Electromyography, and Neuromuscular Ultrasound

- 本輪單一來源：
  - `C:\原始資料\Approach to Nerve Conduction Studies, Electromyography, and Neuromuscular Ultrasound\Approach to Nerve Conduction Studies, Electromyography, and Neuromuscular Ultrasound.md`
  - 本輪只處理此 textbook-style chapter；未混入 `Basic Nerve Conduction Studies`、`Repetitive Nerve Stimulation`、`Late Responses`、`Blink Reflex` 或 disease-specific EDX chapters。
- 新增來源摘要：
  - `09_來源摘要/Approach_NCS_EMG_Neuromuscular_Ultrasound.md`
- 新增頁面：
  - `02_方法學/EDX_定位導向檢查流程.md`
- 更新頁面：
  - `02_方法學/電生理診斷醫學.md`
  - `02_方法學/EDX_轉介問題設計.md`
  - `03_疾病與臨床主題/周邊神經病灶定位與EDX_US框架.md`
  - `index.md`（Total pages 603 -> 605；新增 EDX localization workflow concept page 與 source summary）
  - `log.md`
- 抽出概念：
  - EDX localization-first workflow：EDX study 應先由 brief history / directed neurologic examination 建立 differential diagnosis 與 localization hypothesis，再用 targeted NCS、needle EMG 與必要時 neuromuscular ultrasound 即時修正並輸出 clinical relevance。
- 本輪直接事實：
  - Source 為 textbook-style clinical chapter，source_tier 1。
  - EDX studies 包含 NCS、repetitive nerve stimulation、late responses、blink reflexes、needle EMG 與其他 specialized examinations。
  - NCS and needle EMG form the core of the EDX study，兩者互補，通常先做且提供最大 diagnostic information。
  - EDX studies serve as an extension of the clinical examination。
  - 每次 EDX study 應依 neurologic examination 與 differential diagnosis 個別化，並在檢查進行中依結果修正。
  - The principal goal of every EDX study is localization。
  - EDX 可先分 neuropathic、myopathic、NMJ、CNS，再進一步判斷 neuron / root / plexus / peripheral nerve、fiber type、demyelination vs axonal loss、severity 與 temporal course。
  - Patient encounter 應包含 brief history、directed physical examination、formulate differential diagnosis、formulate study、explain test、perform NCS、perform needle EMG。
  - NCS 結果會影響 needle EMG strategy 與 interpretation。
  - Cardinal rules 包含：EDX 是 clinical examination extension、疑問時先考慮 technical factors、必要時 reexamine patient、報告放回 clinical context、不要 overcall diagnosis、維持 clinical-electrophysiologic correlation。
  - Neuromuscular ultrasound 是 EDX 的 complementary tool，不取代 EDX。
  - EDX 提供 physiologic function；ultrasound 提供 anatomy / structural / possible etiologic information。
  - Ultrasound 在 mononeuropathy 可補 segmental localization / structural cause，在 demyelinating polyneuropathy 可補 hypertrophic pattern，在 pure lower motor neuron syndrome 可協助和 treatable motor neuropathy 鑑別，在 myopathy 可補 involvement pattern 與 biopsy target。
- 發現衝突：
  - 與「EDX 是固定 screening battery」衝突。
  - 與「NCS alone 足以處理多數 neuromuscular localization 問題」衝突。
  - 與「minor abnormal value 可直接等於臨床診斷」衝突。
  - 與「neuromuscular ultrasound 可以取代 EDX」衝突。
  - 與「structural imaging abnormality alone establishes symptom source」衝突。
- 待追蹤問題：
  - 可另處理 `Basic Nerve Conduction Studies`，補 NCS technical setup、waveform 與 normal values。
  - 可另處理 `Repetitive Nerve Stimulation`、`Late Responses`、`Blink Reflex`，拆成 specialized EDX testing concept pages。
  - 可另處理 `Artifacts and Technical Factors`，補 technical-error prevention 與 false positive framework。

## [2026-05-10] ingest | Basic Nerve Conduction Studies

- 本輪單一來源：
  - `C:\原始資料\Basic Nerve Conduction Studies\Basic Nerve Conduction Studies.md`
  - 本輪只處理此 textbook chapter；未混入 `Routine Upper Extremity, Facial, and Phrenic Nerve Conduction Techniques`、`Routine Lower Extremity Nerve Conduction Techniques`、`Repetitive Nerve Stimulation`、`Late Responses`、`Blink Reflex` 或 disease-specific EDX chapters。
- 新增來源摘要：
  - `09_來源摘要/Basic_Nerve_Conduction_Studies.md`
- 新增頁面：
  - `02_方法學/NCS_軸突損失與脫髓鞘判讀.md`
- 更新頁面：
  - `02_方法學/電生理診斷醫學.md`
  - `02_方法學/EDX_定位導向檢查流程.md`
  - `03_疾病與臨床主題/周邊神經病灶定位與EDX_US框架.md`
  - `index.md`（Total pages 605 -> 607；新增 basic NCS source summary 與 NCS axonal-vs-demyelinating concept page）
  - `log.md`
- 抽出概念：
  - NCS 軸突損失與脫髓鞘判讀：用 CMAP / SNAP 的 amplitude、latency、conduction velocity、area、duration、stimulation location 與 injury timing 區分 axonal loss、demyelination、conduction block、pseudo-conduction block 與 technical artifact。
- 本輪直接事實：
  - Source 為 textbook chapter，source_tier 1。
  - EDX 在 history 與 directed physical examination 後以 NCS 開始；needle EMG 通常在 NCS 後執行，因 NCS 結果會影響 needle EMG planning and interpretation。
  - Motor NCS 通常先做，因其 technical demand 較低、noise 影響較少，且可協助確認 nerve course、stimulation site、required current 與 sensory response absence 是否真實。
  - CMAP 代表 summated muscle fiber action potentials；SNAP 代表 summated sensory fiber action potentials。
  - Motor latency 包含 distal nerve conduction、NMJ transmission 與 muscle depolarization time，因此 motor conduction velocity 需 distal + proximal stimulation 才能計算。
  - Sensory conduction velocity 可由 one stimulation 的 onset latency 與 distance 計算；peak latency 易標記但不可計算 conduction velocity。
  - Latency / conduction velocity 主要反映 fastest conducting fibers；amplitude / area 反映 depolarized fiber population；duration 主要反映 synchrony / temporal dispersion。
  - Supramaximal stimulation 應讓 waveform plateau 後再增加 20-25% current；只因 response 落在 normal range 就停止加刺激是常見錯誤。
  - Axonal loss 的 primary abnormality 是 reduced amplitude，但 reduced amplitude 不必然等於 axonal loss。
  - Pure axonal loss 中 conduction velocity 不應低於 lower limit of normal 的 75%，distal latency 不應超過 upper limit of normal 的 130%。
  - Hyperacute axonal loss 可在前 3 天出現 pseudo-conduction block；Wallerian degeneration 完成後轉為典型 low amplitude pattern。
  - Source 描述 Wallerian degeneration 較早出現在 motor fibers（約 days 3-5），sensory fibers 較晚（約 days 6-10）。
  - Demyelination 造成 marked conduction slowing、marked distal latency prolongation 或 conduction block。
  - Source 指出 routine motor / sensory / mixed conduction velocity 若低於 arms 35 m/s 或 legs 30 m/s，除 rare regenerating nerve fibers after complete axonal injury 外，代表 unequivocal demyelination。
  - Sensory symptoms with normal SNAPs 應考慮 lesion proximal to the dorsal root ganglion，包括 root、spinal cord 或 brain lesion。
  - Proximal sensory stimulation 可因 normal temporal dispersion / phase cancellation 造成 SNAP amplitude / area 下降與 duration 增加。
  - Conduction block 判讀需看 stimulation site 與 block location；distal-to-recording block、inter-stimulation-site block 與 very proximal block 會產生不同 CMAP amplitude pattern。
  - Source 討論舊式 >20% CMAP amplitude / area drop 或 >15% duration increase 規則，但也指出 >50% CMAP area drop 更能區分 true electrophysiologic conduction block 與 temporal dispersion / phase cancellation alone。
  - Routine tibial motor study at popliteal fossa 是例外；normal subjects 可見 up to 50% amplitude drop，因此需謹慎稱為 conduction block。
  - Sensory studies 通常在 myopathy 與 NMJ disorders 正常；presynaptic NMJ disorders 可有 low resting CMAP amplitude 但 latency / conduction velocity normal，需 repetitive nerve stimulation 或 exercise testing 證明 transmission disorder。
- 發現衝突：
  - 與「low amplitude = axonal loss」衝突。
  - 與「normal SNAP 排除 sensory pathology」衝突。
  - 與「proximal CMAP drop 一定是 conduction block」衝突。
  - 與「NCS 是固定 routine panel」衝突。
  - 與「normal-range response 就代表 stimulation 技術合格」衝突。
- 待追蹤問題：
  - 可另處理 `Routine Upper Extremity, Facial, and Phrenic Nerve Conduction Techniques` 與 `Routine Lower Extremity Nerve Conduction Techniques`，補常規 nerve-specific protocol。
  - 可另處理 `Artifacts and Technical Factors`，補 false conduction block、submaximal stimulation、co-stimulation、temperature 與 anatomic variation。
  - 可另處理 `Repetitive Nerve Stimulation`，拆 NMJ transmission testing concept page。
  - 可另處理 `Late Responses` 與 `Blink Reflex`，補 proximal segments / reflex arc testing。

## [2026-05-10] ingest | Artifacts and Technical Factors

- 本輪單一來源：
  - `C:\原始資料\Artifacts and Technical Factors\Artifacts and Technical Factors.md`
  - 本輪只處理此 textbook chapter；未混入 `Anomalous Innervations`、`Routine Upper Extremity, Facial, and Phrenic Nerve Conduction Techniques`、`Routine Lower Extremity Nerve Conduction Techniques` 或 disease-specific EDX chapters。
- 新增來源摘要：
  - `09_來源摘要/Artifacts_and_Technical_Factors.md`
- 新增頁面：
  - `02_方法學/EDX_技術假象與品質控制.md`
- 更新頁面：
  - `02_方法學/電生理診斷醫學.md`
  - `02_方法學/EDX_定位導向檢查流程.md`
  - `02_方法學/NCS_軸突損失與脫髓鞘判讀.md`
  - `index.md`（Total pages 607 -> 609；新增 artifacts / technical factors source summary 與 EDX technical quality-control concept page）
  - `log.md`
- 抽出概念：
  - EDX 技術假象與品質控制：在判讀 NCS / EMG 前，必須系統性確認 temperature、age、height、impedance、filters、stimulation、recording montage、distance、limb position 與 display settings，避免把 technical artifact 誤診為 neuropathy、entrapment、axonal loss、demyelination 或 conduction block。
- 本輪直接事實：
  - Source 為 textbook chapter，source_tier 1。
  - EDX study 的價值取決於 correct data collection 與 correct data interpretation；若資料本身 technical inaccurate，後續 interpretation 無法補救。
  - EDX 訊號是 microvolt / millivolt 等級的小 bioelectric signals，因此容易受 physiologic 與 nonphysiologic factors 影響。
  - Failure to recognize technical factors 可造成 type I errors 與 type II errors；source 強調 type I errors 對病人尤其嚴重，因為可能導致不必要檢查與治療。
  - Physiologic factors 包含 temperature、age、height、proximal vs distal nerve segments、anomalous innervations。
  - Nonphysiologic factors 包含 electrode impedance mismatch / 60-Hz interference、filters、electronic averaging、stimulus artifact、cathode position、supramaximal stimulation、co-stimulation、electrode placement、recording method、recording electrode distance、limb position / distance measurement、sweep speed / sensitivity。
  - Temperature 是 source 描述最重要的 physiologic factor。
  - Cooler temperature 會造成 slowed conduction velocity、prolonged distal latency、increased CMAP / SNAP amplitude and duration；SNAP effect 通常比 CMAP 更明顯。
  - 在約 21-34°C 範圍內，conduction velocity 每下降 1°C 約慢 1.5-2.5 m/s，distal latency 約延長 0.2 ms/°C。
  - Cool limb 可模仿 polyneuropathy、distal entrapment neuropathy，或使 axonal neuropathy 速度慢到 demyelinating range。
  - Distal limb temperature 應 routinely recorded and monitored，理想維持 32-34°C。
  - Profound cooling 時 underlying nerve temperature 可能需 20-40 分鐘才 equilibrate。
  - Source 偏好 warming / rewarming，而非單靠 correction factor，因 correction factors 多由 normal nerves 推導。
  - Full-term infant conduction velocity 約 25-30 m/s 可屬正常，但用 adult standard 會落入 demyelinating range。
  - Adult >60 歲 conduction velocity 每 decade 約下降 0.5-4.0 m/s；advanced age 也會明顯降低 SNAP amplitude。
  - Taller individuals 與 lower extremity nerves 的 conduction velocity 較慢；late responses 應使用 height / limb length norms。
  - Electrode impedance mismatch 會降低 common mode rejection，使 60-Hz interference 遮蔽 small SNAPs 或 fibrillation potentials。
  - Filters 可減少 noise，但也會改變 waveform；應只與相同 filter settings 的 normal values 比較。
  - Electronic averaging 可改善 small sensory / mixed responses 的 baseline noise。
  - Stimulus artifact 可扭曲 onset latency 與 amplitude，尤其 sensory potentials 或 short-distance stimulation。
  - Depolarization starts under the cathode；cathode 應面向 active recording electrode。
  - Reversed cathode / anode 可讓 distal latency 延長約 0.3-0.4 ms，sensory conduction velocity 慢約 10 m/s，模仿 polyneuropathy 或 distal entrapment。
  - Supramaximal stimulation 需把 current 增加到 response plateau 後再增加約 25%；normal-range amplitude 不代表 stimulation 已經 supramaximal。
  - Submaximal distal stimulation 可模仿 axonal loss；submaximal proximal stimulation 可模仿 conduction block。
  - Co-stimulation 可讓低 amplitude 看似正常、製造 false conduction block、模仿 anomalous innervation，或遮蔽 true conduction block。
  - Edema 或 recording electrode off nerve 可造成 sensory / mixed response amplitude 明顯下降甚至 absent。
  - Active-reference electrode distance 太短會因 cancellation 降低 sensory amplitude；source 建議 sensory / mixed studies 使用 3-4 cm。
  - Ulnar across-elbow study 若 elbow extended，surface distance 可能低估 true nerve length，造成 artifactually slow conduction velocity。
  - Sensitivity 與 sweep speed 會影響 onset latency measurement，因此同一 nerve conduction study 中需一致。
- 發現衝突：
  - 與「NCS abnormal value equals disease」衝突。
  - 與「low amplitude equals axonal loss」衝突。
  - 與「proximal amplitude drop equals conduction block」衝突。
  - 與「normal-range amplitude proves stimulation adequacy」衝突。
  - 與「absent sural response in edema or advanced age automatically means neuropathy」衝突。
  - 與「temperature correction fully replaces warming」衝突。
- 待追蹤問題：
  - 可另處理 `Anomalous Innervations`，補 Martin-Gruber anastomosis 等 anatomic variants 如何 mimic lesion。
  - 可另處理 upper / lower extremity routine NCS chapters，補 nerve-specific protocol 與常見 pitfall。
  - 可另處理 `Basic Statistics for Electrodiagnostic Studies`，補 normative values、false positive rate 與 diagnostic threshold reasoning。

## [2026-05-10] ingest | Anomalous Innervations

- 本輪單一來源：
  - `C:\原始資料\Anomalous Innervations\Anomalous Innervations.md`
  - 本輪只處理此 textbook chapter；未混入 `Routine Upper Extremity, Facial, and Phrenic Nerve Conduction Techniques`、`Routine Lower Extremity Nerve Conduction Techniques`、`Ulnar Neuropathy at the Elbow`、`Peroneal Neuropathy at the Fibular Neck` 或 disease-specific EDX criteria。
- 新增來源摘要：
  - `09_來源摘要/Anomalous_Innervations.md`
- 新增頁面：
  - `02_方法學/EDX_異常神經支配變異判讀.md`
- 更新頁面：
  - `02_方法學/電生理診斷醫學.md`
  - `02_方法學/EDX_定位導向檢查流程.md`
  - `02_方法學/EDX_技術假象與品質控制.md`
  - `02_方法學/NCS_軸突損失與脫髓鞘判讀.md`
  - `03_疾病與臨床主題/周邊神經病灶定位與EDX_US框架.md`
  - `index.md`（Total pages 609 -> 612；本輪新增 anomalous innervation concept page 與 source summary，並校正既有 index count mismatch）
  - `log.md`
- 抽出概念：
  - EDX 異常神經支配變異判讀：MGA、APN 等 normal anatomic variants 可改變 routine NCS / needle EMG pattern，模仿 conduction block、entrapment neuropathy、technical error 或 diffuse demyelinating neuropathy；需用 targeted stimulation 證實變異後再解讀 pathology。
- 本輪直接事實：
  - Source 為 textbook chapter，source_tier 1。
  - Anomalous innervations are commonly encountered in EMG laboratory and can be mistaken for technical abnormality or pathology。
  - MGA 是 upper extremity 最常見 anomaly，為 median-to-ulnar motor crossover；source 明確指出 sensory fibers spared。
  - Source 報告 MGA prevalence 約 15-30%，可 unilateral 或 bilateral。
  - MGA 可供應 hypothenar muscles、FDI、ulnar-innervated thenar muscles 或 combinations；FDI 最常見。
  - Routine ulnar motor study recording abductor digiti minimi 中，MGA 可造成 wrist CMAP amplitude 大於 below-elbow CMAP amplitude，模仿 forearm conduction block。
  - Source 指出 up to 10% ulnar CMAP amplitude drop from wrist to below-elbow 可由 normal temporal dispersion 解釋；超過時需檢查 MGA。
  - Hypothenar MGA 可用 median stimulation at wrist and antecubital fossa while recording hypothenar muscles 證實；antecubital fossa CMAP amplitude 約等於 ulnar wrist-to-below-elbow drop。
  - Proximal MGA 加上 too-distal below-elbow stimulation site 可模仿 UNE conduction block；source 建議 ulnar below-elbow stimulation site 在 medial epicondyle distal 3 cm。
  - MGA plus CTS 可造成 prolonged distal median motor latency、proximal positive dip 與 factitiously fast median forearm conduction velocity；source 指出 median forearm CV rarely exceeds 70-75 m/s。
  - MGA 可改變 needle EMG localization，因此 NCS 必須先於 needle EMG 並協助解讀 muscle pattern。
  - APN 是 lower extremity 最常見 anomaly，源自 distal superficial peroneal nerve，走 posterior to lateral malleolus，供應 EDB lateral portion。
  - APN 可讓 peroneal motor study recording EDB 出現 below-fibular-neck / lateral-popliteal-fossa CMAP amplitude 高於 ankle；可用 posterior to lateral malleolus stimulation while recording EDB 證實。
  - MGA plus UNE 可形成 multiple ulnar conduction block-like pattern，誤導成 acquired demyelinating polyneuropathy。
  - APN plus PNFN 可形成 ankle low、fibular-neck high、lateral-popliteal-fossa low 的 low-high-low pattern。
  - Riche-Cannieu anastomosis 的 clinical / electrodiagnostic importance 在 source 中仍標示為 debated。
- 發現衝突：
  - 與「proximal amplitude drop equals conduction block」衝突。
  - 與「forearm ulnar conduction block 一定代表 acquired demyelination」衝突。
  - 與「median motor CTS pattern 必然直覺可讀」衝突。
  - 與「peroneal proximal amplitude 高於 ankle 一定是 technical error」衝突。
  - 與「needle EMG muscle distribution 可不經 NCS 直接依標準 nerve map 解讀」衝突。
- 待追蹤問題：
  - 可另處理 routine upper extremity NCS chapter，補 ulnar / median nerve-specific protocol 與 proper stimulation distances。
  - 可另處理 routine lower extremity NCS chapter，補 peroneal / tibial / sural protocol 與 APN screening trigger。
  - 可另處理 `Basic Statistics for Electrodiagnostic Studies`，補 normative values、false positive rate、conduction block threshold 與 diagnostic uncertainty。

## [2026-05-10] ingest | Routine Upper Extremity, Facial, and Phrenic Nerve Conduction Techniques

- 本輪單一來源：
  - `C:\原始資料\Routine Upper Extremity, Facial, and Phrenic Nerve Conduction Techniques\Routine Upper Extremity, Facial, and Phrenic Nerve Conduction Techniques.md`
  - 本輪只處理此 textbook chapter；未混入 `Routine Lower Extremity Nerve Conduction Techniques`、`Ulnar Neuropathy at the Elbow`、`Carpal Tunnel Syndrome`、`Blink Reflex` specialty chapter、`Phrenic Neuropathy` 或 disease-specific EDX criteria。
- 新增來源摘要：
  - `09_來源摘要/Routine_Upper_Extremity_Facial_Phrenic_NCS_Techniques.md`
- 新增頁面：
  - `02_方法學/Upper_Extremity_NCS_常規技術與陷阱.md`
- 更新頁面：
  - `02_方法學/電生理診斷醫學.md`
  - `02_方法學/EDX_定位導向檢查流程.md`
  - `02_方法學/EDX_技術假象與品質控制.md`
  - `02_方法學/NCS_軸突損失與脫髓鞘判讀.md`
  - `02_方法學/EDX_異常神經支配變異判讀.md`
  - `03_疾病與臨床主題/周邊神經病灶定位與EDX_US框架.md`
  - `index.md`（Total pages 612 -> 614；新增 upper-extremity NCS protocol concept page 與 source summary）
  - `log.md`
- 抽出概念：
  - Upper Extremity NCS 常規技術與陷阱：routine NCS 的可解讀性取決於 nerve-specific recording site、stimulation site、distance、limb position、temperature、co-stimulation control、internal comparison 與 side-to-side comparison；protocol error 可直接變成 false slowing、false conduction block 或 false normal localization。
- 本輪直接事實：
  - Source 為 textbook chapter，source_tier 1。
  - Median motor APB wrist distance 為 7 cm；excessive stimulation at wrist or antecubital fossa may co-stimulate ulnar nerve。
  - Median motor CMAP amplitude 若 antecubital fossa 大於 wrist，source 要求考慮 MGA。
  - Median motor palmar study 中 palm/wrist CMAP amplitude ratio >1.2 implies some conduction block across wrist；但因 short distance 與 recurrent thenar branch course，conduction velocity 不可靠。
  - Median sensory digit 2 or 3 distance 為 13 cm；proximal median sensory response normally smaller and harder due to temporal dispersion and phase cancellation。
  - Median sensory palmar study 中 palm/wrist SNAP amplitude ratio >1.6 implies some conduction block across wrist。
  - Median wrist-to-palm conduction velocity normally faster than palm-to-digit 3；CTS 中此 pattern reverses with relative wrist-to-palm slowing。
  - Ulnar motor ADM study 需 wrist、below-elbow、above-elbow stimulations；只做 wrist + above-elbow 會 miss ulnar slowing across elbow。
  - Ulnar NCS optimal elbow position 是 flexed 90-135 degrees；straight-elbow position 因低估 true nerve length 會造成 factitious slowing。
  - Ulnar below-elbow stimulation site 應在 medial epicondyle distal 3 cm；太 distal >4 cm 會使 nerve deep and difficult to stimulate。
  - Across-elbow distance must be measured along a curved line with elbow flexed, not straight line。
  - 若 below-elbow CMAP amplitude 比 wrist 小 >10%，需考慮 MGA。
  - Dorsal ulnar cutaneous sensory response always spared in Guyon's canal lesions，may be abnormal in some but not all UNE。
  - Absent dorsal ulnar cutaneous response 時，可保留 recording electrodes 並 stimulate superficial radial nerve，檢查 rare anomalous dorsal hand innervation。
  - Deep ulnar motor branch recording FDI may be more useful than ADM for focal ulnar slowing across elbow；FDI G2 必須放在 thumb MCP，放 index MCP 會固定出現 initial positive CMAP deflection。
  - Median-ulnar lumbrical-interossei comparison 使用 same recording electrodes and same distance；latency difference >0.5 ms definitely abnormal，且在 coexistent polyneuropathy with absent sensory / mixed potentials 時對 CTS 特別有用。
  - Median-ulnar digit 4、median-radial digit 1 internal sensory comparisons 的 normal latency difference <0.5 ms。
  - Median-ulnar palmar mixed latency difference normally <0.4 ms；short distance makes measurement error important。
  - Radial motor CMAP usually has initial positive deflection due to nearby radial-innervated muscles，不需移動 active electrode 去追 motor point。
  - Radial motor proximal distances, especially below / above spiral groove, are best measured with obstetric calipers。
  - Radial sensory study may be abnormal in radial neuropathy or posterior cord / upper or middle trunk plexus lesions and is spared in PIN neuropathy。
  - Medial antebrachial cutaneous study may be abnormal in medial cord / lower trunk lesions and is typically absent or very low in true neurogenic TOS。
  - Lateral antebrachial cutaneous study may be abnormal in musculocutaneous nerve, lateral cord, or upper trunk lesions。
  - Proximal upper-extremity stimulation at Erb's point or cervical root can be technically difficult；side-to-side amplitude and latency comparisons are necessary。
  - Root stimulation with improper needle placement too laterally has rare pneumothorax reports。
  - Phrenic motor study can accidentally stimulate spinal accessory nerve or brachial plexus；amplitudes are slightly larger during inspiration；study is difficult in obese individuals。
  - Source warns not to perform phrenic study in ICU patients with external pacemaker and to use caution near internal jugular catheter, implanted cardiac pacemaker, or cardioverter-defibrillator。
  - Facial whole-nerve stimulation can be uncomfortable and require higher current；separate facial branch stimulation is often easier and more comfortable。
  - Blink reflex records bilateral orbicularis oculi after supraorbital stimulation and is useful for facial nerve palsies, demyelinating neuropathies, and brainstem lesions。
  - Normal value tables assume controlled temperature and standard distances；sensory / mixed distal latencies are peak latencies but conduction velocities are calculated from onset latency；side-to-side comparison may be more useful than tables；each lab ideally develops its own normal values。
- 發現衝突：
  - 與「routine NCS protocol details are optional」衝突。
  - 與「ulnar wrist + above-elbow stimulation is enough」衝突。
  - 與「straight-line elbow measurement equals nerve path」衝突。
  - 與「absolute normal table always overrides side-to-side comparison」衝突。
  - 與「absent dorsal ulnar cutaneous SNAP automatically means ulnar pathology」衝突。
  - 與「phrenic NCS is just another low-risk peripheral motor study」衝突。
- 待追蹤問題：
  - 可另處理 `Routine Lower Extremity Nerve Conduction Techniques`，補 peroneal / tibial / sural protocol 與 APN screening trigger。
  - 可另處理 `Basic Statistics for Electrodiagnostic Studies`，補 normative values、false positive rate、threshold selection 與 diagnostic uncertainty。
  - 若要建立 CTS、UNE、PIN neuropathy、brachial plexopathy、facial palsy、phrenic neuropathy 或 brainstem lesion 頁，需各自使用 disease-specific source。

## [2026-05-10] structure | 新增 NCV EMG 周邊神經病變資料夾並調整來源摘要編號

- 結構調整：
  - 新增 `09_NCV EMG 周邊神經病變/` 作為 NCV / EMG / 周邊神經病變主題資料夾。
  - 將 `09_來源摘要/` 重新命名為 `10_來源摘要/`。
- 更新路徑：
  - active wiki / config 文件中的 `09_來源摘要` 已改為 `10_來源摘要`。
  - `log.md` 結構調整前的歷史紀錄保留當時的 `09_來源摘要`，不回寫成新路徑。
  - `.claude` hidden worktree 不是主知識庫本體，已排除主庫驗證。
- 更新文件：
  - `AGENTS.md`
  - `SCHEMA.md`
  - `00_總覽/知識百科_基礎規範總覽.md`
  - `00_總覽/主題地圖.md`
  - `log.md`
- 尚未執行：
  - 尚未搬移既有 `02_方法學` 與 `03_疾病與臨床主題` 內的 EDX / NCS / peripheral neuropathy 頁面；避免在未指定頁面清單前改變既有分類與 wikilink 結構。

## [2026-05-10] structure | 搬移 EDX / NCS 方法頁到 09_NCV EMG 周邊神經病變

- 搬移頁面：
  - `02_方法學/電生理診斷醫學.md` -> `09_NCV EMG 周邊神經病變/電生理診斷醫學.md`
  - `02_方法學/EDX_轉介問題設計.md` -> `09_NCV EMG 周邊神經病變/EDX_轉介問題設計.md`
  - `02_方法學/EDX_定位導向檢查流程.md` -> `09_NCV EMG 周邊神經病變/EDX_定位導向檢查流程.md`
  - `02_方法學/NCS_軸突損失與脫髓鞘判讀.md` -> `09_NCV EMG 周邊神經病變/NCS_軸突損失與脫髓鞘判讀.md`
  - `02_方法學/EDX_技術假象與品質控制.md` -> `09_NCV EMG 周邊神經病變/EDX_技術假象與品質控制.md`
  - `02_方法學/EDX_異常神經支配變異判讀.md` -> `09_NCV EMG 周邊神經病變/EDX_異常神經支配變異判讀.md`
  - `02_方法學/Upper_Extremity_NCS_常規技術與陷阱.md` -> `09_NCV EMG 周邊神經病變/Upper_Extremity_NCS_常規技術與陷阱.md`
- 更新：
  - active wiki / canvas 內指向上述 7 頁的明確路徑已更新。
  - `.obsidian/workspace.json` 內仍指向舊路徑的 workspace state 已同步更新。
  - `index.md` 新增 `09 NCV EMG 周邊神經病變` 區段，並將來源摘要區段調整為 `10 來源摘要`。
  - `00_總覽/主題地圖.md` 的 NCV EMG 導航連結已改指向新資料夾。
- 尚未執行：
  - 尚未搬移 peripheral neuropathy disease pages；下一批應先列出頁面清單再搬。

## [2026-05-10] structure | 搬移周邊神經病變主幹頁並建立 NCV EMG hub

- 搬移頁面：
  - `03_疾病與臨床主題/周邊神經病灶定位與EDX_US框架.md` -> `09_NCV EMG 周邊神經病變/周邊神經病灶定位與EDX_US框架.md`
  - `03_疾病與臨床主題/周邊神經損傷分類與恢復機制.md` -> `09_NCV EMG 周邊神經病變/周邊神經損傷分類與恢復機制.md`
  - `03_疾病與臨床主題/周邊多發神經病變_典型與非典型型態.md` -> `09_NCV EMG 周邊神經病變/周邊多發神經病變_典型與非典型型態.md`
- 新增頁面：
  - `09_NCV EMG 周邊神經病變/NCV_EMG_周邊神經病變總覽.md`
- 更新：
  - active wiki / canvas / workspace state 內指向上述 3 頁的明確路徑已更新。
  - `index.md` Total pages 614 -> 615，並將 3 個周邊神經病變主幹頁移入 `09 NCV EMG 周邊神經病變` 區段。
  - `00_總覽/主題地圖.md` 新增 NCV EMG hub link。
- 邊界：
  - 尚未搬移 `ALS_診斷框架`、`Myopathy_診斷框架`、`Spasticity_概論` 等 broader neuromuscular / CNS 邊界頁。

## [2026-05-10] ingest | Routine Lower Extremity Nerve Conduction Techniques

- 本輪單一來源：
  - `C:\原始資料\Routine Lower Extremity Nerve Conduction Techniques\Routine Lower Extremity Nerve Conduction Techniques.md`
  - 本輪只處理此 textbook chapter；未混入 peroneal neuropathy、tarsal tunnel syndrome、polyneuropathy、sciatic neuropathy、lumbar plexopathy、femoral neuropathy、meralgia paresthetica 或 S1 radiculopathy disease-specific criteria。
- 新增來源摘要：
  - `10_來源摘要/Routine_Lower_Extremity_NCS_Techniques.md`
- 新增頁面：
  - `09_NCV EMG 周邊神經病變/Lower_Extremity_NCS_常規技術與陷阱.md`
- 更新頁面：
  - `09_NCV EMG 周邊神經病變/NCV_EMG_周邊神經病變總覽.md`
  - `09_NCV EMG 周邊神經病變/電生理診斷醫學.md`
  - `09_NCV EMG 周邊神經病變/EDX_定位導向檢查流程.md`
  - `09_NCV EMG 周邊神經病變/EDX_技術假象與品質控制.md`
  - `09_NCV EMG 周邊神經病變/NCS_軸突損失與脫髓鞘判讀.md`
  - `09_NCV EMG 周邊神經病變/EDX_異常神經支配變異判讀.md`
  - `09_NCV EMG 周邊神經病變/周邊神經病灶定位與EDX_US框架.md`
  - `index.md`（Total pages 615 -> 617）
  - `log.md`
- 抽出概念：
  - Lower Extremity NCS 常規技術與陷阱：routine lower-extremity NCS 的可解讀性取決於 nerve-specific recording / stimulation / distance、normal lower-extremity amplitude-drop exceptions、small sensory / plantar response limitations、APN review、actual-distance conduction velocity、side-to-side comparison 與 height-adjusted late-response context。
- 本輪直接事實：
  - Source 為 textbook chapter，source_tier 1。
  - Tibial motor AHB distal distance 為 9 cm；tibial popliteal CMAP amplitude 可比 ankle lower，normal controls may drop up to 50%。
  - Tibial popliteal amplitude drop 不可直接解讀為 conduction block；side-to-side comparison often useful。
  - Peroneal motor EDB protocol 必須做 ankle、below-fibular-neck、above-fibular-neck stimulations；只做 ankle + above-fibular-neck 可能 miss peroneal slowing across fibular neck。
  - Excessive lateral popliteal fossa stimulation 可 co-stimulate tibial nerve。
  - Peroneal EDB proximal CMAP amplitude 高於 ankle 應考慮 APN。
  - Peroneal below-fibular-head CMAP amplitude 可正常低於 ankle，average drop 14%，rare individuals 可 drop 20-30%。
  - Peroneal TA recording 對 suspected peroneal neuropathy at fibular neck 特別有價值，可能較 EDB 更容易顯示 conduction block 或 focal slowing。
  - Femoral motor rectus femoris study 主要用 side-to-side motor amplitude 比較 femoral neuropathy、lumbar plexopathy、severe L4 radiculopathy；obesity 可使檢查困難且需要 high currents。
  - Superficial peroneal / sural / saphenous sensory studies standard distance 為 14 cm；若改 shorter distance，應用 onset latency 與 actual distance 算 conduction velocity，不應直接用 standard peak latency 判讀。
  - Source 指出 lower-extremity neuropathy screening 中，sural nerve preferable to superficial peroneal sensory nerve。
  - Saphenous response 可在 normal controls small / difficult / absent，尤其 age >40；低或 absent potential 需 side-to-side comparison。
  - Lateral femoral cutaneous nerve course relative to ASIS 有變異；無 response 時可移動 stimulator lateral then medial。
  - Lateral femoral cutaneous study 在 obesity 可困難，低或 absent response 需 unilateral symptom side-to-side comparison。
  - Medial / lateral plantar motor and sensory studies 可用於 distal tibial neuropathy across ankle。
  - Medial / lateral plantar mixed nerve studies 比 orthodromic sensory studies technically easier，且為 source preferred study for distal tibial neuropathy across ankle。
  - Plantar mixed responses 可 small / absent in normal controls，尤其 age >40；常需 averaging 與 side-to-side comparison。
  - Soleus H reflex pulse duration 必須設 1000 microseconds / 1 ms；H reflex 通常 25-34 ms，side-to-side latency difference >1.5 ms abnormal。
  - H reflex 可 delayed / absent in polyneuropathy、tibial neuropathy、sciatic neuropathy、lumbosacral plexopathy 或 S1 radiculopathy。
  - Late responses in tall or short patients must be normalized for height。
  - Normal value tables assume controlled temperature and standard distances；motor / sensory amplitudes measured baseline to negative peak；sensory / mixed latencies are peak latencies but conduction velocities use onset latency。
- 發現衝突：
  - 與「proximal amplitude drop equals conduction block」衝突。
  - 與「ankle and above-fibular-neck peroneal stimulation are enough」衝突。
  - 與「absent plantar / saphenous / lateral femoral cutaneous response is automatically abnormal」衝突。
  - 與「shorter-distance sensory response can still use standard-distance peak latency cutoff」衝突。
  - 與「H reflex abnormality specifically localizes S1 radiculopathy」衝突。
- 待追蹤問題：
  - 可另處理 `Basic Statistics for Electrodiagnostic Studies`，補 normative values、false positive rate、threshold selection 與 diagnostic uncertainty。
  - 若要建立 peroneal neuropathy at fibular neck、tarsal tunnel syndrome、lateral femoral cutaneous neuropathy、sciatic neuropathy、lumbar plexopathy、femoral neuropathy 或 S1 radiculopathy 頁，需各自使用 disease-specific source。

## [2026-05-10] ingest | Basic Statistics for Electrodiagnostic Studies

- 本輪單一來源：
  - `C:\原始資料\Basic Statistics for Electrodiagnostic Studies\Basic Statistics for Electrodiagnostic Studies.md`
  - 本輪只處理此 textbook chapter；未混入 CTS、UNE、radiculopathy、polyneuropathy 或任何 disease-specific diagnostic criteria。
- 新增來源摘要：
  - `10_來源摘要/Basic_Statistics_for_Electrodiagnostic_Studies.md`
- 新增頁面：
  - `09_NCV EMG 周邊神經病變/EDX_統計閾值與False_Positive控制.md`
- 更新頁面：
  - `09_NCV EMG 周邊神經病變/NCV_EMG_周邊神經病變總覽.md`
  - `09_NCV EMG 周邊神經病變/電生理診斷醫學.md`
  - `09_NCV EMG 周邊神經病變/EDX_轉介問題設計.md`
  - `09_NCV EMG 周邊神經病變/EDX_定位導向檢查流程.md`
  - `09_NCV EMG 周邊神經病變/NCS_軸突損失與脫髓鞘判讀.md`
  - `index.md`（Total pages 617 -> 619）
  - `log.md`
- 抽出概念：
  - EDX 統計閾值與 False-Positive 控制：EDX abnormality 是由 normal-value distribution、cutoff、sensitivity / specificity、pre-test probability、likelihood ratio 與 multiple-testing false-positive risk 共同決定的 post-test probability，不是單一數值超線就等於 disease。
- 本輪直接事實：
  - Source 為 textbook chapter，source_tier 1。
  - Normal distribution 中約 68% observations 在 mean ±1 SD，約 95% 在 ±2 SD，約 99.7% 在 ±3 SD。
  - EDX 常使用單側 tail cutoff；2 SD one-tail 約包含 97.5% population，2.5 SD 約包含 99.4% population。
  - 多數 EDX cutoff values 常設在 2 或 2.5 SD above / below mean。
  - Specificity 是 without condition 且 negative test 的比例；sensitivity 是 with condition 且 positive test 的比例。
  - Normal 與 disease populations 通常 overlap，因此 false positives 與 false negatives 不可完全避免。
  - Lower cutoff 會增加 sensitivity 但降低 specificity；higher cutoff 會增加 specificity 但降低 sensitivity。
  - False positive 是 type I error；false negative 是 type II error。
  - Source 指出 type I error 通常較不可接受，因為會把正常病人貼上 abnormal label，造成不必要 testing / treatment；除非 test 只作 screening，specificity 應優先於 sensitivity。
  - Source 明確寫 EDX 不能完全 "rule out" 或 "rule in" any condition。
  - Digit 4 CTS comparison example 中 cutoff >=0.4 ms specificity >97%，sensitivity 約 70%；cutoff 0.1 ms sensitivity 約 90%，specificity 約 60%。
  - Bayes theorem 下，positive test 的 true-positive probability 取決於 sensitivity、specificity 與 disease prevalence / pre-test probability。
  - 95% sensitivity / 95% specificity test 在 80% prevalence population 的 PPV 為 98.7%；在 1% prevalence population 的 PPV 為 16.1%。
  - Source 指出 minimally positive test result 只有在 disease likelihood 高時才有意義；markedly abnormal test 則較可能為 true positive。
  - Positive likelihood ratio = sensitivity / (1 - specificity)。
  - Fagan nomogram example 中，pre-test probability 50% 時，LR 10 可使 post-test probability 約 93%，LR 3 則約 72%。
  - Multiple tests 會增加 false-positive risk；若 10 tests 各有 2.5% false-positive rate 且任一 abnormal 即診斷，cumulative false-positive rate 可 >20% / almost 25%。
  - 若要求 two or more tests abnormal，10 tests 各 2.5% false-positive rate 的 cumulative false-positive rate 可維持 <2.5%。
- 發現衝突：
  - 與「EDX abnormal value equals disease」衝突。
  - 與「EDX can fully rule in / rule out」衝突。
  - 與「borderline abnormality has same meaning regardless of clinical likelihood」衝突。
  - 與「more tests always increase certainty」衝突。
  - 與「sensitivity should always be maximized」衝突。
- 待追蹤問題：
  - 可另處理 `Anatomy and Neurophysiology for Electrodiagnostic Studies`，補 EDX anatomy / nerve physiology foundational assumptions。
  - 若要建立 CTS、UNE、radiculopathy、polyneuropathy disease-specific diagnostic threshold 頁，需各自使用 disease-specific source。

## [2026-05-10] ingest | The Interaction of Foot Strike and Footwear in Runners

- 本輪單一來源：
  - `C:\原始資料\The Interaction of Foot Strike and Footwear in Runners\The Interaction of Foot Strike and Footwear in Runners.md`
  - 本輪只處理此 textbook chapter / focused narrative review；未混入其他 running injury、footwear 或 gait sources。
- 更新來源摘要：
  - `10_來源摘要/The_Interaction_of_Foot_Strike_and_Footwear_in_Runners.md`
- 新增頁面：
  - `06_Gait_Biomechanics/Foot_Strike與Footwear交互作用.md`
- 更新頁面：
  - `06_Gait_Biomechanics/跑步步態評估.md`
  - `06_Gait_Biomechanics/跑鞋選擇原則.md`
  - `06_Gait_Biomechanics/步態評估總論.md`
  - `index.md`（Total pages 619 -> 620）
  - `log.md`
- 抽出概念：
  - Foot Strike 與 Footwear 交互作用：同一種 foot strike 在不同 footwear geometry、transition history 與 tissue capacity 下，不代表同一種 load distribution。
- 本輪直接事實：
  - Source 為 textbook chapter / focused narrative review，project source_tier 1，但 clinical prescription confidence 為 medium。
  - Source 指出 rearfoot strike 常見 abrupt vertical impact transient 與較高 vertical load rate。
  - Source 指出 forefoot strike 可降低 vertical load rate，並在 selected patellofemoral pain runner 中可能降低 patellofemoral joint contact stress。
  - Source 指出 forefoot strike 會增加 plantar flexors 與 Achilles loading。
  - Source 指出 forefoot strike in traditional shoes 可能降低 vertical load rate，但 anteroposterior / mediolateral load rates 較高，resultant load rate 不一定較低。
  - Source 指出 traditional shoe 的 outer sole flare 與 elevated heel 可能改變 forefoot-strike initial contact 的 inversion / plantarflexion。
  - Source 指出 abrupt transition to minimal footwear 或 forefoot strike 可能導致 calf strain、Achilles tendinopathy、posterior tibialis tendinopathy、plantar fascia stress 或 metatarsal stress injury。
- 發現衝突：
  - 與「forefoot strike 一定比 rearfoot strike 安全」衝突。
  - 與「minimal footwear 可作為 routine injury prevention」衝突。
  - 與「只看 vertical load rate 就能判斷總傷害風險」衝突。
- 待追蹤問題：
  - 可另以 single-source ingest 補足 minimal footwear transition protocol 的 progression dose。
  - 可另以 disease-specific sources 補 Patellofemoral Pain、Achilles tendinopathy、metatarsal stress injury 中的 foot-strike modification 適應症與禁忌。

## [2026-05-10] reorganize | 06_Gait_Biomechanics 資料夾整理

- 整理原則：
  - `06_Gait_Biomechanics` 改作為下肢疾病、lower-limb biomechanics、gait、shoe / footwear、lower-limb orthosis 與 runner injury 相關頁面的集中資料夾。
  - 神經疾病中的 gait 問題，例如 MS / Parkinson / cervical myelopathy，仍保留在 `03_疾病與臨床主題`，因其主體不是下肢 biomechanical disease。
- 移入 `06_Gait_Biomechanics`：
  - 下肢截肢與義肢：`下肢截肢復健總論.md`、`下肢義肢_K_Level_處方邏輯.md`
  - lower-limb pain 與足踝疾病：`Lower_Limb_Pain_分區定位與高風險分流.md`、`足部疼痛分區評估.md`、`Achilles_tendinopathy.md`、`Ankle_sprain_總論.md`、`Syndesmotic_ankle_injury.md`、`Plantar_fasciitis.md`
  - runner injury 與 return-to-run：`跑者下肢傷害評估總論.md`、`受傷跑者復健原則.md`、`跑步傷害風險因子與預防.md`、`跑步與Osteoarthritis.md`、`跑者運動性下腿痛.md`、`跑者膝部疼痛.md`、`跑者髖骨盆與大腿疼痛.md`
  - knee / hip / thigh related conditions：`Patellofemoral_Pain.md`、`Iliotibial_Band_Syndrome.md`、`Hamstring_肌肉與肌腱傷害.md`、`Quadriceps_肌肉與肌腱傷害.md`
- 移出 `06_Gait_Biomechanics`：
  - `上肢矯具與復健機器人.md` -> `03_疾病與臨床主題`
  - `脊椎裝具總論.md` -> `03_疾病與臨床主題`
- 更新：
  - 全域修正 moved pages 的 wikilinks；`log.md` 的歷史紀錄不做回寫，只追加本紀錄。
  - 重建 `index.md` 的 `06 Gait / Biomechanics / Orthotics / Shoes` 區塊，並把上肢/脊椎裝具條目放回 `03_疾病與臨床主題`。
- 待追蹤問題：
  - `血管與淋巴疾病復健` 涵蓋 PAD / venous disease / lymphedema 與 gait，但主體仍較像跨疾病 rehabilitation；本輪暫不移入，日後可視下肢血管病頁面是否拆頁再決定。

## [2026-05-10] ingest | Anatomy and Neurophysiology for Electrodiagnostic Studies

- 本輪單一來源：
  - `C:\原始資料\Anatomy and Neurophysiology for Electrodiagnostic Studies\Anatomy and Neurophysiology for Electrodiagnostic Studies.md`
  - 本輪只處理此 textbook chapter；未混入 disease-specific CTS、radiculopathy、polyneuropathy、small-fiber neuropathy 或 nerve-specific protocol sources。
- 新增來源摘要：
  - `10_來源摘要/Anatomy_and_Neurophysiology_for_Electrodiagnostic_Studies.md`
- 新增頁面：
  - `09_NCV EMG 周邊神經病變/EDX_解剖與神經生理基礎.md`
- 更新頁面：
  - `09_NCV EMG 周邊神經病變/NCV_EMG_周邊神經病變總覽.md`
  - `09_NCV EMG 周邊神經病變/電生理診斷醫學.md`
  - `09_NCV EMG 周邊神經病變/EDX_定位導向檢查流程.md`
  - `09_NCV EMG 周邊神經病變/NCS_軸突損失與脫髓鞘判讀.md`
  - `index.md`（Total pages 620 -> 622）
  - `log.md`
- 抽出概念：
  - EDX 解剖與神經生理基礎：EDX 判讀需以 DRG 位置、root / plexus / peripheral nerve 組織、large-fiber selectivity、myelin / saltatory conduction、motor unit / NMJ 與 volume conduction 為底層假設。
- 本輪直接事實：
  - Source 為 textbook chapter，source_tier 1。
  - NCS and EMG primarily serve as extensions of the clinical examination。
  - DRG 位於 spinal cord 外、靠近 intervertebral foramen；lesion proximal to DRG 可有 sensory symptoms 但 sensory conduction study preserved。
  - Motor and sensory roots unite distal to the DRG to form a mixed spinal nerve；dorsal and ventral rami both contain motor and sensory fibers。
  - Adjacent myotomes / dermatomes overlap substantially；single root lesion seldom causes major sensory loss and should not cause anesthesia。
  - Routine NCS latency / velocity measurements reflect the largest and fastest fibers in the studied nerve。
  - Standard NCS does not record small myelinated A-delta / B fibers or unmyelinated C fibers；selective small-fiber neuropathy may have normal routine NCS。
  - Myelin from Schwann cells enables saltatory conduction；human peripheral myelinated fibers typically conduct around 35-75 m/s。
  - A motor unit consists of one anterior horn cell, its axon, and all innervated muscle fibers。
  - CMAPs, SNAPs and MUAPs are volume-conducted near-field potentials；amplitude and morphology depend on source-electrode distance。
  - Correct motor CMAP recording over the motor point should produce initial negative deflection；off-motor-point recording can produce initial positive deflection。
  - Stimulus artifact is a far-field potential and is transmitted essentially instantly。
- 發現衝突：
  - 與「normal SNAP excludes sensory lesion」衝突。
  - 與「normal routine NCS excludes small-fiber neuropathy」衝突。
  - 與「single root lesion should cause anesthesia」衝突。
  - 與「waveform morphology is purely pathologic」衝突。
- 待追蹤問題：
  - 可另處理 `Late Responses`、`Repetitive Nerve Stimulation` 與 `Blink Reflex`，但需各自作為單一來源 ingest。
  - Disease-specific radiculopathy、CTS、polyneuropathy 與 small-fiber neuropathy 頁仍需各自使用 disease-specific source 補完整 diagnostic boundary。

## [2026-05-11] ingest | Late Responses

- 本輪單一來源：
  - `C:\原始資料\Late Responses\Late Responses.md`
  - 本輪只處理此 textbook chapter；未混入 `Repetitive Nerve Stimulation`、`Blink Reflex`、`Basic Nerve Conduction Studies`、`Anatomy and Neurophysiology for Electrodiagnostic Studies` 或 disease-specific GBS / radiculopathy / polyneuropathy / sciatic neuropathy / lumbosacral plexopathy / S1 radiculopathy sources。
- 新增來源摘要：
  - `10_來源摘要/Late_Responses.md`
- 新增頁面：
  - `09_NCV EMG 周邊神經病變/F_Response_F_Estimate判讀.md`
  - `09_NCV EMG 周邊神經病變/H_Reflex_臨床用途與限制.md`
  - `09_NCV EMG 周邊神經病變/A_Wave_Axon_Reflex判讀.md`
- 更新頁面：
  - `09_NCV EMG 周邊神經病變/NCV_EMG_周邊神經病變總覽.md`
  - `09_NCV EMG 周邊神經病變/電生理診斷醫學.md`
  - `09_NCV EMG 周邊神經病變/EDX_定位導向檢查流程.md`
  - `09_NCV EMG 周邊神經病變/NCS_軸突損失與脫髓鞘判讀.md`
  - `09_NCV EMG 周邊神經病變/Lower_Extremity_NCS_常規技術與陷阱.md`
  - `09_NCV EMG 周邊神經病變/Upper_Extremity_NCS_常規技術與陷阱.md`
  - `index.md`（Total pages 622 -> 626）
  - `log.md`
- 抽出概念：
  - F Response 與 F Estimate 判讀：F response 是 antidromic 折返後 1-5% CMAP 的純 motor 晚期 potential，測整條 motor nerve；F estimate = (2D/CV) × 10 + 1 ms + DL 校正 distal latency / CV / 肢長後判讀 proximal segment，但 site / disease specificity 低，對 EMG-confirmed S1 radiculopathy sensitivity 約 4-8%。
  - H Reflex 臨床用途與限制：H reflex 是 1 ms submaximal 刺激下選擇活化 Ia muscle-spindle afferent 的 monosynaptic reflex，2 歲後成人只能 routinely 從 tibial-soleus 取得，是 S1 ankle jerk 的電生理對應物；對 polyneuropathy、tibial / sciatic neuropathy、lumbosacral plexopathy 與 S1 radiculopathy 都敏感但不特異。
  - A Wave / Axon Reflex 判讀：A wave 是 reinnervated 或 demyelinated 神經 submaximal 刺激下沿 collateral branching point 折返的晚期 motor potential；以每次刺激 latency / configuration 完美一致與變動的 F response 區分，是 reinnervation、demyelination（包含 early GBS）或 distal stimulation 不真正 supramaximal 的 marker，不是 true reflex。
- 本輪直接事實：
  - Source 為 textbook chapter，source_tier 1。
  - F response 是純 motor、不含 synapse、不是 true reflex，每次刺激活化的 anterior horn cell 群不同，因此 latency 與 configuration 略變動。
  - F response 約為 CMAP 的 1%-5%；severely low CMAP 時 absent F 沒有 proximal-lesion 意義。
  - Normal F latency：median / ulnar at wrist 約 25-32 ms；peroneal / tibial at ankle 約 45-56 ms。
  - 設定：supramaximal、cathode proximal、gain 200 μV、sweep 5-10 ms、≤ 0.5 Hz、≥ 10 rastered stimulations。
  - Normal F-wave persistence 80-100%（最少 > 50%），peroneal F 例外可在正常人 absent / impersistent。
  - Normal chronodispersion ≤ 4 ms（upper） / ≤ 6 ms（lower）。
  - Proximal stimulation → M latency 增加但 F latency 縮短。
  - F estimate 公式：F estimate = (2D/CV) × 10 + 1 ms + DL；surface D 用 C7 spinous process–wrist（上肢）或 xiphoid–ankle（下肢）。
  - Measured minimal F latency 通常稍短於 F estimate（近端速度略快）；> F estimate 表 disproportionate proximal slowing。
  - Mauricio et al. (2014)：tibial F response 對 EMG-confirmed S1 radiculopathy 的 sensitivity 約 4%；加 F estimate 約 8%。
  - F response 在上肢 routinely 只能評估 C8-T1，下肢 L5-S1；其他 root 因 dual myotome 與 sensory-predominant lesion 通常 F response normal。
  - Jendrassik 在 F response 不可得時可 prime AHC；但若 F response 已可得就不該做（over-priming 反讓 F response 不出現）。
  - H reflex 是 true reflex：Ia afferent + 突觸 + alpha motor efferent。
  - 2 歲以後 H reflex 在 routine 條件下只能從 tibial-soleus 取得；newborn 廣泛存在於多條 motor nerve。
  - H reflex 設定：1 ms 脈寬、submaximal、popliteal fossa cathode proximal、G1 over soleus 2-3 fingerbreadths distal to gastrocnemius 兩腹會合處、G2 over Achilles tendon。
  - 最佳 G1 位置：popliteal fossa 至 medial malleolus 後方分八等分中的第 5 或 6 段。
  - 典型 H 第一次出現於約 25-34 ms latency、triphasic、肌肉靜息下取得。
  - 隨刺激強度上升：H 增大且 latency 縮短、M 出現、最終 H 因 antidromic motor collision 縮小消失，被 F response 取代。
  - Normal H latency 上限約 34 ms（leg-length / age 或 height nomogram 校正）；同距離下 side-to-side 差 > 1.5 ms 視為顯著；H/M ratio ≤ 50%。
  - H reflex 是 S1 ankle jerk 的電生理對應物：ankle jerk 存在 → H reflex 應存在；ankle jerk 消失，H reflex 仍可能存在。
  - 任何降低 ankle jerk 的 lesion（polyneuropathy、proximal tibial neuropathy、sciatic neuropathy、lumbosacral plexopathy、S1 nerve root lesion）都可能延長或消失 H reflex。
  - 老年人雙側 ankle jerk / H reflex 消失常為正常變異，不必然病理。
  - H/M ratio 增加（特別是 adult 在 soleus 以外肌肉測到 H reflex）暗示 upper motor neuron / 中樞興奮性增高。
  - A wave (axon reflex) 名為 reflex 但無 synapse，並非真正 reflex。
  - 在 rastered F response trace 中以 latency / configuration 完美一致辨識 A wave；F response 則 latency / configuration 略變動。
  - A wave 通常出現在 M response 後、F response 前；極少數 collateral fiber 速度極慢時可在 F response 後。
  - Submaximal stimulation 是 A wave 出現的常見條件；supramaximal 刺激下 antidromic collision 通常消除 A wave。
  - A wave 主要伴隨 axonal-loss 後 reinnervation，也可見於 demyelinating neuropathy；早期 Guillain-Barré syndrome 的前幾天經典出現 A wave，source 對其機制提出 ephaptic spread 推測（未確認）。
  - A wave 也可作為 distal stimulation 不真正 supramaximal 的線索。
- 發現衝突：
  - 與「prolonged F response 等於 radiculopathy」衝突。
  - 與「normal F response 排除 radiculopathy」衝突。
  - 與「absent F response 等於 proximal lesion」衝突。
  - 與「absent / delayed H reflex 特異定位 S1 radiculopathy」衝突。
  - 與「雙側 absent H reflex 一定是 polyneuropathy 或 S1 radiculopathy」衝突。
  - 與「stable latency 的晚期 potential 也是 F response」衝突。
  - 與「axon reflex 是 reflex」衝突。
  - 與「supramaximal 後仍持續的 A wave 必然代表 reinnervation 或 demyelination」衝突（也可能代表 stimulation 實際未 supramaximal）。
- 待追蹤問題：
  - 可另處理 `Repetitive Nerve Stimulation` 與 `Blink Reflex`，建立 specialized EDX testing concept pages。
  - Disease-specific GBS、CIDP、CMT、S1 radiculopathy、sciatic neuropathy、lumbosacral plexopathy 仍需各自以 disease-specific source ingest 後建立 diagnostic criteria 頁。
  - 周邊神經損傷分類與恢復機制頁未來若擴展為 multi-source，可加入 A wave 作為 reinnervation marker 的具體連結。

## [2026-05-11] correction | EDX/NCS 系列來源摘要語言修正（中文化）

- 修正原因：先前 EDX/NCS 系列來源摘要 prose 以英文為主，與 AGENTS.md §5「主要使用台灣繁體中文，醫學與科學專有名詞保留 American English」原則不符。
- 範圍限制：本批次僅修正 prose 語言，未變動結構、概念邊界、來源歸屬或事實內容；skill template structure markers（## Source Type、## Reliability Level、## Core Concepts Extracted、## Clinically Useful Points 等）保留英文，per `feynman-euclidean-summary` skill template。
- 重新檢查來源（每篇仍為單一來源 ingest）：
  - `10_來源摘要/Late_Responses.md`
  - `10_來源摘要/Anatomy_and_Neurophysiology_for_Electrodiagnostic_Studies.md`
  - `10_來源摘要/Basic_Nerve_Conduction_Studies.md`
  - `10_來源摘要/Basic_Statistics_for_Electrodiagnostic_Studies.md`
  - `10_來源摘要/Approach_NCS_EMG_Neuromuscular_Ultrasound.md`
  - `10_來源摘要/Artifacts_and_Technical_Factors.md`
  - `10_來源摘要/Anomalous_Innervations.md`
  - `10_來源摘要/Routine_Upper_Extremity_Facial_Phrenic_NCS_Techniques.md`
  - `10_來源摘要/Routine_Lower_Extremity_NCS_Techniques.md`
  - `10_來源摘要/Peripheral_Nerve_Disorders.md`
  - `10_來源摘要/Myopathic_Disorders.md`
  - `10_來源摘要/Motor_Neuron_Diseases.md`
- 修正頁面：以上 12 篇來源摘要全文改寫為「中文敘述 + 英文醫學專名」風格；frontmatter 的 contradictions 從英文改為中文。
- 移除或降級的陳述：無；事實層級不變。
- 仍不確定之處：
  - `09_NCV EMG 周邊神經病變/` 之下的 EDX 概念頁（F_Response_F_Estimate判讀、H_Reflex_臨床用途與限制、A_Wave_Axon_Reflex判讀 等）大部分已是中文敘述，但結構仍含部分英文 markdown 段落，未列入本輪改寫。
  - 10_來源摘要 中 CJK 比例 < 5% 的英文密集型文件還有約 73 篇（含 Wprime / VO2 / CP / GBS / stroke UpToDate / parenting / rehab textbook 等系列）；本輪未動，待使用者確認下一輪範圍與優先序後再處理。
- 待處理來源：
  - 上述 73 篇英文密集型 source summary（待批次中文化）。
  - 09_NCV EMG 周邊神經病變/ 中的 F_Response、H_Reflex、A_Wave 三篇概念頁（如使用者要求）。

## [2026-05-11] ingest | Repetitive Nerve Stimulation

- 本輪單一來源：
  - `C:\原始資料\Repetitive Nerve Stimulation\Repetitive Nerve Stimulation.md`
  - 本輪只處理此 textbook chapter；未混入 `Blink Reflex`、single-fiber EMG、myasthenia gravis guideline、Lambert-Eaton myasthenic syndrome guideline、botulism guideline 或 antibody testing 來源。
- 新增來源摘要：
  - `10_來源摘要/Repetitive_Nerve_Stimulation.md`
- 新增頁面：
  - `09_NCV EMG 周邊神經病變/RNS_Decrement_Increment判讀.md`
  - `09_NCV EMG 周邊神經病變/RNS_Protocol與技術陷阱.md`
- 更新頁面：
  - `09_NCV EMG 周邊神經病變/NCV_EMG_周邊神經病變總覽.md`
  - `09_NCV EMG 周邊神經病變/電生理診斷醫學.md`
  - `09_NCV EMG 周邊神經病變/EDX_定位導向檢查流程.md`
  - `09_NCV EMG 周邊神經病變/EDX_技術假象與品質控制.md`
  - `index.md`（Total pages 626 -> 629）
  - `log.md`
- 抽出概念：
  - RNS Decrement / Increment 判讀：RNS 用 slow 2-3 Hz stimulation、brief exercise / rapid RNS 與 prolonged-exercise exhaustion 改變 ACh quanta release 與 EPP，從 CMAP decrement / increment 推估 NMJ safety factor；>10% decrement abnormal 但不等於 myasthenia gravis，>100% increment 高度支持 presynaptic NMJ disorder，但 40-100% 屬 equivocal。
  - RNS Protocol 與技術陷阱：RNS 判讀前必須控制 recording site temperature >=33°C、immobilization、supramaximal stimulation、AChE inhibitor status、exercise duration / timing、nerve / muscle selection 與 needle EMG confounders；facial RNS 因 CMAP 小與難固定，false-positive 風險高。
- 本輪直接事實：
  - Source 為 textbook chapter，source_tier 1。
  - RNS 應考慮於 suspected myasthenia gravis、Lambert-Eaton myasthenic syndrome、botulism、fatigability、proximal weakness、dysphagia、dysarthria 或 ocular abnormalities。
  - NMJ 的 ACh quanta stores 包含 immediately available store 約 1000 quanta、mobilization store 約 10,000 quanta、reserve store >100,000 quanta；每個 quantum 約含 10,000 ACh molecules。
  - Slow RNS 2-3 Hz 會造成 quanta depletion；normal safety factor 下 EPP 仍高於 threshold，因此 CMAP 穩定。
  - Postsynaptic NMJ disorder 中同樣 quanta release 產生較小 EPP；slow RNS 可讓部分 EPP 掉到 threshold 以下，造成 CMAP decrement。
  - Presynaptic NMJ disorder 中 release probability 降低，baseline EPP / CMAP 可偏低；rapid RNS 或 10 秒 maximal voluntary exercise 可因 calcium accumulation 造成 facilitation / increment。
  - 1 分鐘 maximal exercise 後，2-4 分鐘內 slow RNS 可顯示 postexercise exhaustion。
  - Pseudofacilitation 可讓 normal CMAP amplitude 增加，但通常 duration 變短、area 變化小，且 amplitude increment 通常不超過 40%。
  - >10% decrement 定義為 abnormal；任何 reproducible decrement 可能 abnormal，但 10% cutoff 用來容納 technical factors。
  - Increment >100% 常見於 presynaptic NMJ disorders；40-100% increment 最好視為 equivocal。
  - RNS protocol 包含 warming to >=33°C、immobilization、routine motor NCS first、3-Hz rest RNS 5-10 impulses repeated three times、brief exercise repair / facilitation、prolonged exercise exhaustion testing、low CMAP 時做 postexercise increment testing，以及 proximal / distal nerve selection。
  - Acetylcholinesterase inhibitors 最好在檢查前停 3-4 小時，除非 medically contraindicated。
  - Facial RNS 因 baseline CMAP 小與 muscle 無法良好固定，容易因小幅變化造成 false-positive decrement。
  - Denervation / reinnervation、motor neuron disease、myotonic disorders 與 metabolic myopathies 也可出現 decrement；RNS 不能孤立判讀，需 history、directed neurologic examination、routine NCS 與 needle EMG。
- 發現衝突：
  - 與「normal RNS 排除 NMJ disorder」衝突。
  - 與「>10% decrement 就是 myasthenia gravis」衝突。
  - 與「postexercise increment 一定是 Lambert-Eaton myasthenic syndrome」衝突。
  - 與「facial RNS 因接近 ocular / bulbar phenotype 所以最可靠」衝突。
  - 與「cold limb 只會影響 routine NCS，不影響 RNS 判讀」衝突。
  - 與「RNS 可以不做 needle EMG confounder control」衝突。
- 待追蹤問題：
  - 可另處理 `Blink Reflex`，建立 specialized EDX testing concept page。
  - Myasthenia gravis、Lambert-Eaton myasthenic syndrome、botulism 與 single-fiber EMG 需各自使用 disease- / method-specific source 補 diagnostic criteria 與 sensitivity / specificity。

## [2026-05-11] ingest | Nurturing Care for Children with Developmental Delays and Disabilities

- 本輪單一來源：
  - `C:\原始資料\Nurturing Care for Children with Developmental Delays and Disabilities\Nurturing Care for Children with Developmental Delays and Disabilities.md`
  - 本輪只處理此 UNICEF / WHO thematic brief；未混入 `Nurturing Care Practice Guide`、WHO 2020 ECD guideline、WHO CST manuals、LEAP-CP 原始研究、Baby Ubuntu 原始研究或 condition-specific guideline。
- 新增來源摘要：
  - `10_來源摘要/Nurturing_Care_for_Children_with_Developmental_Delays_and_Disabilities.md`
- 新增頁面：
  - `07_Pediatric_Development/Disability-Inclusive_Nurturing_Care_發展遲緩與發展障礙兒童.md`
- 更新頁面：
  - `07_Pediatric_Development/Nurturing_Care_健康與營養服務整合.md`
  - `index.md`（Total pages 629 -> 631）
  - `log.md`
- 抽出概念：
  - Disability-inclusive nurturing care：children at risk of or with developmental delays and disabilities 仍需要完整 nurturing care；服務系統需用 individualized、family-centred、coordinated care，把 inclusive universal services 與 targeted / indicated supports 並行，並處理 caregiver burden、stigma、accessibility、assistive technology、ECI 與 referral follow-up。
- 本輪直接事實：
  - Source 為 UNICEF / WHO 2025 thematic brief，非 formal guideline、textbook chapter、systematic review 或 primary trial；本 wiki 依 AGENTS hierarchy 標為 Tier 7 official institutional brief。
  - Nurturing care 包含 good health、adequate nutrition、safety and security、opportunities for early learning、responsive caregiving。
  - 來源定義 developmental delay 為對 actual / adjusted age expected milestones 的 significant variation。
  - 來源定義 developmental disability 為影響 developing nervous system 並造成 motor、cognitive、language、behaviour 或 sensory functioning impairment 的 health conditions，且 participation 會受 barriers / context 限制。
  - 來源採 ICF 觀點：disability 不是 health condition 本身，而是 impairment 與 societal、physical、environmental barriers 的互動結果。
  - 來源列出三個 guiding principles：individualized care、family-centred care、coordinated care。
  - 來源主張 twin-track approach：inclusive mainstream / universal services for all children，加上 targeted / indicated services for children and caregivers requiring additional support。
  - 來源指出 ECI services 應 birth-onward、family-centred、strengths-based、home- and routine-grounded、multisectoral、integrated and transdisciplinary。
  - 來源指出 developmental monitoring 不只是 milestone checking，而要看 child functioning、home environment、family risk / strengths 與 individualized support needs。
  - 來源明確指出 early identification 應促成 timely intervention，但 diagnosis requirement 不應延誤 family-centred services。
  - Caregiver physical / mental health、safety、resources、financial strain、information access、stigma 與 social support 會影響 caregiver 提供 nurturing care 的能力。
- 發現衝突：
  - 與「developmental disability child 只需要 specialist therapy，不需要 ordinary nurturing care」衝突。
  - 與「沒有 formal diagnosis 前不應提供 family-centred support」衝突。
  - 與「universal health / nutrition service 天然公平，不需另外處理 accessibility / stigma / caregiver burden」衝突。
  - 與「developmental monitoring 等於 milestone checklist」衝突。
- 待追蹤問題：
  - 若要把 CST、LEAP-CP、Baby Ubuntu 或 AAC project 寫成 effectiveness page，需各自回到原始研究或 systematic review。
  - Assistive technology access、care coordination、community stigma / participation barriers 可後續拆成單一概念頁。
  - 本 thematic brief 不能替代 CP、ASD、hearing loss、ID / GDD 或 feeding disorder 的 condition-specific diagnostic / treatment sources。

## [2026-05-11] ingest | Blink Reflex

- 本輪單一來源：
  - `C:\原始資料\Blink Reflex\Blink Reflex.md`
  - 本輪只處理此 textbook chapter；未混入 `Routine Upper Extremity, Facial, and Phrenic Nerve Conduction Techniques`、`Late Responses`、`Repetitive Nerve Stimulation`、facial palsy guideline、brainstem stroke source、multiple sclerosis source、Guillain-Barre syndrome guideline 或 trigeminal neuropathy source。
- 新增來源摘要：
  - `10_來源摘要/Blink_Reflex.md`
- 新增頁面：
  - `09_NCV EMG 周邊神經病變/Blink_Reflex_R1_R2判讀.md`
- 更新頁面：
  - `09_NCV EMG 周邊神經病變/NCV_EMG_周邊神經病變總覽.md`
  - `09_NCV EMG 周邊神經病變/電生理診斷醫學.md`
  - `09_NCV EMG 周邊神經病變/EDX_定位導向檢查流程.md`
  - `index.md`（Total pages 631 -> 633）
  - `log.md`
- 抽出概念：
  - Blink Reflex R1/R2 判讀：blink reflex 是 cranial nerve V1 afferent、pontomedullary interneuron network 與 cranial nerve VII efferent 的 true reflex；以 unilateral supraorbital stimulation 與 bilateral orbicularis oculi recording 判讀 ipsilateral R1、ipsilateral R2、contralateral R2 的 latency / absence pattern，可提示 trigeminal afferent、facial efferent、mid-pontine、medullary 或 generalized demyelinating pathway abnormality。
- 本輪直接事實：
  - Source 為 textbook chapter，source_tier 1。
  - Blink reflex 是 clinically evoked corneal reflex 的 electrical correlate。
  - Blink reflex 是 true reflex，包含 sensory afferent limb、intervening synapses 與 motor efferent limb。
  - Afferent limb 由 trigeminal nerve ophthalmic division 的 supraorbital branch sensory fibers 介導。
  - Efferent limb 由 facial nerve motor fibers 介導，recording muscle 為 orbicularis oculi。
  - Ipsilateral supraorbital nerve stimulation 可引發 bilateral facial nerve eye-blink responses。
  - R1 通常 ipsilateral，代表 main sensory nucleus of V in mid-pons 到 ipsilateral facial nucleus in lower pontine tegmentum 的 disynaptic pathway。
  - R2 通常 bilateral，由 nucleus of the spinal tract of V in ipsilateral pons / medulla 到 bilateral facial nuclei 的 multisynaptic pathway 介導。
  - R1 stable / reproducible，常為 biphasic or triphasic；少數正常人 bilateral R1 可能不能可靠誘發。
  - R2 polyphasic、variable，且 repeated stimulation 會 habituate。
  - Typical R1 latency 約 10-12 ms，R2 latency 約 30-40 ms。
  - Normal absolute latency anchors：R1 <13 ms、ipsilateral R2 <41 ms、contralateral R2 <44 ms。
  - Side-to-side anchors：R1 difference <1.2 ms、ipsilateral R2 difference <5 ms、contralateral R2 difference <7 ms。
  - Procedure：relaxed supine position、bilateral orbicularis oculi recording、supraorbital stimulation over medial eyebrow、0.1 ms pulse、sweep 5 or 10 ms/division、sensitivity 100 or 200 uV/division、motor filters 10 Hz to 10 kHz。
  - 每側通常取 4-6 stimuli on rastered tracing and superimposed，選 shortest latency。
  - 應等待數秒避免 habituation；stimulator 不應設為 repetitive stimulation。
  - Trigeminal lesion pattern：刺激 affected side 時 ipsilateral R1/R2 與 contralateral R2 全部 delay / absent；刺激 unaffected side 時 responses normal。
  - Facial lesion pattern：所有 affected-side recorded responses abnormal，不論刺激哪一側。
  - Mid-pontine lesion pattern：刺激 affected side 時 R1 absent / delayed，但 ipsilateral and contralateral R2 intact。
  - Medullary lesion pattern：R1 可保留，但 ipsilateral / contralateral R2 pattern 依受影響的 medullary interneuron pathway 改變。
  - Demyelinating peripheral neuropathy 可讓 all blink responses markedly delayed or absent；typical distal dying-back axonal neuropathy 較少影響 blink reflex。
- 發現衝突：
  - 與「blink reflex 只是 facial motor NCS」衝突。
  - 與「R2 延遲就是 facial neuropathy」衝突。
  - 與「R1 absent 一定是 pontine lesion」衝突，因少數正常人 bilateral R1 可能不可靠。
  - 與「blink reflex abnormality 可直接等同單一 disease diagnosis」衝突；其主要價值是 reflex-arc physiology localization clue。
- 待追蹤問題：
  - Facial palsy prognosis、trigeminal sensory neuropathy、brainstem stroke、multiple sclerosis、Guillain-Barre syndrome / CIDP 中 blink reflex 的 test accuracy 需各自用 disease-specific source 補強。
  - 若未來建立 cranial nerve EDX 專區，可把 blink reflex 與 facial NCS、trigeminal sensory testing、brainstem evoked potentials 分開整理。

## [2026-05-11] ingest | Unipolar depression in adults: Indications, efficacy, and safety of transcranial magnetic stimulation (TMS)

- 本輪單一來源：
  - `C:\原始資料\Unipolar depression in adults_ Indications, efficacy, and safety of transcranial magnetic stimulation (TMS).md`
  - 本輪只處理此 UpToDate topic review；未混入 aphasia TMS、stroke motor recovery TMS、autism complementary therapy、TBI neuromodulation、ECT overview、TMS administration protocol 或 treatment-resistant depression guideline 原文。
- 新增來源摘要：
  - `10_來源摘要/UpToDate_unipolar_depression_TMS_indications_efficacy_safety.md`
- 新增頁面：
  - `03_疾病與臨床主題/rTMS_for_Treatment_Resistant_Unipolar_Depression_適應症與安全.md`
- 更新頁面：
  - `index.md`（Total pages 633 -> 635）
  - `log.md`
- 抽出概念：
  - rTMS for treatment-resistant unipolar depression：adult unipolar major depression 在至少一種 antidepressant response 不足後，可考慮 rTMS；surface cortical TMS、theta burst TMS 與 deep TMS 均有 randomized / meta-analytic evidence，但 ECT 對 major depression 的 efficacy 較高，maintenance TMS benefit 尚未確立，且必須做 seizure、metal、cochlear implant、MRI-unsafe implanted device 與 medication / withdrawal risk screening。
- 本輪直接事實：
  - Source 為 UpToDate topic review；literature review current through 2026-04，topic last updated 2025-07-21；source_tier 6。
  - US FDA 於 2008 核准 TMS 用於 treatment-resistant depression。
  - rTMS is indicated for patients with unipolar major depression who have failed at least one antidepressant medication。
  - Standard TMS categories include surface cortical stimulation, theta burst stimulation, and deep stimulation。
  - Surface cortical TMS 是最廣泛研究的 TMS type。
  - High frequency left dorsolateral prefrontal cortex stimulation 與 low frequency right dorsolateral prefrontal cortex stimulation 均有 sham-controlled efficacy evidence。
  - Theta burst TMS 與 deep TMS 也有 efficacy evidence；protocol 間 direct head-to-head evidence 有限。
  - rTMS 通常與 antidepressant pharmacotherapy 併用；同時啟動 TMS plus pharmacotherapy 是否優於 TMS alone 尚未由 randomized trials 確立。
  - ECT 對 major depression 的 efficacy 高於 rTMS。
  - Acute responder 的 TMS benefit 可短期維持，部分可到一年，但維持比例會下降。
  - Maintenance TMS after acute response 的 benefit 尚未確立。
  - Contraindications include seizure disorder、implanted metallic hardware in the magnetic field、metal fragments、cochlear implants、MRI-unsafe implanted electrical devices、ferromagnetic-containing head/neck tattoo ink。
  - Seizure 是最嚴重 adverse effect，但在遵守 safety guideline 時 rare。
  - Seizure risk factors include epilepsy history、preexisting neurologic disorder、proconvulsant medications、recent alcohol / benzodiazepine / anticonvulsant discontinuation、sleep deprivation、higher frequency、higher intensity、shorter intertrain interval。
  - Common adverse effects include headache、scalp pain、transient auditory threshold increase、vasovagal syncope。
  - Randomized evidence summarized by this source does not show cognitive impairment from rTMS in major depression。
- 發現衝突：
  - 與「TMS 是無風險 noninvasive wellness treatment」衝突。
  - 與「TMS efficacy 等同或優於 ECT」衝突。
  - 與「maintenance TMS 是已確立 relapse prevention」衝突。
  - 與「aphasia / stroke motor / chronic pain 的 TMS evidence 可直接外推到 unipolar depression」衝突。
- 待追蹤問題：
  - 若要寫 TMS administration protocol，需單獨處理 `Unipolar major depression: Administering TMS` source 或 device-specific protocol。
  - 若要處理 poststroke depression neuromodulation，應回到 poststroke depression guideline / systematic review，而不能只用本 adult unipolar depression topic review。
  - Treatment-resistant depression sequencing、ECT comparison、ketamine/esketamine comparison 需要各自單一來源。
  - 仍可後續處理 `Oropharyngeal dysphagia_ Clinical features, diagnosis, and management.md`、CRPS UpToDate topics、vascular cognitive impairment topics。

## [2026-05-11] ingest | Oropharyngeal dysphagia: Clinical features, diagnosis, and management

- 本輪單一來源：
  - `C:\原始資料\Oropharyngeal dysphagia_ Clinical features, diagnosis, and management.md`
  - 本輪只處理此 UpToDate topic review；未混入 `Rehabilitation of swallowing disorders` textbook chapter、stroke complications source、palliative dysphagia source、esophageal dysphagia topic、Zenker's diverticulum topic 或 head/neck cancer guideline。
- 新增來源摘要：
  - `10_來源摘要/UpToDate_oropharyngeal_dysphagia_clinical_features_diagnosis_management.md`
- 新增頁面：
  - `03_疾病與臨床主題/Oropharyngeal_Dysphagia_成人臨床辨識診斷與管理.md`
- 更新頁面：
  - `03_疾病與臨床主題/吞嚥障礙復健總論.md`
  - `index.md`（Total pages 635 -> 637）
  - `log.md`
- 抽出概念：
  - Adult oropharyngeal dysphagia clinical pathway：adult oropharyngeal dysphagia 是 difficulty initiating swallowing / transferring food from mouth to pharynx 的 alarm symptom；需先用 symptom timing 區分 esophageal dysphagia 與 globus，再依 history、head/neck/oral exam、cranial nerve neurologic exam、FEES / VFSS / manometry 找 etiology、aspiration severity 與 UES dysfunction，最後用 cause-specific treatment、swallow rehabilitation、diet / maneuver matching、enteral nutrition、cricopharyngeal intervention 或 structural lesion referral 分流。
- 本輪直接事實：
  - Source 為 UpToDate topic review；literature review current through 2026-04，topic last updated 2025-07-15；source_tier 6。
  - Dysphagia is a subjective sensation of difficulty or abnormality of swallowing。
  - Oropharyngeal or transfer dysphagia is characterized by difficulty initiating a swallow。
  - Oropharyngeal dysphagia may include nasopharyngeal regurgitation、aspiration and residual food sensation in the pharynx。
  - Esophageal dysphagia is characterized by difficulty swallowing several seconds after initiating a swallow and food-stuck sensation。
  - Common symptoms include neck-level obstruction sensation、coughing、choking、drooling、regurgitation with liquids or solids、history of aspiration pneumonia、weight loss。
  - Oropharyngeal dysphagia is an alarm symptom that warrants urgent evaluation。
  - Evaluation should determine underlying etiology and assess severity of oropharyngeal dysfunction and degree of aspiration before treatment。
  - Initial evaluation includes oral cavity / head / neck / supraclavicular exam and cranial nerve-focused neurologic exam。
  - Red flags / etiologic clues include malignancy risk factors、otalgia、xerostomia / xerogenic medications、voice or speech changes、Zenker's-like symptoms、late-meal dysphagia suggesting myasthenia gravis、post-intubation context。
  - For suspected neuromuscular disease, source performs VFSS/modified barium swallow and esophageal manometry。
  - For no evidence of systemic disease, source begins with FEES and proceeds to VFSS/manometry if no etiology is found。
  - VFSS permits dynamic functional evaluation of swallowing events, bolus movement, aspiration severity, hyoid/laryngeal elevation, UES relaxation and pharyngeal contraction。
  - FEES is portable bedside structural/function assessment, visualizes secretions and requires specialized training in swallow physiology and flexible endoscopy。
  - FEES and VFSS correlate, but FEES may rate penetration/aspiration risk more severely; clinical significance is uncertain。
  - Manometry quantifies UES pressure/timing and may help identify etiology or myotomy candidates, though it rarely changes management broadly。
  - Management goals are to improve food transfer and prevent aspiration。
  - Swallow rehabilitation is suggested for mild oropharyngeal dysphagia after stroke, head/neck trauma, surgery or degenerative neurologic diseases；source grades this as Grade 2C。
  - Severe dysfunction with aspiration risk may require enteral nutrition。
  - Primary cricopharyngeal dysfunction may be treated with endoscopic or open myotomy；evidence is not randomized and complications exist。
  - Botulinum toxin injection should be reserved for non-surgical/non-dilation candidates in centers of expertise。
  - NMES evidence is heterogeneous and further studies are needed。
- 發現衝突：
  - 與「吞嚥困難先改飲食質地即可，不需找原因」衝突。
  - 與「FEES / VFSS / manometry 可互相替代」衝突。
  - 與「病人指到脖子就一定是 oropharyngeal dysphagia」衝突；source 指出 distal esophageal disease 也可能感覺在 suprasternal notch。
  - 與「globus 就是 dysphagia」衝突；globus criteria 需 absence of dysphagia / odynophagia 等條件。
  - 與「thickened liquids universally safer」衝突；來源把 viscosity / maneuver 與 specific physiologic defect 配對。
  - 與「cricopharyngeal Botox 是 routine low-risk treatment」衝突。
- 待追蹤問題：
  - 若要建立 local VFSS / FEES protocol，需單獨處理 dysphagia clinical practice guideline 或 local imaging / SLP protocol。
  - Esophageal dysphagia、Zenker's diverticulum、head and neck cancer dysphagia、palliative dysphagia、poststroke dysphagia 各需獨立來源，不可由本頁直接外推。
  - NMES、cricopharyngeal myotomy / dilation / Botox 的適應症與效果需後續用 procedure-specific evidence 補強。

## [2026-05-11] ingest | Complex regional pain syndrome in adults: Pathogenesis, clinical manifestations, and diagnosis

- 本輪單一來源：
  - `C:\原始資料\Complex regional pain syndrome in adults_ Pathogenesis, clinical manifestations, and diagnosis.md`
  - 本輪只處理此 UpToDate topic review；未混入 `Complex regional pain syndrome in adults_ Treatment, prognosis, and prevention (1).md`、Bradley / Daroff pain chapter 以外的新 treatment evidence、poststroke shoulder-hand syndrome source、pediatric CRPS source 或 sympathetic block / SCS / ketamine procedure-specific evidence。
- 新增來源摘要：
  - `10_來源摘要/UpToDate_CRPS_pathogenesis_clinical_manifestations_diagnosis.md`
- 新增頁面：
  - `03_疾病與臨床主題/CRPS_Budapest_Criteria與Mimic排除.md`
- 更新頁面：
  - `03_疾病與臨床主題/CRPS_臨床辨識與治療限制.md`
  - `index.md`（Total pages 637 -> 639）
  - `log.md`
- 抽出概念：
  - CRPS Budapest criteria and mimic exclusion：adult CRPS diagnosis 是 clinical pattern recognition + exclusion process；需 continuing disproportionate regional pain，patient-reported symptoms in 3/4 categories，exam signs in 2/4 categories，且 no better diagnosis explains the presentation。Imaging、autonomic testing、bone scan、MRI/CT 與 sympathetic block response 都不能單獨確診。
- 本輪直接事實：
  - Source 為 UpToDate topic review；literature review current through 2026-04，topic last updated 2024-09-03；source_tier 6。
  - CRPS 通常是 distal limb disorder，characterized by pain、swelling、limited range of motion、vasomotor instability、skin changes、patchy bone demineralization。
  - Consensus definition：continuing spontaneous and/or evoked regional pain，disproportionate to trauma/lesion course；pain is regional, not in a specific nerve territory or dermatome；usually distal-predominant sensory、motor、sudomotor、vasomotor and/or trophic findings。
  - CRPS type I 無 peripheral nerve injury evidence，約佔 90% clinical presentations；type II 有 peripheral nerve injury；type I/type II pathophysiologic basis and clinical utility uncertain。
  - Proposed mechanisms include peripheral inflammation/autoimmunity、neurogenic inflammation、catecholamine hypersensitivity、central sensitization、cortical reorganization、glial activation、genetic associations。
  - Population-based incidence reported 5-26 per 100,000 per year；female-to-male ratio 2:1 to 4:1。
  - Common inciting events include fractures、crush injuries、sprains、surgery；up to 10% have no identified precipitating factor。
  - Earlier psychosocial/personality predisposition claims are controversial and not confirmed by later studies。
  - Clinical onset generally occurs within four to six weeks of inciting event。
  - Main clinical manifestations include pain、sensory changes、motor impairments、autonomic symptoms、trophic changes。
  - Pain is typically most prominent and debilitating；sensory abnormalities may include hyperalgesia、allodynia、hypesthesia。
  - Approximately two-thirds have functional motor impairment related to pain；some develop tremor、myoclonus、dystonic postures or impaired movement initiation。
  - Older three-stage model is largely abandoned by most experts due to lack of evidence for discrete stages。
  - Diagnosis is based on history and physical examination；no gold-standard confirmatory test exists。
  - Budapest clinical criteria require continuing disproportionate pain、symptom in 3 of 4 categories、sign in 2 of 4 categories at evaluation、and no better diagnosis。
  - Four categories：sensory、vasomotor、sudomotor/edema、motor/trophic。
  - Budapest criteria cited cohort sensitivity/specificity：82% / 68%。
  - Bone scintigraphy, radiography and autonomic testing may support diagnosis in atypical cases and exclude alternatives；negative bone scan does not rule out CRPS。
  - MRI may help exclude differential diagnoses but is not useful for confirming CRPS；CT is not suggested as a diagnostic test。
  - Positive response to sympathetic block is not diagnostic of CRPS；it may indicate sympathetically maintained pain。
  - Differential diagnoses include infection、compartment syndrome、peripheral vascular disease、DVT、peripheral neuropathy、vascular thoracic outlet syndrome、rheumatoid arthritis、Raynaud phenomenon、erythromelalgia、functional neurological symptom disorder、factitious disorder。
- 發現衝突：
  - 與「CRPS 可由 bone scan / MRI / CT 單獨確診」衝突。
  - 與「sympathetic block response 證明 CRPS」衝突。
  - 與「CRPS 是 psychogenic / personality disorder」衝突。
  - 與「CRPS 一定按 stage 1-2-3 進展」衝突。
  - 與「regional limb pain after trauma 可直接診斷 CRPS、不必排除 DVT / infection / compartment syndrome / vascular disease」衝突。
- 待追蹤問題：
  - CRPS treatment、prognosis、prevention 需另處理 `Complex regional pain syndrome in adults_ Treatment, prognosis, and prevention (1).md`。
  - Poststroke shoulder-hand syndrome / CRPS phenotype-specific evidence 需單獨來源，不可從本 adult general CRPS diagnosis source 直接外推。
  - Sympathetic block、SCS、ketamine、bisphosphonate、steroid 的適應症與限制需 procedure/treatment-specific evidence。

## [2026-05-11] ingest | Complex regional pain syndrome in adults: Treatment, prognosis, and prevention

- 本輪單一來源：
  - `C:\原始資料\Complex regional pain syndrome in adults_ Treatment, prognosis, and prevention (1).md`
  - 本輪只處理此 UpToDate topic review；未混入 pediatric CRPS、CRPS diagnosis source、Bradley / Daroff pain chapter、poststroke shoulder-hand syndrome、sympathetic block procedure protocol、SCS / DRG stimulation procedure source、ketamine protocol、opioid guideline 或 orthopedic fracture guideline 原文。
- 新增來源摘要：
  - `10_來源摘要/UpToDate_CRPS_treatment_prognosis_prevention.md`
- 新增頁面：
  - `03_疾病與臨床主題/CRPS_多模式治療與升階流程.md`
  - `03_疾病與臨床主題/CRPS_預後復發與預防.md`
- 更新頁面：
  - `03_疾病與臨床主題/CRPS_臨床辨識與治療限制.md`
  - `index.md`（Total pages 639 -> 642）
  - `log.md`
- 抽出概念：
  - CRPS multidisciplinary treatment escalation：adult CRPS 治療應以 education、PT/OT、psychosocial assessment 與 individualized analgesia enabling rehabilitation 起始；pain control 的目的不是取代 active rehabilitation，而是讓病人能恢復 affected-limb use；若 response 不佳、症狀進展、severe 或 chronic，才升階至 pain management specialist 與 interventional options。
  - CRPS prognosis / recurrence / prevention：prognosis variable；six-month symptomatic improvement 常見，但 prolonged disability 與 recurrence 不少見；vitamin C after distal radius fracture evidence inconsistent，來源不支持 routine universal prophylaxis，只支持 fracture nutrition 與 selected low-risk supplementation。
- 本輪直接事實：
  - Source 為 UpToDate topic review；literature review current through 2026-04，topic last updated 2025-12-17；source_tier 6。
  - Treatment goals include restoring affected-limb function, decreasing pain and disability, improving quality of life, and minimizing medication toxicity。
  - Treatment is described as more effective when begun early, ideally after diagnosis and before radiographic changes appear。
  - Interventions appropriate for all patients include patient education、PT/OT、psychosocial assessment and symptomatic pain management。
  - PT/OT are considered first-line treatments, though supporting studies have methodologic limitations。
  - Therapist referral is suggested immediately after diagnosis；PT should ideally begin before limitation of movement occurs to maintain range of motion and prevent contractures。
  - Graded motor imagery has small RCT support, but practice translation is uncertain；a 2023 meta-analysis found low-quality evidence for mirror therapy、graded motor imagery、pain exposure therapy and aerobic exercise。
  - Psychosocial / behavioral therapy may help when CRPS duration is more than two months at presentation, treatment response is insufficient, or psychologic / psychiatric comorbidity is suspected。
  - Pharmacologic pain management goals are to allow active participation in rehabilitation and restore movement/strength。
  - Early medication options in the source include NSAID、neuropathic pain adjuvant such as gabapentin / pregabalin / TCA、selected short bisphosphonate course with abnormal bone scan uptake, and topical lidocaine / capsaicin；source grades these as Grade 2C。
  - Gabapentin evidence is limited；pregabalin has not been studied directly in CRPS in this source。
  - Bisphosphonate evidence comes from several small randomized trials, mainly selected early CRPS with abnormal bone scan or osteopenic change。
  - Glucocorticoid evidence is very weak, and chronic CRPS usually does not respond。
  - Ketamine evidence is low to moderate quality；one trial showed benefit through weeks 1-11 but not by week 12, and frequent side effects included psychomimetic symptoms、nausea and vomiting。
  - Opioid use is controversial, with paucity of high-quality CRPS efficacy data；dose escalation may make risk outweigh benefit。
  - IVIG does not appear beneficial for CRPS after a later multicenter trial in chronic CRPS found no pain reduction versus placebo。
  - Pain specialist referral is appropriate for progressive symptoms/signs, unsatisfactory initial response, severe CRPS or chronic CRPS。
  - Sympathetic block evidence is conflicting；small trials often fail to show short-term pain reduction versus sham/placebo or other active comparators, while selected observational data suggest benefit。
  - SCS plus PT reduced pain and improved HRQoL more than PT alone up to two years in one small study, but did not improve functional outcomes and did not show pain difference from three to five years。
  - Sympathectomy has not been tested against placebo/sham RCT and can cause increased pain, new neuropathic pain and bothersome sweating。
  - Symptomatic improvement within six months is common, but prolonged disability occurs。
  - One 102-patient Dutch cohort followed 5.8 years found 64% still fulfilled CRPS criteria and 31% were unable to work。
  - Recurrence estimates range approximately 10-30%；one 1183-patient study found recurrence in 10% and estimated recurrence incidence 1.8% per patient-year。
  - Vitamin C evidence after distal radius fracture is inconsistent；source does not find evidence compelling enough for routine universal use。
  - Source suggests adequate whole-food protein、vitamin C、calcium and vitamin D intake for six to eight weeks after fracture, and considers vitamin C 500 mg daily for six to eight weeks reasonable in distal radius fracture patients with poor baseline nutrition or inability to maintain whole-food intake。
- 發現衝突：
  - 與「CRPS treatment = opioid escalation」衝突。
  - 與「先完全止痛再開始 PT/OT」衝突。
  - 與「bisphosphonate、ketamine、sympathetic block 或 SCS 是 routine early treatment」衝突。
  - 與「sympathetic block response 可診斷 CRPS」衝突；本來源只把 block 放在 refractory pain management。
  - 與「distal radius fracture 後所有人都應 routine vitamin C prophylaxis」衝突。
  - 與「CRPS prognosis 一定良好或一定長期失能」衝突。
- 待追蹤問題：
  - Sympathetic block、SCS / PNS / DRG stimulation、ketamine、opioid、sympathectomy 仍需 procedure-specific or guideline-level source。
  - Poststroke shoulder-hand syndrome / CRPS phenotype-specific treatment 需單獨來源。
  - Pediatric CRPS treatment / recurrence 不可由本 adult source 直接外推。
  - Vitamin C prophylaxis 若要納入 fracture protocol，需另讀 orthopedic guideline 或 updated systematic review。

## [2026-05-11] ingest | Treatment of vascular cognitive impairment and dementia

- 本輪單一來源：
  - `C:\原始資料\Treatment of vascular cognitive impairment and dementia.md`
  - 本輪只處理此 UpToDate topic review；未混入 `Etiology, clinical manifestations, and diagnosis of vascular dementia.md`、Alzheimer disease treatment topic、secondary stroke prevention guideline、antithrombotic topic、dementia behavior management topic、poststroke neuropsychiatric disorder topic 或 local rehab textbook chapter。
- 新增來源摘要：
  - `10_來源摘要/UpToDate_vascular_cognitive_impairment_dementia_treatment.md`
- 新增頁面：
  - `03_疾病與臨床主題/Vascular_Cognitive_Impairment_血管風險與Antithrombotic邊界.md`
  - `03_疾病與臨床主題/Vascular_Dementia_認知藥物與預後限制.md`
- 更新頁面：
  - `03_疾病與臨床主題/Dementia_復健與Caregiver支持框架.md`
  - `03_疾病與臨床主題/中風次發預防.md`
  - `index.md`（Total pages 642 -> 645）
  - `log.md`
- 抽出概念：
  - VCI vascular risk and antithrombotic boundary：VCI/VaD management 先處理 vascular risk and recurrent stroke prevention；但 antithrombotic therapy 需依 clinical stroke/TIA、imaging infarction、stroke subtype and bleeding risk 分流，white matter lesions alone 不是 automatic aspirin indication。
  - VaD cognitive medication and prognosis limits：VaD cognitive medication 只有有限角色；donepezil 或 galantamine 可考慮用於 progressive cognitive decline not directly attributable to clinical stroke，但 benefit slight and clinically uncertain；memantine 不建議 routine；prognosis heterogeneous。
- 本輪直接事實：
  - Source 為 UpToDate topic review；literature review current through 2026-04，topic last updated 2024-09-17；source_tier 6。
  - Vascular dementia refers to dementia primarily caused by cerebrovascular disease or impaired cerebral blood flow。
  - Vascular cognitive impairment includes cognitive disorders in which cerebrovascular disease or impaired cerebral blood flow contributes causally。
  - VaD is best understood as a heterogeneous syndrome rather than a distinct disease。
  - Patients with cognitive impairment and clinical or radiologic evidence of cerebrovascular pathology should be screened and treated for vascular risk factors, especially hypertension。
  - Recurrent stroke is associated with greater risk of cognitive decline；poststroke dementia is associated with higher mortality。
  - Blood pressure lowering strategies have not been specifically tested for treatment of VaD。
  - In symptomatic VaD, source does not suggest intensively lowering systolic blood pressure to less than 120 mmHg。
  - VaD patients with prior clinical ischemic stroke or TIA should receive appropriate antithrombotic therapy according to stroke subtype。
  - If brain imaging shows white matter lesions only, without symptomatic ischemic stroke or imaging evidence of brain infarction, source does not use antithrombotics。
  - If imaging shows brain infarction without clinical stroke history, source often uses aspirin 50-100 mg daily despite limited evidence；bleeding risk / contraindications may lead to avoiding antiplatelet therapy。
  - Source suggests cholinesterase inhibitor therapy for VaD with progressive cognitive decline not directly attributable to clinical stroke；Grade 2B。
  - Source does not initiate cholinesterase inhibitor therapy in dementia diagnosed after stroke when there is no progressive cognitive decline。
  - Many VaD patients have concomitant Alzheimer disease, and AD pathology is difficult to confirm or exclude。
  - Meta-analysis of six cholinesterase inhibitor trials found statistically significant cognitive-scale benefit, but effect was small, about two ADAS-Cog points, and of uncertain clinical significance。
  - Donepezil or galantamine has somewhat better evidence than rivastigmine in this source。
  - Source suggests against memantine use in VaD because evidence for benefit is not compelling。
  - Memantine trials showed benefit on cognitive scales but not clinical global impression or ADL。
  - Lifestyle interventions such as exercise and social interactions are suggested, but high-quality evidence for cognition benefit in established VaD is lacking。
  - Some poststroke rehabilitation programs include cognitive plus physical rehabilitation, but evidence is limited by inconsistent study quality and nonstandardized interventions。
  - After acute stroke, some cognitive recovery is expected；after initial recovery, some patients remain stable while others decline。
  - White matter change severity, medial temporal lobe atrophy, recurrent strokes and impaired baseline cognition before stroke are poor prognostic factors in this source。
  - Population-based studies suggest increased mortality for vascular cognitive impairment, VaD and dementia after stroke。
- 發現衝突：
  - 與「white matter lesions = aspirin indication」衝突。
  - 與「VaD 就照 Alzheimer disease 直接開 donepezil / memantine」衝突。
  - 與「cholinesterase inhibitor 對 VaD 有明確臨床重要效益」衝突。
  - 與「symptomatic VaD 越 aggressive 降 BP 越好」衝突。
  - 與「poststroke dementia 一定持續惡化」衝突。
  - 與「exercise / cognitive rehab 已證實可改善 established VaD cognition」衝突。
- 待追蹤問題：
  - Vascular dementia etiology / diagnosis 需另處理 `Etiology, clinical manifestations, and diagnosis of vascular dementia.md`。
  - Cholinesterase inhibitor dosing、contraindication、monitoring 需另處理 dementia medication-specific source。
  - Behavioral and neuropsychiatric symptom management in VaD 需另處理 dementia behavior management source。
  - Poststroke cognitive rehabilitation intervention dose / outcome 需另用 systematic review 或 rehab guideline。
  - Silent brain infarction / cerebral small vessel disease 的 antithrombotic strategy 需另用 guideline-level source。

## [2026-05-11] ingest | Etiology, clinical manifestations, and diagnosis of vascular dementia

- 本輪單一來源：
  - `C:\原始資料\Etiology, clinical manifestations, and diagnosis of vascular dementia.md`
  - 本輪只處理此 UpToDate topic review；未混入 `Treatment of vascular cognitive impairment and dementia.md`、Alzheimer disease diagnosis / treatment topic、stroke secondary prevention guideline、dementia behavior management topic 或 local rehab textbook chapter。
- 新增來源摘要：
  - `10_來源摘要/UpToDate_vascular_dementia_etiology_clinical_manifestations_diagnosis.md`
- 新增頁面：
  - `03_疾病與臨床主題/Vascular_Dementia_診斷與病因分層.md`
  - `03_疾病與臨床主題/Vascular_Dementia_臨床表現與評估路徑.md`
- 更新頁面：
  - `03_疾病與臨床主題/Vascular_Cognitive_Impairment_血管風險與Antithrombotic邊界.md`
  - `03_疾病與臨床主題/Vascular_Dementia_認知藥物與預後限制.md`
  - `03_疾病與臨床主題/Dementia_復健與Caregiver支持框架.md`
  - `index.md`（Total pages 645 -> 648）
  - `log.md`
- 抽出概念：
  - VaD diagnosis and etiologic stratification：VCID / VaD 是由 cerebrovascular disease 或 impaired cerebral blood flow 造成或參與造成的 cognitive impairment syndrome；診斷需分類 vascular MCI / VaD，確認 stroke history 或 neuroimaging evidence，並判斷 vascular disease 是否足以造成 cognitive impairment。
  - VaD clinical presentation and evaluation pathway：suspected VaD 評估需整合 trajectory、ADL/IADL、stroke timing、MoCA / neuropsychological pattern、neurologic exam、MRI / STRIVE findings、vascular cause assessment 與 AD / Lewy body disease / NPH / depression differential。
- 本輪直接事實：
  - Source 為 UpToDate topic review；literature review current through 2026-04，topic last updated 2025-02-25；source_tier 6。
  - VCID includes vascular dementia and milder impairment such as vascular MCI。
  - VaD is usually recognized when clinical stroke is followed by dementia, or when imaging identifies vascular brain injury in a person with dementia but no clinical stroke history。
  - Neuroimaging evidence of cerebrovascular brain injury alone is not sufficient to diagnose VaD。
  - VaD is a syndrome rather than a single disease。
  - VaD diagnosis is not complete until the underlying cerebrovascular or cardiovascular damage has been characterized。
  - Vascular disease is a cause or contributor in 25 to 50 percent of dementia cases in this source。
  - Pure VaD is relatively uncommon in clinicopathologic dementia specialty clinic studies, approximately 10 percent of all dementia cases。
  - Multiple-etiology dementia with vascular component, often with AD, accounts for approximately 30 to 40 percent of all dementia cases in those studies。
  - Any cause of ischemic stroke, intracerebral hemorrhage, or subarachnoid hemorrhage can cause VaD if brain injury is severe enough。
  - Cerebral small vessel disease has an outsized role in VaD burden。
  - Consensus criteria share three common elements: classify as vascular MCI or VaD, identify cerebrovascular disease by history or neuroimaging, and judge vascular disease sufficient to cause cognitive impairment。
  - Newer criteria do not require memory impairment；significant impairment in only one domain can be sufficient when functional criteria are met。
  - The two main VaD syndromes are poststroke dementia and VaD without recent stroke。
  - Poststroke dementia often features executive dysfunction with relative episodic memory sparing, but clinical profile varies by stroke location and size。
  - New dementia one to five years after stroke occurs in approximately 10 to 30 percent of patients in systematic reviews cited by this source。
  - VaD without recent stroke may show progressive or stepwise decline with imaging evidence of clinically unrecognized, better termed covert, cerebrovascular disease。
  - Arteriolosclerotic cerebral small vessel disease tends to impair executive function and processing speed, but other domains may also be affected。
  - VaD can be accompanied by depression、abulia、apathy、psychosis、pseudobulbar affect、gait slowing / lower-body parkinsonism and urinary frequency。
  - MoCA appears more sensitive than MMSE for detecting VCID, but cognitive screening does not substitute for integrated clinical diagnosis。
  - MRI is preferred over CT for cerebral small vessel disease and microbleeds unless cost or contraindication prevents MRI。
  - Differential diagnosis includes AD、Lewy body diseases / Parkinson disease dementia、NPH and depression；many dementia cases have multiple causes。
- 發現衝突：
  - 與「MRI 有 white matter lesion 就等於 VaD」衝突。
  - 與「沒有 clinical stroke history 就不能診斷 VaD」衝突。
  - 與「VaD 是單一 disease entity」衝突。
  - 與「VaD 通常是 pure vascular pathology」衝突；multiple-etiology dementia 常見。
  - 與「VaD 一定是 stair-step decline」衝突；covert small vessel disease 可 smooth progressive。
  - 與「memory 必須受損才可診斷 dementia / VaD」衝突。
- 待追蹤問題：
  - AD biomarker、amyloid PET、CSF beta-amyloid / phosphorylated tau 的臨床使用需另讀 AD diagnosis source。
  - Cerebral amyloid angiopathy diagnostic criteria and antithrombotic risk 需另讀 CAA source。
  - CADASIL 與 hereditary small vessel disease 不可由本 general VaD source 完整處理。
  - Silent brain infarction / cerebral small vessel disease 的 prevention strategy 仍需 guideline-level source。
  - Poststroke cognitive rehabilitation intervention dose / outcome 需另用 systematic review 或 rehab guideline。

## [2026-05-12] ingest | Antihypertensive therapy for secondary stroke prevention

- 本輪單一來源：
  - `C:\原始資料\Antihypertensive therapy for secondary stroke prevention.md`
  - 本輪只處理此 UpToDate topic review；未混入 `Overview of secondary prevention of ischemic stroke.md`、`Long-term antithrombotic therapy for the secondary prevention of ischemic stroke.md`、acute ischemic stroke BP protocol、ICH acute BP protocol、SAH treatment topic、hypertension guideline 原文或 vascular dementia treatment topic。
- 新增來源摘要：
  - `10_來源摘要/UpToDate_antihypertensive_therapy_secondary_stroke_prevention.md`
- 新增頁面：
  - `03_疾病與臨床主題/Stroke_Antihypertensive_Therapy_次發預防.md`
- 更新頁面：
  - `03_疾病與臨床主題/中風次發預防.md`
  - `03_疾病與臨床主題/Vascular_Cognitive_Impairment_血管風險與Antithrombotic邊界.md`（新增 BP secondary prevention cross-link）
  - `index.md`（Total pages 648 -> 650）
  - `log.md`
- 抽出概念：
  - Stroke antihypertensive therapy for secondary prevention：stroke / TIA 後降血壓治療需依 acute vs chronic phase、neurologic stability、stroke type、ASCVD risk、tolerability and cerebral perfusion risk 決定 timing、drug class、target intensity and titration speed；不能把 acute permissive hypertension 和 long-term BP goal 混用。
- 本輪直接事實：
  - Source 為 UpToDate topic review；literature review current through 2026-04，topic last updated 2025-09-12；source_tier 6。
  - Hypertension is a major risk factor for stroke and TIA。
  - Among patients with prior stroke or TIA, antihypertensive therapy can reduce recurrence。
  - Acute stroke BP management differs from chronic secondary prevention therapy。
  - Previously treated, neurologically stable patients with known hypertension should resume antihypertensive therapy for recurrent stroke and other vascular event prevention。
  - Previously untreated, neurologically stable patients with any stroke type or TIA and established BP above goal should start antihypertensive therapy。
  - TIA patients who returned to baseline without infarction evidence can initiate or reinstate oral antihypertensive therapy without delay。
  - Acute ischemic stroke generally tolerates permissive hypertension during first 24-48 hours, except for extreme hypertension, end-organ failure, active ischemic coronary disease, aortic dissection, preeclampsia/eclampsia or reperfusion-therapy BP threshold。
  - Stable or improving ischemic stroke patients able to receive oral / enteral medication generally start or resume antihypertensive therapy 24-48 hours after onset and during hospitalization。
  - Ischemic stroke patients with fluctuating deficits or progressive deterioration should delay antihypertensive therapy until deficits stabilize or reach nadir。
  - Spontaneous ICH often requires IV antihypertensive treatment in acute phase, then transition to oral therapy when appropriate。
  - SAH secondary prevention antihypertensive therapy starts when cerebral perfusion pressure is judged adequate。
  - ACE inhibitors, ARBs, calcium channel blockers and diuretics are reasonable initial monotherapy options。
  - Beta blockers should not be used for recurrent stroke prevention unless there is another compelling indication。
  - Combination therapy is recommended when BP is >=20/10 mmHg above goal; source uses angiotensin inhibitor plus long-acting dihydropyridine calcium channel blocker。
  - Meta-analysis of eight trials and over 35,000 prior stroke/TIA patients found antihypertensive therapy reduced stroke rate and cardiovascular death。
  - Ischemic stroke/TIA with atherosclerotic disease generally uses a more intensive BP goal if tolerated。
  - Cardioembolic stroke or paradoxical embolus is not by itself evidence of atherosclerotic cardiovascular disease。
  - Spontaneous ICH recurrence prevention uses a more intensive BP goal similar to ischemic stroke due to atherosclerotic disease in this source。
  - Optimal BP goal for recurrent SAH prevention is unknown。
  - Known cerebrovascular disease or long-standing uncontrolled hypertension should undergo gradual BP reduction, approximately 10 percent per day, unless hypertensive emergency exists。
- 發現衝突：
  - 與「acute ischemic stroke BP 高就立即壓到 <130/80」衝突。
  - 與「permissive hypertension 可以延續到出院後」衝突。
  - 與「beta blocker 可作 post-stroke recurrent stroke prevention default」衝突。
  - 與「所有 ischemic stroke / TIA 都同一個 intensive BP target」衝突；cardioembolic / paradoxical embolus 需看是否另有 ASCVD or high-risk condition。
  - 與「stroke 後降壓速度越快越好」衝突；chronic hypertension / cerebrovascular disease 情境需要 gradual titration。
- 待追蹤問題：
  - Long-term BP target in severe frailty、advanced dementia、orthostatic hypotension、institutionalized patients 需另讀 hypertension guideline / geriatrics source。
  - Spontaneous ICH secondary prevention and long-term prognosis 需另處理 dedicated source，不可只用本 source 補全部 ICH recurrence strategy。
  - SAH recurrence prevention BP target remains uncertain；若要建立 SAH long-term prevention 頁，需 dedicated source。
  - Poststroke cognitive rehabilitation intervention dose / outcome 仍需另用 systematic review 或 rehab guideline。

## [2026-05-12] ingest | Moyamoya disease and moyamoya syndrome: Etiology, clinical features, and diagnosis

- 本輪單一來源：
  - `C:\原始資料\Moyamoya disease and moyamoya syndrome_ Etiology, clinical features, and diagnosis.md`
  - 本輪只處理此 UpToDate topic review；未混入 `Moyamoya disease and moyamoya syndrome_ Treatment and prognosis.md`、AHA/ASA scientific statement 原文、Japanese diagnostic criteria 原文、pediatric stroke guideline 或 intracranial atherosclerosis / dissection / RCVS dedicated sources。
- 新增來源摘要：
  - `10_來源摘要/UpToDate_moyamoya_etiology_clinical_features_diagnosis.md`
- 新增頁面：
  - `03_疾病與臨床主題/Moyamoya_Disease與Moyamoya_Syndrome_病因分層.md`
  - `03_疾病與臨床主題/Moyamoya_臨床辨識與診斷影像.md`
- 更新頁面：
  - `03_疾病與臨床主題/Spontaneous_ICH_診斷與病因分層.md`（新增 moyamoya cross-link 與來源）
  - `index.md`（Total pages 650 -> 653）
  - `log.md`
- 抽出概念：
  - MMD versus MMS etiologic stratification：moyamoya 是 distal ICA / circle of Willis stenosis plus collateral vessels 的 angiographic pattern；MMD 是 primary / idiopathic pattern，MMS 則需要追查 associated medical condition。
  - Clinical recognition and diagnostic imaging：recurrent / triggered TIA、young stroke、unexplained caudate / thalamic / IVH、basal ganglia flow voids、distal ICA stenosis and collaterals 應觸發 CTA/MRA/DSA pathway。
- 本輪直接事實：
  - Source 為 UpToDate topic review；literature review current through 2026-04，topic last updated 2025-04-21；source_tier 6。
  - Moyamoya refers to unilateral or bilateral stenosis / occlusion around the circle of Willis with prominent arterial collateral circulation。
  - MMD is moyamoya angiographic findings with associated genetic susceptibility but no underlying contributing medical condition。
  - MMS is moyamoya angiographic findings with an associated medical condition implicated in vascular change。
  - Pathophysiology involves vessel wall thickening and angiogenesis。
  - Terminal ICAs and proximal MCA / ACA are most involved。
  - Some unilateral cases progress to bilateral involvement in approximately one-third of patients over two to eight years。
  - RNF213 p.R4810K is a susceptibility factor in East Asian populations and is associated with earlier onset / more severe progression in this source。
  - MMD / MMS are rare; cited incidence is 0.35 to 0.94 per 100,000 and prevalence is 3.2 to 10.5 per 100,000。
  - Age distribution is bimodal, with peaks at 5 to 10 years and 30 to 50 years。
  - Ischemic stroke or TIA is the most common presentation in children and adults。
  - Ischemic episodes may be spontaneous or triggered by exercise, crying, coughing, straining, fever or hyperventilation。
  - Hemorrhagic complications account for approximately 25 to 30 percent of presentations, mostly in adults。
  - ICH typically occurs in basal ganglia, thalamus and/or ventricular system。
  - MRI ivy sign and brush sign can support impaired collateral flow / reserve but are not specific。
  - Multiple punctate or serpentine T2 flow voids in basal ganglia or thalamus are considered virtually diagnostic by this source。
  - MRA is preferred initial imaging in children; CTA is commonly used in acute stroke evaluation。
  - DSA is the gold standard and is required for unilateral or nondiagnostic noninvasive findings。
  - DSA diagnostic criteria can diagnose unilateral or bilateral moyamoya findings。
  - Differential diagnosis includes intracranial atherosclerosis, arterial dissection, RCVS, focal cerebral arteriopathy and vasculitis。
  - General asymptomatic screening is not recommended; screening may be reasonable with strong family history or MMS-predisposing condition, but benefit remains uncertain。
- 發現衝突：
  - 與「moyamoya 一定是 bilateral disease」衝突。
  - 與「moyamoya = idiopathic MMD」衝突；MMS 需找 associated condition。
  - 與「ivy sign / brush sign 就能診斷 moyamoya」衝突。
  - 與「adult deep ICH 都可先當 hypertensive ICH」衝突；無典型 risk factors 或有 IVH / caudate / thalamic pattern 時需考慮 moyamoya。
  - 與「asymptomatic relatives 都要 routine screening」衝突。
- 待追蹤問題：
  - Moyamoya treatment / prognosis / revascularization / antiplatelet strategy 需另處理 `Moyamoya disease and moyamoya syndrome_ Treatment and prognosis.md`。
  - AHA/ASA adult moyamoya scientific statement 原文可作 guideline-level correction。
  - Pediatric moyamoya / sickle cell disease 需另讀 pediatric stroke / sickle cell source。
  - Intracranial atherosclerosis、arterial dissection、RCVS、focal cerebral arteriopathy、vasculitis 需各自 dedicated source，不可由本來源完整處理。

## [2026-05-12] ingest | Moyamoya disease and moyamoya syndrome: Treatment and prognosis

- 本輪單一來源：
  - `C:\原始資料\Moyamoya disease and moyamoya syndrome_ Treatment and prognosis.md`
  - 本輪只處理此 UpToDate topic review；未混入 AHA/ASA scientific statement 原文、Japanese guideline 原文、sickle cell disease stroke topic、pregnancy anesthesia topic 或 acute stroke thrombolysis guideline。
- 新增來源摘要：
  - `10_來源摘要/UpToDate_moyamoya_treatment_prognosis.md`
- 新增頁面：
  - `03_疾病與臨床主題/Moyamoya_治療決策與Revascularization.md`
  - `03_疾病與臨床主題/Moyamoya_Antithrombotic與急性支持管理.md`
- 更新頁面：
  - `03_疾病與臨床主題/Moyamoya_Disease與Moyamoya_Syndrome_病因分層.md`
  - `03_疾病與臨床主題/Moyamoya_臨床辨識與診斷影像.md`
  - `10_來源摘要/UpToDate_moyamoya_etiology_clinical_features_diagnosis.md`
  - `index.md`（Total pages 653 -> 656）
  - `log.md`
- 抽出概念：
  - Moyamoya treatment decision and revascularization：symptomatic moyamoya 或 hemodynamic compromise 需 referral for surgical revascularization；asymptomatic preserved-flow patients 可 medical management plus serial surveillance。
  - Moyamoya antithrombotic and acute supportive management：ischemic-type moyamoya 可使用 antiplatelet strategy；hemorrhagic-type acute/recovery 多數避免 antiplatelet；long-term anticoagulation generally contraindicated；急性/圍手術期需避免 hyperventilation、hypovolemia and hypotension。
- 本輪直接事實：
  - Source 為 UpToDate topic review；literature review current through 2026-04，topic last updated 2026-01-02；source_tier 6。
  - Moyamoya is progressive and has no curative treatment。
  - Surgical revascularization is suggested for symptomatic children and adults with cerebral ischemia, TIA, ischemic stroke, cognitive decline or hemorrhage when no contraindication exists。
  - Surgical revascularization is also suggested for asymptomatic children and adults with decreased regional cerebral blood flow or inadequate hemodynamic perfusion reserve。
  - Asymptomatic patients with preserved cerebral blood flow may continue medical management plus follow-up surveillance imaging。
  - Surveillance imaging may be yearly, shorter at six months when severe stenosis is found initially, and every other year or longer in stable adult patients after at least three years。
  - MRA is generally preferred for surveillance vascular imaging；CTA is an alternative；DSA is usually reserved for nondiagnostic noninvasive testing or presurgical planning。
  - Direct revascularization provides immediate flow augmentation；indirect revascularization promotes delayed collateralization and is frequently used in children；combined procedures use both。
  - No single revascularization method is convincingly universally superior in this source。
  - Surgical evidence is limited by observational design, selection bias and heterogeneous outcomes, but meta-analyses associate surgery with lower subsequent stroke risk than conservative care。
  - Perioperative stroke, delayed transient neurologic deficits and hyperperfusion syndrome are important surgical complications。
  - Long-term untreated cohorts reported progressive neurologic deficits and poor outcomes in 50 to 66 percent。
  - For most adult ischemic-type moyamoya, source suggests cilostazol 100 mg twice daily over other antiplatelet agents；aspirin 50-100 mg daily or clopidogrel 75 mg daily are alternatives when cilostazol is not tolerated or contraindicated。
  - For children with ischemic-type moyamoya, source suggests aspirin 2-5 mg/kg daily；pediatric cilostazol / clopidogrel data are limited。
  - For most hemorrhagic-type moyamoya, antiplatelet therapy is avoided acutely and during recovery。
  - Long-term anticoagulation is generally contraindicated；short-term anticoagulation safety is not established。
  - Pregnant patients should maintain hydration；low-dose aspirin is typically used；Cesarean delivery is not proven outcome-superior and delivery planning should be individualized。
  - Acute ischemic stroke management is mainly supportive and includes minimizing hyperventilation, pain/agitation, hypovolemia and hypotension。
  - IV thrombolysis lacks randomized-trial evidence in moyamoya and may be considered only individually for selected disabling ischemic stroke without brain hemorrhage history after risk-benefit discussion。
- 發現衝突：
  - 與「moyamoya 只靠 antiplatelet 追蹤即可」衝突。
  - 與「asymptomatic moyamoya 不需要 serial surveillance」衝突。
  - 與「direct / indirect / combined bypass 有單一 universal best method」衝突。
  - 與「moyamoya ischemic stroke prevention 可以常規 long-term anticoagulation」衝突。
  - 與「hemorrhagic moyamoya acute phase 照常 antiplatelet」衝突。
  - 與「pregnant moyamoya 一律 Cesarean」衝突。
- 待追蹤問題：
  - AHA/ASA moyamoya scientific statement 原文仍需 guideline-level correction。
  - Pediatric sickle cell disease-associated MMS 需 dedicated sickle cell stroke source。
  - Revascularization technique choice、perioperative anesthesia、BP / CO2 targets 需 neurosurgical or anesthesia protocol source。
  - Acute thrombolysis in moyamoya 需 dedicated acute stroke evidence / guideline source。

## [2026-05-12] ingest | Clinical diagnosis of stroke subtypes

- 本輪單一來源：
  - `C:\原始資料\Clinical diagnosis of stroke subtypes.md`
  - 本輪只處理此 UpToDate topic review；未混入 `Stroke_ Etiology, classification, and epidemiology.md`、`Overview of the evaluation of stroke.md`、`Pathophysiology of ischemic stroke.md`、`Stroke in patients with atrial fibrillation.md`、ICH / SAH treatment topics 或 stroke guideline 原文。
- 新增來源摘要：
  - `10_來源摘要/UpToDate_clinical_diagnosis_stroke_subtypes.md`
- 新增頁面：
  - `03_疾病與臨床主題/Stroke_Subtype_Clinical_Diagnosis.md`
- 更新頁面：
  - `03_疾病與臨床主題/中風復健總論.md`
  - `03_疾病與臨床主題/中風急性期處置與時間窗.md`
  - `index.md`（Total pages 656 -> 658）
  - `log.md`
- 抽出概念：
  - Stroke subtype clinical diagnosis：以 symptom onset/course、associated symptoms、risk factors、general physical exam 與 neurologic exam 建立 ischemic thrombotic / embolic / hypoperfusion、ICH、SAH 的 presumptive diagnosis；但最終仍需 brain / vascular imaging confirmation。
- 本輪直接事實：
  - Source 為 UpToDate topic review；literature review current through 2026-04，topic last updated 2026-02-10；source_tier 6。
  - Stroke subtype 包含 ICH、SAH、以及 due to thrombosis、embolism、systemic hypoperfusion 的 brain ischemia。
  - Thrombosis 指 local in situ arterial obstruction，可由 arterial wall disease 如 atherosclerosis、dissection、fibromuscular dysplasia 造成。
  - Thrombotic stroke 可分 large vessel and small vessel disease。
  - Thrombosis-related symptoms often fluctuate、remit or progress in stuttering fashion。
  - Embolism 指 elsewhere debris blocking arterial access；可源自 heart、aorta or large vessels。
  - Embolic stroke 通常 abrupt and maximal at onset；multiple vascular territories favor cardiac or aortic source。
  - Systemic hypoperfusion 是 global circulatory problem，症狀通常 diffuse and nonfocal，可有 bilateral signs。
  - ICH 通常來自 arterioles / small arteries，出血進入 brain tissue，neurologic symptoms 多在 minutes or hours 內 gradually increase。
  - SAH from aneurysm rupture releases blood into CSF under arterial pressure，通常 abrupt onset，severe widespread headache 是核心症狀。
  - The most important historical item for differentiating subtypes is pace / course / clearing of symptoms and signs。
  - Acute ischemic stroke neurologic deterioration 48-72h 內在 cited prospective study 中發生於 256/1964 patients（13%）。
  - Deterioration predictors included ICA occlusion、brainstem infarction、MCA M1 occlusion、territorial infarction and diabetes mellitus。
  - Silent brain infarcts 更適合稱為 covert brain infarcts；它們可能和 cognitive deficits、future stroke risk and dementia risk 相關。
  - Ecology and risk factors increase probability but cannot make a firm subtype diagnosis。
  - AF 是 prominent cardiac risk factor and causes nearly half of cardioembolic strokes in this source。
  - Hypertension 是 most common and most important stroke risk factor，且 severe uncontrolled hypertension strongly favors ICH。
  - Same-territory prior TIAs favor local vascular lesion / thrombosis；multi-territory attacks suggest heart / aorta embolism；TIAs are not a feature of brain hemorrhage。
  - Fever raises suspicion for endocarditis-related embolic stroke。
  - Severe headache at onset favors SAH；headache after onset plus worsening neurologic signs、decreased consciousness and vomiting favors ICH。
  - Vomiting is common in ICH、SAH and posterior circulation large artery ischemia。
  - Acute seizures are more often seen in lobar ICH or brain embolism；population-based cited incidence within first 24h: SAH 10%、ICH 8%、ischemic stroke 3%。
  - Neurologic signs localize brain region more than they identify stroke subtype。
  - Pure motor stroke favors penetrating artery thrombotic stroke or small ICH。
  - Vertigo、staggering、diplopia、deafness、crossed signs、bilateral motor/sensory signs and hemianopsia suggest posterior circulation involvement。
  - Neuroimaging is necessary to identify hemorrhage, assess brain injury and identify the vascular lesion responsible for ischemic deficit。
  - NT-proBNP and D-dimer may have stronger biomarker data for mechanism differentiation, but no biomarkers have sufficient sensitivity or specificity for routine clinical use。
- 發現衝突：
  - 與「history / exam 足以確診 stroke subtype」衝突。
  - 與「AF 自動等於 cardioembolic stroke」衝突；AF 只提高機率，仍需完整評估其他原因。
  - 與「headache / vomiting 一律代表 hemorrhage」衝突；posterior circulation ischemia 也可 vomiting。
  - 與「pure motor stroke 一定是 lacunar infarct」衝突；small ICH 也可能。
  - 與「silent brain infarct 沒臨床意義」衝突；來源支持改稱 covert brain infarct 並指出 cognitive and future-risk relevance。
  - 與「blood biomarkers 可常規分類 stroke mechanism」衝突。
- 待追蹤問題：
  - `Stroke_ Etiology, classification, and epidemiology.md` 應另行單一來源 ingest，補 etiologic classification / epidemiology。
  - `Overview of the evaluation of stroke.md` 應另行處理，補 imaging / lab / diagnostic pathway。
  - `Posterior circulation cerebrovascular syndromes.md` 應另行處理，補 posterior circulation localization 與 mimic。
  - `Stroke in patients with atrial fibrillation.md` 應另行處理，修正 AF stroke mechanism、acute reperfusion contraindications 與 anticoagulation timing。
  - Covert brain infarct / silent brain infarction 的 prevention strategy 需 guideline-level source。

## [2026-05-12] update | wiki governance workflow

- 更新原因：
  - 吸收 Hermes `llm-wiki` skill 中適合本 repo 的治理層優點，但不採用多來源 batch ingest。
- 更新規則：
  - `AGENTS.md` 新增 session orientation、source manifest / source drift、index scaling 與 archive policy。
  - `SCHEMA.md` 對齊 `AGENTS.md`：來源優先序改回 guideline / textbook / systematic review / review / original research / UpToDate 等階層，ingest 明確維持單一來源。
  - `08_工具與Workflow/知識百科_ingest_工作流.md` 移除 5-file batch ingest，改為每輪單一來源與 `待處理來源` queue。
- 新增頁面：
  - `08_工具與Workflow/Source_Manifest與Source_Drift.md`
- 更新腳本：
  - `08_工具與Workflow/wiki_health_check.py` 改用 `10_來源摘要`，納入 `09_NCV EMG 周邊神經病變`。
  - 新增 `--update-source-manifest`，可由來源摘要中的 `source_path` / `原始檔：...` 建立 `source_manifest.json`。
  - 新增 `source_manifest_missing`、`source_drift`、`raw_source_missing`、`source_manifest_orphans` health check 欄位。
- 執行驗證：
  - `python -m unittest C:\知識百科\08_工具與Workflow\tests\test_wiki_health_check.py`：7 tests passed。
  - 已重跑 `health_check_report_latest.md`；目前 source_manifest_missing 0、source_drift 0、raw_source_missing 0。
- 待追蹤問題：
  - 既有 health check 仍回報 25 個 orphan pages、49 個 weakly linked pages、16 個 broken links、41 個 stale candidates、21 個 contradiction candidates、60 個 raw backlog。

## [2026-05-12] ingest | Exercise ECG testing: Performing the test and interpreting the ECG results

- 本輪單一來源：
  - `C:\原始資料\Exercise ECG testing_ Performing the test and interpreting the ECG results.md`
  - 本輪只處理此 UpToDate topic review；未混入 `Treadmill Stress Testing - StatPearls.md`、stress imaging source、CPET guideline、coronary prognosis source 或其他 exercise physiology raw source。
- 新增來源摘要：
  - `10_來源摘要/UpToDate_exercise_ECG_testing_performing_interpreting.md`
- 新增頁面：
  - `02_方法學/Exercise_ECG_Testing_適用條件與安全流程.md`
  - `02_方法學/Exercise_ECG_ST_Segment_判讀.md`
- 更新頁面：
  - `index.md`（Total pages 659 -> 662）
  - `log.md`
- 抽出概念：
  - Exercise ECG testing 適用條件與安全流程：exercise ECG without imaging 需要 adequate exercise capacity、interpretable resting ECG、沒有 absolute contraindications，並以 symptom-limited incremental exercise 監測 ECG、HR、BP、symptoms、RPE and recovery response。
  - Exercise ECG ST segment 判讀：ischemic ECG 判讀以 ≥1 mm horizontal / downsloping ST depression persisting 80 ms after J point、ST elevation pattern、lead distribution、recovery ST depression and ventricular ectopy 為核心，但需放入 baseline ECG、workload、symptoms and BP response。
- 本輪直接事實：
  - Source 為 UpToDate topic review；literature review current through 2026-04，topic last updated 2024-04-26；source_tier 6。
  - Exercise ECG 可用於 CHD diagnosis / prognosis and exercise capacity assessment。
  - Serious complications such as MI, sustained ventricular arrhythmia or death 約 1 in 10,000 tests。
  - Absolute contraindications 包含 acute MI within 2 days、ongoing unstable angina、uncontrolled arrhythmia with hemodynamic compromise、symptomatic severe valvular stenosis、decompensated heart failure、active endocarditis、acute myocarditis / pericarditis、acute aortic dissection、acute PE / pulmonary infarction / DVT、以及 inability to perform safe and adequate testing。
  - Exercise ECG 不適合用於無法充分 exercise 或 resting ECG 會干擾 ischemia interpretation 的病人；例子包括 WPW、ventricular paced rhythm、LBBB、>1 mm resting ST depression、digoxin-related ST-T abnormalities、LVH with ST-T abnormalities and hypokalemia with ST-T abnormalities。
  - Exercise test should generally be symptom-limited；達到 85-90 percent predicted maximal HR 不應作為多數情境的唯一 stop point。
  - BP 應在 rest and each stage last minute 監測；systolic BP 應隨 exercise stage 上升，diastolic BP 多下降或不變。
  - Recovery ECG 應每分鐘記錄約 7-10 minutes，直到 HR <100 bpm 或 ECG 回到 baseline pattern。
  - Exercise ECG abnormal ischemia criterion commonly uses ≥1 mm horizontal or downsloping ST depression in one or more leads persisting 80 ms after the J point。
  - Upsloping ST depression 較不 specific；納入 upsloping ST depression 可增加 sensitivity 但降低 specificity。
  - V4、V5、V6 是 detecting ST depression 的敏感 leads；V5 often best single lead。
  - ST depression in lateral precordial leads does not localize culprit coronary artery；inferior-only ST depression often false positive。
  - Recovery-only ST depression has diagnostic / prognostic significance similar to exercise-phase ST depression in cited studies。
  - Exercise-induced ventricular ectopy occurs in 7-20 percent of patients undergoing exercise ECG for known or suspected CHD；frequent ventricular ectopy during recovery may be the more prognostically relevant signal。
- 發現衝突：
  - 與「達到 85 percent predicted maximal HR 就一定要停止 exercise ECG」衝突。
  - 與「未達 adequate exercise stress 的 negative test 仍可可靠排除 ischemia」衝突。
  - 與「baseline LBBB / ventricular pacing 仍可用 exercise ST depression 判讀 ischemia」衝突。
  - 與「upsloping ST depression 和 horizontal / downsloping ST depression 一樣 specific」衝突。
  - 與「exercise ST depression 可以 reliably localize culprit artery」衝突。
  - 與「recovery ECG findings 不重要」衝突。
  - 與「exercise ECG testing 等同 CPET」衝突。
- 待追蹤問題：
  - 需另行處理 stress test selection / stress imaging source，補 exercise ECG vs imaging / pharmacologic stress testing selection。
  - 需另行處理 Duke treadmill score / stress test prognosis source，補 risk stratification。
  - 需另行處理 CPET cardiovascular disease source，避免把 exercise ECG protocol 直接外推到 gas-exchange CPET。
  - `Treadmill Stress Testing - StatPearls.md` 層級較低，若未來要處理應作補充或比較來源，不可覆寫 UpToDate / guideline-based framework。

## [2026-05-12] ingest | Overview of the evaluation of stroke

- 本輪單一來源：
  - `C:\原始資料\Overview of the evaluation of stroke.md`
  - 本輪只處理此 UpToDate topic review；未混入 `Stroke_ Etiology, classification, and epidemiology.md`、`Posterior circulation cerebrovascular syndromes.md`、`Stroke in patients with atrial fibrillation.md`、`Lacunar infarcts.md` 或 stroke guideline 原文。
- 新增來源摘要：
  - `10_來源摘要/UpToDate_overview_evaluation_of_stroke.md`
- 新增頁面：
  - `03_疾病與臨床主題/Stroke_Evaluation_病因確認與Directed_Diagnostic_Testing.md`
- 更新頁面：
  - `03_疾病與臨床主題/Stroke_Subtype_Clinical_Diagnosis.md`
  - `03_疾病與臨床主題/Acute_Stroke_Initial_Assessment與Stabilization.md`
  - `03_疾病與臨床主題/中風急性期處置與時間窗.md`
  - `03_疾病與臨床主題/中風復健總論.md`
  - `index.md`（Total pages 662 -> 664）
  - `log.md`
- 抽出概念：
  - Stroke evaluation from presumptive diagnosis to directed testing：suspected stroke evaluation 先完成 vital stability、hemorrhage / reperfusion triage，再用 history、physical examination and initial CT / MRI 形成 presumptive mechanism，最後用 neurovascular imaging、cardiac monitoring / echocardiography、selected blood tests 或 ICH-focused workup 確認 pathophysiology。
- 本輪直接事實：
  - Source 為 UpToDate topic review；literature review current through 2026-04，topic last updated 2025-07-01；source_tier 6。
  - Symptoms do not accurately reflect infarction presence，symptom tempo does not identify ischemia cause。
  - Initial evaluation includes classification、rapid stabilization、hemorrhage detection、reperfusion candidacy assessment、presumptive etiology formation and directed diagnostic confirmation。
  - Noncontrast CT is typically the first diagnostic study in suspected stroke because it is fast、available and sensitive for acute hemorrhage。
  - MRI is more sensitive than CT for early brain infarction；DWI / FLAIR are useful early after onset。
  - In ischemia without infarction, CT and MRI may both be normal。
  - A presumptive diagnosis can be made after history、physical examination and CT/MRI, but confirmation requires more extensive testing。
  - Brain imaging and comprehensive neurovascular evaluation should be obtained for most suspected acute ischemic stroke or TIA patients。
  - Embolic stroke is favored by sudden maximal onset、large deficit / infarct、known cardiac or large artery lesion、hemorrhagic infarct、multiple vascular territories or rapid improvement。
  - Suspected large-vessel atherothrombotic stroke requires both intracranial and extracranial vascular testing。
  - Cardiac evaluation is essential in most brain ischemia patients。
  - All ischemic stroke patients should have at least 24 hours of cardiac monitoring after onset to look for subclinical AF。
  - For cryptogenic ischemic stroke / TIA with no AF on ECG and 24-hour monitoring, the source suggests several weeks of ambulatory monitoring。
  - All suspected embolic stroke patients should have echocardiography。
  - TTE is often preferred initial test for most suspected cardiac/aortic embolic sources；TEE is preferred in selected high-yield scenarios and better evaluates left atrial appendage clot、atria、atrial septum、aorta and PFO / ASD / atrial septal aneurysm。
  - Hypercoagulable testing indications are limited；causal link between inherited thrombophilia and arterial stroke remains unclear。
  - Every intracranial hemorrhage patient requires bleeding-disorder evaluation, especially if cause is not immediately apparent。
  - Typical hypertensive ICH may require no further diagnostic testing when severe hypertension and characteristic hematoma location/appearance are present。
  - Lobar or atypical hemorrhage raises suspicion for cerebral amyloid angiopathy、tumor or vascular malformation。
- 發現衝突：
  - 與「CT normal 就排除 ischemia」衝突。
  - 與「symptom tempo alone 可以確定 stroke cause」衝突。
  - 與「AF、carotid stenosis 或 lacunar-like syndrome 自動證明病因」衝突。
  - 與「所有 ischemic stroke 都 routine 做 hypercoagulable panel」衝突。
  - 與「lobar / atypical ICH 可直接歸因於 hypertension」衝突。
- 待追蹤問題：
  - `Stroke_ Etiology, classification, and epidemiology.md` 仍需單一來源 ingest，補 etiologic classification / epidemiology。
  - `Posterior circulation cerebrovascular syndromes.md` 仍需單一來源 ingest，補 posterior circulation vascular anatomy、localization 與 clinical syndromes。
  - `Stroke in patients with atrial fibrillation.md` 仍需單一來源 ingest，補 AF-related stroke features、reperfusion contraindication and anticoagulation timing。
  - `Lacunar infarcts.md` 仍需單一來源 ingest，補 lacunar syndrome、parent artery occlusion mimic 與小血管病限制。

## [2026-05-12] ingest | Stroke: Etiology, classification, and epidemiology

- 本輪單一來源：
  - `C:\原始資料\Stroke_ Etiology, classification, and epidemiology.md`
  - 本輪只處理此 UpToDate topic review；未混入 `Posterior circulation cerebrovascular syndromes.md`、`Stroke in patients with atrial fibrillation.md`、`Lacunar infarcts.md`、stroke guideline 原文或其他 epidemiology source。
- 新增來源摘要：
  - `10_來源摘要/UpToDate_stroke_etiology_classification_epidemiology.md`
- 新增頁面：
  - `03_疾病與臨床主題/Stroke_Etiologic_Classification.md`
  - `03_疾病與臨床主題/Stroke_Epidemiology_全球與美國分布.md`
- 更新頁面：
  - `03_疾病與臨床主題/Stroke_Subtype_Clinical_Diagnosis.md`
  - `03_疾病與臨床主題/Stroke_Evaluation_病因確認與Directed_Diagnostic_Testing.md`
  - `03_疾病與臨床主題/中風復健總論.md`
  - `index.md`（Total pages 664 -> 667）
  - `log.md`
- 抽出概念：
  - Stroke etiologic classification：stroke 先分 brain ischemia vs brain hemorrhage；ischemic stroke 再依 thrombosis、embolism、systemic hypoperfusion、blood disorder / other causes 與 TOAST / SSS-TOAST / CCS / ISPS25-like framework 做 mechanism labeling。
  - Stroke epidemiology：stroke burden、subtype distribution、incidence、mortality and disability 會隨地區、收入層級、sex、race / ethnicity and time period 變動；population-level data 只改變 pretest probability，不能替代個別病人的 diagnostic workup。
- 本輪直接事實：
  - Source 為 UpToDate topic review；literature review current through 2026-04，topic last updated 2025-12-26；source_tier 6。
  - Stroke broadly divides into brain ischemia and brain hemorrhage。
  - Brain ischemia in this source includes thrombosis、embolism and systemic hypoperfusion。
  - Brain hemorrhage includes ICH and SAH。
  - Thrombotic stroke can be divided into large vessel disease and small vessel disease。
  - Large artery lesions may cause reduced distal blood flow、artery-to-artery embolism or both。
  - Small vessel stroke commonly involves penetrating arteries; lipohyalinosis and branch atheromatous disease are important mechanisms。
  - Embolic stroke categories include definite cardiac source、possible cardiac / aortic source、arterial source and truly unknown source after testing。
  - TOAST subtypes are large artery atherosclerosis、cardioembolism、small vessel occlusion、other determined etiology and undetermined etiology。
  - SSS-TOAST / CCS add evident、probable and possible diagnostic confidence levels。
  - Source states original TOAST and CCS agreement is moderate at best。
  - ISPS25 minimum diagnostic evaluation includes history / physical examination、brain and intracranial / extracranial vascular imaging、ECG and at least 24-hour rhythm monitoring if AF is not initially seen、selected echocardiography and laboratory testing。
  - In the United States, source gives approximate stroke subtype proportions as ischemia 87 percent、ICH 10 percent and SAH 3 percent。
  - Source states adult lifetime stroke risk from age 25 years and older is approximately 25 percent。
  - Source states annual United States new or recurrent stroke count is approximately 795,000, including approximately 610,000 first-ever and 185,000 recurrent strokes。
- 發現衝突：
  - 與「bedside subtype recognition 等同 final etiology」衝突。
  - 與「AF、PFO、carotid stenosis 或 lacunar syndrome 自動證明病因」衝突。
  - 與「cryptogenic / undetermined stroke 可以和 incomplete evaluation 混用」衝突。
  - 與「TOAST、CCS、ISPS25 label 可直接互換」衝突。
  - 與「United States stroke subtype proportions 可直接外推全球或個別病人」衝突。
  - Source 內部流行病學比例不一致：正文 epidemiology section 與 summary 對 global ischemia / ICH / SAH proportions 給出不同數字；本輪標記為 source-internal uncertainty，不寫成單一定論。
- 待追蹤問題：
  - `Posterior circulation cerebrovascular syndromes.md` 仍需單一來源 ingest，補 posterior circulation vascular anatomy、localization 與 clinical syndromes。
  - `Stroke in patients with atrial fibrillation.md` 仍需單一來源 ingest，補 AF-related stroke features、reperfusion contraindication and anticoagulation timing。
  - `Lacunar infarcts.md` 仍需單一來源 ingest，補 lacunar syndrome、parent artery occlusion mimic 與小血管病限制。
  - 若需要 Taiwan / East Asia stroke epidemiology，需另找 local or regional epidemiologic source；本篇不可替代。

## [2026-05-12] ingest | Posterior circulation cerebrovascular syndromes

- 本輪單一來源：
  - `C:\原始資料\Posterior circulation cerebrovascular syndromes.md`
  - 本輪只處理此 UpToDate topic review；未混入 `Stroke in patients with atrial fibrillation.md`、`Lacunar infarcts.md`、posterior circulation guideline 原文、HINTS primary studies 或其他 vertigo source。
- 新增來源摘要：
  - `10_來源摘要/UpToDate_posterior_circulation_cerebrovascular_syndromes.md`
- 新增頁面：
  - `03_疾病與臨床主題/Posterior_Circulation_Stroke_臨床定位與診斷陷阱.md`
  - `03_疾病與臨床主題/HINTS_急性前庭症候群中樞與周邊鑑別.md`
- 更新頁面：
  - `03_疾病與臨床主題/Stroke_Subtype_Clinical_Diagnosis.md`
  - `03_疾病與臨床主題/Stroke_Evaluation_病因確認與Directed_Diagnostic_Testing.md`
  - `03_疾病與臨床主題/Acute_Stroke_Initial_Assessment與Stabilization.md`
  - `index.md`（Total pages 667 -> 670）
  - `log.md`
- 抽出概念：
  - Posterior circulation stroke clinical localization and diagnostic pitfalls：vertebral / basilar / PCA territory ischemia 需整合 ocular motor、bulbar、vestibulocerebellar、sensory、visual、alertness / behavior / memory signs；early CT and DWI MRI 均可能漏診 small posterior circulation infarct。
  - HINTS in acute vestibular syndrome：HINTS 只適用 continuous acute vertigo/dizziness；normal head impulse、direction-changing nystagmus or skew deviation 支持 central lesion；peripheral-appearing HINTS 若合併 new hearing loss 仍需考慮 AICA / internal auditory artery infarction。
- 本輪直接事實：
  - Source 為 UpToDate topic review；literature review current through 2026-04，topic last updated 2024-10-24；source_tier 6。
  - Posterior circulation structures account for about 20 percent of ischemic brain events in the source。
  - Large posterior circulation arteries include innominate / subclavian arteries、extracranial vertebral arteries、intracranial vertebral arteries、basilar artery and PCAs。
  - Subclavian / innominate artery disease may cause arm ischemia and TIAs but seldom strokes。
  - Most proximal vertebral artery occlusive lesions are atherosclerotic；proximal ECVA disease more often causes intracranial posterior circulation ischemia by artery-to-artery embolism than by low flow。
  - ECVA dissection commonly presents with neck/occipital pain plus lateral medullary or cerebellar TIA/stroke pattern。
  - Lateral medullary infarction is the most common and important syndrome related to intracranial vertebral artery occlusion。
  - Basilar artery occlusive disease most often presents as pontine ischemia with motor、bulbar and oculomotor abnormalities。
  - Top of basilar syndrome involves rostral basilar territory and affects alertness、behavior、memory、oculomotor and pupillary functions。
  - PCA territory infarction commonly causes hemianopia；lateral thalamic infarction is a major reason for somatosensory symptoms and signs。
  - CT has lower sensitivity than DWI MRI for acute ischemic stroke, particularly posterior fossa stroke；DWI MRI can still be false negative in small acute posterior circulation infarcts。
  - HINTS is most useful for continuous acute vertigo/dizziness and is not useful for momentary position-related vertigo or TIA when the patient is not dizzy at exam。
  - Normal head impulse bilaterally、direction-changing nystagmus or skew deviation suggests brainstem/cerebellar lesion；abnormal unilateral head impulse plus unidirectional horizontal-torsional nystagmus plus absent skew suggests peripheral lesion。
  - Inner ear infarction from internal auditory artery / AICA branch occlusion can mimic peripheral vestibular disease; new ipsilateral hearing loss may be the clue。
- 發現衝突：
  - 與「early CT / MRI negative 排除 posterior circulation stroke」衝突。
  - 與「dizziness alone equals vertebrobasilar TIA」衝突。
  - 與「所有 acute vertigo 有 peripheral-appearing HINTS 都可視為 benign」衝突。
  - 與「NIHSS 低分代表 posterior circulation stroke 低風險」衝突。
  - 與「subclavian steal physiology 常造成 stroke」衝突。
  - 與「proximal ECVA stenosis 主要是 low-flow mechanism」衝突。
- 待追蹤問題：
  - `Stroke in patients with atrial fibrillation.md` 仍需單一來源 ingest，補 AF-related stroke features、reperfusion contraindication and anticoagulation timing。
  - `Lacunar infarcts.md` 仍需單一來源 ingest，補 lacunar syndrome、parent artery occlusion mimic 與 small vessel disease 限制。
  - 若要建立 vertigo differential diagnosis 或 HINTS implementation skill，需要另處理 dedicated vertigo source；本篇不可替代完整 dizziness differential。
## [2026-05-12] ingest | Stroke in patients with atrial fibrillation

- 本輪單一來源：
  - `C:\原始資料\Stroke in patients with atrial fibrillation.md`
  - 本輪只處理此 UpToDate topic review；未混入 `Atrial fibrillation in adults: Use of oral anticoagulants`、`Early antithrombotic treatment of acute ischemic stroke and transient ischemic attack`、LAA occlusion 專題、AF guideline 原文或其他 stroke source。
- 新增來源摘要：
  - `10_來源摘要/UpToDate_stroke_in_patients_with_atrial_fibrillation.md`
- 新增頁面：
  - `03_疾病與臨床主題/AF_Related_Stroke_病因歸屬與診斷評估.md`
  - `03_疾病與臨床主題/AF_Stroke_Anticoagulation_時機與長期策略.md`
  - `03_疾病與臨床主題/AF_Stroke_Anticoagulation_Failure.md`
- 更新頁面：
  - `03_疾病與臨床主題/Stroke_Evaluation_病因確認與Directed_Diagnostic_Testing.md`
  - `03_疾病與臨床主題/Acute_Stroke_Initial_Assessment與Stabilization.md`
  - `03_疾病與臨床主題/中風急性期處置與時間窗.md`
  - `03_疾病與臨床主題/Ischemic_Stroke_Long_term_Antithrombotic_Therapy.md`
  - `03_疾病與臨床主題/中風次發預防.md`
  - `index.md`（Total pages 670 -> 674）
  - `08_工具與Workflow/source_manifest.json`
  - `log.md`
- 抽出概念：
  - AF-related stroke attribution：AF patient 的 ischemic stroke 多由 LAA / cardiac embolism 解釋，但 AF common in older adults；仍需完整 brain / neurovascular imaging、cardiac evaluation and selected TEE，以免忽略 large artery、small vessel、aortic 或其他 competing mechanisms。
  - AF stroke anticoagulation timing：acute infarct 後 anticoagulation 通常暫停以降低 hemorrhagic transformation risk，再依 infarct size / bleeding risk 於 first days to two weeks 重啟；long-term 多數 DOAC preferred，但 mechanical valve / clinically significant rheumatic mitral stenosis 等仍屬 VKA pathway。
  - AF stroke anticoagulation failure：stroke despite DOAC / VKA 先查 missed dose、underdosing、renal function、interactions、INR / time in range、LAA thrombus and competing mechanisms；不應 reflex 加 antiplatelet。
- 本輪直接事實：
  - Source 為 UpToDate topic review；literature review current through 2026-04，topic last updated 2026-01-05；source_tier 6。
  - AF patient 的 ischemic stroke 常見原因是 cardiac embolus，most commonly thrombus from left atrial appendage。
  - AF cardioembolic stroke generally has increased severity compared with embolic stroke from carotid disease。
  - AF cardioembolic stroke may affect any or multiple vascular territories and often appears as wedge-shaped cortical / subcortical infarcts。
  - Source cites a 2014 systematic review / meta-analysis：silent cerebral infarction prevalence among AF patients was 40 percent by MRI and 22 percent by CT；但多數 pooled studies 為 cross-sectional，causal link uncertain。
  - Presence of AF in a stroke patient does not always mean causal relationship。
  - All stroke patients, even in the setting of AF, may benefit from complete evaluation for other causes。
  - TTE is recommended for most ischemic stroke patients；TEE can identify LAA thrombus and other cardiac / aortic embolic sources, but TEE negative does not exclude AF as the cause。
  - Current VKA use with anticoagulant effect such as INR >1.7 or PT >15 seconds and recent DOAC use under specified conditions are IV thrombolysis-relevant contraindication boundaries。
  - Anticoagulation is usually temporarily withheld immediately after ischemic stroke due to hemorrhagic transformation risk。
  - Long-term oral anticoagulation is started or resumed once hemorrhagic transformation risk has diminished, usually within first days to two weeks, guided mainly by infarct size。
  - For medically stable small / moderate infarct without intracranial bleeding, source states warfarin can be started soon and prefers waiting 48 hours for DOAC because DOAC effect is faster。
  - Withholding anticoagulation for one week has generally been recommended for large infarct、symptomatic hemorrhagic transformation or poorly controlled hypertension。
  - Early heparin after acute cardioembolic stroke should generally be avoided。
  - For most ischemic stroke / TIA patients with AF, source recommends DOAC rather than VKA；VKA remains indicated for mechanical valves and clinically significant rheumatic mitral stenosis。
  - LAA occlusion should be considered when long-term anticoagulation is not an option but short-term antithrombotic therapy can be tolerated。
  - Source-cited analysis of breakthrough events：DOAC group attribution was cardioembolism 49 percent、poor adherence or insufficient dose 23 percent、competing mechanism 28 percent；VKA group was cardioembolism 37 percent、poor adherence or insufficient dose 43 percent、competing mechanism 20 percent。
  - For warfarin breakthrough with therapeutic INR 2-3, source favors switching to DOAC rather than routine antiplatelet addition when DOAC is not contraindicated。
- 發現衝突：
  - 與「AF 自動證明 cardioembolic stroke」衝突。
  - 與「AF-related acute ischemic stroke 應 immediate heparin」衝突。
  - 與「DOAC failure 就自動換另一個 DOAC / warfarin」衝突。
  - 與「warfarin failure 直接加 antiplatelet」衝突。
  - 與「fall risk alone 足以取消 anticoagulation」衝突。
  - 與「TEE 沒看到 LAA thrombus 就排除 AF embolism」衝突。
- 待追蹤問題：
  - `Lacunar infarcts.md` 仍需單一來源 ingest，補 lacunar syndrome、parent artery occlusion mimic 與 small vessel disease 限制。
  - 若要處理 AF oral anticoagulant dosing、renal adjustment、drug interaction 或 LAA occlusion indication，需另行單一來源 ingest，不可由本篇直接取代。
  - 若要處理 prior ICH / cerebral amyloid angiopathy + AF 的 anticoagulation dilemma，需另找 dedicated ICH / CAA source。

## [2026-05-12] ingest | Lacunar infarcts

- 本輪單一來源：
  - `C:\原始資料\Lacunar infarcts.md`
  - 本輪只處理此 UpToDate topic review；未混入 lacunar primary studies、CADASIL / CAA 專題、acute reperfusion guideline、secondary prevention guideline 或其他 stroke source。
- 新增來源摘要：
  - `10_來源摘要/UpToDate_lacunar_infarcts.md`
- 新增頁面：
  - `03_疾病與臨床主題/Lacunar_Infarcts_診斷與病因邊界.md`
  - `03_疾病與臨床主題/Lacunar_Stroke_Syndromes_臨床表現與影像確認.md`
- 更新頁面：
  - `03_疾病與臨床主題/Stroke_Subtype_Clinical_Diagnosis.md`
  - `03_疾病與臨床主題/Stroke_Evaluation_病因確認與Directed_Diagnostic_Testing.md`
  - `03_疾病與臨床主題/Stroke_Etiologic_Classification.md`
  - `03_疾病與臨床主題/中風急性期處置與時間窗.md`
  - `03_疾病與臨床主題/中風次發預防.md`
  - `index.md`（Total pages 674 -> 677）
  - `08_工具與Workflow/source_manifest.json`
  - `log.md`
- 抽出概念：
  - Lacunar infarcts diagnosis and etiologic boundary：lacunar infarct 是 small noncortical penetrating-artery infarct，但 syndrome 或 small deep lesion 不能自動證明 small vessel occlusion；需排除 parent artery disease、embolic pattern and other etiologies。
  - Lacunar stroke syndromes and imaging confirmation：five classic lacunar syndromes 提示 subcortical stroke，但 CT sensitivity 低，DWI MRI 可確認 acute culprit lesion、區分 acute/chronic lesions and reveal embolic patterns。
  - Lacunar infarct prevention caveat：lacunar stroke secondary prevention 以 BP / statin / lifestyle and single antiplatelet 為主；long-term aspirin plus clopidogrel 在 SPS3 中增加 hemorrhage/death 且未降低 recurrence。
- 本輪直接事實：
  - Source 為 UpToDate topic review；literature review current through 2026-04，topic last updated 2025-04-15；source_tier 6。
  - Lacunar infarcts are small noncortical infarcts caused by occlusion of a single penetrating branch of a large cerebral artery。
  - Traditional size definition is 2-15 mm, while acute imaging studies may use 20-25 mm because lesions shrink over time。
  - Not all small deep infarcts are lacunar, and diagnosis requires exclusion of other ischemic stroke etiologies。
  - Common locations are basal ganglia、thalamus、internal capsule / corona radiata and pons。
  - Mechanisms described include hypertensive microangiopathy、branch atheromatous disease、embolism and endothelial dysfunction / BBB disruption。
  - Hypertensive microangiopathy and branch atheromatous disease are pathologically proven; endothelial dysfunction remains unconfirmed。
  - Lacunar infarcts account for approximately 15-26 percent of ischemic strokes。
  - Five classic lacunar syndromes are pure motor hemiparesis、pure sensory stroke、ataxic hemiparesis、sensorimotor stroke and dysarthria-clumsy hand syndrome。
  - Lacunar syndromes generally lack aphasia、hemianopia、agnosia、neglect and apraxia。
  - Hyperacute lacunar syndrome recognition may not reflect final diagnosis；one cited study within six hours reported 30 percent positive predictive value by CT。
  - CT sensitivity for small acute lacunar infarcts is low, approximately 30-44 percent in prospective studies。
  - DWI MRI can differentiate acute from chronic lacunes and identify multiple acute lesions suggesting embolic mechanism。
  - One report found nonlacunar infarcts in 21 percent of clinically identified lacunar syndromes；another DWI study found nonlacunar / embolic patterns in 41 percent。
  - Confirmed lacunar infarction is not a mechanical thrombectomy target, but acute vascular imaging is warranted because small deep infarcts are not always lacunar。
  - Standard evaluation includes history and physical examination、brain imaging、neurovascular imaging、cardiac monitoring and echocardiography。
  - Intravenous thrombolysis selection is the same as other ischemic stroke subtypes；a WAKE-UP post hoc analysis found similar functional benefit for lacunar and nonlacunar stroke subtypes。
  - Beyond the acute phase and without anticoagulation indication, long-term single-agent antiplatelet therapy is used；long-term aspirin plus clopidogrel is not recommended in lacunar stroke。
- 發現衝突：
  - 與「pure motor stroke = lacunar infarct」衝突。
  - 與「small deep infarct = small vessel disease」衝突。
  - 與「CT negative 排除 acute lacunar infarct」衝突。
  - 與「懷疑 lacunar stroke 就不需要 vascular / cardiac evaluation」衝突。
  - 與「confirmed lacunar stroke 應長期 aspirin plus clopidogrel」衝突。
- 待追蹤問題：
  - Silent lacunar infarct / covert brain infarct 的 antiplatelet risk-benefit 需另以 guideline-level source 處理。
  - CADASIL、CAA and monogenic cerebral small vessel disease 需各自單一來源，不可由本篇完整取代。
  - Branch atheromatous disease 若要做成 treatment / prognosis 專頁，需要 dedicated source。

## [2026-05-12] ingest | Intracranial large artery atherosclerosis: Treatment and prognosis

- 本輪單一來源：
  - `C:\原始資料\Intracranial large artery atherosclerosis_ Treatment and prognosis.md`
  - 本輪只處理此 UpToDate topic review；未混入 ICAS epidemiology / diagnosis topic、AHA/ASA guideline 原文、SAMMPRIS 原文、Cerebral and cervical artery dissection、Pathophysiology of ischemic stroke 或其他 stroke source。
- 新增來源摘要：
  - `10_來源摘要/UpToDate_intracranial_large_artery_atherosclerosis_treatment_prognosis.md`
- 新增頁面：
  - `03_疾病與臨床主題/Symptomatic_ICAS_次發預防與DAPT邊界.md`
  - `03_疾病與臨床主題/ICAS_Stenting與介入治療限制.md`
  - `03_疾病與臨床主題/ICAS_復發風險與血流動力邊界.md`
- 更新頁面：
  - `03_疾病與臨床主題/中風次發預防.md`
  - `03_疾病與臨床主題/Ischemic_Stroke_Long_term_Antithrombotic_Therapy.md`
  - `index.md`（Total pages 677 -> 681）
  - `08_工具與Workflow/source_manifest.json`
  - `log.md`
- 抽出概念：
  - Symptomatic ICAS secondary prevention and DAPT boundary：recent stroke / TIA attributed to 70-99% ICAS 可用 aspirin plus clopidogrel DAPT up to 90 days；50-69% ICAS 需依 TIA / stroke risk 決定 aspirin alone or 21-day DAPT；long-term 回到 single antiplatelet。
  - ICAS stenting and intervention boundary：routine intracranial stenting 不建議；SAMMPRIS、VISSIT、CASSISS and meta-analysis 顯示 harm 或 no benefit，submaximal angioplasty 仍屬未定研究 / last-resort 討論。
  - ICAS recurrent risk and hemodynamic boundary：severe stenosis、recent symptoms、borderzone infarct / impaired collateral flow、hemodynamic symptoms、female sex and no statin exposure 是復發風險訊號，但 hemodynamic marker 不足以單獨決定 intervention。
- 本輪直接事實：
  - Source 為 UpToDate topic review；literature review current through 2026-04，topic last updated 2026-01-14；source_tier 6。
  - Acute stroke / TIA due to ICAS 的 initial treatment 與其他 acute ischemic stroke / TIA 類似，仍需快速判斷 IV thrombolysis / mechanical thrombectomy eligibility。
  - All patients with recent ischemic stroke / TIA attributed to intracranial large artery stenosis should receive intensive medical therapy with antiplatelet therapy and strict vascular risk factor control。
  - Recent stroke / TIA within 30 days attributed to 70-99% atherosclerotic intracranial stenosis：source suggests aspirin plus clopidogrel DAPT up to 90 days, followed by long-term aspirin monotherapy。
  - 50-69% stenosis with low-risk TIA or moderate-to-major stroke：source starts aspirin alone；high-risk TIA or minor stroke：source uses 21-day aspirin plus clopidogrel DAPT。
  - Clopidogrel monotherapy or aspirin-extended-release dipyridamole are reasonable long-term alternatives to aspirin but not specifically studied in ICAS。
  - WASID found warfarin harmful compared with aspirin for TIA / stroke due to ICAS; routine oral anticoagulation has no role for ICAS alone。
  - Symptomatic 50-99% ICAS with hypertension：source suggests SBP target <140 mmHg rather than lower target and advises caution with SBP <130 / <120 in selected low-flow or unstable patients。
  - Atherosclerotic ischemic stroke / TIA including symptomatic ICAS：source uses high-intensity statin and LDL-C target <70 mg/dL。
  - Physical activity was independently associated with lower recurrent stroke、MI and vascular death in medically treated SAMMPRIS patients。
  - Intracranial stenting is not recommended for first stroke / TIA attributable to severe intracranial stenosis。
  - SAMMPRIS 30-day stroke/death was higher with angioplasty/stenting than medical therapy alone（14.7% vs 5.8%）。
  - VISSIT and CASSISS did not support routine stenting; a source-cited 2023 meta-analysis found higher death/stroke with endovascular therapy plus medical treatment at 30 days and one year。
  - Submaximal balloon angioplasty in BASIS showed promising one-year outcomes but source states more research is needed before wide use。
  - ICAS recurrent risk is higher with severe stenosis >=70%、recent symptoms、borderzone infarct / impaired collateral flow、clinically hemodynamic stenosis and selected high-risk features。
  - Hemodynamic measures inconsistently predict ischemic risk across VERITAS and MyRIAD; source says further research is needed。
- 發現衝突：
  - 與「severe intracranial stenosis should be stented」衝突。
  - 與「DAPT for ICAS should be indefinite」衝突。
  - 與「warfarin is stronger than aspirin for ICAS」衝突。
  - 與「all post-stroke patients should immediately target SBP <130/80 regardless of perfusion」衝突。
  - 與「hemodynamic symptoms alone prove intervention indication」衝突。
- 待追蹤問題：
  - `Intracranial large artery atherosclerosis: Epidemiology, clinical manifestations, and diagnosis` 若 raw source 存在，需另行單一來源 ingest；本篇 treatment/prognosis 不能取代 diagnosis framework。
  - `Cerebral and cervical artery dissection_ Clinical features and diagnosis.md` 仍在 raw backlog，需單一來源處理 young stroke / neck pain / Horner syndrome differentiation。
  - `Pathophysiology of ischemic stroke.md` 仍需單一來源處理 ischemic core / penumbra / autoregulation / excitotoxicity 概念。

## [2026-05-13] ingest | Cerebral and cervical artery dissection: Clinical features and diagnosis

- 本輪單一來源：
  - `C:\原始資料\Cerebral and cervical artery dissection_ Clinical features and diagnosis.md`
  - 本輪只處理此 UpToDate topic review；未混入 dissection treatment/prognosis topic、stroke guideline、young stroke source、Horner syndrome source、FMD source、SAH dedicated source 或其他 stroke source。
- 新增來源摘要：
  - `10_來源摘要/UpToDate_cerebral_cervical_artery_dissection_clinical_features_diagnosis.md`
- 新增頁面：
  - `03_疾病與臨床主題/Cervicocephalic_Artery_Dissection_臨床辨識.md`
  - `03_疾病與臨床主題/Cervicocephalic_Artery_Dissection_影像確認與Pitfalls.md`
- 更新頁面：
  - `03_疾病與臨床主題/Stroke_Subtype_Clinical_Diagnosis.md`
  - `03_疾病與臨床主題/Stroke_Evaluation_病因確認與Directed_Diagnostic_Testing.md`
  - `03_疾病與臨床主題/Stroke_Etiologic_Classification.md`
  - `03_疾病與臨床主題/Posterior_Circulation_Stroke_臨床定位與診斷陷阱.md`
  - `index.md`（Total pages 681 -> 684）
  - `08_工具與Workflow/source_manifest.json`
  - `log.md`
- 抽出概念：
  - Cervicocephalic artery dissection clinical recognition：acute/subacute head or neck pain、Horner syndrome、cranial/cervical neuropathy、pulsatile tinnitus、TIA/stroke、SAH pattern、minor trauma / trigger and vascular predisposition should trigger suspicion and urgent head/neck vascular imaging.
  - Cervicocephalic artery dissection imaging confirmation：diagnosis is confirmed by neuroimaging signs such as long tapered stenosis、tapered occlusion、pseudoaneurysm、intimal flap、double lumen or intramural hematoma；ultrasound negative does not rule out dissection when clinical history remains suggestive.
- 本輪直接事實：
  - Source 為 UpToDate topic review；literature review current through 2026-04；topic last updated 2025-05-27；source_tier 6。
  - Dissection occurs when arterial wall integrity is compromised and blood collects between wall layers as an intramural hematoma。
  - Arterial dissection is a common cause of stroke in the young but may occur at any age。
  - Minor trauma or mechanical events are triggers in up to 40 percent of cervical artery dissection cases。
  - Extracranial carotid dissections typically occur 2 cm or more beyond the carotid bifurcation near skull base；vertebral artery dissection most often occurs in V3 or less often V2。
  - Multiple simultaneous cervicocephalic dissections are found in 13 to 22 percent；three or more occur in approximately 2 percent。
  - Subintimal dissection causes luminal stenosis / occlusion and ischemia via thromboembolism, hypoperfusion or both；source states thromboembolism is considered the major cause of ischemic symptoms。
  - Subadventitial dissection / pseudoaneurysm may cause local symptoms through adjacent nerve compression: pain、partial Horner syndrome、lower cranial neuropathy or cervical nerve root involvement。
  - Intracranial artery dissection can cause SAH in a minority。
  - Head and/or neck pain is the most frequent initial symptom, found in 57 to 90 percent。
  - Horner syndrome occurs in approximately 25 percent and is usually partial in internal carotid artery dissection。
  - Carotid dissection may cause cranial neuropathies in up to 12 percent；CN XII is most common。
  - Pulsatile tinnitus was present in 8 percent in CADISP。
  - In a population-based report of 48 internal carotid / vertebral dissection patients, cerebral ischemia was noted in 67 percent, TIA in 23 percent and cerebral infarction in 56 percent。
  - Vertebral artery dissection may lead to lateral medullary infarction、other posterior circulation stroke syndromes or cervical spinal cord ischemia。
  - Patients age >=60 years with cervical artery dissection may be less likely to present with neck pain、headache、preceding trauma or mechanical trigger。
  - Diagnosis is confirmed by neuroimaging, particularly long tapered stenosis、tapered occlusion、pseudoaneurysm、intimal flap、double lumen or intramural hematoma。
  - Source obtains urgent brain/neck MRI + head/neck MRA or head CT + head/neck CTA to confirm diagnosis and guide serial treatment decisions。
  - There is no single gold standard；complementary and repeat imaging may be required。
  - DSA is reserved for younger patients with high suspicion despite negative noninvasive imaging；DSA is not needed if CTA / MRA clearly diagnoses dissection。
  - Carotid duplex detects abnormalities in only 68 to 95 percent and is unreliable for isolated Horner syndrome；MRA or CTA should be pursued in ultrasound-negative cases when history suggests dissection。
- 發現衝突：
  - 與「young stroke without major trauma is unlikely dissection」衝突。
  - 與「headache / neck pain is required for dissection」衝突。
  - 與「older age rules out cervical artery dissection」衝突。
  - 與「negative carotid duplex rules out dissection」衝突。
  - 與「dizziness/vertigo alone diagnoses vertebral artery dissection」衝突。
  - 與「clinical suspicion alone is enough to label dissection etiology」衝突。
- 待追蹤問題：
  - `Cerebral and cervical artery dissection: Treatment and prognosis` 若 raw source 存在，需另行單一來源 ingest；本篇不可替代 antithrombotic choice、follow-up imaging or recurrence prognosis。
  - `Pathophysiology of ischemic stroke.md` 仍需單一來源處理 ischemic core / penumbra / autoregulation / excitotoxicity。
  - `Intracranial large artery atherosclerosis: Epidemiology, clinical manifestations, and diagnosis` raw source 目前未找到；若日後加入，需另行單一來源 ingest。

## [2026-05-13] ingest | Pathophysiology of ischemic stroke

- 本輪單一來源：
  - `C:\原始資料\Pathophysiology of ischemic stroke.md`
  - 本輪只處理此 UpToDate topic review；未混入 acute stroke treatment guideline、secondary prevention source、malignant infarction topic、stroke genetics source 或原始研究。
- 新增來源摘要：
  - `10_來源摘要/UpToDate_pathophysiology_of_ischemic_stroke.md`
- 新增頁面：
  - `03_疾病與臨床主題/Ischemic_Stroke_Cerebral_Autoregulation與灌流閾值.md`
  - `03_疾病與臨床主題/Ischemic_Core與Penumbra.md`
  - `03_疾病與臨床主題/Ischemic_Stroke_Cell_Injury_Cascade.md`
  - `03_疾病與臨床主題/Ischemic_Stroke_Cerebral_Edema與Hemorrhagic_Conversion.md`
- 更新頁面：
  - `03_疾病與臨床主題/中風急性期處置與時間窗.md`
  - `03_疾病與臨床主題/Acute_Stroke_Initial_Assessment與Stabilization.md`
  - `03_疾病與臨床主題/Stroke_Etiologic_Classification.md`
  - `index.md`（Total pages 684 -> 689）
  - `08_工具與Workflow/source_manifest.json`
  - `log.md`
- 抽出概念：
  - Cerebral autoregulation and perfusion thresholds：ischemic stroke 可 impaired autoregulation；CBF 下降會依序造成 protein synthesis inhibition、anaerobic glycolysis / acidosis、electrical failure and membrane ion homeostasis failure。
  - Ischemic core and penumbra：core 是 irreversible / destined infarct tissue；penumbra 是 residual perfusion 支持、及時 reperfusion 可能 salvage 的 tissue。
  - Ischemic cell injury cascade：ATP depletion、ion gradient failure、glutamate excitotoxicity、calcium influx、nitric oxide / ROS injury、mitochondrial failure、inflammation and necrosis / apoptosis。
  - Cerebral edema and hemorrhagic conversion：cytotoxic、ionic and vasogenic edema 來自 ATP-dependent transport failure、BBB disruption and neurovascular structural failure；嚴重 vascular integrity failure 可導致 hemorrhagic conversion。
- 本輪直接事實：
  - Source 為 UpToDate topic review；literature review current through 2026-04；topic last updated 2025-06-11；source_tier 6。
  - Ischemic stroke is due to reduced or blocked blood flow from decreased systemic perfusion, severe stenosis or vessel occlusion。
  - Main ischemic mechanisms described include thrombosis, embolization and lacunar infarction from small vessel disease。
  - Ischemic strokes represent approximately 80 percent of all strokes in this source。
  - Decreased systemic perfusion may cause generalized brain ischemia, especially borderzone / watershed territories, and can be asymmetric with preexisting vascular lesions。
  - Cerebral autoregulation normally maintains relatively constant CBF across MAP about 60-150 mmHg, with individual variation。
  - Ischemic stroke can impair cerebral autoregulation。
  - Chronic hypertension shifts autoregulation toward higher arterial pressures；acute reduction to normal levels may further decrease CBF during stroke。
  - Source CBF thresholds include <50 mL/100 g/min protein synthesis inhibition, 35 cessation of protein synthesis, 25 anaerobic glycolysis / acidosis, 16-18 neuronal electrical failure, and 10-12 membrane ion homeostasis failure / infarct threshold。
  - Brain receives approximately 20 percent of cardiac output while being about 2 percent of body weight and has little or no energy stores。
  - Core infarct tissue becomes irreversibly damaged and dies by necrosis if ischemia lasts long enough。
  - Penumbra is potentially salvageable tissue supported by partial oxygen / glucose supply from collateral vessels and timely restored flow。
  - ATP levels may fall to about 25 percent of normal in focal ischemic core models and 50-70 percent in penumbra。
  - Ischemic injury cascade includes ATP depletion、sodium/potassium/calcium changes、lactate / acidosis、oxygen free radicals、intracellular water accumulation and proteolytic activation。
  - NMDA receptor activation is a major excitotoxic mechanism; AMPA and metabotropic glutamate receptors may also contribute。
  - Sodium influx contributes to edema and reversed astrocyte glutamate uptake, amplifying glutamate accumulation。
  - Cell death after ischemia can occur by necrosis or apoptosis；core low ATP favors necrosis, while penumbra has enough ATP for apoptosis until ischemia duration depletes energy。
  - Matrix metalloproteases can degrade basal lamina collagen / laminin, contributing to BBB breakdown and cerebral edema。
  - Edema types described are cytotoxic、ionic / interstitial and vasogenic。
  - Roughly 10 percent of ischemic strokes are malignant or massive due to space-occupying cerebral edema severe enough to produce elevated ICP and herniation。
  - Genetic contribution exists, but monogenic disorders together account for only a small percentage of ischemic strokes。
- 發現衝突：
  - 與「acute ischemic stroke 的高 BP 都應快速 normalizing」衝突。
  - 與「penumbra 一定可被救回」衝突。
  - 與「core / penumbra 可由症狀直接判定」衝突。
  - 與「excitotoxicity 是 ischemic injury 的唯一機制」衝突。
  - 與「hemorrhagic conversion 只是藥物副作用」衝突。
  - 與「stroke genetics 可以取代 standard etiologic workup」衝突。
- 待追蹤問題：
  - Late-window imaging selection、CT perfusion / MR perfusion mismatch thresholds 需 dedicated acute reperfusion / imaging source。
  - Malignant MCA infarction、decompressive hemicraniectomy indication and edema management 需 dedicated source。
  - Stroke genetics / CADASIL / CARASIL / Fabry / sickle cell disease 需各自單一來源，不可由本篇建立完整診斷或治療頁。

## [2026-05-13] ingest | Overview of ischemic stroke prognosis in adults

- 本輪單一來源：
  - `C:\原始資料\Overview of ischemic stroke prognosis in adults.md`
  - 本輪只處理此 UpToDate topic review；未混入 acute reperfusion source、stroke complication source、aphasia dedicated source、lacunar / ICAS / AF-specific source 或 rehab guideline。
- 新增來源摘要：
  - `10_來源摘要/UpToDate_overview_ischemic_stroke_prognosis_adults.md`
- 新增頁面：
  - `03_疾病與臨床主題/Ischemic_Stroke_預後判讀與恢復時間軸.md`
- 更新頁面：
  - `03_疾病與臨床主題/中風復健總論.md`
  - `index.md`（Total pages 689 -> 691）
  - `08_工具與Workflow/source_manifest.json`
  - `log.md`
- 抽出概念：
  - Adult ischemic stroke prognosis framing：acute prognosis 不應只看初始 NIHSS；需整合 stroke severity、age、CT/MRI infarct burden/location、mechanism、comorbidities、complications、treatment response、recovery pace and domain-specific function。
- 本輪直接事實：
  - Source 為 UpToDate topic review；literature review current through 2026-04；topic last updated 2025-10-20；source_tier 6。
  - Source states estimated worldwide 30-day case fatality after first ischemic stroke ranges from 13.5 to 23 percent；summary section gives 16 to 23 percent。
  - In one 10-year follow-up study of minor ischemic stroke, cumulative mortality was 32 percent。
  - In a cited older community sample, six-month deficits included hemiparesis 50 percent、cognitive deficits 46 percent、hemianopia 20 percent、aphasia 19 percent and sensory deficits 15 percent。
  - Six-month disability measures included depression symptoms 35 percent、unable to walk unassisted 31 percent、social disability 30 percent、institutionalization 26 percent and bladder incontinence 22 percent。
  - Acute-phase strongest predictors are stroke severity and age。
  - NIHSS predicts outcome, but does not capture hand function、fine motor coordination、cognitive dysfunction or balance。
  - Neuroimaging size and location are important adjuncts because early neurologic examination alone may be falsely grim or falsely favorable。
  - Infarct volume、large artery occlusion、poor collateral flow、diffusion-perfusion mismatch、cerebral edema、cardioembolic / large artery mechanism、comorbidities and complications can worsen prognosis。
  - Most recovery occurs in the first three to six months, but some patients improve up to 18 months。
  - Early active finger extension / shoulder abduction are favorable for arm-hand recovery；early sitting balance and paretic leg contraction are favorable for ambulation recovery。
  - Reperfusion therapy, stroke unit care, rehabilitation and secondary prevention can improve ischemic stroke outcomes when appropriate。
- 發現衝突：
  - 與「NIHSS 低就代表功能預後一定好」衝突。
  - 與「第一次神經學檢查即可定論預後」衝突。
  - 與「mRS / Barthel 足以代表所有 rehab outcome」衝突。
  - 與「最大恢復在 3-6 個月內，所以慢性期 rehabilitation 沒意義」衝突。
  - 與「prognosis poor 就不需 reperfusion / stroke unit / rehabilitation / secondary prevention」衝突。
- 待追蹤問題：
  - Poststroke arm-hand recovery predictors 可由 dedicated motor recovery / upper limb rehab source 拆成單一概念頁。
  - Poststroke ambulation prognosis、dysphagia recovery trajectory、stroke prognostic scales / models limitations 需各自單一來源或 dedicated source。
  - Posterior circulation / infratentorial stroke prognosis 需另找專題來源，不可由 supratentorial infarct volume data 直接外推。

## [2026-05-13] ingest | Sleep-related breathing disorders and stroke

- 本輪單一來源：
  - `C:\原始資料\Sleep-related breathing disorders and stroke.md`
  - 本輪只處理此 UpToDate topic review；未混入 OSA cardiovascular disease topic、AHA/ASA guideline 原文、CSA treatment topic、sleep medicine guideline、Sleep SMART outcome report 或其他 stroke source。
- 新增來源摘要：
  - `10_來源摘要/UpToDate_sleep_related_breathing_disorders_and_stroke.md`
- 新增頁面：
  - `03_疾病與臨床主題/OSA_as_Stroke_Risk_Factor_機制與證據邊界.md`
  - `03_疾病與臨床主題/Poststroke_Sleep_Related_Breathing_Disorders_篩檢與診斷.md`
  - `03_疾病與臨床主題/Poststroke_Sleep_Apnea_PAP治療與預後邊界.md`
- 更新頁面：
  - `03_疾病與臨床主題/中風次發預防.md`
  - `03_疾病與臨床主題/中風併發症總覽.md`
  - `index.md`（Total pages 691 -> 695）
  - `08_工具與Workflow/source_manifest.json`
  - `log.md`
- 抽出概念：
  - OSA as Stroke Risk Factor：OSA 可透過 intermittent hypoxia、sympathetic activation、endothelial dysfunction、hypertension、AF and hemodynamic reserve 影響 ischemic stroke risk，但 CPAP 對 recurrent vascular events 的 trial evidence 仍 mixed。
  - Poststroke Sleep-Related Breathing Disorders screening and diagnosis：poststroke OSA / CSA / Cheyne-Stokes breathing 不能靠 snoring、daytime sleepiness 或 questionnaire 排除；需用 oximetry triage、polysomnography 或 HSAT。
  - Poststroke Sleep Apnea PAP treatment boundary：PAP and behavioral modification 是診斷後主軸，但需依 OSA / CSA predominance、acute stroke status、adherence、tolerance、BP / perfusion concern and recovery trajectory 重評。
- 本輪直接事實：
  - Source 為 UpToDate topic review；literature review current through 2026-04；topic last updated 2026-01-29；source_tier 6。
  - Sleep-related breathing disorders include OSA、CSA and Cheyne-Stokes breathing，且在 stroke / TIA patients 常見。
  - OSA has been associated with increased ischemic stroke risk independent of vascular risk factors；CSA-related stroke risk is not well studied。
  - Source-cited acute stroke / TIA meta-analysis pooled prevalence: AHI >=5 67%、AHI >=15 50%、AHI >=30 32%。
  - In chronic phase after stroke / TIA，severe sleep apnea pooled prevalence was 25% in seven studies。
  - OSA is more common than CSA after stroke；CSA or Cheyne-Stokes breathing was predominant in 7% in one analysis。
  - Sleep-related breathing disorders may be detectable within 24 hours after stroke。
  - Typical clinical features such as daytime sleepiness and snoring may be less reliable in stroke patients。
  - Clinical features linked to higher likelihood include increased BMI、male sex、systolic hypertension、early neurologic deterioration、nocturnal desaturation、increased stroke severity、hemorrhagic stroke、prior stroke and AF。
  - Berlin questionnaire had only moderate diagnostic utility poststroke；modified STOP-Bang without neck circumference had high sensitivity but low specificity。
  - Diagnosis requires formal sleep testing with polysomnography or HSAT type III / IV。
  - Source recommends at least reviewing overnight oximetry during the first five days poststroke when feasible。
  - Frequent nocturnal oxygen desaturations, dysphagia or dysphonia increase suspicion for moderate to severe sleep apnea。
  - PAP therapy and behavioral modifications are mainstays of treatment for diagnosed sleep-related breathing disorders。
  - Treatment decisions in acute stroke must be tailored to clinical status and perceived PAP adherence ability。
  - Sleep-disordered breathing can improve as stroke improves；source repeats testing at three-month intervals during the first year when possible。
  - CSA with Cheyne-Stokes breathing is more likely self-limited than OSA in the poststroke setting。
  - Auto-titrating CPAP may be feasible in selected non-severe stroke / TIA but may be poorly tolerated when central apneas are prevalent。
  - Stroke-specific PAP outcome evidence is limited and mixed；a 2023 meta-analysis of seven randomized trials found nonsignificant trend toward fewer new nonfatal vascular events with CPAP。
  - Poor PAP adherence after stroke may relate to PAP intolerance、motivation、cognitive deficits、age and neglect。
- 發現衝突：
  - 與「沒有 snoring / daytime sleepiness 就沒有 poststroke sleep apnea」衝突。
  - 與「Berlin / STOP-Bang 足以診斷或排除 poststroke OSA」衝突。
  - 與「overnight oximetry 可以完全取代 polysomnography / HSAT」衝突。
  - 與「CPAP 已確定可降低 recurrent stroke」衝突。
  - 與「poststroke sleep apnea 一定永久存在」衝突。
  - 與「auto-titrating CPAP 對所有 acute stroke 都適用」衝突。
- 待追蹤問題：
  - 若 Sleep SMART 已有正式 published outcome report，需另行單一來源 ingest，不可由本篇推測結果。
  - OSA cardiovascular disease guideline / AHA statement 若要升級 evidence hierarchy，需另行單一來源處理。
  - Central sleep apnea treatment、PAP titration and adherence interventions 需 dedicated sleep medicine sources。
