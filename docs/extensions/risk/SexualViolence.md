---
search:
  boost: 10.0
---

# Class: SexualViolence 


_Concept representing Sexual Violence_



<div data-search-exclude markdown="1">



URI: [risk:SexualViolence](https://w3id.org/lmodel/dpv/risk/SexualViolence)





```mermaid
 classDiagram
    class SexualViolence
    click SexualViolence href "../SexualViolence/"
      PotentialConsequence <|-- SexualViolence
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- SexualViolence
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- SexualViolence
        click PotentialRisk href "../PotentialRisk/"
      MentalSafety <|-- SexualViolence
        click MentalSafety href "../MentalSafety/"
      PhysicalSafety <|-- SexualViolence
        click PhysicalSafety href "../PhysicalSafety/"
      Harm <|-- SexualViolence
        click Harm href "../Harm/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [HealthSafety](HealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Harm](Harm.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [IndividualRisk](IndividualRisk.md)]
                * **SexualViolence** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [MentalSafety](MentalSafety.md) [PhysicalSafety](PhysicalSafety.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:SexualViolence](https://w3id.org/lmodel/dpv/risk/SexualViolence) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Sexual Violence




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#SexualViolence |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:SexualViolence |
| native | risk:SexualViolence |
| exact | dpv_risk:SexualViolence, dpv_risk_owl:SexualViolence |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SexualViolence
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SexualViolence
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Sexual Violence
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Sexual Violence
exact_mappings:
- dpv_risk:SexualViolence
- dpv_risk_owl:SexualViolence
is_a: Harm
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- MentalSafety
- PhysicalSafety
class_uri: risk:SexualViolence

```
</details>

### Induced

<details>
```yaml
name: SexualViolence
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SexualViolence
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Sexual Violence
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Sexual Violence
exact_mappings:
- dpv_risk:SexualViolence
- dpv_risk_owl:SexualViolence
is_a: Harm
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- MentalSafety
- PhysicalSafety
class_uri: risk:SexualViolence

```
</details></div>