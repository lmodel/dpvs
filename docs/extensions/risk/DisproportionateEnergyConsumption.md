---
search:
  boost: 10.0
---

# Class: DisproportionateEnergyConsumption 


_The occurrence or potential occurrence of disproportionate energy_

_consumption when considering the value obtained from undertaking the_

_activity and the amount of energy being utilised_



<div data-search-exclude markdown="1">



URI: [risk:DisproportionateEnergyConsumption](https://w3id.org/lmodel/dpv/risk/DisproportionateEnergyConsumption)





```mermaid
 classDiagram
    class DisproportionateEnergyConsumption
    click DisproportionateEnergyConsumption href "../DisproportionateEnergyConsumption/"
      PotentialConsequence <|-- DisproportionateEnergyConsumption
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- DisproportionateEnergyConsumption
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- DisproportionateEnergyConsumption
        click PotentialRisk href "../PotentialRisk/"
      EnvironmentalRisk <|-- DisproportionateEnergyConsumption
        click EnvironmentalRisk href "../EnvironmentalRisk/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [EnvironmentalRisk](EnvironmentalRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **DisproportionateEnergyConsumption** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DisproportionateEnergyConsumption](https://w3id.org/lmodel/dpv/risk/DisproportionateEnergyConsumption) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Disproportionate Energy Consumption




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DisproportionateEnergyConsumption |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DisproportionateEnergyConsumption |
| native | risk:DisproportionateEnergyConsumption |
| exact | dpv_risk:DisproportionateEnergyConsumption, dpv_risk_owl:DisproportionateEnergyConsumption |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DisproportionateEnergyConsumption
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DisproportionateEnergyConsumption
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'The occurrence or potential occurrence of disproportionate energy

  consumption when considering the value obtained from undertaking the

  activity and the amount of energy being utilised'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Disproportionate Energy Consumption
exact_mappings:
- dpv_risk:DisproportionateEnergyConsumption
- dpv_risk_owl:DisproportionateEnergyConsumption
is_a: EnvironmentalRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:DisproportionateEnergyConsumption

```
</details>

### Induced

<details>
```yaml
name: DisproportionateEnergyConsumption
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DisproportionateEnergyConsumption
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'The occurrence or potential occurrence of disproportionate energy

  consumption when considering the value obtained from undertaking the

  activity and the amount of energy being utilised'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Disproportionate Energy Consumption
exact_mappings:
- dpv_risk:DisproportionateEnergyConsumption
- dpv_risk_owl:DisproportionateEnergyConsumption
is_a: EnvironmentalRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:DisproportionateEnergyConsumption

```
</details></div>