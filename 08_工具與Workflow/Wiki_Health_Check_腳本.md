---
title: Wiki health check 腳本
created: 2026-04-23
updated: 2026-05-12
type: workflow
domain: [methodology]
tags: [wiki_maintenance, lint, automation, health_check]
sources: []
source_tier: 1
evidence_level: consensus
confidence: high
contested: false
contradictions: []
---

# Wiki health check 腳本

## 一句話定義

這是知識百科的可執行 lint / health-check 腳本頁，負責把 [[知識百科_健康檢查流程]] 的規則落成可重跑的檢查流程。

## 核心機制

### 腳本位置

- `08_工具與Workflow/wiki_health_check.py`
- `08_工具與Workflow/tests/test_wiki_health_check.py`

### 執行指令

```powershell
python C:\知識百科\08_工具與Workflow\wiki_health_check.py `
  --wiki C:\知識百科 `
  --raw C:\原始資料 `
  --update-source-manifest `
  --format markdown `
  --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md
```

腳本現在會自動偵測 Windows `C:\...` 或 WSL `/mnt/c/...` 預設路徑，但固定在指令列明寫 `--wiki` / `--raw` 仍比較可重現。

### 維護原則

- 規則調整先改 [[知識百科_健康檢查流程]]，再同步腳本。
- 若 lint 結果與人工判讀明顯不符，先修腳本，再重跑報告。
- raw 驗證上限維持每回合 5 件，不在腳本外偷偷擴張。

## 臨床表現

- 本頁不是疾病頁；此處應改讀為常見使用情境、常見失敗模式與需要警覺的流程 red flags。

## 評估方式

### 目前檢查項目

- orphan pages
- weakly linked pages（缺乏交叉連結）
- broken links
- index completeness
- frontmatter completeness
- oversized pages
- stale candidates（舊結論未被新來源更新）
- contradiction candidates（相互矛盾但未標示）
- missing core topics（應建未建）
- source manifest missing（source summary 有 raw path 但 manifest 缺 entry）
- source drift（raw file sha256 與 manifest 不一致）
- raw source missing（source summary 指向不存在的 raw file）
- raw backlog（raw 已存在但尚未編入）
- raw verification queue（每回合最多 5 個 raw files）

## 治療原則

- 目前頁面尚未整理出 Non-pharmacologic、Pharmacologic、Injection / procedure、Rehabilitation program 的決策順序。

## 臨床決策點

- 什麼情況要治療？先看是否真的改變 pain、function、safety、participation 或訓練輸出。
- 什麼情況要轉介？遇到 red flags、診斷不確定、需要程序性介入或超出本頁可處理範圍時。
- 什麼情況不該做？當證據不足、機制不合、風險高於預期收益，或結果不會改變決策時。

## 限制與未定論

- 目前頁面尚未明確寫出證據限制、教材未講清楚處或不同來源可能衝突之處。

## 理解缺口

- Wiki health check 腳本 的核心輸出是什麼？如果要教給住院醫師，最少要保留哪三個步驟？
- 哪些情況代表這個流程或總覽頁仍然不夠可執行？
- 這頁和相鄰主題頁的邊界在哪裡？
- 目前缺少明確處置順序：何時觀察、何時介入、何時轉介仍需補強。
- 目前缺少 bedside 可辨識表現：症狀、檢查發現或 red flags 仍需補強。

## 臨床使用版

- 若 Wiki health check 腳本 不能縮短查找、整理或衝突處理時間，代表流程描述仍然不夠可執行。
- 每一步都要能回答下一個實際動作是什麼，否則就只是說明文件，不是 workflow。

## 來源

### 證據標記

- 來源層級：1
- evidence_level：consensus
- confidence：high

## 相關頁面

### 相關頁面

- 工作流規範：[[知識百科_健康檢查流程]]
- 最新報告位置：`08_工具與Workflow/health_check_report_latest.md`
