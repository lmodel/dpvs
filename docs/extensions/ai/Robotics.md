---
search:
  boost: 10.0
---

# Class: Robotics 


_The science of designing, engineering and using robots, i.e. machines_

_controlled by computers which perform jobs automatically_



<div data-search-exclude markdown="1">



URI: [ai:Robotics](https://w3id.org/lmodel/dpv/ai/Robotics)





```mermaid
 classDiagram
    class Robotics
    click Robotics href "../Robotics/"
      AISystem <|-- Robotics
        click AISystem href "../AISystem/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [AISystem](AISystem.md)
        * **Robotics**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:Robotics](https://w3id.org/lmodel/dpv/ai/Robotics) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Robotics




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#Robotics |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:Robotics |
| native | ai:Robotics |
| exact | dpv_ai:Robotics, dpv_ai_owl:Robotics |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Robotics
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#Robotics
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The science of designing, engineering and using robots, i.e. machines

  controlled by computers which perform jobs automatically'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Robotics
exact_mappings:
- dpv_ai:Robotics
- dpv_ai_owl:Robotics
is_a: AISystem
class_uri: ai:Robotics

```
</details>

### Induced

<details>
```yaml
name: Robotics
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#Robotics
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The science of designing, engineering and using robots, i.e. machines

  controlled by computers which perform jobs automatically'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Robotics
exact_mappings:
- dpv_ai:Robotics
- dpv_ai_owl:Robotics
is_a: AISystem
class_uri: ai:Robotics

```
</details></div>