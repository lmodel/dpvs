---
search:
  boost: 10.0
---

# Class: MentalSafety 


_Concept representing mental safety of individual(s), or group(s), or_

_society at large_



<div data-search-exclude markdown="1">



URI: [risk:MentalSafety](https://w3id.org/lmodel/dpv/risk/MentalSafety)





```mermaid
 classDiagram
    class MentalSafety
    click MentalSafety href "../MentalSafety/"
      PotentialConsequence <|-- MentalSafety
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- MentalSafety
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- MentalSafety
        click PotentialRisk href "../PotentialRisk/"
      Safety <|-- MentalSafety
        click Safety href "../Safety/"
      

      MentalSafety <|-- PsychologicalHarm
        click PsychologicalHarm href "../PsychologicalHarm/"
      MentalSafety <|-- SexualViolence
        click SexualViolence href "../SexualViolence/"
      

      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [HealthSafety](HealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Safety](Safety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
                * **MentalSafety** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:MentalSafety](https://w3id.org/lmodel/dpv/risk/MentalSafety) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Mental Safety




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#MentalSafety |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:MentalSafety |
| native | risk:MentalSafety |
| exact | dpv_risk:MentalSafety, dpv_risk_owl:MentalSafety |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MentalSafety
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#MentalSafety
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing mental safety of individual(s), or group(s), or

  society at large'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Mental Safety
exact_mappings:
- dpv_risk:MentalSafety
- dpv_risk_owl:MentalSafety
is_a: Safety
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:MentalSafety

```
</details>

### Induced

<details>
```yaml
name: MentalSafety
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#MentalSafety
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing mental safety of individual(s), or group(s), or

  society at large'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Mental Safety
exact_mappings:
- dpv_risk:MentalSafety
- dpv_risk_owl:MentalSafety
is_a: Safety
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:MentalSafety

```
</details></div>