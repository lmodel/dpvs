---
search:
  boost: 10.0
---

# Class: LanguageCapability 


_Capabilities related to languages_



<div data-search-exclude markdown="1">



URI: [ai:LanguageCapability](https://w3id.org/lmodel/dpv/ai/LanguageCapability)





```mermaid
 classDiagram
    class LanguageCapability
    click LanguageCapability href "../LanguageCapability/"
      Capability <|-- LanguageCapability
        click Capability href "../Capability/"
      

      LanguageCapability <|-- AutomaticSummarisation
        click AutomaticSummarisation href "../AutomaticSummarisation/"
      LanguageCapability <|-- DialogueManagement
        click DialogueManagement href "../DialogueManagement/"
      LanguageCapability <|-- MachineTranslation
        click MachineTranslation href "../MachineTranslation/"
      LanguageCapability <|-- NamedEntityRecognition
        click NamedEntityRecognition href "../NamedEntityRecognition/"
      LanguageCapability <|-- NaturalLanguageGeneration
        click NaturalLanguageGeneration href "../NaturalLanguageGeneration/"
      LanguageCapability <|-- NaturalLanguageProcessing
        click NaturalLanguageProcessing href "../NaturalLanguageProcessing/"
      LanguageCapability <|-- PartOfSpeechTagging
        click PartOfSpeechTagging href "../PartOfSpeechTagging/"
      LanguageCapability <|-- QuestionAnswering
        click QuestionAnswering href "../QuestionAnswering/"
      LanguageCapability <|-- RelationshipExtraction
        click RelationshipExtraction href "../RelationshipExtraction/"
      LanguageCapability <|-- SentimentAnalysis
        click SentimentAnalysis href "../SentimentAnalysis/"
      

      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * **LanguageCapability**
            * [DialogueManagement](DialogueManagement.md) [ [Capability](Capability.md)]
            * [MachineTranslation](MachineTranslation.md) [ [Capability](Capability.md)]
            * [NamedEntityRecognition](NamedEntityRecognition.md) [ [Capability](Capability.md)]
            * [NaturalLanguageGeneration](NaturalLanguageGeneration.md) [ [Capability](Capability.md)]
            * [NaturalLanguageProcessing](NaturalLanguageProcessing.md) [ [Capability](Capability.md)]
            * [PartOfSpeechTagging](PartOfSpeechTagging.md) [ [Capability](Capability.md)]
            * [QuestionAnswering](QuestionAnswering.md) [ [Capability](Capability.md)]
            * [RelationshipExtraction](RelationshipExtraction.md) [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:LanguageCapability](https://w3id.org/lmodel/dpv/ai/LanguageCapability) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Language Capability




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#LanguageCapability |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:LanguageCapability |
| native | ai:LanguageCapability |
| exact | dpv_ai:LanguageCapability, dpv_ai_owl:LanguageCapability |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LanguageCapability
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#LanguageCapability
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capabilities related to languages
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Language Capability
exact_mappings:
- dpv_ai:LanguageCapability
- dpv_ai_owl:LanguageCapability
is_a: Capability
class_uri: ai:LanguageCapability

```
</details>

### Induced

<details>
```yaml
name: LanguageCapability
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#LanguageCapability
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capabilities related to languages
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Language Capability
exact_mappings:
- dpv_ai:LanguageCapability
- dpv_ai_owl:LanguageCapability
is_a: Capability
class_uri: ai:LanguageCapability

```
</details></div>