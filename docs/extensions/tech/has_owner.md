---
search:
  boost: 5.0
---

# Slot: has_owner 


_Indicates technology owner_



<div data-search-exclude markdown="1">



URI: [tech:has_owner](https://w3id.org/lmodel/dpv/tech/has_owner)

## Inheritance

* [has_actor](has_actor.md)
    * **has_owner**








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


* has owner




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasOwner |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_owner |
| native | tech:has_owner |
| exact | dpv_tech:hasOwner, dpv_tech_owl:hasOwner |




## LinkML Source

<details>
```yaml
name: has_owner
definition_uri: tech:hasOwner
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasOwner
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates technology owner
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has owner
exact_mappings:
- dpv_tech:hasOwner
- dpv_tech_owl:hasOwner
rank: 1000
is_a: has_actor
range: string
multivalued: true

```
</details></div>