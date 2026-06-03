---
search:
  boost: 10.0
---

# Class: ResilienceInconsistent 


_Concepts representing risks and issues where Resilience is Inconsistent_



<div data-search-exclude markdown="1">



URI: [risk:ResilienceInconsistent](https://w3id.org/lmodel/dpv/risk/ResilienceInconsistent)





```mermaid
 classDiagram
    class ResilienceInconsistent
    click ResilienceInconsistent href "../ResilienceInconsistent/"
      PotentialConsequence <|-- ResilienceInconsistent
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- ResilienceInconsistent
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- ResilienceInconsistent
        click PotentialRiskSource href "../PotentialRiskSource/"
      ResilienceRisk <|-- ResilienceInconsistent
        click ResilienceRisk href "../ResilienceRisk/"
      QualityInconsistent <|-- ResilienceInconsistent
        click QualityInconsistent href "../QualityInconsistent/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [QualityInconsistent](QualityInconsistent.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **ResilienceInconsistent** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [ResilienceRisk](ResilienceRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ResilienceInconsistent](https://w3id.org/lmodel/dpv/risk/ResilienceInconsistent) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Resilience Inconsistent




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ResilienceInconsistent |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ResilienceInconsistent |
| native | risk:ResilienceInconsistent |
| exact | dpv_risk:ResilienceInconsistent, dpv_risk_owl:ResilienceInconsistent |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ResilienceInconsistent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ResilienceInconsistent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Resilience is Inconsistent
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Resilience Inconsistent
exact_mappings:
- dpv_risk:ResilienceInconsistent
- dpv_risk_owl:ResilienceInconsistent
is_a: QualityInconsistent
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- ResilienceRisk
class_uri: risk:ResilienceInconsistent

```
</details>

### Induced

<details>
```yaml
name: ResilienceInconsistent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ResilienceInconsistent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Resilience is Inconsistent
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Resilience Inconsistent
exact_mappings:
- dpv_risk:ResilienceInconsistent
- dpv_risk_owl:ResilienceInconsistent
is_a: QualityInconsistent
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- ResilienceRisk
class_uri: risk:ResilienceInconsistent

```
</details></div>