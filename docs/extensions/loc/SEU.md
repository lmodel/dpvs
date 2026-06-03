---
search:
  boost: 10.0
---

# Class: SEU 


_Concept representing region Västmanland County in country Sweden_



<div data-search-exclude markdown="1">



URI: [loc:SE-U](https://w3id.org/lmodel/dpv/loc/SE-U)





```mermaid
 classDiagram
    class SEU
    click SEU href "../SEU/"
      SE <|-- SEU
        click SE href "../SE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SE](SE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SEU**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SE-U](https://w3id.org/lmodel/dpv/loc/SE-U) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SE-U
* Västmanland County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SE-U |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SE-U |
| native | loc:SEU |
| exact | dpv_loc:SE-U, dpv_loc_owl:SE-U |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SEU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-U
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Västmanland County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-U
- Västmanland County
exact_mappings:
- dpv_loc:SE-U
- dpv_loc_owl:SE-U
is_a: SE
class_uri: loc:SE-U

```
</details>

### Induced

<details>
```yaml
name: SEU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-U
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Västmanland County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-U
- Västmanland County
exact_mappings:
- dpv_loc:SE-U
- dpv_loc_owl:SE-U
is_a: SE
class_uri: loc:SE-U

```
</details></div>