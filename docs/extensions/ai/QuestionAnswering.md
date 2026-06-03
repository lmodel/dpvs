---
search:
  boost: 10.0
---

# Class: QuestionAnswering 


_Capability for determining the most appropriate answer to a question_

_provided in natural language_



<div data-search-exclude markdown="1">



URI: [ai:QuestionAnswering](https://w3id.org/lmodel/dpv/ai/QuestionAnswering)





```mermaid
 classDiagram
    class QuestionAnswering
    click QuestionAnswering href "../QuestionAnswering/"
      Capability <|-- QuestionAnswering
        click Capability href "../Capability/"
      LanguageCapability <|-- QuestionAnswering
        click LanguageCapability href "../LanguageCapability/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [LanguageCapability](LanguageCapability.md)
            * **QuestionAnswering** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:QuestionAnswering](https://w3id.org/lmodel/dpv/ai/QuestionAnswering) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Question Answering




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.6.14 |
| upstream_iri | https://w3id.org/dpv/ai/owl#QuestionAnswering |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:QuestionAnswering |
| native | ai:QuestionAnswering |
| exact | dpv_ai:QuestionAnswering, dpv_ai_owl:QuestionAnswering |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: QuestionAnswering
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.6.14
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#QuestionAnswering
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for determining the most appropriate answer to a question

  provided in natural language'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Question Answering
exact_mappings:
- dpv_ai:QuestionAnswering
- dpv_ai_owl:QuestionAnswering
is_a: LanguageCapability
mixins:
- Capability
class_uri: ai:QuestionAnswering

```
</details>

### Induced

<details>
```yaml
name: QuestionAnswering
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.6.14
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#QuestionAnswering
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for determining the most appropriate answer to a question

  provided in natural language'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Question Answering
exact_mappings:
- dpv_ai:QuestionAnswering
- dpv_ai_owl:QuestionAnswering
is_a: LanguageCapability
mixins:
- Capability
class_uri: ai:QuestionAnswering

```
</details></div>