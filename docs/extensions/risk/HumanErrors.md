---
search:
  boost: 10.0
---

# Class: HumanErrors 


_Concept representing activities that are errors caused by humans without_

_intention and which was not caused by following rules or policies or_

_instructions that were not from the person_



<div data-search-exclude markdown="1">



URI: [risk:HumanErrors](https://w3id.org/lmodel/dpv/risk/HumanErrors)





```mermaid
 classDiagram
    class HumanErrors
    click HumanErrors href "../HumanErrors/"
      PotentialConsequence <|-- HumanErrors
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- HumanErrors
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- HumanErrors
        click PotentialRiskSource href "../PotentialRiskSource/"
      UserRisks <|-- HumanErrors
        click UserRisks href "../UserRisks/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [UserRisks](UserRisks.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **HumanErrors** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:HumanErrors](https://w3id.org/lmodel/dpv/risk/HumanErrors) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Human Errors




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#HumanErrors |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:HumanErrors |
| native | risk:HumanErrors |
| exact | dpv_risk:HumanErrors, dpv_risk_owl:HumanErrors |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HumanErrors
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#HumanErrors
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing activities that are errors caused by humans without

  intention and which was not caused by following rules or policies or

  instructions that were not from the person'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Human Errors
exact_mappings:
- dpv_risk:HumanErrors
- dpv_risk_owl:HumanErrors
is_a: UserRisks
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:HumanErrors

```
</details>

### Induced

<details>
```yaml
name: HumanErrors
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#HumanErrors
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing activities that are errors caused by humans without

  intention and which was not caused by following rules or policies or

  instructions that were not from the person'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Human Errors
exact_mappings:
- dpv_risk:HumanErrors
- dpv_risk_owl:HumanErrors
is_a: UserRisks
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:HumanErrors

```
</details></div>