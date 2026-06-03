---
search:
  boost: 5.0
---

# Slot: has_operating_factor 


_Indicates the operating factor for the technology_



<div data-search-exclude markdown="1">



URI: [tech:has_operating_factor](https://w3id.org/lmodel/dpv/tech/has_operating_factor)
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


* has operating factor




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasOperatingFactor |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_operating_factor |
| native | tech:has_operating_factor |
| exact | dpv_tech:hasOperatingFactor, dpv_tech_owl:hasOperatingFactor |




## LinkML Source

<details>
```yaml
name: has_operating_factor
definition_uri: tech:hasOperatingFactor
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasOperatingFactor
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the operating factor for the technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has operating factor
exact_mappings:
- dpv_tech:hasOperatingFactor
- dpv_tech_owl:hasOperatingFactor
rank: 1000
range: string
multivalued: true

```
</details></div>