---
search:
  boost: 10.0
---

# Class: BEWLG 


_Concept representing region Liège (province) in country Belgium_



<div data-search-exclude markdown="1">



URI: [loc:BE-WLG](https://w3id.org/lmodel/dpv/loc/BE-WLG)





```mermaid
 classDiagram
    class BEWLG
    click BEWLG href "../BEWLG/"
      BE <|-- BEWLG
        click BE href "../BE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [BE](BE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **BEWLG**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:BE-WLG](https://w3id.org/lmodel/dpv/loc/BE-WLG) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* BE-WLG
* Liège (province)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#BE-WLG |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:BE-WLG |
| native | loc:BEWLG |
| exact | dpv_loc:BE-WLG, dpv_loc_owl:BE-WLG |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BEWLG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BE-WLG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Liège (province) in country Belgium
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BE-WLG
- Liège (province)
exact_mappings:
- dpv_loc:BE-WLG
- dpv_loc_owl:BE-WLG
is_a: BE
class_uri: loc:BE-WLG

```
</details>

### Induced

<details>
```yaml
name: BEWLG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BE-WLG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Liège (province) in country Belgium
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BE-WLG
- Liège (province)
exact_mappings:
- dpv_loc:BE-WLG
- dpv_loc_owl:BE-WLG
is_a: BE
class_uri: loc:BE-WLG

```
</details></div>