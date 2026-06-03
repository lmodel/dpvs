---
search:
  boost: 5.0
---

# Slot: has_model 


_Indicates the technology has or uses the associated model_



<div data-search-exclude markdown="1">



URI: [tech:has_model](https://w3id.org/lmodel/dpv/tech/has_model)
<!-- no inheritance hierarchy -->







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


* has model




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasModel |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_model |
| native | tech:has_model |
| exact | dpv_tech:hasModel, dpv_tech_owl:hasModel |




## LinkML Source

<details>
```yaml
name: has_model
definition_uri: tech:hasModel
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasModel
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the technology has or uses the associated model
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has model
exact_mappings:
- dpv_tech:hasModel
- dpv_tech_owl:hasModel
rank: 1000
range: string
multivalued: true

```
</details></div>