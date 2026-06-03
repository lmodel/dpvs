---
search:
  boost: 10.0
---

# Class: 5SeverityLevels 


_Scale with 5 Severity Levels from Very High to Very Low_



<div data-search-exclude markdown="1">



URI: [risk:5SeverityLevels](https://w3id.org/lmodel/dpv/risk/5SeverityLevels)





```mermaid
 classDiagram
    class 5SeverityLevels
    click 5SeverityLevels href "../5SeverityLevels/"
      5SeverityLevels <|-- HighSeverity
        click HighSeverity href "../HighSeverity/"
      5SeverityLevels <|-- LowSeverity
        click LowSeverity href "../LowSeverity/"
      5SeverityLevels <|-- ModerateSeverity
        click ModerateSeverity href "../ModerateSeverity/"
      5SeverityLevels <|-- VeryHighSeverity
        click VeryHighSeverity href "../VeryHighSeverity/"
      5SeverityLevels <|-- VeryLowSeverity
        click VeryLowSeverity href "../VeryLowSeverity/"
      
      
```





## Inheritance
* **5SeverityLevels**
    * [VeryHighSeverity](VeryHighSeverity.md) [ [7SeverityLevels](7SeverityLevels.md)]
    * [VeryLowSeverity](VeryLowSeverity.md) [ [7SeverityLevels](7SeverityLevels.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:5SeverityLevels](https://w3id.org/lmodel/dpv/risk/5SeverityLevels) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* 5 Severity Levels




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#5SeverityLevels |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:5SeverityLevels |
| native | risk:5SeverityLevels |
| exact | dpv_risk:5SeverityLevels, dpv_risk_owl:5SeverityLevels |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: 5SeverityLevels
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#5SeverityLevels
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Scale with 5 Severity Levels from Very High to Very Low
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- 5 Severity Levels
exact_mappings:
- dpv_risk:5SeverityLevels
- dpv_risk_owl:5SeverityLevels
class_uri: risk:5SeverityLevels

```
</details>

### Induced

<details>
```yaml
name: 5SeverityLevels
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#5SeverityLevels
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Scale with 5 Severity Levels from Very High to Very Low
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- 5 Severity Levels
exact_mappings:
- dpv_risk:5SeverityLevels
- dpv_risk_owl:5SeverityLevels
class_uri: risk:5SeverityLevels

```
</details></div>