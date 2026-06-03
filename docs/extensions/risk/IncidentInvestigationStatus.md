---
search:
  boost: 10.0
---

# Class: IncidentInvestigationStatus 


_Status associated with investigation of an incident_



<div data-search-exclude markdown="1">



URI: [risk:IncidentInvestigationStatus](https://w3id.org/lmodel/dpv/risk/IncidentInvestigationStatus)





```mermaid
 classDiagram
    class IncidentInvestigationStatus
    click IncidentInvestigationStatus href "../IncidentInvestigationStatus/"
      IncidentInvestigationStatus <|-- IncidentInvestigationCompleted
        click IncidentInvestigationCompleted href "../IncidentInvestigationCompleted/"
      IncidentInvestigationStatus <|-- IncidentInvestigationNotStarted
        click IncidentInvestigationNotStarted href "../IncidentInvestigationNotStarted/"
      IncidentInvestigationStatus <|-- IncidentInvestigationOngoing
        click IncidentInvestigationOngoing href "../IncidentInvestigationOngoing/"
      IncidentInvestigationStatus <|-- IncidentInvestigationPreliminary
        click IncidentInvestigationPreliminary href "../IncidentInvestigationPreliminary/"
      
      
```





## Inheritance
* **IncidentInvestigationStatus**
    * [IncidentInvestigationCompleted](IncidentInvestigationCompleted.md)
    * [IncidentInvestigationNotStarted](IncidentInvestigationNotStarted.md)
    * [IncidentInvestigationOngoing](IncidentInvestigationOngoing.md)
    * [IncidentInvestigationPreliminary](IncidentInvestigationPreliminary.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IncidentInvestigationStatus](https://w3id.org/lmodel/dpv/risk/IncidentInvestigationStatus) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident Investigation Status




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IncidentInvestigationStatus |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IncidentInvestigationStatus |
| native | risk:IncidentInvestigationStatus |
| exact | dpv_risk:IncidentInvestigationStatus, dpv_risk_owl:IncidentInvestigationStatus |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentInvestigationStatus
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentInvestigationStatus
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Status associated with investigation of an incident
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Investigation Status
exact_mappings:
- dpv_risk:IncidentInvestigationStatus
- dpv_risk_owl:IncidentInvestigationStatus
class_uri: risk:IncidentInvestigationStatus

```
</details>

### Induced

<details>
```yaml
name: IncidentInvestigationStatus
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentInvestigationStatus
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Status associated with investigation of an incident
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Investigation Status
exact_mappings:
- dpv_risk:IncidentInvestigationStatus
- dpv_risk_owl:IncidentInvestigationStatus
class_uri: risk:IncidentInvestigationStatus

```
</details></div>