---
search:
  boost: 10.0
---

# Class: ObjectRecognition 


_Capability to recognise objects_



<div data-search-exclude markdown="1">



URI: [ai:ObjectRecognition](https://w3id.org/lmodel/dpv/ai/ObjectRecognition)





```mermaid
 classDiagram
    class ObjectRecognition
    click ObjectRecognition href "../ObjectRecognition/"
      Capability <|-- ObjectRecognition
        click Capability href "../Capability/"
      ComputerVision <|-- ObjectRecognition
        click ComputerVision href "../ComputerVision/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [ComputerVision](ComputerVision.md)
            * **ObjectRecognition** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ObjectRecognition](https://w3id.org/lmodel/dpv/ai/ObjectRecognition) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Object Recognition




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source |  Defining Artificial Intelligence 2.0 |
| upstream_iri | https://w3id.org/dpv/ai/owl#ObjectRecognition |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ObjectRecognition |
| native | ai:ObjectRecognition |
| exact | dpv_ai:ObjectRecognition, dpv_ai_owl:ObjectRecognition |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ObjectRecognition
annotations:
  dct_source:
    tag: dct_source
    value: ' Defining Artificial Intelligence 2.0'
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ObjectRecognition
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability to recognise objects
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Object Recognition
exact_mappings:
- dpv_ai:ObjectRecognition
- dpv_ai_owl:ObjectRecognition
is_a: ComputerVision
mixins:
- Capability
class_uri: ai:ObjectRecognition

```
</details>

### Induced

<details>
```yaml
name: ObjectRecognition
annotations:
  dct_source:
    tag: dct_source
    value: ' Defining Artificial Intelligence 2.0'
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ObjectRecognition
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability to recognise objects
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Object Recognition
exact_mappings:
- dpv_ai:ObjectRecognition
- dpv_ai_owl:ObjectRecognition
is_a: ComputerVision
mixins:
- Capability
class_uri: ai:ObjectRecognition

```
</details></div>