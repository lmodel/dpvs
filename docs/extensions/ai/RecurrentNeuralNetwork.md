---
search:
  boost: 10.0
---

# Class: RecurrentNeuralNetwork 


_Neural network in which outputs from both the previous layer and the_

_previous processing step are fed into the current layer_



<div data-search-exclude markdown="1">



URI: [ai:RecurrentNeuralNetwork](https://w3id.org/lmodel/dpv/ai/RecurrentNeuralNetwork)





```mermaid
 classDiagram
    class RecurrentNeuralNetwork
    click RecurrentNeuralNetwork href "../RecurrentNeuralNetwork/"
      TrainingTechnique <|-- RecurrentNeuralNetwork
        click TrainingTechnique href "../TrainingTechnique/"
      NeuralNetwork <|-- RecurrentNeuralNetwork
        click NeuralNetwork href "../NeuralNetwork/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [MachineLearning](MachineLearning.md)
            * [NeuralNetwork](NeuralNetwork.md) [ [TrainingTechnique](TrainingTechnique.md)]
                * **RecurrentNeuralNetwork** [ [TrainingTechnique](TrainingTechnique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:RecurrentNeuralNetwork](https://w3id.org/lmodel/dpv/ai/RecurrentNeuralNetwork) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Recurrent Neural Network (RNN)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.4.10 |
| upstream_iri | https://w3id.org/dpv/ai/owl#RecurrentNeuralNetwork |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:RecurrentNeuralNetwork |
| native | ai:RecurrentNeuralNetwork |
| exact | dpv_ai:RecurrentNeuralNetwork, dpv_ai_owl:RecurrentNeuralNetwork |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RecurrentNeuralNetwork
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.4.10
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#RecurrentNeuralNetwork
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Neural network in which outputs from both the previous layer and the

  previous processing step are fed into the current layer'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Recurrent Neural Network (RNN)
exact_mappings:
- dpv_ai:RecurrentNeuralNetwork
- dpv_ai_owl:RecurrentNeuralNetwork
is_a: NeuralNetwork
mixins:
- TrainingTechnique
class_uri: ai:RecurrentNeuralNetwork

```
</details>

### Induced

<details>
```yaml
name: RecurrentNeuralNetwork
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.4.10
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#RecurrentNeuralNetwork
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Neural network in which outputs from both the previous layer and the

  previous processing step are fed into the current layer'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Recurrent Neural Network (RNN)
exact_mappings:
- dpv_ai:RecurrentNeuralNetwork
- dpv_ai_owl:RecurrentNeuralNetwork
is_a: NeuralNetwork
mixins:
- TrainingTechnique
class_uri: ai:RecurrentNeuralNetwork

```
</details></div>