---
search:
  boost: 10.0
---

# Class: ReinforcementLearning 


_Learning of an optimal sequence of actions to maximise a reward through_

_interaction with an environment_



<div data-search-exclude markdown="1">



URI: [ai:ReinforcementLearning](https://w3id.org/lmodel/dpv/ai/ReinforcementLearning)





```mermaid
 classDiagram
    class ReinforcementLearning
    click ReinforcementLearning href "../ReinforcementLearning/"
      TrainingTechnique <|-- ReinforcementLearning
        click TrainingTechnique href "../TrainingTechnique/"
      MachineLearning <|-- ReinforcementLearning
        click MachineLearning href "../MachineLearning/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [MachineLearning](MachineLearning.md)
            * **ReinforcementLearning** [ [TrainingTechnique](TrainingTechnique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ReinforcementLearning](https://w3id.org/lmodel/dpv/ai/ReinforcementLearning) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Reinforcement Learning




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.3.9 |
| upstream_iri | https://w3id.org/dpv/ai/owl#ReinforcementLearning |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ReinforcementLearning |
| native | ai:ReinforcementLearning |
| exact | dpv_ai:ReinforcementLearning, dpv_ai_owl:ReinforcementLearning |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ReinforcementLearning
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.3.9
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ReinforcementLearning
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Learning of an optimal sequence of actions to maximise a reward through

  interaction with an environment'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Reinforcement Learning
exact_mappings:
- dpv_ai:ReinforcementLearning
- dpv_ai_owl:ReinforcementLearning
is_a: MachineLearning
mixins:
- TrainingTechnique
class_uri: ai:ReinforcementLearning

```
</details>

### Induced

<details>
```yaml
name: ReinforcementLearning
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.3.9
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ReinforcementLearning
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Learning of an optimal sequence of actions to maximise a reward through

  interaction with an environment'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Reinforcement Learning
exact_mappings:
- dpv_ai:ReinforcementLearning
- dpv_ai_owl:ReinforcementLearning
is_a: MachineLearning
mixins:
- TrainingTechnique
class_uri: ai:ReinforcementLearning

```
</details></div>