---
search:
  boost: 10.0
---

# Class: ROMM 


_Concept representing region Maramureș County in country Romania_



<div data-search-exclude markdown="1">



URI: [loc:RO-MM](https://w3id.org/lmodel/dpv/loc/RO-MM)





```mermaid
 classDiagram
    class ROMM
    click ROMM href "../ROMM/"
      RO <|-- ROMM
        click RO href "../RO/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [RO](RO.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ROMM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RO-MM](https://w3id.org/lmodel/dpv/loc/RO-MM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* RO-MM
* Maramureș County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RO-MM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RO-MM |
| native | loc:ROMM |
| exact | dpv_loc:RO-MM, dpv_loc_owl:RO-MM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ROMM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-MM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Maramureș County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-MM
- Maramureș County
exact_mappings:
- dpv_loc:RO-MM
- dpv_loc_owl:RO-MM
is_a: RO
class_uri: loc:RO-MM

```
</details>

### Induced

<details>
```yaml
name: ROMM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-MM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Maramureș County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-MM
- Maramureș County
exact_mappings:
- dpv_loc:RO-MM
- dpv_loc_owl:RO-MM
is_a: RO
class_uri: loc:RO-MM

```
</details></div>