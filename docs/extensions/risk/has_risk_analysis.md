---
search:
  boost: 5.0
---

# Slot: has_risk_analysis 


_Associates the risk analysis_



<div data-search-exclude markdown="1">



URI: [risk:has_risk_analysis](https://w3id.org/lmodel/dpv/risk/has_risk_analysis)
<!-- no inheritance hierarchy -->







## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |






## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* has risk analysis




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#hasRiskAnalysis |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:has_risk_analysis |
| native | risk:has_risk_analysis |
| exact | dpv_risk:hasRiskAnalysis, dpv_risk_owl:hasRiskAnalysis |




## LinkML Source

<details>
```yaml
name: has_risk_analysis
definition_uri: risk:hasRiskAnalysis
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#hasRiskAnalysis
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Associates the risk analysis
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- has risk analysis
exact_mappings:
- dpv_risk:hasRiskAnalysis
- dpv_risk_owl:hasRiskAnalysis
rank: 1000
range: string
multivalued: true

```
</details></div>