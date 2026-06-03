---
search:
  boost: 5.0
---

# Slot: detects 


_Indicates the specified event or action is detected by this control_



<div data-search-exclude markdown="1">



URI: [risk:detects](https://w3id.org/lmodel/dpv/risk/detects)

## Inheritance

* [controls](controls.md)
    * [monitors](monitors.md)
        * **detects**








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


* detects




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#detects |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:detects |
| native | risk:detects |
| exact | dpv_risk:detects, dpv_risk_owl:detects |




## LinkML Source

<details>
```yaml
name: detects
definition_uri: risk:detects
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#detects
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates the specified event or action is detected by this control
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- detects
exact_mappings:
- dpv_risk:detects
- dpv_risk_owl:detects
rank: 1000
is_a: monitors
range: string
multivalued: true

```
</details></div>