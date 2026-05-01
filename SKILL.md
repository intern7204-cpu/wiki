---
name: feynman-euclidean-summary
description: Use this skill to generate source summaries, concept pages, literature extraction notes, medical knowledge-base pages, mechanism-based explanations, clinical reasoning summaries, and CPET/exercise physiology concept summaries using Feynman teaching rules and Euclidean stepwise derivation. Use it for rigorous single-source extraction, including cases where one source should be split into multiple single-concept pages. This skill inherits the repo-level Accuracy-First Policy from AGENTS.md.
---

# Feynman-Euclidean Summary Skill

Use this skill when the user asks to generate, revise, or standardize any of the following outputs:

- source summary
- concept page
- literature extraction note
- medical knowledge-base page
- single-concept explanation
- mechanism-based explanation
- clinical reasoning summary
- CPET / exercise physiology concept summary

This skill should not be used for casual Q&A unless the user explicitly asks for structured extraction, summary generation, wiki-page generation, or concept clarification.

---

## 0. Repository-Level Policy Inheritance

This skill inherits the repo-level **Accuracy-First Policy** from `AGENTS.md`.

Do not duplicate the full policy here. When using this skill:

- check the premise before summarizing or generating concept pages;
- separate fact, inference, assumption, and uncertainty;
- do not fill unsupported gaps;
- prioritize guideline, textbook, and systematic review evidence for medical content;
- if this skill conflicts with `AGENTS.md`, follow `AGENTS.md`.

## 1. Core Objective

Generate summaries and concept pages using two combined methods:

1. Feynman teaching rule: make each concept explainable in simple, precise language without losing technical accuracy.
2. Euclidean derivation rule: every conclusion must follow from explicit definitions, known facts, assumptions, and stepwise reasoning.

The output must avoid impressionistic summaries. It must produce traceable, concept-separated, mechanism-based notes.

---

## 2. Non-Negotiable Rules

### 2.1 One concept at a time

Each output section should focus on one concept only.

One source may produce multiple concept pages if the concepts are meaningfully separable.
Do not force unrelated concepts into one page merely because they come from the same source.

Do not mix:

- disease entity
- mechanism
- clinical manifestation
- assessment tool
- intervention
- prognosis
- research method

unless their relationship is explicitly derived.

### 2.2 Do not batch-blend sources

When summarizing a source, extract from one source at a time.

Keep the mapping explicit:

- `1 source -> 1 source summary`
- `1 source -> 0..n concept pages`
- `1 concept page -> 1 concept only`

Do not merge multiple papers, chapters, or reviews into a single undifferentiated summary unless the user explicitly asks for synthesis.

If synthesis is requested, first summarize each source separately, then synthesize.

### 2.3 Separate fact, inference, assumption, and uncertainty

Every important claim must be classified as one of:

- Fact: directly supported by the source.
- Inference: reasonably derived from source-supported facts.
- Assumption: required for the reasoning but not proven in the source.
- Uncertainty: insufficient, conflicting, or unresolved evidence.

Do not present inference as fact.

### 2.4 No unsupported clinical authority

For medical content, do not fabricate guidelines, citations, mechanisms, or consensus statements.

If the source does not support a claim, mark it as inference or uncertainty.

---

## 3. Required Output Logic

Use the following derivation order:

```text
Definition → Known facts → Preconditions → Mechanism chain → Observable consequence → Clinical / research implication → Limitation
```

Each reasoning chain should look like:

```text
A is defined as ...
A occurs under condition B.
B changes mechanism C.
C produces observable phenomenon D.
Therefore, D can be interpreted as E only if condition F is met.
```

Avoid unsupported jumps such as:

```text
A happens, therefore E is true.
```

---

## 4. Source Summary Template

Use this template when generating a source summary.

