---
search:
  boost: 10.0
---

# Class: Deception 


_Concept representing Deception_



<div data-search-exclude markdown="1">



URI: [risk:Deception](https://w3id.org/lmodel/dpv/risk/Deception)





```mermaid
 classDiagram
    class Deception
    click Deception href "../Deception/"
      ConfidentialityConcept <|-- Deception
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      IntegrityConcept <|-- Deception
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialConsequence <|-- Deception
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- Deception
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- Deception
        click PotentialRiskSource href "../PotentialRiskSource/"
      MaliciousActivity <|-- Deception
        click MaliciousActivity href "../MaliciousActivity/"
      

      Deception <|-- Fraud
        click Fraud href "../Fraud/"
      Deception <|-- Sabotage
        click Sabotage href "../Sabotage/"
      Deception <|-- Scam
        click Scam href "../Scam/"
      Deception <|-- Spoofing
        click Spoofing href "../Spoofing/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [MaliciousActivity](MaliciousActivity.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **Deception** [ [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * [Fraud](Fraud.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * [Sabotage](Sabotage.md) [ [AvailabilityConcept](AvailabilityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * [Scam](Scam.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * [Spoofing](Spoofing.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Deception](https://w3id.org/lmodel/dpv/risk/Deception) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Deception




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Deception |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Deception |
| native | risk:Deception |
| exact | dpv_risk:Deception, dpv_risk_owl:Deception |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Deception
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Deception
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Deception
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Deception
exact_mappings:
- dpv_risk:Deception
- dpv_risk_owl:Deception
is_a: MaliciousActivity
mixins:
- ConfidentialityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:Deception

```
</details>

### Induced

<details>
```yaml
name: Deception
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Deception
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Deception
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Deception
exact_mappings:
- dpv_risk:Deception
- dpv_risk_owl:Deception
is_a: MaliciousActivity
mixins:
- ConfidentialityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:Deception

```
</details></div>