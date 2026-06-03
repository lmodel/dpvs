---
search:
  boost: 10.0
---

# Class: EquipmentFailure 


_Concept representing Equipment Failure_



<div data-search-exclude markdown="1">



URI: [risk:EquipmentFailure](https://w3id.org/lmodel/dpv/risk/EquipmentFailure)





```mermaid
 classDiagram
    class EquipmentFailure
    click EquipmentFailure href "../EquipmentFailure/"
      AvailabilityConcept <|-- EquipmentFailure
        click AvailabilityConcept href "../AvailabilityConcept/"
      PotentialConsequence <|-- EquipmentFailure
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- EquipmentFailure
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- EquipmentFailure
        click PotentialRiskSource href "../PotentialRiskSource/"
      OperationalSecurityRisk <|-- EquipmentFailure
        click OperationalSecurityRisk href "../OperationalSecurityRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **EquipmentFailure** [ [AvailabilityConcept](AvailabilityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:EquipmentFailure](https://w3id.org/lmodel/dpv/risk/EquipmentFailure) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Equipment Failure


## Comments

* Here equipment refers to physical equipment



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#EquipmentFailure |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:EquipmentFailure |
| native | risk:EquipmentFailure |
| exact | dpv_risk:EquipmentFailure, dpv_risk_owl:EquipmentFailure |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EquipmentFailure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#EquipmentFailure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Equipment Failure
comments:
- Here equipment refers to physical equipment
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Equipment Failure
exact_mappings:
- dpv_risk:EquipmentFailure
- dpv_risk_owl:EquipmentFailure
is_a: OperationalSecurityRisk
mixins:
- AvailabilityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:EquipmentFailure

```
</details>

### Induced

<details>
```yaml
name: EquipmentFailure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#EquipmentFailure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Equipment Failure
comments:
- Here equipment refers to physical equipment
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Equipment Failure
exact_mappings:
- dpv_risk:EquipmentFailure
- dpv_risk_owl:EquipmentFailure
is_a: OperationalSecurityRisk
mixins:
- AvailabilityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:EquipmentFailure

```
</details></div>