---
search:
  boost: 10.0
---

# Class: ExposureToHarmfulSpeech 


_Concept representing Harmful Speech_



<div data-search-exclude markdown="1">



URI: [risk:ExposureToHarmfulSpeech](https://w3id.org/lmodel/dpv/risk/ExposureToHarmfulSpeech)





```mermaid
 classDiagram
    class ExposureToHarmfulSpeech
    click ExposureToHarmfulSpeech href "../ExposureToHarmfulSpeech/"
      PotentialConsequence <|-- ExposureToHarmfulSpeech
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- ExposureToHarmfulSpeech
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- ExposureToHarmfulSpeech
        click PotentialRisk href "../PotentialRisk/"
      MentalHealth <|-- ExposureToHarmfulSpeech
        click MentalHealth href "../MentalHealth/"
      Wellbeing <|-- ExposureToHarmfulSpeech
        click Wellbeing href "../Wellbeing/"
      IndividualRisk <|-- ExposureToHarmfulSpeech
        click IndividualRisk href "../IndividualRisk/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **ExposureToHarmfulSpeech** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [MentalHealth](MentalHealth.md) [Wellbeing](Wellbeing.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ExposureToHarmfulSpeech](https://w3id.org/lmodel/dpv/risk/ExposureToHarmfulSpeech) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Exposure to Harmful Speech


## Comments

* This concept was called "HarmfulSpeech" in DPV 2.0



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ExposureToHarmfulSpeech |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ExposureToHarmfulSpeech |
| native | risk:ExposureToHarmfulSpeech |
| exact | dpv_risk:ExposureToHarmfulSpeech, dpv_risk_owl:ExposureToHarmfulSpeech |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExposureToHarmfulSpeech
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ExposureToHarmfulSpeech
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Harmful Speech
comments:
- This concept was called "HarmfulSpeech" in DPV 2.0
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Exposure to Harmful Speech
exact_mappings:
- dpv_risk:ExposureToHarmfulSpeech
- dpv_risk_owl:ExposureToHarmfulSpeech
is_a: IndividualRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- MentalHealth
- Wellbeing
class_uri: risk:ExposureToHarmfulSpeech

```
</details>

### Induced

<details>
```yaml
name: ExposureToHarmfulSpeech
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ExposureToHarmfulSpeech
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Harmful Speech
comments:
- This concept was called "HarmfulSpeech" in DPV 2.0
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Exposure to Harmful Speech
exact_mappings:
- dpv_risk:ExposureToHarmfulSpeech
- dpv_risk_owl:ExposureToHarmfulSpeech
is_a: IndividualRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- MentalHealth
- Wellbeing
class_uri: risk:ExposureToHarmfulSpeech

```
</details></div>