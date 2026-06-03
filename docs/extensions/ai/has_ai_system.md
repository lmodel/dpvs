---
search:
  boost: 5.0
---

# Slot: has_ai_system 


_Indicates the use of AI system for the associated context_



<div data-search-exclude markdown="1">



URI: [ai:has_ai_system](https://w3id.org/lmodel/dpv/ai/has_ai_system)

## Inheritance

* [has_ai](has_ai.md)
    * **has_ai_system**








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


* has AI system




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#hasAISystem |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:has_ai_system |
| native | ai:has_ai_system |
| exact | dpv_ai:hasAISystem, dpv_ai_owl:hasAISystem |




## LinkML Source

<details>
```yaml
name: has_ai_system
definition_uri: ai:hasAISystem
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#hasAISystem
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Indicates the use of AI system for the associated context
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- has AI system
exact_mappings:
- dpv_ai:hasAISystem
- dpv_ai_owl:hasAISystem
rank: 1000
is_a: has_ai
range: string
multivalued: true

```
</details></div>