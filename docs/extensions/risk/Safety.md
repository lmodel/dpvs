---
search:
  boost: 10.0
---

# Class: Safety 


_Concept representing safety of individual(s), or group(s), or society at_

_large_



<div data-search-exclude markdown="1">



URI: [risk:Safety](https://w3id.org/lmodel/dpv/risk/Safety)





```mermaid
 classDiagram
    class Safety
    click Safety href "../Safety/"
      PotentialConsequence <|-- Safety
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Safety
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Safety
        click PotentialRisk href "../PotentialRisk/"
      HealthSafety <|-- Safety
        click HealthSafety href "../HealthSafety/"
      

      Safety <|-- MentalSafety
        click MentalSafety href "../MentalSafety/"
      Safety <|-- PhysicalSafety
        click PhysicalSafety href "../PhysicalSafety/"
      

      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [HealthSafety](HealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * **Safety** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
                * [MentalSafety](MentalSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
                * [PhysicalSafety](PhysicalSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Safety](https://w3id.org/lmodel/dpv/risk/Safety) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Safety




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Safety |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Safety |
| native | risk:Safety |
| exact | dpv_risk:Safety, dpv_risk_owl:Safety |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Safety
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Safety
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing safety of individual(s), or group(s), or society
  at

  large'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Safety
exact_mappings:
- dpv_risk:Safety
- dpv_risk_owl:Safety
is_a: HealthSafety
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Safety

```
</details>

### Induced

<details>
```yaml
name: Safety
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Safety
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing safety of individual(s), or group(s), or society
  at

  large'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Safety
exact_mappings:
- dpv_risk:Safety
- dpv_risk_owl:Safety
is_a: HealthSafety
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Safety

```
</details></div>