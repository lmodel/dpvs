---
search:
  boost: 5.0
---

# Slot: has_control 


_Indicates the use of specified control_



<div data-search-exclude markdown="1">



URI: [risk:has_control](https://w3id.org/lmodel/dpv/risk/has_control)
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


* has control




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#hasControl |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:has_control |
| native | risk:has_control |
| exact | dpv_risk:hasControl, dpv_risk_owl:hasControl |




## LinkML Source

<details>
```yaml
name: has_control
definition_uri: risk:hasControl
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#hasControl
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates the use of specified control
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- has control
exact_mappings:
- dpv_risk:hasControl
- dpv_risk_owl:hasControl
rank: 1000
range: string
multivalued: true

```
</details></div>