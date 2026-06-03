---
search:
  boost: 10.0
---

# Class: Incident 


_An actual or occurred event_



<div data-search-exclude markdown="1">



URI: [risk:Incident](https://w3id.org/lmodel/dpv/risk/Incident)





```mermaid
 classDiagram
    class Incident
    click Incident href "../Incident/"
      Incident <|-- AccidentalIncident
        click AccidentalIncident href "../AccidentalIncident/"
      Incident <|-- AvailabilityIncident
        click AvailabilityIncident href "../AvailabilityIncident/"
      Incident <|-- ConfidentialityIncident
        click ConfidentialityIncident href "../ConfidentialityIncident/"
      Incident <|-- CrossBorderIncident
        click CrossBorderIncident href "../CrossBorderIncident/"
      Incident <|-- DeliberateIncident
        click DeliberateIncident href "../DeliberateIncident/"
      Incident <|-- EnvironmentalIncident
        click EnvironmentalIncident href "../EnvironmentalIncident/"
      Incident <|-- IntegrityIncident
        click IntegrityIncident href "../IntegrityIncident/"
      
      
```





## Inheritance
* **Incident**
    * [AccidentalIncident](AccidentalIncident.md)
    * [AvailabilityIncident](AvailabilityIncident.md)
    * [ConfidentialityIncident](ConfidentialityIncident.md)
    * [CrossBorderIncident](CrossBorderIncident.md)
    * [DeliberateIncident](DeliberateIncident.md)
    * [EnvironmentalIncident](EnvironmentalIncident.md)
    * [IntegrityIncident](IntegrityIncident.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Incident](https://w3id.org/lmodel/dpv/risk/Incident) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident


## Comments

* Incident is realised or materialised risk



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Incident |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Incident |
| native | risk:Incident |
| exact | dpv_risk:Incident, dpv_risk_owl:Incident, iso42001:AIIncident |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Incident
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Incident
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: An actual or occurred event
comments:
- Incident is realised or materialised risk
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident
exact_mappings:
- dpv_risk:Incident
- dpv_risk_owl:Incident
- iso42001:AIIncident
class_uri: risk:Incident

```
</details>

### Induced

<details>
```yaml
name: Incident
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Incident
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: An actual or occurred event
comments:
- Incident is realised or materialised risk
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident
exact_mappings:
- dpv_risk:Incident
- dpv_risk_owl:Incident
- iso42001:AIIncident
class_uri: risk:Incident

```
</details></div>