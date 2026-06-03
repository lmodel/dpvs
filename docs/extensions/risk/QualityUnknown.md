---
search:
  boost: 10.0
---

# Class: QualityUnknown 


_Concepts representing risks and issues where Quality is Unknown_



<div data-search-exclude markdown="1">



URI: [risk:QualityUnknown](https://w3id.org/lmodel/dpv/risk/QualityUnknown)





```mermaid
 classDiagram
    class QualityUnknown
    click QualityUnknown href "../QualityUnknown/"
      PotentialConsequence <|-- QualityUnknown
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- QualityUnknown
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- QualityUnknown
        click PotentialRiskSource href "../PotentialRiskSource/"
      QualityRisk <|-- QualityUnknown
        click QualityRisk href "../QualityRisk/"
      

      QualityUnknown <|-- AccuracyUnknown
        click AccuracyUnknown href "../AccuracyUnknown/"
      QualityUnknown <|-- ResilienceUnknown
        click ResilienceUnknown href "../ResilienceUnknown/"
      QualityUnknown <|-- RobustnessUnknown
        click RobustnessUnknown href "../RobustnessUnknown/"
      QualityUnknown <|-- SecurityQualityUnknown
        click SecurityQualityUnknown href "../SecurityQualityUnknown/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **QualityUnknown** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * [ResilienceUnknown](ResilienceUnknown.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [ResilienceRisk](ResilienceRisk.md)]
                * [RobustnessUnknown](RobustnessUnknown.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [RobustnessRisk](RobustnessRisk.md)]
                * [SecurityQualityUnknown](SecurityQualityUnknown.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [SecurityQualityRisk](SecurityQualityRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:QualityUnknown](https://w3id.org/lmodel/dpv/risk/QualityUnknown) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Quality Unknown




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#QualityUnknown |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:QualityUnknown |
| native | risk:QualityUnknown |
| exact | dpv_risk:QualityUnknown, dpv_risk_owl:QualityUnknown |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: QualityUnknown
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#QualityUnknown
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Quality is Unknown
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Quality Unknown
exact_mappings:
- dpv_risk:QualityUnknown
- dpv_risk_owl:QualityUnknown
is_a: QualityRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:QualityUnknown

```
</details>

### Induced

<details>
```yaml
name: QualityUnknown
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#QualityUnknown
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Quality is Unknown
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Quality Unknown
exact_mappings:
- dpv_risk:QualityUnknown
- dpv_risk_owl:QualityUnknown
is_a: QualityRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:QualityUnknown

```
</details></div>