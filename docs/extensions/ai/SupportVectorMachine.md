---
search:
  boost: 10.0
---

# Class: SupportVectorMachine 


_A machine learning algorithm that finds decision boundaries with maximal_

_margins_



<div data-search-exclude markdown="1">



URI: [ai:SupportVectorMachine](https://w3id.org/lmodel/dpv/ai/SupportVectorMachine)





```mermaid
 classDiagram
    class SupportVectorMachine
    click SupportVectorMachine href "../SupportVectorMachine/"
      TrainingTechnique <|-- SupportVectorMachine
        click TrainingTechnique href "../TrainingTechnique/"
      MachineLearning <|-- SupportVectorMachine
        click MachineLearning href "../MachineLearning/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [MachineLearning](MachineLearning.md)
            * **SupportVectorMachine** [ [TrainingTechnique](TrainingTechnique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:SupportVectorMachine](https://w3id.org/lmodel/dpv/ai/SupportVectorMachine) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Support Vector Machine




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.3.13 |
| upstream_iri | https://w3id.org/dpv/ai/owl#SupportVectorMachine |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:SupportVectorMachine |
| native | ai:SupportVectorMachine |
| exact | dpv_ai:SupportVectorMachine, dpv_ai_owl:SupportVectorMachine |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SupportVectorMachine
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.3.13
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SupportVectorMachine
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'A machine learning algorithm that finds decision boundaries with maximal

  margins'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Support Vector Machine
exact_mappings:
- dpv_ai:SupportVectorMachine
- dpv_ai_owl:SupportVectorMachine
is_a: MachineLearning
mixins:
- TrainingTechnique
class_uri: ai:SupportVectorMachine

```
</details>

### Induced

<details>
```yaml
name: SupportVectorMachine
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.3.13
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SupportVectorMachine
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'A machine learning algorithm that finds decision boundaries with maximal

  margins'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Support Vector Machine
exact_mappings:
- dpv_ai:SupportVectorMachine
- dpv_ai_owl:SupportVectorMachine
is_a: MachineLearning
mixins:
- TrainingTechnique
class_uri: ai:SupportVectorMachine

```
</details></div>