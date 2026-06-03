---
search:
  boost: 10.0
---

# Class: PostTimeBiometricIdentification 


_Capability involving biometric identification carried out later or not_

_in real-time or non-instantaneously_



<div data-search-exclude markdown="1">



URI: [ai:PostTimeBiometricIdentification](https://w3id.org/lmodel/dpv/ai/PostTimeBiometricIdentification)





```mermaid
 classDiagram
    class PostTimeBiometricIdentification
    click PostTimeBiometricIdentification href "../PostTimeBiometricIdentification/"
      Capability <|-- PostTimeBiometricIdentification
        click Capability href "../Capability/"
      BiometricIdentification <|-- PostTimeBiometricIdentification
        click BiometricIdentification href "../BiometricIdentification/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [HumanOrientedCapability](HumanOrientedCapability.md)
            * [BiometricCapability](BiometricCapability.md) [ [Capability](Capability.md)]
                * [BiometricIdentification](BiometricIdentification.md) [ [Capability](Capability.md) [HumanIdentification](HumanIdentification.md)]
                    * **PostTimeBiometricIdentification** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:PostTimeBiometricIdentification](https://w3id.org/lmodel/dpv/ai/PostTimeBiometricIdentification) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Post-Time Biometric Identification




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#PostTimeBiometricIdentification |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:PostTimeBiometricIdentification |
| native | ai:PostTimeBiometricIdentification |
| exact | dpv_ai:PostTimeBiometricIdentification, dpv_ai_owl:PostTimeBiometricIdentification |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PostTimeBiometricIdentification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#PostTimeBiometricIdentification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability involving biometric identification carried out later or not

  in real-time or non-instantaneously'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Post-Time Biometric Identification
exact_mappings:
- dpv_ai:PostTimeBiometricIdentification
- dpv_ai_owl:PostTimeBiometricIdentification
is_a: BiometricIdentification
mixins:
- Capability
class_uri: ai:PostTimeBiometricIdentification

```
</details>

### Induced

<details>
```yaml
name: PostTimeBiometricIdentification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#PostTimeBiometricIdentification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability involving biometric identification carried out later or not

  in real-time or non-instantaneously'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Post-Time Biometric Identification
exact_mappings:
- dpv_ai:PostTimeBiometricIdentification
- dpv_ai_owl:PostTimeBiometricIdentification
is_a: BiometricIdentification
mixins:
- Capability
class_uri: ai:PostTimeBiometricIdentification

```
</details></div>