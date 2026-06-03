---
search:
  boost: 10.0
---

# Class: ITTV 


_Concept representing region Province of Treviso in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-TV](https://w3id.org/lmodel/dpv/loc/IT-TV)





```mermaid
 classDiagram
    class ITTV
    click ITTV href "../ITTV/"
      IT <|-- ITTV
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITTV**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-TV](https://w3id.org/lmodel/dpv/loc/IT-TV) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-TV
* Province of Treviso




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-TV |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-TV |
| native | loc:ITTV |
| exact | dpv_loc:IT-TV, dpv_loc_owl:IT-TV |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITTV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-TV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Treviso in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-TV
- Province of Treviso
exact_mappings:
- dpv_loc:IT-TV
- dpv_loc_owl:IT-TV
is_a: IT
class_uri: loc:IT-TV

```
</details>

### Induced

<details>
```yaml
name: ITTV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-TV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Treviso in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-TV
- Province of Treviso
exact_mappings:
- dpv_loc:IT-TV
- dpv_loc_owl:IT-TV
is_a: IT
class_uri: loc:IT-TV

```
</details></div>