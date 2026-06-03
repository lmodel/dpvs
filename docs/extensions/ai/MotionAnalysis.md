---
search:
  boost: 10.0
---

# Class: MotionAnalysis 


_Capability of deriving meaningful information about motion from visual_

_data, including tracking objects across frames, analysing trajectories,_

_estimating velocity and acceleration, and interpreting the meaning of_

_motion patterns_



<div data-search-exclude markdown="1">



URI: [ai:MotionAnalysis](https://w3id.org/lmodel/dpv/ai/MotionAnalysis)





```mermaid
 classDiagram
    class MotionAnalysis
    click MotionAnalysis href "../MotionAnalysis/"
      Capability <|-- MotionAnalysis
        click Capability href "../Capability/"
      ComputerVision <|-- MotionAnalysis
        click ComputerVision href "../ComputerVision/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [ComputerVision](ComputerVision.md)
            * **MotionAnalysis** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:MotionAnalysis](https://w3id.org/lmodel/dpv/ai/MotionAnalysis) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Motion Analysis




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#MotionAnalysis |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:MotionAnalysis |
| native | ai:MotionAnalysis |
| exact | dpv_ai:MotionAnalysis, dpv_ai_owl:MotionAnalysis |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MotionAnalysis
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#MotionAnalysis
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability of deriving meaningful information about motion from visual

  data, including tracking objects across frames, analysing trajectories,

  estimating velocity and acceleration, and interpreting the meaning of

  motion patterns'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Motion Analysis
exact_mappings:
- dpv_ai:MotionAnalysis
- dpv_ai_owl:MotionAnalysis
is_a: ComputerVision
mixins:
- Capability
class_uri: ai:MotionAnalysis

```
</details>

### Induced

<details>
```yaml
name: MotionAnalysis
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#MotionAnalysis
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability of deriving meaningful information about motion from visual

  data, including tracking objects across frames, analysing trajectories,

  estimating velocity and acceleration, and interpreting the meaning of

  motion patterns'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Motion Analysis
exact_mappings:
- dpv_ai:MotionAnalysis
- dpv_ai_owl:MotionAnalysis
is_a: ComputerVision
mixins:
- Capability
class_uri: ai:MotionAnalysis

```
</details></div>