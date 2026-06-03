---
search:
  boost: 5.0
---

# Slot: has_producer 


_Indicates technology producer_



<div data-search-exclude markdown="1">



URI: [tech:has_producer](https://w3id.org/lmodel/dpv/tech/has_producer)

## Inheritance

* [has_actor](has_actor.md)
    * **has_producer**








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


* has producer




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasProducer |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_producer |
| native | tech:has_producer |
| exact | dpv_tech:hasProducer, dpv_tech_owl:hasProducer |




## LinkML Source

<details>
```yaml
name: has_producer
definition_uri: tech:hasProducer
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasProducer
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates technology producer
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has producer
exact_mappings:
- dpv_tech:hasProducer
- dpv_tech_owl:hasProducer
rank: 1000
is_a: has_actor
range: string
multivalued: true

```
</details></div>