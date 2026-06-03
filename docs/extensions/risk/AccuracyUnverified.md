---
search:
  boost: 10.0
---

# Class: AccuracyUnverified 


_Concepts representing risks and issues where Accuracy is Unverified_



<div data-search-exclude markdown="1">



URI: [risk:AccuracyUnverified](https://w3id.org/lmodel/dpv/risk/AccuracyUnverified)





```mermaid
 classDiagram
    class AccuracyUnverified
    click AccuracyUnverified href "../AccuracyUnverified/"
      PotentialConsequence <|-- AccuracyUnverified
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- AccuracyUnverified
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- AccuracyUnverified
        click PotentialRiskSource href "../PotentialRiskSource/"
      QualityUnverified <|-- AccuracyUnverified
        click QualityUnverified href "../QualityUnverified/"
      AccuracyRisk <|-- AccuracyUnverified
        click AccuracyRisk href "../AccuracyRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [AccuracyRisk](AccuracyRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **AccuracyUnverified** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [QualityUnverified](QualityUnverified.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:AccuracyUnverified](https://w3id.org/lmodel/dpv/risk/AccuracyUnverified) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Accuracy Unverified




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#AccuracyUnverified |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:AccuracyUnverified |
| native | risk:AccuracyUnverified |
| exact | dpv_risk:AccuracyUnverified, dpv_risk_owl:AccuracyUnverified |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AccuracyUnverified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AccuracyUnverified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Accuracy is Unverified
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Accuracy Unverified
exact_mappings:
- dpv_risk:AccuracyUnverified
- dpv_risk_owl:AccuracyUnverified
is_a: AccuracyRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- QualityUnverified
class_uri: risk:AccuracyUnverified

```
</details>

### Induced

<details>
```yaml
name: AccuracyUnverified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AccuracyUnverified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Accuracy is Unverified
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Accuracy Unverified
exact_mappings:
- dpv_risk:AccuracyUnverified
- dpv_risk_owl:AccuracyUnverified
is_a: AccuracyRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- QualityUnverified
class_uri: risk:AccuracyUnverified

```
</details></div>