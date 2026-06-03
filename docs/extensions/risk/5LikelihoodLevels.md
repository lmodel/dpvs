---
search:
  boost: 10.0
---

# Class: 5LikelihoodLevels 


_Scale with 5 Likelihood Levels from Very High to Very Low_



<div data-search-exclude markdown="1">



URI: [risk:5LikelihoodLevels](https://w3id.org/lmodel/dpv/risk/5LikelihoodLevels)





```mermaid
 classDiagram
    class 5LikelihoodLevels
    click 5LikelihoodLevels href "../5LikelihoodLevels/"
      5LikelihoodLevels <|-- HighLikelihood
        click HighLikelihood href "../HighLikelihood/"
      5LikelihoodLevels <|-- LowLikelihood
        click LowLikelihood href "../LowLikelihood/"
      5LikelihoodLevels <|-- ModerateLikelihood
        click ModerateLikelihood href "../ModerateLikelihood/"
      5LikelihoodLevels <|-- VeryHighLikelihood
        click VeryHighLikelihood href "../VeryHighLikelihood/"
      5LikelihoodLevels <|-- VeryLowLikelihood
        click VeryLowLikelihood href "../VeryLowLikelihood/"
      
      
```





## Inheritance
* **5LikelihoodLevels**
    * [VeryHighLikelihood](VeryHighLikelihood.md) [ [7LikelihoodLevels](7LikelihoodLevels.md)]
    * [VeryLowLikelihood](VeryLowLikelihood.md) [ [7LikelihoodLevels](7LikelihoodLevels.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:5LikelihoodLevels](https://w3id.org/lmodel/dpv/risk/5LikelihoodLevels) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* 5 Likelihood Levels




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#5LikelihoodLevels |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:5LikelihoodLevels |
| native | risk:5LikelihoodLevels |
| exact | dpv_risk:5LikelihoodLevels, dpv_risk_owl:5LikelihoodLevels |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: 5LikelihoodLevels
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#5LikelihoodLevels
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Scale with 5 Likelihood Levels from Very High to Very Low
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- 5 Likelihood Levels
exact_mappings:
- dpv_risk:5LikelihoodLevels
- dpv_risk_owl:5LikelihoodLevels
class_uri: risk:5LikelihoodLevels

```
</details>

### Induced

<details>
```yaml
name: 5LikelihoodLevels
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#5LikelihoodLevels
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Scale with 5 Likelihood Levels from Very High to Very Low
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- 5 Likelihood Levels
exact_mappings:
- dpv_risk:5LikelihoodLevels
- dpv_risk_owl:5LikelihoodLevels
class_uri: risk:5LikelihoodLevels

```
</details></div>