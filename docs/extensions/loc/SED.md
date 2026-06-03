---
search:
  boost: 10.0
---

# Class: SED 


_Concept representing region Södermanland County in country Sweden_



<div data-search-exclude markdown="1">



URI: [loc:SE-D](https://w3id.org/lmodel/dpv/loc/SE-D)





```mermaid
 classDiagram
    class SED
    click SED href "../SED/"
      SE <|-- SED
        click SE href "../SE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SE](SE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SED**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SE-D](https://w3id.org/lmodel/dpv/loc/SE-D) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SE-D
* Södermanland County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SE-D |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SE-D |
| native | loc:SED |
| exact | dpv_loc:SE-D, dpv_loc_owl:SE-D |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SED
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-D
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Södermanland County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-D
- Södermanland County
exact_mappings:
- dpv_loc:SE-D
- dpv_loc_owl:SE-D
is_a: SE
class_uri: loc:SE-D

```
</details>

### Induced

<details>
```yaml
name: SED
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-D
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Södermanland County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-D
- Södermanland County
exact_mappings:
- dpv_loc:SE-D
- dpv_loc_owl:SE-D
is_a: SE
class_uri: loc:SE-D

```
</details></div>