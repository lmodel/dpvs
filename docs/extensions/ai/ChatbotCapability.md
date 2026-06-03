---
search:
  boost: 10.0
---

# Class: ChatbotCapability 


_Capability to simulate human-like conversation with a user through_

_messaging platforms, websites, mobile apps, or telephone systems, often_

_employing natural language processing and machine learning to engage in_

_conversation mimicking human interaction_



<div data-search-exclude markdown="1">



URI: [ai:ChatbotCapability](https://w3id.org/lmodel/dpv/ai/ChatbotCapability)





```mermaid
 classDiagram
    class ChatbotCapability
    click ChatbotCapability href "../ChatbotCapability/"
      Capability <|-- ChatbotCapability
        click Capability href "../Capability/"
      NaturalLanguageProcessing <|-- ChatbotCapability
        click NaturalLanguageProcessing href "../NaturalLanguageProcessing/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [LanguageCapability](LanguageCapability.md)
            * [NaturalLanguageProcessing](NaturalLanguageProcessing.md) [ [Capability](Capability.md)]
                * **ChatbotCapability** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ChatbotCapability](https://w3id.org/lmodel/dpv/ai/ChatbotCapability) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Chatbot Capability




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ChatbotCapability |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ChatbotCapability |
| native | ai:ChatbotCapability |
| exact | dpv_ai:ChatbotCapability, dpv_ai_owl:ChatbotCapability |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ChatbotCapability
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ChatbotCapability
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability to simulate human-like conversation with a user through

  messaging platforms, websites, mobile apps, or telephone systems, often

  employing natural language processing and machine learning to engage in

  conversation mimicking human interaction'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Chatbot Capability
exact_mappings:
- dpv_ai:ChatbotCapability
- dpv_ai_owl:ChatbotCapability
is_a: NaturalLanguageProcessing
mixins:
- Capability
class_uri: ai:ChatbotCapability

```
</details>

### Induced

<details>
```yaml
name: ChatbotCapability
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ChatbotCapability
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability to simulate human-like conversation with a user through

  messaging platforms, websites, mobile apps, or telephone systems, often

  employing natural language processing and machine learning to engage in

  conversation mimicking human interaction'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Chatbot Capability
exact_mappings:
- dpv_ai:ChatbotCapability
- dpv_ai_owl:ChatbotCapability
is_a: NaturalLanguageProcessing
mixins:
- Capability
class_uri: ai:ChatbotCapability

```
</details></div>