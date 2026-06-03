---
search:
  boost: 10.0
---

# Class: ITPE 


_Concept representing region Province of Pescara in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-PE](https://w3id.org/lmodel/dpv/loc/IT-PE)





```mermaid
 classDiagram
    class ITPE
    click ITPE href "../ITPE/"
      IT <|-- ITPE
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITPE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-PE](https://w3id.org/lmodel/dpv/loc/IT-PE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-PE
* Province of Pescara




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-PE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-PE |
| native | loc:ITPE |
| exact | dpv_loc:IT-PE, dpv_loc_owl:IT-PE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITPE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-PE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Pescara in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-PE
- Province of Pescara
exact_mappings:
- dpv_loc:IT-PE
- dpv_loc_owl:IT-PE
is_a: IT
class_uri: loc:IT-PE

```
</details>

### Induced

<details>
```yaml
name: ITPE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-PE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Pescara in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-PE
- Province of Pescara
exact_mappings:
- dpv_loc:IT-PE
- dpv_loc_owl:IT-PE
is_a: IT
class_uri: loc:IT-PE

```
</details></div>