---
search:
  boost: 10.0
---

# Class: HighRisk 


_Level where Risk is High_



<div data-search-exclude markdown="1">



URI: [risk:HighRisk](https://w3id.org/lmodel/dpv/risk/HighRisk)





```mermaid
 classDiagram
    class HighRisk
    click HighRisk href "../HighRisk/"
      5RiskLevels <|-- HighRisk
        click 5RiskLevels href "../5RiskLevels/"
      7RiskLevels <|-- HighRisk
        click 7RiskLevels href "../7RiskLevels/"
      3RiskLevels <|-- HighRisk
        click 3RiskLevels href "../3RiskLevels/"
      
      
```





## Inheritance
* [3RiskLevels](3RiskLevels.md)
    * **HighRisk** [ [5RiskLevels](5RiskLevels.md) [7RiskLevels](7RiskLevels.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:HighRisk](https://w3id.org/lmodel/dpv/risk/HighRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* High Risk


## Comments

* The suggested quantitative value for this concept is 0.75 on a scale of
0 to 1



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#HighRisk |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:HighRisk |
| native | risk:HighRisk |
| exact | dpv_risk:HighRisk, dpv_risk_owl:HighRisk |
| close | iso42001:AIRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HighRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#HighRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Risk is High
comments:
- 'The suggested quantitative value for this concept is 0.75 on a scale of

  0 to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- High Risk
exact_mappings:
- dpv_risk:HighRisk
- dpv_risk_owl:HighRisk
close_mappings:
- iso42001:AIRisk
is_a: 3RiskLevels
mixins:
- 5RiskLevels
- 7RiskLevels
class_uri: risk:HighRisk

```
</details>

### Induced

<details>
```yaml
name: HighRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#HighRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Risk is High
comments:
- 'The suggested quantitative value for this concept is 0.75 on a scale of

  0 to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- High Risk
exact_mappings:
- dpv_risk:HighRisk
- dpv_risk_owl:HighRisk
close_mappings:
- iso42001:AIRisk
is_a: 3RiskLevels
mixins:
- 5RiskLevels
- 7RiskLevels
class_uri: risk:HighRisk

```
</details></div>