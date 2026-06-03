---
search:
  boost: 10.0
---

# Class: MonitorImpact 


_Control that monitors a Risk Impact_



<div data-search-exclude markdown="1">



URI: [risk:MonitorImpact](https://w3id.org/lmodel/dpv/risk/MonitorImpact)





```mermaid
 classDiagram
    class MonitorImpact
    click MonitorImpact href "../MonitorImpact/"
      RiskControl <|-- MonitorImpact
        click RiskControl href "../RiskControl/"
      MonitorControl <|-- MonitorImpact
        click MonitorControl href "../MonitorControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ProactiveControl](ProactiveControl.md)
        * [MonitorControl](MonitorControl.md) [ [RiskControl](RiskControl.md)]
            * **MonitorImpact** [ [RiskControl](RiskControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:MonitorImpact](https://w3id.org/lmodel/dpv/risk/MonitorImpact) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Monitor Impact




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#MonitorImpact |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:MonitorImpact |
| native | risk:MonitorImpact |
| exact | dpv_risk:MonitorImpact, dpv_risk_owl:MonitorImpact |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MonitorImpact
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#MonitorImpact
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Control that monitors a Risk Impact
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Monitor Impact
exact_mappings:
- dpv_risk:MonitorImpact
- dpv_risk_owl:MonitorImpact
is_a: MonitorControl
mixins:
- RiskControl
class_uri: risk:MonitorImpact

```
</details>

### Induced

<details>
```yaml
name: MonitorImpact
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#MonitorImpact
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Control that monitors a Risk Impact
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Monitor Impact
exact_mappings:
- dpv_risk:MonitorImpact
- dpv_risk_owl:MonitorImpact
is_a: MonitorControl
mixins:
- RiskControl
class_uri: risk:MonitorImpact

```
</details></div>