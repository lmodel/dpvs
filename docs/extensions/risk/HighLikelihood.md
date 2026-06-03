---
search:
  boost: 10.0
---

# Class: HighLikelihood 


_Level where Likelihood is High_



<div data-search-exclude markdown="1">



URI: [risk:HighLikelihood](https://w3id.org/lmodel/dpv/risk/HighLikelihood)





```mermaid
 classDiagram
    class HighLikelihood
    click HighLikelihood href "../HighLikelihood/"
      5LikelihoodLevels <|-- HighLikelihood
        click 5LikelihoodLevels href "../5LikelihoodLevels/"
      7LikelihoodLevels <|-- HighLikelihood
        click 7LikelihoodLevels href "../7LikelihoodLevels/"
      3LikelihoodLevels <|-- HighLikelihood
        click 3LikelihoodLevels href "../3LikelihoodLevels/"
      
      
```





## Inheritance
* [3LikelihoodLevels](3LikelihoodLevels.md)
    * **HighLikelihood** [ [5LikelihoodLevels](5LikelihoodLevels.md) [7LikelihoodLevels](7LikelihoodLevels.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:HighLikelihood](https://w3id.org/lmodel/dpv/risk/HighLikelihood) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* High Likelihood


## Comments

* The suggested quantitative value for this concept is 0.75 on a scale of
0 to 1



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#HighLikelihood |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:HighLikelihood |
| native | risk:HighLikelihood |
| exact | dpv_risk:HighLikelihood, dpv_risk_owl:HighLikelihood |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HighLikelihood
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#HighLikelihood
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Likelihood is High
comments:
- 'The suggested quantitative value for this concept is 0.75 on a scale of

  0 to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- High Likelihood
exact_mappings:
- dpv_risk:HighLikelihood
- dpv_risk_owl:HighLikelihood
is_a: 3LikelihoodLevels
mixins:
- 5LikelihoodLevels
- 7LikelihoodLevels
class_uri: risk:HighLikelihood

```
</details>

### Induced

<details>
```yaml
name: HighLikelihood
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#HighLikelihood
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Likelihood is High
comments:
- 'The suggested quantitative value for this concept is 0.75 on a scale of

  0 to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- High Likelihood
exact_mappings:
- dpv_risk:HighLikelihood
- dpv_risk_owl:HighLikelihood
is_a: 3LikelihoodLevels
mixins:
- 5LikelihoodLevels
- 7LikelihoodLevels
class_uri: risk:HighLikelihood

```
</details></div>