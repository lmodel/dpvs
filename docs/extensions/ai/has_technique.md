---
search:
  boost: 5.0
---

# Slot: has_technique 


_Indicates the use of AI technique for the associated context_



<div data-search-exclude markdown="1">



URI: [ai:has_technique](https://w3id.org/lmodel/dpv/ai/has_technique)

## Inheritance

* [has_ai](has_ai.md)
    * **has_technique**








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


* has technique




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#hasTechnique |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:has_technique |
| native | ai:has_technique |
| exact | dpv_ai:hasTechnique, dpv_ai_owl:hasTechnique |




## LinkML Source

<details>
```yaml
name: has_technique
definition_uri: ai:hasTechnique
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#hasTechnique
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Indicates the use of AI technique for the associated context
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- has technique
exact_mappings:
- dpv_ai:hasTechnique
- dpv_ai_owl:hasTechnique
rank: 1000
is_a: has_ai
range: string
multivalued: true

```
</details></div>