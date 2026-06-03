---
search:
  boost: 5.0
---

# Slot: has_manufacturer 


_Indicates technology manufacturer_



<div data-search-exclude markdown="1">



URI: [tech:has_manufacturer](https://w3id.org/lmodel/dpv/tech/has_manufacturer)

## Inheritance

* [has_actor](has_actor.md)
    * **has_manufacturer**








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


* has manufacturer




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasManufacturer |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_manufacturer |
| native | tech:has_manufacturer |
| exact | dpv_tech:hasManufacturer, dpv_tech_owl:hasManufacturer |




## LinkML Source

<details>
```yaml
name: has_manufacturer
definition_uri: tech:hasManufacturer
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasManufacturer
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates technology manufacturer
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has manufacturer
exact_mappings:
- dpv_tech:hasManufacturer
- dpv_tech_owl:hasManufacturer
rank: 1000
is_a: has_actor
range: string
multivalued: true

```
</details></div>