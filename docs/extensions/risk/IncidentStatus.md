---
search:
  boost: 10.0
---

# Class: IncidentStatus 


_Status associated with an incident_



<div data-search-exclude markdown="1">



URI: [risk:IncidentStatus](https://w3id.org/lmodel/dpv/risk/IncidentStatus)





```mermaid
 classDiagram
    class IncidentStatus
    click IncidentStatus href "../IncidentStatus/"
      IncidentStatus <|-- IncidentConcluded
        click IncidentConcluded href "../IncidentConcluded/"
      IncidentStatus <|-- IncidentHalted
        click IncidentHalted href "../IncidentHalted/"
      IncidentStatus <|-- IncidentMitigated
        click IncidentMitigated href "../IncidentMitigated/"
      IncidentStatus <|-- IncidentNearMiss
        click IncidentNearMiss href "../IncidentNearMiss/"
      IncidentStatus <|-- IncidentOngoing
        click IncidentOngoing href "../IncidentOngoing/"
      IncidentStatus <|-- IncidentStatusUnknown
        click IncidentStatusUnknown href "../IncidentStatusUnknown/"
      IncidentStatus <|-- IncidentSuspected
        click IncidentSuspected href "../IncidentSuspected/"
      IncidentStatus <|-- IncidentTerminated
        click IncidentTerminated href "../IncidentTerminated/"
      
      
```





## Inheritance
* **IncidentStatus**
    * [IncidentConcluded](IncidentConcluded.md)
    * [IncidentHalted](IncidentHalted.md)
    * [IncidentMitigated](IncidentMitigated.md)
    * [IncidentNearMiss](IncidentNearMiss.md)
    * [IncidentOngoing](IncidentOngoing.md)
    * [IncidentStatusUnknown](IncidentStatusUnknown.md)
    * [IncidentSuspected](IncidentSuspected.md)
    * [IncidentTerminated](IncidentTerminated.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IncidentStatus](https://w3id.org/lmodel/dpv/risk/IncidentStatus) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident Status




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IncidentStatus |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IncidentStatus |
| native | risk:IncidentStatus |
| exact | dpv_risk:IncidentStatus, dpv_risk_owl:IncidentStatus |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentStatus
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentStatus
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Status associated with an incident
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Status
exact_mappings:
- dpv_risk:IncidentStatus
- dpv_risk_owl:IncidentStatus
class_uri: risk:IncidentStatus

```
</details>

### Induced

<details>
```yaml
name: IncidentStatus
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentStatus
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Status associated with an incident
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Status
exact_mappings:
- dpv_risk:IncidentStatus
- dpv_risk_owl:IncidentStatus
class_uri: risk:IncidentStatus

```
</details></div>