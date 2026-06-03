---
search:
  boost: 10.0
---

# Class: IndividualRisk 


_Risks and issues that affect or have the potential to affect specific_

_individuals_



<div data-search-exclude markdown="1">



URI: [risk:IndividualRisk](https://w3id.org/lmodel/dpv/risk/IndividualRisk)





```mermaid
 classDiagram
    class IndividualRisk
    click IndividualRisk href "../IndividualRisk/"
      PotentialConsequence <|-- IndividualRisk
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- IndividualRisk
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- IndividualRisk
        click PotentialRisk href "../PotentialRisk/"
      SocietalRiskConcept <|-- IndividualRisk
        click SocietalRiskConcept href "../SocietalRiskConcept/"
      

      IndividualRisk <|-- BehaviourDistortion
        click BehaviourDistortion href "../BehaviourDistortion/"
      IndividualRisk <|-- ExposureToHarmfulSpeech
        click ExposureToHarmfulSpeech href "../ExposureToHarmfulSpeech/"
      IndividualRisk <|-- Harm
        click Harm href "../Harm/"
      IndividualRisk <|-- HealthSafety
        click HealthSafety href "../HealthSafety/"
      IndividualRisk <|-- ImpairedDecisionMaking
        click ImpairedDecisionMaking href "../ImpairedDecisionMaking/"
      IndividualRisk <|-- IndividualHealthSafety
        click IndividualHealthSafety href "../IndividualHealthSafety/"
      IndividualRisk <|-- PersonalSafetyEndangerment
        click PersonalSafetyEndangerment href "../PersonalSafetyEndangerment/"
      IndividualRisk <|-- Privacy
        click Privacy href "../Privacy/"
      

      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * **IndividualRisk** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [BehaviourDistortion](BehaviourDistortion.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [ExposureToHarmfulSpeech](ExposureToHarmfulSpeech.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [MentalHealth](MentalHealth.md) [Wellbeing](Wellbeing.md)]
        * [HealthSafety](HealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [ImpairedDecisionMaking](ImpairedDecisionMaking.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [PersonalSafetyEndangerment](PersonalSafetyEndangerment.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [Privacy](Privacy.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IndividualRisk](https://w3id.org/lmodel/dpv/risk/IndividualRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Individual Risk




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IndividualRisk |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IndividualRisk |
| native | risk:IndividualRisk |
| exact | dpv_risk:IndividualRisk, dpv_risk_owl:IndividualRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IndividualRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IndividualRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Risks and issues that affect or have the potential to affect specific

  individuals'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Individual Risk
exact_mappings:
- dpv_risk:IndividualRisk
- dpv_risk_owl:IndividualRisk
is_a: SocietalRiskConcept
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:IndividualRisk

```
</details>

### Induced

<details>
```yaml
name: IndividualRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IndividualRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Risks and issues that affect or have the potential to affect specific

  individuals'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Individual Risk
exact_mappings:
- dpv_risk:IndividualRisk
- dpv_risk_owl:IndividualRisk
is_a: SocietalRiskConcept
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:IndividualRisk

```
</details></div>