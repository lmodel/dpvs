---
search:
  boost: 5.0
---

# Slot: has_risk_owner 


_Indicates the risk owner_



<div data-search-exclude markdown="1">



URI: [risk:has_risk_owner](https://w3id.org/lmodel/dpv/risk/has_risk_owner)
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


* has risk owner




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#hasRiskOwner |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:has_risk_owner |
| native | risk:has_risk_owner |
| exact | dpv_risk:hasRiskOwner, dpv_risk_owl:hasRiskOwner |




## LinkML Source

<details>
```yaml
name: has_risk_owner
definition_uri: risk:hasRiskOwner
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#hasRiskOwner
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates the risk owner
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- has risk owner
exact_mappings:
- dpv_risk:hasRiskOwner
- dpv_risk_owl:hasRiskOwner
rank: 1000
range: string
multivalued: true

```
</details></div>