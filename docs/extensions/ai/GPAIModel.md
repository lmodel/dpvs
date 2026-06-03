---
search:
  boost: 10.0
---

# Class: GPAIModel 


_A model that displays generality in terms of capabilities and potential_

_applications_



<div data-search-exclude markdown="1">



URI: [ai:GPAIModel](https://w3id.org/lmodel/dpv/ai/GPAIModel)





```mermaid
 classDiagram
    class GPAIModel
    click GPAIModel href "../GPAIModel/"
      Model <|-- GPAIModel
        click Model href "../Model/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Model](Model.md)
        * **GPAIModel**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:GPAIModel](https://w3id.org/lmodel/dpv/ai/GPAIModel) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* General Purpose AI Model




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | EU AI Act |
| upstream_iri | https://w3id.org/dpv/ai/owl#GPAIModel |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:GPAIModel |
| native | ai:GPAIModel |
| exact | dpv_ai:GPAIModel, dpv_ai_owl:GPAIModel |
| close | iso42001:AISystem |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GPAIModel
annotations:
  dct_source:
    tag: dct_source
    value: EU AI Act
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#GPAIModel
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'A model that displays generality in terms of capabilities and potential

  applications'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- General Purpose AI Model
exact_mappings:
- dpv_ai:GPAIModel
- dpv_ai_owl:GPAIModel
close_mappings:
- iso42001:AISystem
is_a: Model
class_uri: ai:GPAIModel

```
</details>

### Induced

<details>
```yaml
name: GPAIModel
annotations:
  dct_source:
    tag: dct_source
    value: EU AI Act
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#GPAIModel
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'A model that displays generality in terms of capabilities and potential

  applications'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- General Purpose AI Model
exact_mappings:
- dpv_ai:GPAIModel
- dpv_ai_owl:GPAIModel
close_mappings:
- iso42001:AISystem
is_a: Model
class_uri: ai:GPAIModel

```
</details></div>