---
search:
  boost: 5.0
---

# Slot: has_designer 


_Indicates technology designer_



<div data-search-exclude markdown="1">



URI: [tech:has_designer](https://w3id.org/lmodel/dpv/tech/has_designer)

## Inheritance

* [has_actor](has_actor.md)
    * **has_designer**








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


* has designer




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasDesigner |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_designer |
| native | tech:has_designer |
| exact | dpv_tech:hasDesigner, dpv_tech_owl:hasDesigner |




## LinkML Source

<details>
```yaml
name: has_designer
definition_uri: tech:hasDesigner
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasDesigner
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates technology designer
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has designer
exact_mappings:
- dpv_tech:hasDesigner
- dpv_tech_owl:hasDesigner
rank: 1000
is_a: has_actor
range: string
multivalued: true

```
</details></div>