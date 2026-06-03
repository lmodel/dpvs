---
search:
  boost: 10.0
---

# Class: ITAN 


_Concept representing region Province of Ancona in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-AN](https://w3id.org/lmodel/dpv/loc/IT-AN)





```mermaid
 classDiagram
    class ITAN
    click ITAN href "../ITAN/"
      IT <|-- ITAN
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITAN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-AN](https://w3id.org/lmodel/dpv/loc/IT-AN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-AN
* Province of Ancona




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-AN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-AN |
| native | loc:ITAN |
| exact | dpv_loc:IT-AN, dpv_loc_owl:IT-AN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITAN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-AN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Ancona in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-AN
- Province of Ancona
exact_mappings:
- dpv_loc:IT-AN
- dpv_loc_owl:IT-AN
is_a: IT
class_uri: loc:IT-AN

```
</details>

### Induced

<details>
```yaml
name: ITAN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-AN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Ancona in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-AN
- Province of Ancona
exact_mappings:
- dpv_loc:IT-AN
- dpv_loc_owl:IT-AN
is_a: IT
class_uri: loc:IT-AN

```
</details></div>