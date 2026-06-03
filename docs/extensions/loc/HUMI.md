---
search:
  boost: 10.0
---

# Class: HUMI 


_Concept representing region Miskolc in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-MI](https://w3id.org/lmodel/dpv/loc/HU-MI)





```mermaid
 classDiagram
    class HUMI
    click HUMI href "../HUMI/"
      HU <|-- HUMI
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUMI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-MI](https://w3id.org/lmodel/dpv/loc/HU-MI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-MI
* Miskolc




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-MI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-MI |
| native | loc:HUMI |
| exact | dpv_loc:HU-MI, dpv_loc_owl:HU-MI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUMI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-MI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Miskolc in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-MI
- Miskolc
exact_mappings:
- dpv_loc:HU-MI
- dpv_loc_owl:HU-MI
is_a: HU
class_uri: loc:HU-MI

```
</details>

### Induced

<details>
```yaml
name: HUMI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-MI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Miskolc in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-MI
- Miskolc
exact_mappings:
- dpv_loc:HU-MI
- dpv_loc_owl:HU-MI
is_a: HU
class_uri: loc:HU-MI

```
</details></div>