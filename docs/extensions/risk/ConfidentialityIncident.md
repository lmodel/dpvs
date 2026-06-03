---
search:
  boost: 10.0
---

# Class: ConfidentialityIncident 


_Incident where the confidentiality of information or system has been_

_affected_



<div data-search-exclude markdown="1">



URI: [risk:ConfidentialityIncident](https://w3id.org/lmodel/dpv/risk/ConfidentialityIncident)





```mermaid
 classDiagram
    class ConfidentialityIncident
    click ConfidentialityIncident href "../ConfidentialityIncident/"
      Incident <|-- ConfidentialityIncident
        click Incident href "../Incident/"
      
      
```





## Inheritance
* [Incident](Incident.md)
    * **ConfidentialityIncident**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ConfidentialityIncident](https://w3id.org/lmodel/dpv/risk/ConfidentialityIncident) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Confidentiality Incident




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ConfidentialityIncident |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ConfidentialityIncident |
| native | risk:ConfidentialityIncident |
| exact | dpv_risk:ConfidentialityIncident, dpv_risk_owl:ConfidentialityIncident |
| close | iso42001:AIIncident |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ConfidentialityIncident
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ConfidentialityIncident
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Incident where the confidentiality of information or system has been

  affected'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Confidentiality Incident
exact_mappings:
- dpv_risk:ConfidentialityIncident
- dpv_risk_owl:ConfidentialityIncident
close_mappings:
- iso42001:AIIncident
is_a: Incident
class_uri: risk:ConfidentialityIncident

```
</details>

### Induced

<details>
```yaml
name: ConfidentialityIncident
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ConfidentialityIncident
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Incident where the confidentiality of information or system has been

  affected'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Confidentiality Incident
exact_mappings:
- dpv_risk:ConfidentialityIncident
- dpv_risk_owl:ConfidentialityIncident
close_mappings:
- iso42001:AIIncident
is_a: Incident
class_uri: risk:ConfidentialityIncident

```
</details></div>