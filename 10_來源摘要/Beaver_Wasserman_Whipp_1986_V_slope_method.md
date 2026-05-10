---
title: "Beaver Wasserman Whipp 1986 - A new method for detecting anaerobic threshold by gas exchange"
created: 2026-04-23
updated: 2026-05-09
type: source_summary
domain: [CPET, methodology, exercise_physiology]
tags: [V_slope, gas_exchange_threshold, anaerobic_threshold, bicarbonate_threshold, respiratory_compensation_point, original_article]
source_tier: 5
evidence_level: original_method_study
confidence: medium_high
contested: true
contradictions:
  - "This source introduced the V-slope method but is an original study, not a guideline or review."
  - "The paper uses historical anaerobic threshold language; this wiki preserves the operational gas-exchange method without treating it as proof of muscle dysoxia."
  - "V-slope AT and respiratory compensation point must be detected separately."
---

# Source Summary: Beaver Wasserman Whipp 1986 - A New Method for Detecting Anaerobic Threshold by Gas Exchange

## Source Type

- **Citation**: Beaver WL, Wasserman K, Whipp BJ. *A new method for detecting anaerobic threshold by gas exchange*. Journal of Applied Physiology. 1986;60(6):2020-2027.
- **Source type**: original method / physiology study.
- **Raw source**: `C:\原始資料\beaver-et-al-1986-a-new-method-for-detecting-anaerobic-threshold-by-gas-exchange\beaver-et-al-1986-a-new-method-for-detecting-anaerobic-threshold-by-gas-exchange.md`
- **Question**: can the onset of excess CO2 output from bicarbonate buffering be detected noninvasively by analyzing the VCO2-VO2 relationship during incremental exercise?

## Reliability Level

- **Tier**: 5.
- **Rationale**: original human method study with arterial lactate / bicarbonate comparison; foundational but small, healthy-male sample and historical terminology.
- **Use**: primary source for the original V-slope algorithm and the separation of AT/GET from respiratory compensation point.
- **Limit**: not a guideline, not a modern systematic review, and not direct proof that `anaerobic threshold` equals muscle dysoxia.

## One-Sentence Summary

Beaver, Wasserman, and Whipp introduced the V-slope method: a two-segment regression analysis of VCO2 versus VO2 during incremental CPET that estimates the onset of excess CO2 output from bicarbonate buffering, produces a more consistent AT/GET estimate than visual ventilatory criteria in their small sample, and separates this lower breakpoint from the higher respiratory compensation point.

## Core Concepts Extracted

### Concept: Original V-slope algorithm

#### One-Sentence Definition

The original V-slope method detects gas-exchange AT/GET by finding the breakpoint where VCO2 begins to rise more steeply relative to VO2 during incremental exercise.

#### Known Facts

- The study included 10 healthy male volunteers, aged 19-39 years.
- Protocol used cycle ergometry.
- Each subject performed 4 minutes of unloaded exercise, then incremental exercise to tolerance at 15 W/min.
- Breath-by-breath VO2, VCO2, VE, heart rate, and PETCO2 were measured.
- Arterial blood was sampled at rest, during unloaded cycling, and every 2 minutes during incremental exercise.
- Arterial samples were analyzed for lactate and bicarbonate.
- Breath-by-breath data were interpolated into regular time intervals.
- A 9-second moving average filter was used in the reported studies.
- The authors recommended minimal filtering because excessive filtering can distort curve shape.
- The method analyzes VCO2 as a function of VO2, using VO2 as the independent variable because it indexes metabolic rate.
- The first minute after the start of incremental exercise was usually excluded because CO2 storage makes VCO2 rise more slowly than VO2.
- Additional initial curve segments with slope below 0.6 were also excluded.
- VCO2 fluctuations related to ventilatory / PETCO2 fluctuation could be corrected using a physiological correction term.
- The VCO2-VO2 curve was divided into two linear regions.
- The intersection of the two regression lines was the tentative AT point.
- A solution was accepted as AT only if the lower-to-upper segment slope change was greater than 0.1.
- The respiratory compensation point was detected separately from the VE-VCO2 relationship.
- If respiratory compensation point was found, it was used as the upper boundary for AT calculation.
- Mean V-slope AT was 1.83 +/- 0.30 L/min VO2.
- Mean panel visual AT was 1.85 +/- 0.34 L/min VO2; the difference was not significant.
- V-slope coefficient of variation was 0.023 +/- 0.006.
- Panel average coefficient of variation was 0.127 +/- 0.080.
- All 6 panelists could identify AT in only 5 of 10 subjects; V-slope analysis yielded AT values for all 10 subjects.
- Mean V-slope AT was not significantly different from estimated bicarbonate threshold: 1.83 +/- 0.30 versus 1.78 +/- 0.24 L/min VO2.
- At V-slope AT, lactate averaged 0.50 +/- 0.34 meq/L above the mathematically defined lactate threshold.
- Respiratory compensation point was higher than V-slope AT: 2.51 +/- 0.42 versus 1.83 +/- 0.30 L/min VO2.
- Mean VO2max was 3.35 +/- 0.31 L/min.

