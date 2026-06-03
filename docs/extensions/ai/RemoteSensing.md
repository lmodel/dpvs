---
search:
  boost: 10.0
---

# Class: RemoteSensing 


_Capability for acquisition of information about an object or phenomenon_

_without physical contact, typically using aerial sensor technologies_



<div data-search-exclude markdown="1">



URI: [ai:RemoteSensing](https://w3id.org/lmodel/dpv/ai/RemoteSensing)





```mermaid
 classDiagram
    class RemoteSensing
    click RemoteSensing href "../RemoteSensing/"
      Capability <|-- RemoteSensing
        click Capability href "../Capability/"
      PerceptionBasedAI <|-- RemoteSensing
        click PerceptionBasedAI href "../PerceptionBasedAI/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [ComputerVision](ComputerVision.md)
            * [PerceptionBasedAI](PerceptionBasedAI.md) [ [Capability](Capability.md)]
                * **RemoteSensing** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:RemoteSensing](https://w3id.org/lmodel/dpv/ai/RemoteSensing) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Remote Sensing




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#RemoteSensing |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:RemoteSensing |
| native | ai:RemoteSensing |
| exact | dpv_ai:RemoteSensing, dpv_ai_owl:RemoteSensing |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RemoteSensing
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#RemoteSensing
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for acquisition of information about an object or phenomenon

  without physical contact, typically using aerial sensor technologies'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Remote Sensing
exact_mappings:
- dpv_ai:RemoteSensing
- dpv_ai_owl:RemoteSensing
is_a: PerceptionBasedAI
mixins:
- Capability
class_uri: ai:RemoteSensing

```
</details>

### Induced

<details>
```yaml
name: RemoteSensing
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#RemoteSensing
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for acquisition of information about an object or phenomenon

  without physical contact, typically using aerial sensor technologies'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Remote Sensing
exact_mappings:
- dpv_ai:RemoteSensing
- dpv_ai_owl:RemoteSensing
is_a: PerceptionBasedAI
mixins:
- Capability
class_uri: ai:RemoteSensing

```
</details></div>