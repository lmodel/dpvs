---
search:
  boost: 10.0
---

# Class: NaturalLanguageProcessing 


_Capability enabling computers to understand and communicate with human_

_language_



<div data-search-exclude markdown="1">



URI: [ai:NaturalLanguageProcessing](https://w3id.org/lmodel/dpv/ai/NaturalLanguageProcessing)





```mermaid
 classDiagram
    class NaturalLanguageProcessing
    click NaturalLanguageProcessing href "../NaturalLanguageProcessing/"
      Capability <|-- NaturalLanguageProcessing
        click Capability href "../Capability/"
      LanguageCapability <|-- NaturalLanguageProcessing
        click LanguageCapability href "../LanguageCapability/"
      

      NaturalLanguageProcessing <|-- ChatbotCapability
        click ChatbotCapability href "../ChatbotCapability/"
      NaturalLanguageProcessing <|-- TextClassification
        click TextClassification href "../TextClassification/"
      NaturalLanguageProcessing <|-- TextDataMining
        click TextDataMining href "../TextDataMining/"
      

      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [LanguageCapability](LanguageCapability.md)
            * **NaturalLanguageProcessing** [ [Capability](Capability.md)]
                * [ChatbotCapability](ChatbotCapability.md) [ [Capability](Capability.md)]
                * [TextClassification](TextClassification.md) [ [Capability](Capability.md)]
                * [TextDataMining](TextDataMining.md) [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:NaturalLanguageProcessing](https://w3id.org/lmodel/dpv/ai/NaturalLanguageProcessing) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Natural Language Processing




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#NaturalLanguageProcessing |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:NaturalLanguageProcessing |
| native | ai:NaturalLanguageProcessing |
| exact | dpv_ai:NaturalLanguageProcessing, dpv_ai_owl:NaturalLanguageProcessing |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NaturalLanguageProcessing
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#NaturalLanguageProcessing
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability enabling computers to understand and communicate with human

  language'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Natural Language Processing
exact_mappings:
- dpv_ai:NaturalLanguageProcessing
- dpv_ai_owl:NaturalLanguageProcessing
is_a: LanguageCapability
mixins:
- Capability
class_uri: ai:NaturalLanguageProcessing

```
</details>

### Induced

<details>
```yaml
name: NaturalLanguageProcessing
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#NaturalLanguageProcessing
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability enabling computers to understand and communicate with human

  language'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Natural Language Processing
exact_mappings:
- dpv_ai:NaturalLanguageProcessing
- dpv_ai_owl:NaturalLanguageProcessing
is_a: LanguageCapability
mixins:
- Capability
class_uri: ai:NaturalLanguageProcessing

```
</details></div>