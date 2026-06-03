---
search:
  boost: 5.0
---

# Slot: has_evaluator 


_Indicates technology evaluator_



<div data-search-exclude markdown="1">



URI: [tech:has_evaluator](https://w3id.org/lmodel/dpv/tech/has_evaluator)

## Inheritance

* [has_actor](has_actor.md)
    * **has_evaluator**








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


* has evaluator




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasEvaluator |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_evaluator |
| native | tech:has_evaluator |
| exact | dpv_tech:hasEvaluator, dpv_tech_owl:hasEvaluator |




## LinkML Source

<details>
```yaml
name: has_evaluator
definition_uri: tech:hasEvaluator
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasEvaluator
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates technology evaluator
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has evaluator
exact_mappings:
- dpv_tech:hasEvaluator
- dpv_tech_owl:hasEvaluator
rank: 1000
is_a: has_actor
range: string
multivalued: true

```
</details></div>