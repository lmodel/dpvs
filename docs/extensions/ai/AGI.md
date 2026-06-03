---
search:
  boost: 10.0
---

# Class: AGI 


_Type of AI system that addresses a broad range of tasks with a_

_satisfactory level of performance_



<div data-search-exclude markdown="1">



URI: [ai:AGI](https://w3id.org/lmodel/dpv/ai/AGI)





```mermaid
 classDiagram
    class AGI
    click AGI href "../AGI/"
      AISystem <|-- AGI
        click AISystem href "../AISystem/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [AISystem](AISystem.md)
        * **AGI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:AGI](https://w3id.org/lmodel/dpv/ai/AGI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Artificial General Intelligence (AGI)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/ai/owl#AGI |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:AGI |
| native | ai:AGI |
| exact | dpv_ai:AGI, dpv_ai_owl:AGI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AGI
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#AGI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Type of AI system that addresses a broad range of tasks with a

  satisfactory level of performance'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Artificial General Intelligence (AGI)
exact_mappings:
- dpv_ai:AGI
- dpv_ai_owl:AGI
is_a: AISystem
class_uri: ai:AGI

```
</details>

### Induced

<details>
```yaml
name: AGI
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#AGI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Type of AI system that addresses a broad range of tasks with a

  satisfactory level of performance'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Artificial General Intelligence (AGI)
exact_mappings:
- dpv_ai:AGI
- dpv_ai_owl:AGI
is_a: AISystem
class_uri: ai:AGI

```
</details></div>