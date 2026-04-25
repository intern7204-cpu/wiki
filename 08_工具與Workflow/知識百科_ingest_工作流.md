---
title: 知識百科 ingest 工作流
created: 2026-04-24
updated: 2026-04-25
type: workflow
domain: [methodology]
tags: [wiki_maintenance, ingest, source_triage, evidence_hierarchy, source_summary]
sources: []
source_tier: 1
evidence_level: consensus
confidence: high
contested: false
contradictions: []
---

# 知識百科 ingest 工作流

## 一句話定義

當 `C:\原始資料` 新增文件時，先做主題相關候選排序，再以**單批最多 5 份文件**的小批次讀取、判級、摘要、回寫 `C:\知識百科`，且所有衝突都要顯式標示。

## 核心機制

### 核心原則

1. `C:\原始資料` 是 evidence pool，不修改、不搬移、不覆寫。
2. 先決定本次 ingest 的主題，再列候選，不做無主題的大範圍亂讀。
3. 每一批最多只選讀 5 份文件；超出的保留到下一批。
4. 來源排序先看來源優先級，再看與本次主題的直接相關性。
5. 單篇 `original article` 只能作補充或新興訊號，不可硬改主框架。
6. 網站文字即使語氣肯定，也不能直接視為高等級證據。
7. 發現與既有頁面衝突時，必須顯式標示，不能默默覆蓋。

### 來源類型與分級

### 類型判定

- review article
- textbook chapter
- UpToDate
- 科普書
- 網站資料
- original article

### 來源層級

1. Tier 1：review article、textbook chapter、UpToDate
2. Tier 2：科普書、網站資料
3. Tier 3：original article

### 可信度標籤

- `high`：UpToDate、成熟 textbook chapter、methodologically solid review article
- `medium`：可信專業網站、科普書、敘述性較強或範圍較窄的次級來源
- `low`：商業網站、未清楚揭露方法的網站、內容品質不穩定的輔助來源

### 固定步驟

### Step 1 — 列候選文件

1. 先定義本次主題。
2. 從 `C:\原始資料` 列出最相關候選文件。
3. 若同主題候選很多，先保留檔名、路徑、可能類型與簡短理由。

### Step 2 — 候選排序

排序依據固定如下：
1. 來源優先級
2. 與本次主題的直接相關性
3. 是否能補現有主題頁缺口或來源摘要缺口
4. 是否可能引入需顯式處理的新衝突

### Step 3 — 選批次

1. 本回合最多只選讀 5 個文件。
2. 若候選超過 5 個，未入選者標記為 `下一批待處理`。
3. 對入選文件逐一讀取；若本批實際少於 5 份，就讀完本批全部。
4. `health check` 的 raw verification 5-file cap 與本頁屬不同流程；數字相同也不可混用，見 [[知識百科_健康檢查流程]]。

### Step 4 — 逐一讀取與判級

對入選文件逐一完成：
1. 讀取文件內容。
2. 判定來源類型。
3. 給予來源層級與可信度標籤。
4. 抽出只屬於該來源真正說過的重點，不可擴寫成來源未主張的內容。

### Step 5 — 建立來源摘要

每份已讀文件都要建立或更新一頁 `09_來源摘要/<來源頁>.md`，至少包含：
1. bibliographic identity / 來源類型
2. 本文核心主張
3. 對臨床 / 方法學 / 研究的重要性
4. 限制與不該過度外推之處
5. 與既有主題頁的關聯

### Step 6 — 更新主題頁

1. 更新相關主題頁。
2. 必要時建立新頁。
3. 補上交叉連結，避免新頁只連向來源摘要而不連向平行概念頁。

### Step 7 — 處理衝突

1. 若新來源與既有內容一致，正常整合即可。
2. 若新來源與既有內容衝突，依 [[知識百科_衝突處理規則]] 顯式標示衝突。
3. Tier 3 挑戰 Tier 1 時，先標示為新興訊號或待驗證，不直接重寫主框架。

### Step 8 — 維護索引與紀錄

1. 更新 `index.md`
2. 更新 `log.md`
3. 在 `log.md` 記下：
   - 本次 ingest 主題
   - 本批實際已處理文件
   - 每份文件的來源類型 / tier / 可信度
   - 是否有新頁、更新頁、衝突標示
   - 下一批待處理名單

### 最低輸出要求

每完成一批 ingest，至少要有以下結果：
1. `09_來源摘要/` 新增或更新對應來源頁
2. 至少一個相關主題頁被更新，或建立新頁
3. `index.md` 已補條目
4. `log.md` 已留下 batch-level 紀錄
5. 若仍有候選未讀，已明確列為下一批待處理

### 與其他工作流的邊界

- 本頁處理的是「主動編譯新來源進知識百科」。
- [[知識百科_健康檢查流程]] 處理的是「先掃已編譯 wiki，再決定是否回查 raw」。
- ingest 的 5-file cap 與 health check 的 5-file verification cap 是不同流程上限；數字相同也不可混用。

## 臨床表現

- 本頁不是疾病頁；此處應改讀為常見使用情境、常見失敗模式與需要警覺的流程 red flags。

## 評估方式

- 目前頁面尚未整理出 History、Physical examination、Scale / test、Imaging / lab 的實際用法。

## 治療原則

- 目前頁面尚未整理出 Non-pharmacologic、Pharmacologic、Injection / procedure、Rehabilitation program 的決策順序。

## 臨床決策點

- 什麼情況要治療？先看是否真的改變 pain、function、safety、participation 或訓練輸出。
- 什麼情況要轉介？遇到 red flags、診斷不確定、需要程序性介入或超出本頁可處理範圍時。
- 什麼情況不該做？當證據不足、機制不合、風險高於預期收益，或結果不會改變決策時。

## 限制與未定論

- 目前頁面尚未明確寫出證據限制、教材未講清楚處或不同來源可能衝突之處。

## 理解缺口

- 知識百科 ingest 工作流 的核心輸出是什麼？如果要教給住院醫師，最少要保留哪三個步驟？
- 哪些情況代表這個流程或總覽頁仍然不夠可執行？
- 這頁和相鄰主題頁的邊界在哪裡？
- 目前缺少完整評估框架：History、Physical examination、Scale / test、Imaging / lab 仍需補強。
- 目前缺少明確處置順序：何時觀察、何時介入、何時轉介仍需補強。

## 臨床使用版

- 若 知識百科 ingest 工作流 不能縮短查找、整理或衝突處理時間，代表流程描述仍然不夠可執行。
- 每一步都要能回答下一個實際動作是什麼，否則就只是說明文件，不是 workflow。

## 來源

### 證據標記

- 來源層級：1
- evidence_level：consensus
- confidence：high

## 相關頁面

### 相關頁面

- schema 規範：`SCHEMA.md`
- 總索引：`index.md`
- 維護紀錄：`log.md`
- health check：[[知識百科_健康檢查流程]]
- 衝突處理：[[知識百科_衝突處理規則]]
