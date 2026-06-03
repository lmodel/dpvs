---
search:
  boost: 10.0
---

# Class: BruteForceAuthorisations 


_Concept representing Brute Force Authorisations i.e. bypassing_

_authorisations through brute forcing techniques_



<div data-search-exclude markdown="1">



URI: [risk:BruteForceAuthorisations](https://w3id.org/lmodel/dpv/risk/BruteForceAuthorisations)





```mermaid
 classDiagram
    class BruteForceAuthorisations
    click BruteForceAuthorisations href "../BruteForceAuthorisations/"
      ConfidentialityConcept <|-- BruteForceAuthorisations
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      IntegrityConcept <|-- BruteForceAuthorisations
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialRisk <|-- BruteForceAuthorisations
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- BruteForceAuthorisations
        click PotentialRiskSource href "../PotentialRiskSource/"
      SecurityAttack <|-- BruteForceAuthorisations
        click SecurityAttack href "../SecurityAttack/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [SecurityAttack](SecurityAttack.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **BruteForceAuthorisations** [ [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:BruteForceAuthorisations](https://w3id.org/lmodel/dpv/risk/BruteForceAuthorisations) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Brute Force Authorisations




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#BruteForceAuthorisations |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:BruteForceAuthorisations |
| native | risk:BruteForceAuthorisations |
| exact | dpv_risk:BruteForceAuthorisations, dpv_risk_owl:BruteForceAuthorisations |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BruteForceAuthorisations
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#BruteForceAuthorisations
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing Brute Force Authorisations i.e. bypassing

  authorisations through brute forcing techniques'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Brute Force Authorisations
exact_mappings:
- dpv_risk:BruteForceAuthorisations
- dpv_risk_owl:BruteForceAuthorisations
is_a: SecurityAttack
mixins:
- ConfidentialityConcept
- IntegrityConcept
- PotentialRisk
- PotentialRiskSource
class_uri: risk:BruteForceAuthorisations

```
</details>

### Induced

<details>
```yaml
name: BruteForceAuthorisations
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#BruteForceAuthorisations
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing Brute Force Authorisations i.e. bypassing

  authorisations through brute forcing techniques'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Brute Force Authorisations
exact_mappings:
- dpv_risk:BruteForceAuthorisations
- dpv_risk_owl:BruteForceAuthorisations
is_a: SecurityAttack
mixins:
- ConfidentialityConcept
- IntegrityConcept
- PotentialRisk
- PotentialRiskSource
class_uri: risk:BruteForceAuthorisations

```
</details></div>