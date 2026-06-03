---
search:
  boost: 10.0
---

# Class: ITLU 


_Concept representing region Province of Lucca in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-LU](https://w3id.org/lmodel/dpv/loc/IT-LU)





```mermaid
 classDiagram
    class ITLU
    click ITLU href "../ITLU/"
      IT <|-- ITLU
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITLU**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-LU](https://w3id.org/lmodel/dpv/loc/IT-LU) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-LU
* Province of Lucca




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-LU |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-LU |
| native | loc:ITLU |
| exact | dpv_loc:IT-LU, dpv_loc_owl:IT-LU |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITLU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-LU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Lucca in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-LU
- Province of Lucca
exact_mappings:
- dpv_loc:IT-LU
- dpv_loc_owl:IT-LU
is_a: IT
class_uri: loc:IT-LU

```
</details>

### Induced

<details>
```yaml
name: ITLU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-LU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Lucca in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-LU
- Province of Lucca
exact_mappings:
- dpv_loc:IT-LU
- dpv_loc_owl:IT-LU
is_a: IT
class_uri: loc:IT-LU

```
</details></div>