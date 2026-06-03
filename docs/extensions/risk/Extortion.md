---
search:
  boost: 10.0
---

# Class: Extortion 


_Concept representing Extortion_



<div data-search-exclude markdown="1">



URI: [risk:Extortion](https://w3id.org/lmodel/dpv/risk/Extortion)





```mermaid
 classDiagram
    class Extortion
    click Extortion href "../Extortion/"
      ConfidentialityConcept <|-- Extortion
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      PotentialConsequence <|-- Extortion
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- Extortion
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- Extortion
        click PotentialRiskSource href "../PotentialRiskSource/"
      Exploitation <|-- Extortion
        click Exploitation href "../Exploitation/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [MaliciousActivity](MaliciousActivity.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [Exploitation](Exploitation.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **Extortion** [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Extortion](https://w3id.org/lmodel/dpv/risk/Extortion) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Extortion




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Extortion |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Extortion |
| native | risk:Extortion |
| exact | dpv_risk:Extortion, dpv_risk_owl:Extortion |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Extortion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Extortion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Extortion
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Extortion
exact_mappings:
- dpv_risk:Extortion
- dpv_risk_owl:Extortion
is_a: Exploitation
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:Extortion

```
</details>

### Induced

<details>
```yaml
name: Extortion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Extortion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Extortion
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Extortion
exact_mappings:
- dpv_risk:Extortion
- dpv_risk_owl:Extortion
is_a: Exploitation
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:Extortion

```
</details></div>