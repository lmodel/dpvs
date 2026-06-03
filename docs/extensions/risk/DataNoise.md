---
search:
  boost: 10.0
---

# Class: DataNoise 


_Concept representing data being noise_



<div data-search-exclude markdown="1">



URI: [risk:DataNoise](https://w3id.org/lmodel/dpv/risk/DataNoise)





```mermaid
 classDiagram
    class DataNoise
    click DataNoise href "../DataNoise/"
      PotentialConsequence <|-- DataNoise
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataNoise
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataNoise
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataRisk <|-- DataNoise
        click DataRisk href "../DataRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [DataRisk](DataRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **DataNoise** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataNoise](https://w3id.org/lmodel/dpv/risk/DataNoise) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data Noise




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataNoise |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataNoise |
| native | risk:DataNoise |
| exact | dpv_risk:DataNoise, dpv_risk_owl:DataNoise |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataNoise
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataNoise
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing data being noise
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Noise
exact_mappings:
- dpv_risk:DataNoise
- dpv_risk_owl:DataNoise
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataNoise

```
</details>

### Induced

<details>
```yaml
name: DataNoise
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataNoise
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing data being noise
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Noise
exact_mappings:
- dpv_risk:DataNoise
- dpv_risk_owl:DataNoise
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataNoise

```
</details></div>