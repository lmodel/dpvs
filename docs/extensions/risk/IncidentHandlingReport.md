---
search:
  boost: 10.0
---

# Class: IncidentHandlingReport 


_A report describing the response to or handling of an incident regarding_

_the mitigation of its effects and the prevention of its recurrence_



<div data-search-exclude markdown="1">



URI: [risk:IncidentHandlingReport](https://w3id.org/lmodel/dpv/risk/IncidentHandlingReport)





```mermaid
 classDiagram
    class IncidentHandlingReport
    click IncidentHandlingReport href "../IncidentHandlingReport/"
      IncidentReport <|-- IncidentHandlingReport
        click IncidentReport href "../IncidentReport/"
      
      
```





## Inheritance
* [IncidentReport](IncidentReport.md)
    * **IncidentHandlingReport**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IncidentHandlingReport](https://w3id.org/lmodel/dpv/risk/IncidentHandlingReport) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident Handling Report




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IncidentHandlingReport |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IncidentHandlingReport |
| native | risk:IncidentHandlingReport |
| exact | dpv_risk:IncidentHandlingReport, dpv_risk_owl:IncidentHandlingReport |
| related | iso42001:AIRiskTreatmentPlan |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentHandlingReport
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentHandlingReport
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'A report describing the response to or handling of an incident regarding

  the mitigation of its effects and the prevention of its recurrence'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Handling Report
exact_mappings:
- dpv_risk:IncidentHandlingReport
- dpv_risk_owl:IncidentHandlingReport
related_mappings:
- iso42001:AIRiskTreatmentPlan
is_a: IncidentReport
class_uri: risk:IncidentHandlingReport

```
</details>

### Induced

<details>
```yaml
name: IncidentHandlingReport
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentHandlingReport
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'A report describing the response to or handling of an incident regarding

  the mitigation of its effects and the prevention of its recurrence'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Handling Report
exact_mappings:
- dpv_risk:IncidentHandlingReport
- dpv_risk_owl:IncidentHandlingReport
related_mappings:
- iso42001:AIRiskTreatmentPlan
is_a: IncidentReport
class_uri: risk:IncidentHandlingReport

```
</details></div>