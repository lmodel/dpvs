---
search:
  boost: 10.0
---

# Class: IdentityVerificationFailure 


_Concept representing failure to verify identity_



<div data-search-exclude markdown="1">



URI: [risk:IdentityVerificationFailure](https://w3id.org/lmodel/dpv/risk/IdentityVerificationFailure)





```mermaid
 classDiagram
    class IdentityVerificationFailure
    click IdentityVerificationFailure href "../IdentityVerificationFailure/"
      PotentialConsequence <|-- IdentityVerificationFailure
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- IdentityVerificationFailure
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- IdentityVerificationFailure
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- IdentityVerificationFailure
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **IdentityVerificationFailure** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IdentityVerificationFailure](https://w3id.org/lmodel/dpv/risk/IdentityVerificationFailure) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Identity Verification Failure




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IdentityVerificationFailure |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IdentityVerificationFailure |
| native | risk:IdentityVerificationFailure |
| exact | dpv_risk:IdentityVerificationFailure, dpv_risk_owl:IdentityVerificationFailure |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IdentityVerificationFailure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IdentityVerificationFailure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing failure to verify identity
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Identity Verification Failure
exact_mappings:
- dpv_risk:IdentityVerificationFailure
- dpv_risk_owl:IdentityVerificationFailure
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:IdentityVerificationFailure

```
</details>

### Induced

<details>
```yaml
name: IdentityVerificationFailure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IdentityVerificationFailure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing failure to verify identity
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Identity Verification Failure
exact_mappings:
- dpv_risk:IdentityVerificationFailure
- dpv_risk_owl:IdentityVerificationFailure
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:IdentityVerificationFailure

```
</details></div>