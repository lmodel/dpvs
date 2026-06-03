---
search:
  boost: 10.0
---

# Class: AccuracyInsufficient 


_Concepts representing risks and issues where Accuracy is Insufficient_



<div data-search-exclude markdown="1">



URI: [risk:AccuracyInsufficient](https://w3id.org/lmodel/dpv/risk/AccuracyInsufficient)





```mermaid
 classDiagram
    class AccuracyInsufficient
    click AccuracyInsufficient href "../AccuracyInsufficient/"
      PotentialConsequence <|-- AccuracyInsufficient
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- AccuracyInsufficient
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- AccuracyInsufficient
        click PotentialRiskSource href "../PotentialRiskSource/"
      QualityInsufficient <|-- AccuracyInsufficient
        click QualityInsufficient href "../QualityInsufficient/"
      AccuracyRisk <|-- AccuracyInsufficient
        click AccuracyRisk href "../AccuracyRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [AccuracyRisk](AccuracyRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **AccuracyInsufficient** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [QualityInsufficient](QualityInsufficient.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:AccuracyInsufficient](https://w3id.org/lmodel/dpv/risk/AccuracyInsufficient) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Accuracy Insufficient




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#AccuracyInsufficient |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:AccuracyInsufficient |
| native | risk:AccuracyInsufficient |
| exact | dpv_risk:AccuracyInsufficient, dpv_risk_owl:AccuracyInsufficient |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AccuracyInsufficient
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AccuracyInsufficient
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Accuracy is Insufficient
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Accuracy Insufficient
exact_mappings:
- dpv_risk:AccuracyInsufficient
- dpv_risk_owl:AccuracyInsufficient
is_a: AccuracyRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- QualityInsufficient
class_uri: risk:AccuracyInsufficient

```
</details>

### Induced

<details>
```yaml
name: AccuracyInsufficient
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AccuracyInsufficient
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Accuracy is Insufficient
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Accuracy Insufficient
exact_mappings:
- dpv_risk:AccuracyInsufficient
- dpv_risk_owl:AccuracyInsufficient
is_a: AccuracyRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- QualityInsufficient
class_uri: risk:AccuracyInsufficient

```
</details></div>