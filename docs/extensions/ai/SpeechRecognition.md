---
search:
  boost: 10.0
---

# Class: SpeechRecognition 


_Capability of converting a speech signal to a representation of the_

_content of the speech_



<div data-search-exclude markdown="1">



URI: [ai:SpeechRecognition](https://w3id.org/lmodel/dpv/ai/SpeechRecognition)





```mermaid
 classDiagram
    class SpeechRecognition
    click SpeechRecognition href "../SpeechRecognition/"
      Capability <|-- SpeechRecognition
        click Capability href "../Capability/"
      HumanOrientedCapability <|-- SpeechRecognition
        click HumanOrientedCapability href "../HumanOrientedCapability/"
      AudioProcessing <|-- SpeechRecognition
        click AudioProcessing href "../AudioProcessing/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [AudioProcessing](AudioProcessing.md)
            * **SpeechRecognition** [ [Capability](Capability.md) [HumanOrientedCapability](HumanOrientedCapability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:SpeechRecognition](https://w3id.org/lmodel/dpv/ai/SpeechRecognition) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Speech Recognition




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.6.17 |
| upstream_iri | https://w3id.org/dpv/ai/owl#SpeechRecognition |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:SpeechRecognition |
| native | ai:SpeechRecognition |
| exact | dpv_ai:SpeechRecognition, dpv_ai_owl:SpeechRecognition |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SpeechRecognition
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.6.17
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SpeechRecognition
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability of converting a speech signal to a representation of the

  content of the speech'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Speech Recognition
exact_mappings:
- dpv_ai:SpeechRecognition
- dpv_ai_owl:SpeechRecognition
is_a: AudioProcessing
mixins:
- Capability
- HumanOrientedCapability
class_uri: ai:SpeechRecognition

```
</details>

### Induced

<details>
```yaml
name: SpeechRecognition
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.6.17
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SpeechRecognition
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability of converting a speech signal to a representation of the

  content of the speech'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Speech Recognition
exact_mappings:
- dpv_ai:SpeechRecognition
- dpv_ai_owl:SpeechRecognition
is_a: AudioProcessing
mixins:
- Capability
- HumanOrientedCapability
class_uri: ai:SpeechRecognition

```
</details></div>