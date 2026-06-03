---
search:
  boost: 10.0
---

# Class: NeuralNetwork 


_Network of one or more layers of neurons connected by weighted links_

_with adjustable weights, which takes input data and produces an output_



<div data-search-exclude markdown="1">



URI: [ai:NeuralNetwork](https://w3id.org/lmodel/dpv/ai/NeuralNetwork)





```mermaid
 classDiagram
    class NeuralNetwork
    click NeuralNetwork href "../NeuralNetwork/"
      TrainingTechnique <|-- NeuralNetwork
        click TrainingTechnique href "../TrainingTechnique/"
      MachineLearning <|-- NeuralNetwork
        click MachineLearning href "../MachineLearning/"
      

      NeuralNetwork <|-- ConvolutionalNeuralNetwork
        click ConvolutionalNeuralNetwork href "../ConvolutionalNeuralNetwork/"
      NeuralNetwork <|-- FeedForwardNeuralNetwork
        click FeedForwardNeuralNetwork href "../FeedForwardNeuralNetwork/"
      NeuralNetwork <|-- LongShortTermMemory
        click LongShortTermMemory href "../LongShortTermMemory/"
      NeuralNetwork <|-- RecurrentNeuralNetwork
        click RecurrentNeuralNetwork href "../RecurrentNeuralNetwork/"
      

      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [MachineLearning](MachineLearning.md)
            * **NeuralNetwork** [ [TrainingTechnique](TrainingTechnique.md)]
                * [ConvolutionalNeuralNetwork](ConvolutionalNeuralNetwork.md) [ [TrainingTechnique](TrainingTechnique.md)]
                * [FeedForwardNeuralNetwork](FeedForwardNeuralNetwork.md) [ [TrainingTechnique](TrainingTechnique.md)]
                * [LongShortTermMemory](LongShortTermMemory.md) [ [TrainingTechnique](TrainingTechnique.md)]
                * [RecurrentNeuralNetwork](RecurrentNeuralNetwork.md) [ [TrainingTechnique](TrainingTechnique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:NeuralNetwork](https://w3id.org/lmodel/dpv/ai/NeuralNetwork) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Neural Network




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.4.8 |
| upstream_iri | https://w3id.org/dpv/ai/owl#NeuralNetwork |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:NeuralNetwork |
| native | ai:NeuralNetwork |
| exact | dpv_ai:NeuralNetwork, dpv_ai_owl:NeuralNetwork |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NeuralNetwork
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.4.8
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#NeuralNetwork
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Network of one or more layers of neurons connected by weighted links

  with adjustable weights, which takes input data and produces an output'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Neural Network
exact_mappings:
- dpv_ai:NeuralNetwork
- dpv_ai_owl:NeuralNetwork
is_a: MachineLearning
mixins:
- TrainingTechnique
class_uri: ai:NeuralNetwork

```
</details>

### Induced

<details>
```yaml
name: NeuralNetwork
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.4.8
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#NeuralNetwork
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Network of one or more layers of neurons connected by weighted links

  with adjustable weights, which takes input data and produces an output'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Neural Network
exact_mappings:
- dpv_ai:NeuralNetwork
- dpv_ai_owl:NeuralNetwork
is_a: MachineLearning
mixins:
- TrainingTechnique
class_uri: ai:NeuralNetwork

```
</details></div>