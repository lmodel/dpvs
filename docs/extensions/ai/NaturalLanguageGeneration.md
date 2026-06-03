---
search:
  boost: 10.0
---

# Class: NaturalLanguageGeneration 


_Converting data carrying semantics into natural language_



<div data-search-exclude markdown="1">



URI: [ai:NaturalLanguageGeneration](https://w3id.org/lmodel/dpv/ai/NaturalLanguageGeneration)





```mermaid
 classDiagram
    class NaturalLanguageGeneration
    click NaturalLanguageGeneration href "../NaturalLanguageGeneration/"
      Capability <|-- NaturalLanguageGeneration
        click Capability href "../Capability/"
      LanguageCapability <|-- NaturalLanguageGeneration
        click LanguageCapability href "../LanguageCapability/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [LanguageCapability](LanguageCapability.md)
            * **NaturalLanguageGeneration** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:NaturalLanguageGeneration](https://w3id.org/lmodel/dpv/ai/NaturalLanguageGeneration) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Natural Language Generation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.6.8 |
| upstream_iri | https://w3id.org/dpv/ai/owl#NaturalLanguageGeneration |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:NaturalLanguageGeneration |
| native | ai:NaturalLanguageGeneration |
| exact | dpv_ai:NaturalLanguageGeneration, dpv_ai_owl:NaturalLanguageGeneration |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NaturalLanguageGeneration
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.6.8
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#NaturalLanguageGeneration
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Converting data carrying semantics into natural language
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Natural Language Generation
exact_mappings:
- dpv_ai:NaturalLanguageGeneration
- dpv_ai_owl:NaturalLanguageGeneration
is_a: LanguageCapability
mixins:
- Capability
class_uri: ai:NaturalLanguageGeneration

```
</details>

### Induced

<details>
```yaml
name: NaturalLanguageGeneration
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.6.8
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#NaturalLanguageGeneration
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Converting data carrying semantics into natural language
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Natural Language Generation
exact_mappings:
- dpv_ai:NaturalLanguageGeneration
- dpv_ai_owl:NaturalLanguageGeneration
is_a: LanguageCapability
mixins:
- Capability
class_uri: ai:NaturalLanguageGeneration

```
</details></div>