---
search:
  boost: 10.0
---

# Class: ModerateRisk 


_Level where Risk is Moderate_



<div data-search-exclude markdown="1">



URI: [risk:ModerateRisk](https://w3id.org/lmodel/dpv/risk/ModerateRisk)





```mermaid
 classDiagram
    class ModerateRisk
    click ModerateRisk href "../ModerateRisk/"
      5RiskLevels <|-- ModerateRisk
        click 5RiskLevels href "../5RiskLevels/"
      7RiskLevels <|-- ModerateRisk
        click 7RiskLevels href "../7RiskLevels/"
      3RiskLevels <|-- ModerateRisk
        click 3RiskLevels href "../3RiskLevels/"
      
      
```





## Inheritance
* [3RiskLevels](3RiskLevels.md)
    * **ModerateRisk** [ [5RiskLevels](5RiskLevels.md) [7RiskLevels](7RiskLevels.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ModerateRisk](https://w3id.org/lmodel/dpv/risk/ModerateRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Moderate Risk


## Comments

* The suggested quantitative value for this concept is 0.5 on a scale of 0
to 1



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ModerateRisk |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ModerateRisk |
| native | risk:ModerateRisk |
| exact | dpv_risk:ModerateRisk, dpv_risk_owl:ModerateRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ModerateRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ModerateRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Risk is Moderate
comments:
- 'The suggested quantitative value for this concept is 0.5 on a scale of 0

  to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Moderate Risk
exact_mappings:
- dpv_risk:ModerateRisk
- dpv_risk_owl:ModerateRisk
is_a: 3RiskLevels
mixins:
- 5RiskLevels
- 7RiskLevels
class_uri: risk:ModerateRisk

```
</details>

### Induced

<details>
```yaml
name: ModerateRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ModerateRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Risk is Moderate
comments:
- 'The suggested quantitative value for this concept is 0.5 on a scale of 0

  to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Moderate Risk
exact_mappings:
- dpv_risk:ModerateRisk
- dpv_risk_owl:ModerateRisk
is_a: 3RiskLevels
mixins:
- 5RiskLevels
- 7RiskLevels
class_uri: risk:ModerateRisk

```
</details></div>