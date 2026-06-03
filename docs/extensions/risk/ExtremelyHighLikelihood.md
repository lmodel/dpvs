---
search:
  boost: 10.0
---

# Class: ExtremelyHighLikelihood 


_Level where Likelihood is Extremely High_



<div data-search-exclude markdown="1">



URI: [risk:ExtremelyHighLikelihood](https://w3id.org/lmodel/dpv/risk/ExtremelyHighLikelihood)





```mermaid
 classDiagram
    class ExtremelyHighLikelihood
    click ExtremelyHighLikelihood href "../ExtremelyHighLikelihood/"
      7LikelihoodLevels <|-- ExtremelyHighLikelihood
        click 7LikelihoodLevels href "../7LikelihoodLevels/"
      
      
```





## Inheritance
* [7LikelihoodLevels](7LikelihoodLevels.md)
    * **ExtremelyHighLikelihood**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ExtremelyHighLikelihood](https://w3id.org/lmodel/dpv/risk/ExtremelyHighLikelihood) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Extremely High Likelihood


## Comments

* The suggested quantitative value for this concept is 0.99 on a scale of
0 to 1



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ExtremelyHighLikelihood |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ExtremelyHighLikelihood |
| native | risk:ExtremelyHighLikelihood |
| exact | dpv_risk:ExtremelyHighLikelihood, dpv_risk_owl:ExtremelyHighLikelihood |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExtremelyHighLikelihood
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ExtremelyHighLikelihood
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Likelihood is Extremely High
comments:
- 'The suggested quantitative value for this concept is 0.99 on a scale of

  0 to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Extremely High Likelihood
exact_mappings:
- dpv_risk:ExtremelyHighLikelihood
- dpv_risk_owl:ExtremelyHighLikelihood
is_a: 7LikelihoodLevels
class_uri: risk:ExtremelyHighLikelihood

```
</details>

### Induced

<details>
```yaml
name: ExtremelyHighLikelihood
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ExtremelyHighLikelihood
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Likelihood is Extremely High
comments:
- 'The suggested quantitative value for this concept is 0.99 on a scale of

  0 to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Extremely High Likelihood
exact_mappings:
- dpv_risk:ExtremelyHighLikelihood
- dpv_risk_owl:ExtremelyHighLikelihood
is_a: 7LikelihoodLevels
class_uri: risk:ExtremelyHighLikelihood

```
</details></div>