---
search:
  boost: 10.0
---

# Class: ITBL 


_Concept representing region Province of Belluno in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-BL](https://w3id.org/lmodel/dpv/loc/IT-BL)





```mermaid
 classDiagram
    class ITBL
    click ITBL href "../ITBL/"
      IT <|-- ITBL
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITBL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-BL](https://w3id.org/lmodel/dpv/loc/IT-BL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-BL
* Province of Belluno




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-BL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-BL |
| native | loc:ITBL |
| exact | dpv_loc:IT-BL, dpv_loc_owl:IT-BL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITBL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-BL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Belluno in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-BL
- Province of Belluno
exact_mappings:
- dpv_loc:IT-BL
- dpv_loc_owl:IT-BL
is_a: IT
class_uri: loc:IT-BL

```
</details>

### Induced

<details>
```yaml
name: ITBL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-BL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Belluno in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-BL
- Province of Belluno
exact_mappings:
- dpv_loc:IT-BL
- dpv_loc_owl:IT-BL
is_a: IT
class_uri: loc:IT-BL

```
</details></div>