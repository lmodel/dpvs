---
search:
  boost: 10.0
---

# Class: TextClassification 


_Capability of assigning predefined labels to text data in order to_

_automatically categorise it into groups_



<div data-search-exclude markdown="1">



URI: [ai:TextClassification](https://w3id.org/lmodel/dpv/ai/TextClassification)





```mermaid
 classDiagram
    class TextClassification
    click TextClassification href "../TextClassification/"
      Capability <|-- TextClassification
        click Capability href "../Capability/"
      NaturalLanguageProcessing <|-- TextClassification
        click NaturalLanguageProcessing href "../NaturalLanguageProcessing/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [LanguageCapability](LanguageCapability.md)
            * [NaturalLanguageProcessing](NaturalLanguageProcessing.md) [ [Capability](Capability.md)]
                * **TextClassification** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:TextClassification](https://w3id.org/lmodel/dpv/ai/TextClassification) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Text Classification




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#TextClassification |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:TextClassification |
| native | ai:TextClassification |
| exact | dpv_ai:TextClassification, dpv_ai_owl:TextClassification |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TextClassification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TextClassification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability of assigning predefined labels to text data in order to

  automatically categorise it into groups'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Text Classification
exact_mappings:
- dpv_ai:TextClassification
- dpv_ai_owl:TextClassification
is_a: NaturalLanguageProcessing
mixins:
- Capability
class_uri: ai:TextClassification

```
</details>

### Induced

<details>
```yaml
name: TextClassification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TextClassification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability of assigning predefined labels to text data in order to

  automatically categorise it into groups'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Text Classification
exact_mappings:
- dpv_ai:TextClassification
- dpv_ai_owl:TextClassification
is_a: NaturalLanguageProcessing
mixins:
- Capability
class_uri: ai:TextClassification

```
</details></div>