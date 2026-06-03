---
search:
  boost: 10.0
---

# Class: 7SeverityLevels 


_Scale with 7 Severity Levels from Extremely High to Extremely Low_



<div data-search-exclude markdown="1">



URI: [risk:7SeverityLevels](https://w3id.org/lmodel/dpv/risk/7SeverityLevels)





```mermaid
 classDiagram
    class 7SeverityLevels
    click 7SeverityLevels href "../7SeverityLevels/"
      7SeverityLevels <|-- ExtremelyHighSeverity
        click ExtremelyHighSeverity href "../ExtremelyHighSeverity/"
      7SeverityLevels <|-- ExtremelyLowSeverity
        click ExtremelyLowSeverity href "../ExtremelyLowSeverity/"
      7SeverityLevels <|-- HighSeverity
        click HighSeverity href "../HighSeverity/"
      7SeverityLevels <|-- LowSeverity
        click LowSeverity href "../LowSeverity/"
      7SeverityLevels <|-- ModerateSeverity
        click ModerateSeverity href "../ModerateSeverity/"
      7SeverityLevels <|-- VeryHighSeverity
        click VeryHighSeverity href "../VeryHighSeverity/"
      7SeverityLevels <|-- VeryLowSeverity
        click VeryLowSeverity href "../VeryLowSeverity/"
      
      
```





## Inheritance
* **7SeverityLevels**
    * [ExtremelyHighSeverity](ExtremelyHighSeverity.md)
    * [ExtremelyLowSeverity](ExtremelyLowSeverity.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:7SeverityLevels](https://w3id.org/lmodel/dpv/risk/7SeverityLevels) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* 7 Severity Levels




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#7SeverityLevels |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:7SeverityLevels |
| native | risk:7SeverityLevels |
| exact | dpv_risk:7SeverityLevels, dpv_risk_owl:7SeverityLevels |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: 7SeverityLevels
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#7SeverityLevels
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Scale with 7 Severity Levels from Extremely High to Extremely Low
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- 7 Severity Levels
exact_mappings:
- dpv_risk:7SeverityLevels
- dpv_risk_owl:7SeverityLevels
class_uri: risk:7SeverityLevels

```
</details>

### Induced

<details>
```yaml
name: 7SeverityLevels
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#7SeverityLevels
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Scale with 7 Severity Levels from Extremely High to Extremely Low
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- 7 Severity Levels
exact_mappings:
- dpv_risk:7SeverityLevels
- dpv_risk_owl:7SeverityLevels
class_uri: risk:7SeverityLevels

```
</details></div>