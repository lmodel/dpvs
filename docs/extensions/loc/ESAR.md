---
search:
  boost: 10.0
---

# Class: ESAR 


_Concept representing region Aragon in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-AR](https://w3id.org/lmodel/dpv/loc/ES-AR)





```mermaid
 classDiagram
    class ESAR
    click ESAR href "../ESAR/"
      ES <|-- ESAR
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESAR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-AR](https://w3id.org/lmodel/dpv/loc/ES-AR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-AR
* Aragon




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-AR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-AR |
| native | loc:ESAR |
| exact | dpv_loc:ES-AR, dpv_loc_owl:ES-AR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESAR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-AR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Aragon in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-AR
- Aragon
exact_mappings:
- dpv_loc:ES-AR
- dpv_loc_owl:ES-AR
is_a: ES
class_uri: loc:ES-AR

```
</details>

### Induced

<details>
```yaml
name: ESAR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-AR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Aragon in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-AR
- Aragon
exact_mappings:
- dpv_loc:ES-AR
- dpv_loc_owl:ES-AR
is_a: ES
class_uri: loc:ES-AR

```
</details></div>