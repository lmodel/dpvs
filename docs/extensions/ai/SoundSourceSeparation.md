---
search:
  boost: 10.0
---

# Class: SoundSourceSeparation 


_Capability for extracting individual sound from audio recordings_



<div data-search-exclude markdown="1">



URI: [ai:SoundSourceSeparation](https://w3id.org/lmodel/dpv/ai/SoundSourceSeparation)





```mermaid
 classDiagram
    class SoundSourceSeparation
    click SoundSourceSeparation href "../SoundSourceSeparation/"
      Capability <|-- SoundSourceSeparation
        click Capability href "../Capability/"
      AudioCapability <|-- SoundSourceSeparation
        click AudioCapability href "../AudioCapability/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [AudioCapability](AudioCapability.md)
            * **SoundSourceSeparation** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:SoundSourceSeparation](https://w3id.org/lmodel/dpv/ai/SoundSourceSeparation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Sound Source Separation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source |  Defining Artificial Intelligence 2.0 |
| upstream_iri | https://w3id.org/dpv/ai/owl#SoundSourceSeparation |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:SoundSourceSeparation |
| native | ai:SoundSourceSeparation |
| exact | dpv_ai:SoundSourceSeparation, dpv_ai_owl:SoundSourceSeparation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SoundSourceSeparation
annotations:
  dct_source:
    tag: dct_source
    value: ' Defining Artificial Intelligence 2.0'
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SoundSourceSeparation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability for extracting individual sound from audio recordings
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Sound Source Separation
exact_mappings:
- dpv_ai:SoundSourceSeparation
- dpv_ai_owl:SoundSourceSeparation
is_a: AudioCapability
mixins:
- Capability
class_uri: ai:SoundSourceSeparation

```
</details>

### Induced

<details>
```yaml
name: SoundSourceSeparation
annotations:
  dct_source:
    tag: dct_source
    value: ' Defining Artificial Intelligence 2.0'
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SoundSourceSeparation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability for extracting individual sound from audio recordings
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Sound Source Separation
exact_mappings:
- dpv_ai:SoundSourceSeparation
- dpv_ai_owl:SoundSourceSeparation
is_a: AudioCapability
mixins:
- Capability
class_uri: ai:SoundSourceSeparation

```
</details></div>