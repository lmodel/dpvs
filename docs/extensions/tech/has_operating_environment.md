---
search:
  boost: 5.0
---

# Slot: has_operating_environment 


_Indicates the operating environment for the technology_



<div data-search-exclude markdown="1">



URI: [tech:has_operating_environment](https://w3id.org/lmodel/dpv/tech/has_operating_environment)
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


* has operating environment




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasOperatingEnvironment |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_operating_environment |
| native | tech:has_operating_environment |
| exact | dpv_tech:hasOperatingEnvironment, dpv_tech_owl:hasOperatingEnvironment |




## LinkML Source

<details>
```yaml
name: has_operating_environment
definition_uri: tech:hasOperatingEnvironment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasOperatingEnvironment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the operating environment for the technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has operating environment
exact_mappings:
- dpv_tech:hasOperatingEnvironment
- dpv_tech_owl:hasOperatingEnvironment
rank: 1000
range: string
multivalued: true

```
</details></div>