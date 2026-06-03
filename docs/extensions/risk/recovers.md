---
search:
  boost: 5.0
---

# Slot: recovers 


_Indicates the specified event or action is recovered from by this_

_control_



<div data-search-exclude markdown="1">



URI: [risk:recovers](https://w3id.org/lmodel/dpv/risk/recovers)

## Inheritance

* [controls](controls.md)
    * [resolves](resolves.md)
        * **recovers**








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


* recovers




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#recovers |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:recovers |
| native | risk:recovers |
| exact | dpv_risk:recovers, dpv_risk_owl:recovers |




## LinkML Source

<details>
```yaml
name: recovers
definition_uri: risk:recovers
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#recovers
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Indicates the specified event or action is recovered from by this

  control'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- recovers
exact_mappings:
- dpv_risk:recovers
- dpv_risk_owl:recovers
rank: 1000
is_a: resolves
range: string
multivalued: true

```
</details></div>