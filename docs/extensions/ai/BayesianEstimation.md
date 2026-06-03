---
search:
  boost: 10.0
---

# Class: BayesianEstimation 


_Refers to Bayesian estimation approach_



<div data-search-exclude markdown="1">



URI: [ai:BayesianEstimation](https://w3id.org/lmodel/dpv/ai/BayesianEstimation)





```mermaid
 classDiagram
    class BayesianEstimation
    click BayesianEstimation href "../BayesianEstimation/"
      Technique <|-- BayesianEstimation
        click Technique href "../Technique/"
      StatisticalTechnique <|-- BayesianEstimation
        click StatisticalTechnique href "../StatisticalTechnique/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [StatisticalTechnique](StatisticalTechnique.md)
            * **BayesianEstimation** [ [Technique](Technique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:BayesianEstimation](https://w3id.org/lmodel/dpv/ai/BayesianEstimation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Bayesian Estimation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#BayesianEstimation |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:BayesianEstimation |
| native | ai:BayesianEstimation |
| exact | dpv_ai:BayesianEstimation, dpv_ai_owl:BayesianEstimation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BayesianEstimation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#BayesianEstimation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Refers to Bayesian estimation approach
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Bayesian Estimation
exact_mappings:
- dpv_ai:BayesianEstimation
- dpv_ai_owl:BayesianEstimation
is_a: StatisticalTechnique
mixins:
- Technique
class_uri: ai:BayesianEstimation

```
</details>

### Induced

<details>
```yaml
name: BayesianEstimation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#BayesianEstimation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Refers to Bayesian estimation approach
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Bayesian Estimation
exact_mappings:
- dpv_ai:BayesianEstimation
- dpv_ai_owl:BayesianEstimation
is_a: StatisticalTechnique
mixins:
- Technique
class_uri: ai:BayesianEstimation

```
</details></div>