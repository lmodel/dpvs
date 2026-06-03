---
search:
  boost: 10.0
---

# Class: ISDJU 


_Concept representing region Djúpivogur in country Iceland_



<div data-search-exclude markdown="1">



URI: [loc:IS-DJU](https://w3id.org/lmodel/dpv/loc/IS-DJU)





```mermaid
 classDiagram
    class ISDJU
    click ISDJU href "../ISDJU/"
      IS <|-- ISDJU
        click IS href "../IS/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IS](IS.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **ISDJU**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IS-DJU](https://w3id.org/lmodel/dpv/loc/IS-DJU) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IS-DJU
* Djúpivogur




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IS-DJU |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IS-DJU |
| native | loc:ISDJU |
| exact | dpv_loc:IS-DJU, dpv_loc_owl:IS-DJU |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ISDJU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-DJU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Djúpivogur in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-DJU
- Djúpivogur
exact_mappings:
- dpv_loc:IS-DJU
- dpv_loc_owl:IS-DJU
is_a: IS
class_uri: loc:IS-DJU

```
</details>

### Induced

<details>
```yaml
name: ISDJU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-DJU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Djúpivogur in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-DJU
- Djúpivogur
exact_mappings:
- dpv_loc:IS-DJU
- dpv_loc_owl:IS-DJU
is_a: IS
class_uri: loc:IS-DJU

```
</details></div>