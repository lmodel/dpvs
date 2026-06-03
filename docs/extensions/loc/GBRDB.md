---
search:
  boost: 10.0
---

# Class: GBRDB 


_Concept representing region London Borough of Redbridge in country_

_United Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-RDB](https://w3id.org/lmodel/dpv/loc/GB-RDB)





```mermaid
 classDiagram
    class GBRDB
    click GBRDB href "../GBRDB/"
      GB <|-- GBRDB
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBRDB**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-RDB](https://w3id.org/lmodel/dpv/loc/GB-RDB) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-RDB
* London Borough of Redbridge




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-RDB |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-RDB |
| native | loc:GBRDB |
| exact | dpv_loc:GB-RDB, dpv_loc_owl:GB-RDB |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBRDB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-RDB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Redbridge in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-RDB
- London Borough of Redbridge
exact_mappings:
- dpv_loc:GB-RDB
- dpv_loc_owl:GB-RDB
is_a: GB
class_uri: loc:GB-RDB

```
</details>

### Induced

<details>
```yaml
name: GBRDB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-RDB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Redbridge in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-RDB
- London Borough of Redbridge
exact_mappings:
- dpv_loc:GB-RDB
- dpv_loc_owl:GB-RDB
is_a: GB
class_uri: loc:GB-RDB

```
</details></div>