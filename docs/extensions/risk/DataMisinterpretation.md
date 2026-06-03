---
search:
  boost: 10.0
---

# Class: DataMisinterpretation 


_Concept representing data being misinterpretation_



<div data-search-exclude markdown="1">



URI: [risk:DataMisinterpretation](https://w3id.org/lmodel/dpv/risk/DataMisinterpretation)





```mermaid
 classDiagram
    class DataMisinterpretation
    click DataMisinterpretation href "../DataMisinterpretation/"
      PotentialConsequence <|-- DataMisinterpretation
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataMisinterpretation
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataMisinterpretation
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataRisk <|-- DataMisinterpretation
        click DataRisk href "../DataRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [DataRisk](DataRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **DataMisinterpretation** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataMisinterpretation](https://w3id.org/lmodel/dpv/risk/DataMisinterpretation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data Misinterpretation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataMisinterpretation |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataMisinterpretation |
| native | risk:DataMisinterpretation |
| exact | dpv_risk:DataMisinterpretation, dpv_risk_owl:DataMisinterpretation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataMisinterpretation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataMisinterpretation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing data being misinterpretation
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Misinterpretation
exact_mappings:
- dpv_risk:DataMisinterpretation
- dpv_risk_owl:DataMisinterpretation
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataMisinterpretation

```
</details>

### Induced

<details>
```yaml
name: DataMisinterpretation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataMisinterpretation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing data being misinterpretation
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Misinterpretation
exact_mappings:
- dpv_risk:DataMisinterpretation
- dpv_risk_owl:DataMisinterpretation
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataMisinterpretation

```
</details></div>