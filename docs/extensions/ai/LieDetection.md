---
search:
  boost: 10.0
---

# Class: LieDetection 


_Capability to detect lies in the context of human speech, behaviour,_

_information, or activities_



<div data-search-exclude markdown="1">



URI: [ai:LieDetection](https://w3id.org/lmodel/dpv/ai/LieDetection)





```mermaid
 classDiagram
    class LieDetection
    click LieDetection href "../LieDetection/"
      Capability <|-- LieDetection
        click Capability href "../Capability/"
      HumanOrientedCapability <|-- LieDetection
        click HumanOrientedCapability href "../HumanOrientedCapability/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [HumanOrientedCapability](HumanOrientedCapability.md)
            * **LieDetection** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:LieDetection](https://w3id.org/lmodel/dpv/ai/LieDetection) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Lie Detection




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#LieDetection |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:LieDetection |
| native | ai:LieDetection |
| exact | dpv_ai:LieDetection, dpv_ai_owl:LieDetection |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LieDetection
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#LieDetection
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability to detect lies in the context of human speech, behaviour,

  information, or activities'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Lie Detection
exact_mappings:
- dpv_ai:LieDetection
- dpv_ai_owl:LieDetection
is_a: HumanOrientedCapability
mixins:
- Capability
class_uri: ai:LieDetection

```
</details>

### Induced

<details>
```yaml
name: LieDetection
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#LieDetection
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability to detect lies in the context of human speech, behaviour,

  information, or activities'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Lie Detection
exact_mappings:
- dpv_ai:LieDetection
- dpv_ai_owl:LieDetection
is_a: HumanOrientedCapability
mixins:
- Capability
class_uri: ai:LieDetection

```
</details></div>