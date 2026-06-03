---
search:
  boost: 10.0
---

# Class: RightsUnfulfilled 


_Failure to meet or complete the fulfilment of rights_



<div data-search-exclude markdown="1">



URI: [risk:RightsUnfulfilled](https://w3id.org/lmodel/dpv/risk/RightsUnfulfilled)





```mermaid
 classDiagram
    class RightsUnfulfilled
    click RightsUnfulfilled href "../RightsUnfulfilled/"
      PotentialConsequence <|-- RightsUnfulfilled
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- RightsUnfulfilled
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- RightsUnfulfilled
        click PotentialRisk href "../PotentialRisk/"
      RightsImpact <|-- RightsUnfulfilled
        click RightsImpact href "../RightsImpact/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [RightsImpact](RightsImpact.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **RightsUnfulfilled** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RightsUnfulfilled](https://w3id.org/lmodel/dpv/risk/RightsUnfulfilled) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Rights Unfulfilled


## Comments

* Here unfulfilment refers to non-completion of the right's obligations
and processes. Though specified as a plural i.e. 'rights', this concept
can be applied to a singular right



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RightsUnfulfilled |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RightsUnfulfilled |
| native | risk:RightsUnfulfilled |
| exact | dpv_risk:RightsUnfulfilled, dpv_risk_owl:RightsUnfulfilled |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RightsUnfulfilled
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RightsUnfulfilled
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Failure to meet or complete the fulfilment of rights
comments:
- 'Here unfulfilment refers to non-completion of the right''s obligations

  and processes. Though specified as a plural i.e. ''rights'', this concept

  can be applied to a singular right'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Rights Unfulfilled
exact_mappings:
- dpv_risk:RightsUnfulfilled
- dpv_risk_owl:RightsUnfulfilled
is_a: RightsImpact
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:RightsUnfulfilled

```
</details>

### Induced

<details>
```yaml
name: RightsUnfulfilled
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RightsUnfulfilled
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Failure to meet or complete the fulfilment of rights
comments:
- 'Here unfulfilment refers to non-completion of the right''s obligations

  and processes. Though specified as a plural i.e. ''rights'', this concept

  can be applied to a singular right'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Rights Unfulfilled
exact_mappings:
- dpv_risk:RightsUnfulfilled
- dpv_risk_owl:RightsUnfulfilled
is_a: RightsImpact
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:RightsUnfulfilled

```
</details></div>