---
search:
  boost: 10.0
---

# Class: BEVAN 


_Concept representing region Antwerp (province) in country Belgium_



<div data-search-exclude markdown="1">



URI: [loc:BE-VAN](https://w3id.org/lmodel/dpv/loc/BE-VAN)





```mermaid
 classDiagram
    class BEVAN
    click BEVAN href "../BEVAN/"
      BE <|-- BEVAN
        click BE href "../BE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [BE](BE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **BEVAN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:BE-VAN](https://w3id.org/lmodel/dpv/loc/BE-VAN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* BE-VAN
* Antwerp (province)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#BE-VAN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:BE-VAN |
| native | loc:BEVAN |
| exact | dpv_loc:BE-VAN, dpv_loc_owl:BE-VAN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BEVAN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BE-VAN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Antwerp (province) in country Belgium
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BE-VAN
- Antwerp (province)
exact_mappings:
- dpv_loc:BE-VAN
- dpv_loc_owl:BE-VAN
is_a: BE
class_uri: loc:BE-VAN

```
</details>

### Induced

<details>
```yaml
name: BEVAN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BE-VAN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Antwerp (province) in country Belgium
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BE-VAN
- Antwerp (province)
exact_mappings:
- dpv_loc:BE-VAN
- dpv_loc_owl:BE-VAN
is_a: BE
class_uri: loc:BE-VAN

```
</details></div>