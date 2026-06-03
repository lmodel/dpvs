---
search:
  boost: 10.0
---

# Class: ROIF 


_Concept representing region Ilfov County in country Romania_



<div data-search-exclude markdown="1">



URI: [loc:RO-IF](https://w3id.org/lmodel/dpv/loc/RO-IF)





```mermaid
 classDiagram
    class ROIF
    click ROIF href "../ROIF/"
      RO <|-- ROIF
        click RO href "../RO/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [RO](RO.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ROIF**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RO-IF](https://w3id.org/lmodel/dpv/loc/RO-IF) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* RO-IF
* Ilfov County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RO-IF |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RO-IF |
| native | loc:ROIF |
| exact | dpv_loc:RO-IF, dpv_loc_owl:RO-IF |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ROIF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-IF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ilfov County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-IF
- Ilfov County
exact_mappings:
- dpv_loc:RO-IF
- dpv_loc_owl:RO-IF
is_a: RO
class_uri: loc:RO-IF

```
</details>

### Induced

<details>
```yaml
name: ROIF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-IF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ilfov County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-IF
- Ilfov County
exact_mappings:
- dpv_loc:RO-IF
- dpv_loc_owl:RO-IF
is_a: RO
class_uri: loc:RO-IF

```
</details></div>