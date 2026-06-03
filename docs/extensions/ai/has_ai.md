---
search:
  boost: 5.0
---

# Slot: has_ai 


_Indicates the use of AI for the associated context_



<div data-search-exclude markdown="1">



URI: [ai:has_ai](https://w3id.org/lmodel/dpv/ai/has_ai)

## Inheritance

* **has_ai**
    * [has_ai_system](has_ai_system.md)
    * [has_capability](has_capability.md)
    * [has_model](has_model.md)
    * [has_technique](has_technique.md)








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


* has AI




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#hasAI |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:has_ai |
| native | ai:has_ai |
| exact | dpv_ai:hasAI, dpv_ai_owl:hasAI |




## LinkML Source

<details>
```yaml
name: has_ai
definition_uri: ai:hasAI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#hasAI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Indicates the use of AI for the associated context
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- has AI
exact_mappings:
- dpv_ai:hasAI
- dpv_ai_owl:hasAI
rank: 1000
range: string
multivalued: true

```
</details></div>