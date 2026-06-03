---
search:
  boost: 10.0
---

# Class: ITBG 


_Concept representing region Province of Bergamo in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-BG](https://w3id.org/lmodel/dpv/loc/IT-BG)





```mermaid
 classDiagram
    class ITBG
    click ITBG href "../ITBG/"
      IT <|-- ITBG
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITBG**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-BG](https://w3id.org/lmodel/dpv/loc/IT-BG) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-BG
* Province of Bergamo




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-BG |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-BG |
| native | loc:ITBG |
| exact | dpv_loc:IT-BG, dpv_loc_owl:IT-BG |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITBG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-BG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Bergamo in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-BG
- Province of Bergamo
exact_mappings:
- dpv_loc:IT-BG
- dpv_loc_owl:IT-BG
is_a: IT
class_uri: loc:IT-BG

```
</details>

### Induced

<details>
```yaml
name: ITBG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-BG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Bergamo in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-BG
- Province of Bergamo
exact_mappings:
- dpv_loc:IT-BG
- dpv_loc_owl:IT-BG
is_a: IT
class_uri: loc:IT-BG

```
</details></div>