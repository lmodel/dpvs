---
search:
  boost: 5.0
---

# Slot: reverses 


_Indicates the specified event or action is reversed by this control_



<div data-search-exclude markdown="1">



URI: [risk:reverses](https://w3id.org/lmodel/dpv/risk/reverses)

## Inheritance

* [controls](controls.md)
    * [resolves](resolves.md)
        * **reverses**








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


* reverses




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#reverses |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:reverses |
| native | risk:reverses |
| exact | dpv_risk:reverses, dpv_risk_owl:reverses |




## LinkML Source

<details>
```yaml
name: reverses
definition_uri: risk:reverses
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#reverses
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates the specified event or action is reversed by this control
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- reverses
exact_mappings:
- dpv_risk:reverses
- dpv_risk_owl:reverses
rank: 1000
is_a: resolves
range: string
multivalued: true

```
</details></div>