---
search:
  boost: 10.0
---

# Class: BE 


_Concept representing Country of Belgium_



<div data-search-exclude markdown="1">



URI: [loc:BE](https://w3id.org/lmodel/dpv/loc/BE)





```mermaid
 classDiagram
    class BE
    click BE href "../BE/"
      EEA30 <|-- BE
        click EEA30 href "../EEA30/"
      EEA31 <|-- BE
        click EEA31 href "../EEA31/"
      EU <|-- BE
        click EU href "../EU/"
      EU27 <|-- BE
        click EU27 href "../EU27/"
      EU28 <|-- BE
        click EU28 href "../EU28/"
      EEA <|-- BE
        click EEA href "../EEA/"
      

      BE <|-- BEBRU
        click BEBRU href "../BEBRU/"
      BE <|-- BEVAN
        click BEVAN href "../BEVAN/"
      BE <|-- BEVBR
        click BEVBR href "../BEVBR/"
      BE <|-- BEVLI
        click BEVLI href "../BEVLI/"
      BE <|-- BEVOV
        click BEVOV href "../BEVOV/"
      BE <|-- BEVWV
        click BEVWV href "../BEVWV/"
      BE <|-- BEWAL
        click BEWAL href "../BEWAL/"
      BE <|-- BEWBR
        click BEWBR href "../BEWBR/"
      BE <|-- BEWHT
        click BEWHT href "../BEWHT/"
      BE <|-- BEWLG
        click BEWLG href "../BEWLG/"
      BE <|-- BEWLX
        click BEWLX href "../BEWLX/"
      BE <|-- BEWNA
        click BEWNA href "../BEWNA/"
      

      
```





## Inheritance
* [EEA](EEA.md)
    * **BE** [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * [BEBRU](BEBRU.md)
        * [BEVAN](BEVAN.md)
        * [BEVBR](BEVBR.md)
        * [BEVLI](BEVLI.md)
        * [BEVOV](BEVOV.md)
        * [BEVWV](BEVWV.md)
        * [BEWAL](BEWAL.md)
        * [BEWBR](BEWBR.md)
        * [BEWHT](BEWHT.md)
        * [BEWLG](BEWLG.md)
        * [BEWLX](BEWLX.md)
        * [BEWNA](BEWNA.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:BE](https://w3id.org/lmodel/dpv/loc/BE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Belgium




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#BE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:BE |
| native | loc:BE |
| exact | dpv_loc:BE, dpv_loc_owl:BE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Belgium
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Belgium
exact_mappings:
- dpv_loc:BE
- dpv_loc_owl:BE
is_a: EEA
mixins:
- EEA30
- EEA31
- EU
- EU27
- EU28
class_uri: loc:BE

```
</details>

### Induced

<details>
```yaml
name: BE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Belgium
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Belgium
exact_mappings:
- dpv_loc:BE
- dpv_loc_owl:BE
is_a: EEA
mixins:
- EEA30
- EEA31
- EU
- EU27
- EU28
class_uri: loc:BE

```
</details></div>