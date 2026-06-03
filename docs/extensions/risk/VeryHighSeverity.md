---
search:
  boost: 10.0
---

# Class: VeryHighSeverity 


_Level where Severity is Very High_



<div data-search-exclude markdown="1">



URI: [risk:VeryHighSeverity](https://w3id.org/lmodel/dpv/risk/VeryHighSeverity)





```mermaid
 classDiagram
    class VeryHighSeverity
    click VeryHighSeverity href "../VeryHighSeverity/"
      7SeverityLevels <|-- VeryHighSeverity
        click 7SeverityLevels href "../7SeverityLevels/"
      5SeverityLevels <|-- VeryHighSeverity
        click 5SeverityLevels href "../5SeverityLevels/"
      
      
```





## Inheritance
* [5SeverityLevels](5SeverityLevels.md)
    * **VeryHighSeverity** [ [7SeverityLevels](7SeverityLevels.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:VeryHighSeverity](https://w3id.org/lmodel/dpv/risk/VeryHighSeverity) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Very High Severity


## Comments

* The suggested quantitative value for this concept is 0.9 on a scale of 0
to 1



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#VeryHighSeverity |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:VeryHighSeverity |
| native | risk:VeryHighSeverity |
| exact | dpv_risk:VeryHighSeverity, dpv_risk_owl:VeryHighSeverity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VeryHighSeverity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#VeryHighSeverity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Severity is Very High
comments:
- 'The suggested quantitative value for this concept is 0.9 on a scale of 0

  to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Very High Severity
exact_mappings:
- dpv_risk:VeryHighSeverity
- dpv_risk_owl:VeryHighSeverity
is_a: 5SeverityLevels
mixins:
- 7SeverityLevels
class_uri: risk:VeryHighSeverity

```
</details>

### Induced

<details>
```yaml
name: VeryHighSeverity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#VeryHighSeverity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Severity is Very High
comments:
- 'The suggested quantitative value for this concept is 0.9 on a scale of 0

  to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Very High Severity
exact_mappings:
- dpv_risk:VeryHighSeverity
- dpv_risk_owl:VeryHighSeverity
is_a: 5SeverityLevels
mixins:
- 7SeverityLevels
class_uri: risk:VeryHighSeverity

```
</details></div>