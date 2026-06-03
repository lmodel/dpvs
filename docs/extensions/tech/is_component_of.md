---
search:
  boost: 5.0
---

# Slot: is_component_of 


_Indicates the component is part of the associated system_



<div data-search-exclude markdown="1">



URI: [tech:is_component_of](https://w3id.org/lmodel/dpv/tech/is_component_of)
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


* is component of




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#isComponentOf |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:is_component_of |
| native | tech:is_component_of |
| exact | dpv_tech:isComponentOf, dpv_tech_owl:isComponentOf |




## LinkML Source

<details>
```yaml
name: is_component_of
definition_uri: tech:isComponentOf
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#isComponentOf
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the component is part of the associated system
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- is component of
exact_mappings:
- dpv_tech:isComponentOf
- dpv_tech_owl:isComponentOf
rank: 1000
range: string
multivalued: true

```
</details></div>