#### Mechanism Chain

1. Incremental work rate increases metabolic demand.
2. Beyond the lactate-related transition, H+ load increases.
3. Bicarbonate buffers H+ from lactic acid.
4. This buffering produces excess CO2.
5. VCO2 rises more steeply relative to VO2.
6. The VCO2-VO2 slope breakpoint estimates the gas-exchange AT/GET.
7. At higher intensity, respiratory compensation causes VE to rise disproportionately to VCO2, so RCP must be detected separately.

#### Inferences

- The V-slope method is closer to the excess-CO2 mechanism than methods based mainly on VE or ventilatory equivalents.
- V-slope can be useful when ventilatory response lags or is insensitive, because the method does not depend primarily on respiratory chemosensitivity.
- In modern language, the method is best treated as operational GET detection, not as proof of a discrete muscle anaerobiosis point.

#### Assumptions

- The selected VCO2-VO2 range can be approximated by two linear segments.
- The slope change before RCP is mainly driven by bicarbonate-buffering-related excess CO2.
- PETCO2-related fluctuation correction improves signal fidelity without moving the true metabolic breakpoint.
- The 15 W/min cycle ramp in healthy men is an adequate method-development setting.

#### Uncertainties / Limitations

- Sample size was small and limited to healthy men.
- The study used cycle ergometry only.
- Arterial lactate and bicarbonate were sampled every 2 minutes, which limits fine temporal validation.
- Algorithm choices such as smoothing width, first-minute exclusion, slope-change threshold, PETCO2 correction, and RCP boundary can alter the breakpoint.
- The paper does not establish disease-specific clinical cutoffs or treatment thresholds.

### Concept: Respiratory compensation as upper boundary

#### One-Sentence Definition

The original V-slope workflow treats respiratory compensation point as a separate higher breakpoint that should cap the AT/GET calculation window.

#### Known Facts

- RCP was detected using the VE-VCO2 plot rather than the VCO2-VO2 plot.
- RCP was accepted when the VE-VCO2 slope change exceeded 15% of the initial slope.
- RCP was consistently higher than V-slope AT in this study.
- The authors noted that some subjects, especially patients with obstructive lung disease, may not have a clear RCP.

#### Inferences

- Collapsing AT/GET and RCP into one threshold risks overestimating the lower transition.
- VE-VO2 multisegment methods may detect RCP and mislabel it as AT when the lower ventilatory slope change is small or noisy.

#### Uncertainties / Limitations

- This source does not define RCP as a critical power surrogate.
- It does not resolve how to handle absent or ambiguous RCP in modern disease cohorts.

## Clinically Useful Points

- V-slope GET should be interpreted with RCP explicitly separated.
- A CPET report using `anaerobic threshold` should be translated as operational GET / gas-exchange AT unless additional evidence supports a different mechanism.
- V-slope is a method for locating a physiological transition; it is not a standalone treatment decision rule.

## Research-Useful Points

- The original algorithm makes preprocessing choices visible: interpolation, minimal moving average, CO2-store exclusion, PETCO2 correction, two-segment regression, and RCP boundary.
- Method papers and software should state these assumptions instead of treating breakpoint detection as neutral visual inspection.
- Modern validation should test whether these assumptions hold in treadmill protocols, children, older adults, cardiopulmonary disease, and abnormal ventilatory control.

## Conflicts With Existing Knowledge

- Conflicts with treating VE-only threshold detection as equivalent to V-slope detection.
- Conflicts with labeling RCP as AT/GET.
- Conflicts with reading historical `anaerobic threshold` terminology as proof of muscle dysoxia.
- Conflicts with classifying this original article as Tier 3 evidence under the current repo evidence hierarchy.

## Pages That Should Be Created or Updated

- Created: [[../04_CPET/V_Slope_Method_Original_Algorithm]]
- Updated: [[../04_CPET/V_Slope_Method]]
- Updated: [[../04_CPET/Gas_Exchange_Threshold]]
- Related: [[../04_CPET/Respiratory_Compensation_Point]]
- Related: [[../04_CPET/Anaerobic_Threshold_概念史]]

## Suggested Tags

- `V_slope`
- `gas_exchange_threshold`
- `anaerobic_threshold`
- `bicarbonate_buffering`
- `respiratory_compensation_point`
- `CPET_methodology`

## Links

- [[../04_CPET/V_Slope_Method_Original_Algorithm]]
- [[../04_CPET/V_Slope_Method]]
- [[../04_CPET/Gas_Exchange_Threshold]]
- [[../04_CPET/Respiratory_Compensation_Point]]
- [[../04_CPET/Anaerobic_Threshold_概念史]]
