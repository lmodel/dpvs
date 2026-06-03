---
search:
  boost: 10.0
---

# Class: HUGY 


_Concept representing region Győr in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-GY](https://w3id.org/lmodel/dpv/loc/HU-GY)





```mermaid
 classDiagram
    class HUGY
    click HUGY href "../HUGY/"
      HU <|-- HUGY
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUGY**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-GY](https://w3id.org/lmodel/dpv/loc/HU-GY) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-GY
* Győr




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-GY |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-GY |
| native | loc:HUGY |
| exact | dpv_loc:HU-GY, dpv_loc_owl:HU-GY |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUGY
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-GY
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Győr in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-GY
- Győr
exact_mappings:
- dpv_loc:HU-GY
- dpv_loc_owl:HU-GY
is_a: HU
class_uri: loc:HU-GY

```
</details>

### Induced

<details>
```yaml
name: HUGY
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-GY
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Győr in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-GY
- Győr
exact_mappings:
- dpv_loc:HU-GY
- dpv_loc_owl:HU-GY
is_a: HU
class_uri: loc:HU-GY

```
</details></div>