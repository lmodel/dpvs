---
search:
  boost: 10.0
---

# Class: RealTimeBiometricIdentification 


_Capability involving biometric identification carried out in real-time_

_or instantaneously_



<div data-search-exclude markdown="1">



URI: [ai:RealTimeBiometricIdentification](https://w3id.org/lmodel/dpv/ai/RealTimeBiometricIdentification)





```mermaid
 classDiagram
    class RealTimeBiometricIdentification
    click RealTimeBiometricIdentification href "../RealTimeBiometricIdentification/"
      Capability <|-- RealTimeBiometricIdentification
        click Capability href "../Capability/"
      BiometricIdentification <|-- RealTimeBiometricIdentification
        click BiometricIdentification href "../BiometricIdentification/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [HumanOrientedCapability](HumanOrientedCapability.md)
            * [BiometricCapability](BiometricCapability.md) [ [Capability](Capability.md)]
                * [BiometricIdentification](BiometricIdentification.md) [ [Capability](Capability.md) [HumanIdentification](HumanIdentification.md)]
                    * **RealTimeBiometricIdentification** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:RealTimeBiometricIdentification](https://w3id.org/lmodel/dpv/ai/RealTimeBiometricIdentification) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Real-Time Biometric Identification




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#RealTimeBiometricIdentification |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:RealTimeBiometricIdentification |
| native | ai:RealTimeBiometricIdentification |
| exact | dpv_ai:RealTimeBiometricIdentification, dpv_ai_owl:RealTimeBiometricIdentification |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RealTimeBiometricIdentification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#RealTimeBiometricIdentification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability involving biometric identification carried out in real-time

  or instantaneously'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Real-Time Biometric Identification
exact_mappings:
- dpv_ai:RealTimeBiometricIdentification
- dpv_ai_owl:RealTimeBiometricIdentification
is_a: BiometricIdentification
mixins:
- Capability
class_uri: ai:RealTimeBiometricIdentification

```
</details>

### Induced

<details>
```yaml
name: RealTimeBiometricIdentification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#RealTimeBiometricIdentification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability involving biometric identification carried out in real-time

  or instantaneously'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Real-Time Biometric Identification
exact_mappings:
- dpv_ai:RealTimeBiometricIdentification
- dpv_ai_owl:RealTimeBiometricIdentification
is_a: BiometricIdentification
mixins:
- Capability
class_uri: ai:RealTimeBiometricIdentification

```
</details></div>