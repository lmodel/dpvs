---
search:
  boost: 10.0
---

# Class: OverrideControl 


_Control that aims to override the event with the goal of avoiding its_

_further effects_



<div data-search-exclude markdown="1">



URI: [risk:OverrideControl](https://w3id.org/lmodel/dpv/risk/OverrideControl)





```mermaid
 classDiagram
    class OverrideControl
    click OverrideControl href "../OverrideControl/"
      RiskControl <|-- OverrideControl
        click RiskControl href "../RiskControl/"
      ReactiveControl <|-- OverrideControl
        click ReactiveControl href "../ReactiveControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ReactiveControl](ReactiveControl.md)
        * **OverrideControl** [ [RiskControl](RiskControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:OverrideControl](https://w3id.org/lmodel/dpv/risk/OverrideControl) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Override Control


## Comments

* Override indicates a (temporary) change or bypassing of usual processes,
controls, and measures in response to an event



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#OverrideControl |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:OverrideControl |
| native | risk:OverrideControl |
| exact | dpv_risk:OverrideControl, dpv_risk_owl:OverrideControl |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OverrideControl
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#OverrideControl
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that aims to override the event with the goal of avoiding its

  further effects'
comments:
- 'Override indicates a (temporary) change or bypassing of usual processes,

  controls, and measures in response to an event'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Override Control
exact_mappings:
- dpv_risk:OverrideControl
- dpv_risk_owl:OverrideControl
is_a: ReactiveControl
mixins:
- RiskControl
class_uri: risk:OverrideControl

```
</details>

### Induced

<details>
```yaml
name: OverrideControl
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#OverrideControl
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that aims to override the event with the goal of avoiding its

  further effects'
comments:
- 'Override indicates a (temporary) change or bypassing of usual processes,

  controls, and measures in response to an event'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Override Control
exact_mappings:
- dpv_risk:OverrideControl
- dpv_risk_owl:OverrideControl
is_a: ReactiveControl
mixins:
- RiskControl
class_uri: risk:OverrideControl

```
</details></div>