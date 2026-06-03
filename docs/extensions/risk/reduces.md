---
search:
  boost: 5.0
---

# Slot: reduces 


_Indicates the specified event or action is reduced by this control_



<div data-search-exclude markdown="1">



URI: [risk:reduces](https://w3id.org/lmodel/dpv/risk/reduces)

## Inheritance

* [controls](controls.md)
    * **reduces**
        * [avoids](avoids.md)
        * [interrupts](interrupts.md)
        * [intervenes](intervenes.md)








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


* reduces




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#reduces |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:reduces |
| native | risk:reduces |
| exact | dpv_risk:reduces, dpv_risk_owl:reduces |




## LinkML Source

<details>
```yaml
name: reduces
definition_uri: risk:reduces
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#reduces
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates the specified event or action is reduced by this control
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- reduces
exact_mappings:
- dpv_risk:reduces
- dpv_risk_owl:reduces
rank: 1000
is_a: controls
range: string
multivalued: true

```
</details></div>