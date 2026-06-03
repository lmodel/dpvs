---
search:
  boost: 10.0
---

# Class: DataIncomplete 


_Concept representing data being incomplete_



<div data-search-exclude markdown="1">



URI: [risk:DataIncomplete](https://w3id.org/lmodel/dpv/risk/DataIncomplete)





```mermaid
 classDiagram
    class DataIncomplete
    click DataIncomplete href "../DataIncomplete/"
      PotentialConsequence <|-- DataIncomplete
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataIncomplete
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataIncomplete
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataRisk <|-- DataIncomplete
        click DataRisk href "../DataRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [DataRisk](DataRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **DataIncomplete** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataIncomplete](https://w3id.org/lmodel/dpv/risk/DataIncomplete) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data Incomplete




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataIncomplete |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataIncomplete |
| native | risk:DataIncomplete |
| exact | dpv_risk:DataIncomplete, dpv_risk_owl:DataIncomplete |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataIncomplete
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataIncomplete
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing data being incomplete
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Incomplete
exact_mappings:
- dpv_risk:DataIncomplete
- dpv_risk_owl:DataIncomplete
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataIncomplete

```
</details>

### Induced

<details>
```yaml
name: DataIncomplete
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataIncomplete
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing data being incomplete
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Incomplete
exact_mappings:
- dpv_risk:DataIncomplete
- dpv_risk_owl:DataIncomplete
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataIncomplete

```
</details></div>