---
search:
  boost: 10.0
---

# Class: Misogyny 


_Dislike, contempt, or prejudice against women_



<div data-search-exclude markdown="1">



URI: [risk:Misogyny](https://w3id.org/lmodel/dpv/risk/Misogyny)





```mermaid
 classDiagram
    class Misogyny
    click Misogyny href "../Misogyny/"
      PotentialConsequence <|-- Misogyny
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Misogyny
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Misogyny
        click PotentialRisk href "../PotentialRisk/"
      Sexism <|-- Misogyny
        click Sexism href "../Sexism/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [Sexism](Sexism.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * **Misogyny** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Misogyny](https://w3id.org/lmodel/dpv/risk/Misogyny) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Misogyny




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Misogyny |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Misogyny |
| native | risk:Misogyny |
| exact | dpv_risk:Misogyny, dpv_risk_owl:Misogyny |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Misogyny
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Misogyny
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Dislike, contempt, or prejudice against women
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Misogyny
exact_mappings:
- dpv_risk:Misogyny
- dpv_risk_owl:Misogyny
is_a: Sexism
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Misogyny

```
</details>

### Induced

<details>
```yaml
name: Misogyny
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Misogyny
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Dislike, contempt, or prejudice against women
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Misogyny
exact_mappings:
- dpv_risk:Misogyny
- dpv_risk_owl:Misogyny
is_a: Sexism
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Misogyny

```
</details></div>