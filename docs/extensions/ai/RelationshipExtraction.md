---
search:
  boost: 10.0
---

# Class: RelationshipExtraction 


_Capability for identifying relationships among entities mentioned in a_

_text_



<div data-search-exclude markdown="1">



URI: [ai:RelationshipExtraction](https://w3id.org/lmodel/dpv/ai/RelationshipExtraction)





```mermaid
 classDiagram
    class RelationshipExtraction
    click RelationshipExtraction href "../RelationshipExtraction/"
      Capability <|-- RelationshipExtraction
        click Capability href "../Capability/"
      LanguageCapability <|-- RelationshipExtraction
        click LanguageCapability href "../LanguageCapability/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [LanguageCapability](LanguageCapability.md)
            * **RelationshipExtraction** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:RelationshipExtraction](https://w3id.org/lmodel/dpv/ai/RelationshipExtraction) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Relationship Extraction




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.6.15 |
| upstream_iri | https://w3id.org/dpv/ai/owl#RelationshipExtraction |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:RelationshipExtraction |
| native | ai:RelationshipExtraction |
| exact | dpv_ai:RelationshipExtraction, dpv_ai_owl:RelationshipExtraction |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RelationshipExtraction
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.6.15
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#RelationshipExtraction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for identifying relationships among entities mentioned in
  a

  text'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Relationship Extraction
exact_mappings:
- dpv_ai:RelationshipExtraction
- dpv_ai_owl:RelationshipExtraction
is_a: LanguageCapability
mixins:
- Capability
class_uri: ai:RelationshipExtraction

```
</details>

### Induced

<details>
```yaml
name: RelationshipExtraction
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.6.15
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#RelationshipExtraction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for identifying relationships among entities mentioned in
  a

  text'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Relationship Extraction
exact_mappings:
- dpv_ai:RelationshipExtraction
- dpv_ai_owl:RelationshipExtraction
is_a: LanguageCapability
mixins:
- Capability
class_uri: ai:RelationshipExtraction

```
</details></div>