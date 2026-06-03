---
search:
  boost: 10.0
---

# Class: VeryLowSeverity 


_Level where Severity is Very Low_



<div data-search-exclude markdown="1">



URI: [risk:VeryLowSeverity](https://w3id.org/lmodel/dpv/risk/VeryLowSeverity)





```mermaid
 classDiagram
    class VeryLowSeverity
    click VeryLowSeverity href "../VeryLowSeverity/"
      7SeverityLevels <|-- VeryLowSeverity
        click 7SeverityLevels href "../7SeverityLevels/"
      5SeverityLevels <|-- VeryLowSeverity
        click 5SeverityLevels href "../5SeverityLevels/"
      
      
```





## Inheritance
* [5SeverityLevels](5SeverityLevels.md)
    * **VeryLowSeverity** [ [7SeverityLevels](7SeverityLevels.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:VeryLowSeverity](https://w3id.org/lmodel/dpv/risk/VeryLowSeverity) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Very Low Severity


## Comments

* The suggested quantitative value for this concept is 0.1 on a scale of 0
to 1



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#VeryLowSeverity |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:VeryLowSeverity |
| native | risk:VeryLowSeverity |
| exact | dpv_risk:VeryLowSeverity, dpv_risk_owl:VeryLowSeverity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VeryLowSeverity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#VeryLowSeverity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Severity is Very Low
comments:
- 'The suggested quantitative value for this concept is 0.1 on a scale of 0

  to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Very Low Severity
exact_mappings:
- dpv_risk:VeryLowSeverity
- dpv_risk_owl:VeryLowSeverity
is_a: 5SeverityLevels
mixins:
- 7SeverityLevels
class_uri: risk:VeryLowSeverity

```
</details>

### Induced

<details>
```yaml
name: VeryLowSeverity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#VeryLowSeverity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Severity is Very Low
comments:
- 'The suggested quantitative value for this concept is 0.1 on a scale of 0

  to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Very Low Severity
exact_mappings:
- dpv_risk:VeryLowSeverity
- dpv_risk_owl:VeryLowSeverity
is_a: 5SeverityLevels
mixins:
- 7SeverityLevels
class_uri: risk:VeryLowSeverity

```
</details></div>