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

## [2026-05-08] correction | Ferguson et al. 2010 — Effect of recovery duration from prior exhaustive exercise on the parameters of the power-duration relationship

- 修正原因：
  - 使用者要求跑完一輪完整 §6 流程，並選一篇運動生理相關文獻。
  - 本來源於 2026-04-25 batch ingest（batch 29），依使用者 2026-05-01 cutoff 規則屬「之前不算」之列；舊摘要使用非 skill 模板（一句話定義 / 核心機制 / 臨床表現 / 評估方式 / ...），缺 Fact / Inference / Assumption / Uncertainty 分層、缺 Conflicts With Existing Knowledge 與 Pages That Should Be Created or Updated 段落，須依單一來源 workflow 重做。
- 本輪單一來源：
  - `C:\原始資料\ferguson-et-al-2010-effect-of-recovery-duration-from-prior-exhaustive-exercise-on-the-parameters-of-the-power-duration\effect of recovery duration from prior exhaustive exercise on the parameters of the power duration.md`
  - 只完整處理此一篇來源；未混入 Skiba 2014、Skiba 2015、Caen 2019、Caen 2021、Chorley 2021、Lievens 2024 或其他 W' recovery raw source。
- 重新建立來源摘要：
  - `09_來源摘要/Ferguson_2010_Wprime_recovery_after_exhaustion.md`（依 skill 模板完整重寫，覆蓋舊版）。
- 更新頁面：
  - `04_CPET/Wprime_Recovery.md`（補 t1/2 數值、CP 不變的統計、Ferguson 2010 對 fatigue-metabolite integration 假說的明確主張）。
  - `04_CPET/Wprime_Balance_Model.md`（補 CP `P = 0.922`、三條 t1/2 與 fatigue-metabolite integration 對應）。
  - `04_CPET/CP_Wprime_Interval_Design.md`（補 2 / 6 / 15 min 20-W recovery 對應的 W' 回補比例）。
  - `index.md`（更新 Ferguson 2010 entry 描述；Last updated 2026-05-04 → 2026-05-08；Total pages 維持 540，本輪未新增獨立概念頁）。
  - `log.md`（本則 correction）。
- 抽出概念：
  - Post-exhaustion W' recovery kinetics（與 VO2 / blood lactate 同步比對）：在 supra-CP exhaustive bout 後，CP 對 prior exhaustion 高度穩定，W' 才是承擔 fatigue 的主要參數；W' recovery 速度介於 VO2 與 blood lactate 之間，且不能用任一單一代謝 proxy 取代。
- 本輪重新核對的直接事實：
  - n=6 healthy recreationally active men（24 ± 4.2 yr；179.6 ± 7.5 cm；86.5 ± 15.3 kg）；cycle ergometer。
  - Control：`CP ≈ 212 ± 34 W`、`W' ≈ 21.60 ± 5.16 kJ`、`VO2max ≈ 3.78 ± 0.56 L/min`、`θ̂L ≈ 1.87 ± 0.35 L/min`（≈ 49% VO2peak）、`WR6 ≈ 269 ± 34 W`、`[L−]LIM ≈ 10.14 mM`。
  - Conditioning bout：`tLIM ≈ 366 ± 21 s`；`VO2peak` 與 `[L−]LIM` 與 control 不顯著差異。
  - Postconditioning CP（`P = 0.922` vs control）：2-min Rec `213 ± 36 W`；6-min Rec `213 ± 34 W`；15-min Rec `213 ± 36 W`。
  - Postconditioning W'（`P = 0.001` vs control）：2-min Rec `7.8 ± 1.4 kJ`（37 ± 5%）；6-min Rec `14.1 ± 3.7 kJ`（65 ± 6%）；15-min Rec `18.5 ± 4.6 kJ`（86 ± 4%）。
  - Interpolated half-times：W' `t1/2 = 234 ± 32 s`；VO2 `t1/2 = 74 ± 2 s`；blood `[L−]` `t1/2 ≈ 1366 ± 799 s`。
  - 「Baseline」 VO2 在 conditioning 結束後仍升高（2 min `1.37`、6 min `1.06`、15 min `0.87` L/min），代表 post-conditioning bout 起點 O2 deficit 較小，作者明文承認此為 efficiency caveat。
  - 殘留 `[L−]`：2 min `10.00`、6 min `9.09`、15 min `6.43 mM`；即使 15 min 仍顯著高於 pre-exercise。
  - Postconditioning P-tLIM 仍 hyperbolic（`R² > 0.994`）；CP / W' SE 維持 `< 3 W` / `< 1.25 kJ`。
  - 作者主張：W' 不是單純 finite anaerobic store，而較可能反映 fatigue-related metabolite accumulation/clearance（Pi、K+、可能的 oxidative stress、glycogen / fiber-type-dependent depletion）的整合。
