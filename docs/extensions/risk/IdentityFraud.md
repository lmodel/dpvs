---
search:
  boost: 10.0
---

# Class: IdentityFraud 


_Concept representing Identity Fraud_



<div data-search-exclude markdown="1">



URI: [risk:IdentityFraud](https://w3id.org/lmodel/dpv/risk/IdentityFraud)





```mermaid
 classDiagram
    class IdentityFraud
    click IdentityFraud href "../IdentityFraud/"
      ConfidentialityConcept <|-- IdentityFraud
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      PotentialConsequence <|-- IdentityFraud
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- IdentityFraud
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- IdentityFraud
        click PotentialRiskSource href "../PotentialRiskSource/"
      Fraud <|-- IdentityFraud
        click Fraud href "../Fraud/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [MaliciousActivity](MaliciousActivity.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [Deception](Deception.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * [Fraud](Fraud.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                    * **IdentityFraud** [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IdentityFraud](https://w3id.org/lmodel/dpv/risk/IdentityFraud) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Identity Fraud




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IdentityFraud |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IdentityFraud |
| native | risk:IdentityFraud |
| exact | dpv_risk:IdentityFraud, dpv_risk_owl:IdentityFraud |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IdentityFraud
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IdentityFraud
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Identity Fraud
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Identity Fraud
exact_mappings:
- dpv_risk:IdentityFraud
- dpv_risk_owl:IdentityFraud
is_a: Fraud
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:IdentityFraud

```
</details>

### Induced

<details>
```yaml
name: IdentityFraud
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IdentityFraud
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Identity Fraud
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Identity Fraud
exact_mappings:
- dpv_risk:IdentityFraud
- dpv_risk_owl:IdentityFraud
is_a: Fraud
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:IdentityFraud

```
</details></div>