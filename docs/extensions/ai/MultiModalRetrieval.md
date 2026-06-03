---
search:
  boost: 10.0
---

# Class: MultiModalRetrieval 


_Capability for retrieval of information using multiple modalities such_

_as text, images, audio, and video and supporting cross-modal queries_

_such as taking text as input to search images_



<div data-search-exclude markdown="1">



URI: [ai:MultiModalRetrieval](https://w3id.org/lmodel/dpv/ai/MultiModalRetrieval)





```mermaid
 classDiagram
    class MultiModalRetrieval
    click MultiModalRetrieval href "../MultiModalRetrieval/"
      Capability <|-- MultiModalRetrieval
        click Capability href "../Capability/"
      InformationRetrieval <|-- MultiModalRetrieval
        click InformationRetrieval href "../InformationRetrieval/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [InformationRetrieval](InformationRetrieval.md)
            * **MultiModalRetrieval** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:MultiModalRetrieval](https://w3id.org/lmodel/dpv/ai/MultiModalRetrieval) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Multi-modal Retrieval




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#MultiModalRetrieval |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:MultiModalRetrieval |
| native | ai:MultiModalRetrieval |
| exact | dpv_ai:MultiModalRetrieval, dpv_ai_owl:MultiModalRetrieval |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MultiModalRetrieval
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#MultiModalRetrieval
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for retrieval of information using multiple modalities such

  as text, images, audio, and video and supporting cross-modal queries

  such as taking text as input to search images'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Multi-modal Retrieval
exact_mappings:
- dpv_ai:MultiModalRetrieval
- dpv_ai_owl:MultiModalRetrieval
is_a: InformationRetrieval
mixins:
- Capability
class_uri: ai:MultiModalRetrieval

```
</details>

### Induced

<details>
```yaml
name: MultiModalRetrieval
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#MultiModalRetrieval
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for retrieval of information using multiple modalities such

  as text, images, audio, and video and supporting cross-modal queries

  such as taking text as input to search images'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Multi-modal Retrieval
exact_mappings:
- dpv_ai:MultiModalRetrieval
- dpv_ai_owl:MultiModalRetrieval
is_a: InformationRetrieval
mixins:
- Capability
class_uri: ai:MultiModalRetrieval

```
</details></div>