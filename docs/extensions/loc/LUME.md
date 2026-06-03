---
search:
  boost: 10.0
---

# Class: LUME 


_Concept representing region Canton of Mersch in country Luxembourg_



<div data-search-exclude markdown="1">



URI: [loc:LU-ME](https://w3id.org/lmodel/dpv/loc/LU-ME)





```mermaid
 classDiagram
    class LUME
    click LUME href "../LUME/"
      LU <|-- LUME
        click LU href "../LU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [LU](LU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **LUME**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:LU-ME](https://w3id.org/lmodel/dpv/loc/LU-ME) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* LU-ME
* Canton of Mersch




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#LU-ME |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:LU-ME |
| native | loc:LUME |
| exact | dpv_loc:LU-ME, dpv_loc_owl:LU-ME |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LUME
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LU-ME
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Canton of Mersch in country Luxembourg
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- LU-ME
- Canton of Mersch
exact_mappings:
- dpv_loc:LU-ME
- dpv_loc_owl:LU-ME
is_a: LU
class_uri: loc:LU-ME

```
</details>

### Induced

<details>
```yaml
name: LUME
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LU-ME
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Canton of Mersch in country Luxembourg
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- LU-ME
- Canton of Mersch
exact_mappings:
- dpv_loc:LU-ME
- dpv_loc_owl:LU-ME
is_a: LU
class_uri: loc:LU-ME

```
</details></div>