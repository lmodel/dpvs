---
search:
  boost: 5.0
---

# Slot: has_platform 


_Indicates the technology has or uses the associated platform_



<div data-search-exclude markdown="1">



URI: [tech:has_platform](https://w3id.org/lmodel/dpv/tech/has_platform)
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


* has platform




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasPlatform |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_platform |
| native | tech:has_platform |
| exact | dpv_tech:hasPlatform, dpv_tech_owl:hasPlatform |




## LinkML Source

<details>
```yaml
name: has_platform
definition_uri: tech:hasPlatform
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasPlatform
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the technology has or uses the associated platform
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has platform
exact_mappings:
- dpv_tech:hasPlatform
- dpv_tech_owl:hasPlatform
rank: 1000
range: string
multivalued: true

```
</details></div>