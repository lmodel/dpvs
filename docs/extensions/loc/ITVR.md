---
search:
  boost: 10.0
---

# Class: ITVR 


_Concept representing region Province of Verona in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-VR](https://w3id.org/lmodel/dpv/loc/IT-VR)





```mermaid
 classDiagram
    class ITVR
    click ITVR href "../ITVR/"
      IT <|-- ITVR
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITVR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-VR](https://w3id.org/lmodel/dpv/loc/IT-VR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-VR
* Province of Verona




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-VR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-VR |
| native | loc:ITVR |
| exact | dpv_loc:IT-VR, dpv_loc_owl:IT-VR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITVR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-VR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Verona in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-VR
- Province of Verona
exact_mappings:
- dpv_loc:IT-VR
- dpv_loc_owl:IT-VR
is_a: IT
class_uri: loc:IT-VR

```
</details>

### Induced

<details>
```yaml
name: ITVR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-VR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Verona in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-VR
- Province of Verona
exact_mappings:
- dpv_loc:IT-VR
- dpv_loc_owl:IT-VR
is_a: IT
class_uri: loc:IT-VR

```
</details></div>