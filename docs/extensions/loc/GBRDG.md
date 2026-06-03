---
search:
  boost: 10.0
---

# Class: GBRDG 


_Concept representing region Reading, Berkshire in country United Kingdom_

_of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-RDG](https://w3id.org/lmodel/dpv/loc/GB-RDG)





```mermaid
 classDiagram
    class GBRDG
    click GBRDG href "../GBRDG/"
      GB <|-- GBRDG
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBRDG**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-RDG](https://w3id.org/lmodel/dpv/loc/GB-RDG) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-RDG
* Reading, Berkshire




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-RDG |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-RDG |
| native | loc:GBRDG |
| exact | dpv_loc:GB-RDG, dpv_loc_owl:GB-RDG |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBRDG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-RDG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Reading, Berkshire in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-RDG
- Reading, Berkshire
exact_mappings:
- dpv_loc:GB-RDG
- dpv_loc_owl:GB-RDG
is_a: GB
class_uri: loc:GB-RDG

```
</details>

### Induced

<details>
```yaml
name: GBRDG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-RDG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Reading, Berkshire in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-RDG
- Reading, Berkshire
exact_mappings:
- dpv_loc:GB-RDG
- dpv_loc_owl:GB-RDG
is_a: GB
class_uri: loc:GB-RDG

```
</details></div>