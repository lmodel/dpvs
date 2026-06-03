---
search:
  boost: 10.0
---

# Class: RiskAcceptance 


_Entity decision to accept or enable a particular risk_



<div data-search-exclude markdown="1">



URI: [risk:RiskAcceptance](https://w3id.org/lmodel/dpv/risk/RiskAcceptance)





```mermaid
 classDiagram
    class RiskAcceptance
    click RiskAcceptance href "../RiskAcceptance/"
      RiskManagement <|-- RiskAcceptance
        click RiskManagement href "../RiskManagement/"
      
      
```





## Inheritance
* [RiskManagement](RiskManagement.md)
    * **RiskAcceptance**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RiskAcceptance](https://w3id.org/lmodel/dpv/risk/RiskAcceptance) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Risk Acceptance




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RiskAcceptance |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RiskAcceptance |
| native | risk:RiskAcceptance |
| exact | dpv_risk:RiskAcceptance, dpv_risk_owl:RiskAcceptance |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RiskAcceptance
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RiskAcceptance
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Entity decision to accept or enable a particular risk
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Risk Acceptance
exact_mappings:
- dpv_risk:RiskAcceptance
- dpv_risk_owl:RiskAcceptance
is_a: RiskManagement
class_uri: risk:RiskAcceptance

```
</details>

### Induced

<details>
```yaml
name: RiskAcceptance
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RiskAcceptance
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Entity decision to accept or enable a particular risk
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Risk Acceptance
exact_mappings:
- dpv_risk:RiskAcceptance
- dpv_risk_owl:RiskAcceptance
is_a: RiskManagement
class_uri: risk:RiskAcceptance

```
</details></div>