---
search:
  boost: 10.0
---

# Class: MusicInformationRetrieval 


_Capability for retrieving, analysing, and categorising music-related_

_information such as audio files, melodies, or lyrics using audio_

_features, metadata, and user queries_



<div data-search-exclude markdown="1">



URI: [ai:MusicInformationRetrieval](https://w3id.org/lmodel/dpv/ai/MusicInformationRetrieval)





```mermaid
 classDiagram
    class MusicInformationRetrieval
    click MusicInformationRetrieval href "../MusicInformationRetrieval/"
      Capability <|-- MusicInformationRetrieval
        click Capability href "../Capability/"
      InformationRetrieval <|-- MusicInformationRetrieval
        click InformationRetrieval href "../InformationRetrieval/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [InformationRetrieval](InformationRetrieval.md)
            * **MusicInformationRetrieval** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:MusicInformationRetrieval](https://w3id.org/lmodel/dpv/ai/MusicInformationRetrieval) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Music Information Retrieval (MIR)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source |  Defining Artificial Intelligence 2.0 |
| upstream_iri | https://w3id.org/dpv/ai/owl#MusicInformationRetrieval |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:MusicInformationRetrieval |
| native | ai:MusicInformationRetrieval |
| exact | dpv_ai:MusicInformationRetrieval, dpv_ai_owl:MusicInformationRetrieval |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MusicInformationRetrieval
annotations:
  dct_source:
    tag: dct_source
    value: ' Defining Artificial Intelligence 2.0'
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#MusicInformationRetrieval
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for retrieving, analysing, and categorising music-related

  information such as audio files, melodies, or lyrics using audio

  features, metadata, and user queries'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Music Information Retrieval (MIR)
exact_mappings:
- dpv_ai:MusicInformationRetrieval
- dpv_ai_owl:MusicInformationRetrieval
is_a: InformationRetrieval
mixins:
- Capability
class_uri: ai:MusicInformationRetrieval

```
</details>

### Induced

<details>
```yaml
name: MusicInformationRetrieval
annotations:
  dct_source:
    tag: dct_source
    value: ' Defining Artificial Intelligence 2.0'
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#MusicInformationRetrieval
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for retrieving, analysing, and categorising music-related

  information such as audio files, melodies, or lyrics using audio

  features, metadata, and user queries'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Music Information Retrieval (MIR)
exact_mappings:
- dpv_ai:MusicInformationRetrieval
- dpv_ai_owl:MusicInformationRetrieval
is_a: InformationRetrieval
mixins:
- Capability
class_uri: ai:MusicInformationRetrieval

```
</details></div>