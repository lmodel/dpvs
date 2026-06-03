---
search:
  boost: 10.0
---

# Class: ExtremelyLowLikelihood 


_Level where Likelihood is Extremely Low_



<div data-search-exclude markdown="1">



URI: [risk:ExtremelyLowLikelihood](https://w3id.org/lmodel/dpv/risk/ExtremelyLowLikelihood)





```mermaid
 classDiagram
    class ExtremelyLowLikelihood
    click ExtremelyLowLikelihood href "../ExtremelyLowLikelihood/"
      7LikelihoodLevels <|-- ExtremelyLowLikelihood
        click 7LikelihoodLevels href "../7LikelihoodLevels/"
      
      
```





## Inheritance
* [7LikelihoodLevels](7LikelihoodLevels.md)
    * **ExtremelyLowLikelihood**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ExtremelyLowLikelihood](https://w3id.org/lmodel/dpv/risk/ExtremelyLowLikelihood) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Extremely Low Likelihood


## Comments

* The suggested quantitative value for this concept is 0.01 on a scale of
0 to 1



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ExtremelyLowLikelihood |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ExtremelyLowLikelihood |
| native | risk:ExtremelyLowLikelihood |
| exact | dpv_risk:ExtremelyLowLikelihood, dpv_risk_owl:ExtremelyLowLikelihood |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExtremelyLowLikelihood
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ExtremelyLowLikelihood
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Likelihood is Extremely Low
comments:
- 'The suggested quantitative value for this concept is 0.01 on a scale of

  0 to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Extremely Low Likelihood
exact_mappings:
- dpv_risk:ExtremelyLowLikelihood
- dpv_risk_owl:ExtremelyLowLikelihood
is_a: 7LikelihoodLevels
class_uri: risk:ExtremelyLowLikelihood

```
</details>

### Induced

<details>
```yaml
name: ExtremelyLowLikelihood
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ExtremelyLowLikelihood
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Likelihood is Extremely Low
comments:
- 'The suggested quantitative value for this concept is 0.01 on a scale of

  0 to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Extremely Low Likelihood
exact_mappings:
- dpv_risk:ExtremelyLowLikelihood
- dpv_risk_owl:ExtremelyLowLikelihood
is_a: 7LikelihoodLevels
class_uri: risk:ExtremelyLowLikelihood

```
</details></div>