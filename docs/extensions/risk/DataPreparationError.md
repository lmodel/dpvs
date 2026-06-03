---
search:
  boost: 10.0
---

# Class: DataPreparationError 


_Concept representing error related to data preparation_



<div data-search-exclude markdown="1">



URI: [risk:DataPreparationError](https://w3id.org/lmodel/dpv/risk/DataPreparationError)





```mermaid
 classDiagram
    class DataPreparationError
    click DataPreparationError href "../DataPreparationError/"
      PotentialConsequence <|-- DataPreparationError
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataPreparationError
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataPreparationError
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataProcessingError <|-- DataPreparationError
        click DataProcessingError href "../DataProcessingError/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [DataRisk](DataRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [DataProcessingError](DataProcessingError.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **DataPreparationError** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataPreparationError](https://w3id.org/lmodel/dpv/risk/DataPreparationError) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data Preparation Error




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataPreparationError |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataPreparationError |
| native | risk:DataPreparationError |
| exact | dpv_risk:DataPreparationError, dpv_risk_owl:DataPreparationError |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataPreparationError
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataPreparationError
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing error related to data preparation
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Preparation Error
exact_mappings:
- dpv_risk:DataPreparationError
- dpv_risk_owl:DataPreparationError
is_a: DataProcessingError
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataPreparationError

```
</details>

### Induced

<details>
```yaml
name: DataPreparationError
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataPreparationError
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing error related to data preparation
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Preparation Error
exact_mappings:
- dpv_risk:DataPreparationError
- dpv_risk_owl:DataPreparationError
is_a: DataProcessingError
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataPreparationError

```
</details></div>