- 移除或降級的陳述：
  - 舊摘要的「臨床表現 / 評估方式 / 治療原則 / 臨床決策點 / 理解缺口 / 臨床使用版」段落結構違反 skill 模板，已移除；改採 Source Type / Reliability Level / One-Sentence Summary / Core Concepts Extracted / Clinically Useful Points / Research-Useful Points / Conflicts With Existing Knowledge / Pages That Should Be Created or Updated / Suggested Tags 結構。
  - 舊摘要把 W' 與 VO2 / lactate 的比較寫成「W' recovery 介於 VO2 與 lactate recovery 之間」單行命題；改為列出三條具體 t1/2，並標明 Inference / Assumption。
  - 舊摘要僅以「sample size 小、僅 healthy men、VO2 為 PCr proxy、exhaustion paradigm 不一定等同 partial depletion」四點限制；本輪補上 recovery power 僅 20 W、未做正式 mono / bi-exponential 模型擬合、未量 intramuscular `[PCr] / [L−] / [H+]` 等限制，並區分 Assumption（W' 在 conditioning 結束時 ≈ 0、postconditioning bout 中 W' 不再恢復、pulmonary VO2 為 muscle PCr proxy）與 Uncertainty。
- 發現衝突：
  - 與「W' = 一個有限 anaerobic 油箱，耗盡即 exhaustion」衝突：CP 不變、W' 曲線恢復、`[L−]LIM` 與 `VO2peak` 不隨 prior exhaustion 改變，與單純 finite-store 解釋不合。
  - 與「W' recovery ≈ PCr / VO2 recovery」衝突：W' 慢於 VO2 約三倍 t1/2。
  - 與「W' recovery ≈ lactate clearance」衝突：blood lactate t1/2 ≈ 1366 s，慢於 W' 約 5–6 倍。
  - 與「prior heavy / supra-CP exercise 會降低 CP」衝突：本研究 CP 在三種 recovery 下皆不變，與 Coats et al. 2003 的 CP 可下降說法不一致；作者明確不採信 Coats 假設。
  - 與「W'BAL 等於精確的 anaerobic balance」衝突：本研究強調 W' recovery 是 model-extracted whole-system construct，不是直接量到的儲量。
- 待追蹤問題：
  - 本研究 recovery power 僅 20 W、僅 cycle ergometer、僅 healthy male n=6；女性、青少年、長者、運動員、心肺患者、不同 mode 與不同 recovery power 仍待後續來源各自單一 ingest。
  - 與 partial-depletion / non-exhaustion paradigm 的 cross-validation：本來源僅探討 full exhaustion；後續可挑 Skiba 2015、Caen 2019、Lievens 2024 進行 correction（Lievens 2024 本身已於 5/1 cutoff 後重做需求；本 worktree 仍為 4/25 batch 版本）。
  - 是否新建獨立的 `Fatigue_Metabolite_Integration_Model_of_Wprime` 概念頁，待後續 Pi / K+ / Ca2+ handling 來源（如 Allen 2008、Sjogaard 1990 之外的近年 review）入庫後再決定。
  - 「W'BAL 0 J 不等於精確 exhaustion 秒數」這條共通限制，目前散見於 Wprime_Balance_Model / Wprime_Recovery / CP_Wprime_Interval_Design 三頁，仍未獨立成 caveat 頁。
- 待處理來源：
  - 既有 raw verification queue 不變；本輪未引入新候選。
  - W' recovery 舊 batch 來源剩餘 correction 候選：`Skiba_2014_work_recovery_durations_Wprime_reconstitution`、`Skiba_2015_intramuscular_determinants_Wprime_recovery`、`Caen_2019_Wprime_reconstitution_depends_on_work_and_recovery`、`Bartram_2018_Wprime_recovery_elite_cyclists`、`Sreedhara_2020_Modeling_Wprime_Recovery`、`Chidnok_2013_intermittent_exercise_PCr_CP`、`Karsten_2016_intertrial_recovery_CP_Wprime`、`Karsten_2017_TT_vs_TTE_CP_Wprime`、`Chorley_2021_biexponential_Wprime_reconstitution_trained_cyclists`、`McMahon_Jenkins_PCr_resynthesis_after_intense_exercise`、`Lievens_2024_partial_Wprime_recovery`、`Caen_2021_Wprime_recovery_two_phase`、`Skiba_2012_modeling_Wprime_expenditure_reconstitution`、`Skiba_Clarke_Wprime_balance_model`、`Sreedhara_2019_power_energy_models`。

