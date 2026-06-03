---
search:
  boost: 10.0
---

# Class: SystemFailure 


_Concept representing System Failure_



<div data-search-exclude markdown="1">



URI: [risk:SystemFailure](https://w3id.org/lmodel/dpv/risk/SystemFailure)





```mermaid
 classDiagram
    class SystemFailure
    click SystemFailure href "../SystemFailure/"
      AvailabilityConcept <|-- SystemFailure
        click AvailabilityConcept href "../AvailabilityConcept/"
      PotentialConsequence <|-- SystemFailure
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- SystemFailure
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- SystemFailure
        click PotentialRiskSource href "../PotentialRiskSource/"
      OperationalSecurityRisk <|-- SystemFailure
        click OperationalSecurityRisk href "../OperationalSecurityRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **SystemFailure** [ [AvailabilityConcept](AvailabilityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:SystemFailure](https://w3id.org/lmodel/dpv/risk/SystemFailure) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* System Failure


## Comments

* Here system refers to both hardware and software systems



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#SystemFailure |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:SystemFailure |
| native | risk:SystemFailure |
| exact | dpv_risk:SystemFailure, dpv_risk_owl:SystemFailure |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SystemFailure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SystemFailure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing System Failure
comments:
- Here system refers to both hardware and software systems
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- System Failure
exact_mappings:
- dpv_risk:SystemFailure
- dpv_risk_owl:SystemFailure
is_a: OperationalSecurityRisk
mixins:
- AvailabilityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:SystemFailure

```
</details>

### Induced

<details>
```yaml
name: SystemFailure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SystemFailure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing System Failure
comments:
- Here system refers to both hardware and software systems
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- System Failure
exact_mappings:
- dpv_risk:SystemFailure
- dpv_risk_owl:SystemFailure
is_a: OperationalSecurityRisk
mixins:
- AvailabilityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:SystemFailure

```
</details></div>