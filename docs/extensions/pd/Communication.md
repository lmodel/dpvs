---
search:
  boost: 10.0
---

# Class: Communication 


_Information communicated from or to an individual_



<div data-search-exclude markdown="1">



URI: [pd:Communication](https://w3id.org/lmodel/dpv/pd/Communication)





```mermaid
 classDiagram
    class Communication
    click Communication href "../Communication/"
      Social <|-- Communication
        click Social href "../Social/"
      

      Communication <|-- EmailContent
        click EmailContent href "../EmailContent/"
      Communication <|-- SocialMedia
        click SocialMedia href "../SocialMedia/"
      Communication <|-- SocialMediaCommunication
        click SocialMediaCommunication href "../SocialMediaCommunication/"
      Communication <|-- VoiceCommunicationRecording
        click VoiceCommunicationRecording href "../VoiceCommunicationRecording/"
      Communication <|-- VoiceMail
        click VoiceMail href "../VoiceMail/"
      

      
```





## Inheritance
* [Social](Social.md)
    * **Communication**
        * [EmailContent](EmailContent.md)
        * [SocialMedia](SocialMedia.md)
        * [SocialMediaCommunication](SocialMediaCommunication.md)
        * [VoiceCommunicationRecording](VoiceCommunicationRecording.md)
        * [VoiceMail](VoiceMail.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Communication](https://w3id.org/lmodel/dpv/pd/Communication) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Communication




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Communication |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Communication |
| native | pd:Communication |
| exact | dpv_pd:Communication, dpv_pd_owl:Communication |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Communication
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Communication
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information communicated from or to an individual
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Communication
exact_mappings:
- dpv_pd:Communication
- dpv_pd_owl:Communication
is_a: Social
class_uri: pd:Communication

```
</details>

### Induced

<details>
```yaml
name: Communication
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Communication
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information communicated from or to an individual
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Communication
exact_mappings:
- dpv_pd:Communication
- dpv_pd_owl:Communication
is_a: Social
class_uri: pd:Communication

```
</details></div>