---
search:
  boost: 10.0
---

# Class: RemoveImpact 


_Control that proactively removes the impact event such that the event_

_does not occur in the context_



<div data-search-exclude markdown="1">



URI: [risk:RemoveImpact](https://w3id.org/lmodel/dpv/risk/RemoveImpact)





```mermaid
 classDiagram
    class RemoveImpact
    click RemoveImpact href "../RemoveImpact/"
      RiskControl <|-- RemoveImpact
        click RiskControl href "../RiskControl/"
      ImpactControl <|-- RemoveImpact
        click ImpactControl href "../ImpactControl/"
      EliminationControl <|-- RemoveImpact
        click EliminationControl href "../EliminationControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ProactiveControl](ProactiveControl.md)
        * [AvoidanceControl](AvoidanceControl.md) [ [RiskControl](RiskControl.md)]
            * [EliminationControl](EliminationControl.md) [ [RiskControl](RiskControl.md)]
                * **RemoveImpact** [ [RiskControl](RiskControl.md) [ImpactControl](ImpactControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RemoveImpact](https://w3id.org/lmodel/dpv/risk/RemoveImpact) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Remove Impact




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RemoveImpact |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RemoveImpact |
| native | risk:RemoveImpact |
| exact | dpv_risk:RemoveImpact, dpv_risk_owl:RemoveImpact |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RemoveImpact
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RemoveImpact
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that proactively removes the impact event such that the event

  does not occur in the context'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Remove Impact
exact_mappings:
- dpv_risk:RemoveImpact
- dpv_risk_owl:RemoveImpact
is_a: EliminationControl
mixins:
- RiskControl
- ImpactControl
class_uri: risk:RemoveImpact

```
</details>

### Induced

<details>
```yaml
name: RemoveImpact
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RemoveImpact
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that proactively removes the impact event such that the event

  does not occur in the context'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Remove Impact
exact_mappings:
- dpv_risk:RemoveImpact
- dpv_risk_owl:RemoveImpact
is_a: EliminationControl
mixins:
- RiskControl
- ImpactControl
class_uri: risk:RemoveImpact

```
</details></div>