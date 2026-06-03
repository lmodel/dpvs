---
search:
  boost: 10.0
---

# Class: IncidentInvestigationOngoing 


_Status indicating the investigation is ongoing_



<div data-search-exclude markdown="1">



URI: [risk:IncidentInvestigationOngoing](https://w3id.org/lmodel/dpv/risk/IncidentInvestigationOngoing)





```mermaid
 classDiagram
    class IncidentInvestigationOngoing
    click IncidentInvestigationOngoing href "../IncidentInvestigationOngoing/"
      IncidentInvestigationStatus <|-- IncidentInvestigationOngoing
        click IncidentInvestigationStatus href "../IncidentInvestigationStatus/"
      
      
```





## Inheritance
* [IncidentInvestigationStatus](IncidentInvestigationStatus.md)
    * **IncidentInvestigationOngoing**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IncidentInvestigationOngoing](https://w3id.org/lmodel/dpv/risk/IncidentInvestigationOngoing) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident Investigation Ongoing




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IncidentInvestigationOngoing |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IncidentInvestigationOngoing |
| native | risk:IncidentInvestigationOngoing |
| exact | dpv_risk:IncidentInvestigationOngoing, dpv_risk_owl:IncidentInvestigationOngoing |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentInvestigationOngoing
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentInvestigationOngoing
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Status indicating the investigation is ongoing
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Investigation Ongoing
exact_mappings:
- dpv_risk:IncidentInvestigationOngoing
- dpv_risk_owl:IncidentInvestigationOngoing
is_a: IncidentInvestigationStatus
class_uri: risk:IncidentInvestigationOngoing

```
</details>

### Induced

<details>
```yaml
name: IncidentInvestigationOngoing
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentInvestigationOngoing
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Status indicating the investigation is ongoing
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Investigation Ongoing
exact_mappings:
- dpv_risk:IncidentInvestigationOngoing
- dpv_risk_owl:IncidentInvestigationOngoing
is_a: IncidentInvestigationStatus
class_uri: risk:IncidentInvestigationOngoing

```
</details></div>