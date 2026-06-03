---
search:
  boost: 10.0
---

# Class: ResilienceUnverified 


_Concepts representing risks and issues where Resilience is Unverified_



<div data-search-exclude markdown="1">



URI: [risk:ResilienceUnverified](https://w3id.org/lmodel/dpv/risk/ResilienceUnverified)





```mermaid
 classDiagram
    class ResilienceUnverified
    click ResilienceUnverified href "../ResilienceUnverified/"
      PotentialConsequence <|-- ResilienceUnverified
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- ResilienceUnverified
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- ResilienceUnverified
        click PotentialRiskSource href "../PotentialRiskSource/"
      ResilienceRisk <|-- ResilienceUnverified
        click ResilienceRisk href "../ResilienceRisk/"
      QualityUnverified <|-- ResilienceUnverified
        click QualityUnverified href "../QualityUnverified/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [QualityUnverified](QualityUnverified.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **ResilienceUnverified** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [ResilienceRisk](ResilienceRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ResilienceUnverified](https://w3id.org/lmodel/dpv/risk/ResilienceUnverified) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Resilience Unverified




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ResilienceUnverified |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ResilienceUnverified |
| native | risk:ResilienceUnverified |
| exact | dpv_risk:ResilienceUnverified, dpv_risk_owl:ResilienceUnverified |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ResilienceUnverified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ResilienceUnverified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Resilience is Unverified
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Resilience Unverified
exact_mappings:
- dpv_risk:ResilienceUnverified
- dpv_risk_owl:ResilienceUnverified
is_a: QualityUnverified
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- ResilienceRisk
class_uri: risk:ResilienceUnverified

```
</details>

### Induced

<details>
```yaml
name: ResilienceUnverified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ResilienceUnverified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Resilience is Unverified
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Resilience Unverified
exact_mappings:
- dpv_risk:ResilienceUnverified
- dpv_risk_owl:ResilienceUnverified
is_a: QualityUnverified
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- ResilienceRisk
class_uri: risk:ResilienceUnverified

```
</details></div>