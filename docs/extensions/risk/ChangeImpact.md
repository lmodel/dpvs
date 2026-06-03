---
search:
  boost: 10.0
---

# Class: ChangeImpact 


_Control that proactively changes the impact event such that one event is_

_replaced with the occurrence or applicability of another event in the_

_context_



<div data-search-exclude markdown="1">



URI: [risk:ChangeImpact](https://w3id.org/lmodel/dpv/risk/ChangeImpact)





```mermaid
 classDiagram
    class ChangeImpact
    click ChangeImpact href "../ChangeImpact/"
      RiskControl <|-- ChangeImpact
        click RiskControl href "../RiskControl/"
      SubstitutionControl <|-- ChangeImpact
        click SubstitutionControl href "../SubstitutionControl/"
      ImpactControl <|-- ChangeImpact
        click ImpactControl href "../ImpactControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ImpactControl](ImpactControl.md)
        * **ChangeImpact** [ [RiskControl](RiskControl.md) [SubstitutionControl](SubstitutionControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ChangeImpact](https://w3id.org/lmodel/dpv/risk/ChangeImpact) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Change Impact




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ChangeImpact |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ChangeImpact |
| native | risk:ChangeImpact |
| exact | dpv_risk:ChangeImpact, dpv_risk_owl:ChangeImpact |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ChangeImpact
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ChangeImpact
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that proactively changes the impact event such that one event
  is

  replaced with the occurrence or applicability of another event in the

  context'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Change Impact
exact_mappings:
- dpv_risk:ChangeImpact
- dpv_risk_owl:ChangeImpact
is_a: ImpactControl
mixins:
- RiskControl
- SubstitutionControl
class_uri: risk:ChangeImpact

```
</details>

### Induced

<details>
```yaml
name: ChangeImpact
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ChangeImpact
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that proactively changes the impact event such that one event
  is

  replaced with the occurrence or applicability of another event in the

  context'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Change Impact
exact_mappings:
- dpv_risk:ChangeImpact
- dpv_risk_owl:ChangeImpact
is_a: ImpactControl
mixins:
- RiskControl
- SubstitutionControl
class_uri: risk:ChangeImpact

```
</details></div>