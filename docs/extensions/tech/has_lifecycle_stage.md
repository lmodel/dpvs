---
search:
  boost: 5.0
---

# Slot: has_lifecycle_stage 


_Indicates the lifecycle stage associated with the technology_



<div data-search-exclude markdown="1">



URI: [tech:has_lifecycle_stage](https://w3id.org/lmodel/dpv/tech/has_lifecycle_stage)
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


* has lifecycle stage




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasLifecycleStage |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_lifecycle_stage |
| native | tech:has_lifecycle_stage |
| exact | dpv_tech:hasLifecycleStage, dpv_tech_owl:hasLifecycleStage |




## LinkML Source

<details>
```yaml
name: has_lifecycle_stage
definition_uri: tech:hasLifecycleStage
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasLifecycleStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the lifecycle stage associated with the technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has lifecycle stage
exact_mappings:
- dpv_tech:hasLifecycleStage
- dpv_tech_owl:hasLifecycleStage
rank: 1000
range: string
multivalued: true

```
</details></div>