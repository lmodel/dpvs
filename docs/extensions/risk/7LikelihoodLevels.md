---
search:
  boost: 10.0
---

# Class: 7LikelihoodLevels 


_Scale with 7 Likelihood Levels from Extremely High to Extremely Low_



<div data-search-exclude markdown="1">



URI: [risk:7LikelihoodLevels](https://w3id.org/lmodel/dpv/risk/7LikelihoodLevels)





```mermaid
 classDiagram
    class 7LikelihoodLevels
    click 7LikelihoodLevels href "../7LikelihoodLevels/"
      7LikelihoodLevels <|-- ExtremelyHighLikelihood
        click ExtremelyHighLikelihood href "../ExtremelyHighLikelihood/"
      7LikelihoodLevels <|-- ExtremelyLowLikelihood
        click ExtremelyLowLikelihood href "../ExtremelyLowLikelihood/"
      7LikelihoodLevels <|-- HighLikelihood
        click HighLikelihood href "../HighLikelihood/"
      7LikelihoodLevels <|-- LowLikelihood
        click LowLikelihood href "../LowLikelihood/"
      7LikelihoodLevels <|-- ModerateLikelihood
        click ModerateLikelihood href "../ModerateLikelihood/"
      7LikelihoodLevels <|-- VeryHighLikelihood
        click VeryHighLikelihood href "../VeryHighLikelihood/"
      7LikelihoodLevels <|-- VeryLowLikelihood
        click VeryLowLikelihood href "../VeryLowLikelihood/"
      
      
```





## Inheritance
* **7LikelihoodLevels**
    * [ExtremelyHighLikelihood](ExtremelyHighLikelihood.md)
    * [ExtremelyLowLikelihood](ExtremelyLowLikelihood.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:7LikelihoodLevels](https://w3id.org/lmodel/dpv/risk/7LikelihoodLevels) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* 7 Likelihood Levels




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#7LikelihoodLevels |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:7LikelihoodLevels |
| native | risk:7LikelihoodLevels |
| exact | dpv_risk:7LikelihoodLevels, dpv_risk_owl:7LikelihoodLevels |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: 7LikelihoodLevels
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#7LikelihoodLevels
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Scale with 7 Likelihood Levels from Extremely High to Extremely Low
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- 7 Likelihood Levels
exact_mappings:
- dpv_risk:7LikelihoodLevels
- dpv_risk_owl:7LikelihoodLevels
class_uri: risk:7LikelihoodLevels

```
</details>

### Induced

<details>
```yaml
name: 7LikelihoodLevels
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#7LikelihoodLevels
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Scale with 7 Likelihood Levels from Extremely High to Extremely Low
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- 7 Likelihood Levels
exact_mappings:
- dpv_risk:7LikelihoodLevels
- dpv_risk_owl:7LikelihoodLevels
class_uri: risk:7LikelihoodLevels

```
</details></div>