---
search:
  boost: 10.0
---

# Class: 5RiskLevels 


_Scale with 5 Risk Levels from Very High to Very Low_



<div data-search-exclude markdown="1">



URI: [risk:5RiskLevels](https://w3id.org/lmodel/dpv/risk/5RiskLevels)





```mermaid
 classDiagram
    class 5RiskLevels
    click 5RiskLevels href "../5RiskLevels/"
      5RiskLevels <|-- HighRisk
        click HighRisk href "../HighRisk/"
      5RiskLevels <|-- LowRisk
        click LowRisk href "../LowRisk/"
      5RiskLevels <|-- ModerateRisk
        click ModerateRisk href "../ModerateRisk/"
      5RiskLevels <|-- VeryHighRisk
        click VeryHighRisk href "../VeryHighRisk/"
      5RiskLevels <|-- VeryLowRisk
        click VeryLowRisk href "../VeryLowRisk/"
      
      
```





## Inheritance
* **5RiskLevels**
    * [VeryHighRisk](VeryHighRisk.md) [ [7RiskLevels](7RiskLevels.md)]
    * [VeryLowRisk](VeryLowRisk.md) [ [7RiskLevels](7RiskLevels.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:5RiskLevels](https://w3id.org/lmodel/dpv/risk/5RiskLevels) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* 5 Risk Levels




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#5RiskLevels |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:5RiskLevels |
| native | risk:5RiskLevels |
| exact | dpv_risk:5RiskLevels, dpv_risk_owl:5RiskLevels |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: 5RiskLevels
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#5RiskLevels
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Scale with 5 Risk Levels from Very High to Very Low
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- 5 Risk Levels
exact_mappings:
- dpv_risk:5RiskLevels
- dpv_risk_owl:5RiskLevels
class_uri: risk:5RiskLevels

```
</details>

### Induced

<details>
```yaml
name: 5RiskLevels
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#5RiskLevels
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Scale with 5 Risk Levels from Very High to Very Low
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- 5 Risk Levels
exact_mappings:
- dpv_risk:5RiskLevels
- dpv_risk_owl:5RiskLevels
class_uri: risk:5RiskLevels

```
</details></div>