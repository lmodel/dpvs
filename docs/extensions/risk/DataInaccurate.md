---
search:
  boost: 10.0
---

# Class: DataInaccurate 


_Concept representing data being inaccurate_



<div data-search-exclude markdown="1">



URI: [risk:DataInaccurate](https://w3id.org/lmodel/dpv/risk/DataInaccurate)





```mermaid
 classDiagram
    class DataInaccurate
    click DataInaccurate href "../DataInaccurate/"
      PotentialConsequence <|-- DataInaccurate
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataInaccurate
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataInaccurate
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataRisk <|-- DataInaccurate
        click DataRisk href "../DataRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [DataRisk](DataRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **DataInaccurate** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataInaccurate](https://w3id.org/lmodel/dpv/risk/DataInaccurate) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data Inaccurate




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataInaccurate |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataInaccurate |
| native | risk:DataInaccurate |
| exact | dpv_risk:DataInaccurate, dpv_risk_owl:DataInaccurate |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataInaccurate
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataInaccurate
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing data being inaccurate
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Inaccurate
exact_mappings:
- dpv_risk:DataInaccurate
- dpv_risk_owl:DataInaccurate
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataInaccurate

```
</details>

### Induced

<details>
```yaml
name: DataInaccurate
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataInaccurate
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing data being inaccurate
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Inaccurate
exact_mappings:
- dpv_risk:DataInaccurate
- dpv_risk_owl:DataInaccurate
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataInaccurate

```
</details></div>