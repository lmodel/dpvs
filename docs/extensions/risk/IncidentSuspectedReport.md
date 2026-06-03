---
search:
  boost: 10.0
---

# Class: IncidentSuspectedReport 


_A report describing the suspicion of an incident in the past or_

_occurring_



<div data-search-exclude markdown="1">



URI: [risk:IncidentSuspectedReport](https://w3id.org/lmodel/dpv/risk/IncidentSuspectedReport)





```mermaid
 classDiagram
    class IncidentSuspectedReport
    click IncidentSuspectedReport href "../IncidentSuspectedReport/"
      IncidentReport <|-- IncidentSuspectedReport
        click IncidentReport href "../IncidentReport/"
      
      
```





## Inheritance
* [IncidentReport](IncidentReport.md)
    * **IncidentSuspectedReport**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IncidentSuspectedReport](https://w3id.org/lmodel/dpv/risk/IncidentSuspectedReport) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident Suspected Report




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IncidentSuspectedReport |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IncidentSuspectedReport |
| native | risk:IncidentSuspectedReport |
| exact | dpv_risk:IncidentSuspectedReport, dpv_risk_owl:IncidentSuspectedReport |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentSuspectedReport
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentSuspectedReport
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'A report describing the suspicion of an incident in the past or

  occurring'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Suspected Report
exact_mappings:
- dpv_risk:IncidentSuspectedReport
- dpv_risk_owl:IncidentSuspectedReport
is_a: IncidentReport
class_uri: risk:IncidentSuspectedReport

```
</details>

### Induced

<details>
```yaml
name: IncidentSuspectedReport
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentSuspectedReport
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'A report describing the suspicion of an incident in the past or

  occurring'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Suspected Report
exact_mappings:
- dpv_risk:IncidentSuspectedReport
- dpv_risk_owl:IncidentSuspectedReport
is_a: IncidentReport
class_uri: risk:IncidentSuspectedReport

```
</details></div>