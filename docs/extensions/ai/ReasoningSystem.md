---
search:
  boost: 10.0
---

# Class: ReasoningSystem 


_Artificial intelligence systems that uses available information to_

_generate predictions, make inferences and draw conclusions, involving_

_the representation of data in machine-processable form and application_

_of logic to arrive at decisions_



<div data-search-exclude markdown="1">



URI: [ai:ReasoningSystem](https://w3id.org/lmodel/dpv/ai/ReasoningSystem)





```mermaid
 classDiagram
    class ReasoningSystem
    click ReasoningSystem href "../ReasoningSystem/"
      AISystem <|-- ReasoningSystem
        click AISystem href "../AISystem/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [AISystem](AISystem.md)
        * **ReasoningSystem**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ReasoningSystem](https://w3id.org/lmodel/dpv/ai/ReasoningSystem) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Reasoning System




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ReasoningSystem |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ReasoningSystem |
| native | ai:ReasoningSystem |
| exact | dpv_ai:ReasoningSystem, dpv_ai_owl:ReasoningSystem |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ReasoningSystem
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ReasoningSystem
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Artificial intelligence systems that uses available information to

  generate predictions, make inferences and draw conclusions, involving

  the representation of data in machine-processable form and application

  of logic to arrive at decisions'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Reasoning System
exact_mappings:
- dpv_ai:ReasoningSystem
- dpv_ai_owl:ReasoningSystem
is_a: AISystem
class_uri: ai:ReasoningSystem

```
</details>

### Induced

<details>
```yaml
name: ReasoningSystem
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ReasoningSystem
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Artificial intelligence systems that uses available information to

  generate predictions, make inferences and draw conclusions, involving

  the representation of data in machine-processable form and application

  of logic to arrive at decisions'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Reasoning System
exact_mappings:
- dpv_ai:ReasoningSystem
- dpv_ai_owl:ReasoningSystem
is_a: AISystem
class_uri: ai:ReasoningSystem

```
</details></div>