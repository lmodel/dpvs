---
search:
  boost: 10.0
---

# Class: EnvironmentalIncident 


_Incident caused due to environmental factors outside human controls_



<div data-search-exclude markdown="1">



URI: [risk:EnvironmentalIncident](https://w3id.org/lmodel/dpv/risk/EnvironmentalIncident)





```mermaid
 classDiagram
    class EnvironmentalIncident
    click EnvironmentalIncident href "../EnvironmentalIncident/"
      Incident <|-- EnvironmentalIncident
        click Incident href "../Incident/"
      
      
```





## Inheritance
* [Incident](Incident.md)
    * **EnvironmentalIncident**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:EnvironmentalIncident](https://w3id.org/lmodel/dpv/risk/EnvironmentalIncident) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Environmental Incident




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#EnvironmentalIncident |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:EnvironmentalIncident |
| native | risk:EnvironmentalIncident |
| exact | dpv_risk:EnvironmentalIncident, dpv_risk_owl:EnvironmentalIncident |
| close | iso42001:AIIncident |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EnvironmentalIncident
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#EnvironmentalIncident
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Incident caused due to environmental factors outside human controls
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Environmental Incident
exact_mappings:
- dpv_risk:EnvironmentalIncident
- dpv_risk_owl:EnvironmentalIncident
close_mappings:
- iso42001:AIIncident
is_a: Incident
class_uri: risk:EnvironmentalIncident

```
</details>

### Induced

<details>
```yaml
name: EnvironmentalIncident
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#EnvironmentalIncident
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Incident caused due to environmental factors outside human controls
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Environmental Incident
exact_mappings:
- dpv_risk:EnvironmentalIncident
- dpv_risk_owl:EnvironmentalIncident
close_mappings:
- iso42001:AIIncident
is_a: Incident
class_uri: risk:EnvironmentalIncident

```
</details></div>