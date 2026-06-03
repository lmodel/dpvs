---
search:
  boost: 10.0
---

# Class: TextDataMining 


_Capability of selecting and analysing large amounts of text or data_

_resources to discover patterns, relationships, and semantic insights_

_that provide valuable information for research and decision-making_



<div data-search-exclude markdown="1">



URI: [ai:TextDataMining](https://w3id.org/lmodel/dpv/ai/TextDataMining)





```mermaid
 classDiagram
    class TextDataMining
    click TextDataMining href "../TextDataMining/"
      Capability <|-- TextDataMining
        click Capability href "../Capability/"
      NaturalLanguageProcessing <|-- TextDataMining
        click NaturalLanguageProcessing href "../NaturalLanguageProcessing/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [LanguageCapability](LanguageCapability.md)
            * [NaturalLanguageProcessing](NaturalLanguageProcessing.md) [ [Capability](Capability.md)]
                * **TextDataMining** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:TextDataMining](https://w3id.org/lmodel/dpv/ai/TextDataMining) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Text and Data Mining




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#TextDataMining |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:TextDataMining |
| native | ai:TextDataMining |
| exact | dpv_ai:TextDataMining, dpv_ai_owl:TextDataMining |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TextDataMining
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TextDataMining
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability of selecting and analysing large amounts of text or data

  resources to discover patterns, relationships, and semantic insights

  that provide valuable information for research and decision-making'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Text and Data Mining
exact_mappings:
- dpv_ai:TextDataMining
- dpv_ai_owl:TextDataMining
is_a: NaturalLanguageProcessing
mixins:
- Capability
class_uri: ai:TextDataMining

```
</details>

### Induced

<details>
```yaml
name: TextDataMining
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TextDataMining
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability of selecting and analysing large amounts of text or data

  resources to discover patterns, relationships, and semantic insights

  that provide valuable information for research and decision-making'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Text and Data Mining
exact_mappings:
- dpv_ai:TextDataMining
- dpv_ai_owl:TextDataMining
is_a: NaturalLanguageProcessing
mixins:
- Capability
class_uri: ai:TextDataMining

```
</details></div>