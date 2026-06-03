---
search:
  boost: 5.0
---

# Slot: has_algorithm 


_Indicates the technology has or uses the associated algorithm_



<div data-search-exclude markdown="1">



URI: [tech:has_algorithm](https://w3id.org/lmodel/dpv/tech/has_algorithm)
<!-- no inheritance hierarchy -->







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


* has algorithm




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasAlgorithm |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_algorithm |
| native | tech:has_algorithm |
| exact | dpv_tech:hasAlgorithm, dpv_tech_owl:hasAlgorithm |




## LinkML Source

<details>
```yaml
name: has_algorithm
definition_uri: tech:hasAlgorithm
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasAlgorithm
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the technology has or uses the associated algorithm
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has algorithm
exact_mappings:
- dpv_tech:hasAlgorithm
- dpv_tech_owl:hasAlgorithm
rank: 1000
range: string
multivalued: true

```
</details></div>