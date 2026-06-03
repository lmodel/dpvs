---
search:
  boost: 10.0
---

# Class: ESNC 


_Concept representing region Navarre in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-NC](https://w3id.org/lmodel/dpv/loc/ES-NC)





```mermaid
 classDiagram
    class ESNC
    click ESNC href "../ESNC/"
      ES <|-- ESNC
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESNC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-NC](https://w3id.org/lmodel/dpv/loc/ES-NC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-NC
* Navarre




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-NC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-NC |
| native | loc:ESNC |
| exact | dpv_loc:ES-NC, dpv_loc_owl:ES-NC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESNC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-NC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Navarre in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-NC
- Navarre
exact_mappings:
- dpv_loc:ES-NC
- dpv_loc_owl:ES-NC
is_a: ES
class_uri: loc:ES-NC

```
</details>

### Induced

<details>
```yaml
name: ESNC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-NC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Navarre in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-NC
- Navarre
exact_mappings:
- dpv_loc:ES-NC
- dpv_loc_owl:ES-NC
is_a: ES
class_uri: loc:ES-NC

```
</details></div>