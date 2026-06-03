---
search:
  boost: 10.0
---

# Class: RobustnessRisk 


_Concepts representing risks and issues where Robustness is Risk_



<div data-search-exclude markdown="1">



URI: [risk:RobustnessRisk](https://w3id.org/lmodel/dpv/risk/RobustnessRisk)





```mermaid
 classDiagram
    class RobustnessRisk
    click RobustnessRisk href "../RobustnessRisk/"
      PotentialConsequence <|-- RobustnessRisk
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- RobustnessRisk
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- RobustnessRisk
        click PotentialRiskSource href "../PotentialRiskSource/"
      QualityRisk <|-- RobustnessRisk
        click QualityRisk href "../QualityRisk/"
      

      RobustnessRisk <|-- RobustnessDegraded
        click RobustnessDegraded href "../RobustnessDegraded/"
      RobustnessRisk <|-- RobustnessInconsistent
        click RobustnessInconsistent href "../RobustnessInconsistent/"
      RobustnessRisk <|-- RobustnessInsufficient
        click RobustnessInsufficient href "../RobustnessInsufficient/"
      RobustnessRisk <|-- RobustnessUnknown
        click RobustnessUnknown href "../RobustnessUnknown/"
      RobustnessRisk <|-- RobustnessUnverified
        click RobustnessUnverified href "../RobustnessUnverified/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **RobustnessRisk** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RobustnessRisk](https://w3id.org/lmodel/dpv/risk/RobustnessRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Robustness Risk




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RobustnessRisk |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RobustnessRisk |
| native | risk:RobustnessRisk |
| exact | dpv_risk:RobustnessRisk, dpv_risk_owl:RobustnessRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RobustnessRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RobustnessRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Robustness is Risk
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Robustness Risk
exact_mappings:
- dpv_risk:RobustnessRisk
- dpv_risk_owl:RobustnessRisk
is_a: QualityRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:RobustnessRisk

```
</details>

### Induced

<details>
```yaml
name: RobustnessRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RobustnessRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Robustness is Risk
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Robustness Risk
exact_mappings:
- dpv_risk:RobustnessRisk
- dpv_risk_owl:RobustnessRisk
is_a: QualityRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:RobustnessRisk

```
</details></div>