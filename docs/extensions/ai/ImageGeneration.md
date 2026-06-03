---
search:
  boost: 10.0
---

# Class: ImageGeneration 


_Capability to generate image_



<div data-search-exclude markdown="1">



URI: [ai:ImageGeneration](https://w3id.org/lmodel/dpv/ai/ImageGeneration)





```mermaid
 classDiagram
    class ImageGeneration
    click ImageGeneration href "../ImageGeneration/"
      Capability <|-- ImageGeneration
        click Capability href "../Capability/"
      ContentGeneration <|-- ImageGeneration
        click ContentGeneration href "../ContentGeneration/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [ContentGeneration](ContentGeneration.md)
            * **ImageGeneration** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ImageGeneration](https://w3id.org/lmodel/dpv/ai/ImageGeneration) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Image Generation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ImageGeneration |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ImageGeneration |
| native | ai:ImageGeneration |
| exact | dpv_ai:ImageGeneration, dpv_ai_owl:ImageGeneration |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ImageGeneration
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ImageGeneration
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability to generate image
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Image Generation
exact_mappings:
- dpv_ai:ImageGeneration
- dpv_ai_owl:ImageGeneration
is_a: ContentGeneration
mixins:
- Capability
class_uri: ai:ImageGeneration

```
</details>

### Induced

<details>
```yaml
name: ImageGeneration
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ImageGeneration
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability to generate image
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Image Generation
exact_mappings:
- dpv_ai:ImageGeneration
- dpv_ai_owl:ImageGeneration
is_a: ContentGeneration
mixins:
- Capability
class_uri: ai:ImageGeneration

```
</details></div>