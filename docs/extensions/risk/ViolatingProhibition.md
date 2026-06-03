---
search:
  boost: 10.0
---

# Class: ViolatingProhibition 


_Something that acts as a or violates a prohibition - e.g. in a law, code_

_of conduct, policy, contract_



<div data-search-exclude markdown="1">



URI: [risk:ViolatingProhibition](https://w3id.org/lmodel/dpv/risk/ViolatingProhibition)





```mermaid
 classDiagram
    class ViolatingProhibition
    click ViolatingProhibition href "../ViolatingProhibition/"
      PotentialConsequence <|-- ViolatingProhibition
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- ViolatingProhibition
        click PotentialRisk href "../PotentialRisk/"
      PolicyRisk <|-- ViolatingProhibition
        click PolicyRisk href "../PolicyRisk/"
      
      
```





## Inheritance
* [LegalRiskConcept](LegalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [PolicyRisk](PolicyRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **ViolatingProhibition** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ViolatingProhibition](https://w3id.org/lmodel/dpv/risk/ViolatingProhibition) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Violating Prohibition




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ViolatingProhibition |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ViolatingProhibition |
| native | risk:ViolatingProhibition |
| exact | dpv_risk:ViolatingProhibition, dpv_risk_owl:ViolatingProhibition |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ViolatingProhibition
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ViolatingProhibition
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Something that acts as a or violates a prohibition - e.g. in a law,
  code

  of conduct, policy, contract'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Violating Prohibition
exact_mappings:
- dpv_risk:ViolatingProhibition
- dpv_risk_owl:ViolatingProhibition
is_a: PolicyRisk
mixins:
- PotentialConsequence
- PotentialRisk
class_uri: risk:ViolatingProhibition

```
</details>

### Induced

<details>
```yaml
name: ViolatingProhibition
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ViolatingProhibition
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Something that acts as a or violates a prohibition - e.g. in a law,
  code

  of conduct, policy, contract'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Violating Prohibition
exact_mappings:
- dpv_risk:ViolatingProhibition
- dpv_risk_owl:ViolatingProhibition
is_a: PolicyRisk
mixins:
- PotentialConsequence
- PotentialRisk
class_uri: risk:ViolatingProhibition

```
</details></div>