---
search:
  boost: 10.0
---

# Class: IndirectDiscrimination 


_Occurs when an apparently neutral provision, criterion, or practice puts_

_individuals of a certain group at a disadvantage compared to others,_

_unless it can be objectively justified_



<div data-search-exclude markdown="1">



URI: [risk:IndirectDiscrimination](https://w3id.org/lmodel/dpv/risk/IndirectDiscrimination)





```mermaid
 classDiagram
    class IndirectDiscrimination
    click IndirectDiscrimination href "../IndirectDiscrimination/"
      PotentialConsequence <|-- IndirectDiscrimination
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- IndirectDiscrimination
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- IndirectDiscrimination
        click PotentialRisk href "../PotentialRisk/"
      Discrimination <|-- IndirectDiscrimination
        click Discrimination href "../Discrimination/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **IndirectDiscrimination** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IndirectDiscrimination](https://w3id.org/lmodel/dpv/risk/IndirectDiscrimination) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Indirect Discrimination




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IndirectDiscrimination |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IndirectDiscrimination |
| native | risk:IndirectDiscrimination |
| exact | dpv_risk:IndirectDiscrimination, dpv_risk_owl:IndirectDiscrimination |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IndirectDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IndirectDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Occurs when an apparently neutral provision, criterion, or practice
  puts

  individuals of a certain group at a disadvantage compared to others,

  unless it can be objectively justified'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Indirect Discrimination
exact_mappings:
- dpv_risk:IndirectDiscrimination
- dpv_risk_owl:IndirectDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:IndirectDiscrimination

```
</details>

### Induced

<details>
```yaml
name: IndirectDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IndirectDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Occurs when an apparently neutral provision, criterion, or practice
  puts

  individuals of a certain group at a disadvantage compared to others,

  unless it can be objectively justified'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Indirect Discrimination
exact_mappings:
- dpv_risk:IndirectDiscrimination
- dpv_risk_owl:IndirectDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:IndirectDiscrimination

```
</details></div>