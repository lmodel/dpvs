---
search:
  boost: 10.0
---

# Class: LU 


_Concept representing Country of Luxembourg_



<div data-search-exclude markdown="1">



URI: [loc:LU](https://w3id.org/lmodel/dpv/loc/LU)





```mermaid
 classDiagram
    class LU
    click LU href "../LU/"
      EEA30 <|-- LU
        click EEA30 href "../EEA30/"
      EEA31 <|-- LU
        click EEA31 href "../EEA31/"
      EU <|-- LU
        click EU href "../EU/"
      EU27 <|-- LU
        click EU27 href "../EU27/"
      EU28 <|-- LU
        click EU28 href "../EU28/"
      EEA <|-- LU
        click EEA href "../EEA/"
      

      LU <|-- LUCA
        click LUCA href "../LUCA/"
      LU <|-- LUCL
        click LUCL href "../LUCL/"
      LU <|-- LUD
        click LUD href "../LUD/"
      LU <|-- LUDI
        click LUDI href "../LUDI/"
      LU <|-- LUEC
        click LUEC href "../LUEC/"
      LU <|-- LUES
        click LUES href "../LUES/"
      LU <|-- LUG
        click LUG href "../LUG/"
      LU <|-- LUGR
        click LUGR href "../LUGR/"
      LU <|-- LUL
        click LUL href "../LUL/"
      LU <|-- LULU
        click LULU href "../LULU/"
      LU <|-- LUME
        click LUME href "../LUME/"
      LU <|-- LURD
        click LURD href "../LURD/"
      LU <|-- LURM
        click LURM href "../LURM/"
      LU <|-- LUVD
        click LUVD href "../LUVD/"
      LU <|-- LUWI
        click LUWI href "../LUWI/"
      

      
```





## Inheritance
* [EEA](EEA.md)
    * **LU** [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * [LUCA](LUCA.md)
        * [LUCL](LUCL.md)
        * [LUD](LUD.md)
        * [LUDI](LUDI.md)
        * [LUEC](LUEC.md)
        * [LUES](LUES.md)
        * [LUG](LUG.md)
        * [LUGR](LUGR.md)
        * [LUL](LUL.md)
        * [LULU](LULU.md)
        * [LUME](LUME.md)
        * [LURD](LURD.md)
        * [LURM](LURM.md)
        * [LUVD](LUVD.md)
        * [LUWI](LUWI.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:LU](https://w3id.org/lmodel/dpv/loc/LU) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Luxembourg




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#LU |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:LU |
| native | loc:LU |
| exact | dpv_loc:LU, dpv_loc_owl:LU |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Luxembourg
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Luxembourg
exact_mappings:
- dpv_loc:LU
- dpv_loc_owl:LU
is_a: EEA
mixins:
- EEA30
- EEA31
- EU
- EU27
- EU28
class_uri: loc:LU

```
</details>

### Induced

<details>
```yaml
name: LU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Luxembourg
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Luxembourg
exact_mappings:
- dpv_loc:LU
- dpv_loc_owl:LU
is_a: EEA
mixins:
- EEA30
- EEA31
- EU
- EU27
- EU28
class_uri: loc:LU

```
</details></div>