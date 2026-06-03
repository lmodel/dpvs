---
search:
  boost: 5.0
---

# Slot: has_purchaser 


_Indicates technology purchaser_



<div data-search-exclude markdown="1">



URI: [tech:has_purchaser](https://w3id.org/lmodel/dpv/tech/has_purchaser)

## Inheritance

* [has_actor](has_actor.md)
    * **has_purchaser**








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


* has purchaser




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasPurchaser |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_purchaser |
| native | tech:has_purchaser |
| exact | dpv_tech:hasPurchaser, dpv_tech_owl:hasPurchaser |




## LinkML Source

<details>
```yaml
name: has_purchaser
definition_uri: tech:hasPurchaser
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasPurchaser
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates technology purchaser
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has purchaser
exact_mappings:
- dpv_tech:hasPurchaser
- dpv_tech_owl:hasPurchaser
rank: 1000
is_a: has_actor
range: string
multivalued: true

```
</details></div>