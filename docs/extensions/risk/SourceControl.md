---
search:
  boost: 10.0
---

# Class: SourceControl 


_Risk control for managing risk sources_



<div data-search-exclude markdown="1">



URI: [risk:SourceControl](https://w3id.org/lmodel/dpv/risk/SourceControl)





```mermaid
 classDiagram
    class SourceControl
    click SourceControl href "../SourceControl/"
      RiskControl <|-- SourceControl
        click RiskControl href "../RiskControl/"
      

      SourceControl <|-- AvoidSource
        click AvoidSource href "../AvoidSource/"
      SourceControl <|-- HaltSource
        click HaltSource href "../HaltSource/"
      SourceControl <|-- RemoveSource
        click RemoveSource href "../RemoveSource/"
      

      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * **SourceControl**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:SourceControl](https://w3id.org/lmodel/dpv/risk/SourceControl) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Source Control




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#SourceControl |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:SourceControl |
| native | risk:SourceControl |
| exact | dpv_risk:SourceControl, dpv_risk_owl:SourceControl |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SourceControl
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SourceControl
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Risk control for managing risk sources
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Source Control
exact_mappings:
- dpv_risk:SourceControl
- dpv_risk_owl:SourceControl
is_a: RiskControl
class_uri: risk:SourceControl

```
</details>

### Induced

<details>
```yaml
name: SourceControl
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SourceControl
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Risk control for managing risk sources
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Source Control
exact_mappings:
- dpv_risk:SourceControl
- dpv_risk_owl:SourceControl
is_a: RiskControl
class_uri: risk:SourceControl

```
</details></div>