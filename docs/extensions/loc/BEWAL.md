---
search:
  boost: 10.0
---

# Class: BEWAL 


_Concept representing region Wallonia in country Belgium_



<div data-search-exclude markdown="1">



URI: [loc:BE-WAL](https://w3id.org/lmodel/dpv/loc/BE-WAL)





```mermaid
 classDiagram
    class BEWAL
    click BEWAL href "../BEWAL/"
      BE <|-- BEWAL
        click BE href "../BE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [BE](BE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **BEWAL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:BE-WAL](https://w3id.org/lmodel/dpv/loc/BE-WAL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* BE-WAL
* Wallonia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#BE-WAL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:BE-WAL |
| native | loc:BEWAL |
| exact | dpv_loc:BE-WAL, dpv_loc_owl:BE-WAL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BEWAL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BE-WAL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Wallonia in country Belgium
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BE-WAL
- Wallonia
exact_mappings:
- dpv_loc:BE-WAL
- dpv_loc_owl:BE-WAL
is_a: BE
class_uri: loc:BE-WAL

```
</details>

### Induced

<details>
```yaml
name: BEWAL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BE-WAL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Wallonia in country Belgium
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BE-WAL
- Wallonia
exact_mappings:
- dpv_loc:BE-WAL
- dpv_loc_owl:BE-WAL
is_a: BE
class_uri: loc:BE-WAL

```
</details></div>