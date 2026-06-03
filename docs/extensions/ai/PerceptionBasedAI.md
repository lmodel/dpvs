---
search:
  boost: 10.0
---

# Class: PerceptionBasedAI 


_Capability of using agents to interpret and understand information from_

_their environment through sensory inputs_



<div data-search-exclude markdown="1">



URI: [ai:PerceptionBasedAI](https://w3id.org/lmodel/dpv/ai/PerceptionBasedAI)





```mermaid
 classDiagram
    class PerceptionBasedAI
    click PerceptionBasedAI href "../PerceptionBasedAI/"
      Capability <|-- PerceptionBasedAI
        click Capability href "../Capability/"
      ComputerVision <|-- PerceptionBasedAI
        click ComputerVision href "../ComputerVision/"
      

      PerceptionBasedAI <|-- RemoteSensing
        click RemoteSensing href "../RemoteSensing/"
      

      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [ComputerVision](ComputerVision.md)
            * **PerceptionBasedAI** [ [Capability](Capability.md)]
                * [RemoteSensing](RemoteSensing.md) [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:PerceptionBasedAI](https://w3id.org/lmodel/dpv/ai/PerceptionBasedAI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Perception-based AI




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#PerceptionBasedAI |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:PerceptionBasedAI |
| native | ai:PerceptionBasedAI |
| exact | dpv_ai:PerceptionBasedAI, dpv_ai_owl:PerceptionBasedAI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PerceptionBasedAI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#PerceptionBasedAI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability of using agents to interpret and understand information from

  their environment through sensory inputs'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Perception-based AI
exact_mappings:
- dpv_ai:PerceptionBasedAI
- dpv_ai_owl:PerceptionBasedAI
is_a: ComputerVision
mixins:
- Capability
class_uri: ai:PerceptionBasedAI

```
</details>

### Induced

<details>
```yaml
name: PerceptionBasedAI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#PerceptionBasedAI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability of using agents to interpret and understand information from

  their environment through sensory inputs'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Perception-based AI
exact_mappings:
- dpv_ai:PerceptionBasedAI
- dpv_ai_owl:PerceptionBasedAI
is_a: ComputerVision
mixins:
- Capability
class_uri: ai:PerceptionBasedAI

```
</details></div>