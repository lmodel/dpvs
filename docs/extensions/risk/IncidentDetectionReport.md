---
search:
  boost: 10.0
---

# Class: IncidentDetectionReport 


_A report describing the detection of an incident_



<div data-search-exclude markdown="1">



URI: [risk:IncidentDetectionReport](https://w3id.org/lmodel/dpv/risk/IncidentDetectionReport)





```mermaid
 classDiagram
    class IncidentDetectionReport
    click IncidentDetectionReport href "../IncidentDetectionReport/"
      IncidentReport <|-- IncidentDetectionReport
        click IncidentReport href "../IncidentReport/"
      
      
```





## Inheritance
* [IncidentReport](IncidentReport.md)
    * **IncidentDetectionReport**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IncidentDetectionReport](https://w3id.org/lmodel/dpv/risk/IncidentDetectionReport) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident Detection Report




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IncidentDetectionReport |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IncidentDetectionReport |
| native | risk:IncidentDetectionReport |
| exact | dpv_risk:IncidentDetectionReport, dpv_risk_owl:IncidentDetectionReport |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentDetectionReport
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentDetectionReport
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: A report describing the detection of an incident
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Detection Report
exact_mappings:
- dpv_risk:IncidentDetectionReport
- dpv_risk_owl:IncidentDetectionReport
is_a: IncidentReport
class_uri: risk:IncidentDetectionReport

```
</details>

### Induced

<details>
```yaml
name: IncidentDetectionReport
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentDetectionReport
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: A report describing the detection of an incident
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Detection Report
exact_mappings:
- dpv_risk:IncidentDetectionReport
- dpv_risk_owl:IncidentDetectionReport
is_a: IncidentReport
class_uri: risk:IncidentDetectionReport

```
</details></div>