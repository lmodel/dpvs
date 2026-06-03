---
search:
  boost: 10.0
---

# Class: VideoGeneration 


_Capability to generate video_



<div data-search-exclude markdown="1">



URI: [ai:VideoGeneration](https://w3id.org/lmodel/dpv/ai/VideoGeneration)





```mermaid
 classDiagram
    class VideoGeneration
    click VideoGeneration href "../VideoGeneration/"
      Capability <|-- VideoGeneration
        click Capability href "../Capability/"
      ContentGeneration <|-- VideoGeneration
        click ContentGeneration href "../ContentGeneration/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [ContentGeneration](ContentGeneration.md)
            * **VideoGeneration** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:VideoGeneration](https://w3id.org/lmodel/dpv/ai/VideoGeneration) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Video Generation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#VideoGeneration |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:VideoGeneration |
| native | ai:VideoGeneration |
| exact | dpv_ai:VideoGeneration, dpv_ai_owl:VideoGeneration |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VideoGeneration
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#VideoGeneration
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability to generate video
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Video Generation
exact_mappings:
- dpv_ai:VideoGeneration
- dpv_ai_owl:VideoGeneration
is_a: ContentGeneration
mixins:
- Capability
class_uri: ai:VideoGeneration

```
</details>

### Induced

<details>
```yaml
name: VideoGeneration
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#VideoGeneration
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability to generate video
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Video Generation
exact_mappings:
- dpv_ai:VideoGeneration
- dpv_ai_owl:VideoGeneration
is_a: ContentGeneration
mixins:
- Capability
class_uri: ai:VideoGeneration

```
</details></div>