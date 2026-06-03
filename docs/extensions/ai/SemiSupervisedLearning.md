---
search:
  boost: 10.0
---

# Class: SemiSupervisedLearning 


_Machine learning that makes use of both labelled and unlabelled data_

_during training_



<div data-search-exclude markdown="1">



URI: [ai:SemiSupervisedLearning](https://w3id.org/lmodel/dpv/ai/SemiSupervisedLearning)





```mermaid
 classDiagram
    class SemiSupervisedLearning
    click SemiSupervisedLearning href "../SemiSupervisedLearning/"
      TrainingTechnique <|-- SemiSupervisedLearning
        click TrainingTechnique href "../TrainingTechnique/"
      MachineLearning <|-- SemiSupervisedLearning
        click MachineLearning href "../MachineLearning/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [MachineLearning](MachineLearning.md)
            * **SemiSupervisedLearning** [ [TrainingTechnique](TrainingTechnique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:SemiSupervisedLearning](https://w3id.org/lmodel/dpv/ai/SemiSupervisedLearning) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Semi Supervised Learning




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.3.11 |
| upstream_iri | https://w3id.org/dpv/ai/owl#SemiSupervisedLearning |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:SemiSupervisedLearning |
| native | ai:SemiSupervisedLearning |
| exact | dpv_ai:SemiSupervisedLearning, dpv_ai_owl:SemiSupervisedLearning |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SemiSupervisedLearning
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.3.11
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SemiSupervisedLearning
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Machine learning that makes use of both labelled and unlabelled data

  during training'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Semi Supervised Learning
exact_mappings:
- dpv_ai:SemiSupervisedLearning
- dpv_ai_owl:SemiSupervisedLearning
is_a: MachineLearning
mixins:
- TrainingTechnique
class_uri: ai:SemiSupervisedLearning

```
</details>

### Induced

<details>
```yaml
name: SemiSupervisedLearning
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.3.11
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SemiSupervisedLearning
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Machine learning that makes use of both labelled and unlabelled data

  during training'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Semi Supervised Learning
exact_mappings:
- dpv_ai:SemiSupervisedLearning
- dpv_ai_owl:SemiSupervisedLearning
is_a: MachineLearning
mixins:
- TrainingTechnique
class_uri: ai:SemiSupervisedLearning

```
</details></div>