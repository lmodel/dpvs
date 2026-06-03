---
search:
  boost: 10.0
---

# Class: Injury 


_Concept representing Injury_



<div data-search-exclude markdown="1">



URI: [risk:Injury](https://w3id.org/lmodel/dpv/risk/Injury)





```mermaid
 classDiagram
    class Injury
    click Injury href "../Injury/"
      PotentialConsequence <|-- Injury
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Injury
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Injury
        click PotentialRisk href "../PotentialRisk/"
      PhysicalSafety <|-- Injury
        click PhysicalSafety href "../PhysicalSafety/"
      Harm <|-- Injury
        click Harm href "../Harm/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [HealthSafety](HealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Harm](Harm.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [IndividualRisk](IndividualRisk.md)]
                * **Injury** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PhysicalSafety](PhysicalSafety.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Injury](https://w3id.org/lmodel/dpv/risk/Injury) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Injury




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Injury |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Injury |
| native | risk:Injury |
| exact | dpv_risk:Injury, dpv_risk_owl:Injury |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Injury
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Injury
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Injury
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Injury
exact_mappings:
- dpv_risk:Injury
- dpv_risk_owl:Injury
is_a: Harm
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- PhysicalSafety
class_uri: risk:Injury

```
</details>

### Induced

<details>
```yaml
name: Injury
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Injury
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Injury
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Injury
exact_mappings:
- dpv_risk:Injury
- dpv_risk_owl:Injury
is_a: Harm
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- PhysicalSafety
class_uri: risk:Injury

```
</details></div>