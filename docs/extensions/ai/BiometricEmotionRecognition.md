---
search:
  boost: 10.0
---

# Class: BiometricEmotionRecognition 


_Capability for recognising emotions based on biometrics information_



<div data-search-exclude markdown="1">



URI: [ai:BiometricEmotionRecognition](https://w3id.org/lmodel/dpv/ai/BiometricEmotionRecognition)





```mermaid
 classDiagram
    class BiometricEmotionRecognition
    click BiometricEmotionRecognition href "../BiometricEmotionRecognition/"
      Capability <|-- BiometricEmotionRecognition
        click Capability href "../Capability/"
      EmotionRecognition <|-- BiometricEmotionRecognition
        click EmotionRecognition href "../EmotionRecognition/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [HumanOrientedCapability](HumanOrientedCapability.md)
            * [EmotionRecognition](EmotionRecognition.md) [ [Capability](Capability.md)]
                * **BiometricEmotionRecognition** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:BiometricEmotionRecognition](https://w3id.org/lmodel/dpv/ai/BiometricEmotionRecognition) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Biometric Emotion Recognition




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#BiometricEmotionRecognition |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:BiometricEmotionRecognition |
| native | ai:BiometricEmotionRecognition |
| exact | dpv_ai:BiometricEmotionRecognition, dpv_ai_owl:BiometricEmotionRecognition |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BiometricEmotionRecognition
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#BiometricEmotionRecognition
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability for recognising emotions based on biometrics information
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Biometric Emotion Recognition
exact_mappings:
- dpv_ai:BiometricEmotionRecognition
- dpv_ai_owl:BiometricEmotionRecognition
is_a: EmotionRecognition
mixins:
- Capability
class_uri: ai:BiometricEmotionRecognition

```
</details>

### Induced

<details>
```yaml
name: BiometricEmotionRecognition
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#BiometricEmotionRecognition
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability for recognising emotions based on biometrics information
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Biometric Emotion Recognition
exact_mappings:
- dpv_ai:BiometricEmotionRecognition
- dpv_ai_owl:BiometricEmotionRecognition
is_a: EmotionRecognition
mixins:
- Capability
class_uri: ai:BiometricEmotionRecognition

```
</details></div>