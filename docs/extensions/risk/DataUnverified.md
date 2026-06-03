---
search:
  boost: 10.0
---

# Class: DataUnverified 


_Concept representing data being unverified_



<div data-search-exclude markdown="1">



URI: [risk:DataUnverified](https://w3id.org/lmodel/dpv/risk/DataUnverified)





```mermaid
 classDiagram
    class DataUnverified
    click DataUnverified href "../DataUnverified/"
      PotentialConsequence <|-- DataUnverified
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataUnverified
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataUnverified
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataRisk <|-- DataUnverified
        click DataRisk href "../DataRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [DataRisk](DataRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **DataUnverified** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataUnverified](https://w3id.org/lmodel/dpv/risk/DataUnverified) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data Unverified




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataUnverified |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataUnverified |
| native | risk:DataUnverified |
| exact | dpv_risk:DataUnverified, dpv_risk_owl:DataUnverified |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataUnverified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataUnverified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing data being unverified
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Unverified
exact_mappings:
- dpv_risk:DataUnverified
- dpv_risk_owl:DataUnverified
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataUnverified

```
</details>

### Induced

<details>
```yaml
name: DataUnverified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataUnverified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing data being unverified
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Unverified
exact_mappings:
- dpv_risk:DataUnverified
- dpv_risk_owl:DataUnverified
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataUnverified

```
</details></div>