---
search:
  boost: 10.0
---

# Class: QualityRisk 


_Concept representing risks and issues associated with quality of tasks,_

_resources, processes_



<div data-search-exclude markdown="1">



URI: [risk:QualityRisk](https://w3id.org/lmodel/dpv/risk/QualityRisk)





```mermaid
 classDiagram
    class QualityRisk
    click QualityRisk href "../QualityRisk/"
      PotentialConsequence <|-- QualityRisk
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- QualityRisk
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- QualityRisk
        click PotentialRiskSource href "../PotentialRiskSource/"
      OperationalSecurityRisk <|-- QualityRisk
        click OperationalSecurityRisk href "../OperationalSecurityRisk/"
      

      QualityRisk <|-- AccuracyRisk
        click AccuracyRisk href "../AccuracyRisk/"
      QualityRisk <|-- QualityDegraded
        click QualityDegraded href "../QualityDegraded/"
      QualityRisk <|-- QualityInconsistent
        click QualityInconsistent href "../QualityInconsistent/"
      QualityRisk <|-- QualityInsufficient
        click QualityInsufficient href "../QualityInsufficient/"
      QualityRisk <|-- QualityUnknown
        click QualityUnknown href "../QualityUnknown/"
      QualityRisk <|-- QualityUnverified
        click QualityUnverified href "../QualityUnverified/"
      QualityRisk <|-- ResilienceRisk
        click ResilienceRisk href "../ResilienceRisk/"
      QualityRisk <|-- RobustnessRisk
        click RobustnessRisk href "../RobustnessRisk/"
      QualityRisk <|-- SecurityQualityRisk
        click SecurityQualityRisk href "../SecurityQualityRisk/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **QualityRisk** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [AccuracyRisk](AccuracyRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [QualityDegraded](QualityDegraded.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [QualityInconsistent](QualityInconsistent.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [QualityInsufficient](QualityInsufficient.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [QualityUnknown](QualityUnknown.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [QualityUnverified](QualityUnverified.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [ResilienceRisk](ResilienceRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [RobustnessRisk](RobustnessRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [SecurityQualityRisk](SecurityQualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:QualityRisk](https://w3id.org/lmodel/dpv/risk/QualityRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Quality Risk




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#QualityRisk |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:QualityRisk |
| native | risk:QualityRisk |
| exact | dpv_risk:QualityRisk, dpv_risk_owl:QualityRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: QualityRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#QualityRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing risks and issues associated with quality of tasks,

  resources, processes'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Quality Risk
exact_mappings:
- dpv_risk:QualityRisk
- dpv_risk_owl:QualityRisk
is_a: OperationalSecurityRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:QualityRisk

```
</details>

### Induced

<details>
```yaml
name: QualityRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#QualityRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing risks and issues associated with quality of tasks,

  resources, processes'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Quality Risk
exact_mappings:
- dpv_risk:QualityRisk
- dpv_risk_owl:QualityRisk
is_a: OperationalSecurityRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:QualityRisk

```
</details></div>