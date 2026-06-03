---
search:
  boost: 10.0
---

# Class: ConvolutionalNeuralNetwork 


_Feed forward neural network using convolution in at least one of its_

_layers_



<div data-search-exclude markdown="1">



URI: [ai:ConvolutionalNeuralNetwork](https://w3id.org/lmodel/dpv/ai/ConvolutionalNeuralNetwork)





```mermaid
 classDiagram
    class ConvolutionalNeuralNetwork
    click ConvolutionalNeuralNetwork href "../ConvolutionalNeuralNetwork/"
      TrainingTechnique <|-- ConvolutionalNeuralNetwork
        click TrainingTechnique href "../TrainingTechnique/"
      NeuralNetwork <|-- ConvolutionalNeuralNetwork
        click NeuralNetwork href "../NeuralNetwork/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [MachineLearning](MachineLearning.md)
            * [NeuralNetwork](NeuralNetwork.md) [ [TrainingTechnique](TrainingTechnique.md)]
                * **ConvolutionalNeuralNetwork** [ [TrainingTechnique](TrainingTechnique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ConvolutionalNeuralNetwork](https://w3id.org/lmodel/dpv/ai/ConvolutionalNeuralNetwork) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Convolutional Neural Network (CNN)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.4.2 |
| upstream_iri | https://w3id.org/dpv/ai/owl#ConvolutionalNeuralNetwork |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ConvolutionalNeuralNetwork |
| native | ai:ConvolutionalNeuralNetwork |
| exact | dpv_ai:ConvolutionalNeuralNetwork, dpv_ai_owl:ConvolutionalNeuralNetwork |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ConvolutionalNeuralNetwork
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.4.2
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ConvolutionalNeuralNetwork
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Feed forward neural network using convolution in at least one of its

  layers'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Convolutional Neural Network (CNN)
exact_mappings:
- dpv_ai:ConvolutionalNeuralNetwork
- dpv_ai_owl:ConvolutionalNeuralNetwork
is_a: NeuralNetwork
mixins:
- TrainingTechnique
class_uri: ai:ConvolutionalNeuralNetwork

```
</details>

### Induced

<details>
```yaml
name: ConvolutionalNeuralNetwork
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.4.2
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ConvolutionalNeuralNetwork
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Feed forward neural network using convolution in at least one of its

  layers'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Convolutional Neural Network (CNN)
exact_mappings:
- dpv_ai:ConvolutionalNeuralNetwork
- dpv_ai_owl:ConvolutionalNeuralNetwork
is_a: NeuralNetwork
mixins:
- TrainingTechnique
class_uri: ai:ConvolutionalNeuralNetwork

```
</details></div>