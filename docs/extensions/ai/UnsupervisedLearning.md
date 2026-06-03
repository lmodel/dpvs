---
search:
  boost: 10.0
---

# Class: UnsupervisedLearning 


_Machine learning that makes only use of unlabelled data during training_



<div data-search-exclude markdown="1">



URI: [ai:UnsupervisedLearning](https://w3id.org/lmodel/dpv/ai/UnsupervisedLearning)





```mermaid
 classDiagram
    class UnsupervisedLearning
    click UnsupervisedLearning href "../UnsupervisedLearning/"
      TrainingTechnique <|-- UnsupervisedLearning
        click TrainingTechnique href "../TrainingTechnique/"
      MachineLearning <|-- UnsupervisedLearning
        click MachineLearning href "../MachineLearning/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [MachineLearning](MachineLearning.md)
            * **UnsupervisedLearning** [ [TrainingTechnique](TrainingTechnique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:UnsupervisedLearning](https://w3id.org/lmodel/dpv/ai/UnsupervisedLearning) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Unsupervised Learning




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.3.17 |
| upstream_iri | https://w3id.org/dpv/ai/owl#UnsupervisedLearning |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:UnsupervisedLearning |
| native | ai:UnsupervisedLearning |
| exact | dpv_ai:UnsupervisedLearning, dpv_ai_owl:UnsupervisedLearning |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UnsupervisedLearning
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.3.17
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#UnsupervisedLearning
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Machine learning that makes only use of unlabelled data during training
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Unsupervised Learning
exact_mappings:
- dpv_ai:UnsupervisedLearning
- dpv_ai_owl:UnsupervisedLearning
is_a: MachineLearning
mixins:
- TrainingTechnique
class_uri: ai:UnsupervisedLearning

```
</details>

### Induced

<details>
```yaml
name: UnsupervisedLearning
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.3.17
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#UnsupervisedLearning
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Machine learning that makes only use of unlabelled data during training
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Unsupervised Learning
exact_mappings:
- dpv_ai:UnsupervisedLearning
- dpv_ai_owl:UnsupervisedLearning
is_a: MachineLearning
mixins:
- TrainingTechnique
class_uri: ai:UnsupervisedLearning

```
</details></div>