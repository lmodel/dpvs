---
search:
  boost: 10.0
---

# Class: DataInconsistent 


_Concept representing data being inconsistent_



<div data-search-exclude markdown="1">



URI: [risk:DataInconsistent](https://w3id.org/lmodel/dpv/risk/DataInconsistent)





```mermaid
 classDiagram
    class DataInconsistent
    click DataInconsistent href "../DataInconsistent/"
      PotentialConsequence <|-- DataInconsistent
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataInconsistent
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataInconsistent
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataRisk <|-- DataInconsistent
        click DataRisk href "../DataRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [DataRisk](DataRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **DataInconsistent** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataInconsistent](https://w3id.org/lmodel/dpv/risk/DataInconsistent) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data Inconsistent




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataInconsistent |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataInconsistent |
| native | risk:DataInconsistent |
| exact | dpv_risk:DataInconsistent, dpv_risk_owl:DataInconsistent |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataInconsistent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataInconsistent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing data being inconsistent
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Inconsistent
exact_mappings:
- dpv_risk:DataInconsistent
- dpv_risk_owl:DataInconsistent
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataInconsistent

```
</details>

### Induced

<details>
```yaml
name: DataInconsistent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataInconsistent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing data being inconsistent
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Inconsistent
exact_mappings:
- dpv_risk:DataInconsistent
- dpv_risk_owl:DataInconsistent
is_a: DataRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataInconsistent

```
</details></div>