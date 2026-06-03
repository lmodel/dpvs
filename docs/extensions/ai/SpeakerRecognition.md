---
search:
  boost: 10.0
---

# Class: SpeakerRecognition 


_Capability of recognising speaker(s) in audio recordings_



<div data-search-exclude markdown="1">



URI: [ai:SpeakerRecognition](https://w3id.org/lmodel/dpv/ai/SpeakerRecognition)





```mermaid
 classDiagram
    class SpeakerRecognition
    click SpeakerRecognition href "../SpeakerRecognition/"
      Capability <|-- SpeakerRecognition
        click Capability href "../Capability/"
      HumanOrientedCapability <|-- SpeakerRecognition
        click HumanOrientedCapability href "../HumanOrientedCapability/"
      AudioProcessing <|-- SpeakerRecognition
        click AudioProcessing href "../AudioProcessing/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [AudioProcessing](AudioProcessing.md)
            * **SpeakerRecognition** [ [Capability](Capability.md) [HumanOrientedCapability](HumanOrientedCapability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:SpeakerRecognition](https://w3id.org/lmodel/dpv/ai/SpeakerRecognition) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Speaker Recognition




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source |  Defining Artificial Intelligence 2.0 |
| upstream_iri | https://w3id.org/dpv/ai/owl#SpeakerRecognition |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:SpeakerRecognition |
| native | ai:SpeakerRecognition |
| exact | dpv_ai:SpeakerRecognition, dpv_ai_owl:SpeakerRecognition |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SpeakerRecognition
annotations:
  dct_source:
    tag: dct_source
    value: ' Defining Artificial Intelligence 2.0'
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SpeakerRecognition
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability of recognising speaker(s) in audio recordings
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Speaker Recognition
exact_mappings:
- dpv_ai:SpeakerRecognition
- dpv_ai_owl:SpeakerRecognition
is_a: AudioProcessing
mixins:
- Capability
- HumanOrientedCapability
class_uri: ai:SpeakerRecognition

```
</details>

### Induced

<details>
```yaml
name: SpeakerRecognition
annotations:
  dct_source:
    tag: dct_source
    value: ' Defining Artificial Intelligence 2.0'
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SpeakerRecognition
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability of recognising speaker(s) in audio recordings
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Speaker Recognition
exact_mappings:
- dpv_ai:SpeakerRecognition
- dpv_ai_owl:SpeakerRecognition
is_a: AudioProcessing
mixins:
- Capability
- HumanOrientedCapability
class_uri: ai:SpeakerRecognition

```
</details></div>