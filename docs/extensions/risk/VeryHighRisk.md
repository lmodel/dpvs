---
search:
  boost: 10.0
---

# Class: VeryHighRisk 


_Level where Risk is Very High_



<div data-search-exclude markdown="1">



URI: [risk:VeryHighRisk](https://w3id.org/lmodel/dpv/risk/VeryHighRisk)





```mermaid
 classDiagram
    class VeryHighRisk
    click VeryHighRisk href "../VeryHighRisk/"
      7RiskLevels <|-- VeryHighRisk
        click 7RiskLevels href "../7RiskLevels/"
      5RiskLevels <|-- VeryHighRisk
        click 5RiskLevels href "../5RiskLevels/"
      
      
```





## Inheritance
* [5RiskLevels](5RiskLevels.md)
    * **VeryHighRisk** [ [7RiskLevels](7RiskLevels.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:VeryHighRisk](https://w3id.org/lmodel/dpv/risk/VeryHighRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Very High Risk


## Comments

* The suggested quantitative value for this concept is 0.9 on a scale of 0
to 1



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#VeryHighRisk |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:VeryHighRisk |
| native | risk:VeryHighRisk |
| exact | dpv_risk:VeryHighRisk, dpv_risk_owl:VeryHighRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VeryHighRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#VeryHighRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Risk is Very High
comments:
- 'The suggested quantitative value for this concept is 0.9 on a scale of 0

  to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Very High Risk
exact_mappings:
- dpv_risk:VeryHighRisk
- dpv_risk_owl:VeryHighRisk
is_a: 5RiskLevels
mixins:
- 7RiskLevels
class_uri: risk:VeryHighRisk

```
</details>

### Induced

<details>
```yaml
name: VeryHighRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#VeryHighRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Risk is Very High
comments:
- 'The suggested quantitative value for this concept is 0.9 on a scale of 0

  to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Very High Risk
exact_mappings:
- dpv_risk:VeryHighRisk
- dpv_risk_owl:VeryHighRisk
is_a: 5RiskLevels
mixins:
- 7RiskLevels
class_uri: risk:VeryHighRisk

```
</details></div>