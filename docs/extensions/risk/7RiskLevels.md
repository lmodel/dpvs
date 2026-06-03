---
search:
  boost: 10.0
---

# Class: 7RiskLevels 


_Scale with 7 Risk Levels from Extremely High to Extremely Low_



<div data-search-exclude markdown="1">



URI: [risk:7RiskLevels](https://w3id.org/lmodel/dpv/risk/7RiskLevels)





```mermaid
 classDiagram
    class 7RiskLevels
    click 7RiskLevels href "../7RiskLevels/"
      7RiskLevels <|-- ExtremelyHighRisk
        click ExtremelyHighRisk href "../ExtremelyHighRisk/"
      7RiskLevels <|-- ExtremelyLowRisk
        click ExtremelyLowRisk href "../ExtremelyLowRisk/"
      7RiskLevels <|-- HighRisk
        click HighRisk href "../HighRisk/"
      7RiskLevels <|-- LowRisk
        click LowRisk href "../LowRisk/"
      7RiskLevels <|-- ModerateRisk
        click ModerateRisk href "../ModerateRisk/"
      7RiskLevels <|-- VeryHighRisk
        click VeryHighRisk href "../VeryHighRisk/"
      7RiskLevels <|-- VeryLowRisk
        click VeryLowRisk href "../VeryLowRisk/"
      
      
```





## Inheritance
* **7RiskLevels**
    * [ExtremelyHighRisk](ExtremelyHighRisk.md)
    * [ExtremelyLowRisk](ExtremelyLowRisk.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:7RiskLevels](https://w3id.org/lmodel/dpv/risk/7RiskLevels) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* 7 Risk Levels




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#7RiskLevels |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:7RiskLevels |
| native | risk:7RiskLevels |
| exact | dpv_risk:7RiskLevels, dpv_risk_owl:7RiskLevels |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: 7RiskLevels
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#7RiskLevels
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Scale with 7 Risk Levels from Extremely High to Extremely Low
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- 7 Risk Levels
exact_mappings:
- dpv_risk:7RiskLevels
- dpv_risk_owl:7RiskLevels
class_uri: risk:7RiskLevels

```
</details>

### Induced

<details>
```yaml
name: 7RiskLevels
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#7RiskLevels
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Scale with 7 Risk Levels from Extremely High to Extremely Low
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- 7 Risk Levels
exact_mappings:
- dpv_risk:7RiskLevels
- dpv_risk_owl:7RiskLevels
class_uri: risk:7RiskLevels

```
</details></div>