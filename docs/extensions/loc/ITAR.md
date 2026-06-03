---
search:
  boost: 10.0
---

# Class: ITAR 


_Concept representing region Province of Arezzo in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-AR](https://w3id.org/lmodel/dpv/loc/IT-AR)





```mermaid
 classDiagram
    class ITAR
    click ITAR href "../ITAR/"
      IT <|-- ITAR
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITAR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-AR](https://w3id.org/lmodel/dpv/loc/IT-AR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-AR
* Province of Arezzo




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-AR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-AR |
| native | loc:ITAR |
| exact | dpv_loc:IT-AR, dpv_loc_owl:IT-AR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITAR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-AR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Arezzo in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-AR
- Province of Arezzo
exact_mappings:
- dpv_loc:IT-AR
- dpv_loc_owl:IT-AR
is_a: IT
class_uri: loc:IT-AR

```
</details>

### Induced

<details>
```yaml
name: ITAR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-AR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Arezzo in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-AR
- Province of Arezzo
exact_mappings:
- dpv_loc:IT-AR
- dpv_loc_owl:IT-AR
is_a: IT
class_uri: loc:IT-AR

```
</details></div>