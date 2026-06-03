---
search:
  boost: 10.0
---

# Class: SecurityAttack 


_Concept representing an attack on security with the aim of undermining_

_it_



<div data-search-exclude markdown="1">



URI: [risk:SecurityAttack](https://w3id.org/lmodel/dpv/risk/SecurityAttack)





```mermaid
 classDiagram
    class SecurityAttack
    click SecurityAttack href "../SecurityAttack/"
      AvailabilityConcept <|-- SecurityAttack
        click AvailabilityConcept href "../AvailabilityConcept/"
      ConfidentialityConcept <|-- SecurityAttack
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      IntegrityConcept <|-- SecurityAttack
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialRisk <|-- SecurityAttack
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- SecurityAttack
        click PotentialRiskSource href "../PotentialRiskSource/"
      ExternalSecurityThreat <|-- SecurityAttack
        click ExternalSecurityThreat href "../ExternalSecurityThreat/"
      

      SecurityAttack <|-- BruteForceAuthorisations
        click BruteForceAuthorisations href "../BruteForceAuthorisations/"
      SecurityAttack <|-- Cryptojacking
        click Cryptojacking href "../Cryptojacking/"
      SecurityAttack <|-- DenialServiceAttack
        click DenialServiceAttack href "../DenialServiceAttack/"
      SecurityAttack <|-- MaliciousCodeAttack
        click MaliciousCodeAttack href "../MaliciousCodeAttack/"
      SecurityAttack <|-- MalwareAttack
        click MalwareAttack href "../MalwareAttack/"
      SecurityAttack <|-- SystemIntrusion
        click SystemIntrusion href "../SystemIntrusion/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **SecurityAttack** [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [BruteForceAuthorisations](BruteForceAuthorisations.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [Cryptojacking](Cryptojacking.md) [ [AvailabilityConcept](AvailabilityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [DenialServiceAttack](DenialServiceAttack.md) [ [AvailabilityConcept](AvailabilityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [MaliciousCodeAttack](MaliciousCodeAttack.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [MalwareAttack](MalwareAttack.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [SystemIntrusion](SystemIntrusion.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:SecurityAttack](https://w3id.org/lmodel/dpv/risk/SecurityAttack) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Security Attack




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#SecurityAttack |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:SecurityAttack |
| native | risk:SecurityAttack |
| exact | dpv_risk:SecurityAttack, dpv_risk_owl:SecurityAttack |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SecurityAttack
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SecurityAttack
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing an attack on security with the aim of undermining

  it'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Security Attack
exact_mappings:
- dpv_risk:SecurityAttack
- dpv_risk_owl:SecurityAttack
is_a: ExternalSecurityThreat
mixins:
- AvailabilityConcept
- ConfidentialityConcept
- IntegrityConcept
- PotentialRisk
- PotentialRiskSource
class_uri: risk:SecurityAttack

```
</details>

### Induced

<details>
```yaml
name: SecurityAttack
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SecurityAttack
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing an attack on security with the aim of undermining

  it'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Security Attack
exact_mappings:
- dpv_risk:SecurityAttack
- dpv_risk_owl:SecurityAttack
is_a: ExternalSecurityThreat
mixins:
- AvailabilityConcept
- ConfidentialityConcept
- IntegrityConcept
- PotentialRisk
- PotentialRiskSource
class_uri: risk:SecurityAttack

```
</details></div>