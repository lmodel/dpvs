---
search:
  boost: 10.0
---

# Class: GestureRecognition 


_Capability for recognising human gestures_



<div data-search-exclude markdown="1">



URI: [ai:GestureRecognition](https://w3id.org/lmodel/dpv/ai/GestureRecognition)





```mermaid
 classDiagram
    class GestureRecognition
    click GestureRecognition href "../GestureRecognition/"
      Capability <|-- GestureRecognition
        click Capability href "../Capability/"
      ComputerVision <|-- GestureRecognition
        click ComputerVision href "../ComputerVision/"
      BiometricCapability <|-- GestureRecognition
        click BiometricCapability href "../BiometricCapability/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [HumanOrientedCapability](HumanOrientedCapability.md)
            * [BiometricCapability](BiometricCapability.md) [ [Capability](Capability.md)]
                * **GestureRecognition** [ [Capability](Capability.md) [ComputerVision](ComputerVision.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:GestureRecognition](https://w3id.org/lmodel/dpv/ai/GestureRecognition) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Gesture Recognition




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source |  Defining Artificial Intelligence 2.0 |
| upstream_iri | https://w3id.org/dpv/ai/owl#GestureRecognition |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:GestureRecognition |
| native | ai:GestureRecognition |
| exact | dpv_ai:GestureRecognition, dpv_ai_owl:GestureRecognition |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GestureRecognition
annotations:
  dct_source:
    tag: dct_source
    value: ' Defining Artificial Intelligence 2.0'
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#GestureRecognition
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability for recognising human gestures
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Gesture Recognition
exact_mappings:
- dpv_ai:GestureRecognition
- dpv_ai_owl:GestureRecognition
is_a: BiometricCapability
mixins:
- Capability
- ComputerVision
class_uri: ai:GestureRecognition

```
</details>

### Induced

<details>
```yaml
name: GestureRecognition
annotations:
  dct_source:
    tag: dct_source
    value: ' Defining Artificial Intelligence 2.0'
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#GestureRecognition
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability for recognising human gestures
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Gesture Recognition
exact_mappings:
- dpv_ai:GestureRecognition
- dpv_ai_owl:GestureRecognition
is_a: BiometricCapability
mixins:
- Capability
- ComputerVision
class_uri: ai:GestureRecognition

```
</details></div>