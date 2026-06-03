---
search:
  boost: 10.0
---

# Class: AccuracyDegraded 


_Concepts representing risks and issues where Accuracy is Degraded_



<div data-search-exclude markdown="1">



URI: [risk:AccuracyDegraded](https://w3id.org/lmodel/dpv/risk/AccuracyDegraded)





```mermaid
 classDiagram
    class AccuracyDegraded
    click AccuracyDegraded href "../AccuracyDegraded/"
      PotentialConsequence <|-- AccuracyDegraded
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- AccuracyDegraded
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- AccuracyDegraded
        click PotentialRiskSource href "../PotentialRiskSource/"
      QualityDegraded <|-- AccuracyDegraded
        click QualityDegraded href "../QualityDegraded/"
      AccuracyRisk <|-- AccuracyDegraded
        click AccuracyRisk href "../AccuracyRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [AccuracyRisk](AccuracyRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **AccuracyDegraded** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [QualityDegraded](QualityDegraded.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:AccuracyDegraded](https://w3id.org/lmodel/dpv/risk/AccuracyDegraded) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Accuracy Degraded




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#AccuracyDegraded |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:AccuracyDegraded |
| native | risk:AccuracyDegraded |
| exact | dpv_risk:AccuracyDegraded, dpv_risk_owl:AccuracyDegraded |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AccuracyDegraded
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AccuracyDegraded
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Accuracy is Degraded
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Accuracy Degraded
exact_mappings:
- dpv_risk:AccuracyDegraded
- dpv_risk_owl:AccuracyDegraded
is_a: AccuracyRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- QualityDegraded
class_uri: risk:AccuracyDegraded

```
</details>

### Induced

<details>
```yaml
name: AccuracyDegraded
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AccuracyDegraded
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Accuracy is Degraded
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Accuracy Degraded
exact_mappings:
- dpv_risk:AccuracyDegraded
- dpv_risk_owl:AccuracyDegraded
is_a: AccuracyRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- QualityDegraded
class_uri: risk:AccuracyDegraded

```
</details></div>