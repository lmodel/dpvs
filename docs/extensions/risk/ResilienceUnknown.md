---
search:
  boost: 10.0
---

# Class: ResilienceUnknown 


_Concepts representing risks and issues where Resilience is Unknown_



<div data-search-exclude markdown="1">



URI: [risk:ResilienceUnknown](https://w3id.org/lmodel/dpv/risk/ResilienceUnknown)





```mermaid
 classDiagram
    class ResilienceUnknown
    click ResilienceUnknown href "../ResilienceUnknown/"
      PotentialConsequence <|-- ResilienceUnknown
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- ResilienceUnknown
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- ResilienceUnknown
        click PotentialRiskSource href "../PotentialRiskSource/"
      ResilienceRisk <|-- ResilienceUnknown
        click ResilienceRisk href "../ResilienceRisk/"
      QualityUnknown <|-- ResilienceUnknown
        click QualityUnknown href "../QualityUnknown/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [QualityUnknown](QualityUnknown.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **ResilienceUnknown** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [ResilienceRisk](ResilienceRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ResilienceUnknown](https://w3id.org/lmodel/dpv/risk/ResilienceUnknown) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Resilience Unknown




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ResilienceUnknown |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ResilienceUnknown |
| native | risk:ResilienceUnknown |
| exact | dpv_risk:ResilienceUnknown, dpv_risk_owl:ResilienceUnknown |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ResilienceUnknown
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ResilienceUnknown
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Resilience is Unknown
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Resilience Unknown
exact_mappings:
- dpv_risk:ResilienceUnknown
- dpv_risk_owl:ResilienceUnknown
is_a: QualityUnknown
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- ResilienceRisk
class_uri: risk:ResilienceUnknown

```
</details>

### Induced

<details>
```yaml
name: ResilienceUnknown
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ResilienceUnknown
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Resilience is Unknown
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Resilience Unknown
exact_mappings:
- dpv_risk:ResilienceUnknown
- dpv_risk_owl:ResilienceUnknown
is_a: QualityUnknown
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- ResilienceRisk
class_uri: risk:ResilienceUnknown

```
</details></div>