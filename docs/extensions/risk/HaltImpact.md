---
search:
  boost: 10.0
---

# Class: HaltImpact 


_Control that halts the (ongoing) impact event or process such that it no_

_longer takes place or is applicable in the context_



<div data-search-exclude markdown="1">



URI: [risk:HaltImpact](https://w3id.org/lmodel/dpv/risk/HaltImpact)





```mermaid
 classDiagram
    class HaltImpact
    click HaltImpact href "../HaltImpact/"
      RiskControl <|-- HaltImpact
        click RiskControl href "../RiskControl/"
      InterruptionControl <|-- HaltImpact
        click InterruptionControl href "../InterruptionControl/"
      ImpactControl <|-- HaltImpact
        click ImpactControl href "../ImpactControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ImpactControl](ImpactControl.md)
        * **HaltImpact** [ [RiskControl](RiskControl.md) [InterruptionControl](InterruptionControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:HaltImpact](https://w3id.org/lmodel/dpv/risk/HaltImpact) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Halt Impact




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#HaltImpact |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:HaltImpact |
| native | risk:HaltImpact |
| exact | dpv_risk:HaltImpact, dpv_risk_owl:HaltImpact |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HaltImpact
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#HaltImpact
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that halts the (ongoing) impact event or process such that it
  no

  longer takes place or is applicable in the context'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Halt Impact
exact_mappings:
- dpv_risk:HaltImpact
- dpv_risk_owl:HaltImpact
is_a: ImpactControl
mixins:
- RiskControl
- InterruptionControl
class_uri: risk:HaltImpact

```
</details>

### Induced

<details>
```yaml
name: HaltImpact
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#HaltImpact
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that halts the (ongoing) impact event or process such that it
  no

  longer takes place or is applicable in the context'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Halt Impact
exact_mappings:
- dpv_risk:HaltImpact
- dpv_risk_owl:HaltImpact
is_a: ImpactControl
mixins:
- RiskControl
- InterruptionControl
class_uri: risk:HaltImpact

```
</details></div>