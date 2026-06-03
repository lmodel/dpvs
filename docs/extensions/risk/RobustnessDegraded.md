---
search:
  boost: 10.0
---

# Class: RobustnessDegraded 


_Concepts representing risks and issues where Robustness is Degraded_



<div data-search-exclude markdown="1">



URI: [risk:RobustnessDegraded](https://w3id.org/lmodel/dpv/risk/RobustnessDegraded)





```mermaid
 classDiagram
    class RobustnessDegraded
    click RobustnessDegraded href "../RobustnessDegraded/"
      PotentialConsequence <|-- RobustnessDegraded
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- RobustnessDegraded
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- RobustnessDegraded
        click PotentialRiskSource href "../PotentialRiskSource/"
      RobustnessRisk <|-- RobustnessDegraded
        click RobustnessRisk href "../RobustnessRisk/"
      QualityDegraded <|-- RobustnessDegraded
        click QualityDegraded href "../QualityDegraded/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [QualityDegraded](QualityDegraded.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **RobustnessDegraded** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [RobustnessRisk](RobustnessRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RobustnessDegraded](https://w3id.org/lmodel/dpv/risk/RobustnessDegraded) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Robustness Degraded




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RobustnessDegraded |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RobustnessDegraded |
| native | risk:RobustnessDegraded |
| exact | dpv_risk:RobustnessDegraded, dpv_risk_owl:RobustnessDegraded |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RobustnessDegraded
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RobustnessDegraded
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Robustness is Degraded
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Robustness Degraded
exact_mappings:
- dpv_risk:RobustnessDegraded
- dpv_risk_owl:RobustnessDegraded
is_a: QualityDegraded
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- RobustnessRisk
class_uri: risk:RobustnessDegraded

```
</details>

### Induced

<details>
```yaml
name: RobustnessDegraded
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RobustnessDegraded
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Robustness is Degraded
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Robustness Degraded
exact_mappings:
- dpv_risk:RobustnessDegraded
- dpv_risk_owl:RobustnessDegraded
is_a: QualityDegraded
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- RobustnessRisk
class_uri: risk:RobustnessDegraded

```
</details></div>