---
search:
  boost: 10.0
---

# Class: NamedEntityRecognition 


_Capability for recognising and labelling the denotational names of_

_entities and their categories for sequences of words in a stream of text_

_or speech_



<div data-search-exclude markdown="1">



URI: [ai:NamedEntityRecognition](https://w3id.org/lmodel/dpv/ai/NamedEntityRecognition)





```mermaid
 classDiagram
    class NamedEntityRecognition
    click NamedEntityRecognition href "../NamedEntityRecognition/"
      Capability <|-- NamedEntityRecognition
        click Capability href "../Capability/"
      LanguageCapability <|-- NamedEntityRecognition
        click LanguageCapability href "../LanguageCapability/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [LanguageCapability](LanguageCapability.md)
            * **NamedEntityRecognition** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:NamedEntityRecognition](https://w3id.org/lmodel/dpv/ai/NamedEntityRecognition) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Named Entity Recognition




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.6.6 |
| upstream_iri | https://w3id.org/dpv/ai/owl#NamedEntityRecognition |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:NamedEntityRecognition |
| native | ai:NamedEntityRecognition |
| exact | dpv_ai:NamedEntityRecognition, dpv_ai_owl:NamedEntityRecognition |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NamedEntityRecognition
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.6.6
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#NamedEntityRecognition
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for recognising and labelling the denotational names of

  entities and their categories for sequences of words in a stream of text

  or speech'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Named Entity Recognition
exact_mappings:
- dpv_ai:NamedEntityRecognition
- dpv_ai_owl:NamedEntityRecognition
is_a: LanguageCapability
mixins:
- Capability
class_uri: ai:NamedEntityRecognition

```
</details>

### Induced

<details>
```yaml
name: NamedEntityRecognition
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.6.6
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#NamedEntityRecognition
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for recognising and labelling the denotational names of

  entities and their categories for sequences of words in a stream of text

  or speech'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Named Entity Recognition
exact_mappings:
- dpv_ai:NamedEntityRecognition
- dpv_ai_owl:NamedEntityRecognition
is_a: LanguageCapability
mixins:
- Capability
class_uri: ai:NamedEntityRecognition

```
</details></div>