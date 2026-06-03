---
search:
  boost: 10.0
---

# Class: ReduceLikelihood 


_Control that reduces the likelihood of an event to occur_



<div data-search-exclude markdown="1">



URI: [risk:ReduceLikelihood](https://w3id.org/lmodel/dpv/risk/ReduceLikelihood)





```mermaid
 classDiagram
    class ReduceLikelihood
    click ReduceLikelihood href "../ReduceLikelihood/"
      RiskControl <|-- ReduceLikelihood
        click RiskControl href "../RiskControl/"
      ReductionControl <|-- ReduceLikelihood
        click ReductionControl href "../ReductionControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ReactiveControl](ReactiveControl.md)
        * [ReductionControl](ReductionControl.md) [ [RiskControl](RiskControl.md)]
            * **ReduceLikelihood** [ [RiskControl](RiskControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ReduceLikelihood](https://w3id.org/lmodel/dpv/risk/ReduceLikelihood) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Reduce Likelihood




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ReduceLikelihood |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ReduceLikelihood |
| native | risk:ReduceLikelihood |
| exact | dpv_risk:ReduceLikelihood, dpv_risk_owl:ReduceLikelihood |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ReduceLikelihood
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ReduceLikelihood
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Control that reduces the likelihood of an event to occur
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Reduce Likelihood
exact_mappings:
- dpv_risk:ReduceLikelihood
- dpv_risk_owl:ReduceLikelihood
is_a: ReductionControl
mixins:
- RiskControl
class_uri: risk:ReduceLikelihood

```
</details>

### Induced

<details>
```yaml
name: ReduceLikelihood
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ReduceLikelihood
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Control that reduces the likelihood of an event to occur
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Reduce Likelihood
exact_mappings:
- dpv_risk:ReduceLikelihood
- dpv_risk_owl:ReduceLikelihood
is_a: ReductionControl
mixins:
- RiskControl
class_uri: risk:ReduceLikelihood

```
</details></div>