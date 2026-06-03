---
search:
  boost: 10.0
---

# Class: ExtremelyLowRisk 


_Level where Risk is Extremely Low_



<div data-search-exclude markdown="1">



URI: [risk:ExtremelyLowRisk](https://w3id.org/lmodel/dpv/risk/ExtremelyLowRisk)





```mermaid
 classDiagram
    class ExtremelyLowRisk
    click ExtremelyLowRisk href "../ExtremelyLowRisk/"
      7RiskLevels <|-- ExtremelyLowRisk
        click 7RiskLevels href "../7RiskLevels/"
      
      
```





## Inheritance
* [7RiskLevels](7RiskLevels.md)
    * **ExtremelyLowRisk**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ExtremelyLowRisk](https://w3id.org/lmodel/dpv/risk/ExtremelyLowRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Extremely Low Risk


## Comments

* The suggested quantitative value for this concept is 0.01 on a scale of
0 to 1



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ExtremelyLowRisk |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ExtremelyLowRisk |
| native | risk:ExtremelyLowRisk |
| exact | dpv_risk:ExtremelyLowRisk, dpv_risk_owl:ExtremelyLowRisk |
| close | iso42001:AIRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExtremelyLowRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ExtremelyLowRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Risk is Extremely Low
comments:
- 'The suggested quantitative value for this concept is 0.01 on a scale of

  0 to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Extremely Low Risk
exact_mappings:
- dpv_risk:ExtremelyLowRisk
- dpv_risk_owl:ExtremelyLowRisk
close_mappings:
- iso42001:AIRisk
is_a: 7RiskLevels
class_uri: risk:ExtremelyLowRisk

```
</details>

### Induced

<details>
```yaml
name: ExtremelyLowRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ExtremelyLowRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Level where Risk is Extremely Low
comments:
- 'The suggested quantitative value for this concept is 0.01 on a scale of

  0 to 1'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Extremely Low Risk
exact_mappings:
- dpv_risk:ExtremelyLowRisk
- dpv_risk_owl:ExtremelyLowRisk
close_mappings:
- iso42001:AIRisk
is_a: 7RiskLevels
class_uri: risk:ExtremelyLowRisk

```
</details></div>