---
search:
  boost: 10.0
---

# Class: ShareRisk 


_Risk Mitigation Measure that shares Risk e.g. amongst stakeholders_



<div data-search-exclude markdown="1">



URI: [risk:ShareRisk](https://w3id.org/lmodel/dpv/risk/ShareRisk)





```mermaid
 classDiagram
    class ShareRisk
    click ShareRisk href "../ShareRisk/"
      RiskControl <|-- ShareRisk
        click RiskControl href "../RiskControl/"
      ShareControl <|-- ShareRisk
        click ShareControl href "../ShareControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [TransferControl](TransferControl.md)
        * [ShareControl](ShareControl.md) [ [RiskControl](RiskControl.md)]
            * **ShareRisk** [ [RiskControl](RiskControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ShareRisk](https://w3id.org/lmodel/dpv/risk/ShareRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Share Risk




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ShareRisk |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ShareRisk |
| native | risk:ShareRisk |
| exact | dpv_risk:ShareRisk, dpv_risk_owl:ShareRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ShareRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ShareRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Risk Mitigation Measure that shares Risk e.g. amongst stakeholders
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Share Risk
exact_mappings:
- dpv_risk:ShareRisk
- dpv_risk_owl:ShareRisk
is_a: ShareControl
mixins:
- RiskControl
class_uri: risk:ShareRisk

```
</details>

### Induced

<details>
```yaml
name: ShareRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ShareRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Risk Mitigation Measure that shares Risk e.g. amongst stakeholders
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Share Risk
exact_mappings:
- dpv_risk:ShareRisk
- dpv_risk_owl:ShareRisk
is_a: ShareControl
mixins:
- RiskControl
class_uri: risk:ShareRisk

```
</details></div>