```markdown
# Source Summary: [Title]

## Source Type
- Guideline / textbook chapter / systematic review / narrative review / original article / website / other

## Reliability Level
- High / moderate / low / uncertain
- Reason:

## One-Sentence Summary
[State the central message in one precise sentence.]

## Core Concepts Extracted

### Concept 1: [Concept name]

#### One-Sentence Definition
[Define the concept simply and precisely.]

#### Known Facts
- Fact 1:
- Fact 2:

#### Mechanism Chain
```text
A → B → C → D
```

#### Inferences
- Inference 1:

#### Assumptions
- Assumption 1:

#### Uncertainties / Limitations
- Limitation 1:

---

### Concept 2: [Concept name]

[Repeat the same structure.]

## Clinically Useful Points
- Point 1:
- Point 2:

## Research-Useful Points
- Point 1:
- Point 2:

## Conflicts With Existing Knowledge
- None identified / specify conflict.

## Pages That Should Be Created or Updated
- [[Concept page name]]

## Suggested Tags
- #tag1
- #tag2
```

---

## 5. Concept Page Template

Use this template when generating a wiki concept page.

```markdown
# [Concept Name]

## One-Sentence Definition
[Define the concept in one precise sentence.]

## Definition and Boundary

### What It Is
- 

### What It Is Not
- 

### Commonly Confused Concepts
- 

## Known Facts
- Fact 1:
- Fact 2:

## Core Mechanism

```text
A → B → C → D
```

## Stepwise Derivation

### Step 1: Definition
- 

### Step 2: Preconditions
- 

### Step 3: Mechanism
- 

### Step 4: Observable Consequence
- 

### Step 5: Interpretation
- 

## Clinical Application

### Applicable Situation
- 

### Not Applicable Situation
- 

### Red Flags
- 

### Decision Points
- 

## Research Application
- 

## Limitations and Open Questions
- Evidence limitation:
- Population limitation:
- Methodological limitation:
- Unresolved question:

## Source and Version Note
- Main source:
- Evidence level:
- Last updated:
```

---

## 6. CPET / Exercise Physiology Add-On

When the topic involves CPET, exercise physiology, VO2 kinetics, VCO2 kinetics, critical power, W′, W′ recovery, PCr recovery, lactate, metabolic acidosis, or ventilatory thresholds, add these sections:

```markdown
## Operational Definition

## Physiological Mechanism

## Observable Variables

## Mathematical / Statistical Model

## Confounders

## Model Assumptions

## Methodological Limitations

## Clinical or Research Use
```

Reasoning must explicitly follow:

```text
observed variable → physiological interpretation → model assumption → limitation
```

Example:

```text
VO2 off-kinetics τ is an observed recovery parameter.
It may reflect oxidative recovery dynamics and PCr resynthesis kinetics.
This interpretation assumes adequate model fit, stable transition definition, and absence of major cardiopulmonary confounding.
Therefore, τ_VO2 can be used as an indirect recovery marker, but not as a direct PCr measurement.
```

---

## 7. Quality Checklist

Before finalizing the output, verify:

```text
1. Is each section centered on one concept?
2. Is the one-sentence definition clear?
3. Are facts separated from inferences?
4. Are assumptions explicit?
5. Are uncertainties and limitations stated?
6. Is the mechanism written as a stepwise chain?
7. Are clinical implications supported by the source?
8. Are population and method limits stated?
9. Are there unsupported jumps in reasoning?
10. Are pages or concepts suggested for wiki update?
```

If any item fails, revise before output.

---

## 8. Output Style

- Use Traditional Chinese for general explanation.
- Preserve medical and scientific terms in American English.
- Be concise but not vague.
- Prefer structured Markdown.
- Avoid decorative prose.
- Do not over-summarize mechanisms.
- Do not add new topics unless necessary for the requested output.

---

## 9. Minimal Output Mode

If the user asks for a short version, use:

```markdown
# [Concept / Source Title]

## 一句話摘要

## 核心概念

## 推導鏈
```text
A → B → C → D
```

## 事實 / 推論 / 假設 / 不確定

## 臨床或研究意義

## 限制
```
