---
search:
  boost: 10.0
---

# Class: PhysicalAssault 


_Concept representing Physical Assault_



<div data-search-exclude markdown="1">



URI: [risk:PhysicalAssault](https://w3id.org/lmodel/dpv/risk/PhysicalAssault)





```mermaid
 classDiagram
    class PhysicalAssault
    click PhysicalAssault href "../PhysicalAssault/"
      PotentialConsequence <|-- PhysicalAssault
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- PhysicalAssault
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- PhysicalAssault
        click PotentialRisk href "../PotentialRisk/"
      PhysicalSafety <|-- PhysicalAssault
        click PhysicalSafety href "../PhysicalSafety/"
      Harm <|-- PhysicalAssault
        click Harm href "../Harm/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [HealthSafety](HealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Harm](Harm.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [IndividualRisk](IndividualRisk.md)]
                * **PhysicalAssault** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PhysicalSafety](PhysicalSafety.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:PhysicalAssault](https://w3id.org/lmodel/dpv/risk/PhysicalAssault) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Physical Assault




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#PhysicalAssault |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:PhysicalAssault |
| native | risk:PhysicalAssault |
| exact | dpv_risk:PhysicalAssault, dpv_risk_owl:PhysicalAssault |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PhysicalAssault
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PhysicalAssault
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Physical Assault
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Physical Assault
exact_mappings:
- dpv_risk:PhysicalAssault
- dpv_risk_owl:PhysicalAssault
is_a: Harm
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- PhysicalSafety
class_uri: risk:PhysicalAssault

```
</details>

### Induced

<details>
```yaml
name: PhysicalAssault
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PhysicalAssault
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Physical Assault
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Physical Assault
exact_mappings:
- dpv_risk:PhysicalAssault
- dpv_risk_owl:PhysicalAssault
is_a: Harm
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- PhysicalSafety
class_uri: risk:PhysicalAssault

```
</details></div>