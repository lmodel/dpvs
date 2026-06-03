---
search:
  boost: 10.0
---

# Class: SET 


_Concept representing region Örebro County in country Sweden_



<div data-search-exclude markdown="1">



URI: [loc:SE-T](https://w3id.org/lmodel/dpv/loc/SE-T)





```mermaid
 classDiagram
    class SET
    click SET href "../SET/"
      SE <|-- SET
        click SE href "../SE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SE](SE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SET**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SE-T](https://w3id.org/lmodel/dpv/loc/SE-T) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SE-T
* Örebro County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SE-T |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SE-T |
| native | loc:SET |
| exact | dpv_loc:SE-T, dpv_loc_owl:SE-T |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SET
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-T
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Örebro County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-T
- Örebro County
exact_mappings:
- dpv_loc:SE-T
- dpv_loc_owl:SE-T
is_a: SE
class_uri: loc:SE-T

```
</details>

### Induced

<details>
```yaml
name: SET
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-T
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Örebro County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-T
- Örebro County
exact_mappings:
- dpv_loc:SE-T
- dpv_loc_owl:SE-T
is_a: SE
class_uri: loc:SE-T

```
</details></div>