---
search:
  boost: 10.0
---

# Class: IncidentInvestigationPreliminary 


_Status indicating the investigation is at a preliminary stage with_

_limited findings_



<div data-search-exclude markdown="1">



URI: [risk:IncidentInvestigationPreliminary](https://w3id.org/lmodel/dpv/risk/IncidentInvestigationPreliminary)





```mermaid
 classDiagram
    class IncidentInvestigationPreliminary
    click IncidentInvestigationPreliminary href "../IncidentInvestigationPreliminary/"
      IncidentInvestigationStatus <|-- IncidentInvestigationPreliminary
        click IncidentInvestigationStatus href "../IncidentInvestigationStatus/"
      
      
```





## Inheritance
* [IncidentInvestigationStatus](IncidentInvestigationStatus.md)
    * **IncidentInvestigationPreliminary**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IncidentInvestigationPreliminary](https://w3id.org/lmodel/dpv/risk/IncidentInvestigationPreliminary) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident Investigation Preliminary




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IncidentInvestigationPreliminary |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IncidentInvestigationPreliminary |
| native | risk:IncidentInvestigationPreliminary |
| exact | dpv_risk:IncidentInvestigationPreliminary, dpv_risk_owl:IncidentInvestigationPreliminary |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentInvestigationPreliminary
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentInvestigationPreliminary
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Status indicating the investigation is at a preliminary stage with

  limited findings'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Investigation Preliminary
exact_mappings:
- dpv_risk:IncidentInvestigationPreliminary
- dpv_risk_owl:IncidentInvestigationPreliminary
is_a: IncidentInvestigationStatus
class_uri: risk:IncidentInvestigationPreliminary

```
</details>

### Induced

<details>
```yaml
name: IncidentInvestigationPreliminary
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentInvestigationPreliminary
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Status indicating the investigation is at a preliminary stage with

  limited findings'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Investigation Preliminary
exact_mappings:
- dpv_risk:IncidentInvestigationPreliminary
- dpv_risk_owl:IncidentInvestigationPreliminary
is_a: IncidentInvestigationStatus
class_uri: risk:IncidentInvestigationPreliminary

```
</details></div>