## [2026-05-08] correction | Skiba et al. 2015 — Intramuscular determinants of the ability to recover work capacity above critical power

- 修正原因：
  - 使用者要求再跑一輪完整 §6 流程，並選一篇運動生理相關文獻。
  - 上一輪 Ferguson 2010 correction 已釐清「W' recovery ≠ VO2 / lactate proxy」並列 Skiba 2015 為 W' recovery 舊 batch 來源剩餘 correction 候選；接續以 31P-MRS / 1H-MRS 直接檢驗「W' = PCr」假設的 Skiba 2015 為自然延續。
  - 本來源於 2026-04-25 batch ingest（batch 29 後續 W' recovery 系列），依使用者 2026-05-01 cutoff 規則屬「之前不算」之列；舊摘要使用非 skill 模板（一句話定義 / 核心機制 / 臨床表現 / 評估方式 / 治療原則 / 臨床決策點 / 限制與未定論 / 理解缺口 / 臨床使用版），缺 Fact / Inference / Assumption / Uncertainty 分層、缺 Conflicts With Existing Knowledge 與 Pages That Should Be Created or Updated 段落，且把 [PCr] T1/2 寫成 38 s（與 Table 1 群均 39 ± 16 s 不一致），須依單一來源 workflow 重做。
- 本輪單一來源：
  - `C:\原始資料\s00421-014-3050-3\s00421-014-3050-3.md`
  - 只完整處理此一篇來源；未混入 Ferguson 2010、Skiba 2012、Skiba 2014、Caen 2019、Caen 2021、Chorley 2021、Chidnok 2013、Lievens 2024、Sreedhara 2020 或其他 W' recovery raw source。
- 重新建立來源摘要：
  - `09_來源摘要/Skiba_2015_intramuscular_determinants_Wprime_recovery.md`（依 skill 模板完整重寫，覆蓋舊版）。
- 更新頁面：
  - `04_CPET/Wprime_Recovery.md`（補 [PCr] T1/2 修正為 39 ± 16 s、W' 個體範圍 135–426 s、`τ_[PCr]` vs `τ_W'` 不相關之 r/p、D[PCr] 與 model-predicted W' 的 r=0.99，並標 single-leg / passive recovery / CP ≈ 8.1 W / 60 s 早期採樣 caveat）。
  - `04_CPET/Wprime_Balance_Model.md`（補新 `τ_W' = W'_0 / D_CP` 推導、Passing–Bablok systematic offset intercept ≈ 288 s、carnosine 為 exploratory）。
  - `05_Exercise_Physiology/PCr_Resynthesis.md`（補 D[PCr] 與 oxidative reserve 概念、bulk [PCr] vs D[PCr] 對 `W'` 不同預測力，並標 single-leg passive recovery caveat；frontmatter updated 5/8）。
  - `index.md`（更新 Skiba 2015 entry 描述以反映 D[PCr] / oxidative reserve / 新 τ 推導；Last updated 維持 2026-05-08；Total pages 維持 540，本輪未新增獨立概念頁）。
  - `log.md`（本則 correction）。
- 抽出概念：
  - Intramuscular determinants of W' recovery（W' vs [PCr] vs pH vs carnosine）：使用 31P-MRS / 1H-MRS 同步追蹤 [PCr]、[Pi]、pH、carnosine，並以「conditioning bout / passive recovery / experimental bout」三段式 single-leg 模型，比較 W' recovery 與這些代謝指標的時間進程；本輪結論是 W' recovery 較貼近「再可動員的 oxidative reserve」（D[PCr] / D VO2），而不是 bulk PCr 儲量本身。
