---
search:
  boost: 10.0
---

# Class: RecoveryControl 


_Control that aims to restore the context following an event_



<div data-search-exclude markdown="1">



URI: [risk:RecoveryControl](https://w3id.org/lmodel/dpv/risk/RecoveryControl)





```mermaid
 classDiagram
    class RecoveryControl
    click RecoveryControl href "../RecoveryControl/"
      RiskControl <|-- RecoveryControl
        click RiskControl href "../RiskControl/"
      ResolutionControl <|-- RecoveryControl
        click ResolutionControl href "../ResolutionControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ReactiveControl](ReactiveControl.md)
        * [ResolutionControl](ResolutionControl.md) [ [RiskControl](RiskControl.md)]
            * **RecoveryControl** [ [RiskControl](RiskControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RecoveryControl](https://w3id.org/lmodel/dpv/risk/RecoveryControl) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Recovery Control


## Comments

* Recovery implies taking steps to correct the effects which may not be
the same as the initial conditions before the event, whereas
risk:ReversalControl refers to undoing the effects such that the initial
condition is restored



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RecoveryControl |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RecoveryControl |
| native | risk:RecoveryControl |
| exact | dpv_risk:RecoveryControl, dpv_risk_owl:RecoveryControl |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RecoveryControl
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RecoveryControl
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Control that aims to restore the context following an event
comments:
- 'Recovery implies taking steps to correct the effects which may not be

  the same as the initial conditions before the event, whereas

  risk:ReversalControl refers to undoing the effects such that the initial

  condition is restored'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Recovery Control
exact_mappings:
- dpv_risk:RecoveryControl
- dpv_risk_owl:RecoveryControl
is_a: ResolutionControl
mixins:
- RiskControl
class_uri: risk:RecoveryControl

```
</details>

### Induced

<details>
```yaml
name: RecoveryControl
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RecoveryControl
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Control that aims to restore the context following an event
comments:
- 'Recovery implies taking steps to correct the effects which may not be

  the same as the initial conditions before the event, whereas

  risk:ReversalControl refers to undoing the effects such that the initial

  condition is restored'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Recovery Control
exact_mappings:
- dpv_risk:RecoveryControl
- dpv_risk_owl:RecoveryControl
is_a: ResolutionControl
mixins:
- RiskControl
class_uri: risk:RecoveryControl

```
</details></div>