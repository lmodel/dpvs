---
search:
  boost: 10.0
---

# Class: Cryptojacking 


_Concept representing Cryptojacking_



<div data-search-exclude markdown="1">



URI: [risk:Cryptojacking](https://w3id.org/lmodel/dpv/risk/Cryptojacking)





```mermaid
 classDiagram
    class Cryptojacking
    click Cryptojacking href "../Cryptojacking/"
      AvailabilityConcept <|-- Cryptojacking
        click AvailabilityConcept href "../AvailabilityConcept/"
      PotentialRisk <|-- Cryptojacking
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- Cryptojacking
        click PotentialRiskSource href "../PotentialRiskSource/"
      SecurityAttack <|-- Cryptojacking
        click SecurityAttack href "../SecurityAttack/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [SecurityAttack](SecurityAttack.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **Cryptojacking** [ [AvailabilityConcept](AvailabilityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Cryptojacking](https://w3id.org/lmodel/dpv/risk/Cryptojacking) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Cryptojacking




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Cryptojacking |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Cryptojacking |
| native | risk:Cryptojacking |
| exact | dpv_risk:Cryptojacking, dpv_risk_owl:Cryptojacking |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Cryptojacking
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Cryptojacking
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Cryptojacking
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Cryptojacking
exact_mappings:
- dpv_risk:Cryptojacking
- dpv_risk_owl:Cryptojacking
is_a: SecurityAttack
mixins:
- AvailabilityConcept
- PotentialRisk
- PotentialRiskSource
class_uri: risk:Cryptojacking

```
</details>

### Induced

<details>
```yaml
name: Cryptojacking
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Cryptojacking
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Cryptojacking
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Cryptojacking
exact_mappings:
- dpv_risk:Cryptojacking
- dpv_risk_owl:Cryptojacking
is_a: SecurityAttack
mixins:
- AvailabilityConcept
- PotentialRisk
- PotentialRiskSource
class_uri: risk:Cryptojacking

```
</details></div>