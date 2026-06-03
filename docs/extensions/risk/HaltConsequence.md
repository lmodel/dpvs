---
search:
  boost: 10.0
---

# Class: HaltConsequence 


_Control that halts the (ongoing) consequence event or process such that_

_it no longer takes place or is applicable in the context_



<div data-search-exclude markdown="1">



URI: [risk:HaltConsequence](https://w3id.org/lmodel/dpv/risk/HaltConsequence)





```mermaid
 classDiagram
    class HaltConsequence
    click HaltConsequence href "../HaltConsequence/"
      RiskControl <|-- HaltConsequence
        click RiskControl href "../RiskControl/"
      InterruptionControl <|-- HaltConsequence
        click InterruptionControl href "../InterruptionControl/"
      ConsequenceControl <|-- HaltConsequence
        click ConsequenceControl href "../ConsequenceControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ConsequenceControl](ConsequenceControl.md)
        * **HaltConsequence** [ [RiskControl](RiskControl.md) [InterruptionControl](InterruptionControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:HaltConsequence](https://w3id.org/lmodel/dpv/risk/HaltConsequence) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Halt Consequence




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#HaltConsequence |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:HaltConsequence |
| native | risk:HaltConsequence |
| exact | dpv_risk:HaltConsequence, dpv_risk_owl:HaltConsequence |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HaltConsequence
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#HaltConsequence
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that halts the (ongoing) consequence event or process such that

  it no longer takes place or is applicable in the context'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Halt Consequence
exact_mappings:
- dpv_risk:HaltConsequence
- dpv_risk_owl:HaltConsequence
is_a: ConsequenceControl
mixins:
- RiskControl
- InterruptionControl
class_uri: risk:HaltConsequence

```
</details>

### Induced

<details>
```yaml
name: HaltConsequence
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#HaltConsequence
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that halts the (ongoing) consequence event or process such that

  it no longer takes place or is applicable in the context'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Halt Consequence
exact_mappings:
- dpv_risk:HaltConsequence
- dpv_risk_owl:HaltConsequence
is_a: ConsequenceControl
mixins:
- RiskControl
- InterruptionControl
class_uri: risk:HaltConsequence

```
</details></div>