---
search:
  boost: 5.0
---

# Slot: contains 


_Indicates the specified event or action is contained by this control_



<div data-search-exclude markdown="1">



URI: [risk:contains](https://w3id.org/lmodel/dpv/risk/contains)

## Inheritance

* [controls](controls.md)
    * **contains**








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


* contains




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#contains |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:contains |
| native | risk:contains |
| exact | dpv_risk:contains, dpv_risk_owl:contains |




## LinkML Source

<details>
```yaml
name: contains
definition_uri: risk:contains
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#contains
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates the specified event or action is contained by this control
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- contains
exact_mappings:
- dpv_risk:contains
- dpv_risk_owl:contains
rank: 1000
is_a: controls
range: string
multivalued: true

```
</details></div>