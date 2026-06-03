---
search:
  boost: 10.0
---

# Class: VeryHighLikelihood 


_Level where Likelihood is Very High_



<div data-search-exclude markdown="1">



URI: [risk:VeryHighLikelihood](https://w3id.org/lmodel/dpv/risk/VeryHighLikelihood)





```mermaid
 classDiagram
    class VeryHighLikelihood
    click VeryHighLikelihood href "../VeryHighLikelihood/"
      7LikelihoodLevels <|-- VeryHighLikelihood
        click 7LikelihoodLevels href "../7LikelihoodLevels/"
      5LikelihoodLevels <|-- VeryHighLikelihood
        click 5LikelihoodLevels href "../5LikelihoodLevels/"
      
      
```





## Inheritance
* [5LikelihoodLevels](5LikelihoodLevels.md)
    * **VeryHighLikelihood** [ [7LikelihoodLevels](7LikelihoodLevels.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:VeryHighLikelihood](https://w3id.org/lmodel/dpv/risk/VeryHighLikelihood) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Very High Likelihood


## Comments

* The suggested quantitative value for this concept is 0.9 on a scale of 0
to 1



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#VeryHighLikelihood |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:VeryHighLikelihood |
| native | risk:VeryHighLikelihood |
| exact | dpv_risk:VeryHighLikelihood, dpv_risk_owl:VeryHighLikelihood |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VeryHighLikelihood
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#VeryHighLikelihood
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Likelihood is Very High
comments:
- 'The suggested quantitative value for this concept is 0.9 on a scale of 0

  to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Very High Likelihood
exact_mappings:
- dpv_risk:VeryHighLikelihood
- dpv_risk_owl:VeryHighLikelihood
is_a: 5LikelihoodLevels
mixins:
- 7LikelihoodLevels
class_uri: risk:VeryHighLikelihood

```
</details>

### Induced

<details>
```yaml
name: VeryHighLikelihood
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#VeryHighLikelihood
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Likelihood is Very High
comments:
- 'The suggested quantitative value for this concept is 0.9 on a scale of 0

  to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Very High Likelihood
exact_mappings:
- dpv_risk:VeryHighLikelihood
- dpv_risk_owl:VeryHighLikelihood
is_a: 5LikelihoodLevels
mixins:
- 7LikelihoodLevels
class_uri: risk:VeryHighLikelihood

```
</details></div>