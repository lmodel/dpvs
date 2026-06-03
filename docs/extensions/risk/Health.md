---
search:
  boost: 10.0
---

# Class: Health 


_Concept representing health of individual(s), or group(s), or society at_

_large_



<div data-search-exclude markdown="1">



URI: [risk:Health](https://w3id.org/lmodel/dpv/risk/Health)





```mermaid
 classDiagram
    class Health
    click Health href "../Health/"
      PotentialConsequence <|-- Health
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Health
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Health
        click PotentialRisk href "../PotentialRisk/"
      HealthSafety <|-- Health
        click HealthSafety href "../HealthSafety/"
      

      Health <|-- MentalHealth
        click MentalHealth href "../MentalHealth/"
      Health <|-- PhysicalHealth
        click PhysicalHealth href "../PhysicalHealth/"
      

      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [HealthSafety](HealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * **Health** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
                * [MentalHealth](MentalHealth.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
                * [PhysicalHealth](PhysicalHealth.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Health](https://w3id.org/lmodel/dpv/risk/Health) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Health




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Health |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Health |
| native | risk:Health |
| exact | dpv_risk:Health, dpv_risk_owl:Health |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Health
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Health
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing health of individual(s), or group(s), or society
  at

  large'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Health
exact_mappings:
- dpv_risk:Health
- dpv_risk_owl:Health
is_a: HealthSafety
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Health

```
</details>

### Induced

<details>
```yaml
name: Health
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Health
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing health of individual(s), or group(s), or society
  at

  large'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Health
exact_mappings:
- dpv_risk:Health
- dpv_risk_owl:Health
is_a: HealthSafety
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Health

```
</details></div>