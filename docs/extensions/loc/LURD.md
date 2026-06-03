---
search:
  boost: 10.0
---

# Class: LURD 


_Concept representing region Canton of Redange in country Luxembourg_



<div data-search-exclude markdown="1">



URI: [loc:LU-RD](https://w3id.org/lmodel/dpv/loc/LU-RD)





```mermaid
 classDiagram
    class LURD
    click LURD href "../LURD/"
      LU <|-- LURD
        click LU href "../LU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [LU](LU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **LURD**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:LU-RD](https://w3id.org/lmodel/dpv/loc/LU-RD) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* LU-RD
* Canton of Redange




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#LU-RD |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:LU-RD |
| native | loc:LURD |
| exact | dpv_loc:LU-RD, dpv_loc_owl:LU-RD |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LURD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LU-RD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Canton of Redange in country Luxembourg
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- LU-RD
- Canton of Redange
exact_mappings:
- dpv_loc:LU-RD
- dpv_loc_owl:LU-RD
is_a: LU
class_uri: loc:LU-RD

```
</details>

### Induced

<details>
```yaml
name: LURD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LU-RD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Canton of Redange in country Luxembourg
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- LU-RD
- Canton of Redange
exact_mappings:
- dpv_loc:LU-RD
- dpv_loc_owl:LU-RD
is_a: LU
class_uri: loc:LU-RD

```
</details></div>