---
search:
  boost: 10.0
---

# Class: NarrowAI 


_Type of AI system that is focused on defined tasks to address a specific_

_problem i.e. it addresses a narrow scope of tasks and problems_



<div data-search-exclude markdown="1">



URI: [ai:NarrowAI](https://w3id.org/lmodel/dpv/ai/NarrowAI)





```mermaid
 classDiagram
    class NarrowAI
    click NarrowAI href "../NarrowAI/"
      AISystem <|-- NarrowAI
        click AISystem href "../AISystem/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [AISystem](AISystem.md)
        * **NarrowAI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:NarrowAI](https://w3id.org/lmodel/dpv/ai/NarrowAI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Narrow AI




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.1.24 |
| upstream_iri | https://w3id.org/dpv/ai/owl#NarrowAI |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:NarrowAI |
| native | ai:NarrowAI |
| exact | dpv_ai:NarrowAI, dpv_ai_owl:NarrowAI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NarrowAI
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.1.24
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#NarrowAI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Type of AI system that is focused on defined tasks to address a specific

  problem i.e. it addresses a narrow scope of tasks and problems'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Narrow AI
exact_mappings:
- dpv_ai:NarrowAI
- dpv_ai_owl:NarrowAI
is_a: AISystem
class_uri: ai:NarrowAI

```
</details>

### Induced

<details>
```yaml
name: NarrowAI
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.1.24
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#NarrowAI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Type of AI system that is focused on defined tasks to address a specific

  problem i.e. it addresses a narrow scope of tasks and problems'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Narrow AI
exact_mappings:
- dpv_ai:NarrowAI
- dpv_ai_owl:NarrowAI
is_a: AISystem
class_uri: ai:NarrowAI

```
</details></div>