---
search:
  boost: 10.0
---

# Class: LUL 


_Concept representing region Former Luxembourg District in country_

_Luxembourg_



<div data-search-exclude markdown="1">



URI: [loc:LU-L](https://w3id.org/lmodel/dpv/loc/LU-L)





```mermaid
 classDiagram
    class LUL
    click LUL href "../LUL/"
      LU <|-- LUL
        click LU href "../LU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [LU](LU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **LUL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:LU-L](https://w3id.org/lmodel/dpv/loc/LU-L) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* LU-L
* Former Luxembourg District




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#LU-L |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:LU-L |
| native | loc:LUL |
| exact | dpv_loc:LU-L, dpv_loc_owl:LU-L |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LUL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LU-L
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Former Luxembourg District in country

  Luxembourg'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- LU-L
- Former Luxembourg District
exact_mappings:
- dpv_loc:LU-L
- dpv_loc_owl:LU-L
is_a: LU
class_uri: loc:LU-L

```
</details>

### Induced

<details>
```yaml
name: LUL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LU-L
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Former Luxembourg District in country

  Luxembourg'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- LU-L
- Former Luxembourg District
exact_mappings:
- dpv_loc:LU-L
- dpv_loc_owl:LU-L
is_a: LU
class_uri: loc:LU-L

```
</details></div>