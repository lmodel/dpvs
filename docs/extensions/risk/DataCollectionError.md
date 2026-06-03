---
search:
  boost: 10.0
---

# Class: DataCollectionError 


_Concept representing error related to data collection_



<div data-search-exclude markdown="1">



URI: [risk:DataCollectionError](https://w3id.org/lmodel/dpv/risk/DataCollectionError)





```mermaid
 classDiagram
    class DataCollectionError
    click DataCollectionError href "../DataCollectionError/"
      PotentialConsequence <|-- DataCollectionError
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataCollectionError
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataCollectionError
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataProcessingError <|-- DataCollectionError
        click DataProcessingError href "../DataProcessingError/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [DataRisk](DataRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [DataProcessingError](DataProcessingError.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **DataCollectionError** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataCollectionError](https://w3id.org/lmodel/dpv/risk/DataCollectionError) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data Collection Error




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataCollectionError |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataCollectionError |
| native | risk:DataCollectionError |
| exact | dpv_risk:DataCollectionError, dpv_risk_owl:DataCollectionError |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataCollectionError
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataCollectionError
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing error related to data collection
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Collection Error
exact_mappings:
- dpv_risk:DataCollectionError
- dpv_risk_owl:DataCollectionError
is_a: DataProcessingError
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataCollectionError

```
</details>

### Induced

<details>
```yaml
name: DataCollectionError
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataCollectionError
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing error related to data collection
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Collection Error
exact_mappings:
- dpv_risk:DataCollectionError
- dpv_risk_owl:DataCollectionError
is_a: DataProcessingError
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataCollectionError

```
</details></div>