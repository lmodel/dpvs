---
search:
  boost: 10.0
---

# Class: BayesianOptimisation 


_Refers to Bayesian optimisation technique_



<div data-search-exclude markdown="1">



URI: [ai:BayesianOptimisation](https://w3id.org/lmodel/dpv/ai/BayesianOptimisation)





```mermaid
 classDiagram
    class BayesianOptimisation
    click BayesianOptimisation href "../BayesianOptimisation/"
      Technique <|-- BayesianOptimisation
        click Technique href "../Technique/"
      StatisticalTechnique <|-- BayesianOptimisation
        click StatisticalTechnique href "../StatisticalTechnique/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [StatisticalTechnique](StatisticalTechnique.md)
            * **BayesianOptimisation** [ [Technique](Technique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:BayesianOptimisation](https://w3id.org/lmodel/dpv/ai/BayesianOptimisation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Bayesian Optimisation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#BayesianOptimisation |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:BayesianOptimisation |
| native | ai:BayesianOptimisation |
| exact | dpv_ai:BayesianOptimisation, dpv_ai_owl:BayesianOptimisation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BayesianOptimisation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#BayesianOptimisation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Refers to Bayesian optimisation technique
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Bayesian Optimisation
exact_mappings:
- dpv_ai:BayesianOptimisation
- dpv_ai_owl:BayesianOptimisation
is_a: StatisticalTechnique
mixins:
- Technique
class_uri: ai:BayesianOptimisation

```
</details>

### Induced

<details>
```yaml
name: BayesianOptimisation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#BayesianOptimisation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Refers to Bayesian optimisation technique
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Bayesian Optimisation
exact_mappings:
- dpv_ai:BayesianOptimisation
- dpv_ai_owl:BayesianOptimisation
is_a: StatisticalTechnique
mixins:
- Technique
class_uri: ai:BayesianOptimisation

```
</details></div>