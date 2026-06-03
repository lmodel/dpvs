---
search:
  boost: 5.0
---

# Slot: eliminates 


_Indicates the specified event or action is eliminated by this control_



<div data-search-exclude markdown="1">



URI: [risk:eliminates](https://w3id.org/lmodel/dpv/risk/eliminates)

## Inheritance

* [controls](controls.md)
    * [reduces](reduces.md)
        * [avoids](avoids.md)
            * **eliminates**








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


* eliminates




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#eliminates |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:eliminates |
| native | risk:eliminates |
| exact | dpv_risk:eliminates, dpv_risk_owl:eliminates |




## LinkML Source

<details>
```yaml
name: eliminates
definition_uri: risk:eliminates
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#eliminates
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates the specified event or action is eliminated by this control
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- eliminates
exact_mappings:
- dpv_risk:eliminates
- dpv_risk_owl:eliminates
rank: 1000
is_a: avoids
range: string
multivalued: true

```
</details></div>