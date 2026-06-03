---
search:
  boost: 10.0
---

# Class: SystemMalfunction 


_Concept representing System Malfunction_



<div data-search-exclude markdown="1">



URI: [risk:SystemMalfunction](https://w3id.org/lmodel/dpv/risk/SystemMalfunction)





```mermaid
 classDiagram
    class SystemMalfunction
    click SystemMalfunction href "../SystemMalfunction/"
      AvailabilityConcept <|-- SystemMalfunction
        click AvailabilityConcept href "../AvailabilityConcept/"
      PotentialConsequence <|-- SystemMalfunction
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- SystemMalfunction
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- SystemMalfunction
        click PotentialRiskSource href "../PotentialRiskSource/"
      OperationalSecurityRisk <|-- SystemMalfunction
        click OperationalSecurityRisk href "../OperationalSecurityRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **SystemMalfunction** [ [AvailabilityConcept](AvailabilityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:SystemMalfunction](https://w3id.org/lmodel/dpv/risk/SystemMalfunction) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* System Malfunction


## Comments

* Here system refers to both hardware and software systems



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#SystemMalfunction |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:SystemMalfunction |
| native | risk:SystemMalfunction |
| exact | dpv_risk:SystemMalfunction, dpv_risk_owl:SystemMalfunction |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SystemMalfunction
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SystemMalfunction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing System Malfunction
comments:
- Here system refers to both hardware and software systems
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- System Malfunction
exact_mappings:
- dpv_risk:SystemMalfunction
- dpv_risk_owl:SystemMalfunction
is_a: OperationalSecurityRisk
mixins:
- AvailabilityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:SystemMalfunction

```
</details>

### Induced

<details>
```yaml
name: SystemMalfunction
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SystemMalfunction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing System Malfunction
comments:
- Here system refers to both hardware and software systems
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- System Malfunction
exact_mappings:
- dpv_risk:SystemMalfunction
- dpv_risk_owl:SystemMalfunction
is_a: OperationalSecurityRisk
mixins:
- AvailabilityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:SystemMalfunction

```
</details></div>