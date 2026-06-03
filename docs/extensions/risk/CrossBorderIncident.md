---
search:
  boost: 10.0
---

# Class: CrossBorderIncident 


_Incident involving cross-border or multiple jurisdictions_



<div data-search-exclude markdown="1">



URI: [risk:CrossBorderIncident](https://w3id.org/lmodel/dpv/risk/CrossBorderIncident)





```mermaid
 classDiagram
    class CrossBorderIncident
    click CrossBorderIncident href "../CrossBorderIncident/"
      Incident <|-- CrossBorderIncident
        click Incident href "../Incident/"
      
      
```





## Inheritance
* [Incident](Incident.md)
    * **CrossBorderIncident**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:CrossBorderIncident](https://w3id.org/lmodel/dpv/risk/CrossBorderIncident) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Cross-Border Incident




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#CrossBorderIncident |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:CrossBorderIncident |
| native | risk:CrossBorderIncident |
| exact | dpv_risk:CrossBorderIncident, dpv_risk_owl:CrossBorderIncident |
| related | iso42001:AIIncident |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CrossBorderIncident
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#CrossBorderIncident
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Incident involving cross-border or multiple jurisdictions
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Cross-Border Incident
exact_mappings:
- dpv_risk:CrossBorderIncident
- dpv_risk_owl:CrossBorderIncident
related_mappings:
- iso42001:AIIncident
is_a: Incident
class_uri: risk:CrossBorderIncident

```
</details>

### Induced

<details>
```yaml
name: CrossBorderIncident
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#CrossBorderIncident
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Incident involving cross-border or multiple jurisdictions
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Cross-Border Incident
exact_mappings:
- dpv_risk:CrossBorderIncident
- dpv_risk_owl:CrossBorderIncident
related_mappings:
- iso42001:AIIncident
is_a: Incident
class_uri: risk:CrossBorderIncident

```
</details></div>