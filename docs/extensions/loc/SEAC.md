---
search:
  boost: 10.0
---

# Class: SEAC 


_Concept representing region Västerbotten County in country Sweden_



<div data-search-exclude markdown="1">



URI: [loc:SE-AC](https://w3id.org/lmodel/dpv/loc/SE-AC)





```mermaid
 classDiagram
    class SEAC
    click SEAC href "../SEAC/"
      SE <|-- SEAC
        click SE href "../SE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SE](SE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SEAC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SE-AC](https://w3id.org/lmodel/dpv/loc/SE-AC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SE-AC
* Västerbotten County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SE-AC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SE-AC |
| native | loc:SEAC |
| exact | dpv_loc:SE-AC, dpv_loc_owl:SE-AC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SEAC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-AC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Västerbotten County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-AC
- Västerbotten County
exact_mappings:
- dpv_loc:SE-AC
- dpv_loc_owl:SE-AC
is_a: SE
class_uri: loc:SE-AC

```
</details>

### Induced

<details>
```yaml
name: SEAC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-AC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Västerbotten County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-AC
- Västerbotten County
exact_mappings:
- dpv_loc:SE-AC
- dpv_loc_owl:SE-AC
is_a: SE
class_uri: loc:SE-AC

```
</details></div>