---
search:
  boost: 10.0
---

# Class: MonitorConsequence 


_Control that monitors a Risk Consequence_



<div data-search-exclude markdown="1">



URI: [risk:MonitorConsequence](https://w3id.org/lmodel/dpv/risk/MonitorConsequence)





```mermaid
 classDiagram
    class MonitorConsequence
    click MonitorConsequence href "../MonitorConsequence/"
      RiskControl <|-- MonitorConsequence
        click RiskControl href "../RiskControl/"
      MonitorControl <|-- MonitorConsequence
        click MonitorControl href "../MonitorControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ProactiveControl](ProactiveControl.md)
        * [MonitorControl](MonitorControl.md) [ [RiskControl](RiskControl.md)]
            * **MonitorConsequence** [ [RiskControl](RiskControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:MonitorConsequence](https://w3id.org/lmodel/dpv/risk/MonitorConsequence) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Monitor Consequence




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#MonitorConsequence |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:MonitorConsequence |
| native | risk:MonitorConsequence |
| exact | dpv_risk:MonitorConsequence, dpv_risk_owl:MonitorConsequence |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MonitorConsequence
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#MonitorConsequence
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Control that monitors a Risk Consequence
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Monitor Consequence
exact_mappings:
- dpv_risk:MonitorConsequence
- dpv_risk_owl:MonitorConsequence
is_a: MonitorControl
mixins:
- RiskControl
class_uri: risk:MonitorConsequence

```
</details>

### Induced

<details>
```yaml
name: MonitorConsequence
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#MonitorConsequence
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Control that monitors a Risk Consequence
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Monitor Consequence
exact_mappings:
- dpv_risk:MonitorConsequence
- dpv_risk_owl:MonitorConsequence
is_a: MonitorControl
mixins:
- RiskControl
class_uri: risk:MonitorConsequence

```
</details></div>