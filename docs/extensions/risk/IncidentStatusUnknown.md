---
search:
  boost: 10.0
---

# Class: IncidentStatusUnknown 


_The status of a incident is unknown_



<div data-search-exclude markdown="1">



URI: [risk:IncidentStatusUnknown](https://w3id.org/lmodel/dpv/risk/IncidentStatusUnknown)





```mermaid
 classDiagram
    class IncidentStatusUnknown
    click IncidentStatusUnknown href "../IncidentStatusUnknown/"
      IncidentStatus <|-- IncidentStatusUnknown
        click IncidentStatus href "../IncidentStatus/"
      
      
```





## Inheritance
* [IncidentStatus](IncidentStatus.md)
    * **IncidentStatusUnknown**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IncidentStatusUnknown](https://w3id.org/lmodel/dpv/risk/IncidentStatusUnknown) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident Status Unknown




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IncidentStatusUnknown |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IncidentStatusUnknown |
| native | risk:IncidentStatusUnknown |
| exact | dpv_risk:IncidentStatusUnknown, dpv_risk_owl:IncidentStatusUnknown |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentStatusUnknown
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentStatusUnknown
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: The status of a incident is unknown
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Status Unknown
exact_mappings:
- dpv_risk:IncidentStatusUnknown
- dpv_risk_owl:IncidentStatusUnknown
is_a: IncidentStatus
class_uri: risk:IncidentStatusUnknown

```
</details>

### Induced

<details>
```yaml
name: IncidentStatusUnknown
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentStatusUnknown
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: The status of a incident is unknown
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Status Unknown
exact_mappings:
- dpv_risk:IncidentStatusUnknown
- dpv_risk_owl:IncidentStatusUnknown
is_a: IncidentStatus
class_uri: risk:IncidentStatusUnknown

```
</details></div>