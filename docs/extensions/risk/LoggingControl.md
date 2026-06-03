---
search:
  boost: 10.0
---

# Class: LoggingControl 


_Control that logs an event_



<div data-search-exclude markdown="1">



URI: [risk:LoggingControl](https://w3id.org/lmodel/dpv/risk/LoggingControl)





```mermaid
 classDiagram
    class LoggingControl
    click LoggingControl href "../LoggingControl/"
      RiskControl <|-- LoggingControl
        click RiskControl href "../RiskControl/"
      MonitorControl <|-- LoggingControl
        click MonitorControl href "../MonitorControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ProactiveControl](ProactiveControl.md)
        * [MonitorControl](MonitorControl.md) [ [RiskControl](RiskControl.md)]
            * **LoggingControl** [ [RiskControl](RiskControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:LoggingControl](https://w3id.org/lmodel/dpv/risk/LoggingControl) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Logging Control


## Comments

* Log refers to a record of information regarding the event, including
whether it has occurred, was prevented from occurring, and any actions
or processes taken in response to it or resulting from it



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#LoggingControl |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:LoggingControl |
| native | risk:LoggingControl |
| exact | dpv_risk:LoggingControl, dpv_risk_owl:LoggingControl |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LoggingControl
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#LoggingControl
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Control that logs an event
comments:
- 'Log refers to a record of information regarding the event, including

  whether it has occurred, was prevented from occurring, and any actions

  or processes taken in response to it or resulting from it'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Logging Control
exact_mappings:
- dpv_risk:LoggingControl
- dpv_risk_owl:LoggingControl
is_a: MonitorControl
mixins:
- RiskControl
class_uri: risk:LoggingControl

```
</details>

### Induced

<details>
```yaml
name: LoggingControl
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#LoggingControl
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Control that logs an event
comments:
- 'Log refers to a record of information regarding the event, including

  whether it has occurred, was prevented from occurring, and any actions

  or processes taken in response to it or resulting from it'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Logging Control
exact_mappings:
- dpv_risk:LoggingControl
- dpv_risk_owl:LoggingControl
is_a: MonitorControl
mixins:
- RiskControl
class_uri: risk:LoggingControl

```
</details></div>