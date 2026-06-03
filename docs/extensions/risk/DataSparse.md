---
search:
  boost: 10.0
---

# Class: DataSparse 


_Concept representing data being sparse_



<div data-search-exclude markdown="1">



URI: [risk:DataSparse](https://w3id.org/lmodel/dpv/risk/DataSparse)





```mermaid
 classDiagram
    class DataSparse
    click DataSparse href "../DataSparse/"
      PotentialConsequence <|-- DataSparse
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataSparse
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataSparse
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataRisk <|-- DataSparse
        click DataRisk href "../DataRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [DataRisk](DataRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **DataSparse** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataSparse](https://w3id.org/lmodel/dpv/risk/DataSparse) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data Sparse




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataSparse |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataSparse |
| native | risk:DataSparse |
| exact | dpv_risk:DataSparse, dpv_risk_owl:DataSparse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataSparse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataSparse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing data being sparse
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Sparse
exact_mappings:
- dpv_risk:DataSparse
- dpv_risk_owl:DataSparse
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataSparse

```
</details>

### Induced

<details>
```yaml
name: DataSparse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataSparse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing data being sparse
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Sparse
exact_mappings:
- dpv_risk:DataSparse
- dpv_risk_owl:DataSparse
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataSparse

```
</details></div>