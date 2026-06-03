---
search:
  boost: 5.0
---

# Slot: has_risk_identification 


_Associates the risk identification plan or process or criteria_



<div data-search-exclude markdown="1">



URI: [risk:has_risk_identification](https://w3id.org/lmodel/dpv/risk/has_risk_identification)
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


* has risk identification




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#hasRiskIdentification |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:has_risk_identification |
| native | risk:has_risk_identification |
| exact | dpv_risk:hasRiskIdentification, dpv_risk_owl:hasRiskIdentification |




## LinkML Source

<details>
```yaml
name: has_risk_identification
definition_uri: risk:hasRiskIdentification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#hasRiskIdentification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Associates the risk identification plan or process or criteria
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- has risk identification
exact_mappings:
- dpv_risk:hasRiskIdentification
- dpv_risk_owl:hasRiskIdentification
rank: 1000
range: string
multivalued: true

```
</details></div>