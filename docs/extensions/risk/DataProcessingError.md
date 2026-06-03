---
search:
  boost: 10.0
---

# Class: DataProcessingError 


_Concept representing operational error in the processing of data_



<div data-search-exclude markdown="1">



URI: [risk:DataProcessingError](https://w3id.org/lmodel/dpv/risk/DataProcessingError)





```mermaid
 classDiagram
    class DataProcessingError
    click DataProcessingError href "../DataProcessingError/"
      PotentialConsequence <|-- DataProcessingError
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataProcessingError
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataProcessingError
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataRisk <|-- DataProcessingError
        click DataRisk href "../DataRisk/"
      

      DataProcessingError <|-- DataCollectionError
        click DataCollectionError href "../DataCollectionError/"
      DataProcessingError <|-- DataErasureError
        click DataErasureError href "../DataErasureError/"
      DataProcessingError <|-- DataPreparationError
        click DataPreparationError href "../DataPreparationError/"
      DataProcessingError <|-- DataSelectionError
        click DataSelectionError href "../DataSelectionError/"
      DataProcessingError <|-- DataStorageError
        click DataStorageError href "../DataStorageError/"
      DataProcessingError <|-- DataTransferError
        click DataTransferError href "../DataTransferError/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [DataRisk](DataRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **DataProcessingError** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [DataCollectionError](DataCollectionError.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [DataErasureError](DataErasureError.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [DataPreparationError](DataPreparationError.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [DataSelectionError](DataSelectionError.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [DataStorageError](DataStorageError.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [DataTransferError](DataTransferError.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataProcessingError](https://w3id.org/lmodel/dpv/risk/DataProcessingError) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data Processing Error




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataProcessingError |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataProcessingError |
| native | risk:DataProcessingError |
| exact | dpv_risk:DataProcessingError, dpv_risk_owl:DataProcessingError |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataProcessingError
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataProcessingError
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing operational error in the processing of data
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Processing Error
exact_mappings:
- dpv_risk:DataProcessingError
- dpv_risk_owl:DataProcessingError
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataProcessingError

```
</details>

### Induced

<details>
```yaml
name: DataProcessingError
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataProcessingError
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing operational error in the processing of data
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Processing Error
exact_mappings:
- dpv_risk:DataProcessingError
- dpv_risk_owl:DataProcessingError
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataProcessingError

```
</details></div>