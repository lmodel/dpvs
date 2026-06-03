---
search:
  boost: 10.0
---

# Class: LocalBiometricIdentification 


_Capability involving biometric identification carried out locally_



<div data-search-exclude markdown="1">



URI: [ai:LocalBiometricIdentification](https://w3id.org/lmodel/dpv/ai/LocalBiometricIdentification)





```mermaid
 classDiagram
    class LocalBiometricIdentification
    click LocalBiometricIdentification href "../LocalBiometricIdentification/"
      Capability <|-- LocalBiometricIdentification
        click Capability href "../Capability/"
      BiometricIdentification <|-- LocalBiometricIdentification
        click BiometricIdentification href "../BiometricIdentification/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [HumanOrientedCapability](HumanOrientedCapability.md)
            * [BiometricCapability](BiometricCapability.md) [ [Capability](Capability.md)]
                * [BiometricIdentification](BiometricIdentification.md) [ [Capability](Capability.md) [HumanIdentification](HumanIdentification.md)]
                    * **LocalBiometricIdentification** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:LocalBiometricIdentification](https://w3id.org/lmodel/dpv/ai/LocalBiometricIdentification) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Local Biometric Identification




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#LocalBiometricIdentification |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:LocalBiometricIdentification |
| native | ai:LocalBiometricIdentification |
| exact | dpv_ai:LocalBiometricIdentification, dpv_ai_owl:LocalBiometricIdentification |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LocalBiometricIdentification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#LocalBiometricIdentification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability involving biometric identification carried out locally
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Local Biometric Identification
exact_mappings:
- dpv_ai:LocalBiometricIdentification
- dpv_ai_owl:LocalBiometricIdentification
is_a: BiometricIdentification
mixins:
- Capability
class_uri: ai:LocalBiometricIdentification

```
</details>

### Induced

<details>
```yaml
name: LocalBiometricIdentification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#LocalBiometricIdentification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability involving biometric identification carried out locally
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Local Biometric Identification
exact_mappings:
- dpv_ai:LocalBiometricIdentification
- dpv_ai_owl:LocalBiometricIdentification
is_a: BiometricIdentification
mixins:
- Capability
class_uri: ai:LocalBiometricIdentification

```
</details></div>