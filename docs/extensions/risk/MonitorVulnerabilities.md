---
search:
  boost: 10.0
---

# Class: MonitorVulnerabilities 


_Control that monitors a Risk Vulnerability_



<div data-search-exclude markdown="1">



URI: [risk:MonitorVulnerabilities](https://w3id.org/lmodel/dpv/risk/MonitorVulnerabilities)





```mermaid
 classDiagram
    class MonitorVulnerabilities
    click MonitorVulnerabilities href "../MonitorVulnerabilities/"
      RiskControl <|-- MonitorVulnerabilities
        click RiskControl href "../RiskControl/"
      MonitorControl <|-- MonitorVulnerabilities
        click MonitorControl href "../MonitorControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ProactiveControl](ProactiveControl.md)
        * [MonitorControl](MonitorControl.md) [ [RiskControl](RiskControl.md)]
            * **MonitorVulnerabilities** [ [RiskControl](RiskControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:MonitorVulnerabilities](https://w3id.org/lmodel/dpv/risk/MonitorVulnerabilities) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Monitor Vulnerabilities




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#MonitorVulnerabilities |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:MonitorVulnerabilities |
| native | risk:MonitorVulnerabilities |
| exact | dpv_risk:MonitorVulnerabilities, dpv_risk_owl:MonitorVulnerabilities |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MonitorVulnerabilities
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#MonitorVulnerabilities
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Control that monitors a Risk Vulnerability
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Monitor Vulnerabilities
exact_mappings:
- dpv_risk:MonitorVulnerabilities
- dpv_risk_owl:MonitorVulnerabilities
is_a: MonitorControl
mixins:
- RiskControl
class_uri: risk:MonitorVulnerabilities

```
</details>

### Induced

<details>
```yaml
name: MonitorVulnerabilities
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#MonitorVulnerabilities
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Control that monitors a Risk Vulnerability
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Monitor Vulnerabilities
exact_mappings:
- dpv_risk:MonitorVulnerabilities
- dpv_risk_owl:MonitorVulnerabilities
is_a: MonitorControl
mixins:
- RiskControl
class_uri: risk:MonitorVulnerabilities

```
</details></div>