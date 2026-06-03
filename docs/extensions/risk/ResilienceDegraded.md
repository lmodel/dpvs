---
search:
  boost: 10.0
---

# Class: ResilienceDegraded 


_Concepts representing risks and issues where Resilience is Degraded_



<div data-search-exclude markdown="1">



URI: [risk:ResilienceDegraded](https://w3id.org/lmodel/dpv/risk/ResilienceDegraded)





```mermaid
 classDiagram
    class ResilienceDegraded
    click ResilienceDegraded href "../ResilienceDegraded/"
      PotentialConsequence <|-- ResilienceDegraded
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- ResilienceDegraded
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- ResilienceDegraded
        click PotentialRiskSource href "../PotentialRiskSource/"
      ResilienceRisk <|-- ResilienceDegraded
        click ResilienceRisk href "../ResilienceRisk/"
      QualityDegraded <|-- ResilienceDegraded
        click QualityDegraded href "../QualityDegraded/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [QualityDegraded](QualityDegraded.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **ResilienceDegraded** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [ResilienceRisk](ResilienceRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ResilienceDegraded](https://w3id.org/lmodel/dpv/risk/ResilienceDegraded) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Resilience Degraded




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ResilienceDegraded |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ResilienceDegraded |
| native | risk:ResilienceDegraded |
| exact | dpv_risk:ResilienceDegraded, dpv_risk_owl:ResilienceDegraded |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ResilienceDegraded
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ResilienceDegraded
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Resilience is Degraded
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Resilience Degraded
exact_mappings:
- dpv_risk:ResilienceDegraded
- dpv_risk_owl:ResilienceDegraded
is_a: QualityDegraded
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- ResilienceRisk
class_uri: risk:ResilienceDegraded

```
</details>

### Induced

<details>
```yaml
name: ResilienceDegraded
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ResilienceDegraded
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Resilience is Degraded
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Resilience Degraded
exact_mappings:
- dpv_risk:ResilienceDegraded
- dpv_risk_owl:ResilienceDegraded
is_a: QualityDegraded
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- ResilienceRisk
class_uri: risk:ResilienceDegraded

```
</details></div>