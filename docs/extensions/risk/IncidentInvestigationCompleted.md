---
search:
  boost: 10.0
---

# Class: IncidentInvestigationCompleted 


_Status indicating the investigation has been completed and findings are_

_available_



<div data-search-exclude markdown="1">



URI: [risk:IncidentInvestigationCompleted](https://w3id.org/lmodel/dpv/risk/IncidentInvestigationCompleted)





```mermaid
 classDiagram
    class IncidentInvestigationCompleted
    click IncidentInvestigationCompleted href "../IncidentInvestigationCompleted/"
      IncidentInvestigationStatus <|-- IncidentInvestigationCompleted
        click IncidentInvestigationStatus href "../IncidentInvestigationStatus/"
      
      
```





## Inheritance
* [IncidentInvestigationStatus](IncidentInvestigationStatus.md)
    * **IncidentInvestigationCompleted**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IncidentInvestigationCompleted](https://w3id.org/lmodel/dpv/risk/IncidentInvestigationCompleted) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident Investigation Completed




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IncidentInvestigationCompleted |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IncidentInvestigationCompleted |
| native | risk:IncidentInvestigationCompleted |
| exact | dpv_risk:IncidentInvestigationCompleted, dpv_risk_owl:IncidentInvestigationCompleted |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentInvestigationCompleted
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentInvestigationCompleted
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Status indicating the investigation has been completed and findings
  are

  available'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Investigation Completed
exact_mappings:
- dpv_risk:IncidentInvestigationCompleted
- dpv_risk_owl:IncidentInvestigationCompleted
is_a: IncidentInvestigationStatus
class_uri: risk:IncidentInvestigationCompleted

```
</details>

### Induced

<details>
```yaml
name: IncidentInvestigationCompleted
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentInvestigationCompleted
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Status indicating the investigation has been completed and findings
  are

  available'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Investigation Completed
exact_mappings:
- dpv_risk:IncidentInvestigationCompleted
- dpv_risk_owl:IncidentInvestigationCompleted
is_a: IncidentInvestigationStatus
class_uri: risk:IncidentInvestigationCompleted

```
</details></div>