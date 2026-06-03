---
search:
  boost: 10.0
---

# Class: ViolatingObligation 


_Something that acts as a or violates an obligation - e.g. in a law, code_

_of conduct, policy, contract_



<div data-search-exclude markdown="1">



URI: [risk:ViolatingObligation](https://w3id.org/lmodel/dpv/risk/ViolatingObligation)





```mermaid
 classDiagram
    class ViolatingObligation
    click ViolatingObligation href "../ViolatingObligation/"
      PotentialConsequence <|-- ViolatingObligation
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- ViolatingObligation
        click PotentialRisk href "../PotentialRisk/"
      PolicyRisk <|-- ViolatingObligation
        click PolicyRisk href "../PolicyRisk/"
      

      ViolatingObligation <|-- CopyrightViolation
        click CopyrightViolation href "../CopyrightViolation/"
      ViolatingObligation <|-- ViolatingContractualObligation
        click ViolatingContractualObligation href "../ViolatingContractualObligation/"
      ViolatingObligation <|-- ViolatingLegalObligation
        click ViolatingLegalObligation href "../ViolatingLegalObligation/"
      ViolatingObligation <|-- ViolatingStatutoryObligations
        click ViolatingStatutoryObligations href "../ViolatingStatutoryObligations/"
      

      
```





## Inheritance
* [LegalRiskConcept](LegalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [PolicyRisk](PolicyRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **ViolatingObligation** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ViolatingObligation](https://w3id.org/lmodel/dpv/risk/ViolatingObligation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Violating Obligation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ViolatingObligation |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ViolatingObligation |
| native | risk:ViolatingObligation |
| exact | dpv_risk:ViolatingObligation, dpv_risk_owl:ViolatingObligation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ViolatingObligation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ViolatingObligation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Something that acts as a or violates an obligation - e.g. in a law,
  code

  of conduct, policy, contract'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Violating Obligation
exact_mappings:
- dpv_risk:ViolatingObligation
- dpv_risk_owl:ViolatingObligation
is_a: PolicyRisk
mixins:
- PotentialConsequence
- PotentialRisk
class_uri: risk:ViolatingObligation

```
</details>

### Induced

<details>
```yaml
name: ViolatingObligation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ViolatingObligation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Something that acts as a or violates an obligation - e.g. in a law,
  code

  of conduct, policy, contract'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Violating Obligation
exact_mappings:
- dpv_risk:ViolatingObligation
- dpv_risk_owl:ViolatingObligation
is_a: PolicyRisk
mixins:
- PotentialConsequence
- PotentialRisk
class_uri: risk:ViolatingObligation

```
</details></div>