---
search:
  boost: 10.0
---

# Class: ActionRecognition 


_Capability to recognise actions_



<div data-search-exclude markdown="1">



URI: [ai:ActionRecognition](https://w3id.org/lmodel/dpv/ai/ActionRecognition)





```mermaid
 classDiagram
    class ActionRecognition
    click ActionRecognition href "../ActionRecognition/"
      Capability <|-- ActionRecognition
        click Capability href "../Capability/"
      ComputerVision <|-- ActionRecognition
        click ComputerVision href "../ComputerVision/"
      BiometricCapability <|-- ActionRecognition
        click BiometricCapability href "../BiometricCapability/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [HumanOrientedCapability](HumanOrientedCapability.md)
            * [BiometricCapability](BiometricCapability.md) [ [Capability](Capability.md)]
                * **ActionRecognition** [ [Capability](Capability.md) [ComputerVision](ComputerVision.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ActionRecognition](https://w3id.org/lmodel/dpv/ai/ActionRecognition) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Action Recognition




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source |  Defining Artificial Intelligence 2.0 |
| upstream_iri | https://w3id.org/dpv/ai/owl#ActionRecognition |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ActionRecognition |
| native | ai:ActionRecognition |
| exact | dpv_ai:ActionRecognition, dpv_ai_owl:ActionRecognition |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ActionRecognition
annotations:
  dct_source:
    tag: dct_source
    value: ' Defining Artificial Intelligence 2.0'
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ActionRecognition
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability to recognise actions
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Action Recognition
exact_mappings:
- dpv_ai:ActionRecognition
- dpv_ai_owl:ActionRecognition
is_a: BiometricCapability
mixins:
- Capability
- ComputerVision
class_uri: ai:ActionRecognition

```
</details>

### Induced

<details>
```yaml
name: ActionRecognition
annotations:
  dct_source:
    tag: dct_source
    value: ' Defining Artificial Intelligence 2.0'
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ActionRecognition
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability to recognise actions
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Action Recognition
exact_mappings:
- dpv_ai:ActionRecognition
- dpv_ai_owl:ActionRecognition
is_a: BiometricCapability
mixins:
- Capability
- ComputerVision
class_uri: ai:ActionRecognition

```
</details></div>