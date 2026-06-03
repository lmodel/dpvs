---
search:
  boost: 10.0
---

# Class: ModelFineTuning 


_Process where a pre-trained model is further refined through the use of_

_a smaller training dataset_



<div data-search-exclude markdown="1">



URI: [ai:ModelFineTuning](https://w3id.org/lmodel/dpv/ai/ModelFineTuning)





```mermaid
 classDiagram
    class ModelFineTuning
    click ModelFineTuning href "../ModelFineTuning/"
      ModelTraining <|-- ModelFineTuning
        click ModelTraining href "../ModelTraining/"
      
      
```





## Inheritance
* [ModelTraining](ModelTraining.md)
    * **ModelFineTuning**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ModelFineTuning](https://w3id.org/lmodel/dpv/ai/ModelFineTuning) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Model Fine-Tuning




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ModelFineTuning |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ModelFineTuning |
| native | ai:ModelFineTuning |
| exact | dpv_ai:ModelFineTuning, dpv_ai_owl:ModelFineTuning |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ModelFineTuning
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ModelFineTuning
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Process where a pre-trained model is further refined through the use
  of

  a smaller training dataset'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Model Fine-Tuning
exact_mappings:
- dpv_ai:ModelFineTuning
- dpv_ai_owl:ModelFineTuning
is_a: ModelTraining
class_uri: ai:ModelFineTuning

```
</details>

### Induced

<details>
```yaml
name: ModelFineTuning
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ModelFineTuning
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Process where a pre-trained model is further refined through the use
  of

  a smaller training dataset'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Model Fine-Tuning
exact_mappings:
- dpv_ai:ModelFineTuning
- dpv_ai_owl:ModelFineTuning
is_a: ModelTraining
class_uri: ai:ModelFineTuning

```
</details></div>