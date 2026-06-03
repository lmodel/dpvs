---
search:
  boost: 10.0
---

# Class: 3RiskLevels 


_Scale with 3 Risk Levels from High to Low_



<div data-search-exclude markdown="1">



URI: [risk:3RiskLevels](https://w3id.org/lmodel/dpv/risk/3RiskLevels)





```mermaid
 classDiagram
    class 3RiskLevels
    click 3RiskLevels href "../3RiskLevels/"
      3RiskLevels <|-- HighRisk
        click HighRisk href "../HighRisk/"
      3RiskLevels <|-- LowRisk
        click LowRisk href "../LowRisk/"
      3RiskLevels <|-- ModerateRisk
        click ModerateRisk href "../ModerateRisk/"
      
      
```





## Inheritance
* **3RiskLevels**
    * [HighRisk](HighRisk.md) [ [5RiskLevels](5RiskLevels.md) [7RiskLevels](7RiskLevels.md)]
    * [LowRisk](LowRisk.md) [ [5RiskLevels](5RiskLevels.md) [7RiskLevels](7RiskLevels.md)]
    * [ModerateRisk](ModerateRisk.md) [ [5RiskLevels](5RiskLevels.md) [7RiskLevels](7RiskLevels.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:3RiskLevels](https://w3id.org/lmodel/dpv/risk/3RiskLevels) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* 3 Risk Levels




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#3RiskLevels |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:3RiskLevels |
| native | risk:3RiskLevels |
| exact | dpv_risk:3RiskLevels, dpv_risk_owl:3RiskLevels |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: 3RiskLevels
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#3RiskLevels
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Scale with 3 Risk Levels from High to Low
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- 3 Risk Levels
exact_mappings:
- dpv_risk:3RiskLevels
- dpv_risk_owl:3RiskLevels
class_uri: risk:3RiskLevels

```
</details>

### Induced

<details>
```yaml
name: 3RiskLevels
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#3RiskLevels
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Scale with 3 Risk Levels from High to Low
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- 3 Risk Levels
exact_mappings:
- dpv_risk:3RiskLevels
- dpv_risk_owl:3RiskLevels
class_uri: risk:3RiskLevels

```
</details></div>