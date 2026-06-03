---
search:
  boost: 5.0
---

# Slot: has_user 


_Indicates technology user_



<div data-search-exclude markdown="1">



URI: [tech:has_user](https://w3id.org/lmodel/dpv/tech/has_user)

## Inheritance

* [has_actor](has_actor.md)
    * **has_user**








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


* has user




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasUser |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_user |
| native | tech:has_user |
| exact | dpv_tech:hasUser, dpv_tech_owl:hasUser |




## LinkML Source

<details>
```yaml
name: has_user
definition_uri: tech:hasUser
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasUser
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates technology user
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has user
exact_mappings:
- dpv_tech:hasUser
- dpv_tech_owl:hasUser
rank: 1000
is_a: has_actor
range: string
multivalued: true

```
</details></div>