---
search:
  boost: 5.0
---

# Slot: has_system 


_Indicates the technology has or uses the associated system_



<div data-search-exclude markdown="1">



URI: [tech:has_system](https://w3id.org/lmodel/dpv/tech/has_system)
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


* has system




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasSystem |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_system |
| native | tech:has_system |
| exact | dpv_tech:hasSystem, dpv_tech_owl:hasSystem |




## LinkML Source

<details>
```yaml
name: has_system
definition_uri: tech:hasSystem
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasSystem
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the technology has or uses the associated system
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has system
exact_mappings:
- dpv_tech:hasSystem
- dpv_tech_owl:hasSystem
rank: 1000
range: string
multivalued: true

```
</details></div>