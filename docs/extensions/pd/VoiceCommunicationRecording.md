---
search:
  boost: 10.0
---

# Class: VoiceCommunicationRecording 


_Information about vocal recorded communication (e.g. telephony, VoIP)_



<div data-search-exclude markdown="1">



URI: [pd:VoiceCommunicationRecording](https://w3id.org/lmodel/dpv/pd/VoiceCommunicationRecording)





```mermaid
 classDiagram
    class VoiceCommunicationRecording
    click VoiceCommunicationRecording href "../VoiceCommunicationRecording/"
      Communication <|-- VoiceCommunicationRecording
        click Communication href "../Communication/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Communication](Communication.md)
        * **VoiceCommunicationRecording**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:VoiceCommunicationRecording](https://w3id.org/lmodel/dpv/pd/VoiceCommunicationRecording) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Voice Communication Recording




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#VoiceCommunicationRecording |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:VoiceCommunicationRecording |
| native | pd:VoiceCommunicationRecording |
| exact | dpv_pd:VoiceCommunicationRecording, dpv_pd_owl:VoiceCommunicationRecording |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VoiceCommunicationRecording
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#VoiceCommunicationRecording
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about vocal recorded communication (e.g. telephony, VoIP)
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Voice Communication Recording
exact_mappings:
- dpv_pd:VoiceCommunicationRecording
- dpv_pd_owl:VoiceCommunicationRecording
is_a: Communication
class_uri: pd:VoiceCommunicationRecording

```
</details>

### Induced

<details>
```yaml
name: VoiceCommunicationRecording
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#VoiceCommunicationRecording
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about vocal recorded communication (e.g. telephony, VoIP)
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Voice Communication Recording
exact_mappings:
- dpv_pd:VoiceCommunicationRecording
- dpv_pd_owl:VoiceCommunicationRecording
is_a: Communication
class_uri: pd:VoiceCommunicationRecording

```
</details></div>