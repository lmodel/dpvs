---
search:
  boost: 5.0
---

# Slot: substitutes 


_Indicates the specified event or action is substituted by this control_



<div data-search-exclude markdown="1">



URI: [risk:substitutes](https://w3id.org/lmodel/dpv/risk/substitutes)

## Inheritance

* [controls](controls.md)
    * [reduces](reduces.md)
        * [avoids](avoids.md)
            * **substitutes**








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


* substitutes




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#substitutes |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:substitutes |
| native | risk:substitutes |
| exact | dpv_risk:substitutes, dpv_risk_owl:substitutes |




## LinkML Source

<details>
```yaml
name: substitutes
definition_uri: risk:substitutes
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#substitutes
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates the specified event or action is substituted by this control
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- substitutes
exact_mappings:
- dpv_risk:substitutes
- dpv_risk_owl:substitutes
rank: 1000
is_a: avoids
range: string
multivalued: true

```
</details></div>