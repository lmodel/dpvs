---
search:
  boost: 10.0
---

# Class: MaliciousCodeAttack 


_Concept representing Malicious Code Attack_



<div data-search-exclude markdown="1">



URI: [risk:MaliciousCodeAttack](https://w3id.org/lmodel/dpv/risk/MaliciousCodeAttack)





```mermaid
 classDiagram
    class MaliciousCodeAttack
    click MaliciousCodeAttack href "../MaliciousCodeAttack/"
      AvailabilityConcept <|-- MaliciousCodeAttack
        click AvailabilityConcept href "../AvailabilityConcept/"
      ConfidentialityConcept <|-- MaliciousCodeAttack
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      IntegrityConcept <|-- MaliciousCodeAttack
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialRisk <|-- MaliciousCodeAttack
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- MaliciousCodeAttack
        click PotentialRiskSource href "../PotentialRiskSource/"
      SecurityAttack <|-- MaliciousCodeAttack
        click SecurityAttack href "../SecurityAttack/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [SecurityAttack](SecurityAttack.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **MaliciousCodeAttack** [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:MaliciousCodeAttack](https://w3id.org/lmodel/dpv/risk/MaliciousCodeAttack) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Malicious Code Attack




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#MaliciousCodeAttack |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:MaliciousCodeAttack |
| native | risk:MaliciousCodeAttack |
| exact | dpv_risk:MaliciousCodeAttack, dpv_risk_owl:MaliciousCodeAttack |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MaliciousCodeAttack
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#MaliciousCodeAttack
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Malicious Code Attack
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Malicious Code Attack
exact_mappings:
- dpv_risk:MaliciousCodeAttack
- dpv_risk_owl:MaliciousCodeAttack
is_a: SecurityAttack
mixins:
- AvailabilityConcept
- ConfidentialityConcept
- IntegrityConcept
- PotentialRisk
- PotentialRiskSource
class_uri: risk:MaliciousCodeAttack

```
</details>

### Induced

<details>
```yaml
name: MaliciousCodeAttack
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#MaliciousCodeAttack
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Malicious Code Attack
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Malicious Code Attack
exact_mappings:
- dpv_risk:MaliciousCodeAttack
- dpv_risk_owl:MaliciousCodeAttack
is_a: SecurityAttack
mixins:
- AvailabilityConcept
- ConfidentialityConcept
- IntegrityConcept
- PotentialRisk
- PotentialRiskSource
class_uri: risk:MaliciousCodeAttack

```
</details></div>