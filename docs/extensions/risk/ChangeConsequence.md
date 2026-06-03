---
search:
  boost: 10.0
---

# Class: ChangeConsequence 


_Control that proactively changes the consequence event such that one_

_event is replaced with the occurrence or applicability of another event_

_in the context_



<div data-search-exclude markdown="1">



URI: [risk:ChangeConsequence](https://w3id.org/lmodel/dpv/risk/ChangeConsequence)





```mermaid
 classDiagram
    class ChangeConsequence
    click ChangeConsequence href "../ChangeConsequence/"
      RiskControl <|-- ChangeConsequence
        click RiskControl href "../RiskControl/"
      SubstitutionControl <|-- ChangeConsequence
        click SubstitutionControl href "../SubstitutionControl/"
      ConsequenceControl <|-- ChangeConsequence
        click ConsequenceControl href "../ConsequenceControl/"
      
      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * [ConsequenceControl](ConsequenceControl.md)
        * **ChangeConsequence** [ [RiskControl](RiskControl.md) [SubstitutionControl](SubstitutionControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ChangeConsequence](https://w3id.org/lmodel/dpv/risk/ChangeConsequence) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Change Consequence




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ChangeConsequence |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ChangeConsequence |
| native | risk:ChangeConsequence |
| exact | dpv_risk:ChangeConsequence, dpv_risk_owl:ChangeConsequence |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ChangeConsequence
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ChangeConsequence
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that proactively changes the consequence event such that one

  event is replaced with the occurrence or applicability of another event

  in the context'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Change Consequence
exact_mappings:
- dpv_risk:ChangeConsequence
- dpv_risk_owl:ChangeConsequence
is_a: ConsequenceControl
mixins:
- RiskControl
- SubstitutionControl
class_uri: risk:ChangeConsequence

```
</details>

### Induced

<details>
```yaml
name: ChangeConsequence
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ChangeConsequence
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Control that proactively changes the consequence event such that one

  event is replaced with the occurrence or applicability of another event

  in the context'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Change Consequence
exact_mappings:
- dpv_risk:ChangeConsequence
- dpv_risk_owl:ChangeConsequence
is_a: ConsequenceControl
mixins:
- RiskControl
- SubstitutionControl
class_uri: risk:ChangeConsequence

```
</details></div>