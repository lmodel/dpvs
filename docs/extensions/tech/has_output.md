---
search:
  boost: 5.0
---

# Slot: has_output 


_Indicates the output associated with the technology_



<div data-search-exclude markdown="1">



URI: [tech:has_output](https://w3id.org/lmodel/dpv/tech/has_output)

## Inheritance

* **has_output**
    * [has_output_action](has_output_action.md)








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


* has output




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasOutput |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_output |
| native | tech:has_output |
| exact | dpv_tech:hasOutput, dpv_tech_owl:hasOutput |




## LinkML Source

<details>
```yaml
name: has_output
definition_uri: tech:hasOutput
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasOutput
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the output associated with the technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has output
exact_mappings:
- dpv_tech:hasOutput
- dpv_tech_owl:hasOutput
rank: 1000
range: string
multivalued: true

```
</details></div>