---
search:
  boost: 10.0
---

# Class: ResilienceInsufficient 


_Concepts representing risks and issues where Resilience is Insufficient_



<div data-search-exclude markdown="1">



URI: [risk:ResilienceInsufficient](https://w3id.org/lmodel/dpv/risk/ResilienceInsufficient)





```mermaid
 classDiagram
    class ResilienceInsufficient
    click ResilienceInsufficient href "../ResilienceInsufficient/"
      PotentialConsequence <|-- ResilienceInsufficient
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- ResilienceInsufficient
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- ResilienceInsufficient
        click PotentialRiskSource href "../PotentialRiskSource/"
      ResilienceRisk <|-- ResilienceInsufficient
        click ResilienceRisk href "../ResilienceRisk/"
      QualityInsufficient <|-- ResilienceInsufficient
        click QualityInsufficient href "../QualityInsufficient/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [QualityInsufficient](QualityInsufficient.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **ResilienceInsufficient** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [ResilienceRisk](ResilienceRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ResilienceInsufficient](https://w3id.org/lmodel/dpv/risk/ResilienceInsufficient) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Resilience Insufficient




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ResilienceInsufficient |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ResilienceInsufficient |
| native | risk:ResilienceInsufficient |
| exact | dpv_risk:ResilienceInsufficient, dpv_risk_owl:ResilienceInsufficient |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ResilienceInsufficient
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ResilienceInsufficient
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Resilience is Insufficient
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Resilience Insufficient
exact_mappings:
- dpv_risk:ResilienceInsufficient
- dpv_risk_owl:ResilienceInsufficient
is_a: QualityInsufficient
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- ResilienceRisk
class_uri: risk:ResilienceInsufficient

```
</details>

### Induced

<details>
```yaml
name: ResilienceInsufficient
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ResilienceInsufficient
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Resilience is Insufficient
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Resilience Insufficient
exact_mappings:
- dpv_risk:ResilienceInsufficient
- dpv_risk_owl:ResilienceInsufficient
is_a: QualityInsufficient
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- ResilienceRisk
class_uri: risk:ResilienceInsufficient

```
</details></div>