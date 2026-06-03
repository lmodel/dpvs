---
search:
  boost: 10.0
---

# Class: Scam 


_Concept representing Scam_



<div data-search-exclude markdown="1">



URI: [risk:Scam](https://w3id.org/lmodel/dpv/risk/Scam)





```mermaid
 classDiagram
    class Scam
    click Scam href "../Scam/"
      ConfidentialityConcept <|-- Scam
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      PotentialConsequence <|-- Scam
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- Scam
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- Scam
        click PotentialRiskSource href "../PotentialRiskSource/"
      Deception <|-- Scam
        click Deception href "../Deception/"
      

      Scam <|-- PhishingScam
        click PhishingScam href "../PhishingScam/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [MaliciousActivity](MaliciousActivity.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [Deception](Deception.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **Scam** [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                    * [PhishingScam](PhishingScam.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Scam](https://w3id.org/lmodel/dpv/risk/Scam) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Scam




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Scam |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Scam |
| native | risk:Scam |
| exact | dpv_risk:Scam, dpv_risk_owl:Scam |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Scam
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Scam
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Scam
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Scam
exact_mappings:
- dpv_risk:Scam
- dpv_risk_owl:Scam
is_a: Deception
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:Scam

```
</details>

### Induced

<details>
```yaml
name: Scam
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Scam
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Scam
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Scam
exact_mappings:
- dpv_risk:Scam
- dpv_risk_owl:Scam
is_a: Deception
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:Scam

```
</details></div>