---
search:
  boost: 10.0
---

# Class: LUDI 


_Concept representing region Canton of Diekirch in country Luxembourg_



<div data-search-exclude markdown="1">



URI: [loc:LU-DI](https://w3id.org/lmodel/dpv/loc/LU-DI)





```mermaid
 classDiagram
    class LUDI
    click LUDI href "../LUDI/"
      LU <|-- LUDI
        click LU href "../LU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [LU](LU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **LUDI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:LU-DI](https://w3id.org/lmodel/dpv/loc/LU-DI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* LU-DI
* Canton of Diekirch




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#LU-DI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:LU-DI |
| native | loc:LUDI |
| exact | dpv_loc:LU-DI, dpv_loc_owl:LU-DI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LUDI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LU-DI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Canton of Diekirch in country Luxembourg
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- LU-DI
- Canton of Diekirch
exact_mappings:
- dpv_loc:LU-DI
- dpv_loc_owl:LU-DI
is_a: LU
class_uri: loc:LU-DI

```
</details>

### Induced

<details>
```yaml
name: LUDI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LU-DI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Canton of Diekirch in country Luxembourg
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- LU-DI
- Canton of Diekirch
exact_mappings:
- dpv_loc:LU-DI
- dpv_loc_owl:LU-DI
is_a: LU
class_uri: loc:LU-DI

```
</details></div>