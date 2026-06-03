---
search:
  boost: 5.0
---

# Slot: resolves 


_Indicates the specified event or action is resolved by this control_



<div data-search-exclude markdown="1">



URI: [risk:resolves](https://w3id.org/lmodel/dpv/risk/resolves)

## Inheritance

* [controls](controls.md)
    * **resolves**
        * [recovers](recovers.md)
        * [remedies](remedies.md)
        * [reverses](reverses.md)








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


* resolves




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#resolves |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:resolves |
| native | risk:resolves |
| exact | dpv_risk:resolves, dpv_risk_owl:resolves |




## LinkML Source

<details>
```yaml
name: resolves
definition_uri: risk:resolves
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#resolves
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates the specified event or action is resolved by this control
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- resolves
exact_mappings:
- dpv_risk:resolves
- dpv_risk_owl:resolves
rank: 1000
is_a: controls
range: string
multivalued: true

```
</details></div>