---
search:
  boost: 10.0
---

# Class: CopyrightViolation 


_Concept representing Copyright Violation_



<div data-search-exclude markdown="1">



URI: [risk:CopyrightViolation](https://w3id.org/lmodel/dpv/risk/CopyrightViolation)





```mermaid
 classDiagram
    class CopyrightViolation
    click CopyrightViolation href "../CopyrightViolation/"
      PotentialConsequence <|-- CopyrightViolation
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- CopyrightViolation
        click PotentialRisk href "../PotentialRisk/"
      ViolatingObligation <|-- CopyrightViolation
        click ViolatingObligation href "../ViolatingObligation/"
      LegalComplianceRisk <|-- CopyrightViolation
        click LegalComplianceRisk href "../LegalComplianceRisk/"
      
      
```





## Inheritance
* [LegalRiskConcept](LegalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [LegalComplianceRisk](LegalComplianceRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **CopyrightViolation** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [ViolatingObligation](ViolatingObligation.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:CopyrightViolation](https://w3id.org/lmodel/dpv/risk/CopyrightViolation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Copyright Violation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#CopyrightViolation |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:CopyrightViolation |
| native | risk:CopyrightViolation |
| exact | dpv_risk:CopyrightViolation, dpv_risk_owl:CopyrightViolation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CopyrightViolation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#CopyrightViolation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Copyright Violation
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Copyright Violation
exact_mappings:
- dpv_risk:CopyrightViolation
- dpv_risk_owl:CopyrightViolation
is_a: LegalComplianceRisk
mixins:
- PotentialConsequence
- PotentialRisk
- ViolatingObligation
class_uri: risk:CopyrightViolation

```
</details>

### Induced

<details>
```yaml
name: CopyrightViolation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#CopyrightViolation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Copyright Violation
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Copyright Violation
exact_mappings:
- dpv_risk:CopyrightViolation
- dpv_risk_owl:CopyrightViolation
is_a: LegalComplianceRisk
mixins:
- PotentialConsequence
- PotentialRisk
- ViolatingObligation
class_uri: risk:CopyrightViolation

```
</details></div>