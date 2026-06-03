---
search:
  boost: 10.0
---

# Class: ResolutionControl 


_Control that aims to resolve an event's effects with the goal of fixing_

_or recovering from it_



<div data-search-exclude markdown="1">



URI: [risk:ResolutionControl](https://w3id.org/lmodel/dpv/risk/ResolutionControl)





```mermaid
 classDiagram
    class ResolutionControl
    click ResolutionControl href "../ResolutionControl/"
      RiskControl <|-- ResolutionControl
        click RiskControl href "../RiskControl/"
      ReactiveControl <|-- ResolutionControl
        click ReactiveControl href "../ReactiveControl/"
      

      ResolutionControl <|-- RecoveryControl
        click RecoveryControl href "../RecoveryControl/"
      ResolutionControl <|-- RemediationControl
        click RemediationControl href "../RemediationControl/"
      ResolutionControl <|-- ReversalControl
        click ReversalControl href "../ReversalControl/"
      

      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ReactiveControl](ReactiveControl.md)
        * **ResolutionControl** [ [RiskControl](RiskControl.md)]
            * [RecoveryControl](RecoveryControl.md) [ [RiskControl](RiskControl.md)]
            * [RemediationControl](RemediationControl.md) [ [RiskControl](RiskControl.md)]
            * [ReversalControl](ReversalControl.md) [ [RiskControl](RiskControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ResolutionControl](https://w3id.org/lmodel/dpv/risk/ResolutionControl) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Resolution Control




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ResolutionControl |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ResolutionControl |
| native | risk:ResolutionControl |
| exact | dpv_risk:ResolutionControl, dpv_risk_owl:ResolutionControl |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ResolutionControl
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ResolutionControl
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that aims to resolve an event''s effects with the goal of fixing

  or recovering from it'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Resolution Control
exact_mappings:
- dpv_risk:ResolutionControl
- dpv_risk_owl:ResolutionControl
is_a: ReactiveControl
mixins:
- RiskControl
class_uri: risk:ResolutionControl

```
</details>

### Induced

<details>
```yaml
name: ResolutionControl
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ResolutionControl
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that aims to resolve an event''s effects with the goal of fixing

  or recovering from it'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Resolution Control
exact_mappings:
- dpv_risk:ResolutionControl
- dpv_risk_owl:ResolutionControl
is_a: ReactiveControl
mixins:
- RiskControl
class_uri: risk:ResolutionControl

```
</details></div>