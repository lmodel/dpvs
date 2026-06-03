---
search:
  boost: 10.0
---

# Class: ExtremelyHighRisk 


_Level where Risk is Extremely High_



<div data-search-exclude markdown="1">



URI: [risk:ExtremelyHighRisk](https://w3id.org/lmodel/dpv/risk/ExtremelyHighRisk)





```mermaid
 classDiagram
    class ExtremelyHighRisk
    click ExtremelyHighRisk href "../ExtremelyHighRisk/"
      7RiskLevels <|-- ExtremelyHighRisk
        click 7RiskLevels href "../7RiskLevels/"
      
      
```





## Inheritance
* [7RiskLevels](7RiskLevels.md)
    * **ExtremelyHighRisk**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ExtremelyHighRisk](https://w3id.org/lmodel/dpv/risk/ExtremelyHighRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Extremely High Risk


## Comments

* The suggested quantitative value for this concept is 0.99 on a scale of
0 to 1



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ExtremelyHighRisk |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ExtremelyHighRisk |
| native | risk:ExtremelyHighRisk |
| exact | dpv_risk:ExtremelyHighRisk, dpv_risk_owl:ExtremelyHighRisk |
| close | iso42001:AIRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExtremelyHighRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ExtremelyHighRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Risk is Extremely High
comments:
- 'The suggested quantitative value for this concept is 0.99 on a scale of

  0 to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Extremely High Risk
exact_mappings:
- dpv_risk:ExtremelyHighRisk
- dpv_risk_owl:ExtremelyHighRisk
close_mappings:
- iso42001:AIRisk
is_a: 7RiskLevels
class_uri: risk:ExtremelyHighRisk

```
</details>

### Induced

<details>
```yaml
name: ExtremelyHighRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ExtremelyHighRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Risk is Extremely High
comments:
- 'The suggested quantitative value for this concept is 0.99 on a scale of

  0 to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Extremely High Risk
exact_mappings:
- dpv_risk:ExtremelyHighRisk
- dpv_risk_owl:ExtremelyHighRisk
close_mappings:
- iso42001:AIRisk
is_a: 7RiskLevels
class_uri: risk:ExtremelyHighRisk

```
</details></div>