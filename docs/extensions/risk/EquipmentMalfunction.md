---
search:
  boost: 10.0
---

# Class: EquipmentMalfunction 


_Concept representing Equipment Malfunction_



<div data-search-exclude markdown="1">



URI: [risk:EquipmentMalfunction](https://w3id.org/lmodel/dpv/risk/EquipmentMalfunction)





```mermaid
 classDiagram
    class EquipmentMalfunction
    click EquipmentMalfunction href "../EquipmentMalfunction/"
      AvailabilityConcept <|-- EquipmentMalfunction
        click AvailabilityConcept href "../AvailabilityConcept/"
      PotentialConsequence <|-- EquipmentMalfunction
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- EquipmentMalfunction
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- EquipmentMalfunction
        click PotentialRiskSource href "../PotentialRiskSource/"
      OperationalSecurityRisk <|-- EquipmentMalfunction
        click OperationalSecurityRisk href "../OperationalSecurityRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **EquipmentMalfunction** [ [AvailabilityConcept](AvailabilityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:EquipmentMalfunction](https://w3id.org/lmodel/dpv/risk/EquipmentMalfunction) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Equipment Malfunction


## Comments

* Here equipment refers to physical equipment



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#EquipmentMalfunction |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:EquipmentMalfunction |
| native | risk:EquipmentMalfunction |
| exact | dpv_risk:EquipmentMalfunction, dpv_risk_owl:EquipmentMalfunction |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EquipmentMalfunction
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#EquipmentMalfunction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Equipment Malfunction
comments:
- Here equipment refers to physical equipment
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Equipment Malfunction
exact_mappings:
- dpv_risk:EquipmentMalfunction
- dpv_risk_owl:EquipmentMalfunction
is_a: OperationalSecurityRisk
mixins:
- AvailabilityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:EquipmentMalfunction

```
</details>

### Induced

<details>
```yaml
name: EquipmentMalfunction
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#EquipmentMalfunction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Equipment Malfunction
comments:
- Here equipment refers to physical equipment
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Equipment Malfunction
exact_mappings:
- dpv_risk:EquipmentMalfunction
- dpv_risk_owl:EquipmentMalfunction
is_a: OperationalSecurityRisk
mixins:
- AvailabilityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:EquipmentMalfunction

```
</details></div>