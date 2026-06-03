---
search:
  boost: 5.0
---

# Slot: has_gpai_model 


_Indicates the use of an GPAI model for the associated context_



<div data-search-exclude markdown="1">



URI: [ai:has_gpai_model](https://w3id.org/lmodel/dpv/ai/has_gpai_model)

## Inheritance

* [has_ai](has_ai.md)
    * [has_model](has_model.md)
        * **has_gpai_model**








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


* has GPAI model




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#hasGPAIModel |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:has_gpai_model |
| native | ai:has_gpai_model |
| exact | dpv_ai:hasGPAIModel, dpv_ai_owl:hasGPAIModel |




## LinkML Source

<details>
```yaml
name: has_gpai_model
definition_uri: ai:hasGPAIModel
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#hasGPAIModel
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Indicates the use of an GPAI model for the associated context
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- has GPAI model
exact_mappings:
- dpv_ai:hasGPAIModel
- dpv_ai_owl:hasGPAIModel
rank: 1000
is_a: has_model
range: string
multivalued: true

```
</details></div>