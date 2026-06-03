---
search:
  boost: 5.0
---

# Slot: overrides 


_Indicates the specified event or action is overridden by this control_



<div data-search-exclude markdown="1">



URI: [risk:overrides](https://w3id.org/lmodel/dpv/risk/overrides)

## Inheritance

* [controls](controls.md)
    * **overrides**








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


* overrides




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#overrides |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:overrides |
| native | risk:overrides |
| exact | dpv_risk:overrides, dpv_risk_owl:overrides |




## LinkML Source

<details>
```yaml
name: overrides
definition_uri: risk:overrides
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#overrides
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates the specified event or action is overridden by this control
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- overrides
exact_mappings:
- dpv_risk:overrides
- dpv_risk_owl:overrides
rank: 1000
is_a: controls
range: string
multivalued: true

```
</details></div>