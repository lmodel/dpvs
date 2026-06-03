---
search:
  boost: 10.0
---

# Class: LTVL 


_Concept representing region Vilnius County in country Lithuania_



<div data-search-exclude markdown="1">



URI: [loc:LT-VL](https://w3id.org/lmodel/dpv/loc/LT-VL)





```mermaid
 classDiagram
    class LTVL
    click LTVL href "../LTVL/"
      LT <|-- LTVL
        click LT href "../LT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [LT](LT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **LTVL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:LT-VL](https://w3id.org/lmodel/dpv/loc/LT-VL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* LT-VL
* Vilnius County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#LT-VL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:LT-VL |
| native | loc:LTVL |
| exact | dpv_loc:LT-VL, dpv_loc_owl:LT-VL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LTVL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LT-VL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Vilnius County in country Lithuania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- LT-VL
- Vilnius County
exact_mappings:
- dpv_loc:LT-VL
- dpv_loc_owl:LT-VL
is_a: LT
class_uri: loc:LT-VL

```
</details>

### Induced

<details>
```yaml
name: LTVL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LT-VL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Vilnius County in country Lithuania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- LT-VL
- Vilnius County
exact_mappings:
- dpv_loc:LT-VL
- dpv_loc_owl:LT-VL
is_a: LT
class_uri: loc:LT-VL

```
</details></div>