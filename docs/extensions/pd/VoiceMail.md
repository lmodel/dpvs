---
search:
  boost: 10.0
---

# Class: VoiceMail 


_Information about voice mail messages_



<div data-search-exclude markdown="1">



URI: [pd:VoiceMail](https://w3id.org/lmodel/dpv/pd/VoiceMail)





```mermaid
 classDiagram
    class VoiceMail
    click VoiceMail href "../VoiceMail/"
      Communication <|-- VoiceMail
        click Communication href "../Communication/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Communication](Communication.md)
        * **VoiceMail**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:VoiceMail](https://w3id.org/lmodel/dpv/pd/VoiceMail) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Voice Mail




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#VoiceMail |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:VoiceMail |
| native | pd:VoiceMail |
| exact | dpv_pd:VoiceMail, dpv_pd_owl:VoiceMail |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VoiceMail
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#VoiceMail
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about voice mail messages
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Voice Mail
exact_mappings:
- dpv_pd:VoiceMail
- dpv_pd_owl:VoiceMail
is_a: Communication
class_uri: pd:VoiceMail

```
</details>

### Induced

<details>
```yaml
name: VoiceMail
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#VoiceMail
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about voice mail messages
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Voice Mail
exact_mappings:
- dpv_pd:VoiceMail
- dpv_pd_owl:VoiceMail
is_a: Communication
class_uri: pd:VoiceMail

```
</details></div>