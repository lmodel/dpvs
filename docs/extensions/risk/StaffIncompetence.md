---
search:
  boost: 10.0
---

# Class: StaffIncompetence 


_Concept representing incompetence of staff_



<div data-search-exclude markdown="1">



URI: [risk:StaffIncompetence](https://w3id.org/lmodel/dpv/risk/StaffIncompetence)





```mermaid
 classDiagram
    class StaffIncompetence
    click StaffIncompetence href "../StaffIncompetence/"
      PotentialConsequence <|-- StaffIncompetence
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- StaffIncompetence
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- StaffIncompetence
        click PotentialRiskSource href "../PotentialRiskSource/"
      OrganisationalManagementRisk <|-- StaffIncompetence
        click OrganisationalManagementRisk href "../OrganisationalManagementRisk/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OrganisationalManagementRisk](OrganisationalManagementRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **StaffIncompetence** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:StaffIncompetence](https://w3id.org/lmodel/dpv/risk/StaffIncompetence) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Staff Incompetence




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#StaffIncompetence |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:StaffIncompetence |
| native | risk:StaffIncompetence |
| exact | dpv_risk:StaffIncompetence, dpv_risk_owl:StaffIncompetence |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: StaffIncompetence
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#StaffIncompetence
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing incompetence of staff
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Staff Incompetence
exact_mappings:
- dpv_risk:StaffIncompetence
- dpv_risk_owl:StaffIncompetence
is_a: OrganisationalManagementRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:StaffIncompetence

```
</details>

### Induced

<details>
```yaml
name: StaffIncompetence
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#StaffIncompetence
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing incompetence of staff
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Staff Incompetence
exact_mappings:
- dpv_risk:StaffIncompetence
- dpv_risk_owl:StaffIncompetence
is_a: OrganisationalManagementRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:StaffIncompetence

```
</details></div>