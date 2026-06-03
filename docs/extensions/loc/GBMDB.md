---
search:
  boost: 10.0
---

# Class: GBMDB 


_Concept representing region Borough of Middlesbrough in country United_

_Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-MDB](https://w3id.org/lmodel/dpv/loc/GB-MDB)





```mermaid
 classDiagram
    class GBMDB
    click GBMDB href "../GBMDB/"
      GB <|-- GBMDB
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBMDB**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-MDB](https://w3id.org/lmodel/dpv/loc/GB-MDB) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-MDB
* Borough of Middlesbrough




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-MDB |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-MDB |
| native | loc:GBMDB |
| exact | dpv_loc:GB-MDB, dpv_loc_owl:GB-MDB |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBMDB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-MDB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Borough of Middlesbrough in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-MDB
- Borough of Middlesbrough
exact_mappings:
- dpv_loc:GB-MDB
- dpv_loc_owl:GB-MDB
is_a: GB
class_uri: loc:GB-MDB

```
</details>

### Induced

<details>
```yaml
name: GBMDB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-MDB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Borough of Middlesbrough in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-MDB
- Borough of Middlesbrough
exact_mappings:
- dpv_loc:GB-MDB
- dpv_loc_owl:GB-MDB
is_a: GB
class_uri: loc:GB-MDB

```
</details></div>