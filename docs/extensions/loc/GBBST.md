---
search:
  boost: 10.0
---

# Class: GBBST 


_Concept representing region Bristol in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-BST](https://w3id.org/lmodel/dpv/loc/GB-BST)





```mermaid
 classDiagram
    class GBBST
    click GBBST href "../GBBST/"
      GB <|-- GBBST
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBBST**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-BST](https://w3id.org/lmodel/dpv/loc/GB-BST) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-BST
* Bristol




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-BST |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-BST |
| native | loc:GBBST |
| exact | dpv_loc:GB-BST, dpv_loc_owl:GB-BST |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBBST
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-BST
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Bristol in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-BST
- Bristol
exact_mappings:
- dpv_loc:GB-BST
- dpv_loc_owl:GB-BST
is_a: GB
class_uri: loc:GB-BST

```
</details>

### Induced

<details>
```yaml
name: GBBST
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-BST
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Bristol in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-BST
- Bristol
exact_mappings:
- dpv_loc:GB-BST
- dpv_loc_owl:GB-BST
is_a: GB
class_uri: loc:GB-BST

```
</details></div>