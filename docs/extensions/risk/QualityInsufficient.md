---
search:
  boost: 10.0
---

# Class: QualityInsufficient 


_Concepts representing risks and issues where Quality is Insufficient_



<div data-search-exclude markdown="1">



URI: [risk:QualityInsufficient](https://w3id.org/lmodel/dpv/risk/QualityInsufficient)





```mermaid
 classDiagram
    class QualityInsufficient
    click QualityInsufficient href "../QualityInsufficient/"
      PotentialConsequence <|-- QualityInsufficient
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- QualityInsufficient
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- QualityInsufficient
        click PotentialRiskSource href "../PotentialRiskSource/"
      QualityRisk <|-- QualityInsufficient
        click QualityRisk href "../QualityRisk/"
      

      QualityInsufficient <|-- AccuracyInsufficient
        click AccuracyInsufficient href "../AccuracyInsufficient/"
      QualityInsufficient <|-- ResilienceInsufficient
        click ResilienceInsufficient href "../ResilienceInsufficient/"
      QualityInsufficient <|-- RobustnessInsufficient
        click RobustnessInsufficient href "../RobustnessInsufficient/"
      QualityInsufficient <|-- SecurityQualityInsufficient
        click SecurityQualityInsufficient href "../SecurityQualityInsufficient/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **QualityInsufficient** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * [ResilienceInsufficient](ResilienceInsufficient.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [ResilienceRisk](ResilienceRisk.md)]
                * [RobustnessInsufficient](RobustnessInsufficient.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [RobustnessRisk](RobustnessRisk.md)]
                * [SecurityQualityInsufficient](SecurityQualityInsufficient.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [SecurityQualityRisk](SecurityQualityRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:QualityInsufficient](https://w3id.org/lmodel/dpv/risk/QualityInsufficient) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Quality Insufficient




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#QualityInsufficient |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:QualityInsufficient |
| native | risk:QualityInsufficient |
| exact | dpv_risk:QualityInsufficient, dpv_risk_owl:QualityInsufficient |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: QualityInsufficient
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#QualityInsufficient
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Quality is Insufficient
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Quality Insufficient
exact_mappings:
- dpv_risk:QualityInsufficient
- dpv_risk_owl:QualityInsufficient
is_a: QualityRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:QualityInsufficient

```
</details>

### Induced

<details>
```yaml
name: QualityInsufficient
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#QualityInsufficient
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Quality is Insufficient
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Quality Insufficient
exact_mappings:
- dpv_risk:QualityInsufficient
- dpv_risk_owl:QualityInsufficient
is_a: QualityRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:QualityInsufficient

```
</details></div>