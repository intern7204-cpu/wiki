---
type: source
tags: [exercise-physiology, VO2-kinetics, method, CPET]
created: 2026-06-11
---

# 來源：A novel geometric method for determining the time constant for oxygen uptake kinetics

## 出處
- 作者：Christopher B. Cooper、Alan Garfinkel（University of California, Los Angeles）
- 篇名：*A novel geometric method for determining the time constant for oxygen uptake kinetics*
- 類型：Innovative Methodology（含 "NEW & NOTEWORTHY" 摘要框，為 *Journal of Applied Physiology* 之體例）
- 年份：2022（檔名標記 cooper-garfinkel-2022）
- 原始檔：`C:\原始資料\A novel geometric method for determining the time constant for oxygen uptake kinetics\`
- 註：抽取出的 markdown 與 meta.json 未含期刊卷期頁碼與 DOI；期刊依體例判定為 *J Appl Physiol*，卷期待補。

## 核心主張
只做**一趟**運動，把逐口攝氧換成「累積攝氧量（cumVO2）對時間」圖，τVO2 即可從圖上三段穩態直線的斜率與截距用幾何解出——免去傳統「重複六趟再疊平均」的負擔，且模擬顯示準度達 1.5–3.5 秒內。

## 本份新增／更新的概念
- [[Cumulative oxygen uptake]]（新增）：cumVO2＝VO2 對時間的積分；穩態在 cumVO2 圖上是直線、斜率＝該段 VO2；累加作為對抗逐口雜訊的平滑手段。
- [[Oxygen debt]]（新增）：off-transit 的氧虧鏡像；氧債＝δVO2×τ(off)；on-τ≈off-τ 的對稱性；與現代 EPOC 的區別。
- [[Geometric method for VO2 time constant]]（新增）：本文獻頭條方法。三步幾何（τ＝氧虧/δVO2；化為三條回歸線的斜率/截距；τ＝兩線交點離轉換時刻的水平距離）；3,600 條模擬驗證、限中等強度、需可忽略 Phase I、僅模擬未經人體驗證、系統性略低估 τ。
- [[O2 deficit]]（更新）：補上與 [[Oxygen debt]] 的對稱關係、以及 τ＝氧虧/δVO2 被幾何法用作樞紐等式（Whipp 1971）。
- [[VO2 kinetics]]（更新）：補上 τVO2 的量測方法學——傳統六趟疊平均 vs 幾何法單趟；佐證「避開 Phase I 擬合 Phase II」。
- [[Time constant]]（更新）：補上「怎麼把 τ 量出來」——曲線擬合 vs 幾何法兩條路。

## 與既有知識的關係
一致／補充。本文獻不挑戰任何既有概念，而是**補上方法學的一塊**：先前的頁說明了 τVO2 是什麼、為何重要（[[VO2 kinetics]]、[[Time constant]]、[[O2 deficit]]），本文獻補上「在雜訊與臨床限制下怎麼實際把它量準」。其數學樞紐 τ＝氧虧/δVO2 與既有 [[O2 deficit]] 頁的 O2 deficit＝ΔVO2×τ 完全一致（同一條 Whipp 1971 關係的兩種寫法）。

需留意的張力（已在概念頁標明，非與 wiki 衝突）：本法僅以**數學模擬**驗證、尚未用人體資料對照；且限定中等強度、需從升高基線出發使 Phase I 可忽略——超出此範圍（重度強度的 [[VO2 slow component|慢成分]]、真靜息起跑的明顯 Phase I）則不適用。
