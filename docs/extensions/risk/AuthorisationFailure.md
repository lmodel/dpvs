---
search:
  boost: 10.0
---

# Class: AuthorisationFailure 


_Concept representing Authorisation Failure_



<div data-search-exclude markdown="1">



URI: [risk:AuthorisationFailure](https://w3id.org/lmodel/dpv/risk/AuthorisationFailure)





```mermaid
 classDiagram
    class AuthorisationFailure
    click AuthorisationFailure href "../AuthorisationFailure/"
      ConfidentialityConcept <|-- AuthorisationFailure
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      IntegrityConcept <|-- AuthorisationFailure
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialRisk <|-- AuthorisationFailure
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- AuthorisationFailure
        click PotentialRiskSource href "../PotentialRiskSource/"
      OperationalSecurityRisk <|-- AuthorisationFailure
        click OperationalSecurityRisk href "../OperationalSecurityRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **AuthorisationFailure** [ [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:AuthorisationFailure](https://w3id.org/lmodel/dpv/risk/AuthorisationFailure) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Authorisation Failure




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#AuthorisationFailure |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:AuthorisationFailure |
| native | risk:AuthorisationFailure |
| exact | dpv_risk:AuthorisationFailure, dpv_risk_owl:AuthorisationFailure |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AuthorisationFailure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AuthorisationFailure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Authorisation Failure
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Authorisation Failure
exact_mappings:
- dpv_risk:AuthorisationFailure
- dpv_risk_owl:AuthorisationFailure
is_a: OperationalSecurityRisk
mixins:
- ConfidentialityConcept
- IntegrityConcept
- PotentialRisk
- PotentialRiskSource
class_uri: risk:AuthorisationFailure

```
</details>

### Induced

<details>
```yaml
name: AuthorisationFailure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AuthorisationFailure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Authorisation Failure
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Authorisation Failure
exact_mappings:
- dpv_risk:AuthorisationFailure
- dpv_risk_owl:AuthorisationFailure
is_a: OperationalSecurityRisk
mixins:
- ConfidentialityConcept
- IntegrityConcept
- PotentialRisk
- PotentialRiskSource
class_uri: risk:AuthorisationFailure

```
</details></div>