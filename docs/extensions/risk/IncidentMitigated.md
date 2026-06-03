---
search:
  boost: 10.0
---

# Class: IncidentMitigated 


_The incident has been mitigated against future recurrences i.e. a_

_measure has been applied to prevent the same or similar incident from_

_recurring_



<div data-search-exclude markdown="1">



URI: [risk:IncidentMitigated](https://w3id.org/lmodel/dpv/risk/IncidentMitigated)





```mermaid
 classDiagram
    class IncidentMitigated
    click IncidentMitigated href "../IncidentMitigated/"
      IncidentStatus <|-- IncidentMitigated
        click IncidentStatus href "../IncidentStatus/"
      
      
```





## Inheritance
* [IncidentStatus](IncidentStatus.md)
    * **IncidentMitigated**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IncidentMitigated](https://w3id.org/lmodel/dpv/risk/IncidentMitigated) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident Mitigated




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IncidentMitigated |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IncidentMitigated |
| native | risk:IncidentMitigated |
| exact | dpv_risk:IncidentMitigated, dpv_risk_owl:IncidentMitigated |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentMitigated
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentMitigated
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'The incident has been mitigated against future recurrences i.e. a

  measure has been applied to prevent the same or similar incident from

  recurring'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Mitigated
exact_mappings:
- dpv_risk:IncidentMitigated
- dpv_risk_owl:IncidentMitigated
is_a: IncidentStatus
class_uri: risk:IncidentMitigated

```
</details>

### Induced

<details>
```yaml
name: IncidentMitigated
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentMitigated
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'The incident has been mitigated against future recurrences i.e. a

  measure has been applied to prevent the same or similar incident from

  recurring'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Mitigated
exact_mappings:
- dpv_risk:IncidentMitigated
- dpv_risk_owl:IncidentMitigated
is_a: IncidentStatus
class_uri: risk:IncidentMitigated

```
</details></div>