---
search:
  boost: 10.0
---

# Class: AvoidImpact 


_Control that proactively avoids the impact such that it has a reduced_

_exposure or applicability in the context_



<div data-search-exclude markdown="1">



URI: [risk:AvoidImpact](https://w3id.org/lmodel/dpv/risk/AvoidImpact)





```mermaid
 classDiagram
    class AvoidImpact
    click AvoidImpact href "../AvoidImpact/"
      RiskControl <|-- AvoidImpact
        click RiskControl href "../RiskControl/"
      ImpactControl <|-- AvoidImpact
        click ImpactControl href "../ImpactControl/"
      AvoidanceControl <|-- AvoidImpact
        click AvoidanceControl href "../AvoidanceControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ProactiveControl](ProactiveControl.md)
        * [AvoidanceControl](AvoidanceControl.md) [ [RiskControl](RiskControl.md)]
            * **AvoidImpact** [ [RiskControl](RiskControl.md) [ImpactControl](ImpactControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:AvoidImpact](https://w3id.org/lmodel/dpv/risk/AvoidImpact) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Avoid Impact




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#AvoidImpact |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:AvoidImpact |
| native | risk:AvoidImpact |
| exact | dpv_risk:AvoidImpact, dpv_risk_owl:AvoidImpact |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AvoidImpact
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AvoidImpact
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that proactively avoids the impact such that it has a reduced

  exposure or applicability in the context'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Avoid Impact
exact_mappings:
- dpv_risk:AvoidImpact
- dpv_risk_owl:AvoidImpact
is_a: AvoidanceControl
mixins:
- RiskControl
- ImpactControl
class_uri: risk:AvoidImpact

```
</details>

### Induced

<details>
```yaml
name: AvoidImpact
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AvoidImpact
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that proactively avoids the impact such that it has a reduced

  exposure or applicability in the context'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Avoid Impact
exact_mappings:
- dpv_risk:AvoidImpact
- dpv_risk_owl:AvoidImpact
is_a: AvoidanceControl
mixins:
- RiskControl
- ImpactControl
class_uri: risk:AvoidImpact

```
</details></div>