---
search:
  boost: 5.0
---

# Slot: monitors 


_Indicates the specified event or action is monitored by this control_



<div data-search-exclude markdown="1">



URI: [risk:monitors](https://w3id.org/lmodel/dpv/risk/monitors)

## Inheritance

* [controls](controls.md)
    * **monitors**
        * [detects](detects.md)
        * [identifies](identifies.md)
        * [logs](logs.md)








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


* monitors




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#monitors |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:monitors |
| native | risk:monitors |
| exact | dpv_risk:monitors, dpv_risk_owl:monitors |




## LinkML Source

<details>
```yaml
name: monitors
definition_uri: risk:monitors
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#monitors
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates the specified event or action is monitored by this control
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- monitors
exact_mappings:
- dpv_risk:monitors
- dpv_risk_owl:monitors
rank: 1000
is_a: controls
range: string
multivalued: true

```
</details></div>