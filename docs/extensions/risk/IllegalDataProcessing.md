---
search:
  boost: 10.0
---

# Class: IllegalDataProcessing 


_Concept representing Illegal Processing of Data_



<div data-search-exclude markdown="1">



URI: [risk:IllegalDataProcessing](https://w3id.org/lmodel/dpv/risk/IllegalDataProcessing)





```mermaid
 classDiagram
    class IllegalDataProcessing
    click IllegalDataProcessing href "../IllegalDataProcessing/"
      PotentialConsequence <|-- IllegalDataProcessing
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- IllegalDataProcessing
        click PotentialRisk href "../PotentialRisk/"
      LegalComplianceRisk <|-- IllegalDataProcessing
        click LegalComplianceRisk href "../LegalComplianceRisk/"
      
      
```





## Inheritance
* [LegalRiskConcept](LegalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [LegalComplianceRisk](LegalComplianceRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **IllegalDataProcessing** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IllegalDataProcessing](https://w3id.org/lmodel/dpv/risk/IllegalDataProcessing) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Illegal Data Processing


## Comments

* This concept was called "IllegalProcessingData" in DPV 2.0



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IllegalDataProcessing |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IllegalDataProcessing |
| native | risk:IllegalDataProcessing |
| exact | dpv_risk:IllegalDataProcessing, dpv_risk_owl:IllegalDataProcessing |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IllegalDataProcessing
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IllegalDataProcessing
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Illegal Processing of Data
comments:
- This concept was called "IllegalProcessingData" in DPV 2.0
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Illegal Data Processing
exact_mappings:
- dpv_risk:IllegalDataProcessing
- dpv_risk_owl:IllegalDataProcessing
is_a: LegalComplianceRisk
mixins:
- PotentialConsequence
- PotentialRisk
class_uri: risk:IllegalDataProcessing

```
</details>

### Induced

<details>
```yaml
name: IllegalDataProcessing
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IllegalDataProcessing
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Illegal Processing of Data
comments:
- This concept was called "IllegalProcessingData" in DPV 2.0
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Illegal Data Processing
exact_mappings:
- dpv_risk:IllegalDataProcessing
- dpv_risk_owl:IllegalDataProcessing
is_a: LegalComplianceRisk
mixins:
- PotentialConsequence
- PotentialRisk
class_uri: risk:IllegalDataProcessing

```
</details></div>