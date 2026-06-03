---
search:
  boost: 10.0
---

# Class: IncidentHalted 


_The incident has halted or paused with a high likelihood of resuming or_

_recurring_



<div data-search-exclude markdown="1">



URI: [risk:IncidentHalted](https://w3id.org/lmodel/dpv/risk/IncidentHalted)





```mermaid
 classDiagram
    class IncidentHalted
    click IncidentHalted href "../IncidentHalted/"
      IncidentStatus <|-- IncidentHalted
        click IncidentStatus href "../IncidentStatus/"
      
      
```





## Inheritance
* [IncidentStatus](IncidentStatus.md)
    * **IncidentHalted**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IncidentHalted](https://w3id.org/lmodel/dpv/risk/IncidentHalted) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident Halted




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IncidentHalted |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IncidentHalted |
| native | risk:IncidentHalted |
| exact | dpv_risk:IncidentHalted, dpv_risk_owl:IncidentHalted |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentHalted
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentHalted
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'The incident has halted or paused with a high likelihood of resuming
  or

  recurring'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Halted
exact_mappings:
- dpv_risk:IncidentHalted
- dpv_risk_owl:IncidentHalted
is_a: IncidentStatus
class_uri: risk:IncidentHalted

```
</details>

### Induced

<details>
```yaml
name: IncidentHalted
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentHalted
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'The incident has halted or paused with a high likelihood of resuming
  or

  recurring'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Halted
exact_mappings:
- dpv_risk:IncidentHalted
- dpv_risk_owl:IncidentHalted
is_a: IncidentStatus
class_uri: risk:IncidentHalted

```
</details></div>