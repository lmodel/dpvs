---
search:
  boost: 10.0
---

# Class: DataSelectionError 


_Concept representing an error in data selection_



<div data-search-exclude markdown="1">



URI: [risk:DataSelectionError](https://w3id.org/lmodel/dpv/risk/DataSelectionError)





```mermaid
 classDiagram
    class DataSelectionError
    click DataSelectionError href "../DataSelectionError/"
      PotentialConsequence <|-- DataSelectionError
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataSelectionError
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataSelectionError
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataProcessingError <|-- DataSelectionError
        click DataProcessingError href "../DataProcessingError/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [DataRisk](DataRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [DataProcessingError](DataProcessingError.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **DataSelectionError** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataSelectionError](https://w3id.org/lmodel/dpv/risk/DataSelectionError) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data SelectionError




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataSelectionError |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataSelectionError |
| native | risk:DataSelectionError |
| exact | dpv_risk:DataSelectionError, dpv_risk_owl:DataSelectionError |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataSelectionError
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataSelectionError
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing an error in data selection
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data SelectionError
exact_mappings:
- dpv_risk:DataSelectionError
- dpv_risk_owl:DataSelectionError
is_a: DataProcessingError
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataSelectionError

```
</details>

### Induced

<details>
```yaml
name: DataSelectionError
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataSelectionError
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing an error in data selection
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data SelectionError
exact_mappings:
- dpv_risk:DataSelectionError
- dpv_risk_owl:DataSelectionError
is_a: DataProcessingError
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataSelectionError

```
</details></div>