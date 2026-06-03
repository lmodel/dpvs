---
search:
  boost: 10.0
---

# Class: ViolatingCodeOfConduct 


_Concept representing Violation of Code of Conduct_



<div data-search-exclude markdown="1">



URI: [risk:ViolatingCodeOfConduct](https://w3id.org/lmodel/dpv/risk/ViolatingCodeOfConduct)





```mermaid
 classDiagram
    class ViolatingCodeOfConduct
    click ViolatingCodeOfConduct href "../ViolatingCodeOfConduct/"
      PotentialConsequence <|-- ViolatingCodeOfConduct
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- ViolatingCodeOfConduct
        click PotentialRisk href "../PotentialRisk/"
      PolicyRisk <|-- ViolatingCodeOfConduct
        click PolicyRisk href "../PolicyRisk/"
      
      
```





## Inheritance
* [LegalRiskConcept](LegalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [PolicyRisk](PolicyRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **ViolatingCodeOfConduct** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ViolatingCodeOfConduct](https://w3id.org/lmodel/dpv/risk/ViolatingCodeOfConduct) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Violating Code of Conduct


## Comments

* This concept was called "ViolationCodeConduct" in DPV 2.0



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ViolatingCodeOfConduct |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ViolatingCodeOfConduct |
| native | risk:ViolatingCodeOfConduct |
| exact | dpv_risk:ViolatingCodeOfConduct, dpv_risk_owl:ViolatingCodeOfConduct |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ViolatingCodeOfConduct
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ViolatingCodeOfConduct
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Violation of Code of Conduct
comments:
- This concept was called "ViolationCodeConduct" in DPV 2.0
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Violating Code of Conduct
exact_mappings:
- dpv_risk:ViolatingCodeOfConduct
- dpv_risk_owl:ViolatingCodeOfConduct
is_a: PolicyRisk
mixins:
- PotentialConsequence
- PotentialRisk
class_uri: risk:ViolatingCodeOfConduct

```
</details>

### Induced

<details>
```yaml
name: ViolatingCodeOfConduct
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ViolatingCodeOfConduct
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Violation of Code of Conduct
comments:
- This concept was called "ViolationCodeConduct" in DPV 2.0
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Violating Code of Conduct
exact_mappings:
- dpv_risk:ViolatingCodeOfConduct
- dpv_risk_owl:ViolatingCodeOfConduct
is_a: PolicyRisk
mixins:
- PotentialConsequence
- PotentialRisk
class_uri: risk:ViolatingCodeOfConduct

```
</details></div>