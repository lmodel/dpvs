---
search:
  boost: 10.0
---

# Class: RightsImpact 


_Concept representing Impact to Rights_



<div data-search-exclude markdown="1">



URI: [risk:RightsImpact](https://w3id.org/lmodel/dpv/risk/RightsImpact)





```mermaid
 classDiagram
    class RightsImpact
    click RightsImpact href "../RightsImpact/"
      PotentialConsequence <|-- RightsImpact
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- RightsImpact
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- RightsImpact
        click PotentialRisk href "../PotentialRisk/"
      SocietalRiskConcept <|-- RightsImpact
        click SocietalRiskConcept href "../SocietalRiskConcept/"
      

      RightsImpact <|-- RightsDenied
        click RightsDenied href "../RightsDenied/"
      RightsImpact <|-- RightsEroded
        click RightsEroded href "../RightsEroded/"
      RightsImpact <|-- RightsExercisePrevented
        click RightsExercisePrevented href "../RightsExercisePrevented/"
      RightsImpact <|-- RightsLimited
        click RightsLimited href "../RightsLimited/"
      RightsImpact <|-- RightsObstructed
        click RightsObstructed href "../RightsObstructed/"
      RightsImpact <|-- RightsUnfulfilled
        click RightsUnfulfilled href "../RightsUnfulfilled/"
      RightsImpact <|-- RightsViolated
        click RightsViolated href "../RightsViolated/"
      

      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * **RightsImpact** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [RightsDenied](RightsDenied.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [RightsEroded](RightsEroded.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [RightsExercisePrevented](RightsExercisePrevented.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [RightsLimited](RightsLimited.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [RightsObstructed](RightsObstructed.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [RightsUnfulfilled](RightsUnfulfilled.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [RightsViolated](RightsViolated.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RightsImpact](https://w3id.org/lmodel/dpv/risk/RightsImpact) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Rights Impact


## Comments

* This concept was called "ImpactToRights" in DPV 2.0. Though specified as
a plural i.e. 'rights', this concept can be applied to a singular right



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RightsImpact |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RightsImpact |
| native | risk:RightsImpact |
| exact | dpv_risk:RightsImpact, dpv_risk_owl:RightsImpact |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RightsImpact
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RightsImpact
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Impact to Rights
comments:
- 'This concept was called "ImpactToRights" in DPV 2.0. Though specified as

  a plural i.e. ''rights'', this concept can be applied to a singular right'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Rights Impact
exact_mappings:
- dpv_risk:RightsImpact
- dpv_risk_owl:RightsImpact
is_a: SocietalRiskConcept
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:RightsImpact

```
</details>

### Induced

<details>
```yaml
name: RightsImpact
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RightsImpact
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Impact to Rights
comments:
- 'This concept was called "ImpactToRights" in DPV 2.0. Though specified as

  a plural i.e. ''rights'', this concept can be applied to a singular right'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Rights Impact
exact_mappings:
- dpv_risk:RightsImpact
- dpv_risk_owl:RightsImpact
is_a: SocietalRiskConcept
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:RightsImpact

```
</details></div>