---
search:
  boost: 10.0
---

# Class: OutputAction 


_Action produced as an output from a technology_



<div data-search-exclude markdown="1">



URI: [tech:OutputAction](https://w3id.org/lmodel/dpv/tech/OutputAction)





```mermaid
 classDiagram
    class OutputAction
    click OutputAction href "../OutputAction/"
      Output <|-- OutputAction
        click Output href "../Output/"
      DpvAction <|-- OutputAction
        click DpvAction href "../DpvAction/"
      
      
```





## Inheritance
* [InputOutput](InputOutput.md)
    * [DpvAction](DpvAction.md)
        * **OutputAction** [ [Output](Output.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:OutputAction](https://w3id.org/lmodel/dpv/tech/OutputAction) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Output Action


## Comments

* Action can mean a physical action, such as the movements involved in
robotics



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#OutputAction |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:OutputAction |
| native | tech:OutputAction |
| exact | dpv_tech:OutputAction, dpv_tech_owl:OutputAction |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OutputAction
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#OutputAction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Action produced as an output from a technology
comments:
- 'Action can mean a physical action, such as the movements involved in

  robotics'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Output Action
exact_mappings:
- dpv_tech:OutputAction
- dpv_tech_owl:OutputAction
is_a: DpvAction
mixins:
- Output
class_uri: tech:OutputAction

```
</details>

### Induced

<details>
```yaml
name: OutputAction
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#OutputAction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Action produced as an output from a technology
comments:
- 'Action can mean a physical action, such as the movements involved in

  robotics'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Output Action
exact_mappings:
- dpv_tech:OutputAction
- dpv_tech_owl:OutputAction
is_a: DpvAction
mixins:
- Output
class_uri: tech:OutputAction

```
</details></div>