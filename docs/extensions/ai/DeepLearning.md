---
search:
  boost: 10.0
---

# Class: DeepLearning 


_Approach to creating rich hierarchical representations through the_

_training of neural networks with many hidden layers_



<div data-search-exclude markdown="1">



URI: [ai:DeepLearning](https://w3id.org/lmodel/dpv/ai/DeepLearning)





```mermaid
 classDiagram
    class DeepLearning
    click DeepLearning href "../DeepLearning/"
      TrainingTechnique <|-- DeepLearning
        click TrainingTechnique href "../TrainingTechnique/"
      MachineLearning <|-- DeepLearning
        click MachineLearning href "../MachineLearning/"
      

      DeepLearning <|-- TransferLearning
        click TransferLearning href "../TransferLearning/"
      

      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [MachineLearning](MachineLearning.md)
            * **DeepLearning** [ [TrainingTechnique](TrainingTechnique.md)]
                * [TransferLearning](TransferLearning.md) [ [TrainingTechnique](TrainingTechnique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:DeepLearning](https://w3id.org/lmodel/dpv/ai/DeepLearning) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Deep Learning




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.4.4 |
| upstream_iri | https://w3id.org/dpv/ai/owl#DeepLearning |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:DeepLearning |
| native | ai:DeepLearning |
| exact | dpv_ai:DeepLearning, dpv_ai_owl:DeepLearning |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DeepLearning
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.4.4
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DeepLearning
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Approach to creating rich hierarchical representations through the

  training of neural networks with many hidden layers'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Deep Learning
exact_mappings:
- dpv_ai:DeepLearning
- dpv_ai_owl:DeepLearning
is_a: MachineLearning
mixins:
- TrainingTechnique
class_uri: ai:DeepLearning

```
</details>

### Induced

<details>
```yaml
name: DeepLearning
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.4.4
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DeepLearning
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Approach to creating rich hierarchical representations through the

  training of neural networks with many hidden layers'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Deep Learning
exact_mappings:
- dpv_ai:DeepLearning
- dpv_ai_owl:DeepLearning
is_a: MachineLearning
mixins:
- TrainingTechnique
class_uri: ai:DeepLearning

```
</details></div>