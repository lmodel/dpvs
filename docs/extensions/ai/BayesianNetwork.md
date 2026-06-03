---
search:
  boost: 10.0
---

# Class: BayesianNetwork 


_Probabilistic technique that uses Bayesian inference for probability_

_computations using a directed acyclic graph_



<div data-search-exclude markdown="1">



URI: [ai:BayesianNetwork](https://w3id.org/lmodel/dpv/ai/BayesianNetwork)





```mermaid
 classDiagram
    class BayesianNetwork
    click BayesianNetwork href "../BayesianNetwork/"
      Technique <|-- BayesianNetwork
        click Technique href "../Technique/"
      StatisticalTechnique <|-- BayesianNetwork
        click StatisticalTechnique href "../StatisticalTechnique/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [StatisticalTechnique](StatisticalTechnique.md)
            * **BayesianNetwork** [ [Technique](Technique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:BayesianNetwork](https://w3id.org/lmodel/dpv/ai/BayesianNetwork) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Bayesian Network




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.3.1 |
| upstream_iri | https://w3id.org/dpv/ai/owl#BayesianNetwork |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:BayesianNetwork |
| native | ai:BayesianNetwork |
| exact | dpv_ai:BayesianNetwork, dpv_ai_owl:BayesianNetwork |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BayesianNetwork
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.3.1
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#BayesianNetwork
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Probabilistic technique that uses Bayesian inference for probability

  computations using a directed acyclic graph'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Bayesian Network
exact_mappings:
- dpv_ai:BayesianNetwork
- dpv_ai_owl:BayesianNetwork
is_a: StatisticalTechnique
mixins:
- Technique
class_uri: ai:BayesianNetwork

```
</details>

### Induced

<details>
```yaml
name: BayesianNetwork
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.3.1
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#BayesianNetwork
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Probabilistic technique that uses Bayesian inference for probability

  computations using a directed acyclic graph'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Bayesian Network
exact_mappings:
- dpv_ai:BayesianNetwork
- dpv_ai_owl:BayesianNetwork
is_a: StatisticalTechnique
mixins:
- Technique
class_uri: ai:BayesianNetwork

```
</details></div>