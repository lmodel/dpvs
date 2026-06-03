---
search:
  boost: 5.0
---

# Slot: avoids 


_Indicates the event or action is avoided by the specified control_



<div data-search-exclude markdown="1">



URI: [risk:avoids](https://w3id.org/lmodel/dpv/risk/avoids)

## Inheritance

* [controls](controls.md)
    * [reduces](reduces.md)
        * **avoids**
            * [eliminates](eliminates.md)
            * [mitigates](mitigates.md)
            * [modifies](modifies.md)
            * [substitutes](substitutes.md)








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


* avoids




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#avoids |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:avoids |
| native | risk:avoids |
| exact | dpv_risk:avoids, dpv_risk_owl:avoids |




## LinkML Source

<details>
```yaml
name: avoids
definition_uri: risk:avoids
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#avoids
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates the event or action is avoided by the specified control
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- avoids
exact_mappings:
- dpv_risk:avoids
- dpv_risk_owl:avoids
rank: 1000
is_a: reduces
range: string
multivalued: true

```
</details></div>