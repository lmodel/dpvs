---
search:
  boost: 10.0
---

# Class: RightsViolated 


_The infringement or breach of rights in a manner that constitutes a_

_'violation' of those rights_



<div data-search-exclude markdown="1">



URI: [risk:RightsViolated](https://w3id.org/lmodel/dpv/risk/RightsViolated)





```mermaid
 classDiagram
    class RightsViolated
    click RightsViolated href "../RightsViolated/"
      PotentialConsequence <|-- RightsViolated
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- RightsViolated
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- RightsViolated
        click PotentialRisk href "../PotentialRisk/"
      RightsImpact <|-- RightsViolated
        click RightsImpact href "../RightsImpact/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [RightsImpact](RightsImpact.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **RightsViolated** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RightsViolated](https://w3id.org/lmodel/dpv/risk/RightsViolated) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Rights Violated


## Comments

* This concept was called "ViolationOfRights" in DPV 2.0. Though specified
as a plural i.e. 'rights', this concept can be applied to a singular
right



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RightsViolated |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RightsViolated |
| native | risk:RightsViolated |
| exact | dpv_risk:RightsViolated, dpv_risk_owl:RightsViolated |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RightsViolated
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RightsViolated
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'The infringement or breach of rights in a manner that constitutes a

  ''violation'' of those rights'
comments:
- 'This concept was called "ViolationOfRights" in DPV 2.0. Though specified

  as a plural i.e. ''rights'', this concept can be applied to a singular

  right'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Rights Violated
exact_mappings:
- dpv_risk:RightsViolated
- dpv_risk_owl:RightsViolated
is_a: RightsImpact
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:RightsViolated

```
</details>

### Induced

<details>
```yaml
name: RightsViolated
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RightsViolated
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'The infringement or breach of rights in a manner that constitutes a

  ''violation'' of those rights'
comments:
- 'This concept was called "ViolationOfRights" in DPV 2.0. Though specified

  as a plural i.e. ''rights'', this concept can be applied to a singular

  right'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Rights Violated
exact_mappings:
- dpv_risk:RightsViolated
- dpv_risk_owl:RightsViolated
is_a: RightsImpact
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:RightsViolated

```
</details></div>