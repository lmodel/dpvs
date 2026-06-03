---
search:
  boost: 5.0
---

# Slot: has_input_action 


_Indicates the input action associated with the technology_



<div data-search-exclude markdown="1">



URI: [tech:has_input_action](https://w3id.org/lmodel/dpv/tech/has_input_action)

## Inheritance

* [has_input](has_input.md)
    * **has_input_action**








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


* [TechSubset](TechSubset.md)



## Aliases


* has input action




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasInputAction |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_input_action |
| native | tech:has_input_action |
| exact | dpv_tech:hasInputAction, dpv_tech_owl:hasInputAction |




## LinkML Source

<details>
```yaml
name: has_input_action
definition_uri: tech:hasInputAction
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasInputAction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the input action associated with the technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has input action
exact_mappings:
- dpv_tech:hasInputAction
- dpv_tech_owl:hasInputAction
rank: 1000
is_a: has_input
range: string
multivalued: true

```
</details></div>