---
search:
  boost: 5.0
---

# Slot: has_risk_assessment 


_Associates the risk assessment_



<div data-search-exclude markdown="1">



URI: [risk:has_risk_assessment](https://w3id.org/lmodel/dpv/risk/has_risk_assessment)
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


* has risk assessment




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#hasRiskAssessment |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:has_risk_assessment |
| native | risk:has_risk_assessment |
| exact | dpv_risk:hasRiskAssessment, dpv_risk_owl:hasRiskAssessment |




## LinkML Source

<details>
```yaml
name: has_risk_assessment
definition_uri: risk:hasRiskAssessment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#hasRiskAssessment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Associates the risk assessment
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- has risk assessment
exact_mappings:
- dpv_risk:hasRiskAssessment
- dpv_risk_owl:hasRiskAssessment
rank: 1000
range: string
multivalued: true

```
</details></div>