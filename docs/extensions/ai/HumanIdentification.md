---
search:
  boost: 10.0
---

# Class: HumanIdentification 


_Capability of a system that identifies a human whether at an individual_

_or group level_



<div data-search-exclude markdown="1">



URI: [ai:HumanIdentification](https://w3id.org/lmodel/dpv/ai/HumanIdentification)





```mermaid
 classDiagram
    class HumanIdentification
    click HumanIdentification href "../HumanIdentification/"
      Capability <|-- HumanIdentification
        click Capability href "../Capability/"
      HumanOrientedCapability <|-- HumanIdentification
        click HumanOrientedCapability href "../HumanOrientedCapability/"
      

      HumanIdentification <|-- BiometricIdentification
        click BiometricIdentification href "../BiometricIdentification/"
      

      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [HumanOrientedCapability](HumanOrientedCapability.md)
            * **HumanIdentification** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:HumanIdentification](https://w3id.org/lmodel/dpv/ai/HumanIdentification) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Human Identification




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#HumanIdentification |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:HumanIdentification |
| native | ai:HumanIdentification |
| exact | dpv_ai:HumanIdentification, dpv_ai_owl:HumanIdentification |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HumanIdentification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#HumanIdentification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability of a system that identifies a human whether at an individual

  or group level'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Human Identification
exact_mappings:
- dpv_ai:HumanIdentification
- dpv_ai_owl:HumanIdentification
is_a: HumanOrientedCapability
mixins:
- Capability
class_uri: ai:HumanIdentification

```
</details>

### Induced

<details>
```yaml
name: HumanIdentification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#HumanIdentification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability of a system that identifies a human whether at an individual

  or group level'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Human Identification
exact_mappings:
- dpv_ai:HumanIdentification
- dpv_ai_owl:HumanIdentification
is_a: HumanOrientedCapability
mixins:
- Capability
class_uri: ai:HumanIdentification

```
</details></div>