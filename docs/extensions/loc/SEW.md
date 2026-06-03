---
search:
  boost: 10.0
---

# Class: SEW 


_Concept representing region Dalarna County in country Sweden_



<div data-search-exclude markdown="1">



URI: [loc:SE-W](https://w3id.org/lmodel/dpv/loc/SE-W)





```mermaid
 classDiagram
    class SEW
    click SEW href "../SEW/"
      SE <|-- SEW
        click SE href "../SE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SE](SE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SEW**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SE-W](https://w3id.org/lmodel/dpv/loc/SE-W) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SE-W
* Dalarna County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SE-W |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SE-W |
| native | loc:SEW |
| exact | dpv_loc:SE-W, dpv_loc_owl:SE-W |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SEW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-W
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Dalarna County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-W
- Dalarna County
exact_mappings:
- dpv_loc:SE-W
- dpv_loc_owl:SE-W
is_a: SE
class_uri: loc:SE-W

```
</details>

### Induced

<details>
```yaml
name: SEW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-W
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Dalarna County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-W
- Dalarna County
exact_mappings:
- dpv_loc:SE-W
- dpv_loc_owl:SE-W
is_a: SE
class_uri: loc:SE-W

```
</details></div>