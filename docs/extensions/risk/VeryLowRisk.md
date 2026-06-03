---
search:
  boost: 10.0
---

# Class: VeryLowRisk 


_Level where Risk is Very Low_



<div data-search-exclude markdown="1">



URI: [risk:VeryLowRisk](https://w3id.org/lmodel/dpv/risk/VeryLowRisk)





```mermaid
 classDiagram
    class VeryLowRisk
    click VeryLowRisk href "../VeryLowRisk/"
      7RiskLevels <|-- VeryLowRisk
        click 7RiskLevels href "../7RiskLevels/"
      5RiskLevels <|-- VeryLowRisk
        click 5RiskLevels href "../5RiskLevels/"
      
      
```





## Inheritance
* [5RiskLevels](5RiskLevels.md)
    * **VeryLowRisk** [ [7RiskLevels](7RiskLevels.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:VeryLowRisk](https://w3id.org/lmodel/dpv/risk/VeryLowRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Very Low Risk


## Comments

* The suggested quantitative value for this concept is 0.1 on a scale of 0
to 1



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#VeryLowRisk |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:VeryLowRisk |
| native | risk:VeryLowRisk |
| exact | dpv_risk:VeryLowRisk, dpv_risk_owl:VeryLowRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VeryLowRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#VeryLowRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Risk is Very Low
comments:
- 'The suggested quantitative value for this concept is 0.1 on a scale of 0

  to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Very Low Risk
exact_mappings:
- dpv_risk:VeryLowRisk
- dpv_risk_owl:VeryLowRisk
is_a: 5RiskLevels
mixins:
- 7RiskLevels
class_uri: risk:VeryLowRisk

```
</details>

### Induced

<details>
```yaml
name: VeryLowRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#VeryLowRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Risk is Very Low
comments:
- 'The suggested quantitative value for this concept is 0.1 on a scale of 0

  to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Very Low Risk
exact_mappings:
- dpv_risk:VeryLowRisk
- dpv_risk_owl:VeryLowRisk
is_a: 5RiskLevels
mixins:
- 7RiskLevels
class_uri: risk:VeryLowRisk

```
</details></div>