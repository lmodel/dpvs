---
search:
  boost: 5.0
---

# Slot: investigates 


_Indicates the specified event or action is investigated by this control_



<div data-search-exclude markdown="1">



URI: [risk:investigates](https://w3id.org/lmodel/dpv/risk/investigates)

## Inheritance

* [controls](controls.md)
    * **investigates**








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


* investigates




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#investigates |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:investigates |
| native | risk:investigates |
| exact | dpv_risk:investigates, dpv_risk_owl:investigates |




## LinkML Source

<details>
```yaml
name: investigates
definition_uri: risk:investigates
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#investigates
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates the specified event or action is investigated by this control
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- investigates
exact_mappings:
- dpv_risk:investigates
- dpv_risk_owl:investigates
rank: 1000
is_a: controls
range: string
multivalued: true

```
</details></div>