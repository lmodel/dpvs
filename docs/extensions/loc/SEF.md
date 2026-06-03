---
search:
  boost: 10.0
---

# Class: SEF 


_Concept representing region Jönköping County in country Sweden_



<div data-search-exclude markdown="1">



URI: [loc:SE-F](https://w3id.org/lmodel/dpv/loc/SE-F)





```mermaid
 classDiagram
    class SEF
    click SEF href "../SEF/"
      SE <|-- SEF
        click SE href "../SE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SE](SE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SEF**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SE-F](https://w3id.org/lmodel/dpv/loc/SE-F) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SE-F
* Jönköping County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SE-F |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SE-F |
| native | loc:SEF |
| exact | dpv_loc:SE-F, dpv_loc_owl:SE-F |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SEF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-F
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Jönköping County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-F
- Jönköping County
exact_mappings:
- dpv_loc:SE-F
- dpv_loc_owl:SE-F
is_a: SE
class_uri: loc:SE-F

```
</details>

### Induced

<details>
```yaml
name: SEF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-F
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Jönköping County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-F
- Jönköping County
exact_mappings:
- dpv_loc:SE-F
- dpv_loc_owl:SE-F
is_a: SE
class_uri: loc:SE-F

```
</details></div>