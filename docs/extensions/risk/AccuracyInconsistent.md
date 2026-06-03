---
search:
  boost: 10.0
---

# Class: AccuracyInconsistent 


_Concepts representing risks and issues where Accuracy is Inconsistent_



<div data-search-exclude markdown="1">



URI: [risk:AccuracyInconsistent](https://w3id.org/lmodel/dpv/risk/AccuracyInconsistent)





```mermaid
 classDiagram
    class AccuracyInconsistent
    click AccuracyInconsistent href "../AccuracyInconsistent/"
      PotentialConsequence <|-- AccuracyInconsistent
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- AccuracyInconsistent
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- AccuracyInconsistent
        click PotentialRiskSource href "../PotentialRiskSource/"
      QualityInconsistent <|-- AccuracyInconsistent
        click QualityInconsistent href "../QualityInconsistent/"
      AccuracyRisk <|-- AccuracyInconsistent
        click AccuracyRisk href "../AccuracyRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [AccuracyRisk](AccuracyRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **AccuracyInconsistent** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [QualityInconsistent](QualityInconsistent.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:AccuracyInconsistent](https://w3id.org/lmodel/dpv/risk/AccuracyInconsistent) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Accuracy Inconsistent




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#AccuracyInconsistent |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:AccuracyInconsistent |
| native | risk:AccuracyInconsistent |
| exact | dpv_risk:AccuracyInconsistent, dpv_risk_owl:AccuracyInconsistent |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AccuracyInconsistent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AccuracyInconsistent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Accuracy is Inconsistent
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Accuracy Inconsistent
exact_mappings:
- dpv_risk:AccuracyInconsistent
- dpv_risk_owl:AccuracyInconsistent
is_a: AccuracyRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- QualityInconsistent
class_uri: risk:AccuracyInconsistent

```
</details>

### Induced

<details>
```yaml
name: AccuracyInconsistent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AccuracyInconsistent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Accuracy is Inconsistent
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Accuracy Inconsistent
exact_mappings:
- dpv_risk:AccuracyInconsistent
- dpv_risk_owl:AccuracyInconsistent
is_a: AccuracyRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- QualityInconsistent
class_uri: risk:AccuracyInconsistent

```
</details></div>