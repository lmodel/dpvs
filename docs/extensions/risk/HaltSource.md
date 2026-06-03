---
search:
  boost: 10.0
---

# Class: HaltSource 


_Control that halts the (ongoing) risk source event or process such that_

_it no longer takes place or is applicable in the context_



<div data-search-exclude markdown="1">



URI: [risk:HaltSource](https://w3id.org/lmodel/dpv/risk/HaltSource)





```mermaid
 classDiagram
    class HaltSource
    click HaltSource href "../HaltSource/"
      RiskControl <|-- HaltSource
        click RiskControl href "../RiskControl/"
      SourceControl <|-- HaltSource
        click SourceControl href "../SourceControl/"
      InterruptionControl <|-- HaltSource
        click InterruptionControl href "../InterruptionControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ReactiveControl](ReactiveControl.md)
        * [ReductionControl](ReductionControl.md) [ [RiskControl](RiskControl.md)]
            * [InterruptionControl](InterruptionControl.md) [ [RiskControl](RiskControl.md)]
                * **HaltSource** [ [RiskControl](RiskControl.md) [SourceControl](SourceControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:HaltSource](https://w3id.org/lmodel/dpv/risk/HaltSource) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Halt Source




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#HaltSource |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:HaltSource |
| native | risk:HaltSource |
| exact | dpv_risk:HaltSource, dpv_risk_owl:HaltSource |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HaltSource
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#HaltSource
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that halts the (ongoing) risk source event or process such that

  it no longer takes place or is applicable in the context'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Halt Source
exact_mappings:
- dpv_risk:HaltSource
- dpv_risk_owl:HaltSource
is_a: InterruptionControl
mixins:
- RiskControl
- SourceControl
class_uri: risk:HaltSource

```
</details>

### Induced

<details>
```yaml
name: HaltSource
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#HaltSource
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that halts the (ongoing) risk source event or process such that

  it no longer takes place or is applicable in the context'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Halt Source
exact_mappings:
- dpv_risk:HaltSource
- dpv_risk_owl:HaltSource
is_a: InterruptionControl
mixins:
- RiskControl
- SourceControl
class_uri: risk:HaltSource

```
</details></div>