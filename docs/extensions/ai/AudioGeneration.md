---
search:
  boost: 10.0
---

# Class: AudioGeneration 


_Capability to generate audio_



<div data-search-exclude markdown="1">



URI: [ai:AudioGeneration](https://w3id.org/lmodel/dpv/ai/AudioGeneration)





```mermaid
 classDiagram
    class AudioGeneration
    click AudioGeneration href "../AudioGeneration/"
      Capability <|-- AudioGeneration
        click Capability href "../Capability/"
      ContentGeneration <|-- AudioGeneration
        click ContentGeneration href "../ContentGeneration/"
      AudioCapability <|-- AudioGeneration
        click AudioCapability href "../AudioCapability/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [AudioCapability](AudioCapability.md)
            * **AudioGeneration** [ [Capability](Capability.md) [ContentGeneration](ContentGeneration.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:AudioGeneration](https://w3id.org/lmodel/dpv/ai/AudioGeneration) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Audio Generation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#AudioGeneration |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:AudioGeneration |
| native | ai:AudioGeneration |
| exact | dpv_ai:AudioGeneration, dpv_ai_owl:AudioGeneration |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AudioGeneration
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#AudioGeneration
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability to generate audio
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Audio Generation
exact_mappings:
- dpv_ai:AudioGeneration
- dpv_ai_owl:AudioGeneration
is_a: AudioCapability
mixins:
- Capability
- ContentGeneration
class_uri: ai:AudioGeneration

```
</details>

### Induced

<details>
```yaml
name: AudioGeneration
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#AudioGeneration
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability to generate audio
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Audio Generation
exact_mappings:
- dpv_ai:AudioGeneration
- dpv_ai_owl:AudioGeneration
is_a: AudioCapability
mixins:
- Capability
- ContentGeneration
class_uri: ai:AudioGeneration

```
</details></div>