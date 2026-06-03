---
search:
  boost: 10.0
---

# Class: LegalComplianceRisk 


_Risks and consequences regarding legal compliance and its violation_



<div data-search-exclude markdown="1">



URI: [risk:LegalComplianceRisk](https://w3id.org/lmodel/dpv/risk/LegalComplianceRisk)





```mermaid
 classDiagram
    class LegalComplianceRisk
    click LegalComplianceRisk href "../LegalComplianceRisk/"
      PotentialConsequence <|-- LegalComplianceRisk
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- LegalComplianceRisk
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- LegalComplianceRisk
        click PotentialRiskSource href "../PotentialRiskSource/"
      LegalRiskConcept <|-- LegalComplianceRisk
        click LegalRiskConcept href "../LegalRiskConcept/"
      

      LegalComplianceRisk <|-- CopyrightViolation
        click CopyrightViolation href "../CopyrightViolation/"
      LegalComplianceRisk <|-- IllegalDataProcessing
        click IllegalDataProcessing href "../IllegalDataProcessing/"
      LegalComplianceRisk <|-- PublicOrderBreach
        click PublicOrderBreach href "../PublicOrderBreach/"
      LegalComplianceRisk <|-- ViolatingContractualObligation
        click ViolatingContractualObligation href "../ViolatingContractualObligation/"
      LegalComplianceRisk <|-- ViolatingLegalObligation
        click ViolatingLegalObligation href "../ViolatingLegalObligation/"
      LegalComplianceRisk <|-- ViolatingStatutoryObligations
        click ViolatingStatutoryObligations href "../ViolatingStatutoryObligations/"
      

      
```





## Inheritance
* [LegalRiskConcept](LegalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * **LegalComplianceRisk** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [CopyrightViolation](CopyrightViolation.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [ViolatingObligation](ViolatingObligation.md)]
        * [IllegalDataProcessing](IllegalDataProcessing.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md)]
        * [PublicOrderBreach](PublicOrderBreach.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md)]
        * [ViolatingContractualObligation](ViolatingContractualObligation.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [ViolatingObligation](ViolatingObligation.md)]
        * [ViolatingLegalObligation](ViolatingLegalObligation.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [ViolatingObligation](ViolatingObligation.md)]
        * [ViolatingStatutoryObligations](ViolatingStatutoryObligations.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [ViolatingObligation](ViolatingObligation.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:LegalComplianceRisk](https://w3id.org/lmodel/dpv/risk/LegalComplianceRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Legal Compliance Risk




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#LegalComplianceRisk |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:LegalComplianceRisk |
| native | risk:LegalComplianceRisk |
| exact | dpv_risk:LegalComplianceRisk, dpv_risk_owl:LegalComplianceRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LegalComplianceRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#LegalComplianceRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Risks and consequences regarding legal compliance and its violation
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Legal Compliance Risk
exact_mappings:
- dpv_risk:LegalComplianceRisk
- dpv_risk_owl:LegalComplianceRisk
is_a: LegalRiskConcept
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:LegalComplianceRisk

```
</details>

### Induced

<details>
```yaml
name: LegalComplianceRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#LegalComplianceRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Risks and consequences regarding legal compliance and its violation
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Legal Compliance Risk
exact_mappings:
- dpv_risk:LegalComplianceRisk
- dpv_risk_owl:LegalComplianceRisk
is_a: LegalRiskConcept
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:LegalComplianceRisk

```
</details></div>