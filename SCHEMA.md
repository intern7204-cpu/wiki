# Wiki Schema — 個人醫學知識百科

此 schema 由 user 提供的長期維護指令濃縮而成，作為 agent 工作時的固定規範。
若與指令正文衝突，以 user 指令正文為準。

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
- `09_來源摘要/`

## 4. 語言與檔名

- 頁面內容：繁體中文
- 醫學專有名詞：保留 American English
- 病歷 / report / consultation note / discharge summary 類模板：美式英文
- 檔名：**繁體中文**，允許使用底線與中文括號，不使用空白
  - 例：`無氧閾值.md`、`CPET_通氣閾值.md`、`ADHD_臨床診斷.md`
  - 來源摘要頁可以保留英文原檔名重點 + 年份：`Poole_2020_anaerobic_threshold.md`

## 5. 來源優先級

### 第一優先（主框架來源）
1. review article
2. textbook chapter
3. UpToDate

### 第二優先（輔助理解）
4. 科普書
5. 網站資料（須評估可信度）

### 第三優先（修正/補充訊號，不作主框架）
6. original article

## 6. 頁面 frontmatter

```yaml
---
title: 頁面標題
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: overview | concept | method | clinical | source_summary | workflow | query
domain: [CPET, exercise_physiology, rehabilitation, PMR, gait, pediatric, methodology, ...]
tags: []
sources: [09_來源摘要/xxx.md]
source_tier: 1 | 2 | 3           # 主要來源層級
evidence_level: consensus | emerging | limited | conflicting | expert_opinion
confidence: high | medium | low
contested: true | false
contradictions: []
---
```

## 7. 頁面結構（建議）

每個知識頁儘量包含：
1. 一句話定義
2. 核心概念
3. 機制 / 原理
4. 臨床或研究上的重要性
5. 方法學重點（若適用）
6. 證據層級與來源
7. 目前限制 / 爭議點
8. 相關頁面連結（至少 2 條 `[[wikilink]]`）

## 8. 來源處理規則

- review / textbook / UpToDate → 建主幹、定義概念、形成共識段落
- original article → 只做補充、修正、更新、新興證據標示；**不可直接覆寫主結論**
- 科普書、網站 → 輔助理解，不作高階醫學結論唯一依據，須顯示屬性與可信度
- 網站分類：官方機構 / 專業醫學平台 / 教育網站 / 商業網站 / 未知可信度

## 9. 衝突處理

1. 先保留高層級來源建立的主框架
2. original article 作為修正訊號，不直接覆寫
3. 多篇一致的 original article → 可建「新興證據」段落
4. 新版 review / guideline / textbook / UpToDate → 用於更新主框架
5. 所有衝突**顯式記錄**於頁面「爭議 / 衝突」段落與 frontmatter `contradictions`

## 10. ingest 工作流

每次新增 `C:\原始資料` 文件：
1. 先列出與本次主題最相關的候選文件
2. 依來源優先級與相關性排序
3. 本回合最多只選讀 5 個文件
4. 逐一讀取這 5 個文件
5. 判定來源類型：review article / textbook chapter / UpToDate / 科普書 / 網站資料 / original article
6. 給每個文件一個來源等級與可信度標籤
7. 產生來源摘要頁到 `09_來源摘要/`
8. 更新相關主題頁
9. 必要時建立新頁
10. 更新 `index.md`
11. 在 `log.md` 記錄本次 ingest 與本批次已處理文件
12. 若發現與既有內容衝突，明確標示衝突，不可默默覆蓋
13. 若仍有未處理候選文件，標記為下一批待處理

補充邊界：
- ingest 的 5-file cap 與 lint / health check 的 5-file raw verification cap 是不同流程上限，數字相同也不可混用
- 不可修改 `C:\原始資料`
- 不可虛構來源內容
- 不可把單篇 original article 誇大成共識
- 不可因網站語氣肯定就視為高等級證據

## 11. query 工作流

1. 先查已有 wiki 頁
2. 以已整理知識為主回答
3. 必要時再回查 `C:\原始資料`
4. 高價值整理 → 回寫 `queries/` 或對應主題頁
5. 回答須標示共識 / 有限證據 / 新興研究

## 12. lint 工作流

檢查項目：
- 孤立頁面（無反向連結）
- 缺交叉連結
- 舊結論未被新來源更新
- 矛盾但未標示
- 缺少應建立的核心主題頁
- 原始資料已存在但未編入
- frontmatter 缺失
- tag 不在 taxonomy 內
- 頁面 > 200 行（考慮拆分）
- log.md > 500 條（rotate）

## 13. 行為邊界

可以：整理、摘要、交叉連結、建頁、合併、重組、補索引、建研究骨架
不可以：
- 修改 `C:\原始資料`
- 虛構來源內容
- 把單篇 original article 誇大成共識
- 把未經驗證網站當高等級證據

## 14. log.md 格式

```
## [YYYY-MM-DD] ingest | <來源標題>
## [YYYY-MM-DD] synthesis | <主題>
## [YYYY-MM-DD] lint | <範圍>
## [YYYY-MM-DD] create | <頁名>
## [YYYY-MM-DD] update | <頁名>
## [YYYY-MM-DD] archive | <頁名>
```
