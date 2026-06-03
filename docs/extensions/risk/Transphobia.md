---
search:
  boost: 10.0
---

# Class: Transphobia 


_Hostility or prejudice against transgender people or those perceived as_

_not conforming to traditional gender norms_



<div data-search-exclude markdown="1">



URI: [risk:Transphobia](https://w3id.org/lmodel/dpv/risk/Transphobia)





```mermaid
 classDiagram
    class Transphobia
    click Transphobia href "../Transphobia/"
      PotentialConsequence <|-- Transphobia
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Transphobia
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Transphobia
        click PotentialRisk href "../PotentialRisk/"
      Sexism <|-- Transphobia
        click Sexism href "../Sexism/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [Sexism](Sexism.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * **Transphobia** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Transphobia](https://w3id.org/lmodel/dpv/risk/Transphobia) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Transphobia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Transphobia |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Transphobia |
| native | risk:Transphobia |
| exact | dpv_risk:Transphobia, dpv_risk_owl:Transphobia |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Transphobia
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Transphobia
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Hostility or prejudice against transgender people or those perceived
  as

  not conforming to traditional gender norms'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Transphobia
exact_mappings:
- dpv_risk:Transphobia
- dpv_risk_owl:Transphobia
is_a: Sexism
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Transphobia

```
</details>

### Induced

<details>
```yaml
name: Transphobia
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Transphobia
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Hostility or prejudice against transgender people or those perceived
  as

  not conforming to traditional gender norms'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Transphobia
exact_mappings:
- dpv_risk:Transphobia
- dpv_risk_owl:Transphobia
is_a: Sexism
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Transphobia

```
</details></div>