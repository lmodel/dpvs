---
search:
  boost: 10.0
---

# Class: DK 


_Concept representing Country of Denmark_



<div data-search-exclude markdown="1">



URI: [loc:DK](https://w3id.org/lmodel/dpv/loc/DK)





```mermaid
 classDiagram
    class DK
    click DK href "../DK/"
      EEA30 <|-- DK
        click EEA30 href "../EEA30/"
      EEA31 <|-- DK
        click EEA31 href "../EEA31/"
      EU <|-- DK
        click EU href "../EU/"
      EU27 <|-- DK
        click EU27 href "../EU27/"
      EU28 <|-- DK
        click EU28 href "../EU28/"
      EEA <|-- DK
        click EEA href "../EEA/"
      

      DK <|-- DK81
        click DK81 href "../DK81/"
      DK <|-- DK82
        click DK82 href "../DK82/"
      DK <|-- DK83
        click DK83 href "../DK83/"
      DK <|-- DK84
        click DK84 href "../DK84/"
      DK <|-- DK85
        click DK85 href "../DK85/"
      DK <|-- DKGL
        click DKGL href "../DKGL/"
      

      
```





## Inheritance
* [EEA](EEA.md)
    * **DK** [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * [DK81](DK81.md)
        * [DK82](DK82.md)
        * [DK83](DK83.md)
        * [DK84](DK84.md)
        * [DK85](DK85.md)
        * [DKGL](DKGL.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:DK](https://w3id.org/lmodel/dpv/loc/DK) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Denmark




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#DK |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:DK |
| native | loc:DK |
| exact | dpv_loc:DK, dpv_loc_owl:DK |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DK
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DK
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Denmark
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Denmark
exact_mappings:
- dpv_loc:DK
- dpv_loc_owl:DK
is_a: EEA
mixins:
- EEA30
- EEA31
- EU
- EU27
- EU28
class_uri: loc:DK

```
</details>

### Induced

<details>
```yaml
name: DK
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DK
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Denmark
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Denmark
exact_mappings:
- dpv_loc:DK
- dpv_loc_owl:DK
is_a: EEA
mixins:
- EEA30
- EEA31
- EU
- EU27
- EU28
class_uri: loc:DK

```
</details></div>