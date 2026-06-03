---
search:
  boost: 5.0
---

# Slot: modifies 


_Indicates the specified event or action is modified by this control_



<div data-search-exclude markdown="1">



URI: [risk:modifies](https://w3id.org/lmodel/dpv/risk/modifies)

## Inheritance

* [controls](controls.md)
    * [reduces](reduces.md)
        * [avoids](avoids.md)
            * **modifies**








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


* modifies




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#modifies |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:modifies |
| native | risk:modifies |
| exact | dpv_risk:modifies, dpv_risk_owl:modifies |




## LinkML Source

<details>
```yaml
name: modifies
definition_uri: risk:modifies
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#modifies
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates the specified event or action is modified by this control
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- modifies
exact_mappings:
- dpv_risk:modifies
- dpv_risk_owl:modifies
rank: 1000
is_a: avoids
range: string
multivalued: true

```
</details></div>