---
search:
  boost: 10.0
---

# Class: ROMS 


_Concept representing region Mureș County in country Romania_



<div data-search-exclude markdown="1">



URI: [loc:RO-MS](https://w3id.org/lmodel/dpv/loc/RO-MS)





```mermaid
 classDiagram
    class ROMS
    click ROMS href "../ROMS/"
      RO <|-- ROMS
        click RO href "../RO/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [RO](RO.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ROMS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RO-MS](https://w3id.org/lmodel/dpv/loc/RO-MS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* RO-MS
* Mureș County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RO-MS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RO-MS |
| native | loc:ROMS |
| exact | dpv_loc:RO-MS, dpv_loc_owl:RO-MS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ROMS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-MS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Mureș County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-MS
- Mureș County
exact_mappings:
- dpv_loc:RO-MS
- dpv_loc_owl:RO-MS
is_a: RO
class_uri: loc:RO-MS

```
</details>

### Induced

<details>
```yaml
name: ROMS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-MS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Mureș County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-MS
- Mureș County
exact_mappings:
- dpv_loc:RO-MS
- dpv_loc_owl:RO-MS
is_a: RO
class_uri: loc:RO-MS

```
</details></div>