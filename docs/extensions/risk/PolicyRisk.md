---
search:
  boost: 10.0
---

# Class: PolicyRisk 


_Risks and consequences regarding policy and its associated processes_



<div data-search-exclude markdown="1">



URI: [risk:PolicyRisk](https://w3id.org/lmodel/dpv/risk/PolicyRisk)





```mermaid
 classDiagram
    class PolicyRisk
    click PolicyRisk href "../PolicyRisk/"
      PotentialConsequence <|-- PolicyRisk
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- PolicyRisk
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- PolicyRisk
        click PotentialRiskSource href "../PotentialRiskSource/"
      LegalRiskConcept <|-- PolicyRisk
        click LegalRiskConcept href "../LegalRiskConcept/"
      

      PolicyRisk <|-- ViolatingCodeOfConduct
        click ViolatingCodeOfConduct href "../ViolatingCodeOfConduct/"
      PolicyRisk <|-- ViolatingEthicsCode
        click ViolatingEthicsCode href "../ViolatingEthicsCode/"
      PolicyRisk <|-- ViolatingObligation
        click ViolatingObligation href "../ViolatingObligation/"
      PolicyRisk <|-- ViolatingPolicy
        click ViolatingPolicy href "../ViolatingPolicy/"
      PolicyRisk <|-- ViolatingProhibition
        click ViolatingProhibition href "../ViolatingProhibition/"
      

      
```





## Inheritance
* [LegalRiskConcept](LegalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * **PolicyRisk** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [ViolatingCodeOfConduct](ViolatingCodeOfConduct.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md)]
        * [ViolatingEthicsCode](ViolatingEthicsCode.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md)]
        * [ViolatingObligation](ViolatingObligation.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md)]
        * [ViolatingPolicy](ViolatingPolicy.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md)]
        * [ViolatingProhibition](ViolatingProhibition.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:PolicyRisk](https://w3id.org/lmodel/dpv/risk/PolicyRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Policy Risk




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#PolicyRisk |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:PolicyRisk |
| native | risk:PolicyRisk |
| exact | dpv_risk:PolicyRisk, dpv_risk_owl:PolicyRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PolicyRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PolicyRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Risks and consequences regarding policy and its associated processes
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Policy Risk
exact_mappings:
- dpv_risk:PolicyRisk
- dpv_risk_owl:PolicyRisk
is_a: LegalRiskConcept
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:PolicyRisk

```
</details>

### Induced

<details>
```yaml
name: PolicyRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PolicyRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Risks and consequences regarding policy and its associated processes
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Policy Risk
exact_mappings:
- dpv_risk:PolicyRisk
- dpv_risk_owl:PolicyRisk
is_a: LegalRiskConcept
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:PolicyRisk

```
</details></div>