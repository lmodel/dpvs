---
search:
  boost: 10.0
---

# Class: Harm 


_Concept representing Harm to humans_



<div data-search-exclude markdown="1">



URI: [risk:Harm](https://w3id.org/lmodel/dpv/risk/Harm)





```mermaid
 classDiagram
    class Harm
    click Harm href "../Harm/"
      PotentialConsequence <|-- Harm
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Harm
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Harm
        click PotentialRisk href "../PotentialRisk/"
      IndividualRisk <|-- Harm
        click IndividualRisk href "../IndividualRisk/"
      HealthSafety <|-- Harm
        click HealthSafety href "../HealthSafety/"
      

      Harm <|-- Harassment
        click Harassment href "../Harassment/"
      Harm <|-- Injury
        click Injury href "../Injury/"
      Harm <|-- PhysicalAssault
        click PhysicalAssault href "../PhysicalAssault/"
      Harm <|-- PhysicalHarm
        click PhysicalHarm href "../PhysicalHarm/"
      Harm <|-- PsychologicalHarm
        click PsychologicalHarm href "../PsychologicalHarm/"
      Harm <|-- SexualViolence
        click SexualViolence href "../SexualViolence/"
      Harm <|-- ViolenceAgainstChildren
        click ViolenceAgainstChildren href "../ViolenceAgainstChildren/"
      

      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [HealthSafety](HealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * **Harm** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [IndividualRisk](IndividualRisk.md)]
                * [Harassment](Harassment.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [Wellbeing](Wellbeing.md)]
                * [Injury](Injury.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PhysicalSafety](PhysicalSafety.md)]
                * [PhysicalAssault](PhysicalAssault.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PhysicalSafety](PhysicalSafety.md)]
                * [PhysicalHarm](PhysicalHarm.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PhysicalHealth](PhysicalHealth.md)]
                * [PsychologicalHarm](PsychologicalHarm.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [MentalSafety](MentalSafety.md) [Wellbeing](Wellbeing.md)]
                * [SexualViolence](SexualViolence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [MentalSafety](MentalSafety.md) [PhysicalSafety](PhysicalSafety.md)]
                * [ViolenceAgainstChildren](ViolenceAgainstChildren.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Harm](https://w3id.org/lmodel/dpv/risk/Harm) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Harm


## Comments

* This concept refers to the general abstract notion of harm



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Harm |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Harm |
| native | risk:Harm |
| exact | dpv_risk:Harm, dpv_risk_owl:Harm |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Harm
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Harm
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Harm to humans
comments:
- This concept refers to the general abstract notion of harm
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Harm
exact_mappings:
- dpv_risk:Harm
- dpv_risk_owl:Harm
is_a: HealthSafety
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- IndividualRisk
class_uri: risk:Harm

```
</details>

### Induced

<details>
```yaml
name: Harm
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Harm
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Harm to humans
comments:
- This concept refers to the general abstract notion of harm
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Harm
exact_mappings:
- dpv_risk:Harm
- dpv_risk_owl:Harm
is_a: HealthSafety
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- IndividualRisk
class_uri: risk:Harm

```
</details></div>