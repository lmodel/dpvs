---
search:
  boost: 10.0
---

# Class: IncidentPreliminaryReport 


_A report describing the preliminary investigation regarding an incident_

_where the complete facts or extent of the incident may not be known_



<div data-search-exclude markdown="1">



URI: [risk:IncidentPreliminaryReport](https://w3id.org/lmodel/dpv/risk/IncidentPreliminaryReport)





```mermaid
 classDiagram
    class IncidentPreliminaryReport
    click IncidentPreliminaryReport href "../IncidentPreliminaryReport/"
      IncidentReport <|-- IncidentPreliminaryReport
        click IncidentReport href "../IncidentReport/"
      
      
```





## Inheritance
* [IncidentReport](IncidentReport.md)
    * **IncidentPreliminaryReport**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IncidentPreliminaryReport](https://w3id.org/lmodel/dpv/risk/IncidentPreliminaryReport) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident Preliminary Report




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IncidentPreliminaryReport |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IncidentPreliminaryReport |
| native | risk:IncidentPreliminaryReport |
| exact | dpv_risk:IncidentPreliminaryReport, dpv_risk_owl:IncidentPreliminaryReport |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentPreliminaryReport
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentPreliminaryReport
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'A report describing the preliminary investigation regarding an incident

  where the complete facts or extent of the incident may not be known'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Preliminary Report
exact_mappings:
- dpv_risk:IncidentPreliminaryReport
- dpv_risk_owl:IncidentPreliminaryReport
is_a: IncidentReport
class_uri: risk:IncidentPreliminaryReport

```
</details>

### Induced

<details>
```yaml
name: IncidentPreliminaryReport
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentPreliminaryReport
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'A report describing the preliminary investigation regarding an incident

  where the complete facts or extent of the incident may not be known'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Preliminary Report
exact_mappings:
- dpv_risk:IncidentPreliminaryReport
- dpv_risk_owl:IncidentPreliminaryReport
is_a: IncidentReport
class_uri: risk:IncidentPreliminaryReport

```
</details></div>