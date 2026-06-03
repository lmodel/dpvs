---
search:
  boost: 10.0
---

# Class: OversightControl 


_Control that provides oversight for an event in terms of having_

_information about it and being able to supervise or manage it_



<div data-search-exclude markdown="1">



URI: [risk:OversightControl](https://w3id.org/lmodel/dpv/risk/OversightControl)





```mermaid
 classDiagram
    class OversightControl
    click OversightControl href "../OversightControl/"
      RiskControl <|-- OversightControl
        click RiskControl href "../RiskControl/"
      MonitorControl <|-- OversightControl
        click MonitorControl href "../MonitorControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ProactiveControl](ProactiveControl.md)
        * [MonitorControl](MonitorControl.md) [ [RiskControl](RiskControl.md)]
            * **OversightControl** [ [RiskControl](RiskControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:OversightControl](https://w3id.org/lmodel/dpv/risk/OversightControl) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Oversight Control


## Comments

* Oversight can be ambiguously used in terms of having knowledge about an
event (see risk:TransparencyControl instead), or being able to identify
when it occurs (see risk:DetectionControl instead). The control defined
by this concept includes the ability to act on the event as part of the
'oversight' term used in management



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#OversightControl |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:OversightControl |
| native | risk:OversightControl |
| exact | dpv_risk:OversightControl, dpv_risk_owl:OversightControl |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OversightControl
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#OversightControl
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that provides oversight for an event in terms of having

  information about it and being able to supervise or manage it'
comments:
- 'Oversight can be ambiguously used in terms of having knowledge about an

  event (see risk:TransparencyControl instead), or being able to identify

  when it occurs (see risk:DetectionControl instead). The control defined

  by this concept includes the ability to act on the event as part of the

  ''oversight'' term used in management'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Oversight Control
exact_mappings:
- dpv_risk:OversightControl
- dpv_risk_owl:OversightControl
is_a: MonitorControl
mixins:
- RiskControl
class_uri: risk:OversightControl

```
</details>

### Induced

<details>
```yaml
name: OversightControl
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#OversightControl
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that provides oversight for an event in terms of having

  information about it and being able to supervise or manage it'
comments:
- 'Oversight can be ambiguously used in terms of having knowledge about an

  event (see risk:TransparencyControl instead), or being able to identify

  when it occurs (see risk:DetectionControl instead). The control defined

  by this concept includes the ability to act on the event as part of the

  ''oversight'' term used in management'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Oversight Control
exact_mappings:
- dpv_risk:OversightControl
- dpv_risk_owl:OversightControl
is_a: MonitorControl
mixins:
- RiskControl
class_uri: risk:OversightControl

```
</details></div>