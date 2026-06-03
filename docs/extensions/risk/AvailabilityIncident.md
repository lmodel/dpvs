---
search:
  boost: 10.0
---

# Class: AvailabilityIncident 


_Incident where the availability of information or system has been_

_affected_



<div data-search-exclude markdown="1">



URI: [risk:AvailabilityIncident](https://w3id.org/lmodel/dpv/risk/AvailabilityIncident)





```mermaid
 classDiagram
    class AvailabilityIncident
    click AvailabilityIncident href "../AvailabilityIncident/"
      Incident <|-- AvailabilityIncident
        click Incident href "../Incident/"
      
      
```





## Inheritance
* [Incident](Incident.md)
    * **AvailabilityIncident**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:AvailabilityIncident](https://w3id.org/lmodel/dpv/risk/AvailabilityIncident) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Availability Incident




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#AvailabilityIncident |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:AvailabilityIncident |
| native | risk:AvailabilityIncident |
| exact | dpv_risk:AvailabilityIncident, dpv_risk_owl:AvailabilityIncident |
| close | iso42001:AIIncident |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AvailabilityIncident
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AvailabilityIncident
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Incident where the availability of information or system has been

  affected'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Availability Incident
exact_mappings:
- dpv_risk:AvailabilityIncident
- dpv_risk_owl:AvailabilityIncident
close_mappings:
- iso42001:AIIncident
is_a: Incident
class_uri: risk:AvailabilityIncident

```
</details>

### Induced

<details>
```yaml
name: AvailabilityIncident
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AvailabilityIncident
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Incident where the availability of information or system has been

  affected'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Availability Incident
exact_mappings:
- dpv_risk:AvailabilityIncident
- dpv_risk_owl:AvailabilityIncident
close_mappings:
- iso42001:AIIncident
is_a: Incident
class_uri: risk:AvailabilityIncident

```
</details></div>