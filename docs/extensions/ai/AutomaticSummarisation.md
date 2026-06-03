---
search:
  boost: 10.0
---

# Class: AutomaticSummarisation 


_Capability for shortening a portion of content such as text while_

_retaining important semantic information_



<div data-search-exclude markdown="1">



URI: [ai:AutomaticSummarisation](https://w3id.org/lmodel/dpv/ai/AutomaticSummarisation)





```mermaid
 classDiagram
    class AutomaticSummarisation
    click AutomaticSummarisation href "../AutomaticSummarisation/"
      Capability <|-- AutomaticSummarisation
        click Capability href "../Capability/"
      LanguageCapability <|-- AutomaticSummarisation
        click LanguageCapability href "../LanguageCapability/"
      InformationRetrieval <|-- AutomaticSummarisation
        click InformationRetrieval href "../InformationRetrieval/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [InformationRetrieval](InformationRetrieval.md)
            * **AutomaticSummarisation** [ [Capability](Capability.md) [LanguageCapability](LanguageCapability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:AutomaticSummarisation](https://w3id.org/lmodel/dpv/ai/AutomaticSummarisation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Automatic Summarisation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.6.1 |
| upstream_iri | https://w3id.org/dpv/ai/owl#AutomaticSummarisation |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:AutomaticSummarisation |
| native | ai:AutomaticSummarisation |
| exact | dpv_ai:AutomaticSummarisation, dpv_ai_owl:AutomaticSummarisation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AutomaticSummarisation
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.6.1
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#AutomaticSummarisation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for shortening a portion of content such as text while

  retaining important semantic information'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Automatic Summarisation
exact_mappings:
- dpv_ai:AutomaticSummarisation
- dpv_ai_owl:AutomaticSummarisation
is_a: InformationRetrieval
mixins:
- Capability
- LanguageCapability
class_uri: ai:AutomaticSummarisation

```
</details>

### Induced

<details>
```yaml
name: AutomaticSummarisation
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.6.1
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#AutomaticSummarisation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for shortening a portion of content such as text while

  retaining important semantic information'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Automatic Summarisation
exact_mappings:
- dpv_ai:AutomaticSummarisation
- dpv_ai_owl:AutomaticSummarisation
is_a: InformationRetrieval
mixins:
- Capability
- LanguageCapability
class_uri: ai:AutomaticSummarisation

```
</details></div>