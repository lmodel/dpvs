---
search:
  boost: 10.0
---

# Class: ITPG 


_Concept representing region Province of Perugia in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-PG](https://w3id.org/lmodel/dpv/loc/IT-PG)





```mermaid
 classDiagram
    class ITPG
    click ITPG href "../ITPG/"
      IT <|-- ITPG
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITPG**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-PG](https://w3id.org/lmodel/dpv/loc/IT-PG) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-PG
* Province of Perugia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-PG |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-PG |
| native | loc:ITPG |
| exact | dpv_loc:IT-PG, dpv_loc_owl:IT-PG |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITPG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-PG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Perugia in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-PG
- Province of Perugia
exact_mappings:
- dpv_loc:IT-PG
- dpv_loc_owl:IT-PG
is_a: IT
class_uri: loc:IT-PG

```
</details>

### Induced

<details>
```yaml
name: ITPG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-PG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Perugia in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-PG
- Province of Perugia
exact_mappings:
- dpv_loc:IT-PG
- dpv_loc_owl:IT-PG
is_a: IT
class_uri: loc:IT-PG

```
</details></div>