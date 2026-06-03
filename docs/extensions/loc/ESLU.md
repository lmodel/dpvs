---
search:
  boost: 10.0
---

# Class: ESLU 


_Concept representing region Province of Lugo in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-LU](https://w3id.org/lmodel/dpv/loc/ES-LU)





```mermaid
 classDiagram
    class ESLU
    click ESLU href "../ESLU/"
      ES <|-- ESLU
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESLU**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-LU](https://w3id.org/lmodel/dpv/loc/ES-LU) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-LU
* Province of Lugo




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-LU |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-LU |
| native | loc:ESLU |
| exact | dpv_loc:ES-LU, dpv_loc_owl:ES-LU |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESLU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-LU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Lugo in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-LU
- Province of Lugo
exact_mappings:
- dpv_loc:ES-LU
- dpv_loc_owl:ES-LU
is_a: ES
class_uri: loc:ES-LU

```
</details>

### Induced

<details>
```yaml
name: ESLU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-LU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Lugo in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-LU
- Province of Lugo
exact_mappings:
- dpv_loc:ES-LU
- dpv_loc_owl:ES-LU
is_a: ES
class_uri: loc:ES-LU

```
</details></div>