---
search:
  boost: 5.0
---

# Slot: has_infrastructure 


_Indicates the technology has or uses the associated infrastructure_



<div data-search-exclude markdown="1">



URI: [tech:has_infrastructure](https://w3id.org/lmodel/dpv/tech/has_infrastructure)
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


* has infrastructure




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasInfrastructure |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_infrastructure |
| native | tech:has_infrastructure |
| exact | dpv_tech:hasInfrastructure, dpv_tech_owl:hasInfrastructure |




## LinkML Source

<details>
```yaml
name: has_infrastructure
definition_uri: tech:hasInfrastructure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasInfrastructure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the technology has or uses the associated infrastructure
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has infrastructure
exact_mappings:
- dpv_tech:hasInfrastructure
- dpv_tech_owl:hasInfrastructure
rank: 1000
range: string
multivalued: true

```
</details></div>