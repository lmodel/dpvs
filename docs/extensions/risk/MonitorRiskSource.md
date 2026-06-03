---
search:
  boost: 10.0
---

# Class: MonitorRiskSource 


_Control that monitors a Risk Source_



<div data-search-exclude markdown="1">



URI: [risk:MonitorRiskSource](https://w3id.org/lmodel/dpv/risk/MonitorRiskSource)





```mermaid
 classDiagram
    class MonitorRiskSource
    click MonitorRiskSource href "../MonitorRiskSource/"
      RiskControl <|-- MonitorRiskSource
        click RiskControl href "../RiskControl/"
      MonitorControl <|-- MonitorRiskSource
        click MonitorControl href "../MonitorControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ProactiveControl](ProactiveControl.md)
        * [MonitorControl](MonitorControl.md) [ [RiskControl](RiskControl.md)]
            * **MonitorRiskSource** [ [RiskControl](RiskControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:MonitorRiskSource](https://w3id.org/lmodel/dpv/risk/MonitorRiskSource) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Monitor Risk Source




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#MonitorRiskSource |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:MonitorRiskSource |
| native | risk:MonitorRiskSource |
| exact | dpv_risk:MonitorRiskSource, dpv_risk_owl:MonitorRiskSource |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MonitorRiskSource
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#MonitorRiskSource
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Control that monitors a Risk Source
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Monitor Risk Source
exact_mappings:
- dpv_risk:MonitorRiskSource
- dpv_risk_owl:MonitorRiskSource
is_a: MonitorControl
mixins:
- RiskControl
class_uri: risk:MonitorRiskSource

```
</details>

### Induced

<details>
```yaml
name: MonitorRiskSource
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#MonitorRiskSource
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Control that monitors a Risk Source
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Monitor Risk Source
exact_mappings:
- dpv_risk:MonitorRiskSource
- dpv_risk_owl:MonitorRiskSource
is_a: MonitorControl
mixins:
- RiskControl
class_uri: risk:MonitorRiskSource

```
</details></div>