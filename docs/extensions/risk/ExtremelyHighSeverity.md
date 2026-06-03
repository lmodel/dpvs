---
search:
  boost: 10.0
---

# Class: ExtremelyHighSeverity 


_Level where Severity is Extremely High_



<div data-search-exclude markdown="1">



URI: [risk:ExtremelyHighSeverity](https://w3id.org/lmodel/dpv/risk/ExtremelyHighSeverity)





```mermaid
 classDiagram
    class ExtremelyHighSeverity
    click ExtremelyHighSeverity href "../ExtremelyHighSeverity/"
      7SeverityLevels <|-- ExtremelyHighSeverity
        click 7SeverityLevels href "../7SeverityLevels/"
      
      
```





## Inheritance
* [7SeverityLevels](7SeverityLevels.md)
    * **ExtremelyHighSeverity**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ExtremelyHighSeverity](https://w3id.org/lmodel/dpv/risk/ExtremelyHighSeverity) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Extremely High Severity


## Comments

* The suggested quantitative value for this concept is 0.99 on a scale of
0 to 1



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ExtremelyHighSeverity |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ExtremelyHighSeverity |
| native | risk:ExtremelyHighSeverity |
| exact | dpv_risk:ExtremelyHighSeverity, dpv_risk_owl:ExtremelyHighSeverity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExtremelyHighSeverity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ExtremelyHighSeverity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Severity is Extremely High
comments:
- 'The suggested quantitative value for this concept is 0.99 on a scale of

  0 to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Extremely High Severity
exact_mappings:
- dpv_risk:ExtremelyHighSeverity
- dpv_risk_owl:ExtremelyHighSeverity
is_a: 7SeverityLevels
class_uri: risk:ExtremelyHighSeverity

```
</details>

### Induced

<details>
```yaml
name: ExtremelyHighSeverity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ExtremelyHighSeverity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Severity is Extremely High
comments:
- 'The suggested quantitative value for this concept is 0.99 on a scale of

  0 to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Extremely High Severity
exact_mappings:
- dpv_risk:ExtremelyHighSeverity
- dpv_risk_owl:ExtremelyHighSeverity
is_a: 7SeverityLevels
class_uri: risk:ExtremelyHighSeverity

```
</details></div>