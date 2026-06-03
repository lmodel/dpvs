---
search:
  boost: 5.0
---

# Slot: has_capability 


_Indicates the use of AI capability for the associated context_



<div data-search-exclude markdown="1">



URI: [ai:has_capability](https://w3id.org/lmodel/dpv/ai/has_capability)

## Inheritance

* [has_ai](has_ai.md)
    * **has_capability**








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


* has capability




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#hasCapability |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:has_capability |
| native | ai:has_capability |
| exact | dpv_ai:hasCapability, dpv_ai_owl:hasCapability |




## LinkML Source

<details>
```yaml
name: has_capability
definition_uri: ai:hasCapability
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#hasCapability
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Indicates the use of AI capability for the associated context
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- has capability
exact_mappings:
- dpv_ai:hasCapability
- dpv_ai_owl:hasCapability
rank: 1000
is_a: has_ai
range: string
multivalued: true

```
</details></div>