---
search:
  boost: 10.0
---

# Class: BEWNA 


_Concept representing region Namur (province) in country Belgium_



<div data-search-exclude markdown="1">



URI: [loc:BE-WNA](https://w3id.org/lmodel/dpv/loc/BE-WNA)





```mermaid
 classDiagram
    class BEWNA
    click BEWNA href "../BEWNA/"
      BE <|-- BEWNA
        click BE href "../BE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [BE](BE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **BEWNA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:BE-WNA](https://w3id.org/lmodel/dpv/loc/BE-WNA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* BE-WNA
* Namur (province)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#BE-WNA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:BE-WNA |
| native | loc:BEWNA |
| exact | dpv_loc:BE-WNA, dpv_loc_owl:BE-WNA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BEWNA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BE-WNA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Namur (province) in country Belgium
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BE-WNA
- Namur (province)
exact_mappings:
- dpv_loc:BE-WNA
- dpv_loc_owl:BE-WNA
is_a: BE
class_uri: loc:BE-WNA

```
</details>

### Induced

<details>
```yaml
name: BEWNA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BE-WNA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Namur (province) in country Belgium
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BE-WNA
- Namur (province)
exact_mappings:
- dpv_loc:BE-WNA
- dpv_loc_owl:BE-WNA
is_a: BE
class_uri: loc:BE-WNA

```
</details></div>