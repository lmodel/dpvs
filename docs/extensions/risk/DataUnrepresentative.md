---
search:
  boost: 10.0
---

# Class: DataUnrepresentative 


_Concept representing data being unrepresentative_



<div data-search-exclude markdown="1">



URI: [risk:DataUnrepresentative](https://w3id.org/lmodel/dpv/risk/DataUnrepresentative)





```mermaid
 classDiagram
    class DataUnrepresentative
    click DataUnrepresentative href "../DataUnrepresentative/"
      PotentialConsequence <|-- DataUnrepresentative
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataUnrepresentative
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataUnrepresentative
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataRisk <|-- DataUnrepresentative
        click DataRisk href "../DataRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [DataRisk](DataRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **DataUnrepresentative** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataUnrepresentative](https://w3id.org/lmodel/dpv/risk/DataUnrepresentative) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data Unrepresentative




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataUnrepresentative |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataUnrepresentative |
| native | risk:DataUnrepresentative |
| exact | dpv_risk:DataUnrepresentative, dpv_risk_owl:DataUnrepresentative |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataUnrepresentative
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataUnrepresentative
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing data being unrepresentative
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Unrepresentative
exact_mappings:
- dpv_risk:DataUnrepresentative
- dpv_risk_owl:DataUnrepresentative
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataUnrepresentative

```
</details>

### Induced

<details>
```yaml
name: DataUnrepresentative
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataUnrepresentative
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing data being unrepresentative
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Unrepresentative
exact_mappings:
- dpv_risk:DataUnrepresentative
- dpv_risk_owl:DataUnrepresentative
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataUnrepresentative

```
</details></div>