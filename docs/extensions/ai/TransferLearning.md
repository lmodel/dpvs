---
search:
  boost: 10.0
---

# Class: TransferLearning 


_a technique in machine learning in which knowledge learned from a task_

_is re-used in order to boost performance on a related task_



<div data-search-exclude markdown="1">



URI: [ai:TransferLearning](https://w3id.org/lmodel/dpv/ai/TransferLearning)





```mermaid
 classDiagram
    class TransferLearning
    click TransferLearning href "../TransferLearning/"
      TrainingTechnique <|-- TransferLearning
        click TrainingTechnique href "../TrainingTechnique/"
      DeepLearning <|-- TransferLearning
        click DeepLearning href "../DeepLearning/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [MachineLearning](MachineLearning.md)
            * [DeepLearning](DeepLearning.md) [ [TrainingTechnique](TrainingTechnique.md)]
                * **TransferLearning** [ [TrainingTechnique](TrainingTechnique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:TransferLearning](https://w3id.org/lmodel/dpv/ai/TransferLearning) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* TransferLearning




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#TransferLearning |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:TransferLearning |
| native | ai:TransferLearning |
| exact | dpv_ai:TransferLearning, dpv_ai_owl:TransferLearning |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TransferLearning
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TransferLearning
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'a technique in machine learning in which knowledge learned from a task

  is re-used in order to boost performance on a related task'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- TransferLearning
exact_mappings:
- dpv_ai:TransferLearning
- dpv_ai_owl:TransferLearning
is_a: DeepLearning
mixins:
- TrainingTechnique
class_uri: ai:TransferLearning

```
</details>

### Induced

<details>
```yaml
name: TransferLearning
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TransferLearning
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'a technique in machine learning in which knowledge learned from a task

  is re-used in order to boost performance on a related task'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- TransferLearning
exact_mappings:
- dpv_ai:TransferLearning
- dpv_ai_owl:TransferLearning
is_a: DeepLearning
mixins:
- TrainingTechnique
class_uri: ai:TransferLearning

```
</details></div>