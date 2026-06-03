---
search:
  boost: 10.0
---

# Class: QualityDegraded 


_Concepts representing risks and issues where Quality is Degraded_



<div data-search-exclude markdown="1">



URI: [risk:QualityDegraded](https://w3id.org/lmodel/dpv/risk/QualityDegraded)





```mermaid
 classDiagram
    class QualityDegraded
    click QualityDegraded href "../QualityDegraded/"
      PotentialConsequence <|-- QualityDegraded
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- QualityDegraded
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- QualityDegraded
        click PotentialRiskSource href "../PotentialRiskSource/"
      QualityRisk <|-- QualityDegraded
        click QualityRisk href "../QualityRisk/"
      

      QualityDegraded <|-- AccuracyDegraded
        click AccuracyDegraded href "../AccuracyDegraded/"
      QualityDegraded <|-- ResilienceDegraded
        click ResilienceDegraded href "../ResilienceDegraded/"
      QualityDegraded <|-- RobustnessDegraded
        click RobustnessDegraded href "../RobustnessDegraded/"
      QualityDegraded <|-- SecurityQualityDegraded
        click SecurityQualityDegraded href "../SecurityQualityDegraded/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **QualityDegraded** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * [ResilienceDegraded](ResilienceDegraded.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [ResilienceRisk](ResilienceRisk.md)]
                * [RobustnessDegraded](RobustnessDegraded.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [RobustnessRisk](RobustnessRisk.md)]
                * [SecurityQualityDegraded](SecurityQualityDegraded.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [SecurityQualityRisk](SecurityQualityRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:QualityDegraded](https://w3id.org/lmodel/dpv/risk/QualityDegraded) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Quality Degraded




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#QualityDegraded |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:QualityDegraded |
| native | risk:QualityDegraded |
| exact | dpv_risk:QualityDegraded, dpv_risk_owl:QualityDegraded |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: QualityDegraded
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#QualityDegraded
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Quality is Degraded
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Quality Degraded
exact_mappings:
- dpv_risk:QualityDegraded
- dpv_risk_owl:QualityDegraded
is_a: QualityRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:QualityDegraded

```
</details>

### Induced

<details>
```yaml
name: QualityDegraded
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#QualityDegraded
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Quality is Degraded
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Quality Degraded
exact_mappings:
- dpv_risk:QualityDegraded
- dpv_risk_owl:QualityDegraded
is_a: QualityRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:QualityDegraded

```
</details></div>