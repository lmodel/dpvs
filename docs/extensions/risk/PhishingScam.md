---
search:
  boost: 10.0
---

# Class: PhishingScam 


_Concept representing Phishing Scam_



<div data-search-exclude markdown="1">



URI: [risk:PhishingScam](https://w3id.org/lmodel/dpv/risk/PhishingScam)





```mermaid
 classDiagram
    class PhishingScam
    click PhishingScam href "../PhishingScam/"
      ConfidentialityConcept <|-- PhishingScam
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      PotentialConsequence <|-- PhishingScam
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- PhishingScam
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- PhishingScam
        click PotentialRiskSource href "../PotentialRiskSource/"
      Scam <|-- PhishingScam
        click Scam href "../Scam/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [MaliciousActivity](MaliciousActivity.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [Deception](Deception.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * [Scam](Scam.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                    * **PhishingScam** [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:PhishingScam](https://w3id.org/lmodel/dpv/risk/PhishingScam) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Phishing Scam




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#PhishingScam |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:PhishingScam |
| native | risk:PhishingScam |
| exact | dpv_risk:PhishingScam, dpv_risk_owl:PhishingScam |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PhishingScam
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PhishingScam
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Phishing Scam
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Phishing Scam
exact_mappings:
- dpv_risk:PhishingScam
- dpv_risk_owl:PhishingScam
is_a: Scam
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:PhishingScam

```
</details>

### Induced

<details>
```yaml
name: PhishingScam
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PhishingScam
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Phishing Scam
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Phishing Scam
exact_mappings:
- dpv_risk:PhishingScam
- dpv_risk_owl:PhishingScam
is_a: Scam
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:PhishingScam

```
</details></div>