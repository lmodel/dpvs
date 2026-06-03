---
search:
  boost: 10.0
---

# Class: OrganisationalManagementRisk 


_Concept representing issues and risks associated with the management of_

_operations and resources by the organisation_



<div data-search-exclude markdown="1">



URI: [risk:OrganisationalManagementRisk](https://w3id.org/lmodel/dpv/risk/OrganisationalManagementRisk)





```mermaid
 classDiagram
    class OrganisationalManagementRisk
    click OrganisationalManagementRisk href "../OrganisationalManagementRisk/"
      PotentialConsequence <|-- OrganisationalManagementRisk
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- OrganisationalManagementRisk
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- OrganisationalManagementRisk
        click PotentialRiskSource href "../PotentialRiskSource/"
      OrganisationalRiskConcept <|-- OrganisationalManagementRisk
        click OrganisationalRiskConcept href "../OrganisationalRiskConcept/"
      

      OrganisationalManagementRisk <|-- DocumentationIssues
        click DocumentationIssues href "../DocumentationIssues/"
      OrganisationalManagementRisk <|-- HumanOversightIneffective
        click HumanOversightIneffective href "../HumanOversightIneffective/"
      OrganisationalManagementRisk <|-- HumanOversightInsufficient
        click HumanOversightInsufficient href "../HumanOversightInsufficient/"
      OrganisationalManagementRisk <|-- LackOfSystemTransparency
        click LackOfSystemTransparency href "../LackOfSystemTransparency/"
      OrganisationalManagementRisk <|-- StaffIncompetence
        click StaffIncompetence href "../StaffIncompetence/"
      OrganisationalManagementRisk <|-- TechnologyOverreliance
        click TechnologyOverreliance href "../TechnologyOverreliance/"
      

      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * **OrganisationalManagementRisk** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [DocumentationIssues](DocumentationIssues.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [HumanOversightIneffective](HumanOversightIneffective.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [HumanOversightInsufficient](HumanOversightInsufficient.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [LackOfSystemTransparency](LackOfSystemTransparency.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [StaffIncompetence](StaffIncompetence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [TechnologyOverreliance](TechnologyOverreliance.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:OrganisationalManagementRisk](https://w3id.org/lmodel/dpv/risk/OrganisationalManagementRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Organisational Management Risk




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#OrganisationalManagementRisk |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:OrganisationalManagementRisk |
| native | risk:OrganisationalManagementRisk |
| exact | dpv_risk:OrganisationalManagementRisk, dpv_risk_owl:OrganisationalManagementRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OrganisationalManagementRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#OrganisationalManagementRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing issues and risks associated with the management
  of

  operations and resources by the organisation'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Organisational Management Risk
exact_mappings:
- dpv_risk:OrganisationalManagementRisk
- dpv_risk_owl:OrganisationalManagementRisk
is_a: OrganisationalRiskConcept
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:OrganisationalManagementRisk

```
</details>

### Induced

<details>
```yaml
name: OrganisationalManagementRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#OrganisationalManagementRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing issues and risks associated with the management
  of

  operations and resources by the organisation'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Organisational Management Risk
exact_mappings:
- dpv_risk:OrganisationalManagementRisk
- dpv_risk_owl:OrganisationalManagementRisk
is_a: OrganisationalRiskConcept
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:OrganisationalManagementRisk

```
</details></div>