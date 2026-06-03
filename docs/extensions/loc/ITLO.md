---
search:
  boost: 10.0
---

# Class: ITLO 


_Concept representing region Province of Lodi in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-LO](https://w3id.org/lmodel/dpv/loc/IT-LO)





```mermaid
 classDiagram
    class ITLO
    click ITLO href "../ITLO/"
      IT <|-- ITLO
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITLO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-LO](https://w3id.org/lmodel/dpv/loc/IT-LO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-LO
* Province of Lodi




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-LO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-LO |
| native | loc:ITLO |
| exact | dpv_loc:IT-LO, dpv_loc_owl:IT-LO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITLO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-LO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Lodi in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-LO
- Province of Lodi
exact_mappings:
- dpv_loc:IT-LO
- dpv_loc_owl:IT-LO
is_a: IT
class_uri: loc:IT-LO

```
</details>

### Induced

<details>
```yaml
name: ITLO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-LO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Lodi in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-LO
- Province of Lodi
exact_mappings:
- dpv_loc:IT-LO
- dpv_loc_owl:IT-LO
is_a: IT
class_uri: loc:IT-LO

```
</details></div>