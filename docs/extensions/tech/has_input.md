---
search:
  boost: 5.0
---

# Slot: has_input 


_Indicates the input associated with the technology_



<div data-search-exclude markdown="1">



URI: [tech:has_input](https://w3id.org/lmodel/dpv/tech/has_input)

## Inheritance

* **has_input**
    * [has_input_action](has_input_action.md)








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


* has input




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasInput |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_input |
| native | tech:has_input |
| exact | dpv_tech:hasInput, dpv_tech_owl:hasInput |




## LinkML Source

<details>
```yaml
name: has_input
definition_uri: tech:hasInput
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasInput
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the input associated with the technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has input
exact_mappings:
- dpv_tech:hasInput
- dpv_tech_owl:hasInput
rank: 1000
range: string
multivalued: true

```
</details></div>