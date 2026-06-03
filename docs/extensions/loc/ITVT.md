---
search:
  boost: 10.0
---

# Class: ITVT 


_Concept representing region Province of Viterbo in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-VT](https://w3id.org/lmodel/dpv/loc/IT-VT)





```mermaid
 classDiagram
    class ITVT
    click ITVT href "../ITVT/"
      IT <|-- ITVT
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITVT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-VT](https://w3id.org/lmodel/dpv/loc/IT-VT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-VT
* Province of Viterbo




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-VT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-VT |
| native | loc:ITVT |
| exact | dpv_loc:IT-VT, dpv_loc_owl:IT-VT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITVT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-VT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Viterbo in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-VT
- Province of Viterbo
exact_mappings:
- dpv_loc:IT-VT
- dpv_loc_owl:IT-VT
is_a: IT
class_uri: loc:IT-VT

```
</details>

### Induced

<details>
```yaml
name: ITVT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-VT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Viterbo in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-VT
- Province of Viterbo
exact_mappings:
- dpv_loc:IT-VT
- dpv_loc_owl:IT-VT
is_a: IT
class_uri: loc:IT-VT

```
</details></div>