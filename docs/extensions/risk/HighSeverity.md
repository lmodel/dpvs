---
search:
  boost: 10.0
---

# Class: HighSeverity 


_Level where Severity is High_



<div data-search-exclude markdown="1">



URI: [risk:HighSeverity](https://w3id.org/lmodel/dpv/risk/HighSeverity)





```mermaid
 classDiagram
    class HighSeverity
    click HighSeverity href "../HighSeverity/"
      5SeverityLevels <|-- HighSeverity
        click 5SeverityLevels href "../5SeverityLevels/"
      7SeverityLevels <|-- HighSeverity
        click 7SeverityLevels href "../7SeverityLevels/"
      3SeverityLevels <|-- HighSeverity
        click 3SeverityLevels href "../3SeverityLevels/"
      
      
```





## Inheritance
* [3SeverityLevels](3SeverityLevels.md)
    * **HighSeverity** [ [5SeverityLevels](5SeverityLevels.md) [7SeverityLevels](7SeverityLevels.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:HighSeverity](https://w3id.org/lmodel/dpv/risk/HighSeverity) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* High Severity


## Comments

* The suggested quantitative value for this concept is 0.75 on a scale of
0 to 1



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#HighSeverity |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:HighSeverity |
| native | risk:HighSeverity |
| exact | dpv_risk:HighSeverity, dpv_risk_owl:HighSeverity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HighSeverity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#HighSeverity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Severity is High
comments:
- 'The suggested quantitative value for this concept is 0.75 on a scale of

  0 to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- High Severity
exact_mappings:
- dpv_risk:HighSeverity
- dpv_risk_owl:HighSeverity
is_a: 3SeverityLevels
mixins:
- 5SeverityLevels
- 7SeverityLevels
class_uri: risk:HighSeverity

```
</details>

### Induced

<details>
```yaml
name: HighSeverity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#HighSeverity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Severity is High
comments:
- 'The suggested quantitative value for this concept is 0.75 on a scale of

  0 to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- High Severity
exact_mappings:
- dpv_risk:HighSeverity
- dpv_risk_owl:HighSeverity
is_a: 3SeverityLevels
mixins:
- 5SeverityLevels
- 7SeverityLevels
class_uri: risk:HighSeverity

```
</details></div>