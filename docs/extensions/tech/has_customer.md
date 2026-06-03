---
search:
  boost: 5.0
---

# Slot: has_customer 


_Indicates technology customer_



<div data-search-exclude markdown="1">



URI: [tech:has_customer](https://w3id.org/lmodel/dpv/tech/has_customer)

## Inheritance

* [has_actor](has_actor.md)
    * **has_customer**








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


* has customer




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasCustomer |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_customer |
| native | tech:has_customer |
| exact | dpv_tech:hasCustomer, dpv_tech_owl:hasCustomer |




## LinkML Source

<details>
```yaml
name: has_customer
definition_uri: tech:hasCustomer
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasCustomer
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates technology customer
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has customer
exact_mappings:
- dpv_tech:hasCustomer
- dpv_tech_owl:hasCustomer
rank: 1000
is_a: has_actor
range: string
multivalued: true

```
</details></div>