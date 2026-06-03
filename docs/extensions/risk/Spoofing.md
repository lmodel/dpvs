---
search:
  boost: 10.0
---

# Class: Spoofing 


_Concept representing Spoofing_



<div data-search-exclude markdown="1">



URI: [risk:Spoofing](https://w3id.org/lmodel/dpv/risk/Spoofing)





```mermaid
 classDiagram
    class Spoofing
    click Spoofing href "../Spoofing/"
      ConfidentialityConcept <|-- Spoofing
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      IntegrityConcept <|-- Spoofing
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialConsequence <|-- Spoofing
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- Spoofing
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- Spoofing
        click PotentialRiskSource href "../PotentialRiskSource/"
      Deception <|-- Spoofing
        click Deception href "../Deception/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [MaliciousActivity](MaliciousActivity.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [Deception](Deception.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **Spoofing** [ [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Spoofing](https://w3id.org/lmodel/dpv/risk/Spoofing) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Spoofing




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Spoofing |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Spoofing |
| native | risk:Spoofing |
| exact | dpv_risk:Spoofing, dpv_risk_owl:Spoofing |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Spoofing
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Spoofing
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Spoofing
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Spoofing
exact_mappings:
- dpv_risk:Spoofing
- dpv_risk_owl:Spoofing
is_a: Deception
mixins:
- ConfidentialityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:Spoofing

```
</details>

### Induced

<details>
```yaml
name: Spoofing
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Spoofing
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Spoofing
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Spoofing
exact_mappings:
- dpv_risk:Spoofing
- dpv_risk_owl:Spoofing
is_a: Deception
mixins:
- ConfidentialityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:Spoofing

```
</details></div>