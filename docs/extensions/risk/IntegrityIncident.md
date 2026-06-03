---
search:
  boost: 10.0
---

# Class: IntegrityIncident 


_Incident where the integrity of information or system has been affected_



<div data-search-exclude markdown="1">



URI: [risk:IntegrityIncident](https://w3id.org/lmodel/dpv/risk/IntegrityIncident)





```mermaid
 classDiagram
    class IntegrityIncident
    click IntegrityIncident href "../IntegrityIncident/"
      Incident <|-- IntegrityIncident
        click Incident href "../Incident/"
      
      
```





## Inheritance
* [Incident](Incident.md)
    * **IntegrityIncident**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IntegrityIncident](https://w3id.org/lmodel/dpv/risk/IntegrityIncident) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Integrity Incident




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IntegrityIncident |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IntegrityIncident |
| native | risk:IntegrityIncident |
| exact | dpv_risk:IntegrityIncident, dpv_risk_owl:IntegrityIncident |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IntegrityIncident
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IntegrityIncident
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Incident where the integrity of information or system has been affected
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Integrity Incident
exact_mappings:
- dpv_risk:IntegrityIncident
- dpv_risk_owl:IntegrityIncident
is_a: Incident
class_uri: risk:IntegrityIncident

```
</details>

### Induced

<details>
```yaml
name: IntegrityIncident
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IntegrityIncident
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Incident where the integrity of information or system has been affected
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Integrity Incident
exact_mappings:
- dpv_risk:IntegrityIncident
- dpv_risk_owl:IntegrityIncident
is_a: Incident
class_uri: risk:IntegrityIncident

```
</details></div>