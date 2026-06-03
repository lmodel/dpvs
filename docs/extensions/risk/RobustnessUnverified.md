---
search:
  boost: 10.0
---

# Class: RobustnessUnverified 


_Concepts representing risks and issues where Robustness is Unverified_



<div data-search-exclude markdown="1">



URI: [risk:RobustnessUnverified](https://w3id.org/lmodel/dpv/risk/RobustnessUnverified)





```mermaid
 classDiagram
    class RobustnessUnverified
    click RobustnessUnverified href "../RobustnessUnverified/"
      PotentialConsequence <|-- RobustnessUnverified
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- RobustnessUnverified
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- RobustnessUnverified
        click PotentialRiskSource href "../PotentialRiskSource/"
      RobustnessRisk <|-- RobustnessUnverified
        click RobustnessRisk href "../RobustnessRisk/"
      QualityUnverified <|-- RobustnessUnverified
        click QualityUnverified href "../QualityUnverified/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [QualityUnverified](QualityUnverified.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **RobustnessUnverified** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [RobustnessRisk](RobustnessRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RobustnessUnverified](https://w3id.org/lmodel/dpv/risk/RobustnessUnverified) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Robustness Unverified




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RobustnessUnverified |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RobustnessUnverified |
| native | risk:RobustnessUnverified |
| exact | dpv_risk:RobustnessUnverified, dpv_risk_owl:RobustnessUnverified |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RobustnessUnverified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RobustnessUnverified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Robustness is Unverified
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Robustness Unverified
exact_mappings:
- dpv_risk:RobustnessUnverified
- dpv_risk_owl:RobustnessUnverified
is_a: QualityUnverified
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- RobustnessRisk
class_uri: risk:RobustnessUnverified

```
</details>

### Induced

<details>
```yaml
name: RobustnessUnverified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RobustnessUnverified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Robustness is Unverified
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Robustness Unverified
exact_mappings:
- dpv_risk:RobustnessUnverified
- dpv_risk_owl:RobustnessUnverified
is_a: QualityUnverified
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- RobustnessRisk
class_uri: risk:RobustnessUnverified

```
</details></div>