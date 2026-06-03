---
search:
  boost: 10.0
---

# Class: ExternalSecurityThreat 


_Concepts associated with security threats that are likely to originate_

_externally_



<div data-search-exclude markdown="1">



URI: [risk:ExternalSecurityThreat](https://w3id.org/lmodel/dpv/risk/ExternalSecurityThreat)





```mermaid
 classDiagram
    class ExternalSecurityThreat
    click ExternalSecurityThreat href "../ExternalSecurityThreat/"
      PotentialConsequence <|-- ExternalSecurityThreat
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- ExternalSecurityThreat
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- ExternalSecurityThreat
        click PotentialRiskSource href "../PotentialRiskSource/"
      TechnicalRiskConcept <|-- ExternalSecurityThreat
        click TechnicalRiskConcept href "../TechnicalRiskConcept/"
      

      ExternalSecurityThreat <|-- CompromiseAccount
        click CompromiseAccount href "../CompromiseAccount/"
      ExternalSecurityThreat <|-- CompromiseAccountCredentials
        click CompromiseAccountCredentials href "../CompromiseAccountCredentials/"
      ExternalSecurityThreat <|-- MaliciousActivity
        click MaliciousActivity href "../MaliciousActivity/"
      ExternalSecurityThreat <|-- SecurityAttack
        click SecurityAttack href "../SecurityAttack/"
      ExternalSecurityThreat <|-- UnauthorisedActivity
        click UnauthorisedActivity href "../UnauthorisedActivity/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * **ExternalSecurityThreat** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [CompromiseAccount](CompromiseAccount.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [CompromiseAccountCredentials](CompromiseAccountCredentials.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [MaliciousActivity](MaliciousActivity.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [SecurityAttack](SecurityAttack.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [UnauthorisedActivity](UnauthorisedActivity.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ExternalSecurityThreat](https://w3id.org/lmodel/dpv/risk/ExternalSecurityThreat) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* External Security Threat




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ExternalSecurityThreat |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ExternalSecurityThreat |
| native | risk:ExternalSecurityThreat |
| exact | dpv_risk:ExternalSecurityThreat, dpv_risk_owl:ExternalSecurityThreat |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExternalSecurityThreat
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ExternalSecurityThreat
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concepts associated with security threats that are likely to originate

  externally'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- External Security Threat
exact_mappings:
- dpv_risk:ExternalSecurityThreat
- dpv_risk_owl:ExternalSecurityThreat
is_a: TechnicalRiskConcept
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:ExternalSecurityThreat

```
</details>

### Induced

<details>
```yaml
name: ExternalSecurityThreat
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ExternalSecurityThreat
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concepts associated with security threats that are likely to originate

  externally'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- External Security Threat
exact_mappings:
- dpv_risk:ExternalSecurityThreat
- dpv_risk_owl:ExternalSecurityThreat
is_a: TechnicalRiskConcept
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:ExternalSecurityThreat

```
</details></div>