---
search:
  boost: 10.0
---

# Class: ViolatingPolicy 


_Concept representing violation of policy which can be either internal or_

_external policy_



<div data-search-exclude markdown="1">



URI: [risk:ViolatingPolicy](https://w3id.org/lmodel/dpv/risk/ViolatingPolicy)





```mermaid
 classDiagram
    class ViolatingPolicy
    click ViolatingPolicy href "../ViolatingPolicy/"
      PotentialConsequence <|-- ViolatingPolicy
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- ViolatingPolicy
        click PotentialRisk href "../PotentialRisk/"
      PolicyRisk <|-- ViolatingPolicy
        click PolicyRisk href "../PolicyRisk/"
      
      
```





## Inheritance
* [LegalRiskConcept](LegalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [PolicyRisk](PolicyRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **ViolatingPolicy** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ViolatingPolicy](https://w3id.org/lmodel/dpv/risk/ViolatingPolicy) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Violating Policy




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ViolatingPolicy |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ViolatingPolicy |
| native | risk:ViolatingPolicy |
| exact | dpv_risk:ViolatingPolicy, dpv_risk_owl:ViolatingPolicy |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ViolatingPolicy
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ViolatingPolicy
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing violation of policy which can be either internal
  or

  external policy'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Violating Policy
exact_mappings:
- dpv_risk:ViolatingPolicy
- dpv_risk_owl:ViolatingPolicy
is_a: PolicyRisk
mixins:
- PotentialConsequence
- PotentialRisk
class_uri: risk:ViolatingPolicy

```
</details>

### Induced

<details>
```yaml
name: ViolatingPolicy
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ViolatingPolicy
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing violation of policy which can be either internal
  or

  external policy'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Violating Policy
exact_mappings:
- dpv_risk:ViolatingPolicy
- dpv_risk_owl:ViolatingPolicy
is_a: PolicyRisk
mixins:
- PotentialConsequence
- PotentialRisk
class_uri: risk:ViolatingPolicy

```
</details></div>