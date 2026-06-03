---
search:
  boost: 5.0
---

# Slot: identifies 


_Indicates the specified event or action is identified by this control_



<div data-search-exclude markdown="1">



URI: [risk:identifies](https://w3id.org/lmodel/dpv/risk/identifies)

## Inheritance

* [controls](controls.md)
    * [monitors](monitors.md)
        * **identifies**








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


* identifies




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#identifies |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:identifies |
| native | risk:identifies |
| exact | dpv_risk:identifies, dpv_risk_owl:identifies |




## LinkML Source

<details>
```yaml
name: identifies
definition_uri: risk:identifies
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#identifies
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates the specified event or action is identified by this control
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- identifies
exact_mappings:
- dpv_risk:identifies
- dpv_risk_owl:identifies
rank: 1000
is_a: monitors
range: string
multivalued: true

```
</details></div>