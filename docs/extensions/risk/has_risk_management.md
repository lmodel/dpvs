---
search:
  boost: 5.0
---

# Slot: has_risk_management 


_Associates the risk management plan or process_



<div data-search-exclude markdown="1">



URI: [risk:has_risk_management](https://w3id.org/lmodel/dpv/risk/has_risk_management)
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


* has risk management




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#hasRiskManagement |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:has_risk_management |
| native | risk:has_risk_management |
| exact | dpv_risk:hasRiskManagement, dpv_risk_owl:hasRiskManagement |




## LinkML Source

<details>
```yaml
name: has_risk_management
definition_uri: risk:hasRiskManagement
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#hasRiskManagement
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Associates the risk management plan or process
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- has risk management
exact_mappings:
- dpv_risk:hasRiskManagement
- dpv_risk_owl:hasRiskManagement
rank: 1000
range: string
multivalued: true

```
</details></div>