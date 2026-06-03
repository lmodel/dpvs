---
search:
  boost: 10.0
---

# Class: GBMAN 


_Concept representing region City of Manchester in country United Kingdom_

_of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-MAN](https://w3id.org/lmodel/dpv/loc/GB-MAN)





```mermaid
 classDiagram
    class GBMAN
    click GBMAN href "../GBMAN/"
      GB <|-- GBMAN
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBMAN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-MAN](https://w3id.org/lmodel/dpv/loc/GB-MAN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-MAN
* City of Manchester




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-MAN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-MAN |
| native | loc:GBMAN |
| exact | dpv_loc:GB-MAN, dpv_loc_owl:GB-MAN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBMAN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-MAN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region City of Manchester in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-MAN
- City of Manchester
exact_mappings:
- dpv_loc:GB-MAN
- dpv_loc_owl:GB-MAN
is_a: GB
class_uri: loc:GB-MAN

```
</details>

### Induced

<details>
```yaml
name: GBMAN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-MAN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region City of Manchester in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-MAN
- City of Manchester
exact_mappings:
- dpv_loc:GB-MAN
- dpv_loc_owl:GB-MAN
is_a: GB
class_uri: loc:GB-MAN

```
</details></div>