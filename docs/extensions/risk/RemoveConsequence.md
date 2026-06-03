---
search:
  boost: 10.0
---

# Class: RemoveConsequence 


_Control that proactively removes the consequence event such that the_

_event does not occur in the context_



<div data-search-exclude markdown="1">



URI: [risk:RemoveConsequence](https://w3id.org/lmodel/dpv/risk/RemoveConsequence)





```mermaid
 classDiagram
    class RemoveConsequence
    click RemoveConsequence href "../RemoveConsequence/"
      RiskControl <|-- RemoveConsequence
        click RiskControl href "../RiskControl/"
      EliminationControl <|-- RemoveConsequence
        click EliminationControl href "../EliminationControl/"
      ConsequenceControl <|-- RemoveConsequence
        click ConsequenceControl href "../ConsequenceControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ConsequenceControl](ConsequenceControl.md)
        * **RemoveConsequence** [ [RiskControl](RiskControl.md) [EliminationControl](EliminationControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RemoveConsequence](https://w3id.org/lmodel/dpv/risk/RemoveConsequence) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Remove Consequence




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RemoveConsequence |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RemoveConsequence |
| native | risk:RemoveConsequence |
| exact | dpv_risk:RemoveConsequence, dpv_risk_owl:RemoveConsequence |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RemoveConsequence
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RemoveConsequence
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that proactively removes the consequence event such that the

  event does not occur in the context'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Remove Consequence
exact_mappings:
- dpv_risk:RemoveConsequence
- dpv_risk_owl:RemoveConsequence
is_a: ConsequenceControl
mixins:
- RiskControl
- EliminationControl
class_uri: risk:RemoveConsequence

```
</details>

### Induced

<details>
```yaml
name: RemoveConsequence
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RemoveConsequence
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that proactively removes the consequence event such that the

  event does not occur in the context'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Remove Consequence
exact_mappings:
- dpv_risk:RemoveConsequence
- dpv_risk_owl:RemoveConsequence
is_a: ConsequenceControl
mixins:
- RiskControl
- EliminationControl
class_uri: risk:RemoveConsequence

```
</details></div>