---
search:
  boost: 10.0
---

# Class: IncidentOngoing 


_The incident is ongoing i.e. still active_



<div data-search-exclude markdown="1">



URI: [risk:IncidentOngoing](https://w3id.org/lmodel/dpv/risk/IncidentOngoing)





```mermaid
 classDiagram
    class IncidentOngoing
    click IncidentOngoing href "../IncidentOngoing/"
      IncidentStatus <|-- IncidentOngoing
        click IncidentStatus href "../IncidentStatus/"
      
      
```





## Inheritance
* [IncidentStatus](IncidentStatus.md)
    * **IncidentOngoing**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IncidentOngoing](https://w3id.org/lmodel/dpv/risk/IncidentOngoing) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident Ongoing




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IncidentOngoing |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IncidentOngoing |
| native | risk:IncidentOngoing |
| exact | dpv_risk:IncidentOngoing, dpv_risk_owl:IncidentOngoing |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentOngoing
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentOngoing
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: The incident is ongoing i.e. still active
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Ongoing
exact_mappings:
- dpv_risk:IncidentOngoing
- dpv_risk_owl:IncidentOngoing
is_a: IncidentStatus
class_uri: risk:IncidentOngoing

```
</details>

### Induced

<details>
```yaml
name: IncidentOngoing
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentOngoing
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: The incident is ongoing i.e. still active
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Ongoing
exact_mappings:
- dpv_risk:IncidentOngoing
- dpv_risk_owl:IncidentOngoing
is_a: IncidentStatus
class_uri: risk:IncidentOngoing

```
</details></div>