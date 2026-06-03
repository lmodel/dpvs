---
search:
  boost: 10.0
---

# Class: UserRisks 


_Concepts associated with risks that arise due to User or Human use_



<div data-search-exclude markdown="1">



URI: [risk:UserRisks](https://w3id.org/lmodel/dpv/risk/UserRisks)





```mermaid
 classDiagram
    class UserRisks
    click UserRisks href "../UserRisks/"
      PotentialConsequence <|-- UserRisks
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- UserRisks
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- UserRisks
        click PotentialRiskSource href "../PotentialRiskSource/"
      OrganisationalRiskConcept <|-- UserRisks
        click OrganisationalRiskConcept href "../OrganisationalRiskConcept/"
      

      UserRisks <|-- ErroneousUse
        click ErroneousUse href "../ErroneousUse/"
      UserRisks <|-- HumanErrors
        click HumanErrors href "../HumanErrors/"
      UserRisks <|-- Misuse
        click Misuse href "../Misuse/"
      

      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * **UserRisks** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [ErroneousUse](ErroneousUse.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [HumanErrors](HumanErrors.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [Misuse](Misuse.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:UserRisks](https://w3id.org/lmodel/dpv/risk/UserRisks) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* User Risks




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#UserRisks |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:UserRisks |
| native | risk:UserRisks |
| exact | dpv_risk:UserRisks, dpv_risk_owl:UserRisks |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UserRisks
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UserRisks
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts associated with risks that arise due to User or Human use
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- User Risks
exact_mappings:
- dpv_risk:UserRisks
- dpv_risk_owl:UserRisks
is_a: OrganisationalRiskConcept
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UserRisks

```
</details>

### Induced

<details>
```yaml
name: UserRisks
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UserRisks
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts associated with risks that arise due to User or Human use
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- User Risks
exact_mappings:
- dpv_risk:UserRisks
- dpv_risk_owl:UserRisks
is_a: OrganisationalRiskConcept
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UserRisks

```
</details></div>