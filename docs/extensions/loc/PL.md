---
search:
  boost: 10.0
---

# Class: PL 


_Concept representing Country of Poland_



<div data-search-exclude markdown="1">



URI: [loc:PL](https://w3id.org/lmodel/dpv/loc/PL)





```mermaid
 classDiagram
    class PL
    click PL href "../PL/"
      EEA30 <|-- PL
        click EEA30 href "../EEA30/"
      EEA31 <|-- PL
        click EEA31 href "../EEA31/"
      EU <|-- PL
        click EU href "../EU/"
      EU27 <|-- PL
        click EU27 href "../EU27/"
      EU28 <|-- PL
        click EU28 href "../EU28/"
      EEA <|-- PL
        click EEA href "../EEA/"
      

      PL <|-- PL02
        click PL02 href "../PL02/"
      PL <|-- PL04
        click PL04 href "../PL04/"
      PL <|-- PL06
        click PL06 href "../PL06/"
      PL <|-- PL08
        click PL08 href "../PL08/"
      PL <|-- PL10
        click PL10 href "../PL10/"
      PL <|-- PL12
        click PL12 href "../PL12/"
      PL <|-- PL14
        click PL14 href "../PL14/"
      PL <|-- PL16
        click PL16 href "../PL16/"
      PL <|-- PL18
        click PL18 href "../PL18/"
      PL <|-- PL20
        click PL20 href "../PL20/"
      PL <|-- PL22
        click PL22 href "../PL22/"
      PL <|-- PL24
        click PL24 href "../PL24/"
      PL <|-- PL26
        click PL26 href "../PL26/"
      PL <|-- PL28
        click PL28 href "../PL28/"
      PL <|-- PL30
        click PL30 href "../PL30/"
      PL <|-- PL32
        click PL32 href "../PL32/"
      PL <|-- PLKI
        click PLKI href "../PLKI/"
      

      
```





## Inheritance
* [EEA](EEA.md)
    * **PL** [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * [PL02](PL02.md)
        * [PL04](PL04.md)
        * [PL06](PL06.md)
        * [PL08](PL08.md)
        * [PL10](PL10.md)
        * [PL12](PL12.md)
        * [PL14](PL14.md)
        * [PL16](PL16.md)
        * [PL18](PL18.md)
        * [PL20](PL20.md)
        * [PL22](PL22.md)
        * [PL24](PL24.md)
        * [PL26](PL26.md)
        * [PL28](PL28.md)
        * [PL30](PL30.md)
        * [PL32](PL32.md)
        * [PLKI](PLKI.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:PL](https://w3id.org/lmodel/dpv/loc/PL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Poland




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#PL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:PL |
| native | loc:PL |
| exact | dpv_loc:PL, dpv_loc_owl:PL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#PL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Poland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Poland
exact_mappings:
- dpv_loc:PL
- dpv_loc_owl:PL
is_a: EEA
mixins:
- EEA30
- EEA31
- EU
- EU27
- EU28
class_uri: loc:PL

```
</details>

### Induced

<details>
```yaml
name: PL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#PL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Poland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Poland
exact_mappings:
- dpv_loc:PL
- dpv_loc_owl:PL
is_a: EEA
mixins:
- EEA30
- EEA31
- EU
- EU27
- EU28
class_uri: loc:PL

```
</details></div>