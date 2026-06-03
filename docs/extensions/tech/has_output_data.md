---
search:
  boost: 5.0
---

# Slot: has_output_data 


_Indicates the output data associated with the technology_



<div data-search-exclude markdown="1">



URI: [tech:has_output_data](https://w3id.org/lmodel/dpv/tech/has_output_data)
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


* has output data




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasOutputData |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_output_data |
| native | tech:has_output_data |
| exact | dpv_tech:hasOutputData, dpv_tech_owl:hasOutputData |




## LinkML Source

<details>
```yaml
name: has_output_data
definition_uri: tech:hasOutputData
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasOutputData
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the output data associated with the technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has output data
exact_mappings:
- dpv_tech:hasOutputData
- dpv_tech_owl:hasOutputData
rank: 1000
range: string
multivalued: true

```
</details></div>