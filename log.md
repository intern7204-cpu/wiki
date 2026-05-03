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
