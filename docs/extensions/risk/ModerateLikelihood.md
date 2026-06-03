---
search:
  boost: 10.0
---

# Class: ModerateLikelihood 


_Level where Likelihood is Moderate_



<div data-search-exclude markdown="1">



URI: [risk:ModerateLikelihood](https://w3id.org/lmodel/dpv/risk/ModerateLikelihood)





```mermaid
 classDiagram
    class ModerateLikelihood
    click ModerateLikelihood href "../ModerateLikelihood/"
      5LikelihoodLevels <|-- ModerateLikelihood
        click 5LikelihoodLevels href "../5LikelihoodLevels/"
      7LikelihoodLevels <|-- ModerateLikelihood
        click 7LikelihoodLevels href "../7LikelihoodLevels/"
      3LikelihoodLevels <|-- ModerateLikelihood
        click 3LikelihoodLevels href "../3LikelihoodLevels/"
      
      
```





## Inheritance
* [3LikelihoodLevels](3LikelihoodLevels.md)
    * **ModerateLikelihood** [ [5LikelihoodLevels](5LikelihoodLevels.md) [7LikelihoodLevels](7LikelihoodLevels.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ModerateLikelihood](https://w3id.org/lmodel/dpv/risk/ModerateLikelihood) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Moderate Likelihood


## Comments

* The suggested quantitative value for this concept is 0.5 on a scale of 0
to 1



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ModerateLikelihood |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ModerateLikelihood |
| native | risk:ModerateLikelihood |
| exact | dpv_risk:ModerateLikelihood, dpv_risk_owl:ModerateLikelihood |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ModerateLikelihood
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ModerateLikelihood
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Likelihood is Moderate
comments:
- 'The suggested quantitative value for this concept is 0.5 on a scale of 0

  to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Moderate Likelihood
exact_mappings:
- dpv_risk:ModerateLikelihood
- dpv_risk_owl:ModerateLikelihood
is_a: 3LikelihoodLevels
mixins:
- 5LikelihoodLevels
- 7LikelihoodLevels
class_uri: risk:ModerateLikelihood

```
</details>

### Induced

<details>
```yaml
name: ModerateLikelihood
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ModerateLikelihood
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Likelihood is Moderate
comments:
- 'The suggested quantitative value for this concept is 0.5 on a scale of 0

  to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Moderate Likelihood
exact_mappings:
- dpv_risk:ModerateLikelihood
- dpv_risk_owl:ModerateLikelihood
is_a: 3LikelihoodLevels
mixins:
- 5LikelihoodLevels
- 7LikelihoodLevels
class_uri: risk:ModerateLikelihood

```
</details></div>