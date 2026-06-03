---
search:
  boost: 10.0
---

# Class: ExtremelyLowSeverity 


_Level where Severity is Extremely Low_



<div data-search-exclude markdown="1">



URI: [risk:ExtremelyLowSeverity](https://w3id.org/lmodel/dpv/risk/ExtremelyLowSeverity)





```mermaid
 classDiagram
    class ExtremelyLowSeverity
    click ExtremelyLowSeverity href "../ExtremelyLowSeverity/"
      7SeverityLevels <|-- ExtremelyLowSeverity
        click 7SeverityLevels href "../7SeverityLevels/"
      
      
```





## Inheritance
* [7SeverityLevels](7SeverityLevels.md)
    * **ExtremelyLowSeverity**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ExtremelyLowSeverity](https://w3id.org/lmodel/dpv/risk/ExtremelyLowSeverity) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Extremely Low Severity


## Comments

* The suggested quantitative value for this concept is 0.01 on a scale of
0 to 1



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ExtremelyLowSeverity |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ExtremelyLowSeverity |
| native | risk:ExtremelyLowSeverity |
| exact | dpv_risk:ExtremelyLowSeverity, dpv_risk_owl:ExtremelyLowSeverity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExtremelyLowSeverity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ExtremelyLowSeverity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Severity is Extremely Low
comments:
- 'The suggested quantitative value for this concept is 0.01 on a scale of

  0 to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Extremely Low Severity
exact_mappings:
- dpv_risk:ExtremelyLowSeverity
- dpv_risk_owl:ExtremelyLowSeverity
is_a: 7SeverityLevels
class_uri: risk:ExtremelyLowSeverity

```
</details>

### Induced

<details>
```yaml
name: ExtremelyLowSeverity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ExtremelyLowSeverity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Severity is Extremely Low
comments:
- 'The suggested quantitative value for this concept is 0.01 on a scale of

  0 to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Extremely Low Severity
exact_mappings:
- dpv_risk:ExtremelyLowSeverity
- dpv_risk_owl:ExtremelyLowSeverity
is_a: 7SeverityLevels
class_uri: risk:ExtremelyLowSeverity

```
</details></div>