- 本輪重新核對的直接事實：
  - n=10 healthy recreationally trained subjects（4F/6M；age `22 ± 7 yr`；height `1.71 ± 0.1 m`；body mass `71.8 ± 15.4 kg`）；3 位 strength/power background、其餘 endurance；非高度訓練者。
  - Phase 1（lab）：3–5 段 single-leg knee-extension to exhaustion（90–600 s，metronome 40 ext/min），以 work（`m × g × h`）對 time 線性回歸求 CP（slope）與 W'（y-intercept）；線性度 `r² = 0.99–1.0`。
  - Phase 2（1.5T MRI bore）：4 次 trials；每次 conditioning bout（B_C）at `WR180` to exhaustion → passive 1 / 2 / 5 / 7 min recovery（leg fully extended on scanner bed）→ experimental bout（B_E）at the same `WR180` to exhaustion；W' recovery = work in B_E / work in B_C。
  - 31P-MRS：每 12 s 一筆，spectral width 1500 Hz；jMRUI / AMARES fit `[Pi]、PCr、α/β/γ-ATP、PDE` peaks；intracellular pH 由 `Pi` 對 `PCr` chemical shift 估。
  - 1H-MRS：right rectus femoris voxel `20 × 30 × 50 mm`、PRESS、TR 2000 ms / TE 31 ms / 96 averages；以 water peak 為內標。
  - Group means：CP `8.1 ± 2.79 W`；W' `1.14 ± 0.93 kJ`。
  - W' recovery：group mean `T1/2 = 232 ± 108 s`；個體範圍 `135–426 s`；group 線性回歸 `r = 0.99, p = 0.0009`；CUSUM 與 runs test 均不偏離線性；60 s 已恢復 `57%`，420 s 已恢復 `96%`。
  - [PCr] recovery：group mean `T1/2 = 39 ± 16 s`（abstract 寫 `38 s`）；single-exp `r² = 0.99`、`τ ≈ 57 s`。
  - B_C 結束 vs B_E 耗竭時 [PCr]、[Pi]、pH 在 4 個 recovery 條件下無顯著差異（`p = 0.98 / 0.31 / 0.07`）。
  - `τ_[PCr]` vs interpolated `τ_W'`：`r = 0.38, p = 0.28`（無顯著相關）。
  - D[PCr]（B_C 結束 [PCr] − B_E 耗竭 [PCr]）vs model-predicted W' recovery：`r = 0.99, p = 0.005`。
  - 新 `τ_W' = W'_0 / D_CP` 推導（Appendix 1）vs Skiba 2012 既有 τ：`r = 0.84, p = 0.001`；Passing–Bablok systematic offset（intercept `288, 95% CI 235–350`），slope 非 proportional（`0.79, 95% CI 0.59–1.26`）。
  - 個體層次 model vs 觀測 W' 線性回歸：6/10 顯著（`r = 0.96–0.99`，allow non-zero intercept）；強迫 zero intercept 時 10/10 顯著（`r = 0.88–0.98`）。
  - carnosine vs `W' T1/2` inverse curvilinear `R² = 0.55`；剔除單一 outlier 後 `R² = 0.80`。
  - pH 與 W' 強度 / W' recovery / pH 變化在所有層級皆無相關。
  - Appendix 2：「微觀線性、巨觀曲線」假設模擬，提供 fiber/muscle 異質性建模路徑，但屬 hypothesis-level。
- 移除或降級的陳述：
  - 舊摘要的「臨床表現 / 評估方式 / 治療原則 / 臨床決策點 / 理解缺口 / 臨床使用版」段落結構違反 skill 模板，已移除；改採 Source Type / Reliability Level / One-Sentence Summary / Core Concepts Extracted / Clinically Useful Points / Research-Useful Points / Conflicts With Existing Knowledge / Pages That Should Be Created or Updated / Suggested Tags 結構。
  - 舊摘要把 [PCr] T1/2 直接寫成「`38 s`」（abstract 文字），未標 group mean `39 ± 16 s` 的個體分散；本輪以 Table 1 群均為主、abstract 數字併陳。
  - 舊摘要寫「研究中的 novel derivation 對 W' recovery 的預測和實測值相當接近」未標明 (a) Skiba 2012 既有資料與新 τ 之間 Passing–Bablok systematic offset，(b) 個體層次 6/10 顯著（須 non-zero intercept）、強迫 zero intercept 才 10/10 顯著；本輪補上。
  - 舊摘要把 carnosine 與 `W' T1/2` 的 inverse 關係寫成「inverse curvilinear」未標 `R²` 與 outlier 敏感度；本輪補 `R² = 0.55` 含 outlier、`R² = 0.80` 排除後，並標 exploratory。
  - 舊摘要的「W' = D[PCr] / oxidative reserve」單行寫法易被誤解為等價；本輪改述為 D[PCr] 與 model-predicted W' 高度相關（r=0.99），並區分 D[PCr] 與 actual measured W' 的 r=0.93（接近但未達 p<0.05 顯著）。
  - 舊摘要把 single-leg 線性 vs whole-body 曲線形差異略帶過；本輪補上「微觀線性、巨觀曲線」hypothesis 與 60 s 採樣 caveat 兩種解釋。
