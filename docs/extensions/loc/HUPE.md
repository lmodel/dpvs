---
search:
  boost: 10.0
---

# Class: HUPE 


_Concept representing region Pest County in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-PE](https://w3id.org/lmodel/dpv/loc/HU-PE)





```mermaid
 classDiagram
    class HUPE
    click HUPE href "../HUPE/"
      HU <|-- HUPE
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUPE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-PE](https://w3id.org/lmodel/dpv/loc/HU-PE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-PE
* Pest County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-PE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-PE |
| native | loc:HUPE |
| exact | dpv_loc:HU-PE, dpv_loc_owl:HU-PE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUPE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-PE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Pest County in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-PE
- Pest County
exact_mappings:
- dpv_loc:HU-PE
- dpv_loc_owl:HU-PE
is_a: HU
class_uri: loc:HU-PE

```
</details>

### Induced

<details>
```yaml
name: HUPE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-PE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Pest County in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-PE
- Pest County
exact_mappings:
- dpv_loc:HU-PE
- dpv_loc_owl:HU-PE
is_a: HU
class_uri: loc:HU-PE

```
</details></div>