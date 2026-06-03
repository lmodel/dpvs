---
search:
  boost: 10.0
---

# Class: Sexism 


_Discrimination based on a person's sex or gender, typically involving_

_unequal treatment or stereotyping_



<div data-search-exclude markdown="1">



URI: [risk:Sexism](https://w3id.org/lmodel/dpv/risk/Sexism)





```mermaid
 classDiagram
    class Sexism
    click Sexism href "../Sexism/"
      PotentialConsequence <|-- Sexism
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Sexism
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Sexism
        click PotentialRisk href "../PotentialRisk/"
      Discrimination <|-- Sexism
        click Discrimination href "../Discrimination/"
      

      Sexism <|-- GenderDiscrimination
        click GenderDiscrimination href "../GenderDiscrimination/"
      Sexism <|-- Misandry
        click Misandry href "../Misandry/"
      Sexism <|-- Misogyny
        click Misogyny href "../Misogyny/"
      Sexism <|-- SexDiscrimination
        click SexDiscrimination href "../SexDiscrimination/"
      Sexism <|-- Transphobia
        click Transphobia href "../Transphobia/"
      

      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **Sexism** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [GenderDiscrimination](GenderDiscrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Misandry](Misandry.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Misogyny](Misogyny.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [SexDiscrimination](SexDiscrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Transphobia](Transphobia.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Sexism](https://w3id.org/lmodel/dpv/risk/Sexism) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Sexism




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Sexism |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Sexism |
| native | risk:Sexism |
| exact | dpv_risk:Sexism, dpv_risk_owl:Sexism |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Sexism
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Sexism
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Discrimination based on a person''s sex or gender, typically involving

  unequal treatment or stereotyping'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Sexism
exact_mappings:
- dpv_risk:Sexism
- dpv_risk_owl:Sexism
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Sexism

```
</details>

### Induced

<details>
```yaml
name: Sexism
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Sexism
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Discrimination based on a person''s sex or gender, typically involving

  unequal treatment or stereotyping'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Sexism
exact_mappings:
- dpv_risk:Sexism
- dpv_risk_owl:Sexism
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Sexism

```
</details></div>