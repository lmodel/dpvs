---
search:
  boost: 10.0
---

# Class: ViolatingLegalObligation 


_Concept representing Violation of Legal Obligations_



<div data-search-exclude markdown="1">



URI: [risk:ViolatingLegalObligation](https://w3id.org/lmodel/dpv/risk/ViolatingLegalObligation)





```mermaid
 classDiagram
    class ViolatingLegalObligation
    click ViolatingLegalObligation href "../ViolatingLegalObligation/"
      PotentialConsequence <|-- ViolatingLegalObligation
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- ViolatingLegalObligation
        click PotentialRisk href "../PotentialRisk/"
      ViolatingObligation <|-- ViolatingLegalObligation
        click ViolatingObligation href "../ViolatingObligation/"
      LegalComplianceRisk <|-- ViolatingLegalObligation
        click LegalComplianceRisk href "../LegalComplianceRisk/"
      
      
```





## Inheritance
* [LegalRiskConcept](LegalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [LegalComplianceRisk](LegalComplianceRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **ViolatingLegalObligation** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [ViolatingObligation](ViolatingObligation.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ViolatingLegalObligation](https://w3id.org/lmodel/dpv/risk/ViolatingLegalObligation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Violating Legal Obligation


## Comments

* This concept was called "ViolationRegulatoryObligations" in DPV 2.0



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ViolatingLegalObligation |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ViolatingLegalObligation |
| native | risk:ViolatingLegalObligation |
| exact | dpv_risk:ViolatingLegalObligation, dpv_risk_owl:ViolatingLegalObligation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ViolatingLegalObligation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ViolatingLegalObligation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Violation of Legal Obligations
comments:
- This concept was called "ViolationRegulatoryObligations" in DPV 2.0
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Violating Legal Obligation
exact_mappings:
- dpv_risk:ViolatingLegalObligation
- dpv_risk_owl:ViolatingLegalObligation
is_a: LegalComplianceRisk
mixins:
- PotentialConsequence
- PotentialRisk
- ViolatingObligation
class_uri: risk:ViolatingLegalObligation

```
</details>

### Induced

<details>
```yaml
name: ViolatingLegalObligation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ViolatingLegalObligation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Violation of Legal Obligations
comments:
- This concept was called "ViolationRegulatoryObligations" in DPV 2.0
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Violating Legal Obligation
exact_mappings:
- dpv_risk:ViolatingLegalObligation
- dpv_risk_owl:ViolatingLegalObligation
is_a: LegalComplianceRisk
mixins:
- PotentialConsequence
- PotentialRisk
- ViolatingObligation
class_uri: risk:ViolatingLegalObligation

```
</details></div>