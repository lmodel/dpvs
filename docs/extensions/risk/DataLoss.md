---
search:
  boost: 10.0
---

# Class: DataLoss 


_Concept representing data loss (e.g. due to errors)_



<div data-search-exclude markdown="1">



URI: [risk:DataLoss](https://w3id.org/lmodel/dpv/risk/DataLoss)





```mermaid
 classDiagram
    class DataLoss
    click DataLoss href "../DataLoss/"
      PotentialConsequence <|-- DataLoss
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataLoss
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataLoss
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataRisk <|-- DataLoss
        click DataRisk href "../DataRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [DataRisk](DataRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **DataLoss** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataLoss](https://w3id.org/lmodel/dpv/risk/DataLoss) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data Loss




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataLoss |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataLoss |
| native | risk:DataLoss |
| exact | dpv_risk:DataLoss, dpv_risk_owl:DataLoss |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataLoss
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataLoss
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing data loss (e.g. due to errors)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Loss
exact_mappings:
- dpv_risk:DataLoss
- dpv_risk_owl:DataLoss
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataLoss

```
</details>

### Induced

<details>
```yaml
name: DataLoss
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataLoss
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing data loss (e.g. due to errors)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Loss
exact_mappings:
- dpv_risk:DataLoss
- dpv_risk_owl:DataLoss
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataLoss

```
</details></div>