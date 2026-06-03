---
search:
  boost: 10.0
---

# Class: DataMisclassified 


_Concept representing data being misclassified_



<div data-search-exclude markdown="1">



URI: [risk:DataMisclassified](https://w3id.org/lmodel/dpv/risk/DataMisclassified)





```mermaid
 classDiagram
    class DataMisclassified
    click DataMisclassified href "../DataMisclassified/"
      PotentialConsequence <|-- DataMisclassified
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataMisclassified
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataMisclassified
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataRisk <|-- DataMisclassified
        click DataRisk href "../DataRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [DataRisk](DataRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **DataMisclassified** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataMisclassified](https://w3id.org/lmodel/dpv/risk/DataMisclassified) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data Misclassified




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataMisclassified |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataMisclassified |
| native | risk:DataMisclassified |
| exact | dpv_risk:DataMisclassified, dpv_risk_owl:DataMisclassified |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataMisclassified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataMisclassified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing data being misclassified
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Misclassified
exact_mappings:
- dpv_risk:DataMisclassified
- dpv_risk_owl:DataMisclassified
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataMisclassified

```
</details>

### Induced

<details>
```yaml
name: DataMisclassified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataMisclassified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing data being misclassified
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Misclassified
exact_mappings:
- dpv_risk:DataMisclassified
- dpv_risk_owl:DataMisclassified
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataMisclassified

```
</details></div>