---
search:
  boost: 10.0
---

# Class: ViolatingStatutoryObligations 


_Concept representing Violation of Statutory Obligations_



<div data-search-exclude markdown="1">



URI: [risk:ViolatingStatutoryObligations](https://w3id.org/lmodel/dpv/risk/ViolatingStatutoryObligations)





```mermaid
 classDiagram
    class ViolatingStatutoryObligations
    click ViolatingStatutoryObligations href "../ViolatingStatutoryObligations/"
      PotentialConsequence <|-- ViolatingStatutoryObligations
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- ViolatingStatutoryObligations
        click PotentialRisk href "../PotentialRisk/"
      ViolatingObligation <|-- ViolatingStatutoryObligations
        click ViolatingObligation href "../ViolatingObligation/"
      LegalComplianceRisk <|-- ViolatingStatutoryObligations
        click LegalComplianceRisk href "../LegalComplianceRisk/"
      
      
```





## Inheritance
* [LegalRiskConcept](LegalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [LegalComplianceRisk](LegalComplianceRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **ViolatingStatutoryObligations** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [ViolatingObligation](ViolatingObligation.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ViolatingStatutoryObligations](https://w3id.org/lmodel/dpv/risk/ViolatingStatutoryObligations) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Violating Statutory Obligations


## Comments

* This concept was called "ViolationStatutoryObligations" in DPV 2.0



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ViolatingStatutoryObligations |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ViolatingStatutoryObligations |
| native | risk:ViolatingStatutoryObligations |
| exact | dpv_risk:ViolatingStatutoryObligations, dpv_risk_owl:ViolatingStatutoryObligations |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ViolatingStatutoryObligations
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ViolatingStatutoryObligations
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Violation of Statutory Obligations
comments:
- This concept was called "ViolationStatutoryObligations" in DPV 2.0
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Violating Statutory Obligations
exact_mappings:
- dpv_risk:ViolatingStatutoryObligations
- dpv_risk_owl:ViolatingStatutoryObligations
is_a: LegalComplianceRisk
mixins:
- PotentialConsequence
- PotentialRisk
- ViolatingObligation
class_uri: risk:ViolatingStatutoryObligations

```
</details>

### Induced

<details>
```yaml
name: ViolatingStatutoryObligations
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ViolatingStatutoryObligations
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Violation of Statutory Obligations
comments:
- This concept was called "ViolationStatutoryObligations" in DPV 2.0
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Violating Statutory Obligations
exact_mappings:
- dpv_risk:ViolatingStatutoryObligations
- dpv_risk_owl:ViolatingStatutoryObligations
is_a: LegalComplianceRisk
mixins:
- PotentialConsequence
- PotentialRisk
- ViolatingObligation
class_uri: risk:ViolatingStatutoryObligations

```
</details></div>