---
search:
  boost: 10.0
---

# Class: ModerateSeverity 


_Level where Severity is Moderate_



<div data-search-exclude markdown="1">



URI: [risk:ModerateSeverity](https://w3id.org/lmodel/dpv/risk/ModerateSeverity)





```mermaid
 classDiagram
    class ModerateSeverity
    click ModerateSeverity href "../ModerateSeverity/"
      5SeverityLevels <|-- ModerateSeverity
        click 5SeverityLevels href "../5SeverityLevels/"
      7SeverityLevels <|-- ModerateSeverity
        click 7SeverityLevels href "../7SeverityLevels/"
      3SeverityLevels <|-- ModerateSeverity
        click 3SeverityLevels href "../3SeverityLevels/"
      
      
```





## Inheritance
* [3SeverityLevels](3SeverityLevels.md)
    * **ModerateSeverity** [ [5SeverityLevels](5SeverityLevels.md) [7SeverityLevels](7SeverityLevels.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ModerateSeverity](https://w3id.org/lmodel/dpv/risk/ModerateSeverity) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Moderate Severity


## Comments

* The suggested quantitative value for this concept is 0.5 on a scale of 0
to 1



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ModerateSeverity |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ModerateSeverity |
| native | risk:ModerateSeverity |
| exact | dpv_risk:ModerateSeverity, dpv_risk_owl:ModerateSeverity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ModerateSeverity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ModerateSeverity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Severity is Moderate
comments:
- 'The suggested quantitative value for this concept is 0.5 on a scale of 0

  to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Moderate Severity
exact_mappings:
- dpv_risk:ModerateSeverity
- dpv_risk_owl:ModerateSeverity
is_a: 3SeverityLevels
mixins:
- 5SeverityLevels
- 7SeverityLevels
class_uri: risk:ModerateSeverity

```
</details>

### Induced

<details>
```yaml
name: ModerateSeverity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ModerateSeverity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Severity is Moderate
comments:
- 'The suggested quantitative value for this concept is 0.5 on a scale of 0

  to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Moderate Severity
exact_mappings:
- dpv_risk:ModerateSeverity
- dpv_risk_owl:ModerateSeverity
is_a: 3SeverityLevels
mixins:
- 5SeverityLevels
- 7SeverityLevels
class_uri: risk:ModerateSeverity

```
</details></div>