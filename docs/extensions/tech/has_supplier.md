---
search:
  boost: 5.0
---

# Slot: has_supplier 


_Indicates technology supplier_



<div data-search-exclude markdown="1">



URI: [tech:has_supplier](https://w3id.org/lmodel/dpv/tech/has_supplier)

## Inheritance

* [has_actor](has_actor.md)
    * **has_supplier**








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


* has supplier




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasSupplier |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_supplier |
| native | tech:has_supplier |
| exact | dpv_tech:hasSupplier, dpv_tech_owl:hasSupplier |




## LinkML Source

<details>
```yaml
name: has_supplier
definition_uri: tech:hasSupplier
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasSupplier
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates technology supplier
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has supplier
exact_mappings:
- dpv_tech:hasSupplier
- dpv_tech_owl:hasSupplier
rank: 1000
is_a: has_actor
range: string
multivalued: true

```
</details></div>