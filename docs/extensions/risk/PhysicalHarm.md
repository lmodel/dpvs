---
search:
  boost: 10.0
---

# Class: PhysicalHarm 


_Concept representing physical harm to an individual or individual(s)_



<div data-search-exclude markdown="1">



URI: [risk:PhysicalHarm](https://w3id.org/lmodel/dpv/risk/PhysicalHarm)





```mermaid
 classDiagram
    class PhysicalHarm
    click PhysicalHarm href "../PhysicalHarm/"
      PotentialConsequence <|-- PhysicalHarm
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- PhysicalHarm
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- PhysicalHarm
        click PotentialRisk href "../PotentialRisk/"
      PhysicalHealth <|-- PhysicalHarm
        click PhysicalHealth href "../PhysicalHealth/"
      Harm <|-- PhysicalHarm
        click Harm href "../Harm/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [HealthSafety](HealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Harm](Harm.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [IndividualRisk](IndividualRisk.md)]
                * **PhysicalHarm** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PhysicalHealth](PhysicalHealth.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:PhysicalHarm](https://w3id.org/lmodel/dpv/risk/PhysicalHarm) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Physical Harm




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#PhysicalHarm |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:PhysicalHarm |
| native | risk:PhysicalHarm |
| exact | dpv_risk:PhysicalHarm, dpv_risk_owl:PhysicalHarm |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PhysicalHarm
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PhysicalHarm
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing physical harm to an individual or individual(s)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Physical Harm
exact_mappings:
- dpv_risk:PhysicalHarm
- dpv_risk_owl:PhysicalHarm
is_a: Harm
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- PhysicalHealth
class_uri: risk:PhysicalHarm

```
</details>

### Induced

<details>
```yaml
name: PhysicalHarm
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PhysicalHarm
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing physical harm to an individual or individual(s)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Physical Harm
exact_mappings:
- dpv_risk:PhysicalHarm
- dpv_risk_owl:PhysicalHarm
is_a: Harm
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- PhysicalHealth
class_uri: risk:PhysicalHarm

```
</details></div>