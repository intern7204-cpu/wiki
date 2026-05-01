---
name: feynman-euclidean-summary
description: Use this skill to generate single-source summaries, concept pages, mechanism-based explanations, and clinical reasoning notes for this wiki. Use it when one source needs to be summarized rigorously and, if necessary, split into multiple single-concept pages while preserving fact/inference boundaries.
---

# Feynman-Euclidean Summary Skill

本檔是 repo 內正式 skill 入口；上位規則以 `AGENTS.md` 為準，根目錄 `SKILL.md` 可視為同主題參考版本。

## 何時使用

- source summary
- concept page
- mechanism-based explanation
- clinical reasoning summary
- CPET / exercise physiology concept summary

## 不可違反規則

- 一次只處理一篇來源。
- 一篇來源可以拆成多個 concept pages，但每頁只能處理一個 concept。
- 不得把多篇來源混成未標示的共識。
- 重要陳述要區分 Fact / Inference / Assumption / Uncertainty。
- 結論不得超出來源可直接支持或合理推導的範圍。
- 若 `AGENTS.md` 與其他模板衝突，以 `AGENTS.md` 為準。

## 來源與輸出對應

- `1 source -> 1 source summary`
- `1 source -> 0..n concept pages`
- `1 concept page -> 1 concept only`
- `n sources -> 先各自摘要，再決定是否進入 synthesis`

## 推導順序

`Definition → Known facts → Preconditions → Mechanism chain → Observable consequence → Clinical or research implication → Limitation`

## 來源摘要最少結構

一篇來源固定產生一份來源摘要；若該來源含有多個可分離概念，再由此摘要延伸出多個概念頁。

```markdown
# Source Summary: [Title]

## Source Type

## Reliability Level

## One-Sentence Summary

## Core Concepts Extracted

### Concept: [Name]

#### One-Sentence Definition

#### Known Facts

#### Mechanism Chain

#### Inferences

#### Assumptions

#### Uncertainties / Limitations

## Clinically Useful Points

## Research-Useful Points

## Conflicts With Existing Knowledge

## Pages That Should Be Created or Updated

## Suggested Tags
```

## 概念頁最少結構

若同一篇來源要拆成多頁，每頁仍維持單一概念邊界，不得把 mechanism、assessment、intervention 等不同層級硬混在一起。

```markdown
# [Concept Name]

## One-Sentence Definition

## Definition and Boundary

## Why It Matters

## Preconditions or Conditions

## Mechanism

## Observable Patterns

## Clinical / Research Implication

## Fact

## Inference

## Assumption

## Uncertainty

## Limitations and Misreadings

## Links
```
