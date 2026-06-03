---
search:
  boost: 10.0
---

# Class: SoundSynthesis 


_Capability for generation of artificial sound_



<div data-search-exclude markdown="1">



URI: [ai:SoundSynthesis](https://w3id.org/lmodel/dpv/ai/SoundSynthesis)





```mermaid
 classDiagram
    class SoundSynthesis
    click SoundSynthesis href "../SoundSynthesis/"
      Capability <|-- SoundSynthesis
        click Capability href "../Capability/"
      ContentGeneration <|-- SoundSynthesis
        click ContentGeneration href "../ContentGeneration/"
      AudioCapability <|-- SoundSynthesis
        click AudioCapability href "../AudioCapability/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [AudioCapability](AudioCapability.md)
            * **SoundSynthesis** [ [Capability](Capability.md) [ContentGeneration](ContentGeneration.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:SoundSynthesis](https://w3id.org/lmodel/dpv/ai/SoundSynthesis) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Sound Synthesis




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source |  Defining Artificial Intelligence 2.0 |
| upstream_iri | https://w3id.org/dpv/ai/owl#SoundSynthesis |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:SoundSynthesis |
| native | ai:SoundSynthesis |
| exact | dpv_ai:SoundSynthesis, dpv_ai_owl:SoundSynthesis |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SoundSynthesis
annotations:
  dct_source:
    tag: dct_source
    value: ' Defining Artificial Intelligence 2.0'
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SoundSynthesis
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability for generation of artificial sound
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Sound Synthesis
exact_mappings:
- dpv_ai:SoundSynthesis
- dpv_ai_owl:SoundSynthesis
is_a: AudioCapability
mixins:
- Capability
- ContentGeneration
class_uri: ai:SoundSynthesis

```
</details>

### Induced

<details>
```yaml
name: SoundSynthesis
annotations:
  dct_source:
    tag: dct_source
    value: ' Defining Artificial Intelligence 2.0'
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SoundSynthesis
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability for generation of artificial sound
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Sound Synthesis
exact_mappings:
- dpv_ai:SoundSynthesis
- dpv_ai_owl:SoundSynthesis
is_a: AudioCapability
mixins:
- Capability
- ContentGeneration
class_uri: ai:SoundSynthesis

```
</details></div>