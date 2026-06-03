---
search:
  boost: 10.0
---

# Class: MonitorRisk 


_Control that monitors a Risk_



<div data-search-exclude markdown="1">



URI: [risk:MonitorRisk](https://w3id.org/lmodel/dpv/risk/MonitorRisk)





```mermaid
 classDiagram
    class MonitorRisk
    click MonitorRisk href "../MonitorRisk/"
      RiskControl <|-- MonitorRisk
        click RiskControl href "../RiskControl/"
      MonitorControl <|-- MonitorRisk
        click MonitorControl href "../MonitorControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ProactiveControl](ProactiveControl.md)
        * [MonitorControl](MonitorControl.md) [ [RiskControl](RiskControl.md)]
            * **MonitorRisk** [ [RiskControl](RiskControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:MonitorRisk](https://w3id.org/lmodel/dpv/risk/MonitorRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Monitor Risk




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#MonitorRisk |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:MonitorRisk |
| native | risk:MonitorRisk |
| exact | dpv_risk:MonitorRisk, dpv_risk_owl:MonitorRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MonitorRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#MonitorRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Control that monitors a Risk
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Monitor Risk
exact_mappings:
- dpv_risk:MonitorRisk
- dpv_risk_owl:MonitorRisk
is_a: MonitorControl
mixins:
- RiskControl
class_uri: risk:MonitorRisk

```
</details>

### Induced

<details>
```yaml
name: MonitorRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#MonitorRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Control that monitors a Risk
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Monitor Risk
exact_mappings:
- dpv_risk:MonitorRisk
- dpv_risk_owl:MonitorRisk
is_a: MonitorControl
mixins:
- RiskControl
class_uri: risk:MonitorRisk

```
</details></div>