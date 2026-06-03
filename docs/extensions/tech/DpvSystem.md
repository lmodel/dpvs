---
search:
  boost: 10.0
---

# Class: DpvSystem 


_A collection of components that interact to achieve a specific goal or_

_function_



<div data-search-exclude markdown="1">



URI: [tech:System](https://w3id.org/lmodel/dpv/tech/System)





```mermaid
 classDiagram
    class DpvSystem
    click DpvSystem href "../DpvSystem/"
      DpvSystem <|-- IoTSystem
        click IoTSystem href "../IoTSystem/"
      
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:System](https://w3id.org/lmodel/dpv/tech/System) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* System




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#System |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:System |
| native | tech:DpvSystem |
| exact | dpv_tech:System, dpv_tech_owl:System |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DpvSystem
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#System
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'A collection of components that interact to achieve a specific goal
  or

  function'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- System
exact_mappings:
- dpv_tech:System
- dpv_tech_owl:System
class_uri: tech:System

```
</details>

### Induced

<details>
```yaml
name: DpvSystem
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#System
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'A collection of components that interact to achieve a specific goal
  or

  function'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- System
exact_mappings:
- dpv_tech:System
- dpv_tech_owl:System
class_uri: tech:System

```
</details></div>