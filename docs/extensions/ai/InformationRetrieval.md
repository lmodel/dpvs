---
search:
  boost: 10.0
---

# Class: InformationRetrieval 


_Capability for retrieving relevant documents or parts of documents from_

_a dataset, typically based on keyword or natural language queries_



<div data-search-exclude markdown="1">



URI: [ai:InformationRetrieval](https://w3id.org/lmodel/dpv/ai/InformationRetrieval)





```mermaid
 classDiagram
    class InformationRetrieval
    click InformationRetrieval href "../InformationRetrieval/"
      Capability <|-- InformationRetrieval
        click Capability href "../Capability/"
      

      InformationRetrieval <|-- AutomaticSummarisation
        click AutomaticSummarisation href "../AutomaticSummarisation/"
      InformationRetrieval <|-- ContentBasedRetrieval
        click ContentBasedRetrieval href "../ContentBasedRetrieval/"
      InformationRetrieval <|-- ContextAwareRetrieval
        click ContextAwareRetrieval href "../ContextAwareRetrieval/"
      InformationRetrieval <|-- MultiModalRetrieval
        click MultiModalRetrieval href "../MultiModalRetrieval/"
      InformationRetrieval <|-- MusicInformationRetrieval
        click MusicInformationRetrieval href "../MusicInformationRetrieval/"
      

      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * **InformationRetrieval**
            * [AutomaticSummarisation](AutomaticSummarisation.md) [ [Capability](Capability.md) [LanguageCapability](LanguageCapability.md)]
            * [ContentBasedRetrieval](ContentBasedRetrieval.md) [ [Capability](Capability.md)]
            * [ContextAwareRetrieval](ContextAwareRetrieval.md) [ [Capability](Capability.md)]
            * [MultiModalRetrieval](MultiModalRetrieval.md) [ [Capability](Capability.md)]
            * [MusicInformationRetrieval](MusicInformationRetrieval.md) [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:InformationRetrieval](https://w3id.org/lmodel/dpv/ai/InformationRetrieval) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Information Retrieval (IR)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.6.4 |
| upstream_iri | https://w3id.org/dpv/ai/owl#InformationRetrieval |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:InformationRetrieval |
| native | ai:InformationRetrieval |
| exact | dpv_ai:InformationRetrieval, dpv_ai_owl:InformationRetrieval |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InformationRetrieval
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.6.4
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InformationRetrieval
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for retrieving relevant documents or parts of documents from

  a dataset, typically based on keyword or natural language queries'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Information Retrieval (IR)
exact_mappings:
- dpv_ai:InformationRetrieval
- dpv_ai_owl:InformationRetrieval
is_a: Capability
class_uri: ai:InformationRetrieval

```
</details>

### Induced

<details>
```yaml
name: InformationRetrieval
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.6.4
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InformationRetrieval
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for retrieving relevant documents or parts of documents from

  a dataset, typically based on keyword or natural language queries'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Information Retrieval (IR)
exact_mappings:
- dpv_ai:InformationRetrieval
- dpv_ai_owl:InformationRetrieval
is_a: Capability
class_uri: ai:InformationRetrieval

```
</details></div>