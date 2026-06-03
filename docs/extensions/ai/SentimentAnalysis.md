---
search:
  boost: 10.0
---

# Class: SentimentAnalysis 


_Capability for computationally identifying and categorising opinions_

_expressed in a piece of text, speech or image, to determine a range of_

_feeling such as from positive to negative_



<div data-search-exclude markdown="1">



URI: [ai:SentimentAnalysis](https://w3id.org/lmodel/dpv/ai/SentimentAnalysis)





```mermaid
 classDiagram
    class SentimentAnalysis
    click SentimentAnalysis href "../SentimentAnalysis/"
      Capability <|-- SentimentAnalysis
        click Capability href "../Capability/"
      LanguageCapability <|-- SentimentAnalysis
        click LanguageCapability href "../LanguageCapability/"
      HumanOrientedCapability <|-- SentimentAnalysis
        click HumanOrientedCapability href "../HumanOrientedCapability/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [HumanOrientedCapability](HumanOrientedCapability.md)
            * **SentimentAnalysis** [ [Capability](Capability.md) [LanguageCapability](LanguageCapability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:SentimentAnalysis](https://w3id.org/lmodel/dpv/ai/SentimentAnalysis) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Sentiment Analysis




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.6.16 |
| upstream_iri | https://w3id.org/dpv/ai/owl#SentimentAnalysis |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:SentimentAnalysis |
| native | ai:SentimentAnalysis |
| exact | dpv_ai:SentimentAnalysis, dpv_ai_owl:SentimentAnalysis |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SentimentAnalysis
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.6.16
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SentimentAnalysis
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for computationally identifying and categorising opinions

  expressed in a piece of text, speech or image, to determine a range of

  feeling such as from positive to negative'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Sentiment Analysis
exact_mappings:
- dpv_ai:SentimentAnalysis
- dpv_ai_owl:SentimentAnalysis
is_a: HumanOrientedCapability
mixins:
- Capability
- LanguageCapability
class_uri: ai:SentimentAnalysis

```
</details>

### Induced

<details>
```yaml
name: SentimentAnalysis
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.6.16
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SentimentAnalysis
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for computationally identifying and categorising opinions

  expressed in a piece of text, speech or image, to determine a range of

  feeling such as from positive to negative'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Sentiment Analysis
exact_mappings:
- dpv_ai:SentimentAnalysis
- dpv_ai_owl:SentimentAnalysis
is_a: HumanOrientedCapability
mixins:
- Capability
- LanguageCapability
class_uri: ai:SentimentAnalysis

```
</details></div>