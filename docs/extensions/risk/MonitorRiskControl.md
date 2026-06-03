---
search:
  boost: 10.0
---

# Class: MonitorRiskControl 


_Control that monitors another Control_



<div data-search-exclude markdown="1">



URI: [risk:MonitorRiskControl](https://w3id.org/lmodel/dpv/risk/MonitorRiskControl)





```mermaid
 classDiagram
    class MonitorRiskControl
    click MonitorRiskControl href "../MonitorRiskControl/"
      RiskControl <|-- MonitorRiskControl
        click RiskControl href "../RiskControl/"
      MonitorControl <|-- MonitorRiskControl
        click MonitorControl href "../MonitorControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ProactiveControl](ProactiveControl.md)
        * [MonitorControl](MonitorControl.md) [ [RiskControl](RiskControl.md)]
            * **MonitorRiskControl** [ [RiskControl](RiskControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:MonitorRiskControl](https://w3id.org/lmodel/dpv/risk/MonitorRiskControl) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Monitor Control




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#MonitorRiskControl |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:MonitorRiskControl |
| native | risk:MonitorRiskControl |
| exact | dpv_risk:MonitorRiskControl, dpv_risk_owl:MonitorRiskControl |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MonitorRiskControl
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#MonitorRiskControl
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Control that monitors another Control
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Monitor Control
exact_mappings:
- dpv_risk:MonitorRiskControl
- dpv_risk_owl:MonitorRiskControl
is_a: MonitorControl
mixins:
- RiskControl
class_uri: risk:MonitorRiskControl

```
</details>

### Induced

<details>
```yaml
name: MonitorRiskControl
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#MonitorRiskControl
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Control that monitors another Control
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Monitor Control
exact_mappings:
- dpv_risk:MonitorRiskControl
- dpv_risk_owl:MonitorRiskControl
is_a: MonitorControl
mixins:
- RiskControl
class_uri: risk:MonitorRiskControl

```
</details></div>