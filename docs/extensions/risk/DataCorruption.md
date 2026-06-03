---
search:
  boost: 10.0
---

# Class: DataCorruption 


_Concept representing Corruption of Data_



<div data-search-exclude markdown="1">



URI: [risk:DataCorruption](https://w3id.org/lmodel/dpv/risk/DataCorruption)





```mermaid
 classDiagram
    class DataCorruption
    click DataCorruption href "../DataCorruption/"
      IntegrityConcept <|-- DataCorruption
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialConsequence <|-- DataCorruption
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataCorruption
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataCorruption
        click PotentialRiskSource href "../PotentialRiskSource/"
      OperationalSecurityRisk <|-- DataCorruption
        click OperationalSecurityRisk href "../OperationalSecurityRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **DataCorruption** [ [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataCorruption](https://w3id.org/lmodel/dpv/risk/DataCorruption) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data Corruption


## Comments

* This concept was called "Corruption Data" in DPV 2.0



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataCorruption |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataCorruption |
| native | risk:DataCorruption |
| exact | dpv_risk:DataCorruption, dpv_risk_owl:DataCorruption |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataCorruption
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataCorruption
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Corruption of Data
comments:
- This concept was called "Corruption Data" in DPV 2.0
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Corruption
exact_mappings:
- dpv_risk:DataCorruption
- dpv_risk_owl:DataCorruption
is_a: OperationalSecurityRisk
mixins:
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataCorruption

```
</details>

### Induced

<details>
```yaml
name: DataCorruption
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataCorruption
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Corruption of Data
comments:
- This concept was called "Corruption Data" in DPV 2.0
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Corruption
exact_mappings:
- dpv_risk:DataCorruption
- dpv_risk_owl:DataCorruption
is_a: OperationalSecurityRisk
mixins:
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataCorruption

```
</details></div>