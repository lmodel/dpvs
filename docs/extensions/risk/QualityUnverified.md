---
search:
  boost: 10.0
---

# Class: QualityUnverified 


_Concepts representing risks and issues where Quality is Unverified_



<div data-search-exclude markdown="1">



URI: [risk:QualityUnverified](https://w3id.org/lmodel/dpv/risk/QualityUnverified)





```mermaid
 classDiagram
    class QualityUnverified
    click QualityUnverified href "../QualityUnverified/"
      PotentialConsequence <|-- QualityUnverified
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- QualityUnverified
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- QualityUnverified
        click PotentialRiskSource href "../PotentialRiskSource/"
      QualityRisk <|-- QualityUnverified
        click QualityRisk href "../QualityRisk/"
      

      QualityUnverified <|-- AccuracyUnverified
        click AccuracyUnverified href "../AccuracyUnverified/"
      QualityUnverified <|-- ResilienceUnverified
        click ResilienceUnverified href "../ResilienceUnverified/"
      QualityUnverified <|-- RobustnessUnverified
        click RobustnessUnverified href "../RobustnessUnverified/"
      QualityUnverified <|-- SecurityQualityUnverified
        click SecurityQualityUnverified href "../SecurityQualityUnverified/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **QualityUnverified** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * [ResilienceUnverified](ResilienceUnverified.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [ResilienceRisk](ResilienceRisk.md)]
                * [RobustnessUnverified](RobustnessUnverified.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [RobustnessRisk](RobustnessRisk.md)]
                * [SecurityQualityUnverified](SecurityQualityUnverified.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [SecurityQualityRisk](SecurityQualityRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:QualityUnverified](https://w3id.org/lmodel/dpv/risk/QualityUnverified) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Quality Unverified




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#QualityUnverified |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:QualityUnverified |
| native | risk:QualityUnverified |
| exact | dpv_risk:QualityUnverified, dpv_risk_owl:QualityUnverified |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: QualityUnverified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#QualityUnverified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Quality is Unverified
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Quality Unverified
exact_mappings:
- dpv_risk:QualityUnverified
- dpv_risk_owl:QualityUnverified
is_a: QualityRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:QualityUnverified

```
</details>

### Induced

<details>
```yaml
name: QualityUnverified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#QualityUnverified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Quality is Unverified
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Quality Unverified
exact_mappings:
- dpv_risk:QualityUnverified
- dpv_risk_owl:QualityUnverified
is_a: QualityRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:QualityUnverified

```
</details></div>