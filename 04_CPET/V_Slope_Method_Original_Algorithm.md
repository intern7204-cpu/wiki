---
title: V-Slope Method Original Algorithm
created: 2026-05-09
updated: 2026-05-09
type: concept
domain: [CPET, methodology, exercise_physiology]
tags: [V_slope, gas_exchange_threshold, anaerobic_threshold, bicarbonate_buffering, respiratory_compensation_point, CPET_methodology]
sources:
  - 10_來源摘要/Beaver_Wasserman_Whipp_1986_V_slope_method.md
source_tier: 5
evidence_level: original_method_study
confidence: medium_high
contested: true
contradictions:
  - "This is the original V-slope method paper, not a guideline-level algorithm."
  - "Historical anaerobic threshold terminology should be translated into operational GET / gas-exchange AT."
  - "Respiratory compensation point is a separate higher breakpoint and should not be collapsed into GET."
---

# V-Slope Method Original Algorithm

## One-Sentence Definition

Beaver, Wasserman, and Whipp 1986 defined the original V-slope method as a two-segment regression analysis of VCO2 versus VO2 that detects the onset of excess CO2 output during incremental exercise.

## Definition and Boundary

This page describes only the original 1986 method article. It is not a full modern CPET guideline, not a disease-specific validation page, and not a claim that `anaerobic threshold` proves muscle dysoxia.

The modern wiki translation is: the method estimates [[Gas_Exchange_Threshold]] / gas-exchange AT by identifying the VCO2-VO2 breakpoint before frank respiratory compensation.

## Why It Matters

- It provides the historical algorithm behind [[V_Slope_Method]].
- It explains why VCO2-VO2 is more directly tied to bicarbonate-buffering-related excess CO2 than VE-only threshold methods.
- It forces separation between GET/AT and [[Respiratory_Compensation_Point]].

## Preconditions or Conditions

- Incremental cycle exercise in the original study.
- Breath-by-breath VO2, VCO2, VE, heart rate, and PETCO2.
- Data conditioning before regression.
- Exclusion of early CO2-store distortion after ramp onset.
- RCP identified separately and used as an upper boundary if present.

## Mechanism

1. Exercise intensity increases progressively.
2. Lactic acid production begins to exceed handling sufficiently to increase H+ load.
3. HCO3- buffers the added H+.
4. Buffering produces excess CO2.
5. VCO2 begins to increase more steeply relative to VO2.
6. A two-line regression intersection on the VCO2-VO2 plot estimates the transition.
7. At higher intensity, ventilatory compensation changes VE-VCO2 behavior; this is a separate RCP signal.

## Observable Patterns

- Below GET / AT, VCO2 rises approximately linearly with VO2.
- Above GET / AT but below RCP, VCO2 rises more steeply relative to VO2 because of excess CO2.
- Above RCP, ventilation rises disproportionately, so VCO2 interpretation is increasingly affected by ventilatory control and CO2-store dynamics.

## Original Algorithm Steps

1. Interpolate breath-by-breath data into regular time intervals.
2. Apply minimal moving average smoothing; Beaver et al. used 9 seconds.
3. Correct recognizable VCO2 fluctuations related to PETCO2 / ventilatory irregularity when needed.
4. Exclude the first minute after incremental phase onset because VCO2 kinetics lag VO2 due to CO2 stores.
5. Exclude remaining initial segments with slope below 0.6.
6. Detect RCP separately from VE versus VCO2; if present, use it as the upper boundary.
7. Fit two linear regression segments to VCO2 versus VO2.
8. Move the division point systematically to find the best two-segment fit.
9. Accept the breakpoint as AT only if the slope change exceeds 0.1.

## Clinical / Research Implication

- Clinical CPET interpretation should not identify GET by a single VCO2-VO2 plot without checking RCP, PETCO2, ventilatory equivalents, protocol, and signal quality.
- Research reports should specify preprocessing and breakpoint rules, because these assumptions alter the result.
- The original algorithm is strongest as a methodology reference, not as a universal clinical cutoff.

## Fact

- The study enrolled 10 healthy men aged 19-39 years.
- The protocol used 4 minutes of unloaded cycling followed by 15 W/min incremental exercise to tolerance.
- Mean V-slope AT was 1.83 +/- 0.30 L/min VO2.
- Mean visual panel AT was 1.85 +/- 0.34 L/min VO2.
- V-slope coefficient of variation was 0.023 +/- 0.006; panel average coefficient of variation was 0.127 +/- 0.080.
- V-slope AT did not differ significantly from estimated bicarbonate threshold.
- V-slope AT corresponded to lactate 0.50 +/- 0.34 meq/L above mathematically defined LT.
- RCP was higher than V-slope AT: 2.51 +/- 0.42 versus 1.83 +/- 0.30 L/min VO2.

## Inference

- V-slope is more robust than VE-only methods when ventilatory response lags the metabolic signal.
- V-slope is best interpreted as a gas-exchange estimate of buffering-related transition, not as a direct tissue oxygenation marker.
- RCP should be actively searched for so the lower GET/AT breakpoint is not overestimated.

## Assumption

- The selected analysis region can be approximated by two linear VCO2-VO2 segments.
- Before RCP, the slope increase is primarily caused by bicarbonate-buffering-related excess CO2.
- PETCO2 correction improves the metabolic signal rather than introducing artifact.
- A 15 W/min cycle ramp provides adequate transition resolution for the studied population.

## Uncertainty

- Generalization to treadmill tests, older adults, children, cardiopulmonary disease, and abnormal ventilatory control requires separate validation.
- The original study sampled arterial lactate / bicarbonate every 2 minutes, so exact temporal alignment remains limited.
- Modern software may implement different smoothing, regression, and breakpoint rules.

## Limitations and Misreadings

- Do not call this Tier 3 evidence under the current repo hierarchy; it is Tier 5 original research.
- Do not equate `anaerobic threshold` with muscle dysoxia.
- Do not use V-slope GET as a substitute for [[Critical_Power]] or severe-domain boundary.
- Do not collapse GET and RCP into one threshold.

## Links

- [[10_來源摘要/Beaver_Wasserman_Whipp_1986_V_slope_method]]
- [[V_Slope_Method]]
- [[Gas_Exchange_Threshold]]
- [[Respiratory_Compensation_Point]]
- [[Anaerobic_Threshold_概念史]]
