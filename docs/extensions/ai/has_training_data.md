---
search:
  boost: 5.0
---

# Slot: has_training_data 


_Associates the data used for training AI_



<div data-search-exclude markdown="1">



URI: [ai:has_training_data](https://w3id.org/lmodel/dpv/ai/has_training_data)

## Inheritance

* [has_data](has_data.md)
    * **has_training_data**








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


* has training data




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#hasTrainingData |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:has_training_data |
| native | ai:has_training_data |
| exact | dpv_ai:hasTrainingData, dpv_ai_owl:hasTrainingData |




## LinkML Source

<details>
```yaml
name: has_training_data
definition_uri: ai:hasTrainingData
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#hasTrainingData
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Associates the data used for training AI
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- has training data
exact_mappings:
- dpv_ai:hasTrainingData
- dpv_ai_owl:hasTrainingData
rank: 1000
is_a: has_data
range: string
multivalued: true

```
</details></div>