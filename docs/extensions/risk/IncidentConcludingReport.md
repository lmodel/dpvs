---
search:
  boost: 10.0
---

# Class: IncidentConcludingReport 


_A report describing the conclusion of an investigation regarding an_

_incident where all relevant facts are known_



<div data-search-exclude markdown="1">



URI: [risk:IncidentConcludingReport](https://w3id.org/lmodel/dpv/risk/IncidentConcludingReport)





```mermaid
 classDiagram
    class IncidentConcludingReport
    click IncidentConcludingReport href "../IncidentConcludingReport/"
      IncidentReport <|-- IncidentConcludingReport
        click IncidentReport href "../IncidentReport/"
      
      
```





## Inheritance
* [IncidentReport](IncidentReport.md)
    * **IncidentConcludingReport**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IncidentConcludingReport](https://w3id.org/lmodel/dpv/risk/IncidentConcludingReport) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident Concluding Report




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IncidentConcludingReport |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IncidentConcludingReport |
| native | risk:IncidentConcludingReport |
| exact | dpv_risk:IncidentConcludingReport, dpv_risk_owl:IncidentConcludingReport |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentConcludingReport
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentConcludingReport
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'A report describing the conclusion of an investigation regarding an

  incident where all relevant facts are known'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Concluding Report
exact_mappings:
- dpv_risk:IncidentConcludingReport
- dpv_risk_owl:IncidentConcludingReport
is_a: IncidentReport
class_uri: risk:IncidentConcludingReport

```
</details>

### Induced

<details>
```yaml
name: IncidentConcludingReport
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentConcludingReport
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'A report describing the conclusion of an investigation regarding an

  incident where all relevant facts are known'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Concluding Report
exact_mappings:
- dpv_risk:IncidentConcludingReport
- dpv_risk_owl:IncidentConcludingReport
is_a: IncidentReport
class_uri: risk:IncidentConcludingReport

```
</details></div>