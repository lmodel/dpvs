---
search:
  boost: 10.0
---

# Class: IncidentSuspected 


_The state where a incident is suspected, but has not yet been confirmed._

_This can be due to lack of information, or because the process of_

_detection and investigation is still ongoing_



<div data-search-exclude markdown="1">



URI: [risk:IncidentSuspected](https://w3id.org/lmodel/dpv/risk/IncidentSuspected)





```mermaid
 classDiagram
    class IncidentSuspected
    click IncidentSuspected href "../IncidentSuspected/"
      IncidentStatus <|-- IncidentSuspected
        click IncidentStatus href "../IncidentStatus/"
      
      
```





## Inheritance
* [IncidentStatus](IncidentStatus.md)
    * **IncidentSuspected**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IncidentSuspected](https://w3id.org/lmodel/dpv/risk/IncidentSuspected) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident Suspected




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IncidentSuspected |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IncidentSuspected |
| native | risk:IncidentSuspected |
| exact | dpv_risk:IncidentSuspected, dpv_risk_owl:IncidentSuspected |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentSuspected
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentSuspected
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'The state where a incident is suspected, but has not yet been confirmed.

  This can be due to lack of information, or because the process of

  detection and investigation is still ongoing'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Suspected
exact_mappings:
- dpv_risk:IncidentSuspected
- dpv_risk_owl:IncidentSuspected
is_a: IncidentStatus
class_uri: risk:IncidentSuspected

```
</details>

### Induced

<details>
```yaml
name: IncidentSuspected
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentSuspected
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'The state where a incident is suspected, but has not yet been confirmed.

  This can be due to lack of information, or because the process of

  detection and investigation is still ongoing'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Suspected
exact_mappings:
- dpv_risk:IncidentSuspected
- dpv_risk_owl:IncidentSuspected
is_a: IncidentStatus
class_uri: risk:IncidentSuspected

```
</details></div>