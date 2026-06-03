---
search:
  boost: 10.0
---

# Class: ViolatingEthicsCode 


_Concept representing Violation of Ethics Code_



<div data-search-exclude markdown="1">



URI: [risk:ViolatingEthicsCode](https://w3id.org/lmodel/dpv/risk/ViolatingEthicsCode)





```mermaid
 classDiagram
    class ViolatingEthicsCode
    click ViolatingEthicsCode href "../ViolatingEthicsCode/"
      PotentialConsequence <|-- ViolatingEthicsCode
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- ViolatingEthicsCode
        click PotentialRisk href "../PotentialRisk/"
      PolicyRisk <|-- ViolatingEthicsCode
        click PolicyRisk href "../PolicyRisk/"
      
      
```





## Inheritance
* [LegalRiskConcept](LegalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [PolicyRisk](PolicyRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **ViolatingEthicsCode** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ViolatingEthicsCode](https://w3id.org/lmodel/dpv/risk/ViolatingEthicsCode) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Violating Ethics Code


## Comments

* This concept was called "ViolationEthicalCode" in DPV 2.0



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ViolatingEthicsCode |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ViolatingEthicsCode |
| native | risk:ViolatingEthicsCode |
| exact | dpv_risk:ViolatingEthicsCode, dpv_risk_owl:ViolatingEthicsCode |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ViolatingEthicsCode
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ViolatingEthicsCode
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Violation of Ethics Code
comments:
- This concept was called "ViolationEthicalCode" in DPV 2.0
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Violating Ethics Code
exact_mappings:
- dpv_risk:ViolatingEthicsCode
- dpv_risk_owl:ViolatingEthicsCode
is_a: PolicyRisk
mixins:
- PotentialConsequence
- PotentialRisk
class_uri: risk:ViolatingEthicsCode

```
</details>

### Induced

<details>
```yaml
name: ViolatingEthicsCode
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ViolatingEthicsCode
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Violation of Ethics Code
comments:
- This concept was called "ViolationEthicalCode" in DPV 2.0
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Violating Ethics Code
exact_mappings:
- dpv_risk:ViolatingEthicsCode
- dpv_risk_owl:ViolatingEthicsCode
is_a: PolicyRisk
mixins:
- PotentialConsequence
- PotentialRisk
class_uri: risk:ViolatingEthicsCode

```
</details></div>