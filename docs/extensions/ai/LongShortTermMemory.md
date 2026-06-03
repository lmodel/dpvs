---
search:
  boost: 10.0
---

# Class: LongShortTermMemory 


_Type of recurrent neural network that processes sequential data with a_

_satisfactory performance for both long and short span dependencies_



<div data-search-exclude markdown="1">



URI: [ai:LongShortTermMemory](https://w3id.org/lmodel/dpv/ai/LongShortTermMemory)





```mermaid
 classDiagram
    class LongShortTermMemory
    click LongShortTermMemory href "../LongShortTermMemory/"
      TrainingTechnique <|-- LongShortTermMemory
        click TrainingTechnique href "../TrainingTechnique/"
      NeuralNetwork <|-- LongShortTermMemory
        click NeuralNetwork href "../NeuralNetwork/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [MachineLearning](MachineLearning.md)
            * [NeuralNetwork](NeuralNetwork.md) [ [TrainingTechnique](TrainingTechnique.md)]
                * **LongShortTermMemory** [ [TrainingTechnique](TrainingTechnique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:LongShortTermMemory](https://w3id.org/lmodel/dpv/ai/LongShortTermMemory) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Long Short-Term Memory (LSTM)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.4.7 |
| upstream_iri | https://w3id.org/dpv/ai/owl#LongShortTermMemory |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:LongShortTermMemory |
| native | ai:LongShortTermMemory |
| exact | dpv_ai:LongShortTermMemory, dpv_ai_owl:LongShortTermMemory |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LongShortTermMemory
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.4.7
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#LongShortTermMemory
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Type of recurrent neural network that processes sequential data with
  a

  satisfactory performance for both long and short span dependencies'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Long Short-Term Memory (LSTM)
exact_mappings:
- dpv_ai:LongShortTermMemory
- dpv_ai_owl:LongShortTermMemory
is_a: NeuralNetwork
mixins:
- TrainingTechnique
class_uri: ai:LongShortTermMemory

```
</details>

### Induced

<details>
```yaml
name: LongShortTermMemory
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.4.7
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#LongShortTermMemory
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Type of recurrent neural network that processes sequential data with
  a

  satisfactory performance for both long and short span dependencies'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Long Short-Term Memory (LSTM)
exact_mappings:
- dpv_ai:LongShortTermMemory
- dpv_ai_owl:LongShortTermMemory
is_a: NeuralNetwork
mixins:
- TrainingTechnique
class_uri: ai:LongShortTermMemory

```
</details></div>