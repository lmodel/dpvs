---
search:
  boost: 10.0
---

# Class: DpvDecision 


_A conclusion or determination of an action or choice in the context of_

_technologies_



<div data-search-exclude markdown="1">



URI: [tech:Decision](https://w3id.org/lmodel/dpv/tech/Decision)





```mermaid
 classDiagram
    class DpvDecision
    click DpvDecision href "../DpvDecision/"
      InputOutput <|-- DpvDecision
        click InputOutput href "../InputOutput/"
      
      
```





## Inheritance
* [InputOutput](InputOutput.md)
    * **DpvDecision**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Decision](https://w3id.org/lmodel/dpv/tech/Decision) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Decision


## Comments

* Decision is a concept referring to activities or tasks in the context of
technologies producing or using them as inputs or outputs



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Decision |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Decision |
| native | tech:DpvDecision |
| exact | dpv_tech:Decision, dpv_tech_owl:Decision |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DpvDecision
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Decision
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'A conclusion or determination of an action or choice in the context
  of

  technologies'
comments:
- 'Decision is a concept referring to activities or tasks in the context of

  technologies producing or using them as inputs or outputs'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Decision
exact_mappings:
- dpv_tech:Decision
- dpv_tech_owl:Decision
is_a: InputOutput
class_uri: tech:Decision

```
</details>

### Induced

<details>
```yaml
name: DpvDecision
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Decision
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'A conclusion or determination of an action or choice in the context
  of

  technologies'
comments:
- 'Decision is a concept referring to activities or tasks in the context of

  technologies producing or using them as inputs or outputs'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Decision
exact_mappings:
- dpv_tech:Decision
- dpv_tech_owl:Decision
is_a: InputOutput
class_uri: tech:Decision

```
</details></div>