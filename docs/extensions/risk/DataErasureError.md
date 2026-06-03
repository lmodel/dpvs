---
search:
  boost: 10.0
---

# Class: DataErasureError 


_Concept representing error related to data erasure_



<div data-search-exclude markdown="1">



URI: [risk:DataErasureError](https://w3id.org/lmodel/dpv/risk/DataErasureError)





```mermaid
 classDiagram
    class DataErasureError
    click DataErasureError href "../DataErasureError/"
      PotentialConsequence <|-- DataErasureError
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataErasureError
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataErasureError
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataProcessingError <|-- DataErasureError
        click DataProcessingError href "../DataProcessingError/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [DataRisk](DataRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [DataProcessingError](DataProcessingError.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **DataErasureError** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataErasureError](https://w3id.org/lmodel/dpv/risk/DataErasureError) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data Erasure Error




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataErasureError |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataErasureError |
| native | risk:DataErasureError |
| exact | dpv_risk:DataErasureError, dpv_risk_owl:DataErasureError |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataErasureError
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataErasureError
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing error related to data erasure
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Erasure Error
exact_mappings:
- dpv_risk:DataErasureError
- dpv_risk_owl:DataErasureError
is_a: DataProcessingError
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataErasureError

```
</details>

### Induced

<details>
```yaml
name: DataErasureError
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataErasureError
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing error related to data erasure
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Erasure Error
exact_mappings:
- dpv_risk:DataErasureError
- dpv_risk_owl:DataErasureError
is_a: DataProcessingError
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataErasureError

```
</details></div>