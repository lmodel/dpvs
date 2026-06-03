---
search:
  boost: 10.0
---

# Class: AgeDiscrimination 


_Discrimination based on a person's age, often impacting older or younger_

_individuals_



<div data-search-exclude markdown="1">



URI: [risk:AgeDiscrimination](https://w3id.org/lmodel/dpv/risk/AgeDiscrimination)





```mermaid
 classDiagram
    class AgeDiscrimination
    click AgeDiscrimination href "../AgeDiscrimination/"
      PotentialConsequence <|-- AgeDiscrimination
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- AgeDiscrimination
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- AgeDiscrimination
        click PotentialRisk href "../PotentialRisk/"
      Discrimination <|-- AgeDiscrimination
        click Discrimination href "../Discrimination/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **AgeDiscrimination** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:AgeDiscrimination](https://w3id.org/lmodel/dpv/risk/AgeDiscrimination) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Age Discrimination




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#AgeDiscrimination |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:AgeDiscrimination |
| native | risk:AgeDiscrimination |
| exact | dpv_risk:AgeDiscrimination, dpv_risk_owl:AgeDiscrimination |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AgeDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AgeDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Discrimination based on a person''s age, often impacting older or younger

  individuals'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Age Discrimination
exact_mappings:
- dpv_risk:AgeDiscrimination
- dpv_risk_owl:AgeDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:AgeDiscrimination

```
</details>

### Induced

<details>
```yaml
name: AgeDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AgeDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Discrimination based on a person''s age, often impacting older or younger

  individuals'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Age Discrimination
exact_mappings:
- dpv_risk:AgeDiscrimination
- dpv_risk_owl:AgeDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:AgeDiscrimination

```
</details></div>