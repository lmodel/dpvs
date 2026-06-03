---
search:
  boost: 10.0
---

# Class: HUTB 


_Concept representing region Tatabánya in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-TB](https://w3id.org/lmodel/dpv/loc/HU-TB)





```mermaid
 classDiagram
    class HUTB
    click HUTB href "../HUTB/"
      HU <|-- HUTB
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUTB**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-TB](https://w3id.org/lmodel/dpv/loc/HU-TB) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-TB
* Tatabánya




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-TB |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-TB |
| native | loc:HUTB |
| exact | dpv_loc:HU-TB, dpv_loc_owl:HU-TB |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUTB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-TB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Tatabánya in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-TB
- Tatabánya
exact_mappings:
- dpv_loc:HU-TB
- dpv_loc_owl:HU-TB
is_a: HU
class_uri: loc:HU-TB

```
</details>

### Induced

<details>
```yaml
name: HUTB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-TB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Tatabánya in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-TB
- Tatabánya
exact_mappings:
- dpv_loc:HU-TB
- dpv_loc_owl:HU-TB
is_a: HU
class_uri: loc:HU-TB

```
</details></div>