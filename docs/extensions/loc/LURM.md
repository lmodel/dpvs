---
search:
  boost: 10.0
---

# Class: LURM 


_Concept representing region Canton of Remich in country Luxembourg_



<div data-search-exclude markdown="1">



URI: [loc:LU-RM](https://w3id.org/lmodel/dpv/loc/LU-RM)





```mermaid
 classDiagram
    class LURM
    click LURM href "../LURM/"
      LU <|-- LURM
        click LU href "../LU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [LU](LU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **LURM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:LU-RM](https://w3id.org/lmodel/dpv/loc/LU-RM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* LU-RM
* Canton of Remich




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#LU-RM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:LU-RM |
| native | loc:LURM |
| exact | dpv_loc:LU-RM, dpv_loc_owl:LU-RM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LURM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LU-RM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Canton of Remich in country Luxembourg
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- LU-RM
- Canton of Remich
exact_mappings:
- dpv_loc:LU-RM
- dpv_loc_owl:LU-RM
is_a: LU
class_uri: loc:LU-RM

```
</details>

### Induced

<details>
```yaml
name: LURM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LU-RM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Canton of Remich in country Luxembourg
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- LU-RM
- Canton of Remich
exact_mappings:
- dpv_loc:LU-RM
- dpv_loc_owl:LU-RM
is_a: LU
class_uri: loc:LU-RM

```
</details></div>