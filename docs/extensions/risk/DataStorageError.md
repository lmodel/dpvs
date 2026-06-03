---
search:
  boost: 10.0
---

# Class: DataStorageError 


_Concept representing error related to data storage_



<div data-search-exclude markdown="1">



URI: [risk:DataStorageError](https://w3id.org/lmodel/dpv/risk/DataStorageError)





```mermaid
 classDiagram
    class DataStorageError
    click DataStorageError href "../DataStorageError/"
      PotentialConsequence <|-- DataStorageError
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataStorageError
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataStorageError
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataProcessingError <|-- DataStorageError
        click DataProcessingError href "../DataProcessingError/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [DataRisk](DataRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [DataProcessingError](DataProcessingError.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **DataStorageError** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataStorageError](https://w3id.org/lmodel/dpv/risk/DataStorageError) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data Storage Error




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataStorageError |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataStorageError |
| native | risk:DataStorageError |
| exact | dpv_risk:DataStorageError, dpv_risk_owl:DataStorageError |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataStorageError
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataStorageError
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing error related to data storage
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Storage Error
exact_mappings:
- dpv_risk:DataStorageError
- dpv_risk_owl:DataStorageError
is_a: DataProcessingError
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataStorageError

```
</details>

### Induced

<details>
```yaml
name: DataStorageError
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataStorageError
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing error related to data storage
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Storage Error
exact_mappings:
- dpv_risk:DataStorageError
- dpv_risk_owl:DataStorageError
is_a: DataProcessingError
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataStorageError

```
</details></div>