---
search:
  boost: 10.0
---

# Class: LowLikelihood 


_Level where Likelihood is Low_



<div data-search-exclude markdown="1">



URI: [risk:LowLikelihood](https://w3id.org/lmodel/dpv/risk/LowLikelihood)





```mermaid
 classDiagram
    class LowLikelihood
    click LowLikelihood href "../LowLikelihood/"
      5LikelihoodLevels <|-- LowLikelihood
        click 5LikelihoodLevels href "../5LikelihoodLevels/"
      7LikelihoodLevels <|-- LowLikelihood
        click 7LikelihoodLevels href "../7LikelihoodLevels/"
      3LikelihoodLevels <|-- LowLikelihood
        click 3LikelihoodLevels href "../3LikelihoodLevels/"
      
      
```





## Inheritance
* [3LikelihoodLevels](3LikelihoodLevels.md)
    * **LowLikelihood** [ [5LikelihoodLevels](5LikelihoodLevels.md) [7LikelihoodLevels](7LikelihoodLevels.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:LowLikelihood](https://w3id.org/lmodel/dpv/risk/LowLikelihood) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Low Likelihood


## Comments

* The suggested quantitative value for this concept is 0.25 on a scale of
0 to 1



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#LowLikelihood |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:LowLikelihood |
| native | risk:LowLikelihood |
| exact | dpv_risk:LowLikelihood, dpv_risk_owl:LowLikelihood |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LowLikelihood
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#LowLikelihood
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Likelihood is Low
comments:
- 'The suggested quantitative value for this concept is 0.25 on a scale of

  0 to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Low Likelihood
exact_mappings:
- dpv_risk:LowLikelihood
- dpv_risk_owl:LowLikelihood
is_a: 3LikelihoodLevels
mixins:
- 5LikelihoodLevels
- 7LikelihoodLevels
class_uri: risk:LowLikelihood

```
</details>

### Induced

<details>
```yaml
name: LowLikelihood
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#LowLikelihood
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Likelihood is Low
comments:
- 'The suggested quantitative value for this concept is 0.25 on a scale of

  0 to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Low Likelihood
exact_mappings:
- dpv_risk:LowLikelihood
- dpv_risk_owl:LowLikelihood
is_a: 3LikelihoodLevels
mixins:
- 5LikelihoodLevels
- 7LikelihoodLevels
class_uri: risk:LowLikelihood

```
</details></div>