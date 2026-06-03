---
search:
  boost: 10.0
---

# Class: DeliberateIncident 


_Incident caused due to deliberate actions of a human_



<div data-search-exclude markdown="1">



URI: [risk:DeliberateIncident](https://w3id.org/lmodel/dpv/risk/DeliberateIncident)





```mermaid
 classDiagram
    class DeliberateIncident
    click DeliberateIncident href "../DeliberateIncident/"
      Incident <|-- DeliberateIncident
        click Incident href "../Incident/"
      
      
```





## Inheritance
* [Incident](Incident.md)
    * **DeliberateIncident**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DeliberateIncident](https://w3id.org/lmodel/dpv/risk/DeliberateIncident) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Deliberate Incident




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DeliberateIncident |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DeliberateIncident |
| native | risk:DeliberateIncident |
| exact | dpv_risk:DeliberateIncident, dpv_risk_owl:DeliberateIncident |
| close | iso42001:AIIncident |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DeliberateIncident
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DeliberateIncident
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Incident caused due to deliberate actions of a human
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Deliberate Incident
exact_mappings:
- dpv_risk:DeliberateIncident
- dpv_risk_owl:DeliberateIncident
close_mappings:
- iso42001:AIIncident
is_a: Incident
class_uri: risk:DeliberateIncident

```
</details>

### Induced

<details>
```yaml
name: DeliberateIncident
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DeliberateIncident
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Incident caused due to deliberate actions of a human
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Deliberate Incident
exact_mappings:
- dpv_risk:DeliberateIncident
- dpv_risk_owl:DeliberateIncident
close_mappings:
- iso42001:AIIncident
is_a: Incident
class_uri: risk:DeliberateIncident

```
</details></div>