---
search:
  boost: 10.0
---

# Class: Fraud 


_Concept representing Fraud_



<div data-search-exclude markdown="1">



URI: [risk:Fraud](https://w3id.org/lmodel/dpv/risk/Fraud)





```mermaid
 classDiagram
    class Fraud
    click Fraud href "../Fraud/"
      ConfidentialityConcept <|-- Fraud
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      PotentialConsequence <|-- Fraud
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- Fraud
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- Fraud
        click PotentialRiskSource href "../PotentialRiskSource/"
      Deception <|-- Fraud
        click Deception href "../Deception/"
      

      Fraud <|-- IdentityFraud
        click IdentityFraud href "../IdentityFraud/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [MaliciousActivity](MaliciousActivity.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [Deception](Deception.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **Fraud** [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                    * [IdentityFraud](IdentityFraud.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Fraud](https://w3id.org/lmodel/dpv/risk/Fraud) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Fraud




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Fraud |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Fraud |
| native | risk:Fraud |
| exact | dpv_risk:Fraud, dpv_risk_owl:Fraud |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Fraud
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Fraud
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Fraud
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Fraud
exact_mappings:
- dpv_risk:Fraud
- dpv_risk_owl:Fraud
is_a: Deception
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:Fraud

```
</details>

### Induced

<details>
```yaml
name: Fraud
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Fraud
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Fraud
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Fraud
exact_mappings:
- dpv_risk:Fraud
- dpv_risk_owl:Fraud
is_a: Deception
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:Fraud

```
</details></div>