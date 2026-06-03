---
search:
  boost: 10.0
---

# Class: OrganisationalRiskConcept 


_Risk concepts, including any potential risk sources, consequences, or_

_impacts, that are organisational in nature or relate to an_

_organisational process_



<div data-search-exclude markdown="1">



URI: [risk:OrganisationalRiskConcept](https://w3id.org/lmodel/dpv/risk/OrganisationalRiskConcept)





```mermaid
 classDiagram
    class OrganisationalRiskConcept
    click OrganisationalRiskConcept href "../OrganisationalRiskConcept/"
      PotentialConsequence <|-- OrganisationalRiskConcept
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- OrganisationalRiskConcept
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- OrganisationalRiskConcept
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- OrganisationalRiskConcept
        click PotentialRiskSource href "../PotentialRiskSource/"
      

      OrganisationalRiskConcept <|-- FinancialImpact
        click FinancialImpact href "../FinancialImpact/"
      OrganisationalRiskConcept <|-- OrganisationalManagementRisk
        click OrganisationalManagementRisk href "../OrganisationalManagementRisk/"
      OrganisationalRiskConcept <|-- ReputationalRisk
        click ReputationalRisk href "../ReputationalRisk/"
      OrganisationalRiskConcept <|-- ServiceRelatedConsequence
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      OrganisationalRiskConcept <|-- UserRisks
        click UserRisks href "../UserRisks/"
      

      
```





## Inheritance
* **OrganisationalRiskConcept** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [FinancialImpact](FinancialImpact.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
    * [OrganisationalManagementRisk](OrganisationalManagementRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ReputationalRisk](ReputationalRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
    * [UserRisks](UserRisks.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:OrganisationalRiskConcept](https://w3id.org/lmodel/dpv/risk/OrganisationalRiskConcept) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Organisational Risk Concept


## Comments

* Organisational in this context refers to an organisation which is not
human but is managed by humans



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#OrganisationalRiskConcept |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:OrganisationalRiskConcept |
| native | risk:OrganisationalRiskConcept |
| exact | dpv_risk:OrganisationalRiskConcept, dpv_risk_owl:OrganisationalRiskConcept |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OrganisationalRiskConcept
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#OrganisationalRiskConcept
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Risk concepts, including any potential risk sources, consequences, or

  impacts, that are organisational in nature or relate to an

  organisational process'
comments:
- 'Organisational in this context refers to an organisation which is not

  human but is managed by humans'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Organisational Risk Concept
exact_mappings:
- dpv_risk:OrganisationalRiskConcept
- dpv_risk_owl:OrganisationalRiskConcept
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- PotentialRiskSource
class_uri: risk:OrganisationalRiskConcept

```
</details>

### Induced

<details>
```yaml
name: OrganisationalRiskConcept
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#OrganisationalRiskConcept
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Risk concepts, including any potential risk sources, consequences, or

  impacts, that are organisational in nature or relate to an

  organisational process'
comments:
- 'Organisational in this context refers to an organisation which is not

  human but is managed by humans'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Organisational Risk Concept
exact_mappings:
- dpv_risk:OrganisationalRiskConcept
- dpv_risk_owl:OrganisationalRiskConcept
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- PotentialRiskSource
class_uri: risk:OrganisationalRiskConcept

```
</details></div>