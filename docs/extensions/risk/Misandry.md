---
search:
  boost: 10.0
---

# Class: Misandry 


_Dislike, contempt, or prejudice against men_



<div data-search-exclude markdown="1">



URI: [risk:Misandry](https://w3id.org/lmodel/dpv/risk/Misandry)





```mermaid
 classDiagram
    class Misandry
    click Misandry href "../Misandry/"
      PotentialConsequence <|-- Misandry
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Misandry
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Misandry
        click PotentialRisk href "../PotentialRisk/"
      Sexism <|-- Misandry
        click Sexism href "../Sexism/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [Sexism](Sexism.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * **Misandry** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Misandry](https://w3id.org/lmodel/dpv/risk/Misandry) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Misandry




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Misandry |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Misandry |
| native | risk:Misandry |
| exact | dpv_risk:Misandry, dpv_risk_owl:Misandry |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Misandry
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Misandry
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Dislike, contempt, or prejudice against men
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Misandry
exact_mappings:
- dpv_risk:Misandry
- dpv_risk_owl:Misandry
is_a: Sexism
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Misandry

```
</details>

### Induced

<details>
```yaml
name: Misandry
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Misandry
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Dislike, contempt, or prejudice against men
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Misandry
exact_mappings:
- dpv_risk:Misandry
- dpv_risk_owl:Misandry
is_a: Sexism
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Misandry

```
</details></div>