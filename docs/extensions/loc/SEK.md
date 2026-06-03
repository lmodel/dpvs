---
search:
  boost: 10.0
---

# Class: SEK 


_Concept representing region Blekinge in country Sweden_



<div data-search-exclude markdown="1">



URI: [loc:SE-K](https://w3id.org/lmodel/dpv/loc/SE-K)





```mermaid
 classDiagram
    class SEK
    click SEK href "../SEK/"
      SE <|-- SEK
        click SE href "../SE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SE](SE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SEK**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SE-K](https://w3id.org/lmodel/dpv/loc/SE-K) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SE-K
* Blekinge




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SE-K |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SE-K |
| native | loc:SEK |
| exact | dpv_loc:SE-K, dpv_loc_owl:SE-K |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SEK
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-K
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Blekinge in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-K
- Blekinge
exact_mappings:
- dpv_loc:SE-K
- dpv_loc_owl:SE-K
is_a: SE
class_uri: loc:SE-K

```
</details>

### Induced

<details>
```yaml
name: SEK
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-K
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Blekinge in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-K
- Blekinge
exact_mappings:
- dpv_loc:SE-K
- dpv_loc_owl:SE-K
is_a: SE
class_uri: loc:SE-K

```
</details></div>