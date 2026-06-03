---
search:
  boost: 10.0
---

# Class: ROIS 


_Concept representing region Iași County in country Romania_



<div data-search-exclude markdown="1">



URI: [loc:RO-IS](https://w3id.org/lmodel/dpv/loc/RO-IS)





```mermaid
 classDiagram
    class ROIS
    click ROIS href "../ROIS/"
      RO <|-- ROIS
        click RO href "../RO/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [RO](RO.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ROIS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RO-IS](https://w3id.org/lmodel/dpv/loc/RO-IS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* RO-IS
* Iași County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RO-IS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RO-IS |
| native | loc:ROIS |
| exact | dpv_loc:RO-IS, dpv_loc_owl:RO-IS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ROIS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-IS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Iași County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-IS
- Iași County
exact_mappings:
- dpv_loc:RO-IS
- dpv_loc_owl:RO-IS
is_a: RO
class_uri: loc:RO-IS

```
</details>

### Induced

<details>
```yaml
name: ROIS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-IS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Iași County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-IS
- Iași County
exact_mappings:
- dpv_loc:RO-IS
- dpv_loc_owl:RO-IS
is_a: RO
class_uri: loc:RO-IS

```
</details></div>