---
search:
  boost: 10.0
---

# Class: RobustnessUnknown 


_Concepts representing risks and issues where Robustness is Unknown_



<div data-search-exclude markdown="1">



URI: [risk:RobustnessUnknown](https://w3id.org/lmodel/dpv/risk/RobustnessUnknown)





```mermaid
 classDiagram
    class RobustnessUnknown
    click RobustnessUnknown href "../RobustnessUnknown/"
      PotentialConsequence <|-- RobustnessUnknown
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- RobustnessUnknown
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- RobustnessUnknown
        click PotentialRiskSource href "../PotentialRiskSource/"
      RobustnessRisk <|-- RobustnessUnknown
        click RobustnessRisk href "../RobustnessRisk/"
      QualityUnknown <|-- RobustnessUnknown
        click QualityUnknown href "../QualityUnknown/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [QualityUnknown](QualityUnknown.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **RobustnessUnknown** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [RobustnessRisk](RobustnessRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RobustnessUnknown](https://w3id.org/lmodel/dpv/risk/RobustnessUnknown) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Robustness Unknown




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RobustnessUnknown |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RobustnessUnknown |
| native | risk:RobustnessUnknown |
| exact | dpv_risk:RobustnessUnknown, dpv_risk_owl:RobustnessUnknown |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RobustnessUnknown
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RobustnessUnknown
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Robustness is Unknown
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Robustness Unknown
exact_mappings:
- dpv_risk:RobustnessUnknown
- dpv_risk_owl:RobustnessUnknown
is_a: QualityUnknown
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- RobustnessRisk
class_uri: risk:RobustnessUnknown

```
</details>

### Induced

<details>
```yaml
name: RobustnessUnknown
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RobustnessUnknown
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Robustness is Unknown
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Robustness Unknown
exact_mappings:
- dpv_risk:RobustnessUnknown
- dpv_risk_owl:RobustnessUnknown
is_a: QualityUnknown
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- RobustnessRisk
class_uri: risk:RobustnessUnknown

```
</details></div>