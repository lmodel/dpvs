---
search:
  boost: 10.0
---

# Class: ComponentMalfunction 


_Concept representing Component Malfunction_



<div data-search-exclude markdown="1">



URI: [risk:ComponentMalfunction](https://w3id.org/lmodel/dpv/risk/ComponentMalfunction)





```mermaid
 classDiagram
    class ComponentMalfunction
    click ComponentMalfunction href "../ComponentMalfunction/"
      AvailabilityConcept <|-- ComponentMalfunction
        click AvailabilityConcept href "../AvailabilityConcept/"
      PotentialConsequence <|-- ComponentMalfunction
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- ComponentMalfunction
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- ComponentMalfunction
        click PotentialRiskSource href "../PotentialRiskSource/"
      OperationalSecurityRisk <|-- ComponentMalfunction
        click OperationalSecurityRisk href "../OperationalSecurityRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **ComponentMalfunction** [ [AvailabilityConcept](AvailabilityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ComponentMalfunction](https://w3id.org/lmodel/dpv/risk/ComponentMalfunction) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Component Malfunction


## Comments

* Here component refers to both physical and virtual components. The
malfunction of a component may or may not also cause a malfunction in
other related components or the systems they are part of



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ComponentMalfunction |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ComponentMalfunction |
| native | risk:ComponentMalfunction |
| exact | dpv_risk:ComponentMalfunction, dpv_risk_owl:ComponentMalfunction |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ComponentMalfunction
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ComponentMalfunction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Component Malfunction
comments:
- 'Here component refers to both physical and virtual components. The

  malfunction of a component may or may not also cause a malfunction in

  other related components or the systems they are part of'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Component Malfunction
exact_mappings:
- dpv_risk:ComponentMalfunction
- dpv_risk_owl:ComponentMalfunction
is_a: OperationalSecurityRisk
mixins:
- AvailabilityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:ComponentMalfunction

```
</details>

### Induced

<details>
```yaml
name: ComponentMalfunction
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ComponentMalfunction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Component Malfunction
comments:
- 'Here component refers to both physical and virtual components. The

  malfunction of a component may or may not also cause a malfunction in

  other related components or the systems they are part of'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Component Malfunction
exact_mappings:
- dpv_risk:ComponentMalfunction
- dpv_risk_owl:ComponentMalfunction
is_a: OperationalSecurityRisk
mixins:
- AvailabilityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:ComponentMalfunction

```
</details></div>