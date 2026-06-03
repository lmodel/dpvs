---
search:
  boost: 10.0
---

# Class: SelfSupervisedLearning 


_Machine learning approach that uses unsupervised learning for tasks that_

_typically require supervision, generating implicit labels from_

_unstructured data, where models are trained on a task using the data_

_itself to provide supervisory signals, often used in neural networks to_

_exploit inherent structures or relationships within input data to_

_generate training signals_



<div data-search-exclude markdown="1">



URI: [ai:SelfSupervisedLearning](https://w3id.org/lmodel/dpv/ai/SelfSupervisedLearning)





```mermaid
 classDiagram
    class SelfSupervisedLearning
    click SelfSupervisedLearning href "../SelfSupervisedLearning/"
      TrainingTechnique <|-- SelfSupervisedLearning
        click TrainingTechnique href "../TrainingTechnique/"
      MachineLearning <|-- SelfSupervisedLearning
        click MachineLearning href "../MachineLearning/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [MachineLearning](MachineLearning.md)
            * **SelfSupervisedLearning** [ [TrainingTechnique](TrainingTechnique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:SelfSupervisedLearning](https://w3id.org/lmodel/dpv/ai/SelfSupervisedLearning) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Self-Supervised Learning




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#SelfSupervisedLearning |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:SelfSupervisedLearning |
| native | ai:SelfSupervisedLearning |
| exact | dpv_ai:SelfSupervisedLearning, dpv_ai_owl:SelfSupervisedLearning |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SelfSupervisedLearning
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SelfSupervisedLearning
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Machine learning approach that uses unsupervised learning for tasks
  that

  typically require supervision, generating implicit labels from

  unstructured data, where models are trained on a task using the data

  itself to provide supervisory signals, often used in neural networks to

  exploit inherent structures or relationships within input data to

  generate training signals'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Self-Supervised Learning
exact_mappings:
- dpv_ai:SelfSupervisedLearning
- dpv_ai_owl:SelfSupervisedLearning
is_a: MachineLearning
mixins:
- TrainingTechnique
class_uri: ai:SelfSupervisedLearning

```
</details>

### Induced

<details>
```yaml
name: SelfSupervisedLearning
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SelfSupervisedLearning
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Machine learning approach that uses unsupervised learning for tasks
  that

  typically require supervision, generating implicit labels from

  unstructured data, where models are trained on a task using the data

  itself to provide supervisory signals, often used in neural networks to

  exploit inherent structures or relationships within input data to

  generate training signals'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Self-Supervised Learning
exact_mappings:
- dpv_ai:SelfSupervisedLearning
- dpv_ai_owl:SelfSupervisedLearning
is_a: MachineLearning
mixins:
- TrainingTechnique
class_uri: ai:SelfSupervisedLearning

```
</details></div>