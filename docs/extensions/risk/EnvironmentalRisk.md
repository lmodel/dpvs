---
search:
  boost: 10.0
---

# Class: EnvironmentalRisk 


_Risks and issues that have their origin in environment or can affect the_

_environment at large_



<div data-search-exclude markdown="1">



URI: [risk:EnvironmentalRisk](https://w3id.org/lmodel/dpv/risk/EnvironmentalRisk)





```mermaid
 classDiagram
    class EnvironmentalRisk
    click EnvironmentalRisk href "../EnvironmentalRisk/"
      PotentialConsequence <|-- EnvironmentalRisk
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- EnvironmentalRisk
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- EnvironmentalRisk
        click PotentialRisk href "../PotentialRisk/"
      SocietalRiskConcept <|-- EnvironmentalRisk
        click SocietalRiskConcept href "../SocietalRiskConcept/"
      

      EnvironmentalRisk <|-- DisproportionateEnergyConsumption
        click DisproportionateEnergyConsumption href "../DisproportionateEnergyConsumption/"
      EnvironmentalRisk <|-- Earthquake
        click Earthquake href "../Earthquake/"
      EnvironmentalRisk <|-- Floods
        click Floods href "../Floods/"
      

      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * **EnvironmentalRisk** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [DisproportionateEnergyConsumption](DisproportionateEnergyConsumption.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [Earthquake](Earthquake.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [Floods](Floods.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:EnvironmentalRisk](https://w3id.org/lmodel/dpv/risk/EnvironmentalRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Environmental Risk




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#EnvironmentalRisk |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:EnvironmentalRisk |
| native | risk:EnvironmentalRisk |
| exact | dpv_risk:EnvironmentalRisk, dpv_risk_owl:EnvironmentalRisk |
| related | iso42001:AIRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EnvironmentalRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#EnvironmentalRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Risks and issues that have their origin in environment or can affect
  the

  environment at large'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Environmental Risk
exact_mappings:
- dpv_risk:EnvironmentalRisk
- dpv_risk_owl:EnvironmentalRisk
related_mappings:
- iso42001:AIRisk
is_a: SocietalRiskConcept
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:EnvironmentalRisk

```
</details>

### Induced

<details>
```yaml
name: EnvironmentalRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#EnvironmentalRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Risks and issues that have their origin in environment or can affect
  the

  environment at large'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Environmental Risk
exact_mappings:
- dpv_risk:EnvironmentalRisk
- dpv_risk_owl:EnvironmentalRisk
related_mappings:
- iso42001:AIRisk
is_a: SocietalRiskConcept
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:EnvironmentalRisk

```
</details></div>