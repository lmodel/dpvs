---
search:
  boost: 10.0
---

# Class: IncidentOngoingReport 


_A report describing on ongoing investigation regarding an incident where_

_facts and extent of the investigation are being investigated_



<div data-search-exclude markdown="1">



URI: [risk:IncidentOngoingReport](https://w3id.org/lmodel/dpv/risk/IncidentOngoingReport)





```mermaid
 classDiagram
    class IncidentOngoingReport
    click IncidentOngoingReport href "../IncidentOngoingReport/"
      IncidentReport <|-- IncidentOngoingReport
        click IncidentReport href "../IncidentReport/"
      
      
```





## Inheritance
* [IncidentReport](IncidentReport.md)
    * **IncidentOngoingReport**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IncidentOngoingReport](https://w3id.org/lmodel/dpv/risk/IncidentOngoingReport) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident Ongoing Report




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IncidentOngoingReport |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IncidentOngoingReport |
| native | risk:IncidentOngoingReport |
| exact | dpv_risk:IncidentOngoingReport, dpv_risk_owl:IncidentOngoingReport |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentOngoingReport
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentOngoingReport
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'A report describing on ongoing investigation regarding an incident where

  facts and extent of the investigation are being investigated'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Ongoing Report
exact_mappings:
- dpv_risk:IncidentOngoingReport
- dpv_risk_owl:IncidentOngoingReport
is_a: IncidentReport
class_uri: risk:IncidentOngoingReport

```
</details>

### Induced

<details>
```yaml
name: IncidentOngoingReport
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentOngoingReport
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'A report describing on ongoing investigation regarding an incident where

  facts and extent of the investigation are being investigated'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Ongoing Report
exact_mappings:
- dpv_risk:IncidentOngoingReport
- dpv_risk_owl:IncidentOngoingReport
is_a: IncidentReport
class_uri: risk:IncidentOngoingReport

```
</details></div>