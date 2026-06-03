---
search:
  boost: 10.0
---

# Class: IncidentMitigationMeasure 


_A mitigation measure taken in response specifically to mitigate an_

_incident and prevent it from occurring again_



<div data-search-exclude markdown="1">



URI: [risk:IncidentMitigationMeasure](https://w3id.org/lmodel/dpv/risk/IncidentMitigationMeasure)





```mermaid
 classDiagram
    class IncidentMitigationMeasure
    click IncidentMitigationMeasure href "../IncidentMitigationMeasure/"
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IncidentMitigationMeasure](https://w3id.org/lmodel/dpv/risk/IncidentMitigationMeasure) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident Mitigation Measure




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IncidentMitigationMeasure |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IncidentMitigationMeasure |
| native | risk:IncidentMitigationMeasure |
| exact | dpv_risk:IncidentMitigationMeasure, dpv_risk_owl:IncidentMitigationMeasure |
| close | iso42001:AIRiskTreatmentPlan |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentMitigationMeasure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentMitigationMeasure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'A mitigation measure taken in response specifically to mitigate an

  incident and prevent it from occurring again'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Mitigation Measure
exact_mappings:
- dpv_risk:IncidentMitigationMeasure
- dpv_risk_owl:IncidentMitigationMeasure
close_mappings:
- iso42001:AIRiskTreatmentPlan
class_uri: risk:IncidentMitigationMeasure

```
</details>

### Induced

<details>
```yaml
name: IncidentMitigationMeasure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentMitigationMeasure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'A mitigation measure taken in response specifically to mitigate an

  incident and prevent it from occurring again'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Mitigation Measure
exact_mappings:
- dpv_risk:IncidentMitigationMeasure
- dpv_risk_owl:IncidentMitigationMeasure
close_mappings:
- iso42001:AIRiskTreatmentPlan
class_uri: risk:IncidentMitigationMeasure

```
</details></div>