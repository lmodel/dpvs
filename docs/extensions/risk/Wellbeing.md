---
search:
  boost: 10.0
---

# Class: Wellbeing 


_Concept representing wellbeing of individual(s)_



<div data-search-exclude markdown="1">



URI: [risk:Wellbeing](https://w3id.org/lmodel/dpv/risk/Wellbeing)





```mermaid
 classDiagram
    class Wellbeing
    click Wellbeing href "../Wellbeing/"
      PotentialConsequence <|-- Wellbeing
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Wellbeing
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Wellbeing
        click PotentialRisk href "../PotentialRisk/"
      HealthSafety <|-- Wellbeing
        click HealthSafety href "../HealthSafety/"
      

      Wellbeing <|-- ExposureToHarmfulSpeech
        click ExposureToHarmfulSpeech href "../ExposureToHarmfulSpeech/"
      Wellbeing <|-- Harassment
        click Harassment href "../Harassment/"
      Wellbeing <|-- PsychologicalHarm
        click PsychologicalHarm href "../PsychologicalHarm/"
      

      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [HealthSafety](HealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * **Wellbeing** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Wellbeing](https://w3id.org/lmodel/dpv/risk/Wellbeing) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Wellbeing




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Wellbeing |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Wellbeing |
| native | risk:Wellbeing |
| exact | dpv_risk:Wellbeing, dpv_risk_owl:Wellbeing |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Wellbeing
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Wellbeing
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing wellbeing of individual(s)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Wellbeing
exact_mappings:
- dpv_risk:Wellbeing
- dpv_risk_owl:Wellbeing
is_a: HealthSafety
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Wellbeing

```
</details>

### Induced

<details>
```yaml
name: Wellbeing
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Wellbeing
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing wellbeing of individual(s)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Wellbeing
exact_mappings:
- dpv_risk:Wellbeing
- dpv_risk_owl:Wellbeing
is_a: HealthSafety
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Wellbeing

```
</details></div>