---
search:
  boost: 10.0
---

# Class: QualityInconsistent 


_Concepts representing risks and issues where Quality is Inconsistent_



<div data-search-exclude markdown="1">



URI: [risk:QualityInconsistent](https://w3id.org/lmodel/dpv/risk/QualityInconsistent)





```mermaid
 classDiagram
    class QualityInconsistent
    click QualityInconsistent href "../QualityInconsistent/"
      PotentialConsequence <|-- QualityInconsistent
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- QualityInconsistent
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- QualityInconsistent
        click PotentialRiskSource href "../PotentialRiskSource/"
      QualityRisk <|-- QualityInconsistent
        click QualityRisk href "../QualityRisk/"
      

      QualityInconsistent <|-- AccuracyInconsistent
        click AccuracyInconsistent href "../AccuracyInconsistent/"
      QualityInconsistent <|-- ResilienceInconsistent
        click ResilienceInconsistent href "../ResilienceInconsistent/"
      QualityInconsistent <|-- RobustnessInconsistent
        click RobustnessInconsistent href "../RobustnessInconsistent/"
      QualityInconsistent <|-- SecurityQualityInconsistent
        click SecurityQualityInconsistent href "../SecurityQualityInconsistent/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **QualityInconsistent** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * [ResilienceInconsistent](ResilienceInconsistent.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [ResilienceRisk](ResilienceRisk.md)]
                * [RobustnessInconsistent](RobustnessInconsistent.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [RobustnessRisk](RobustnessRisk.md)]
                * [SecurityQualityInconsistent](SecurityQualityInconsistent.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [SecurityQualityRisk](SecurityQualityRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:QualityInconsistent](https://w3id.org/lmodel/dpv/risk/QualityInconsistent) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Quality Inconsistent




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#QualityInconsistent |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:QualityInconsistent |
| native | risk:QualityInconsistent |
| exact | dpv_risk:QualityInconsistent, dpv_risk_owl:QualityInconsistent |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: QualityInconsistent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#QualityInconsistent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Quality is Inconsistent
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Quality Inconsistent
exact_mappings:
- dpv_risk:QualityInconsistent
- dpv_risk_owl:QualityInconsistent
is_a: QualityRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:QualityInconsistent

```
</details>

### Induced

<details>
```yaml
name: QualityInconsistent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#QualityInconsistent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Quality is Inconsistent
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Quality Inconsistent
exact_mappings:
- dpv_risk:QualityInconsistent
- dpv_risk_owl:QualityInconsistent
is_a: QualityRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:QualityInconsistent

```
</details></div>