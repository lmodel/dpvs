---
search:
  boost: 10.0
---

# Class: ResilienceRisk 


_Concepts representing risks and issues regarding Resilience_



<div data-search-exclude markdown="1">



URI: [risk:ResilienceRisk](https://w3id.org/lmodel/dpv/risk/ResilienceRisk)





```mermaid
 classDiagram
    class ResilienceRisk
    click ResilienceRisk href "../ResilienceRisk/"
      PotentialConsequence <|-- ResilienceRisk
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- ResilienceRisk
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- ResilienceRisk
        click PotentialRiskSource href "../PotentialRiskSource/"
      QualityRisk <|-- ResilienceRisk
        click QualityRisk href "../QualityRisk/"
      

      ResilienceRisk <|-- ResilienceDegraded
        click ResilienceDegraded href "../ResilienceDegraded/"
      ResilienceRisk <|-- ResilienceInconsistent
        click ResilienceInconsistent href "../ResilienceInconsistent/"
      ResilienceRisk <|-- ResilienceInsufficient
        click ResilienceInsufficient href "../ResilienceInsufficient/"
      ResilienceRisk <|-- ResilienceUnknown
        click ResilienceUnknown href "../ResilienceUnknown/"
      ResilienceRisk <|-- ResilienceUnverified
        click ResilienceUnverified href "../ResilienceUnverified/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **ResilienceRisk** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ResilienceRisk](https://w3id.org/lmodel/dpv/risk/ResilienceRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Resilience Risk




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ResilienceRisk |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ResilienceRisk |
| native | risk:ResilienceRisk |
| exact | dpv_risk:ResilienceRisk, dpv_risk_owl:ResilienceRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ResilienceRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ResilienceRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues regarding Resilience
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Resilience Risk
exact_mappings:
- dpv_risk:ResilienceRisk
- dpv_risk_owl:ResilienceRisk
is_a: QualityRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:ResilienceRisk

```
</details>

### Induced

<details>
```yaml
name: ResilienceRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ResilienceRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues regarding Resilience
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Resilience Risk
exact_mappings:
- dpv_risk:ResilienceRisk
- dpv_risk_owl:ResilienceRisk
is_a: QualityRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:ResilienceRisk

```
</details></div>