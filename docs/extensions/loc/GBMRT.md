---
search:
  boost: 10.0
---

# Class: GBMRT 


_Concept representing region London Borough of Merton in country United_

_Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-MRT](https://w3id.org/lmodel/dpv/loc/GB-MRT)





```mermaid
 classDiagram
    class GBMRT
    click GBMRT href "../GBMRT/"
      GB <|-- GBMRT
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBMRT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-MRT](https://w3id.org/lmodel/dpv/loc/GB-MRT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-MRT
* London Borough of Merton




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-MRT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-MRT |
| native | loc:GBMRT |
| exact | dpv_loc:GB-MRT, dpv_loc_owl:GB-MRT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBMRT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-MRT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Merton in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-MRT
- London Borough of Merton
exact_mappings:
- dpv_loc:GB-MRT
- dpv_loc_owl:GB-MRT
is_a: GB
class_uri: loc:GB-MRT

```
</details>

### Induced

<details>
```yaml
name: GBMRT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-MRT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Merton in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-MRT
- London Borough of Merton
exact_mappings:
- dpv_loc:GB-MRT
- dpv_loc_owl:GB-MRT
is_a: GB
class_uri: loc:GB-MRT

```
</details></div>