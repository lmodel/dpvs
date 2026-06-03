---
search:
  boost: 10.0
---

# Class: RobustnessInsufficient 


_Concepts representing risks and issues where Robustness is Insufficient_



<div data-search-exclude markdown="1">



URI: [risk:RobustnessInsufficient](https://w3id.org/lmodel/dpv/risk/RobustnessInsufficient)





```mermaid
 classDiagram
    class RobustnessInsufficient
    click RobustnessInsufficient href "../RobustnessInsufficient/"
      PotentialConsequence <|-- RobustnessInsufficient
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- RobustnessInsufficient
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- RobustnessInsufficient
        click PotentialRiskSource href "../PotentialRiskSource/"
      RobustnessRisk <|-- RobustnessInsufficient
        click RobustnessRisk href "../RobustnessRisk/"
      QualityInsufficient <|-- RobustnessInsufficient
        click QualityInsufficient href "../QualityInsufficient/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [QualityInsufficient](QualityInsufficient.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **RobustnessInsufficient** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [RobustnessRisk](RobustnessRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RobustnessInsufficient](https://w3id.org/lmodel/dpv/risk/RobustnessInsufficient) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Robustness Insufficient




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RobustnessInsufficient |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RobustnessInsufficient |
| native | risk:RobustnessInsufficient |
| exact | dpv_risk:RobustnessInsufficient, dpv_risk_owl:RobustnessInsufficient |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RobustnessInsufficient
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RobustnessInsufficient
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Robustness is Insufficient
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Robustness Insufficient
exact_mappings:
- dpv_risk:RobustnessInsufficient
- dpv_risk_owl:RobustnessInsufficient
is_a: QualityInsufficient
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- RobustnessRisk
class_uri: risk:RobustnessInsufficient

```
</details>

### Induced

<details>
```yaml
name: RobustnessInsufficient
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RobustnessInsufficient
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Robustness is Insufficient
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Robustness Insufficient
exact_mappings:
- dpv_risk:RobustnessInsufficient
- dpv_risk_owl:RobustnessInsufficient
is_a: QualityInsufficient
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- RobustnessRisk
class_uri: risk:RobustnessInsufficient

```
</details></div>