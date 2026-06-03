---
search:
  boost: 10.0
---

# Class: IncidentInvestigationNotStarted 


_Status indicating the investigation has not yet been started_



<div data-search-exclude markdown="1">



URI: [risk:IncidentInvestigationNotStarted](https://w3id.org/lmodel/dpv/risk/IncidentInvestigationNotStarted)





```mermaid
 classDiagram
    class IncidentInvestigationNotStarted
    click IncidentInvestigationNotStarted href "../IncidentInvestigationNotStarted/"
      IncidentInvestigationStatus <|-- IncidentInvestigationNotStarted
        click IncidentInvestigationStatus href "../IncidentInvestigationStatus/"
      
      
```





## Inheritance
* [IncidentInvestigationStatus](IncidentInvestigationStatus.md)
    * **IncidentInvestigationNotStarted**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IncidentInvestigationNotStarted](https://w3id.org/lmodel/dpv/risk/IncidentInvestigationNotStarted) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident Investigation Not Started




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IncidentInvestigationNotStarted |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IncidentInvestigationNotStarted |
| native | risk:IncidentInvestigationNotStarted |
| exact | dpv_risk:IncidentInvestigationNotStarted, dpv_risk_owl:IncidentInvestigationNotStarted |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentInvestigationNotStarted
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentInvestigationNotStarted
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Status indicating the investigation has not yet been started
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Investigation Not Started
exact_mappings:
- dpv_risk:IncidentInvestigationNotStarted
- dpv_risk_owl:IncidentInvestigationNotStarted
is_a: IncidentInvestigationStatus
class_uri: risk:IncidentInvestigationNotStarted

```
</details>

### Induced

<details>
```yaml
name: IncidentInvestigationNotStarted
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentInvestigationNotStarted
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Status indicating the investigation has not yet been started
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Investigation Not Started
exact_mappings:
- dpv_risk:IncidentInvestigationNotStarted
- dpv_risk_owl:IncidentInvestigationNotStarted
is_a: IncidentInvestigationStatus
class_uri: risk:IncidentInvestigationNotStarted

```
</details></div>