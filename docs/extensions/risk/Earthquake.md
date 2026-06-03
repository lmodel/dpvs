---
search:
  boost: 10.0
---

# Class: Earthquake 


_The occurrence or potential occurrence of earthquakes_



<div data-search-exclude markdown="1">



URI: [risk:Earthquake](https://w3id.org/lmodel/dpv/risk/Earthquake)





```mermaid
 classDiagram
    class Earthquake
    click Earthquake href "../Earthquake/"
      PotentialConsequence <|-- Earthquake
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Earthquake
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Earthquake
        click PotentialRisk href "../PotentialRisk/"
      EnvironmentalRisk <|-- Earthquake
        click EnvironmentalRisk href "../EnvironmentalRisk/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [EnvironmentalRisk](EnvironmentalRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **Earthquake** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Earthquake](https://w3id.org/lmodel/dpv/risk/Earthquake) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Earthquake




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Earthquake |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Earthquake |
| native | risk:Earthquake |
| exact | dpv_risk:Earthquake, dpv_risk_owl:Earthquake |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Earthquake
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Earthquake
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: The occurrence or potential occurrence of earthquakes
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Earthquake
exact_mappings:
- dpv_risk:Earthquake
- dpv_risk_owl:Earthquake
is_a: EnvironmentalRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Earthquake

```
</details>

### Induced

<details>
```yaml
name: Earthquake
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Earthquake
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: The occurrence or potential occurrence of earthquakes
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Earthquake
exact_mappings:
- dpv_risk:Earthquake
- dpv_risk_owl:Earthquake
is_a: EnvironmentalRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Earthquake

```
</details></div>