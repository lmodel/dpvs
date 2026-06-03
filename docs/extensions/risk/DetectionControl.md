---
search:
  boost: 10.0
---

# Class: DetectionControl 


_Control that detects an event_



<div data-search-exclude markdown="1">



URI: [risk:DetectionControl](https://w3id.org/lmodel/dpv/risk/DetectionControl)





```mermaid
 classDiagram
    class DetectionControl
    click DetectionControl href "../DetectionControl/"
      RiskControl <|-- DetectionControl
        click RiskControl href "../RiskControl/"
      MonitorControl <|-- DetectionControl
        click MonitorControl href "../MonitorControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ProactiveControl](ProactiveControl.md)
        * [MonitorControl](MonitorControl.md) [ [RiskControl](RiskControl.md)]
            * **DetectionControl** [ [RiskControl](RiskControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DetectionControl](https://w3id.org/lmodel/dpv/risk/DetectionControl) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Detection Control


## Comments

* Detection refers to the observation, derivation, inference, or any other
method for drawing conclusions that an event has occurred or is likely
to occur with a given certainty. For controls that identify information
about the event in terms of metrics or characteristics, see
risk:IdentificationControl



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DetectionControl |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DetectionControl |
| native | risk:DetectionControl |
| exact | dpv_risk:DetectionControl, dpv_risk_owl:DetectionControl |
| close | iso42001:AIReferenceControl |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DetectionControl
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DetectionControl
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Control that detects an event
comments:
- 'Detection refers to the observation, derivation, inference, or any other

  method for drawing conclusions that an event has occurred or is likely

  to occur with a given certainty. For controls that identify information

  about the event in terms of metrics or characteristics, see

  risk:IdentificationControl'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Detection Control
exact_mappings:
- dpv_risk:DetectionControl
- dpv_risk_owl:DetectionControl
close_mappings:
- iso42001:AIReferenceControl
is_a: MonitorControl
mixins:
- RiskControl
class_uri: risk:DetectionControl

```
</details>

### Induced

<details>
```yaml
name: DetectionControl
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DetectionControl
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Control that detects an event
comments:
- 'Detection refers to the observation, derivation, inference, or any other

  method for drawing conclusions that an event has occurred or is likely

  to occur with a given certainty. For controls that identify information

  about the event in terms of metrics or characteristics, see

  risk:IdentificationControl'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Detection Control
exact_mappings:
- dpv_risk:DetectionControl
- dpv_risk_owl:DetectionControl
close_mappings:
- iso42001:AIReferenceControl
is_a: MonitorControl
mixins:
- RiskControl
class_uri: risk:DetectionControl

```
</details></div>