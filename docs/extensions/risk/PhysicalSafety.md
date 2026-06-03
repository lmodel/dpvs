---
search:
  boost: 10.0
---

# Class: PhysicalSafety 


_Concept representing physical safety of individual(s), or group(s), or_

_society at large_



<div data-search-exclude markdown="1">



URI: [risk:PhysicalSafety](https://w3id.org/lmodel/dpv/risk/PhysicalSafety)





```mermaid
 classDiagram
    class PhysicalSafety
    click PhysicalSafety href "../PhysicalSafety/"
      PotentialConsequence <|-- PhysicalSafety
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- PhysicalSafety
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- PhysicalSafety
        click PotentialRisk href "../PotentialRisk/"
      Safety <|-- PhysicalSafety
        click Safety href "../Safety/"
      

      PhysicalSafety <|-- Injury
        click Injury href "../Injury/"
      PhysicalSafety <|-- PhysicalAssault
        click PhysicalAssault href "../PhysicalAssault/"
      PhysicalSafety <|-- SexualViolence
        click SexualViolence href "../SexualViolence/"
      

      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [HealthSafety](HealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Safety](Safety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
                * **PhysicalSafety** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:PhysicalSafety](https://w3id.org/lmodel/dpv/risk/PhysicalSafety) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Physical Safety




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#PhysicalSafety |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:PhysicalSafety |
| native | risk:PhysicalSafety |
| exact | dpv_risk:PhysicalSafety, dpv_risk_owl:PhysicalSafety |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PhysicalSafety
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PhysicalSafety
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing physical safety of individual(s), or group(s),
  or

  society at large'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Physical Safety
exact_mappings:
- dpv_risk:PhysicalSafety
- dpv_risk_owl:PhysicalSafety
is_a: Safety
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:PhysicalSafety

```
</details>

### Induced

<details>
```yaml
name: PhysicalSafety
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PhysicalSafety
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing physical safety of individual(s), or group(s),
  or

  society at large'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Physical Safety
exact_mappings:
- dpv_risk:PhysicalSafety
- dpv_risk_owl:PhysicalSafety
is_a: Safety
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:PhysicalSafety

```
</details></div>