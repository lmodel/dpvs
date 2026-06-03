---
search:
  boost: 10.0
---

# Class: MentalHealth 


_Concept representing mental health of individual(s), or group(s), or_

_society at large_



<div data-search-exclude markdown="1">



URI: [risk:MentalHealth](https://w3id.org/lmodel/dpv/risk/MentalHealth)





```mermaid
 classDiagram
    class MentalHealth
    click MentalHealth href "../MentalHealth/"
      PotentialConsequence <|-- MentalHealth
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- MentalHealth
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- MentalHealth
        click PotentialRisk href "../PotentialRisk/"
      Health <|-- MentalHealth
        click Health href "../Health/"
      

      MentalHealth <|-- ExposureToHarmfulSpeech
        click ExposureToHarmfulSpeech href "../ExposureToHarmfulSpeech/"
      

      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [HealthSafety](HealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Health](Health.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
                * **MentalHealth** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:MentalHealth](https://w3id.org/lmodel/dpv/risk/MentalHealth) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Mental Health




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#MentalHealth |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:MentalHealth |
| native | risk:MentalHealth |
| exact | dpv_risk:MentalHealth, dpv_risk_owl:MentalHealth |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MentalHealth
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#MentalHealth
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing mental health of individual(s), or group(s), or

  society at large'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Mental Health
exact_mappings:
- dpv_risk:MentalHealth
- dpv_risk_owl:MentalHealth
is_a: Health
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:MentalHealth

```
</details>

### Induced

<details>
```yaml
name: MentalHealth
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#MentalHealth
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing mental health of individual(s), or group(s), or

  society at large'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Mental Health
exact_mappings:
- dpv_risk:MentalHealth
- dpv_risk_owl:MentalHealth
is_a: Health
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:MentalHealth

```
</details></div>