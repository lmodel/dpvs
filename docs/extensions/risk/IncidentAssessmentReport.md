---
search:
  boost: 10.0
---

# Class: IncidentAssessmentReport 


_A report describing the assessment of an incident in terms of its_

_effects or impacts_



<div data-search-exclude markdown="1">



URI: [risk:IncidentAssessmentReport](https://w3id.org/lmodel/dpv/risk/IncidentAssessmentReport)





```mermaid
 classDiagram
    class IncidentAssessmentReport
    click IncidentAssessmentReport href "../IncidentAssessmentReport/"
      IncidentReport <|-- IncidentAssessmentReport
        click IncidentReport href "../IncidentReport/"
      
      
```





## Inheritance
* [IncidentReport](IncidentReport.md)
    * **IncidentAssessmentReport**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IncidentAssessmentReport](https://w3id.org/lmodel/dpv/risk/IncidentAssessmentReport) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident Assessment Report




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IncidentAssessmentReport |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IncidentAssessmentReport |
| native | risk:IncidentAssessmentReport |
| exact | dpv_risk:IncidentAssessmentReport, dpv_risk_owl:IncidentAssessmentReport |
| related | iso42001:AISystemImpactAssessment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentAssessmentReport
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentAssessmentReport
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'A report describing the assessment of an incident in terms of its

  effects or impacts'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Assessment Report
exact_mappings:
- dpv_risk:IncidentAssessmentReport
- dpv_risk_owl:IncidentAssessmentReport
related_mappings:
- iso42001:AISystemImpactAssessment
is_a: IncidentReport
class_uri: risk:IncidentAssessmentReport

```
</details>

### Induced

<details>
```yaml
name: IncidentAssessmentReport
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentAssessmentReport
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'A report describing the assessment of an incident in terms of its

  effects or impacts'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Assessment Report
exact_mappings:
- dpv_risk:IncidentAssessmentReport
- dpv_risk_owl:IncidentAssessmentReport
related_mappings:
- iso42001:AISystemImpactAssessment
is_a: IncidentReport
class_uri: risk:IncidentAssessmentReport

```
</details></div>