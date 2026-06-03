---
search:
  boost: 10.0
---

# Class: SEI 


_Concept representing region Gotland in country Sweden_



<div data-search-exclude markdown="1">



URI: [loc:SE-I](https://w3id.org/lmodel/dpv/loc/SE-I)





```mermaid
 classDiagram
    class SEI
    click SEI href "../SEI/"
      SE <|-- SEI
        click SE href "../SE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SE](SE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SEI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SE-I](https://w3id.org/lmodel/dpv/loc/SE-I) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SE-I
* Gotland




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SE-I |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SE-I |
| native | loc:SEI |
| exact | dpv_loc:SE-I, dpv_loc_owl:SE-I |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SEI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-I
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Gotland in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-I
- Gotland
exact_mappings:
- dpv_loc:SE-I
- dpv_loc_owl:SE-I
is_a: SE
class_uri: loc:SE-I

```
</details>

### Induced

<details>
```yaml
name: SEI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-I
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Gotland in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-I
- Gotland
exact_mappings:
- dpv_loc:SE-I
- dpv_loc_owl:SE-I
is_a: SE
class_uri: loc:SE-I

```
</details></div>