---
search:
  boost: 10.0
---

# Class: SpeechSynthesis 


_Capability for generation of artificial speech_



<div data-search-exclude markdown="1">



URI: [ai:SpeechSynthesis](https://w3id.org/lmodel/dpv/ai/SpeechSynthesis)





```mermaid
 classDiagram
    class SpeechSynthesis
    click SpeechSynthesis href "../SpeechSynthesis/"
      Capability <|-- SpeechSynthesis
        click Capability href "../Capability/"
      ContentGeneration <|-- SpeechSynthesis
        click ContentGeneration href "../ContentGeneration/"
      AudioCapability <|-- SpeechSynthesis
        click AudioCapability href "../AudioCapability/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [AudioCapability](AudioCapability.md)
            * **SpeechSynthesis** [ [Capability](Capability.md) [ContentGeneration](ContentGeneration.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:SpeechSynthesis](https://w3id.org/lmodel/dpv/ai/SpeechSynthesis) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Speech Synthesis




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.6.18 |
| upstream_iri | https://w3id.org/dpv/ai/owl#SpeechSynthesis |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:SpeechSynthesis |
| native | ai:SpeechSynthesis |
| exact | dpv_ai:SpeechSynthesis, dpv_ai_owl:SpeechSynthesis |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SpeechSynthesis
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.6.18
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SpeechSynthesis
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability for generation of artificial speech
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Speech Synthesis
exact_mappings:
- dpv_ai:SpeechSynthesis
- dpv_ai_owl:SpeechSynthesis
is_a: AudioCapability
mixins:
- Capability
- ContentGeneration
class_uri: ai:SpeechSynthesis

```
</details>

### Induced

<details>
```yaml
name: SpeechSynthesis
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.6.18
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SpeechSynthesis
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability for generation of artificial speech
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Speech Synthesis
exact_mappings:
- dpv_ai:SpeechSynthesis
- dpv_ai_owl:SpeechSynthesis
is_a: AudioCapability
mixins:
- Capability
- ContentGeneration
class_uri: ai:SpeechSynthesis

```
</details></div>