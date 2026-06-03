---
search:
  boost: 5.0
---

# Slot: logs 


_Indicates the specified event or action is logged by this control_



<div data-search-exclude markdown="1">



URI: [risk:logs](https://w3id.org/lmodel/dpv/risk/logs)

## Inheritance

* [controls](controls.md)
    * [monitors](monitors.md)
        * **logs**








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


* logs




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#logs |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:logs |
| native | risk:logs |
| exact | dpv_risk:logs, dpv_risk_owl:logs |




## LinkML Source

<details>
```yaml
name: logs
definition_uri: risk:logs
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#logs
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates the specified event or action is logged by this control
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- logs
exact_mappings:
- dpv_risk:logs
- dpv_risk_owl:logs
rank: 1000
is_a: monitors
range: string
multivalued: true

```
</details></div>