---
search:
  boost: 5.0
---

# Slot: remedies 


_Indicates the specified event or action is remedied by this control_



<div data-search-exclude markdown="1">



URI: [risk:remedies](https://w3id.org/lmodel/dpv/risk/remedies)

## Inheritance

* [controls](controls.md)
    * [resolves](resolves.md)
        * **remedies**








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


* remedies




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#remedies |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:remedies |
| native | risk:remedies |
| exact | dpv_risk:remedies, dpv_risk_owl:remedies |




## LinkML Source

<details>
```yaml
name: remedies
definition_uri: risk:remedies
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#remedies
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates the specified event or action is remedied by this control
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- remedies
exact_mappings:
- dpv_risk:remedies
- dpv_risk_owl:remedies
rank: 1000
is_a: resolves
range: string
multivalued: true

```
</details></div>