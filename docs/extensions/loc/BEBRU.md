---
search:
  boost: 10.0
---

# Class: BEBRU 


_Concept representing region Brussels-Capital Region in country Belgium_



<div data-search-exclude markdown="1">



URI: [loc:BE-BRU](https://w3id.org/lmodel/dpv/loc/BE-BRU)





```mermaid
 classDiagram
    class BEBRU
    click BEBRU href "../BEBRU/"
      BE <|-- BEBRU
        click BE href "../BE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [BE](BE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **BEBRU**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:BE-BRU](https://w3id.org/lmodel/dpv/loc/BE-BRU) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* BE-BRU
* Brussels-Capital Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#BE-BRU |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:BE-BRU |
| native | loc:BEBRU |
| exact | dpv_loc:BE-BRU, dpv_loc_owl:BE-BRU |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BEBRU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BE-BRU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Brussels-Capital Region in country Belgium
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BE-BRU
- Brussels-Capital Region
exact_mappings:
- dpv_loc:BE-BRU
- dpv_loc_owl:BE-BRU
is_a: BE
class_uri: loc:BE-BRU

```
</details>

### Induced

<details>
```yaml
name: BEBRU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BE-BRU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Brussels-Capital Region in country Belgium
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BE-BRU
- Brussels-Capital Region
exact_mappings:
- dpv_loc:BE-BRU
- dpv_loc_owl:BE-BRU
is_a: BE
class_uri: loc:BE-BRU

```
</details></div>