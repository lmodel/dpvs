---
search:
  boost: 10.0
---

# Class: FeedForwardNeuralNetwork 


_Neural network where information is fed from the input layer to the_

_output layer in one direction only_



<div data-search-exclude markdown="1">



URI: [ai:FeedForwardNeuralNetwork](https://w3id.org/lmodel/dpv/ai/FeedForwardNeuralNetwork)





```mermaid
 classDiagram
    class FeedForwardNeuralNetwork
    click FeedForwardNeuralNetwork href "../FeedForwardNeuralNetwork/"
      TrainingTechnique <|-- FeedForwardNeuralNetwork
        click TrainingTechnique href "../TrainingTechnique/"
      NeuralNetwork <|-- FeedForwardNeuralNetwork
        click NeuralNetwork href "../NeuralNetwork/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [MachineLearning](MachineLearning.md)
            * [NeuralNetwork](NeuralNetwork.md) [ [TrainingTechnique](TrainingTechnique.md)]
                * **FeedForwardNeuralNetwork** [ [TrainingTechnique](TrainingTechnique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:FeedForwardNeuralNetwork](https://w3id.org/lmodel/dpv/ai/FeedForwardNeuralNetwork) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Feed Forward Neural Network




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.4.6 |
| upstream_iri | https://w3id.org/dpv/ai/owl#FeedForwardNeuralNetwork |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:FeedForwardNeuralNetwork |
| native | ai:FeedForwardNeuralNetwork |
| exact | dpv_ai:FeedForwardNeuralNetwork, dpv_ai_owl:FeedForwardNeuralNetwork |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FeedForwardNeuralNetwork
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.4.6
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#FeedForwardNeuralNetwork
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Neural network where information is fed from the input layer to the

  output layer in one direction only'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Feed Forward Neural Network
exact_mappings:
- dpv_ai:FeedForwardNeuralNetwork
- dpv_ai_owl:FeedForwardNeuralNetwork
is_a: NeuralNetwork
mixins:
- TrainingTechnique
class_uri: ai:FeedForwardNeuralNetwork

```
</details>

### Induced

<details>
```yaml
name: FeedForwardNeuralNetwork
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.4.6
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#FeedForwardNeuralNetwork
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Neural network where information is fed from the input layer to the

  output layer in one direction only'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Feed Forward Neural Network
exact_mappings:
- dpv_ai:FeedForwardNeuralNetwork
- dpv_ai_owl:FeedForwardNeuralNetwork
is_a: NeuralNetwork
mixins:
- TrainingTechnique
class_uri: ai:FeedForwardNeuralNetwork

```
</details></div>