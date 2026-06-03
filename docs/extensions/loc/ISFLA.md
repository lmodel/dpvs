---
search:
  boost: 10.0
---

# Class: ISFLA 


_Concept representing region Flóahreppur in country Iceland_



<div data-search-exclude markdown="1">



URI: [loc:IS-FLA](https://w3id.org/lmodel/dpv/loc/IS-FLA)





```mermaid
 classDiagram
    class ISFLA
    click ISFLA href "../ISFLA/"
      IS <|-- ISFLA
        click IS href "../IS/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IS](IS.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **ISFLA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IS-FLA](https://w3id.org/lmodel/dpv/loc/IS-FLA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IS-FLA
* Flóahreppur




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IS-FLA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IS-FLA |
| native | loc:ISFLA |
| exact | dpv_loc:IS-FLA, dpv_loc_owl:IS-FLA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ISFLA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-FLA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Flóahreppur in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-FLA
- Flóahreppur
exact_mappings:
- dpv_loc:IS-FLA
- dpv_loc_owl:IS-FLA
is_a: IS
class_uri: loc:IS-FLA

```
</details>

### Induced

<details>
```yaml
name: ISFLA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-FLA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Flóahreppur in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-FLA
- Flóahreppur
exact_mappings:
- dpv_loc:IS-FLA
- dpv_loc_owl:IS-FLA
is_a: IS
class_uri: loc:IS-FLA

```
</details></div>