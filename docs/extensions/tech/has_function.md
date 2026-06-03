---
search:
  boost: 5.0
---

# Slot: has_function 


_Indicates the function of the technology_



<div data-search-exclude markdown="1">



URI: [tech:has_function](https://w3id.org/lmodel/dpv/tech/has_function)
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


* has function




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasFunction |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_function |
| native | tech:has_function |
| exact | dpv_tech:hasFunction, dpv_tech_owl:hasFunction |




## LinkML Source

<details>
```yaml
name: has_function
definition_uri: tech:hasFunction
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasFunction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the function of the technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has function
exact_mappings:
- dpv_tech:hasFunction
- dpv_tech_owl:hasFunction
rank: 1000
range: string
multivalued: true

```
</details></div>