---
search:
  boost: 10.0
---

# Class: PT 


_Concept representing Country of Portugal_



<div data-search-exclude markdown="1">



URI: [loc:PT](https://w3id.org/lmodel/dpv/loc/PT)





```mermaid
 classDiagram
    class PT
    click PT href "../PT/"
      EEA30 <|-- PT
        click EEA30 href "../EEA30/"
      EEA31 <|-- PT
        click EEA31 href "../EEA31/"
      EU <|-- PT
        click EU href "../EU/"
      EU27 <|-- PT
        click EU27 href "../EU27/"
      EU28 <|-- PT
        click EU28 href "../EU28/"
      EEA <|-- PT
        click EEA href "../EEA/"
      

      PT <|-- PT01
        click PT01 href "../PT01/"
      PT <|-- PT02
        click PT02 href "../PT02/"
      PT <|-- PT03
        click PT03 href "../PT03/"
      PT <|-- PT04
        click PT04 href "../PT04/"
      PT <|-- PT05
        click PT05 href "../PT05/"
      PT <|-- PT06
        click PT06 href "../PT06/"
      PT <|-- PT07
        click PT07 href "../PT07/"
      PT <|-- PT08
        click PT08 href "../PT08/"
      PT <|-- PT09
        click PT09 href "../PT09/"
      PT <|-- PT10
        click PT10 href "../PT10/"
      PT <|-- PT11
        click PT11 href "../PT11/"
      PT <|-- PT12
        click PT12 href "../PT12/"
      PT <|-- PT13
        click PT13 href "../PT13/"
      PT <|-- PT14
        click PT14 href "../PT14/"
      PT <|-- PT15
        click PT15 href "../PT15/"
      PT <|-- PT16
        click PT16 href "../PT16/"
      PT <|-- PT17
        click PT17 href "../PT17/"
      PT <|-- PT18
        click PT18 href "../PT18/"
      PT <|-- PT20
        click PT20 href "../PT20/"
      PT <|-- PT30
        click PT30 href "../PT30/"
      

      
```





## Inheritance
* [EEA](EEA.md)
    * **PT** [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * [PT01](PT01.md)
        * [PT02](PT02.md)
        * [PT03](PT03.md)
        * [PT04](PT04.md)
        * [PT05](PT05.md)
        * [PT06](PT06.md)
        * [PT07](PT07.md)
        * [PT08](PT08.md)
        * [PT09](PT09.md)
        * [PT10](PT10.md)
        * [PT11](PT11.md)
        * [PT12](PT12.md)
        * [PT13](PT13.md)
        * [PT14](PT14.md)
        * [PT15](PT15.md)
        * [PT16](PT16.md)
        * [PT17](PT17.md)
        * [PT18](PT18.md)
        * [PT20](PT20.md)
        * [PT30](PT30.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:PT](https://w3id.org/lmodel/dpv/loc/PT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Portugal




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#PT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:PT |
| native | loc:PT |
| exact | dpv_loc:PT, dpv_loc_owl:PT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#PT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Portugal
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Portugal
exact_mappings:
- dpv_loc:PT
- dpv_loc_owl:PT
is_a: EEA
mixins:
- EEA30
- EEA31
- EU
- EU27
- EU28
class_uri: loc:PT

```
</details>

### Induced

<details>
```yaml
name: PT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#PT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Portugal
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Portugal
exact_mappings:
- dpv_loc:PT
- dpv_loc_owl:PT
is_a: EEA
mixins:
- EEA30
- EEA31
- EU
- EU27
- EU28
class_uri: loc:PT

```
</details></div>