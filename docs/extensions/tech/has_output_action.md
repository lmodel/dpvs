---
search:
  boost: 5.0
---

# Slot: has_output_action 


_Indicates the output action associated with the technology_



<div data-search-exclude markdown="1">



URI: [tech:has_output_action](https://w3id.org/lmodel/dpv/tech/has_output_action)

## Inheritance

* [has_output](has_output.md)
    * **has_output_action**








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


* has output action




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasOutputAction |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_output_action |
| native | tech:has_output_action |
| exact | dpv_tech:hasOutputAction, dpv_tech_owl:hasOutputAction |




## LinkML Source

<details>
```yaml
name: has_output_action
definition_uri: tech:hasOutputAction
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasOutputAction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the output action associated with the technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has output action
exact_mappings:
- dpv_tech:hasOutputAction
- dpv_tech_owl:hasOutputAction
rank: 1000
is_a: has_output
range: string
multivalued: true

```
</details></div>