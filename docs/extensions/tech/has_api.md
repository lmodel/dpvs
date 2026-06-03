---
search:
  boost: 5.0
---

# Slot: has_api 


_Indicates the technology has or uses the associated api_



<div data-search-exclude markdown="1">



URI: [tech:has_api](https://w3id.org/lmodel/dpv/tech/has_api)
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


* has api




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasAPI |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_api |
| native | tech:has_api |
| exact | dpv_tech:hasAPI, dpv_tech_owl:hasAPI |




## LinkML Source

<details>
```yaml
name: has_api
definition_uri: tech:hasAPI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasAPI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the technology has or uses the associated api
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has api
exact_mappings:
- dpv_tech:hasAPI
- dpv_tech_owl:hasAPI
rank: 1000
range: string
multivalued: true

```
</details></div>