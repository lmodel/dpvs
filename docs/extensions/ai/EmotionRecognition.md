---
search:
  boost: 10.0
---

# Class: EmotionRecognition 


_Capability for identifying and categorising emotions expressed in a_

_piece of text, speech, video or image or combination thereof_



<div data-search-exclude markdown="1">



URI: [ai:EmotionRecognition](https://w3id.org/lmodel/dpv/ai/EmotionRecognition)





```mermaid
 classDiagram
    class EmotionRecognition
    click EmotionRecognition href "../EmotionRecognition/"
      Capability <|-- EmotionRecognition
        click Capability href "../Capability/"
      HumanOrientedCapability <|-- EmotionRecognition
        click HumanOrientedCapability href "../HumanOrientedCapability/"
      

      EmotionRecognition <|-- BiometricEmotionRecognition
        click BiometricEmotionRecognition href "../BiometricEmotionRecognition/"
      

      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [HumanOrientedCapability](HumanOrientedCapability.md)
            * **EmotionRecognition** [ [Capability](Capability.md)]
                * [BiometricEmotionRecognition](BiometricEmotionRecognition.md) [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:EmotionRecognition](https://w3id.org/lmodel/dpv/ai/EmotionRecognition) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Emotion Recognition




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.6.3 |
| upstream_iri | https://w3id.org/dpv/ai/owl#EmotionRecognition |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:EmotionRecognition |
| native | ai:EmotionRecognition |
| exact | dpv_ai:EmotionRecognition, dpv_ai_owl:EmotionRecognition |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EmotionRecognition
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.6.3
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#EmotionRecognition
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for identifying and categorising emotions expressed in a

  piece of text, speech, video or image or combination thereof'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Emotion Recognition
exact_mappings:
- dpv_ai:EmotionRecognition
- dpv_ai_owl:EmotionRecognition
is_a: HumanOrientedCapability
mixins:
- Capability
class_uri: ai:EmotionRecognition

```
</details>

### Induced

<details>
```yaml
name: EmotionRecognition
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.6.3
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#EmotionRecognition
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for identifying and categorising emotions expressed in a

  piece of text, speech, video or image or combination thereof'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Emotion Recognition
exact_mappings:
- dpv_ai:EmotionRecognition
- dpv_ai_owl:EmotionRecognition
is_a: HumanOrientedCapability
mixins:
- Capability
class_uri: ai:EmotionRecognition

```
</details></div>