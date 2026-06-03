---
search:
  boost: 5.0
---

# Slot: has_data 


_Associates data with an AI system or model or implementation_



<div data-search-exclude markdown="1">



URI: [ai:has_data](https://w3id.org/lmodel/dpv/ai/has_data)

## Inheritance

* **has_data**
    * [has_testing_data](has_testing_data.md)
    * [has_training_data](has_training_data.md)
    * [has_validation_data](has_validation_data.md)








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


* [AiSubset](AiSubset.md)



## Aliases


* has data




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#hasData |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:has_data |
| native | ai:has_data |
| exact | dpv_ai:hasData, dpv_ai_owl:hasData |




## LinkML Source

<details>
```yaml
name: has_data
definition_uri: ai:hasData
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#hasData
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Associates data with an AI system or model or implementation
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- has data
exact_mappings:
- dpv_ai:hasData
- dpv_ai_owl:hasData
rank: 1000
range: string
multivalued: true

```
</details></div>