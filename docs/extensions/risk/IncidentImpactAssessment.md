---
search:
  boost: 10.0
---

# Class: IncidentImpactAssessment 


_An impact assessment associated with an incident_



<div data-search-exclude markdown="1">



URI: [risk:IncidentImpactAssessment](https://w3id.org/lmodel/dpv/risk/IncidentImpactAssessment)





```mermaid
 classDiagram
    class IncidentImpactAssessment
    click IncidentImpactAssessment href "../IncidentImpactAssessment/"
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IncidentImpactAssessment](https://w3id.org/lmodel/dpv/risk/IncidentImpactAssessment) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Incident Impact Assessment




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IncidentImpactAssessment |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IncidentImpactAssessment |
| native | risk:IncidentImpactAssessment |
| exact | dpv_risk:IncidentImpactAssessment, dpv_risk_owl:IncidentImpactAssessment |
| close | iso42001:AISystemImpactAssessment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentImpactAssessment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentImpactAssessment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: An impact assessment associated with an incident
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Impact Assessment
exact_mappings:
- dpv_risk:IncidentImpactAssessment
- dpv_risk_owl:IncidentImpactAssessment
close_mappings:
- iso42001:AISystemImpactAssessment
class_uri: risk:IncidentImpactAssessment

```
</details>

### Induced

<details>
```yaml
name: IncidentImpactAssessment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IncidentImpactAssessment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: An impact assessment associated with an incident
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Incident Impact Assessment
exact_mappings:
- dpv_risk:IncidentImpactAssessment
- dpv_risk_owl:IncidentImpactAssessment
close_mappings:
- iso42001:AISystemImpactAssessment
class_uri: risk:IncidentImpactAssessment

```
</details></div>