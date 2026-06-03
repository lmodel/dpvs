---
search:
  boost: 10.0
---

# Class: AudioProcessing 


_Technique involving processing audio_



<div data-search-exclude markdown="1">



URI: [ai:AudioProcessing](https://w3id.org/lmodel/dpv/ai/AudioProcessing)





```mermaid
 classDiagram
    class AudioProcessing
    click AudioProcessing href "../AudioProcessing/"
      Technique <|-- AudioProcessing
        click Technique href "../Technique/"
      

      AudioProcessing <|-- SpeakerRecognition
        click SpeakerRecognition href "../SpeakerRecognition/"
      AudioProcessing <|-- SpeechRecognition
        click SpeechRecognition href "../SpeechRecognition/"
      

      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * **AudioProcessing**
            * [SpeakerRecognition](SpeakerRecognition.md) [ [Capability](Capability.md) [HumanOrientedCapability](HumanOrientedCapability.md)]
            * [SpeechRecognition](SpeechRecognition.md) [ [Capability](Capability.md) [HumanOrientedCapability](HumanOrientedCapability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:AudioProcessing](https://w3id.org/lmodel/dpv/ai/AudioProcessing) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Audio Processing




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#AudioProcessing |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:AudioProcessing |
| native | ai:AudioProcessing |
| exact | dpv_ai:AudioProcessing, dpv_ai_owl:AudioProcessing |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AudioProcessing
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#AudioProcessing
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Technique involving processing audio
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Audio Processing
exact_mappings:
- dpv_ai:AudioProcessing
- dpv_ai_owl:AudioProcessing
is_a: Technique
class_uri: ai:AudioProcessing

```
</details>

### Induced

<details>
```yaml
name: AudioProcessing
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#AudioProcessing
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Technique involving processing audio
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Audio Processing
exact_mappings:
- dpv_ai:AudioProcessing
- dpv_ai_owl:AudioProcessing
is_a: Technique
class_uri: ai:AudioProcessing

```
</details></div>