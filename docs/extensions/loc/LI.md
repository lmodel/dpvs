---
search:
  boost: 10.0
---

# Class: LI 


_Concept representing Country of Liechtenstein_



<div data-search-exclude markdown="1">



URI: [loc:LI](https://w3id.org/lmodel/dpv/loc/LI)





```mermaid
 classDiagram
    class LI
    click LI href "../LI/"
      EEA30 <|-- LI
        click EEA30 href "../EEA30/"
      EEA31 <|-- LI
        click EEA31 href "../EEA31/"
      EEA <|-- LI
        click EEA href "../EEA/"
      

      LI <|-- LI01
        click LI01 href "../LI01/"
      LI <|-- LI02
        click LI02 href "../LI02/"
      LI <|-- LI03
        click LI03 href "../LI03/"
      LI <|-- LI04
        click LI04 href "../LI04/"
      LI <|-- LI05
        click LI05 href "../LI05/"
      LI <|-- LI06
        click LI06 href "../LI06/"
      LI <|-- LI07
        click LI07 href "../LI07/"
      LI <|-- LI08
        click LI08 href "../LI08/"
      LI <|-- LI09
        click LI09 href "../LI09/"
      LI <|-- LI10
        click LI10 href "../LI10/"
      LI <|-- LI11
        click LI11 href "../LI11/"
      

      
```





## Inheritance
* [EEA](EEA.md)
    * **LI** [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * [LI01](LI01.md)
        * [LI02](LI02.md)
        * [LI03](LI03.md)
        * [LI04](LI04.md)
        * [LI05](LI05.md)
        * [LI06](LI06.md)
        * [LI07](LI07.md)
        * [LI08](LI08.md)
        * [LI09](LI09.md)
        * [LI10](LI10.md)
        * [LI11](LI11.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:LI](https://w3id.org/lmodel/dpv/loc/LI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Liechtenstein




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#LI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:LI |
| native | loc:LI |
| exact | dpv_loc:LI, dpv_loc_owl:LI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Liechtenstein
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Liechtenstein
exact_mappings:
- dpv_loc:LI
- dpv_loc_owl:LI
is_a: EEA
mixins:
- EEA30
- EEA31
class_uri: loc:LI

```
</details>

### Induced

<details>
```yaml
name: LI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Liechtenstein
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Liechtenstein
exact_mappings:
- dpv_loc:LI
- dpv_loc_owl:LI
is_a: EEA
mixins:
- EEA30
- EEA31
class_uri: loc:LI

```
</details></div>