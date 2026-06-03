---
search:
  boost: 10.0
---

# Class: TrainedModel 


_Model resulted from model training_



<div data-search-exclude markdown="1">



URI: [ai:TrainedModel](https://w3id.org/lmodel/dpv/ai/TrainedModel)





```mermaid
 classDiagram
    class TrainedModel
    click TrainedModel href "../TrainedModel/"
      Model <|-- TrainedModel
        click Model href "../Model/"
      

      TrainedModel <|-- FineTunedModel
        click FineTunedModel href "../FineTunedModel/"
      

      
```





## Inheritance
* [AI](AI.md)
    * [Model](Model.md)
        * **TrainedModel**
            * [FineTunedModel](FineTunedModel.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:TrainedModel](https://w3id.org/lmodel/dpv/ai/TrainedModel) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Trained Model




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source |  ISO 8373:2021 3.7 |
| upstream_iri | https://w3id.org/dpv/ai/owl#TrainedModel |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:TrainedModel |
| native | ai:TrainedModel |
| exact | dpv_ai:TrainedModel, dpv_ai_owl:TrainedModel |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TrainedModel
annotations:
  dct_source:
    tag: dct_source
    value: ' ISO 8373:2021 3.7'
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TrainedModel
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Model resulted from model training
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Trained Model
exact_mappings:
- dpv_ai:TrainedModel
- dpv_ai_owl:TrainedModel
is_a: Model
class_uri: ai:TrainedModel

```
</details>

### Induced

<details>
```yaml
name: TrainedModel
annotations:
  dct_source:
    tag: dct_source
    value: ' ISO 8373:2021 3.7'
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TrainedModel
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Model resulted from model training
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Trained Model
exact_mappings:
- dpv_ai:TrainedModel
- dpv_ai_owl:TrainedModel
is_a: Model
class_uri: ai:TrainedModel

```
</details></div>