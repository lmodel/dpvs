---
search:
  boost: 10.0
---

# Class: Input 


_Input to a technology_



<div data-search-exclude markdown="1">



URI: [tech:Input](https://w3id.org/lmodel/dpv/tech/Input)





```mermaid
 classDiagram
    class Input
    click Input href "../Input/"
      InputOutput <|-- Input
        click InputOutput href "../InputOutput/"
      

      Input <|-- InputAction
        click InputAction href "../InputAction/"
      Input <|-- InputData
        click InputData href "../InputData/"
      

      
```





## Inheritance
* [InputOutput](InputOutput.md)
    * **Input**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Input](https://w3id.org/lmodel/dpv/tech/Input) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Input




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Input |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Input |
| native | tech:Input |
| exact | dpv_tech:Input, dpv_tech_owl:Input |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Input
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Input
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Input to a technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Input
exact_mappings:
- dpv_tech:Input
- dpv_tech_owl:Input
is_a: InputOutput
class_uri: tech:Input

```
</details>

### Induced

<details>
```yaml
name: Input
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Input
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Input to a technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Input
exact_mappings:
- dpv_tech:Input
- dpv_tech_owl:Input
is_a: InputOutput
class_uri: tech:Input

```
</details></div>