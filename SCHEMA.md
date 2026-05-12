# Wiki Schema — 個人醫學知識百科

此 schema 由 user 提供的長期維護指令濃縮而成，作為 agent 工作時的固定規範。
若與 `AGENTS.md` 或使用者指令正文衝突，以 `AGENTS.md` 與使用者指令正文為準。

## 1. 領域（Domain）

主要面向：
- rehabilitation / PM&R
- CPET
- exercise physiology
- medical methodology / clinical reasoning
- gait / biomechanics / orthotics / shoes
- pediatric developmental evaluation
- research notes and synthesis

## 2. 目錄分層

### 原始資料層（immutable）
- 路徑：`C:\原始資料`（WSL 下 `/mnt/c/原始資料`）
- 只讀，不得修改、覆寫、搬移、刪除

### 知識百科層（editable）
- 路徑：`C:\知識百科`（WSL 下 `/mnt/c/知識百科`）
- agent 工作區，所有編譯、整理、交叉連結結果存於此

## 3. 資料夾結構

必備：
- `index.md`
- `log.md`

主題資料夾：
- `00_總覽/`
- `01_核心概念/`
- `02_方法學/`
- `03_疾病與臨床主題/`
- `04_CPET/`
- `05_Exercise_Physiology/`
- `06_Gait_Biomechanics/`
- `07_Pediatric_Development/`
- `08_工具與Workflow/`
- `09_NCV EMG 周邊神經病變/`
- `10_來源摘要/`

## 4. 語言與檔名

- 頁面內容：繁體中文
- 醫學專有名詞：保留 American English
- 病歷 / report / consultation note / discharge summary 類模板：美式英文
- 檔名：**繁體中文**，允許使用底線與中文括號，不使用空白
  - 例：`無氧閾值.md`、`CPET_通氣閾值.md`、`ADHD_臨床診斷.md`
  - 來源摘要頁可以保留英文原檔名重點 + 年份：`Poole_2020_anaerobic_threshold.md`

## 5. Session orientation

每次開始 ingest、query、lint 或大型整理前，先完成 orientation：

1. 讀 `SCHEMA.md`。
2. 讀 `index.md`，確認既有頁面、hub pages 與可能重複頁。
3. 讀 `log.md` 最近紀錄，確認 pending source、近期 correction 與待追蹤問題。
4. 搜尋 wiki 中同義或相鄰概念；既有頁面優先更新，不重複建頁。

## 6. 來源優先級

醫學與臨床知識來源可信度依序為：

1. guideline
2. textbook chapter
3. systematic review / meta-analysis
4. narrative review / scoping review
5. original research article
6. UpToDate / ClinicalKey topic review
7. 專業機構網站
8. 臨床經驗或個人筆記
9. 一般網站、社群文章、未審查內容

若來源衝突，優先保留高層級證據，標記低層級證據限制，不把不確定內容寫成定論。

## 7. 頁面 frontmatter

```yaml
---
title: 頁面標題
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: overview | concept | method | clinical | source_summary | workflow | query
domain: [CPET, exercise_physiology, rehabilitation, PMR, gait, pediatric, methodology, ...]
tags: []
sources: [10_來源摘要/xxx.md]
source_tier: 1 | 2 | 3           # 主要來源層級
evidence_level: consensus | emerging | limited | conflicting | expert_opinion
confidence: high | medium | low
contested: true | false
contradictions: []
---
```

## 8. 頁面結構（建議）

每個知識頁儘量包含：
1. 一句話定義
2. 核心概念
3. 機制 / 原理
4. 臨床或研究上的重要性
5. 方法學重點（若適用）
6. 證據層級與來源
7. 目前限制 / 爭議點
8. 相關頁面連結（至少 2 條 `[[wikilink]]`）

## 9. 來源處理規則

- guideline / textbook / systematic review / high-quality review → 建主幹、定義概念、形成共識段落
- original research article → 補充、修正、更新或標示新興證據；**不可單獨覆寫主結論**
- UpToDate / ClinicalKey topic review → 可作臨床整理來源，但需保留其 topic review 屬性與更新日期
- 科普書、網站 → 輔助理解，不作高階醫學結論唯一依據，須顯示屬性與可信度
- 網站分類：官方機構 / 專業醫學平台 / 教育網站 / 商業網站 / 未知可信度

