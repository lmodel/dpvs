---
search:
  boost: 5.0
---

# Slot: has_risk_acceptance 


_Associates the risk acceptance plan or process or criteria_



<div data-search-exclude markdown="1">



URI: [risk:has_risk_acceptance](https://w3id.org/lmodel/dpv/risk/has_risk_acceptance)
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


* has risk acceptance




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#hasRiskAcceptance |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:has_risk_acceptance |
| native | risk:has_risk_acceptance |
| exact | dpv_risk:hasRiskAcceptance, dpv_risk_owl:hasRiskAcceptance |




## LinkML Source

<details>
```yaml
name: has_risk_acceptance
definition_uri: risk:hasRiskAcceptance
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#hasRiskAcceptance
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Associates the risk acceptance plan or process or criteria
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- has risk acceptance
exact_mappings:
- dpv_risk:hasRiskAcceptance
- dpv_risk_owl:hasRiskAcceptance
rank: 1000
range: string
multivalued: true

```
</details></div>