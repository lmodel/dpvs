---
search:
  boost: 10.0
---

# Class: RemoveSource 


_Control that proactively removes the risk source such that it is no_

_longer present or applicable in the context_



<div data-search-exclude markdown="1">



URI: [risk:RemoveSource](https://w3id.org/lmodel/dpv/risk/RemoveSource)





```mermaid
 classDiagram
    class RemoveSource
    click RemoveSource href "../RemoveSource/"
      RiskControl <|-- RemoveSource
        click RiskControl href "../RiskControl/"
      SourceControl <|-- RemoveSource
        click SourceControl href "../SourceControl/"
      EliminationControl <|-- RemoveSource
        click EliminationControl href "../EliminationControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ProactiveControl](ProactiveControl.md)
        * [AvoidanceControl](AvoidanceControl.md) [ [RiskControl](RiskControl.md)]
            * [EliminationControl](EliminationControl.md) [ [RiskControl](RiskControl.md)]
                * **RemoveSource** [ [RiskControl](RiskControl.md) [SourceControl](SourceControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RemoveSource](https://w3id.org/lmodel/dpv/risk/RemoveSource) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Remove Source




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RemoveSource |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RemoveSource |
| native | risk:RemoveSource |
| exact | dpv_risk:RemoveSource, dpv_risk_owl:RemoveSource |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RemoveSource
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RemoveSource
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that proactively removes the risk source such that it is no

  longer present or applicable in the context'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Remove Source
exact_mappings:
- dpv_risk:RemoveSource
- dpv_risk_owl:RemoveSource
is_a: EliminationControl
mixins:
- RiskControl
- SourceControl
class_uri: risk:RemoveSource

```
</details>

### Induced

<details>
```yaml
name: RemoveSource
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RemoveSource
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that proactively removes the risk source such that it is no

  longer present or applicable in the context'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Remove Source
exact_mappings:
- dpv_risk:RemoveSource
- dpv_risk_owl:RemoveSource
is_a: EliminationControl
mixins:
- RiskControl
- SourceControl
class_uri: risk:RemoveSource

```
</details></div>