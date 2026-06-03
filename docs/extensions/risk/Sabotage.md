---
search:
  boost: 10.0
---

# Class: Sabotage 


_Concept representing Sabotage_



<div data-search-exclude markdown="1">



URI: [risk:Sabotage](https://w3id.org/lmodel/dpv/risk/Sabotage)





```mermaid
 classDiagram
    class Sabotage
    click Sabotage href "../Sabotage/"
      AvailabilityConcept <|-- Sabotage
        click AvailabilityConcept href "../AvailabilityConcept/"
      IntegrityConcept <|-- Sabotage
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialConsequence <|-- Sabotage
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- Sabotage
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- Sabotage
        click PotentialRiskSource href "../PotentialRiskSource/"
      Deception <|-- Sabotage
        click Deception href "../Deception/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [MaliciousActivity](MaliciousActivity.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [Deception](Deception.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **Sabotage** [ [AvailabilityConcept](AvailabilityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Sabotage](https://w3id.org/lmodel/dpv/risk/Sabotage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Sabotage




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Sabotage |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Sabotage |
| native | risk:Sabotage |
| exact | dpv_risk:Sabotage, dpv_risk_owl:Sabotage |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Sabotage
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Sabotage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Sabotage
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Sabotage
exact_mappings:
- dpv_risk:Sabotage
- dpv_risk_owl:Sabotage
is_a: Deception
mixins:
- AvailabilityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:Sabotage

```
</details>

### Induced

<details>
```yaml
name: Sabotage
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Sabotage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Sabotage
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Sabotage
exact_mappings:
- dpv_risk:Sabotage
- dpv_risk_owl:Sabotage
is_a: Deception
mixins:
- AvailabilityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:Sabotage

```
</details></div>