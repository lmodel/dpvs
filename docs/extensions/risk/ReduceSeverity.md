---
search:
  boost: 10.0
---

# Class: ReduceSeverity 


_Control that reduces the severity of an event's effects_



<div data-search-exclude markdown="1">



URI: [risk:ReduceSeverity](https://w3id.org/lmodel/dpv/risk/ReduceSeverity)





```mermaid
 classDiagram
    class ReduceSeverity
    click ReduceSeverity href "../ReduceSeverity/"
      RiskControl <|-- ReduceSeverity
        click RiskControl href "../RiskControl/"
      ReductionControl <|-- ReduceSeverity
        click ReductionControl href "../ReductionControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ReactiveControl](ReactiveControl.md)
        * [ReductionControl](ReductionControl.md) [ [RiskControl](RiskControl.md)]
            * **ReduceSeverity** [ [RiskControl](RiskControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ReduceSeverity](https://w3id.org/lmodel/dpv/risk/ReduceSeverity) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Reduce Severity




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ReduceSeverity |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ReduceSeverity |
| native | risk:ReduceSeverity |
| exact | dpv_risk:ReduceSeverity, dpv_risk_owl:ReduceSeverity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ReduceSeverity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ReduceSeverity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Control that reduces the severity of an event's effects
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Reduce Severity
exact_mappings:
- dpv_risk:ReduceSeverity
- dpv_risk_owl:ReduceSeverity
is_a: ReductionControl
mixins:
- RiskControl
class_uri: risk:ReduceSeverity

```
</details>

### Induced

<details>
```yaml
name: ReduceSeverity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ReduceSeverity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Control that reduces the severity of an event's effects
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Reduce Severity
exact_mappings:
- dpv_risk:ReduceSeverity
- dpv_risk_owl:ReduceSeverity
is_a: ReductionControl
mixins:
- RiskControl
class_uri: risk:ReduceSeverity

```
</details></div>