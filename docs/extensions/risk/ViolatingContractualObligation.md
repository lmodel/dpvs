---
search:
  boost: 10.0
---

# Class: ViolatingContractualObligation 


_Concept representing Violation of Contractual Obligations_



<div data-search-exclude markdown="1">



URI: [risk:ViolatingContractualObligation](https://w3id.org/lmodel/dpv/risk/ViolatingContractualObligation)





```mermaid
 classDiagram
    class ViolatingContractualObligation
    click ViolatingContractualObligation href "../ViolatingContractualObligation/"
      PotentialConsequence <|-- ViolatingContractualObligation
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- ViolatingContractualObligation
        click PotentialRisk href "../PotentialRisk/"
      ViolatingObligation <|-- ViolatingContractualObligation
        click ViolatingObligation href "../ViolatingObligation/"
      LegalComplianceRisk <|-- ViolatingContractualObligation
        click LegalComplianceRisk href "../LegalComplianceRisk/"
      
      
```





## Inheritance
* [LegalRiskConcept](LegalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [LegalComplianceRisk](LegalComplianceRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **ViolatingContractualObligation** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [ViolatingObligation](ViolatingObligation.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ViolatingContractualObligation](https://w3id.org/lmodel/dpv/risk/ViolatingContractualObligation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Violating Contractual Obligation


## Comments

* This concept was called "ViolationContractualObligations" in DPV 2.0



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ViolatingContractualObligation |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ViolatingContractualObligation |
| native | risk:ViolatingContractualObligation |
| exact | dpv_risk:ViolatingContractualObligation, dpv_risk_owl:ViolatingContractualObligation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ViolatingContractualObligation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ViolatingContractualObligation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Violation of Contractual Obligations
comments:
- This concept was called "ViolationContractualObligations" in DPV 2.0
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Violating Contractual Obligation
exact_mappings:
- dpv_risk:ViolatingContractualObligation
- dpv_risk_owl:ViolatingContractualObligation
is_a: LegalComplianceRisk
mixins:
- PotentialConsequence
- PotentialRisk
- ViolatingObligation
class_uri: risk:ViolatingContractualObligation

```
</details>

### Induced

<details>
```yaml
name: ViolatingContractualObligation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ViolatingContractualObligation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Violation of Contractual Obligations
comments:
- This concept was called "ViolationContractualObligations" in DPV 2.0
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Violating Contractual Obligation
exact_mappings:
- dpv_risk:ViolatingContractualObligation
- dpv_risk_owl:ViolatingContractualObligation
is_a: LegalComplianceRisk
mixins:
- PotentialConsequence
- PotentialRisk
- ViolatingObligation
class_uri: risk:ViolatingContractualObligation

```
</details></div>