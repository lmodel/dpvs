---
search:
  boost: 10.0
---

# Class: GeneticAlgorithm 


_Algorithm which simulates natural selection by creating and evolving a_

_population of individuals (solutions) for optimization problems_



<div data-search-exclude markdown="1">



URI: [ai:GeneticAlgorithm](https://w3id.org/lmodel/dpv/ai/GeneticAlgorithm)





```mermaid
 classDiagram
    class GeneticAlgorithm
    click GeneticAlgorithm href "../GeneticAlgorithm/"
      TrainingTechnique <|-- GeneticAlgorithm
        click TrainingTechnique href "../TrainingTechnique/"
      MachineLearning <|-- GeneticAlgorithm
        click MachineLearning href "../MachineLearning/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [MachineLearning](MachineLearning.md)
            * **GeneticAlgorithm** [ [TrainingTechnique](TrainingTechnique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:GeneticAlgorithm](https://w3id.org/lmodel/dpv/ai/GeneticAlgorithm) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Genetic Algorithm




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.1.15 |
| upstream_iri | https://w3id.org/dpv/ai/owl#GeneticAlgorithm |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:GeneticAlgorithm |
| native | ai:GeneticAlgorithm |
| exact | dpv_ai:GeneticAlgorithm, dpv_ai_owl:GeneticAlgorithm |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeneticAlgorithm
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.1.15
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#GeneticAlgorithm
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Algorithm which simulates natural selection by creating and evolving
  a

  population of individuals (solutions) for optimization problems'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Genetic Algorithm
exact_mappings:
- dpv_ai:GeneticAlgorithm
- dpv_ai_owl:GeneticAlgorithm
is_a: MachineLearning
mixins:
- TrainingTechnique
class_uri: ai:GeneticAlgorithm

```
</details>

### Induced

<details>
```yaml
name: GeneticAlgorithm
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.1.15
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#GeneticAlgorithm
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Algorithm which simulates natural selection by creating and evolving
  a

  population of individuals (solutions) for optimization problems'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Genetic Algorithm
exact_mappings:
- dpv_ai:GeneticAlgorithm
- dpv_ai_owl:GeneticAlgorithm
is_a: MachineLearning
mixins:
- TrainingTechnique
class_uri: ai:GeneticAlgorithm

```
</details></div>