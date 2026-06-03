---
search:
  boost: 10.0
---

# Class: SystemIntrusion 


_Concept representing System Intrusion_



<div data-search-exclude markdown="1">



URI: [risk:SystemIntrusion](https://w3id.org/lmodel/dpv/risk/SystemIntrusion)





```mermaid
 classDiagram
    class SystemIntrusion
    click SystemIntrusion href "../SystemIntrusion/"
      AvailabilityConcept <|-- SystemIntrusion
        click AvailabilityConcept href "../AvailabilityConcept/"
      ConfidentialityConcept <|-- SystemIntrusion
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      IntegrityConcept <|-- SystemIntrusion
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialRisk <|-- SystemIntrusion
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- SystemIntrusion
        click PotentialRiskSource href "../PotentialRiskSource/"
      SecurityAttack <|-- SystemIntrusion
        click SecurityAttack href "../SecurityAttack/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [SecurityAttack](SecurityAttack.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **SystemIntrusion** [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:SystemIntrusion](https://w3id.org/lmodel/dpv/risk/SystemIntrusion) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* System Intrusion




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#SystemIntrusion |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:SystemIntrusion |
| native | risk:SystemIntrusion |
| exact | dpv_risk:SystemIntrusion, dpv_risk_owl:SystemIntrusion |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SystemIntrusion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SystemIntrusion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing System Intrusion
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- System Intrusion
exact_mappings:
- dpv_risk:SystemIntrusion
- dpv_risk_owl:SystemIntrusion
is_a: SecurityAttack
mixins:
- AvailabilityConcept
- ConfidentialityConcept
- IntegrityConcept
- PotentialRisk
- PotentialRiskSource
class_uri: risk:SystemIntrusion

```
</details>

### Induced

<details>
```yaml
name: SystemIntrusion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SystemIntrusion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing System Intrusion
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- System Intrusion
exact_mappings:
- dpv_risk:SystemIntrusion
- dpv_risk_owl:SystemIntrusion
is_a: SecurityAttack
mixins:
- AvailabilityConcept
- ConfidentialityConcept
- IntegrityConcept
- PotentialRisk
- PotentialRiskSource
class_uri: risk:SystemIntrusion

```
</details></div>