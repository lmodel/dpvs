---
search:
  boost: 10.0
---

# Class: IncidentConcluded 


_The incident has stopped or finished or concluded without any active_

_mitigation and with a low likelihood of resuming or recurring_



<div data-search-exclude markdown="1">



URI: [risk:IncidentConcluded](https://w3id.org/lmodel/dpv/risk/IncidentConcluded)





```mermaid
 classDiagram
    class IncidentConcluded
    click IncidentConcluded href "../IncidentConcluded/"
      IncidentStatus <|-- IncidentConcluded
        click IncidentStatus href "../IncidentStatus/"
      
      
```





## Inheritance
* [IncidentStatus](IncidentStatus.md)
    * **IncidentConcluded**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IncidentConcluded](https://w3id.org/lmodel/dpv/risk/IncidentConcluded) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident Concluded




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IncidentConcluded |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IncidentConcluded |
| native | risk:IncidentConcluded |
| exact | dpv_risk:IncidentConcluded, dpv_risk_owl:IncidentConcluded |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentConcluded
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentConcluded
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'The incident has stopped or finished or concluded without any active

  mitigation and with a low likelihood of resuming or recurring'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Concluded
exact_mappings:
- dpv_risk:IncidentConcluded
- dpv_risk_owl:IncidentConcluded
is_a: IncidentStatus
class_uri: risk:IncidentConcluded

```
</details>

### Induced

<details>
```yaml
name: IncidentConcluded
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentConcluded
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'The incident has stopped or finished or concluded without any active

  mitigation and with a low likelihood of resuming or recurring'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Concluded
exact_mappings:
- dpv_risk:IncidentConcluded
- dpv_risk_owl:IncidentConcluded
is_a: IncidentStatus
class_uri: risk:IncidentConcluded

```
</details></div>