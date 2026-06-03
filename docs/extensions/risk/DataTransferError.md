---
search:
  boost: 10.0
---

# Class: DataTransferError 


_Concept representing error related to data transfer_



<div data-search-exclude markdown="1">



URI: [risk:DataTransferError](https://w3id.org/lmodel/dpv/risk/DataTransferError)





```mermaid
 classDiagram
    class DataTransferError
    click DataTransferError href "../DataTransferError/"
      PotentialConsequence <|-- DataTransferError
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataTransferError
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataTransferError
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataProcessingError <|-- DataTransferError
        click DataProcessingError href "../DataProcessingError/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [DataRisk](DataRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [DataProcessingError](DataProcessingError.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **DataTransferError** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataTransferError](https://w3id.org/lmodel/dpv/risk/DataTransferError) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data Transfer Error




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataTransferError |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataTransferError |
| native | risk:DataTransferError |
| exact | dpv_risk:DataTransferError, dpv_risk_owl:DataTransferError |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataTransferError
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataTransferError
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing error related to data transfer
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Transfer Error
exact_mappings:
- dpv_risk:DataTransferError
- dpv_risk_owl:DataTransferError
is_a: DataProcessingError
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataTransferError

```
</details>

### Induced

<details>
```yaml
name: DataTransferError
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataTransferError
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing error related to data transfer
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Transfer Error
exact_mappings:
- dpv_risk:DataTransferError
- dpv_risk_owl:DataTransferError
is_a: DataProcessingError
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataTransferError

```
</details></div>