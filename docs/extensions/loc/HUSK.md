---
search:
  boost: 10.0
---

# Class: HUSK 


_Concept representing region Szolnok in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-SK](https://w3id.org/lmodel/dpv/loc/HU-SK)





```mermaid
 classDiagram
    class HUSK
    click HUSK href "../HUSK/"
      HU <|-- HUSK
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUSK**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-SK](https://w3id.org/lmodel/dpv/loc/HU-SK) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-SK
* Szolnok




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-SK |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-SK |
| native | loc:HUSK |
| exact | dpv_loc:HU-SK, dpv_loc_owl:HU-SK |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUSK
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-SK
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Szolnok in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-SK
- Szolnok
exact_mappings:
- dpv_loc:HU-SK
- dpv_loc_owl:HU-SK
is_a: HU
class_uri: loc:HU-SK

```
</details>

### Induced

<details>
```yaml
name: HUSK
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-SK
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Szolnok in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-SK
- Szolnok
exact_mappings:
- dpv_loc:HU-SK
- dpv_loc_owl:HU-SK
is_a: HU
class_uri: loc:HU-SK

```
</details></div>