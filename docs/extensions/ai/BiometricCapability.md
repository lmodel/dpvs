---
search:
  boost: 10.0
---

# Class: BiometricCapability 


_Capability involving processing of biometric data or related to_

_biometrics_



<div data-search-exclude markdown="1">



URI: [ai:BiometricCapability](https://w3id.org/lmodel/dpv/ai/BiometricCapability)





```mermaid
 classDiagram
    class BiometricCapability
    click BiometricCapability href "../BiometricCapability/"
      Capability <|-- BiometricCapability
        click Capability href "../Capability/"
      HumanOrientedCapability <|-- BiometricCapability
        click HumanOrientedCapability href "../HumanOrientedCapability/"
      

      BiometricCapability <|-- ActionRecognition
        click ActionRecognition href "../ActionRecognition/"
      BiometricCapability <|-- BiometricCategorisation
        click BiometricCategorisation href "../BiometricCategorisation/"
      BiometricCapability <|-- BiometricIdentification
        click BiometricIdentification href "../BiometricIdentification/"
      BiometricCapability <|-- FaceRecognition
        click FaceRecognition href "../FaceRecognition/"
      BiometricCapability <|-- GestureRecognition
        click GestureRecognition href "../GestureRecognition/"
      

      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [HumanOrientedCapability](HumanOrientedCapability.md)
            * **BiometricCapability** [ [Capability](Capability.md)]
                * [ActionRecognition](ActionRecognition.md) [ [Capability](Capability.md) [ComputerVision](ComputerVision.md)]
                * [BiometricCategorisation](BiometricCategorisation.md) [ [Capability](Capability.md)]
                * [BiometricIdentification](BiometricIdentification.md) [ [Capability](Capability.md) [HumanIdentification](HumanIdentification.md)]
                * [FaceRecognition](FaceRecognition.md) [ [Capability](Capability.md) [ComputerVision](ComputerVision.md)]
                * [GestureRecognition](GestureRecognition.md) [ [Capability](Capability.md) [ComputerVision](ComputerVision.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:BiometricCapability](https://w3id.org/lmodel/dpv/ai/BiometricCapability) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Biometric Capability




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#BiometricCapability |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:BiometricCapability |
| native | ai:BiometricCapability |
| exact | dpv_ai:BiometricCapability, dpv_ai_owl:BiometricCapability |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BiometricCapability
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#BiometricCapability
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability involving processing of biometric data or related to

  biometrics'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Biometric Capability
exact_mappings:
- dpv_ai:BiometricCapability
- dpv_ai_owl:BiometricCapability
is_a: HumanOrientedCapability
mixins:
- Capability
class_uri: ai:BiometricCapability

```
</details>

### Induced

<details>
```yaml
name: BiometricCapability
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#BiometricCapability
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability involving processing of biometric data or related to

  biometrics'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Biometric Capability
exact_mappings:
- dpv_ai:BiometricCapability
- dpv_ai_owl:BiometricCapability
is_a: HumanOrientedCapability
mixins:
- Capability
class_uri: ai:BiometricCapability

```
</details></div>