## 10. 衝突處理

1. 先保留高層級來源建立的主框架
2. original article 作為修正訊號，不直接覆寫
3. 多篇一致的 original article → 可建「新興證據」段落
4. 新版 review / guideline / textbook / UpToDate → 用於更新主框架
5. 所有衝突**顯式記錄**於頁面「爭議 / 衝突」段落與 frontmatter `contradictions`

## 11. ingest 工作流

每次新增 `C:\原始資料` 文件：
1. 先完成 session orientation：`SCHEMA.md`、`index.md`、`log.md` 最近紀錄。
2. 列出與本次主題最相關的候選文件。
3. 依來源優先級與相關性排序。
4. 本回合只能完整處理 1 個來源。
5. 只讀取這 1 個來源，不混入第二個來源內容。
6. 判定來源類型：guideline / textbook chapter / systematic review / review / UpToDate / ClinicalKey / original research / 科普書 / 網站資料 / local note。
7. 給該來源一個來源等級與可信度標籤。
8. 產生來源摘要頁到 `10_來源摘要/`。
9. 視概念邊界更新既有主題頁或建立新頁。
10. 更新 `index.md`。
11. 在 `log.md` 記錄本次單一來源 ingest、更新頁面、衝突與待處理來源。
12. 若發現與既有內容衝突，明確標示衝突，不可默默覆蓋。
13. 若仍有未處理候選文件，列入 `待處理來源`，不得在同一輪繼續摘要。
14. 若來源摘要有 raw path，更新 `08_工具與Workflow/source_manifest.json`。

補充邊界：
- ingest 永遠是單一來源流程；health check 的 5-file raw verification cap 只適用於驗證佇列，不可混用
- 不可修改 `C:\原始資料`
- 不可虛構來源內容
- 不可把單篇 original article 誇大成共識
- 不可因網站語氣肯定就視為高等級證據

## 12. source manifest 與 source drift

source manifest 位置：

```text
08_工具與Workflow/source_manifest.json
```

用途：
- 記錄已 ingest raw source 的 relative path、size、mtime、sha256、last_checked 與對應 source summary。
- health check 若發現 raw source hash 改變，標記 `source_drift`。
- health check 若來源摘要有 `source_path` 或 `原始檔：...` 但 manifest 無紀錄，標記 `source_manifest_missing`。
- raw source missing 時標記 `raw_source_missing`，不得自行替換來源。

## 13. query 工作流

1. 先讀 `SCHEMA.md`、`index.md` 與 `log.md` 最近紀錄
2. 查已有 wiki 頁
3. 以已整理知識為主回答
4. 必要時再回查 `C:\原始資料`
5. 高價值整理 → 回寫對應主題頁或 query note
6. 回答須標示 fact / inference / assumption / uncertainty，並標示共識 / 有限證據 / 新興研究

## 14. lint 工作流

檢查項目：
- 孤立頁面（無反向連結）
- 缺交叉連結
- broken wikilinks
- 舊結論未被新來源更新
- 矛盾但未標示
- 缺少應建立的核心主題頁
- 原始資料已存在但未編入
- frontmatter 缺失
- tag 不在 taxonomy 內
- 頁面 > 200 行（考慮拆分）
- log.md > 500 條（rotate）
- index 未收錄既有頁面，或 index 指向不存在檔案
- source summary 指向不存在 raw source
- source_manifest_missing / source_drift
- contested / contradictions 欄位與正文不一致

## 15. 行為邊界

可以：整理、摘要、交叉連結、建頁、合併、重組、補索引、建研究骨架
不可以：
- 修改 `C:\原始資料`
- 虛構來源內容
- 把單篇 original article 誇大成共識
- 把未經驗證網站當高等級證據

## 16. log.md 格式

```
## [YYYY-MM-DD] ingest | <來源標題>
## [YYYY-MM-DD] synthesis | <主題>
## [YYYY-MM-DD] lint | <範圍>
## [YYYY-MM-DD] create | <頁名>
## [YYYY-MM-DD] update | <頁名>
## [YYYY-MM-DD] archive | <頁名>
```
