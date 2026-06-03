---
search:
  boost: 10.0
---

# Class: HealthSafety 


_Concept representing health & safety of individual(s), or group(s), or_

_society at large_



<div data-search-exclude markdown="1">



URI: [risk:HealthSafety](https://w3id.org/lmodel/dpv/risk/HealthSafety)





```mermaid
 classDiagram
    class HealthSafety
    click HealthSafety href "../HealthSafety/"
      PotentialConsequence <|-- HealthSafety
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- HealthSafety
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- HealthSafety
        click PotentialRisk href "../PotentialRisk/"
      IndividualRisk <|-- HealthSafety
        click IndividualRisk href "../IndividualRisk/"
      

      HealthSafety <|-- GroupHealthSafety
        click GroupHealthSafety href "../GroupHealthSafety/"
      HealthSafety <|-- Harm
        click Harm href "../Harm/"
      HealthSafety <|-- Health
        click Health href "../Health/"
      HealthSafety <|-- IndividualHealthSafety
        click IndividualHealthSafety href "../IndividualHealthSafety/"
      HealthSafety <|-- PublicHealthSafety
        click PublicHealthSafety href "../PublicHealthSafety/"
      HealthSafety <|-- Safety
        click Safety href "../Safety/"
      HealthSafety <|-- Wellbeing
        click Wellbeing href "../Wellbeing/"
      

      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **HealthSafety** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Harm](Harm.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [IndividualRisk](IndividualRisk.md)]
            * [Health](Health.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [IndividualHealthSafety](IndividualHealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [IndividualRisk](IndividualRisk.md)]
            * [PublicHealthSafety](PublicHealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Safety](Safety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Wellbeing](Wellbeing.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:HealthSafety](https://w3id.org/lmodel/dpv/risk/HealthSafety) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Health & Safety




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#HealthSafety |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:HealthSafety |
| native | risk:HealthSafety |
| exact | dpv_risk:HealthSafety, dpv_risk_owl:HealthSafety |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HealthSafety
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#HealthSafety
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing health & safety of individual(s), or group(s),
  or

  society at large'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Health & Safety
exact_mappings:
- dpv_risk:HealthSafety
- dpv_risk_owl:HealthSafety
is_a: IndividualRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:HealthSafety

```
</details>

### Induced

<details>
```yaml
name: HealthSafety
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#HealthSafety
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing health & safety of individual(s), or group(s),
  or

  society at large'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Health & Safety
exact_mappings:
- dpv_risk:HealthSafety
- dpv_risk_owl:HealthSafety
is_a: IndividualRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:HealthSafety

```
</details></div>