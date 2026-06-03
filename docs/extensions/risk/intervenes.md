---
search:
  boost: 5.0
---

# Slot: intervenes 


_Indicates the specified event or action is intervened by this control_



<div data-search-exclude markdown="1">



URI: [risk:intervenes](https://w3id.org/lmodel/dpv/risk/intervenes)

## Inheritance

* [controls](controls.md)
    * [reduces](reduces.md)
        * **intervenes**








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


* intervenes




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#intervenes |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:intervenes |
| native | risk:intervenes |
| exact | dpv_risk:intervenes, dpv_risk_owl:intervenes |




## LinkML Source

<details>
```yaml
name: intervenes
definition_uri: risk:intervenes
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#intervenes
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates the specified event or action is intervened by this control
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- intervenes
exact_mappings:
- dpv_risk:intervenes
- dpv_risk_owl:intervenes
rank: 1000
is_a: reduces
range: string
multivalued: true

```
</details></div>