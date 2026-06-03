---
search:
  boost: 10.0
---

# Class: FineTunedModel 


_Model resulting from fine-tuning of a pre-trained model_



<div data-search-exclude markdown="1">



URI: [ai:FineTunedModel](https://w3id.org/lmodel/dpv/ai/FineTunedModel)





```mermaid
 classDiagram
    class FineTunedModel
    click FineTunedModel href "../FineTunedModel/"
      TrainedModel <|-- FineTunedModel
        click TrainedModel href "../TrainedModel/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Model](Model.md)
        * [TrainedModel](TrainedModel.md)
            * **FineTunedModel**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:FineTunedModel](https://w3id.org/lmodel/dpv/ai/FineTunedModel) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Fine-tuned Model




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#FineTunedModel |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:FineTunedModel |
| native | ai:FineTunedModel |
| exact | dpv_ai:FineTunedModel, dpv_ai_owl:FineTunedModel |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FineTunedModel
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#FineTunedModel
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Model resulting from fine-tuning of a pre-trained model
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Fine-tuned Model
exact_mappings:
- dpv_ai:FineTunedModel
- dpv_ai_owl:FineTunedModel
is_a: TrainedModel
class_uri: ai:FineTunedModel

```
</details>

### Induced

<details>
```yaml
name: FineTunedModel
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#FineTunedModel
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Model resulting from fine-tuning of a pre-trained model
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Fine-tuned Model
exact_mappings:
- dpv_ai:FineTunedModel
- dpv_ai_owl:FineTunedModel
is_a: TrainedModel
class_uri: ai:FineTunedModel

```
</details></div>