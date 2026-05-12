---
title: Source Manifest 與 Source Drift
created: 2026-05-12
updated: 2026-05-12
type: workflow
domain: [methodology]
tags: [wiki_maintenance, source_manifest, source_drift, provenance]
sources: []
source_tier: 1
evidence_level: consensus
confidence: high
contested: false
contradictions: []
---

# Source Manifest 與 Source Drift

## 一句話定義

Source manifest 是 `C:\知識百科` 端用來追蹤已 ingest raw source fingerprint 的 JSON 檔；source drift 指來源摘要指向的 raw file 路徑相同，但 sha256 與先前紀錄不同。

## 核心機制

### 固定位置

```text
08_工具與Workflow/source_manifest.json
```

### manifest entry 至少記錄

1. raw source relative path
2. sha256
3. size_bytes
4. mtime_ns
5. last_checked
6. 對應 `10_來源摘要/` 頁面

### 操作原則

1. `C:\原始資料` 仍然是 immutable；manifest 只記錄，不修改 raw file。
2. 新增或更新來源摘要後，若該頁有 `source_path` 或 `原始檔：...`，就更新 manifest。
3. health check 發現 `source_manifest_missing` 時，代表摘要可追溯但尚未 fingerprint。
4. health check 發現 `source_drift` 時，不可直接覆寫摘要；先回到該單一來源重新確認。
5. health check 發現 `raw_source_missing` 時，不得自行換成另一個 raw source；需在 `log.md` 標記並等待確認。

## 可執行命令

```powershell
python C:\知識百科\08_工具與Workflow\wiki_health_check.py `
  --wiki C:\知識百科 `
  --raw C:\原始資料 `
  --update-source-manifest `
  --format markdown `
  --output C:\知識百科\08_工具與Workflow\health_check_report_latest.md
```

## 相關頁面

- ingest：[[知識百科_ingest_工作流]]
- health check：[[知識百科_健康檢查流程]]
- 腳本：[[Wiki_Health_Check_腳本]]
