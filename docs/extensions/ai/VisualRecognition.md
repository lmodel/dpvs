---
search:
  boost: 10.0
---

# Class: VisualRecognition 


_Capability that identifies and categorises objects, scenes, activities,_

_and other visual elements in images or video, and includes image_

_classification, object detection, scene understanding, and visual_

_pattern recognition_



<div data-search-exclude markdown="1">



URI: [ai:VisualRecognition](https://w3id.org/lmodel/dpv/ai/VisualRecognition)





```mermaid
 classDiagram
    class VisualRecognition
    click VisualRecognition href "../VisualRecognition/"
      Capability <|-- VisualRecognition
        click Capability href "../Capability/"
      ComputerVision <|-- VisualRecognition
        click ComputerVision href "../ComputerVision/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [ComputerVision](ComputerVision.md)
            * **VisualRecognition** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:VisualRecognition](https://w3id.org/lmodel/dpv/ai/VisualRecognition) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Visual Recognition




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#VisualRecognition |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:VisualRecognition |
| native | ai:VisualRecognition |
| exact | dpv_ai:VisualRecognition, dpv_ai_owl:VisualRecognition |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VisualRecognition
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#VisualRecognition
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability that identifies and categorises objects, scenes, activities,

  and other visual elements in images or video, and includes image

  classification, object detection, scene understanding, and visual

  pattern recognition'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Visual Recognition
exact_mappings:
- dpv_ai:VisualRecognition
- dpv_ai_owl:VisualRecognition
is_a: ComputerVision
mixins:
- Capability
class_uri: ai:VisualRecognition

```
</details>

### Induced

<details>
```yaml
name: VisualRecognition
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#VisualRecognition
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability that identifies and categorises objects, scenes, activities,

  and other visual elements in images or video, and includes image

  classification, object detection, scene understanding, and visual

  pattern recognition'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Visual Recognition
exact_mappings:
- dpv_ai:VisualRecognition
- dpv_ai_owl:VisualRecognition
is_a: ComputerVision
mixins:
- Capability
class_uri: ai:VisualRecognition

```
</details></div>