---
search:
  boost: 10.0
---

# Class: DataOutdated 


_Concept representing data being outdated_



<div data-search-exclude markdown="1">



URI: [risk:DataOutdated](https://w3id.org/lmodel/dpv/risk/DataOutdated)





```mermaid
 classDiagram
    class DataOutdated
    click DataOutdated href "../DataOutdated/"
      PotentialConsequence <|-- DataOutdated
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataOutdated
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataOutdated
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataRisk <|-- DataOutdated
        click DataRisk href "../DataRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [DataRisk](DataRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **DataOutdated** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataOutdated](https://w3id.org/lmodel/dpv/risk/DataOutdated) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data Outdated




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataOutdated |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataOutdated |
| native | risk:DataOutdated |
| exact | dpv_risk:DataOutdated, dpv_risk_owl:DataOutdated |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataOutdated
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataOutdated
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing data being outdated
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Outdated
exact_mappings:
- dpv_risk:DataOutdated
- dpv_risk_owl:DataOutdated
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataOutdated

```
</details>

### Induced

<details>
```yaml
name: DataOutdated
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataOutdated
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing data being outdated
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Outdated
exact_mappings:
- dpv_risk:DataOutdated
- dpv_risk_owl:DataOutdated
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataOutdated

```
</details></div>