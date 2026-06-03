---
search:
  boost: 5.0
---

# Slot: interrupts 


_Indicates the specified event or action is interrupted by this control_



<div data-search-exclude markdown="1">



URI: [risk:interrupts](https://w3id.org/lmodel/dpv/risk/interrupts)

## Inheritance

* [controls](controls.md)
    * [reduces](reduces.md)
        * **interrupts**








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


* interrupts




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#interrupts |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:interrupts |
| native | risk:interrupts |
| exact | dpv_risk:interrupts, dpv_risk_owl:interrupts |




## LinkML Source

<details>
```yaml
name: interrupts
definition_uri: risk:interrupts
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#interrupts
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates the specified event or action is interrupted by this control
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- interrupts
exact_mappings:
- dpv_risk:interrupts
- dpv_risk_owl:interrupts
rank: 1000
is_a: reduces
range: string
multivalued: true

```
</details></div>