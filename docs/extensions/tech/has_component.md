---
search:
  boost: 5.0
---

# Slot: has_component 


_Indicates the system has or uses the associated component_



<div data-search-exclude markdown="1">



URI: [tech:has_component](https://w3id.org/lmodel/dpv/tech/has_component)
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


* has component




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasComponent |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_component |
| native | tech:has_component |
| exact | dpv_tech:hasComponent, dpv_tech_owl:hasComponent |




## LinkML Source

<details>
```yaml
name: has_component
definition_uri: tech:hasComponent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasComponent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the system has or uses the associated component
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has component
exact_mappings:
- dpv_tech:hasComponent
- dpv_tech_owl:hasComponent
rank: 1000
range: string
multivalued: true

```
</details></div>