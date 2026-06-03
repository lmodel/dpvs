---
search:
  boost: 10.0
---

# Class: ComponentFailure 


_Concept representing Component Failure_



<div data-search-exclude markdown="1">



URI: [risk:ComponentFailure](https://w3id.org/lmodel/dpv/risk/ComponentFailure)





```mermaid
 classDiagram
    class ComponentFailure
    click ComponentFailure href "../ComponentFailure/"
      AvailabilityConcept <|-- ComponentFailure
        click AvailabilityConcept href "../AvailabilityConcept/"
      PotentialConsequence <|-- ComponentFailure
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- ComponentFailure
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- ComponentFailure
        click PotentialRiskSource href "../PotentialRiskSource/"
      OperationalSecurityRisk <|-- ComponentFailure
        click OperationalSecurityRisk href "../OperationalSecurityRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **ComponentFailure** [ [AvailabilityConcept](AvailabilityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ComponentFailure](https://w3id.org/lmodel/dpv/risk/ComponentFailure) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Component Failure


## Comments

* Here component refers to both physical and virtual components. The
failure of a component may or may not also cause a failure in other
related components or the systems they are part of



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ComponentFailure |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ComponentFailure |
| native | risk:ComponentFailure |
| exact | dpv_risk:ComponentFailure, dpv_risk_owl:ComponentFailure |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ComponentFailure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ComponentFailure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Component Failure
comments:
- 'Here component refers to both physical and virtual components. The

  failure of a component may or may not also cause a failure in other

  related components or the systems they are part of'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Component Failure
exact_mappings:
- dpv_risk:ComponentFailure
- dpv_risk_owl:ComponentFailure
is_a: OperationalSecurityRisk
mixins:
- AvailabilityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:ComponentFailure

```
</details>

### Induced

<details>
```yaml
name: ComponentFailure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ComponentFailure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Component Failure
comments:
- 'Here component refers to both physical and virtual components. The

  failure of a component may or may not also cause a failure in other

  related components or the systems they are part of'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Component Failure
exact_mappings:
- dpv_risk:ComponentFailure
- dpv_risk_owl:ComponentFailure
is_a: OperationalSecurityRisk
mixins:
- AvailabilityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:ComponentFailure

```
</details></div>