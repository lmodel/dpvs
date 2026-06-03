---
search:
  boost: 10.0
---

# Class: AvoidConsequence 


_Control that proactively avoids the consequence such that it has a_

_reduced exposure or applicability in the context_



<div data-search-exclude markdown="1">



URI: [risk:AvoidConsequence](https://w3id.org/lmodel/dpv/risk/AvoidConsequence)





```mermaid
 classDiagram
    class AvoidConsequence
    click AvoidConsequence href "../AvoidConsequence/"
      RiskControl <|-- AvoidConsequence
        click RiskControl href "../RiskControl/"
      ConsequenceControl <|-- AvoidConsequence
        click ConsequenceControl href "../ConsequenceControl/"
      AvoidanceControl <|-- AvoidConsequence
        click AvoidanceControl href "../AvoidanceControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ProactiveControl](ProactiveControl.md)
        * [AvoidanceControl](AvoidanceControl.md) [ [RiskControl](RiskControl.md)]
            * **AvoidConsequence** [ [RiskControl](RiskControl.md) [ConsequenceControl](ConsequenceControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:AvoidConsequence](https://w3id.org/lmodel/dpv/risk/AvoidConsequence) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Avoid Consequence




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#AvoidConsequence |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:AvoidConsequence |
| native | risk:AvoidConsequence |
| exact | dpv_risk:AvoidConsequence, dpv_risk_owl:AvoidConsequence |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AvoidConsequence
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AvoidConsequence
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that proactively avoids the consequence such that it has a

  reduced exposure or applicability in the context'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Avoid Consequence
exact_mappings:
- dpv_risk:AvoidConsequence
- dpv_risk_owl:AvoidConsequence
is_a: AvoidanceControl
mixins:
- RiskControl
- ConsequenceControl
class_uri: risk:AvoidConsequence

```
</details>

### Induced

<details>
```yaml
name: AvoidConsequence
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AvoidConsequence
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that proactively avoids the consequence such that it has a

  reduced exposure or applicability in the context'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Avoid Consequence
exact_mappings:
- dpv_risk:AvoidConsequence
- dpv_risk_owl:AvoidConsequence
is_a: AvoidanceControl
mixins:
- RiskControl
- ConsequenceControl
class_uri: risk:AvoidConsequence

```
</details></div>