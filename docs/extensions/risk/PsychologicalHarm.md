---
search:
  boost: 10.0
---

# Class: PsychologicalHarm 


_Concept representing Psychological Harm_



<div data-search-exclude markdown="1">



URI: [risk:PsychologicalHarm](https://w3id.org/lmodel/dpv/risk/PsychologicalHarm)





```mermaid
 classDiagram
    class PsychologicalHarm
    click PsychologicalHarm href "../PsychologicalHarm/"
      PotentialConsequence <|-- PsychologicalHarm
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- PsychologicalHarm
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- PsychologicalHarm
        click PotentialRisk href "../PotentialRisk/"
      MentalSafety <|-- PsychologicalHarm
        click MentalSafety href "../MentalSafety/"
      Wellbeing <|-- PsychologicalHarm
        click Wellbeing href "../Wellbeing/"
      Harm <|-- PsychologicalHarm
        click Harm href "../Harm/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [HealthSafety](HealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Harm](Harm.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [IndividualRisk](IndividualRisk.md)]
                * **PsychologicalHarm** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [MentalSafety](MentalSafety.md) [Wellbeing](Wellbeing.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:PsychologicalHarm](https://w3id.org/lmodel/dpv/risk/PsychologicalHarm) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Psychological Harm




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#PsychologicalHarm |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:PsychologicalHarm |
| native | risk:PsychologicalHarm |
| exact | dpv_risk:PsychologicalHarm, dpv_risk_owl:PsychologicalHarm |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PsychologicalHarm
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PsychologicalHarm
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Psychological Harm
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Psychological Harm
exact_mappings:
- dpv_risk:PsychologicalHarm
- dpv_risk_owl:PsychologicalHarm
is_a: Harm
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- MentalSafety
- Wellbeing
class_uri: risk:PsychologicalHarm

```
</details>

### Induced

<details>
```yaml
name: PsychologicalHarm
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PsychologicalHarm
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Psychological Harm
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Psychological Harm
exact_mappings:
- dpv_risk:PsychologicalHarm
- dpv_risk_owl:PsychologicalHarm
is_a: Harm
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- MentalSafety
- Wellbeing
class_uri: risk:PsychologicalHarm

```
</details></div>