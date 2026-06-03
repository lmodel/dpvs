---
search:
  boost: 10.0
---

# Class: TrainingData 


_Data involved in the training of an AI system or model_



<div data-search-exclude markdown="1">



URI: [ai:TrainingData](https://w3id.org/lmodel/dpv/ai/TrainingData)





```mermaid
 classDiagram
    class TrainingData
    click TrainingData href "../TrainingData/"
      DpvData <|-- TrainingData
        click DpvData href "../DpvData/"
      
      
```





## Inheritance
* [DpvData](DpvData.md)
    * **TrainingData**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:TrainingData](https://w3id.org/lmodel/dpv/ai/TrainingData) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Training Data




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#TrainingData |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:TrainingData |
| native | ai:TrainingData |
| exact | dpv_ai:TrainingData, dpv_ai_owl:TrainingData |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TrainingData
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TrainingData
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Data involved in the training of an AI system or model
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Training Data
exact_mappings:
- dpv_ai:TrainingData
- dpv_ai_owl:TrainingData
is_a: DpvData
class_uri: ai:TrainingData

```
</details>

### Induced

<details>
```yaml
name: TrainingData
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TrainingData
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Data involved in the training of an AI system or model
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Training Data
exact_mappings:
- dpv_ai:TrainingData
- dpv_ai_owl:TrainingData
is_a: DpvData
class_uri: ai:TrainingData

```
</details></div>