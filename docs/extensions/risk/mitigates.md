---
search:
  boost: 5.0
---

# Slot: mitigates 


_Indicates the specified event or action is mitigated by this control_



<div data-search-exclude markdown="1">



URI: [risk:mitigates](https://w3id.org/lmodel/dpv/risk/mitigates)

## Inheritance

* [controls](controls.md)
    * [reduces](reduces.md)
        * [avoids](avoids.md)
            * **mitigates**








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


* mitigates




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#mitigates |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:mitigates |
| native | risk:mitigates |
| exact | dpv_risk:mitigates, dpv_risk_owl:mitigates |




## LinkML Source

<details>
```yaml
name: mitigates
definition_uri: risk:mitigates
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#mitigates
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates the specified event or action is mitigated by this control
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- mitigates
exact_mappings:
- dpv_risk:mitigates
- dpv_risk_owl:mitigates
rank: 1000
is_a: avoids
range: string
multivalued: true

```
</details></div>