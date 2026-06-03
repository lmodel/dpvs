---
search:
  boost: 10.0
---

# Class: IncidentTerminated 


_The incident has been stopped or terminated through the use of a_

_mitigation or deterrent measure with a low likelihood of resuming or_

_recurring_



<div data-search-exclude markdown="1">



URI: [risk:IncidentTerminated](https://w3id.org/lmodel/dpv/risk/IncidentTerminated)





```mermaid
 classDiagram
    class IncidentTerminated
    click IncidentTerminated href "../IncidentTerminated/"
      IncidentStatus <|-- IncidentTerminated
        click IncidentStatus href "../IncidentStatus/"
      
      
```





## Inheritance
* [IncidentStatus](IncidentStatus.md)
    * **IncidentTerminated**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IncidentTerminated](https://w3id.org/lmodel/dpv/risk/IncidentTerminated) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident Terminated




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IncidentTerminated |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IncidentTerminated |
| native | risk:IncidentTerminated |
| exact | dpv_risk:IncidentTerminated, dpv_risk_owl:IncidentTerminated |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentTerminated
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentTerminated
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'The incident has been stopped or terminated through the use of a

  mitigation or deterrent measure with a low likelihood of resuming or

  recurring'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Terminated
exact_mappings:
- dpv_risk:IncidentTerminated
- dpv_risk_owl:IncidentTerminated
is_a: IncidentStatus
class_uri: risk:IncidentTerminated

```
</details>

### Induced

<details>
```yaml
name: IncidentTerminated
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentTerminated
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'The incident has been stopped or terminated through the use of a

  mitigation or deterrent measure with a low likelihood of resuming or

  recurring'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Terminated
exact_mappings:
- dpv_risk:IncidentTerminated
- dpv_risk_owl:IncidentTerminated
is_a: IncidentStatus
class_uri: risk:IncidentTerminated

```
</details></div>