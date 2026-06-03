---
search:
  boost: 10.0
---

# Class: SupervisedLearning 


_Machine learning that makes only use of labelled data during training_



<div data-search-exclude markdown="1">



URI: [ai:SupervisedLearning](https://w3id.org/lmodel/dpv/ai/SupervisedLearning)





```mermaid
 classDiagram
    class SupervisedLearning
    click SupervisedLearning href "../SupervisedLearning/"
      TrainingTechnique <|-- SupervisedLearning
        click TrainingTechnique href "../TrainingTechnique/"
      MachineLearning <|-- SupervisedLearning
        click MachineLearning href "../MachineLearning/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [MachineLearning](MachineLearning.md)
            * **SupervisedLearning** [ [TrainingTechnique](TrainingTechnique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:SupervisedLearning](https://w3id.org/lmodel/dpv/ai/SupervisedLearning) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Supervised Learning




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.3.11 |
| upstream_iri | https://w3id.org/dpv/ai/owl#SupervisedLearning |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:SupervisedLearning |
| native | ai:SupervisedLearning |
| exact | dpv_ai:SupervisedLearning, dpv_ai_owl:SupervisedLearning |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SupervisedLearning
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.3.11
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SupervisedLearning
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Machine learning that makes only use of labelled data during training
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Supervised Learning
exact_mappings:
- dpv_ai:SupervisedLearning
- dpv_ai_owl:SupervisedLearning
is_a: MachineLearning
mixins:
- TrainingTechnique
class_uri: ai:SupervisedLearning

```
</details>

### Induced

<details>
```yaml
name: SupervisedLearning
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.3.11
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SupervisedLearning
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Machine learning that makes only use of labelled data during training
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Supervised Learning
exact_mappings:
- dpv_ai:SupervisedLearning
- dpv_ai_owl:SupervisedLearning
is_a: MachineLearning
mixins:
- TrainingTechnique
class_uri: ai:SupervisedLearning

```
</details></div>