---
search:
  boost: 10.0
---

# Class: AvoidSource 


_Control that proactively avoids the risk source such that it has a_

_reduced exposure or applicability in the context_



<div data-search-exclude markdown="1">



URI: [risk:AvoidSource](https://w3id.org/lmodel/dpv/risk/AvoidSource)





```mermaid
 classDiagram
    class AvoidSource
    click AvoidSource href "../AvoidSource/"
      RiskControl <|-- AvoidSource
        click RiskControl href "../RiskControl/"
      SourceControl <|-- AvoidSource
        click SourceControl href "../SourceControl/"
      AvoidanceControl <|-- AvoidSource
        click AvoidanceControl href "../AvoidanceControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ProactiveControl](ProactiveControl.md)
        * [AvoidanceControl](AvoidanceControl.md) [ [RiskControl](RiskControl.md)]
            * **AvoidSource** [ [RiskControl](RiskControl.md) [SourceControl](SourceControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:AvoidSource](https://w3id.org/lmodel/dpv/risk/AvoidSource) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Avoid Source




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#AvoidSource |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:AvoidSource |
| native | risk:AvoidSource |
| exact | dpv_risk:AvoidSource, dpv_risk_owl:AvoidSource |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AvoidSource
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AvoidSource
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that proactively avoids the risk source such that it has a

  reduced exposure or applicability in the context'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Avoid Source
exact_mappings:
- dpv_risk:AvoidSource
- dpv_risk_owl:AvoidSource
is_a: AvoidanceControl
mixins:
- RiskControl
- SourceControl
class_uri: risk:AvoidSource

```
</details>

### Induced

<details>
```yaml
name: AvoidSource
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AvoidSource
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that proactively avoids the risk source such that it has a

  reduced exposure or applicability in the context'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Avoid Source
exact_mappings:
- dpv_risk:AvoidSource
- dpv_risk_owl:AvoidSource
is_a: AvoidanceControl
mixins:
- RiskControl
- SourceControl
class_uri: risk:AvoidSource

```
</details></div>