- 發現衝突：
  - 與「W' = 一個 PCr / anaerobic 油箱」衝突：bulk `[PCr]` 比 `W'` 快約 6×，且 `τ_[PCr]` 與 `τ_W'` 不相關。
  - 與「W' recovery 可用單一 universal `tau` 完整描述」衝突：本研究個體 T1/2 範圍 `135–426 s`，且 `τ_W' = W'_0 / D_CP` 由 D_CP 與 W'_0 共同決定。
  - 與「W' recovery 在 small muscle 與 whole-body 完全相同」衝突：本研究 group mean 為線性、whole-body（Ferguson 2010、Skiba 2012）為曲線形；需以 Appendix 2 微觀 - 巨觀模型 / 取樣不足解釋。
  - 與「pH 是 W' 主要 mediator」衝突：pH at exhaustion / pH recovery / pH 變化與 W' 無相關。
  - 與「Skiba 2012 的 empirical `τ_W' = 546 e^(−0.01·D_CP) + 316` 為 universal recovery formula」衝突：作者自己引入的新推導顯示 systematic offset，代表舊式不該外推到不同 modality / 個體。
  - 與「W'BAL 是直接量到的真實剩餘油箱」衝突：本研究反覆強調 W' recovery 為 model-extracted、whole-system construct。
- 待追蹤問題：
  - 本研究為 single-leg knee-extension、passive recovery、CP ≈ 8.1 W；女性次群體分析、trained athletes、心肺族群、不同 mode（cycle / row / run）與不同 recovery power 仍待後續來源各自單一 ingest。
  - W' recovery 舊 batch 來源剩餘 correction 候選下一輪可挑 `Skiba_2012_modeling_Wprime_expenditure_reconstitution`（核對新 τ 推導的原始驗證資料）、`Caen_2019_Wprime_reconstitution_depends_on_work_and_recovery`（W' 對 prior bout architecture 的依賴性）或 `Sreedhara_2020_Modeling_Wprime_Recovery`（recovery power × duration 的 over-prediction by SK2 / BAR）。
  - carnosine vs W' 為 exploratory；後續若有 β-alanine supplementation RCT + 31P/1H-MRS 來源入庫，可獨立成 `Carnosine_and_Muscle_Performance` 概念頁。
  - D[PCr] / oxidative reserve 概念可考慮與 `D VO2` 整合為單獨概念頁，但需多一輪 correction 後再評估。
  - 「W'BAL 0 J 不等於精確 exhaustion 秒數」這條共通限制，目前散見於三頁，仍未獨立成 caveat 頁。
- 待處理來源：
  - 既有 raw verification queue 不變；本輪未引入新候選。
  - W' recovery 舊 batch 來源剩餘 correction 候選（已扣除本輪處理之 Skiba 2015）：`Skiba_2014_work_recovery_durations_Wprime_reconstitution`、`Caen_2019_Wprime_reconstitution_depends_on_work_and_recovery`、`Bartram_2018_Wprime_recovery_elite_cyclists`、`Sreedhara_2020_Modeling_Wprime_Recovery`、`Chidnok_2013_intermittent_exercise_PCr_CP`、`Karsten_2016_intertrial_recovery_CP_Wprime`、`Karsten_2017_TT_vs_TTE_CP_Wprime`、`Chorley_2021_biexponential_Wprime_reconstitution_trained_cyclists`、`McMahon_Jenkins_PCr_resynthesis_after_intense_exercise`、`Lievens_2024_partial_Wprime_recovery`、`Caen_2021_Wprime_recovery_two_phase`、`Skiba_2012_modeling_Wprime_expenditure_reconstitution`、`Skiba_Clarke_Wprime_balance_model`、`Sreedhara_2019_power_energy_models`。

