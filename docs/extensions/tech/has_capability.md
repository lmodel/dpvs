---
search:
  boost: 5.0
---

# Slot: has_capability 


_Indicates the capability of the technology_



<div data-search-exclude markdown="1">



URI: [tech:has_capability](https://w3id.org/lmodel/dpv/tech/has_capability)
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


* has capability




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasCapability |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_capability |
| native | tech:has_capability |
| exact | dpv_tech:hasCapability, dpv_tech_owl:hasCapability |




## LinkML Source

<details>
```yaml
name: has_capability
definition_uri: tech:hasCapability
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasCapability
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the capability of the technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has capability
exact_mappings:
- dpv_tech:hasCapability
- dpv_tech_owl:hasCapability
rank: 1000
range: string
multivalued: true

```
</details></div>