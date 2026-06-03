---
search:
  boost: 10.0
---

# Class: AccuracyUnknown 


_Concepts representing risks and issues where Accuracy is Unknown_



<div data-search-exclude markdown="1">



URI: [risk:AccuracyUnknown](https://w3id.org/lmodel/dpv/risk/AccuracyUnknown)





```mermaid
 classDiagram
    class AccuracyUnknown
    click AccuracyUnknown href "../AccuracyUnknown/"
      PotentialConsequence <|-- AccuracyUnknown
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- AccuracyUnknown
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- AccuracyUnknown
        click PotentialRiskSource href "../PotentialRiskSource/"
      QualityUnknown <|-- AccuracyUnknown
        click QualityUnknown href "../QualityUnknown/"
      AccuracyRisk <|-- AccuracyUnknown
        click AccuracyRisk href "../AccuracyRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [AccuracyRisk](AccuracyRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **AccuracyUnknown** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [QualityUnknown](QualityUnknown.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:AccuracyUnknown](https://w3id.org/lmodel/dpv/risk/AccuracyUnknown) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Accuracy Unknown




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#AccuracyUnknown |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:AccuracyUnknown |
| native | risk:AccuracyUnknown |
| exact | dpv_risk:AccuracyUnknown, dpv_risk_owl:AccuracyUnknown |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AccuracyUnknown
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AccuracyUnknown
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Accuracy is Unknown
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Accuracy Unknown
exact_mappings:
- dpv_risk:AccuracyUnknown
- dpv_risk_owl:AccuracyUnknown
is_a: AccuracyRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- QualityUnknown
class_uri: risk:AccuracyUnknown

```
</details>

### Induced

<details>
```yaml
name: AccuracyUnknown
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AccuracyUnknown
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Accuracy is Unknown
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Accuracy Unknown
exact_mappings:
- dpv_risk:AccuracyUnknown
- dpv_risk_owl:AccuracyUnknown
is_a: AccuracyRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- QualityUnknown
class_uri: risk:AccuracyUnknown

```
</details></div>