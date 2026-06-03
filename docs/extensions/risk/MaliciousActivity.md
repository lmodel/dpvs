---
search:
  boost: 10.0
---

# Class: MaliciousActivity 


_Intentional actions designed to harm, exploit, manipulate, or disrupt_

_individuals, systems, or organizations for personal gain or detriment to_

_others_



<div data-search-exclude markdown="1">



URI: [risk:MaliciousActivity](https://w3id.org/lmodel/dpv/risk/MaliciousActivity)





```mermaid
 classDiagram
    class MaliciousActivity
    click MaliciousActivity href "../MaliciousActivity/"
      PotentialConsequence <|-- MaliciousActivity
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- MaliciousActivity
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- MaliciousActivity
        click PotentialRiskSource href "../PotentialRiskSource/"
      ExternalSecurityThreat <|-- MaliciousActivity
        click ExternalSecurityThreat href "../ExternalSecurityThreat/"
      

      MaliciousActivity <|-- Deception
        click Deception href "../Deception/"
      MaliciousActivity <|-- Exploitation
        click Exploitation href "../Exploitation/"
      MaliciousActivity <|-- IdentityTheft
        click IdentityTheft href "../IdentityTheft/"
      MaliciousActivity <|-- IntentionalManipulation
        click IntentionalManipulation href "../IntentionalManipulation/"
      MaliciousActivity <|-- InterceptCommunications
        click InterceptCommunications href "../InterceptCommunications/"
      MaliciousActivity <|-- VulnerabilityExploitation
        click VulnerabilityExploitation href "../VulnerabilityExploitation/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **MaliciousActivity** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [Deception](Deception.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [Exploitation](Exploitation.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [IdentityTheft](IdentityTheft.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [IntentionalManipulation](IntentionalManipulation.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [InterceptCommunications](InterceptCommunications.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [VulnerabilityExploitation](VulnerabilityExploitation.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:MaliciousActivity](https://w3id.org/lmodel/dpv/risk/MaliciousActivity) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Malicious Activity




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#MaliciousActivity |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:MaliciousActivity |
| native | risk:MaliciousActivity |
| exact | dpv_risk:MaliciousActivity, dpv_risk_owl:MaliciousActivity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MaliciousActivity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#MaliciousActivity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Intentional actions designed to harm, exploit, manipulate, or disrupt

  individuals, systems, or organizations for personal gain or detriment to

  others'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Malicious Activity
exact_mappings:
- dpv_risk:MaliciousActivity
- dpv_risk_owl:MaliciousActivity
is_a: ExternalSecurityThreat
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:MaliciousActivity

```
</details>

### Induced

<details>
```yaml
name: MaliciousActivity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#MaliciousActivity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Intentional actions designed to harm, exploit, manipulate, or disrupt

  individuals, systems, or organizations for personal gain or detriment to

  others'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Malicious Activity
exact_mappings:
- dpv_risk:MaliciousActivity
- dpv_risk_owl:MaliciousActivity
is_a: ExternalSecurityThreat
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:MaliciousActivity

```
</details></div>