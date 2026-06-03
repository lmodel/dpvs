---
search:
  boost: 10.0
---

# Class: RemoteBiometricIdentification 


_Capability involving biometric identification carried out remotely_



<div data-search-exclude markdown="1">



URI: [ai:RemoteBiometricIdentification](https://w3id.org/lmodel/dpv/ai/RemoteBiometricIdentification)





```mermaid
 classDiagram
    class RemoteBiometricIdentification
    click RemoteBiometricIdentification href "../RemoteBiometricIdentification/"
      Capability <|-- RemoteBiometricIdentification
        click Capability href "../Capability/"
      BiometricIdentification <|-- RemoteBiometricIdentification
        click BiometricIdentification href "../BiometricIdentification/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [HumanOrientedCapability](HumanOrientedCapability.md)
            * [BiometricCapability](BiometricCapability.md) [ [Capability](Capability.md)]
                * [BiometricIdentification](BiometricIdentification.md) [ [Capability](Capability.md) [HumanIdentification](HumanIdentification.md)]
                    * **RemoteBiometricIdentification** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:RemoteBiometricIdentification](https://w3id.org/lmodel/dpv/ai/RemoteBiometricIdentification) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Remote Biometric Identification




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#RemoteBiometricIdentification |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:RemoteBiometricIdentification |
| native | ai:RemoteBiometricIdentification |
| exact | dpv_ai:RemoteBiometricIdentification, dpv_ai_owl:RemoteBiometricIdentification |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RemoteBiometricIdentification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#RemoteBiometricIdentification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability involving biometric identification carried out remotely
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Remote Biometric Identification
exact_mappings:
- dpv_ai:RemoteBiometricIdentification
- dpv_ai_owl:RemoteBiometricIdentification
is_a: BiometricIdentification
mixins:
- Capability
class_uri: ai:RemoteBiometricIdentification

```
</details>

### Induced

<details>
```yaml
name: RemoteBiometricIdentification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#RemoteBiometricIdentification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability involving biometric identification carried out remotely
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Remote Biometric Identification
exact_mappings:
- dpv_ai:RemoteBiometricIdentification
- dpv_ai_owl:RemoteBiometricIdentification
is_a: BiometricIdentification
mixins:
- Capability
class_uri: ai:RemoteBiometricIdentification

```
</details></div>