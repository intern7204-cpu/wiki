---
title: Incremental Exercise VCO2 Partitioning Model
created: 2026-05-09
updated: 2026-05-09
type: concept
domain: [CPET, exercise_physiology, methodology]
tags: [VCO2, CO2_transport, gas_exchange_threshold, PaCO2, PvCO2, lactate, bicarbonate_buffering]
sources:
  - 10_來源摘要/Physiological_model_of_CO2_output_during_incremental_exercise.md
source_tier: 5
evidence_level: original_physiology_model_study
confidence: medium
contested: true
contradictions:
  - "This is a historical mechanistic model, not a clinical GET algorithm."
  - "VCO2 partitioning does not make excess VCO2 a direct lactate meter."
  - "The source studied a small trained-athlete sample and used estimated PaCO2."
---

# Incremental Exercise VCO2 Partitioning Model

## One-Sentence Definition

Incremental exercise VCO2 partitioning is Yano 1997's historical model that separates VCO2 into non-lactic and excess components to explain how CO2 transport, lactate-related buffering, and PaCO2 reduction shape high-intensity gas exchange.

## Definition and Boundary

This page describes one model from one source: Yano 1997.

It is not the original [[V_Slope_Method_Original_Algorithm]], not a modern automated breakpoint method, not [[Respiratory_Compensation_Point]], and not a replacement for [[Gas_Exchange_Threshold]] pattern recognition.

## Why It Matters

- It helps explain why VCO2 is not a single-source signal during incremental exercise.
- It connects [[V_Slope_Method]] teaching to CO2 transport and acid-base physiology.
- It prevents the overinterpretation that excess VCO2 directly equals lactate production.

## Preconditions or Conditions

- Incremental cycle exercise.
- A detectable lower VCO2-work-rate relation that can be extrapolated.
- Measures or estimates of VCO2, PvCO2, PaCO2 / PETCO2, ventilation, and blood lactate.
- Interpretation as a physiology model, not as a clinical decision rule.

## Mechanism

1. Exercise intensity rises progressively.
2. Tissue CO2 production and venous CO2 pressure increase.
3. Non-lactic VCO2 is modeled as related to the PvCO2-to-base-PaCO2 transport gradient.
4. With higher intensity, lactate-related acid load shifts CO2 handling through the blood CO2 dissociation curve.
5. Bicarbonate buffering adds CO2 to the system.
6. Hyperventilation can reduce PaCO2.
7. Lower PaCO2 increases CO2 unloading from tissue to lung.
8. Measured VCO2 becomes the sum of metabolic CO2, CO2 transport / storage effects, buffering-related CO2, and ventilatory unloading.

## Observable Patterns

- Non-lactic VCO2 correlated strongly with mixed venous CO2 pressure in the source.
- PaCO2 stayed approximately stable through lower submaximal work but fell at exhaustion.
- CO2 excess correlated with blood lactate increase.
- Excess VCO2 was not present in every subject at the 1080 kpm/min stage, showing that the pattern was not uniform across the small sample.

## Clinical / Research Implication

- In CPET teaching, this model is best used as a historical mechanistic supplement for [[Gas_Exchange_Threshold]] and [[V_Slope_Method]].
- In research, it supports separating the language of VCO2 breakpoint, lactate rise, bicarbonate buffering, PaCO2 decline, and RCP.
- In clinical CPET, do not use this model alone to label GET, RCP, prognosis, or exercise prescription zones.

## Fact

- Yano 1997 studied 8 trained university athletes.
- The protocol used incremental Monark cycle ergometry.
- Expired gas was collected with Douglas bags at rest and every minute during exercise.
- Mixed venous CO2 pressure was estimated with CO2 rebreathing.
- PaCO2 was estimated from PETCO2 and tidal volume, not directly sampled.
- Blood lactate was sampled at rest, after exercise to 1080 kpm/min, and at exhaustion.
- Non-lactic VCO2 correlated with PvCO2: r = 0.950.
- VCO2 showed a multiple correlation with PaCO2 and PvCO2: r = 0.971.
- CO2 excess correlated with blood lactate increase: r = 0.828.

## Inference

- The source supports a multi-factor interpretation of VCO2 during high-intensity exercise.
- The model is compatible with bicarbonate-buffering physiology, but it is less directly tied to GET detection than Beaver 1986 or Stringer 1995.
- The clinical value is mainly conceptual: it cautions against treating VCO2 as pure lactate output or pure ventilation.

## Assumption

- A pre-transition VCO2 line can estimate non-lactic VCO2.
- A base PaCO2 can separate non-lactic and excess VCO2 components conceptually.
- Estimated PaCO2 and rebreathing-derived PvCO2 are adequate for building the model.
- Venous lactate change can represent the relevant acid-base load.

## Uncertainty

- Exact demographic reporting is partly limited by OCR ambiguity in the raw Markdown.
- Disease populations were not studied.
- The model was not compared against modern automated GET algorithms.
- The source cannot determine how much of a patient's VCO2 rise comes from buffering versus CO2 stores, hyperventilation, dead space, anxiety, or cardiopulmonary disease.

## Limitations and Misreadings

- Do not treat this as a universal V-slope implementation.
- Do not equate excess VCO2 with direct lactate production.
- Do not treat historical AT language as proof of muscle dysoxia.
- Do not apply the healthy-athlete model directly to HF, COPD, PH, anemia, neuromuscular disease, or pediatric CPET without disease-specific sources.

## Links

- [[10_來源摘要/Physiological_model_of_CO2_output_during_incremental_exercise]]
- [[V_Slope_Method]]
- [[Gas_Exchange_Threshold]]
- [[Heavy_Constant_Work_VCO2_VO2_Inflection]]
- [[V_Slope_Method_Original_Algorithm]]
- [[Anaerobic_Threshold_概念史]]
